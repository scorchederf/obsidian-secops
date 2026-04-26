---
sigma_id: "472159c5-31b9-4f56-b794-b766faa8b0a7"
title: "Suspicious LSASS Access Via MalSecLogon"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_access/proc_access_win_lsass_seclogon_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_lsass_seclogon_access.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "high"
logsource: "windows / process_access"
aliases:
  - "472159c5-31b9-4f56-b794-b766faa8b0a7"
  - "Suspicious LSASS Access Via MalSecLogon"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious LSASS Access Via MalSecLogon

Detects suspicious access to LSASS handle via a call trace to "seclogon.dll" with a suspicious access right.

## Metadata

- Rule ID: 472159c5-31b9-4f56-b794-b766faa8b0a7
- Status: test
- Level: high
- Author: Samir Bousseaden (original elastic rule), Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-29
- Source Path: rules/windows/process_access/proc_access_win_lsass_seclogon_access.yml

## Logsource

- category: process_access
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection:
  TargetImage|endswith: \lsass.exe
  SourceImage|endswith: \svchost.exe
  GrantedAccess: '0x14c0'
  CallTrace|contains: seclogon.dll
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/SBousseaden/status/1541920424635912196
- https://github.com/elastic/detection-rules/blob/2bc1795f3d7bcc3946452eb4f07ae799a756d94e/rules/windows/credential_access_lsass_handle_via_malseclogon.toml
- https://splintercod3.blogspot.com/p/the-hidden-side-of-seclogon-part-3.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_lsass_seclogon_access.yml)
