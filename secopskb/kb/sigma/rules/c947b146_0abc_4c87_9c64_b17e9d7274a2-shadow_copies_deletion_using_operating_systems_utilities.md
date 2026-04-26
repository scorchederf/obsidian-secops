---
sigma_id: "c947b146-0abc-4c87-9c64-b17e9d7274a2"
title: "Shadow Copies Deletion Using Operating Systems Utilities"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_shadow_copies_deletion.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_shadow_copies_deletion.yml"
build_date: "2026-04-26 15:01:51"
status: "stable"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "c947b146-0abc-4c87-9c64-b17e9d7274a2"
  - "Shadow Copies Deletion Using Operating Systems Utilities"
attack_technique_ids:
  - "T1070"
  - "T1490"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Shadow Copies Deletion Using Operating Systems Utilities

Shadow Copies deletion using operating systems utilities

## Metadata

- Rule ID: c947b146-0abc-4c87-9c64-b17e9d7274a2
- Status: stable
- Level: high
- Author: Florian Roth (Nextron Systems), Michael Haag, Teymur Kheirkhabarov, Daniil Yugoslavskiy, oscd.community, Andreas Hunkeler (@Karneades)
- Date: 2019-10-22
- Modified: 2022-11-03
- Source Path: rules/windows/process_creation/proc_creation_win_susp_shadow_copies_deletion.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070]]
- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490]]

## Detection

```yaml
selection1_img:
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
  - \wmic.exe
  - \vssadmin.exe
  - \diskshadow.exe
- OriginalFileName:
  - PowerShell.EXE
  - pwsh.dll
  - wmic.exe
  - VSSADMIN.EXE
  - diskshadow.exe
selection1_cli:
  CommandLine|contains|all:
  - shadow
  - delete
selection2_img:
- Image|endswith: \wbadmin.exe
- OriginalFileName: WBADMIN.EXE
selection2_cli:
  CommandLine|contains|all:
  - delete
  - catalog
  - quiet
selection3_img:
- Image|endswith: \vssadmin.exe
- OriginalFileName: VSSADMIN.EXE
selection3_cli:
  CommandLine|contains|all:
  - resize
  - shadowstorage
  CommandLine|contains:
  - unbounded
  - /MaxSize=
condition: (all of selection1*) or (all of selection2*) or (all of selection3*)
```

## False Positives

- Legitimate Administrator deletes Shadow Copies using operating systems utilities for legitimate reason
- LANDesk LDClient Ivanti-PSModule (PS EncodedCommand)

## References

- https://www.slideshare.net/heirhabarov/hunting-for-credentials-dumping-in-windows-environment
- https://blog.talosintelligence.com/2017/05/wannacry.html
- https://securingtomorrow.mcafee.com/other-blogs/mcafee-labs/new-teslacrypt-ransomware-arrives-via-spam/
- https://www.bleepingcomputer.com/news/security/why-everyone-should-disable-vssadmin-exe-now/
- https://www.hybrid-analysis.com/sample/ed01ebfbc9eb5bbea545af4d01bf5f1071661840480439c6e5babe8e080e41aa?environmentId=100
- https://github.com/Neo23x0/Raccine#the-process
- https://github.com/Neo23x0/Raccine/blob/20a569fa21625086433dcce8bb2765d0ea08dcb6/yara/gen_ransomware_command_lines.yar
- https://redcanary.com/blog/intelligence-insights-october-2021/
- https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/blackbyte-exbyte-ransomware

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_shadow_copies_deletion.yml)
