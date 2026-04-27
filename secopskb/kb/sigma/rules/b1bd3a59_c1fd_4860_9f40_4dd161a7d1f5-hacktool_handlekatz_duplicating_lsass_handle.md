---
sigma_id: "b1bd3a59-c1fd-4860-9f40-4dd161a7d1f5"
title: "HackTool - HandleKatz Duplicating LSASS Handle"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_access/proc_access_win_hktl_handlekatz_lsass_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_hktl_handlekatz_lsass_access.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_access"
aliases:
  - "b1bd3a59-c1fd-4860-9f40-4dd161a7d1f5"
  - "HackTool - HandleKatz Duplicating LSASS Handle"
attack_technique_ids:
  - "T1106"
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# HackTool - HandleKatz Duplicating LSASS Handle

Detects HandleKatz opening LSASS to duplicate its handle to later dump the memory without opening any new handles

## Metadata

- Rule ID: b1bd3a59-c1fd-4860-9f40-4dd161a7d1f5
- Status: test
- Level: high
- Author: Bhabesh Raj (rule), @thefLinkk
- Date: 2022-06-27
- Modified: 2023-11-28
- Source Path: rules/windows/process_access/proc_access_win_hktl_handlekatz_lsass_access.yml

## Logsource

- category: process_access
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1106-native_api|T1106]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection:
  TargetImage|endswith: \lsass.exe
  GrantedAccess: '0x1440'
  CallTrace|startswith: C:\Windows\System32\ntdll.dll+
  CallTrace|contains: '|UNKNOWN('
  CallTrace|endswith: )
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/codewhitesec/HandleKatz

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_hktl_handlekatz_lsass_access.yml)
