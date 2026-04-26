---
atomic_guid: "95018438-454a-468c-a0fa-59c800149b59"
title: "Automated AD Recon (ADRecon)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1087.002"
attack_technique_name: "Account Discovery: Domain Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.002/T1087.002.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "95018438-454a-468c-a0fa-59c800149b59"
  - "Automated AD Recon (ADRecon)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Automated AD Recon (ADRecon)

ADRecon extracts and combines information about an AD environement into a report. Upon execution, an Excel file with all of the data will be generated and its
path will be displayed.

## Metadata

- Atomic GUID: 95018438-454a-468c-a0fa-59c800149b59
- Technique: T1087.002: Account Discovery: Domain Account
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1087.002/T1087.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1087-account_discovery|T1087.002]]

## Input Arguments

### adrecon_path

- description: Path of ADRecon.ps1 file
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\ADRecon.ps1

## Dependencies

ADRecon must exist on disk at specified location (#{adrecon_path})

### Prerequisite Check

```text
if (Test-Path "#{adrecon_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/sense-of-security/ADRecon/38e4abae3e26d0fa87281c1d0c65cabd4d3c6ebd/ADRecon.ps1" -OutFile "#{adrecon_path}"
```

## Executor

- name: powershell

### Command

```powershell
Invoke-Expression "#{adrecon_path}"
```

### Cleanup

```powershell
Get-ChildItem "PathToAtomicsFolder\..\ExternalPayloads" -Recurse -Force | Where{$_.Name -Match "^ADRecon-Report-"} | Remove-Item -Force -Recurse
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.002/T1087.002.yaml)
