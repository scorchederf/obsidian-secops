---
sigma_id: "98b53e78-ebaf-46f8-be06-421aafd176d9"
title: "HackTool - winPEAS Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_winpeas.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_winpeas.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "98b53e78-ebaf-46f8-be06-421aafd176d9"
  - "HackTool - winPEAS Execution"
attack_technique_ids:
  - "T1082"
  - "T1087"
  - "T1046"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - winPEAS Execution

WinPEAS is a script that search for possible paths to escalate privileges on Windows hosts. The checks are explained on book.hacktricks.xyz

## Metadata

- Rule ID: 98b53e78-ebaf-46f8-be06-421aafd176d9
- Status: test
- Level: high
- Author: Georg Lauenstein (sure[secure])
- Date: 2022-09-19
- Modified: 2023-03-23
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_winpeas.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]
- [[kb/attack/techniques/T1087-account_discovery|T1087]]
- [[kb/attack/techniques/T1046-network_service_discovery|T1046]]

## Detection

```yaml
selection_img:
- OriginalFileName: winPEAS.exe
- Image|endswith:
  - \winPEASany_ofs.exe
  - \winPEASany.exe
  - \winPEASx64_ofs.exe
  - \winPEASx64.exe
  - \winPEASx86_ofs.exe
  - \winPEASx86.exe
selection_cli_option:
  CommandLine|contains:
  - ' applicationsinfo'
  - ' browserinfo'
  - ' eventsinfo'
  - ' fileanalysis'
  - ' filesinfo'
  - ' processinfo'
  - ' servicesinfo'
  - ' windowscreds'
selection_cli_dl:
  CommandLine|contains: https://github.com/carlospolop/PEASS-ng/releases/latest/download/
selection_cli_specific:
- ParentCommandLine|endswith: ' -linpeas'
- CommandLine|endswith: ' -linpeas'
condition: 1 of selection_*
```

## False Positives

- Unlikely

## References

- https://github.com/carlospolop/PEASS-ng
- https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_winpeas.yml)
