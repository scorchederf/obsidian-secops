---
sigma_id: "3f3f3506-1895-401b-9cc3-e86b16e630d0"
title: "Potential Direct Syscall of NtOpenProcess"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_access/proc_access_win_susp_direct_ntopenprocess_call.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_susp_direct_ntopenprocess_call.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_access"
aliases:
  - "3f3f3506-1895-401b-9cc3-e86b16e630d0"
  - "Potential Direct Syscall of NtOpenProcess"
attack_technique_ids:
  - "T1106"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Direct Syscall of NtOpenProcess

Detects potential calls to NtOpenProcess directly from NTDLL.

## Metadata

- Rule ID: 3f3f3506-1895-401b-9cc3-e86b16e630d0
- Status: test
- Level: medium
- Author: Christian Burkard (Nextron Systems), Tim Shelton (FP)
- Date: 2021-07-28
- Modified: 2023-12-13
- Source Path: rules/windows/process_access/proc_access_win_susp_direct_ntopenprocess_call.yml

## Logsource

- category: process_access
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1106-native_api|T1106]]

## Detection

```yaml
selection:
  CallTrace|startswith: UNKNOWN
filter_main_vcredist:
  TargetImage|endswith: vcredist_x64.exe
  SourceImage|endswith: vcredist_x64.exe
filter_main_generic:
  SourceImage|contains:
  - :\Program Files (x86)\
  - :\Program Files\
  - :\Windows\System32\
  - :\Windows\SysWOW64\
  - :\Windows\WinSxS\
  TargetImage|contains:
  - :\Program Files (x86)\
  - :\Program Files\
  - :\Windows\System32\
  - :\Windows\SysWOW64\
  - :\Windows\WinSxS\
filter_main_kerneltrace_edge:
  Provider_Name: Microsoft-Windows-Kernel-Audit-API-Calls
filter_optional_vmware:
  TargetImage|endswith: :\Windows\system32\systeminfo.exe
  SourceImage|endswith: setup64.exe
filter_optional_cylance:
  SourceImage|endswith: :\Windows\Explorer.EXE
  TargetImage|endswith: :\Program Files\Cylance\Desktop\CylanceUI.exe
filter_optional_amazon:
  SourceImage|endswith: AmazonSSMAgentSetup.exe
  TargetImage|endswith: AmazonSSMAgentSetup.exe
filter_optional_vscode:
  SourceImage|endswith: \AppData\Local\Programs\Microsoft VS Code\Code.exe
  TargetImage|endswith: \AppData\Local\Programs\Microsoft VS Code\Code.exe
filter_optional_teams:
  TargetImage|endswith: \AppData\Local\Microsoft\Teams\current\Teams.exe
  SourceImage|endswith: \AppData\Local\Microsoft\Teams\current\Teams.exe
filter_optional_discord:
  TargetImage|contains: \AppData\Local\Discord\
  TargetImage|endswith: \Discord.exe
filter_optional_yammer:
  SourceImage|contains: \AppData\Local\yammerdesktop\app-
  SourceImage|endswith: \Yammer.exe
  TargetImage|contains: \AppData\Local\yammerdesktop\app-
  TargetImage|endswith: \Yammer.exe
  GrantedAccess: '0x1000'
filter_optional_evernote:
  TargetImage|endswith: \Evernote\Evernote.exe
filter_optional_adobe_acrobat:
  SourceImage|contains: :\Program Files\Adobe\Acrobat DC\Acrobat\
  SourceImage|endswith: \AcroCEF.exe
  TargetImage|contains: :\Program Files\Adobe\Acrobat DC\Acrobat\
  TargetImage|endswith: \AcroCEF.exe
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://medium.com/falconforce/falconfriday-direct-system-calls-and-cobalt-strike-bofs-0xff14-741fa8e1bdd6

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_susp_direct_ntopenprocess_call.yml)
