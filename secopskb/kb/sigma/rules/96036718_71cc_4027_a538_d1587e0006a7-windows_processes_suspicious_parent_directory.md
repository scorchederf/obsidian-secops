---
sigma_id: "96036718-71cc-4027-a538-d1587e0006a7"
title: "Windows Processes Suspicious Parent Directory"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_proc_wrong_parent.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_proc_wrong_parent.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "96036718-71cc-4027-a538-d1587e0006a7"
  - "Windows Processes Suspicious Parent Directory"
attack_technique_ids:
  - "T1036.003"
  - "T1036.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Processes Suspicious Parent Directory

Detect suspicious parent processes of well-known Windows processes

## Metadata

- Rule ID: 96036718-71cc-4027-a538-d1587e0006a7
- Status: test
- Level: low
- Author: vburov
- Date: 2019-02-23
- Modified: 2025-03-06
- Source Path: rules/windows/process_creation/proc_creation_win_susp_proc_wrong_parent.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036.003]]
- [[kb/attack/techniques/T1036-masquerading|T1036.005]]

## Detection

```yaml
selection:
  Image|endswith:
  - \svchost.exe
  - \taskhost.exe
  - \lsm.exe
  - \lsass.exe
  - \services.exe
  - \lsaiso.exe
  - \csrss.exe
  - \wininit.exe
  - \winlogon.exe
filter_sys:
- ParentImage|endswith:
  - \SavService.exe
  - \ngen.exe
- ParentImage|contains:
  - \System32\
  - \SysWOW64\
filter_msmpeng:
  ParentImage|contains:
  - \Windows Defender\
  - \Microsoft Security Client\
  ParentImage|endswith: \MsMpEng.exe
filter_null:
- ParentImage: null
- ParentImage:
  - ''
  - '-'
condition: selection and not 1 of filter_*
```

## False Positives

- Some security products seem to spawn these

## References

- https://web.archive.org/web/20180718061628/https://securitybytes.io/blue-team-fundamentals-part-two-windows-processes-759fe15965e2
- https://www.carbonblack.com/2014/06/10/screenshot-demo-hunt-evil-faster-than-ever-with-carbon-black/
- https://www.13cubed.com/downloads/windows_process_genealogy_v2.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_proc_wrong_parent.yml)
