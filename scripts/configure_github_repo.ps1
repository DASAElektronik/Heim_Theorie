param(
    [string]$Repository = "DASAElektronik/Heim_Theorie",
    [string]$DefaultBranch = "main"
)

$ErrorActionPreference = "Stop"

$GhPath = (Get-Command gh -ErrorAction SilentlyContinue).Source
if (-not $GhPath) {
    $fallbackGhPath = "C:\Program Files\GitHub CLI\gh.exe"
    if (Test-Path -LiteralPath $fallbackGhPath) {
        $GhPath = $fallbackGhPath
    }
}

if (-not $GhPath) {
    throw "GitHub CLI 'gh' is not installed. Install it first, then run 'gh auth login'."
}

function Invoke-GhApiJson {
    param(
        [Parameter(Mandatory = $true)][string[]]$Arguments,
        [Parameter(Mandatory = $false)][object]$Body
    )

    $tempFile = $null
    try {
        if ($null -ne $Body) {
            $tempFile = New-TemporaryFile
            $Body | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $tempFile -Encoding UTF8
            & $GhPath api @Arguments --input $tempFile
        }
        else {
            & $GhPath api @Arguments
        }
    }
    finally {
        if ($tempFile -and (Test-Path -LiteralPath $tempFile)) {
            Remove-Item -LiteralPath $tempFile -Force
        }
    }
}

function Invoke-GhOptional {
    param(
        [Parameter(Mandatory = $true)][scriptblock]$Script,
        [Parameter(Mandatory = $true)][string]$Label
    )

    try {
        & $Script
        Write-Host "[ok] $Label"
    }
    catch {
        Write-Warning "[skipped/failed] $Label :: $($_.Exception.Message)"
    }
}

& $GhPath auth status

$description = "Source-checked reconstruction and audit workspace for Heim theory formulas"
$topics = @(
    "heim-theory",
    "formula-reconstruction",
    "physics-audit",
    "source-checking",
    "scientific-computing"
)

Write-Host "Configuring repository metadata and merge settings for $Repository"

$repoSettings = @{
    description = $description
    has_issues = $true
    has_projects = $false
    has_wiki = $false
    allow_squash_merge = $true
    allow_merge_commit = $false
    allow_rebase_merge = $false
    delete_branch_on_merge = $true
    allow_auto_merge = $false
    allow_update_branch = $true
    squash_merge_commit_title = "PR_TITLE"
    squash_merge_commit_message = "COMMIT_MESSAGES"
}

Invoke-GhApiJson -Arguments @("-X", "PATCH", "repos/$Repository") -Body $repoSettings | Out-Null
Write-Host "[ok] repository settings"

Invoke-GhApiJson -Arguments @(
    "-X", "PUT",
    "-H", "Accept: application/vnd.github+json",
    "repos/$Repository/topics"
) -Body @{ names = $topics } | Out-Null
Write-Host "[ok] repository topics"

$labels = @(
    @{ name = "source-check"; color = "1f883d"; description = "Source image or OCR verification" },
    @{ name = "normalization"; color = "0969da"; description = "Formula normalization before implementation" },
    @{ name = "implementation"; color = "5319e7"; description = "Code implementation work" },
    @{ name = "validation"; color = "d1242f"; description = "Numerical or scientific validation" },
    @{ name = "high-risk"; color = "fbca04"; description = "Fragile source, notation, or interpretation risk" },
    @{ name = "third-party-source"; color = "6e7781"; description = "Third-party source/provenance handling" },
    @{ name = "documentation"; color = "0075ca"; description = "Documentation work" },
    @{ name = "data-provenance"; color = "b60205"; description = "Reference data and provenance tracking" }
)

foreach ($label in $labels) {
    Invoke-GhOptional -Label "label $($label.name)" -Script {
        try {
            Invoke-GhApiJson -Arguments @("-X", "POST", "repos/$Repository/labels") -Body $label | Out-Null
        }
        catch {
            Invoke-GhApiJson -Arguments @("-X", "PATCH", "repos/$Repository/labels/$([uri]::EscapeDataString($label.name))") -Body @{
                new_name = $label.name
                color = $label.color
                description = $label.description
            } | Out-Null
        }
    }
}

Write-Host "Configuring branch protection for $DefaultBranch"

$branchProtection = @{
    required_status_checks = $null
    enforce_admins = $false
    required_pull_request_reviews = @{
        required_approving_review_count = 1
        dismiss_stale_reviews = $false
        require_code_owner_reviews = $false
        require_last_push_approval = $false
    }
    restrictions = $null
    required_linear_history = $false
    allow_force_pushes = $false
    allow_deletions = $false
    block_creations = $false
    required_conversation_resolution = $false
    lock_branch = $false
    allow_fork_syncing = $true
}

Invoke-GhApiJson -Arguments @(
    "-X", "PUT",
    "-H", "Accept: application/vnd.github+json",
    "repos/$Repository/branches/$DefaultBranch/protection"
) -Body $branchProtection | Out-Null
Write-Host "[ok] branch protection"

Invoke-GhOptional -Label "Dependabot alerts" -Script {
    Invoke-GhApiJson -Arguments @("-X", "PUT", "repos/$Repository/vulnerability-alerts") | Out-Null
}

Invoke-GhOptional -Label "Dependabot security updates" -Script {
    Invoke-GhApiJson -Arguments @("-X", "PUT", "repos/$Repository/automated-security-fixes") | Out-Null
}

Invoke-GhOptional -Label "secret scanning and push protection" -Script {
    Invoke-GhApiJson -Arguments @("-X", "PATCH", "repos/$Repository") -Body @{
        security_and_analysis = @{
            secret_scanning = @{ status = "enabled" }
            secret_scanning_push_protection = @{ status = "enabled" }
        }
    } | Out-Null
}

Write-Host "Done."
