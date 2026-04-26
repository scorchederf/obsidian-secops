---
sigma_id: "e20b5b14-ce93-4230-88af-981983ef6e74"
title: "QuickAssist Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_quickassist_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_quickassist_execution.yml"
build_date: "2026-04-26 14:14:34"
status: "experimental"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "e20b5b14-ce93-4230-88af-981983ef6e74"
  - "QuickAssist Execution"
attack_technique_ids:
  - "T1219.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# QuickAssist Execution

Detects the execution of Microsoft Quick Assist tool "QuickAssist.exe". This utility can be used by attackers to gain remote access.

## Metadata

- Rule ID: e20b5b14-ce93-4230-88af-981983ef6e74
- Status: experimental
- Level: low
- Author: Muhammad Faisal (@faisalusuf)
- Date: 2024-12-19
- Source Path: rules/windows/process_creation/proc_creation_win_quickassist_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools|T1219.002]]

## Detection

```yaml
selection:
  Image|endswith: \QuickAssist.exe
condition: selection
```

## False Positives

- Legitimate use of Quick Assist in the environment.

## References

- https://www.microsoft.com/en-us/security/blog/2024/05/15/threat-actors-misusing-quick-assist-in-social-engineering-attacks-leading-to-ransomware/
- https://www.linkedin.com/posts/kevin-beaumont-security_ive-been-assisting-a-few-orgs-hit-with-successful-activity-7268055739116445701-xxjZ/
- https://x.com/cyb3rops/status/1862406110365245506
- https://learn.microsoft.com/en-us/windows/client-management/client-tools/quick-assist

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_quickassist_execution.yml)
