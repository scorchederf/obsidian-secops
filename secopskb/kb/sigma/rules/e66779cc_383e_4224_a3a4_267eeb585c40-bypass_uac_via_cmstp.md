---
sigma_id: "e66779cc-383e-4224-a3a4-267eeb585c40"
title: "Bypass UAC via CMSTP"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_uac_bypass_cmstp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_cmstp.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "e66779cc-383e-4224-a3a4-267eeb585c40"
  - "Bypass UAC via CMSTP"
attack_technique_ids:
  - "T1548.002"
  - "T1218.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detect commandline usage of Microsoft Connection Manager Profile Installer (cmstp.exe) to install specially formatted local .INF files

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218003-cmstp|T1218.003: CMSTP]]

## Detection

```yaml
selection_img:
- Image|endswith: \cmstp.exe
- OriginalFileName: CMSTP.EXE
selection_cli:
  CommandLine|contains:
  - /s
  - -s
  - /au
  - -au
  - /ni
  - -ni
condition: all of selection*
```

## False Positives

- Legitimate use of cmstp.exe utility by legitimate user

## References

- https://eqllib.readthedocs.io/en/latest/analytics/e584f1a1-c303-4885-8a66-21360c90995b.html
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1218.003/T1218.003.md
- https://lolbas-project.github.io/lolbas/Binaries/Cmstp/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_cmstp.yml)
