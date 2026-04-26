---
sigma_id: "4be8b654-0c01-4c9d-a10c-6b28467fc651"
title: "LSASS Access From Potentially White-Listed Processes"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_access/proc_access_win_lsass_whitelisted_process_names.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_lsass_whitelisted_process_names.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "high"
logsource: "windows / process_access"
aliases:
  - "4be8b654-0c01-4c9d-a10c-6b28467fc651"
  - "LSASS Access From Potentially White-Listed Processes"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# LSASS Access From Potentially White-Listed Processes

Detects a possible process memory dump that uses a white-listed filename like TrolleyExpress.exe as a way to dump the LSASS process memory without Microsoft Defender interference

## Metadata

- Rule ID: 4be8b654-0c01-4c9d-a10c-6b28467fc651
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-02-10
- Modified: 2023-11-29
- Source Path: rules/windows/process_access/proc_access_win_lsass_whitelisted_process_names.yml

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
  SourceImage|endswith:
  - \TrolleyExpress.exe
  - \ProcessDump.exe
  - \dump64.exe
  GrantedAccess|endswith:
  - '10'
  - '30'
  - '50'
  - '70'
  - '90'
  - B0
  - D0
  - F0
  - '18'
  - '38'
  - '58'
  - '78'
  - '98'
  - B8
  - D8
  - F8
  - 1A
  - 3A
  - 5A
  - 7A
  - 9A
  - BA
  - DA
  - FA
  - '0x14C2'
  - FF
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/_xpn_/status/1491557187168178176
- https://www.ired.team/offensive-security/credential-access-and-credential-dumping/dump-credentials-from-lsass-process-without-mimikatz
- https://twitter.com/mrd0x/status/1460597833917251595

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_lsass_whitelisted_process_names.yml)
