---
sigma_id: "8bc64091-6875-4881-aaf9-7bd25b5dda08"
title: "Suspicious Process Patterns NTDS.DIT Exfil"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_ntds.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_ntds.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "8bc64091-6875-4881-aaf9-7bd25b5dda08"
  - "Suspicious Process Patterns NTDS.DIT Exfil"
attack_technique_ids:
  - "T1003.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious Process Patterns NTDS.DIT Exfil

Detects suspicious process patterns used in NTDS.DIT exfiltration

## Metadata

- Rule ID: 8bc64091-6875-4881-aaf9-7bd25b5dda08
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-03-11
- Modified: 2022-11-10
- Source Path: rules/windows/process_creation/proc_creation_win_susp_ntds.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]

## Detection

```yaml
selection_tool:
- Image|endswith:
  - \NTDSDump.exe
  - \NTDSDumpEx.exe
- CommandLine|contains|all:
  - ntds.dit
  - system.hiv
- CommandLine|contains: NTDSgrab.ps1
selection_oneliner_1:
  CommandLine|contains|all:
  - ac i ntds
  - create full
selection_onliner_2:
  CommandLine|contains|all:
  - '/c copy '
  - \windows\ntds\ntds.dit
selection_onliner_3:
  CommandLine|contains|all:
  - activate instance ntds
  - create full
selection_powershell:
  CommandLine|contains|all:
  - powershell
  - ntds.dit
set1_selection_ntds_dit:
  CommandLine|contains: ntds.dit
set1_selection_image_folder:
- ParentImage|contains:
  - \apache
  - \tomcat
  - \AppData\
  - \Temp\
  - \Public\
  - \PerfLogs\
- Image|contains:
  - \apache
  - \tomcat
  - \AppData\
  - \Temp\
  - \Public\
  - \PerfLogs\
condition: 1 of selection* or all of set1*
```

## False Positives

- Unknown

## References

- https://www.ired.team/offensive-security/credential-access-and-credential-dumping/ntds.dit-enumeration
- https://www.n00py.io/2022/03/manipulating-user-passwords-without-mimikatz/
- https://pentestlab.blog/tag/ntds-dit/
- https://github.com/samratashok/nishang/blob/414ee1104526d7057f9adaeee196d91ae447283e/Gather/Copy-VSS.ps1
- https://github.com/zcgonvh/NTDSDumpEx
- https://github.com/rapid7/metasploit-framework/blob/d297adcebb5c1df6fe30b12ca79b161deb71571c/data/post/powershell/NTDSgrab.ps1
- https://blog.talosintelligence.com/2022/08/recent-cyber-attack.html?m=1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_ntds.yml)
