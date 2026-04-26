---
atomic_guid: "28ca4f81-fa96-47ff-8555-dde98017e89b"
title: "Python Startup Hook - atomic_hook.pth (macOS)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.018"
attack_technique_name: "Event Triggered Execution: Python Startup Hooks"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.018/T1546.018.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "28ca4f81-fa96-47ff-8555-dde98017e89b"
  - "Python Startup Hook - atomic_hook.pth (macOS)"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Python Startup Hook - atomic_hook.pth (macOS)

Creates a Python startup hook using a .pth file inside a virtual environment on macOS.

## Metadata

- Atomic GUID: 28ca4f81-fa96-47ff-8555-dde98017e89b
- Technique: T1546.018: Event Triggered Execution: Python Startup Hooks
- Platforms: macos
- Executor: sh
- Elevation Required: False
- Dependency Executor: sh
- Source Path: atomics/T1546.018/T1546.018.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.018]]

## Input Arguments

### exe_name

- description: App to launch
- type: string
- default: Calculator

### python_exe

- description: The python binary name to test
- type: string
- default: python3

## Dependencies

Python must be installed and the specified binary (#{python_exe}) must be in the PATH.

### Prerequisite Check

```text
PYTHON_CMD=$(command -v python || command -v #{python_exe})
if [ -z "$PYTHON_CMD" ]; then exit 1; fi
$PYTHON_CMD -m venv --help >/dev/null 2>&1
```

### Get Prerequisite

```text
echo "Python3 not found. Please install it using Homebrew ('brew install python' or 'brew install python3 or brew install python@3.X') or the macOS developer tools ('xcode-select --install')."
```

## Executor

- elevation_required: False
- name: sh

### Command

```sh
PYTHON_EXE=$(command -v #{python_exe} || command -v python)
TEMPDIR=$(mktemp -d /tmp/atomic_python_hook_XX)
echo "$TEMPDIR" > /tmp/atomic_python_hook_path.txt
$PYTHON_EXE -m venv "$TEMPDIR/env"
SITE_PACKAGES=$("$TEMPDIR/env/bin/#{python_exe}" -c "import site; print(site.getsitepackages()[0])")
echo "import subprocess; subprocess.Popen(['open', '-a', '#{exe_name}'])" > "$SITE_PACKAGES/atomic_hook.pth"
"$TEMPDIR/env/bin/python" -c "print('Triggering Hook via atomic_hook...')"
```

### Cleanup

```sh
if [ ! -f /tmp/atomic_python_hook_path.txt ] || [ ! -d $(cat /tmp/atomic_python_hook_path.txt) ]; then echo "[!] Artifact missing: /tmp/atomic_python_hook_path.txt — [-] Please Run : Invoke-AtomicTest T1546.018"; exit 0; fi
pkill "#{exe_name}" || true
[ -f /tmp/atomic_python_hook_path.txt ] && rm -rf $(cat /tmp/atomic_python_hook_path.txt) && rm -f /tmp/atomic_python_hook_path.txt
echo "[+] Successful Removed atomic_hook.pth and terminated #{exe_name}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.018/T1546.018.yaml)
