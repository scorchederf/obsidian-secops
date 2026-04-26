---
sigma_id: "5ef9853e-4d0e-4a70-846f-a9ca37d876da"
title: "Potential Credential Dumping Activity Via LSASS"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_access/proc_access_win_lsass_memdump.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_lsass_memdump.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / process_access"
aliases:
  - "5ef9853e-4d0e-4a70-846f-a9ca37d876da"
  - "Potential Credential Dumping Activity Via LSASS"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Credential Dumping Activity Via LSASS

Detects process access requests to the LSASS process with specific call trace calls and access masks.
This behaviour is expressed by many credential dumping tools such as Mimikatz, NanoDump, Invoke-Mimikatz, Procdump and even the Taskmgr dumping feature.

## Metadata

- Rule ID: 5ef9853e-4d0e-4a70-846f-a9ca37d876da
- Status: test
- Level: medium
- Author: Samir Bousseaden, Michael Haag
- Date: 2019-04-03
- Modified: 2024-03-02
- Source Path: rules/windows/process_access/proc_access_win_lsass_memdump.yml

## Logsource

- category: process_access
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

### Software Tags

- S0002

## Detection

```yaml
selection:
  TargetImage|endswith: \lsass.exe
  GrantedAccess|contains:
  - '0x1038'
  - '0x1438'
  - '0x143a'
  - '0x1fffff'
  CallTrace|contains:
  - dbgcore.dll
  - dbghelp.dll
  - kernel32.dll
  - kernelbase.dll
  - ntdll.dll
filter_main_system_user:
  SourceUser|contains:
  - AUTHORI
  - AUTORI
filter_optional_thor:
  CallTrace|contains|all:
  - :\Windows\Temp\asgard2-agent\
  - \thor\thor64.exe+
  - '|UNKNOWN('
  GrantedAccess: '0x103800'
filter_optional_sysmon:
  SourceImage|endswith: :\Windows\Sysmon64.exe
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://web.archive.org/web/20230329170326/https://blog.menasec.net/2019/02/threat-hunting-21-procdump-or-taskmgr.html
- https://web.archive.org/web/20230208123920/https://cyberwardog.blogspot.com/2017/03/chronicles-of-threat-hunter-hunting-for_22.html
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1003.001/T1003.001.md
- https://research.splunk.com/endpoint/windows_possible_credential_dumping/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_lsass_memdump.yml)
