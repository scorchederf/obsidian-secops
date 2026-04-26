---
sigma_id: "b5b29e4e-31fa-4fdf-b058-296e7a1aa0c2"
title: "Suspicious FileFix Execution Pattern"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_filefix_execution_pattern.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_filefix_execution_pattern.yml"
build_date: "2026-04-26 14:14:36"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "b5b29e4e-31fa-4fdf-b058-296e7a1aa0c2"
  - "Suspicious FileFix Execution Pattern"
attack_technique_ids:
  - "T1204.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious FileFix Execution Pattern

Detects suspicious FileFix execution patterns where users are tricked into running malicious commands through browser file upload dialog manipulation.
This attack typically begins when users visit malicious websites impersonating legitimate services or news platforms,
which may display fake CAPTCHA challenges or direct instructions to open file explorer and paste clipboard content.
The clipboard content usually contains commands that download and execute malware, such as information stealing tools.

## Metadata

- Rule ID: b5b29e4e-31fa-4fdf-b058-296e7a1aa0c2
- Status: experimental
- Level: high
- Author: 0xFustang, Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-11-24
- Source Path: rules/windows/process_creation/proc_creation_win_susp_filefix_execution_pattern.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution|T1204.004]]

## Detection

```yaml
selection_exec_parent:
  ParentImage|endswith:
  - \brave.exe
  - \chrome.exe
  - \firefox.exe
  - \msedge.exe
  CommandLine|contains: '#'
selection_cli_lolbin:
  CommandLine|contains:
  - '%comspec%'
  - bitsadmin
  - certutil
  - cmd
  - cscript
  - curl
  - finger
  - mshta
  - powershell
  - pwsh
  - regsvr32
  - rundll32
  - schtasks
  - wget
  - wscript
selection_cli_captcha:
  CommandLine|contains:
  - account
  - anti-bot
  - botcheck
  - captcha
  - challenge
  - confirmation
  - fraud
  - human
  - identification
  - identificator
  - identity
  - robot
  - validation
  - verification
  - verify
condition: selection_exec_parent and 1 of selection_cli_*
```

## False Positives

- Legitimate use of PowerShell or other utilities launched from browser extensions or automation tools

## References

- https://mrd0x.com/filefix-clickfix-alternative/
- https://expel.com/blog/cache-smuggling-when-a-picture-isnt-a-thousand-words/
- https://blog.checkpoint.com/research/filefix-the-new-social-engineering-attack-building-on-clickfix-tested-in-the-wild/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_filefix_execution_pattern.yml)
