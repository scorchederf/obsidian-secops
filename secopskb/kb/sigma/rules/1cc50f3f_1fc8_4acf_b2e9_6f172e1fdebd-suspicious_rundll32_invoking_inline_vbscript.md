---
sigma_id: "1cc50f3f-1fc8-4acf-b2e9-6f172e1fdebd"
title: "Suspicious Rundll32 Invoking Inline VBScript"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_inline_vbs.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_inline_vbs.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "1cc50f3f-1fc8-4acf-b2e9-6f172e1fdebd"
  - "Suspicious Rundll32 Invoking Inline VBScript"
attack_technique_ids:
  - "T1055"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Rundll32 Invoking Inline VBScript

Detects suspicious process related to rundll32 based on command line that invokes inline VBScript as seen being used by UNC2452

## Metadata

- Rule ID: 1cc50f3f-1fc8-4acf-b2e9-6f172e1fdebd
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2021-03-05
- Modified: 2022-10-09
- Source Path: rules/windows/process_creation/proc_creation_win_rundll32_inline_vbs.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection|T1055]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - rundll32.exe
  - Execute
  - RegRead
  - window.close
condition: selection
```

## False Positives

- Unknown

## References

- https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_inline_vbs.yml)
