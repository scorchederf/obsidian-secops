---
sigma_id: "fa1a7e52-3d02-435b-81b8-00da14dd66c1"
title: "Diskshadow Script Mode - Execution From Potential Suspicious Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_diskshadow_script_mode_susp_location.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_diskshadow_script_mode_susp_location.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "fa1a7e52-3d02-435b-81b8-00da14dd66c1"
  - "Diskshadow Script Mode - Execution From Potential Suspicious Location"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Diskshadow Script Mode - Execution From Potential Suspicious Location

Detects execution of "Diskshadow.exe" in script mode using the "/s" flag where the script is located in a potentially suspicious location.

## Metadata

- Rule ID: fa1a7e52-3d02-435b-81b8-00da14dd66c1
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-09-15
- Modified: 2024-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_diskshadow_script_mode_susp_location.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- OriginalFileName: diskshadow.exe
- Image|endswith: \diskshadow.exe
selection_cli:
  CommandLine|contains|windash: '-s '
selection_paths:
  CommandLine|contains:
  - :\Temp\
  - :\Windows\Temp\
  - \AppData\Local\
  - \AppData\Roaming\
  - \ProgramData\
  - \Users\Public\
condition: all of selection_*
```

## False Positives

- False positives may occur if you execute the script from one of the paths mentioned in the rule. Apply additional filters that fits your org needs.

## References

- https://bohops.com/2018/03/26/diskshadow-the-return-of-vss-evasion-persistence-and-active-directory-database-extraction/
- https://www.ired.team/offensive-security/credential-access-and-credential-dumping/ntds.dit-enumeration
- https://medium.com/@cyberjyot/lolbin-execution-via-diskshadow-f6ff681a27a4
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/diskshadow
- https://www.lifars.com/wp-content/uploads/2022/01/GriefRansomware_Whitepaper-2.pdf
- https://www.zscaler.com/blogs/security-research/technical-analysis-crytox-ransomware
- https://research.checkpoint.com/2022/evilplayout-attack-against-irans-state-broadcaster/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_diskshadow_script_mode_susp_location.yml)
