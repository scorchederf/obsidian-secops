---
sigma_id: "9f546b25-5f12-4c8d-8532-5893dcb1e4b8"
title: "Potentially Suspicious Child Process Of DiskShadow.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_diskshadow_child_process_susp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_diskshadow_child_process_susp.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "9f546b25-5f12-4c8d-8532-5893dcb1e4b8"
  - "Potentially Suspicious Child Process Of DiskShadow.EXE"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious Child Process Of DiskShadow.EXE

Detects potentially suspicious child processes of "Diskshadow.exe". This could be an attempt to bypass parent/child relationship detection or application whitelisting rules.

## Metadata

- Rule ID: 9f546b25-5f12-4c8d-8532-5893dcb1e4b8
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-09-15
- Source Path: rules/windows/process_creation/proc_creation_win_diskshadow_child_process_susp.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  ParentImage|endswith: \diskshadow.exe
  Image|endswith:
  - \certutil.exe
  - \cscript.exe
  - \mshta.exe
  - \powershell.exe
  - \pwsh.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \wscript.exe
condition: selection
```

## False Positives

- False postitve can occur in cases where admin scripts levreage the "exec" flag to execute applications

## References

- https://bohops.com/2018/03/26/diskshadow-the-return-of-vss-evasion-persistence-and-active-directory-database-extraction/
- https://www.ired.team/offensive-security/credential-access-and-credential-dumping/ntds.dit-enumeration
- https://medium.com/@cyberjyot/lolbin-execution-via-diskshadow-f6ff681a27a4
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/diskshadow
- https://www.lifars.com/wp-content/uploads/2022/01/GriefRansomware_Whitepaper-2.pdf
- https://www.zscaler.com/blogs/security-research/technical-analysis-crytox-ransomware
- https://research.checkpoint.com/2022/evilplayout-attack-against-irans-state-broadcaster/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_diskshadow_child_process_susp.yml)
