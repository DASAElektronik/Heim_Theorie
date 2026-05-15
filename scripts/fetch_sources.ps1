param(
    [string]$ManifestPath = "..\01_sources\download_manifest.csv",
    [string]$ProjectRoot = ".."
)

$ErrorActionPreference = "Stop"

$manifest = Import-Csv -LiteralPath $ManifestPath

foreach ($item in $manifest) {
    if ($item.status -ne "planned") {
        continue
    }

    $targetDir = Join-Path -Path $ProjectRoot -ChildPath $item.target_dir
    New-Item -ItemType Directory -Force -Path $targetDir | Out-Null

    $uri = [Uri]$item.url
    $fileName = [System.IO.Path]::GetFileName($uri.LocalPath)
    if ([string]::IsNullOrWhiteSpace($fileName)) {
        $safeId = $item.id.ToLowerInvariant()
        $fileName = "$safeId.html"
    }

    $targetPath = Join-Path -Path $targetDir -ChildPath $fileName

    Write-Host "Fetching $($item.id): $($item.title)"
    Invoke-WebRequest -Uri $item.url -OutFile $targetPath
}

