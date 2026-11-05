#!/usr/bin/env bash
# Install the pinned gitleaks release, checksum-verified.
# Shared by check.yml (checks job) and pages.yml (deploy gate) so the two
# copies cannot drift. POSIX bash; uses sudo for /usr/local/bin.
set -euo pipefail
VERSION="8.30.1"
curl -fsSL --max-time 60 -o /tmp/gl.tar.gz \
  "https://github.com/gitleaks/gitleaks/releases/download/v${VERSION}/gitleaks_${VERSION}_linux_x64.tar.gz"
curl -fsSL --max-time 60 -o /tmp/checksums.txt \
  "https://github.com/gitleaks/gitleaks/releases/download/v${VERSION}/checksums.txt"
grep "gitleaks_${VERSION}_linux_x64.tar.gz" /tmp/checksums.txt | (cd /tmp && sha256sum -c -)
sudo tar -xzf /tmp/gl.tar.gz -C /usr/local/bin gitleaks
gitleaks version
