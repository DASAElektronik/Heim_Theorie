"""Use the existing gh login and verified OpenSSL TLS for this repo's remote.

No credentials are read or printed by this script; gh is Git's credential
helper. Explicit argv preserves the empty helper reset across Windows shells.
This does not change filesystem permissions or persistent Git configuration.
"""

import argparse
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("check", "push"))
    args = parser.parse_args()
    branch = subprocess.check_output(
        ["git", "symbolic-ref", "--quiet", "--short", "HEAD"],
        cwd=ROOT, text=True,
    ).strip()
    if not branch or branch.startswith("-"):
        parser.error("A named local branch is required")
    command = [
        "git", "-c", "http.sslBackend=openssl",
        "-c", "credential.helper=",
        "-c", "credential.helper=!gh auth git-credential",
    ]
    if args.action == "check":
        command += ["ls-remote", "--exit-code", "origin", f"refs/heads/{branch}"]
    else:
        command += ["push", "--porcelain", "origin", f"HEAD:refs/heads/{branch}"]
    return subprocess.run(command, cwd=ROOT, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
