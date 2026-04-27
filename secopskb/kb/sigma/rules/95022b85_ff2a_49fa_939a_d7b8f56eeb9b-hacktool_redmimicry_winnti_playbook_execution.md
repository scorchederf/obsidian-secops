---
sigma_id: "95022b85-ff2a-49fa-939a-d7b8f56eeb9b"
title: "HackTool - RedMimicry Winnti Playbook Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_redmimicry_winnti_playbook.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_redmimicry_winnti_playbook.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "95022b85-ff2a-49fa-939a-d7b8f56eeb9b"
  - "HackTool - RedMimicry Winnti Playbook Execution"
attack_technique_ids:
  - "T1106"
  - "T1059.003"
  - "T1218.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# HackTool - RedMimicry Winnti Playbook Execution

Detects actions caused by the RedMimicry Winnti playbook a automated breach emulations utility

## Metadata

- Rule ID: 95022b85-ff2a-49fa-939a-d7b8f56eeb9b
- Status: test
- Level: high
- Author: Alexander Rausch
- Date: 2020-06-24
- Modified: 2023-03-01
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_redmimicry_winnti_playbook.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1106-native_api|T1106]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.003]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Detection

```yaml
selection:
  Image|endswith:
  - \rundll32.exe
  - \cmd.exe
  CommandLine|contains:
  - gthread-3.6.dll
  - \Windows\Temp\tmp.bat
  - sigcmm-2.4.dll
condition: selection
```

## False Positives

- Unknown

## References

- https://redmimicry.com/posts/redmimicry-winnti/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_redmimicry_winnti_playbook.yml)
