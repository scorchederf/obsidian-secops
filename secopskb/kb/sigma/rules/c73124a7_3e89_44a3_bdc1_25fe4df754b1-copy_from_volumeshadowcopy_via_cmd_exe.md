---
sigma_id: "c73124a7-3e89-44a3-bdc1-25fe4df754b1"
title: "Copy From VolumeShadowCopy Via Cmd.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmd_shadowcopy_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_shadowcopy_access.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "c73124a7-3e89-44a3-bdc1-25fe4df754b1"
  - "Copy From VolumeShadowCopy Via Cmd.EXE"
attack_technique_ids:
  - "T1490"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the execution of the builtin "copy" command that targets a shadow copy (sometimes used to copy registry hives that are in use)

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490: Inhibit System Recovery]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - 'copy '
  - \\\\\?\\GLOBALROOT\\Device\\HarddiskVolumeShadowCopy
condition: selection
```

## False Positives

- Backup scenarios using the commandline

## References

- https://twitter.com/vxunderground/status/1423336151860002816?s=20
- https://www.virustotal.com/gui/file/03e9b8c2e86d6db450e5eceec057d7e369ee2389b9daecaf06331a95410aa5f8/detection
- https://pentestlab.blog/2018/07/04/dumping-domain-password-hashes/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_shadowcopy_access.yml)
