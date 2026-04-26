---
sigma_id: "9bd012ee-0dff-44d7-84a0-aa698cfd87a3"
title: "LSASS Memory Access by Tool With Dump Keyword In Name"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_access/proc_access_win_lsass_dump_keyword_image.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_lsass_dump_keyword_image.yml"
build_date: "2026-04-26 15:01:46"
status: "test"
level: "high"
logsource: "windows / process_access"
aliases:
  - "9bd012ee-0dff-44d7-84a0-aa698cfd87a3"
  - "LSASS Memory Access by Tool With Dump Keyword In Name"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# LSASS Memory Access by Tool With Dump Keyword In Name

Detects LSASS process access requests from a source process with the "dump" keyword in its image name.

## Metadata

- Rule ID: 9bd012ee-0dff-44d7-84a0-aa698cfd87a3
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-02-10
- Modified: 2023-11-29
- Source Path: rules/windows/process_access/proc_access_win_lsass_dump_keyword_image.yml

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
  SourceImage|contains: dump
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

- Rare programs that contain the word dump in their name and access lsass

## References

- https://twitter.com/_xpn_/status/1491557187168178176
- https://www.ired.team/offensive-security/credential-access-and-credential-dumping/dump-credentials-from-lsass-process-without-mimikatz

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_lsass_dump_keyword_image.yml)
