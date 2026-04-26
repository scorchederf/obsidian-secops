---
sigma_id: "1dde5376-a648-492e-9e54-4241dd9b0c7f"
title: "Diskshadow Script Mode - Uncommon Script Extension Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_diskshadow_script_mode_susp_ext.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_diskshadow_script_mode_susp_ext.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "1dde5376-a648-492e-9e54-4241dd9b0c7f"
  - "Diskshadow Script Mode - Uncommon Script Extension Execution"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Diskshadow Script Mode - Uncommon Script Extension Execution

Detects execution of "Diskshadow.exe" in script mode to execute an script with a potentially uncommon extension.
Initial baselining of the allowed extension list is required.

## Metadata

- Rule ID: 1dde5376-a648-492e-9e54-4241dd9b0c7f
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-09-15
- Modified: 2024-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_diskshadow_script_mode_susp_ext.yml

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
selection_flag:
  CommandLine|contains|windash: '-s '
filter_main_ext:
  CommandLine|contains: .txt
condition: all of selection_* and not 1 of filter_main_*
```

## False Positives

- False postitve might occur with legitimate or uncommon extensions used internally. Initial baseline is required.

## References

- https://bohops.com/2018/03/26/diskshadow-the-return-of-vss-evasion-persistence-and-active-directory-database-extraction/
- https://www.ired.team/offensive-security/credential-access-and-credential-dumping/ntds.dit-enumeration
- https://medium.com/@cyberjyot/lolbin-execution-via-diskshadow-f6ff681a27a4
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/diskshadow
- https://www.lifars.com/wp-content/uploads/2022/01/GriefRansomware_Whitepaper-2.pdf
- https://www.zscaler.com/blogs/security-research/technical-analysis-crytox-ransomware
- https://research.checkpoint.com/2022/evilplayout-attack-against-irans-state-broadcaster/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_diskshadow_script_mode_susp_ext.yml)
