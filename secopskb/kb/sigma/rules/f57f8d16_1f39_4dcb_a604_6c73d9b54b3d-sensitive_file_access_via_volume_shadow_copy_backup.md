---
sigma_id: "f57f8d16-1f39-4dcb-a604-6c73d9b54b3d"
title: "Sensitive File Access Via Volume Shadow Copy Backup"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_sensitive_file_access_shadowcopy.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_sensitive_file_access_shadowcopy.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f57f8d16-1f39-4dcb-a604-6c73d9b54b3d"
  - "Sensitive File Access Via Volume Shadow Copy Backup"
attack_technique_ids:
  - "T1490"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a command that accesses the VolumeShadowCopy in order to extract sensitive files such as the Security or SAM registry hives or the AD database (ntds.dit)

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490: Inhibit System Recovery]]

## Detection

```yaml
selection_1:
  CommandLine|contains: \\\\\?\\GLOBALROOT\\Device\\HarddiskVolumeShadowCopy
selection_2:
  CommandLine|contains:
  - \\NTDS.dit
  - \\SYSTEM
  - \\SECURITY
condition: all of selection_*
```

## False Positives

- Unlikely

## References

- https://twitter.com/vxunderground/status/1423336151860002816?s=20
- https://www.virustotal.com/gui/file/03e9b8c2e86d6db450e5eceec057d7e369ee2389b9daecaf06331a95410aa5f8/detection
- https://pentestlab.blog/2018/07/04/dumping-domain-password-hashes/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_sensitive_file_access_shadowcopy.yml)
