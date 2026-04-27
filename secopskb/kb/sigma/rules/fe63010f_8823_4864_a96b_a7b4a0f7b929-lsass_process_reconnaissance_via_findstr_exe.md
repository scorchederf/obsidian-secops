---
sigma_id: "fe63010f-8823-4864-a96b-a7b4a0f7b929"
title: "LSASS Process Reconnaissance Via Findstr.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_findstr_lsass.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_findstr_lsass.yml"
build_date: "2026-04-27 19:13:52"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "fe63010f-8823-4864-a96b-a7b4a0f7b929"
  - "LSASS Process Reconnaissance Via Findstr.EXE"
attack_technique_ids:
  - "T1552.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects findstring commands that include the keyword lsass, which indicates recon actviity for the LSASS process PID

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials#^t1552006-group-policy-preferences|T1552.006: Group Policy Preferences]]

## Detection

```yaml
selection_findstr_img:
- Image|endswith:
  - \find.exe
  - \findstr.exe
- OriginalFileName:
  - FIND.EXE
  - FINDSTR.EXE
selection_findstr_cli:
  CommandLine|contains: lsass
selection_special:
  CommandLine|contains|windash:
  - ' /i "lsass'
  - ' /i lsass.exe'
  - findstr "lsass
  - findstr lsass
  - findstr.exe "lsass
  - findstr.exe lsass
condition: all of selection_findstr_* or selection_special
```

## False Positives

- Unknown

## References

- https://blog.talosintelligence.com/2022/08/recent-cyber-attack.html?m=1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_findstr_lsass.yml)
