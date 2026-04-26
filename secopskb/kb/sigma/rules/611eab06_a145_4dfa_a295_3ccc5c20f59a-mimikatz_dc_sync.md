---
sigma_id: "611eab06-a145-4dfa-a295-3ccc5c20f59a"
title: "Mimikatz DC Sync"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_dcsync.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_dcsync.yml"
build_date: "2026-04-26 15:01:46"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "611eab06-a145-4dfa-a295-3ccc5c20f59a"
  - "Mimikatz DC Sync"
attack_technique_ids:
  - "T1003.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Mimikatz DC Sync

Detects Mimikatz DC sync security events

## Metadata

- Rule ID: 611eab06-a145-4dfa-a295-3ccc5c20f59a
- Status: test
- Level: high
- Author: Benjamin Delpy, Florian Roth (Nextron Systems), Scott Dermott, Sorina Ionescu
- Date: 2018-06-03
- Modified: 2022-04-26
- Source Path: rules/windows/builtin/security/win_security_dcsync.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.006]]

### Software Tags

- S0002

## Detection

```yaml
selection:
  EventID: 4662
  Properties|contains:
  - Replicating Directory Changes All
  - 1131f6ad-9c07-11d1-f79f-00c04fc2dcd2
  - 1131f6aa-9c07-11d1-f79f-00c04fc2dcd2
  - 9923a32a-3607-11d2-b9be-0000f87a36b2
  - 89e95b76-444d-4c62-991a-0facbeda640c
  AccessMask: '0x100'
filter1:
  SubjectDomainName: Window Manager
filter2:
  SubjectUserName|startswith:
  - NT AUT
  - MSOL_
filter3:
  SubjectUserName|endswith: $
condition: selection and not 1 of filter*
```

## False Positives

- Valid DC Sync that is not covered by the filters; please report
- Local Domain Admin account used for Azure AD Connect

## References

- https://twitter.com/gentilkiwi/status/1003236624925413376
- https://gist.github.com/gentilkiwi/dcc132457408cf11ad2061340dcb53c2
- https://blog.blacklanternsecurity.com/p/detecting-dcsync?s=r
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4662

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_dcsync.yml)
