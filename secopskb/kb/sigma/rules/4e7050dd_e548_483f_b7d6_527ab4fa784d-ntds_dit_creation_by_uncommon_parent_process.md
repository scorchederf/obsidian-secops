---
sigma_id: "4e7050dd-e548-483f-b7d6-527ab4fa784d"
title: "NTDS.DIT Creation By Uncommon Parent Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_ntds_dit_uncommon_parent_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_ntds_dit_uncommon_parent_process.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "4e7050dd-e548-483f-b7d6-527ab4fa784d"
  - "NTDS.DIT Creation By Uncommon Parent Process"
attack_technique_ids:
  - "T1003.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# NTDS.DIT Creation By Uncommon Parent Process

Detects creation of a file named "ntds.dit" (Active Directory Database) by an uncommon parent process or directory

## Metadata

- Rule ID: 4e7050dd-e548-483f-b7d6-527ab4fa784d
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-03-11
- Modified: 2023-01-05
- Source Path: rules/windows/file/file_event/file_event_win_ntds_dit_uncommon_parent_process.yml

## Logsource

- category: file_event
- definition: Requirements: The "ParentImage" field is not available by default on EID 11 of Sysmon logs. To be able to use this rule to the full extent you need to enrich the log with additional ParentImage data
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]

## Detection

```yaml
selection_file:
  TargetFilename|endswith: \ntds.dit
selection_process_parent:
  ParentImage|endswith:
  - \cscript.exe
  - \httpd.exe
  - \nginx.exe
  - \php-cgi.exe
  - \powershell.exe
  - \pwsh.exe
  - \w3wp.exe
  - \wscript.exe
selection_process_parent_path:
  ParentImage|contains:
  - \apache
  - \tomcat
  - \AppData\
  - \Temp\
  - \Public\
  - \PerfLogs\
condition: selection_file and 1 of selection_process_*
```

## False Positives

- Unknown

## References

- https://www.ired.team/offensive-security/credential-access-and-credential-dumping/ntds.dit-enumeration
- https://www.n00py.io/2022/03/manipulating-user-passwords-without-mimikatz/
- https://pentestlab.blog/tag/ntds-dit/
- https://github.com/samratashok/nishang/blob/414ee1104526d7057f9adaeee196d91ae447283e/Gather/Copy-VSS.ps1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_ntds_dit_uncommon_parent_process.yml)
