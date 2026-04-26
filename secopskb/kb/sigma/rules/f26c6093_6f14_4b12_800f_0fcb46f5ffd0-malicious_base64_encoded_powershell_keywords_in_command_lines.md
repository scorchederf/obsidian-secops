---
sigma_id: "f26c6093-6f14-4b12-800f-0fcb46f5ffd0"
title: "Malicious Base64 Encoded PowerShell Keywords in Command Lines"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_base64_hidden_flag.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_base64_hidden_flag.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f26c6093-6f14-4b12-800f-0fcb46f5ffd0"
  - "Malicious Base64 Encoded PowerShell Keywords in Command Lines"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Malicious Base64 Encoded PowerShell Keywords in Command Lines

Detects base64 encoded strings used in hidden malicious PowerShell command lines

## Metadata

- Rule ID: f26c6093-6f14-4b12-800f-0fcb46f5ffd0
- Status: test
- Level: high
- Author: John Lambert (rule)
- Date: 2019-01-16
- Modified: 2023-01-05
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_base64_hidden_flag.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
- OriginalFileName:
  - PowerShell.EXE
  - pwsh.dll
selection_hidden:
  CommandLine|contains: ' hidden '
selection_encoded:
  CommandLine|contains:
  - AGkAdABzAGEAZABtAGkAbgAgAC8AdAByAGEAbgBzAGYAZQByA
  - aXRzYWRtaW4gL3RyYW5zZmVy
  - IAaQB0AHMAYQBkAG0AaQBuACAALwB0AHIAYQBuAHMAZgBlAHIA
  - JpdHNhZG1pbiAvdHJhbnNmZX
  - YgBpAHQAcwBhAGQAbQBpAG4AIAAvAHQAcgBhAG4AcwBmAGUAcg
  - Yml0c2FkbWluIC90cmFuc2Zlc
  - AGMAaAB1AG4AawBfAHMAaQB6AGUA
  - JABjAGgAdQBuAGsAXwBzAGkAegBlA
  - JGNodW5rX3Npem
  - QAYwBoAHUAbgBrAF8AcwBpAHoAZQ
  - RjaHVua19zaXpl
  - Y2h1bmtfc2l6Z
  - AE8ALgBDAG8AbQBwAHIAZQBzAHMAaQBvAG4A
  - kATwAuAEMAbwBtAHAAcgBlAHMAcwBpAG8Abg
  - lPLkNvbXByZXNzaW9u
  - SQBPAC4AQwBvAG0AcAByAGUAcwBzAGkAbwBuA
  - SU8uQ29tcHJlc3Npb2
  - Ty5Db21wcmVzc2lvb
  - AE8ALgBNAGUAbQBvAHIAeQBTAHQAcgBlAGEAbQ
  - kATwAuAE0AZQBtAG8AcgB5AFMAdAByAGUAYQBtA
  - lPLk1lbW9yeVN0cmVhb
  - SQBPAC4ATQBlAG0AbwByAHkAUwB0AHIAZQBhAG0A
  - SU8uTWVtb3J5U3RyZWFt
  - Ty5NZW1vcnlTdHJlYW
  - 4ARwBlAHQAQwBoAHUAbgBrA
  - 5HZXRDaHVua
  - AEcAZQB0AEMAaAB1AG4Aaw
  - LgBHAGUAdABDAGgAdQBuAGsA
  - LkdldENodW5r
  - R2V0Q2h1bm
  - AEgAUgBFAEEARABfAEkATgBGAE8ANgA0A
  - QASABSAEUAQQBEAF8ASQBOAEYATwA2ADQA
  - RIUkVBRF9JTkZPNj
  - SFJFQURfSU5GTzY0
  - VABIAFIARQBBAEQAXwBJAE4ARgBPADYANA
  - VEhSRUFEX0lORk82N
  - AHIAZQBhAHQAZQBSAGUAbQBvAHQAZQBUAGgAcgBlAGEAZA
  - cmVhdGVSZW1vdGVUaHJlYW
  - MAcgBlAGEAdABlAFIAZQBtAG8AdABlAFQAaAByAGUAYQBkA
  - NyZWF0ZVJlbW90ZVRocmVhZ
  - Q3JlYXRlUmVtb3RlVGhyZWFk
  - QwByAGUAYQB0AGUAUgBlAG0AbwB0AGUAVABoAHIAZQBhAGQA
  - 0AZQBtAG0AbwB2AGUA
  - 1lbW1vdm
  - AGUAbQBtAG8AdgBlA
  - bQBlAG0AbQBvAHYAZQ
  - bWVtbW92Z
  - ZW1tb3Zl
condition: all of selection_*
```

## False Positives

- Unknown

## References

- http://www.leeholmes.com/blog/2017/09/21/searching-for-content-in-base-64-strings/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_base64_hidden_flag.yml)
