---
sigma_id: "d487ed4a-fd24-436d-a0b2-f4e95f7b2635"
title: "Suspicious ClickFix/FileFix Execution Pattern"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_clickfix_filefix_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_clickfix_filefix_execution.yml"
build_date: "2026-04-26 17:03:22"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "d487ed4a-fd24-436d-a0b2-f4e95f7b2635"
  - "Suspicious ClickFix/FileFix Execution Pattern"
attack_technique_ids:
  - "T1204.001"
  - "T1204.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious ClickFix/FileFix Execution Pattern

Detects suspicious execution patterns where users are tricked into running malicious commands via clipboard manipulation, either through the Windows Run dialog (ClickFix) or File Explorer address bar (FileFix).
Attackers leverage social engineering campaigns—such as fake CAPTCHA challenges or urgent alerts—encouraging victims to paste clipboard contents, often executing mshta.exe, powershell.exe, or similar commands to infect systems.

## Metadata

- Rule ID: d487ed4a-fd24-436d-a0b2-f4e95f7b2635
- Status: experimental
- Level: high
- Author: montysecurity, Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-11-19
- Source Path: rules/windows/process_creation/proc_creation_win_susp_clickfix_filefix_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution|T1204.001]]
- [[kb/attack/techniques/T1204-user_execution|T1204.004]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith: \explorer.exe
  CommandLine|contains: '#'
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
condition: all of selection_*
```

## False Positives

- Unlikely

## References

- https://github.com/JohnHammond/recaptcha-phish
- https://www.zscaler.com/blogs/security-research/deepseek-lure-using-captchas-spread-malware
- https://www.threatdown.com/blog/clipboard-hijacker-tries-to-install-a-trojan/
- https://app.any.run/tasks/5c16b4db-4b36-4039-a0ed-9b09abff8be2
- https://www.esentire.com/security-advisories/netsupport-rat-clickfix-distribution
- https://www.scpx.com.au/2025/11/16/decades-old-finger-protocol-abused-in-clickfix-malware-attacks/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_clickfix_filefix_execution.yml)
