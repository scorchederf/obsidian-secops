---
sigma_id: "fdb62a13-9a81-4e5c-a38f-ea93a16f6d7c"
title: "PowerShell Base64 Encoded FromBase64String Cmdlet"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_base64_frombase64string.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_base64_frombase64string.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "fdb62a13-9a81-4e5c-a38f-ea93a16f6d7c"
  - "PowerShell Base64 Encoded FromBase64String Cmdlet"
attack_technique_ids:
  - "T1140"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PowerShell Base64 Encoded FromBase64String Cmdlet

Detects usage of a base64 encoded "FromBase64String" cmdlet in a process command line

## Metadata

- Rule ID: fdb62a13-9a81-4e5c-a38f-ea93a16f6d7c
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2019-08-24
- Modified: 2023-04-06
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_base64_frombase64string.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1140-deobfuscate_decode_files_or_information|T1140]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
- CommandLine|base64offset|contains: ::FromBase64String
- CommandLine|contains:
  - OgA6AEYAcgBvAG0AQgBhAHMAZQA2ADQAUwB0AHIAaQBuAGcA
  - oAOgBGAHIAbwBtAEIAYQBzAGUANgA0AFMAdAByAGkAbgBnA
  - 6ADoARgByAG8AbQBCAGEAcwBlADYANABTAHQAcgBpAG4AZw
condition: selection
```

## False Positives

- Unknown

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_base64_frombase64string.yml)
