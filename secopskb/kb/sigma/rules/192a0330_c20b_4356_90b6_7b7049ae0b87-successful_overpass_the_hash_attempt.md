---
sigma_id: "192a0330-c20b-4356-90b6-7b7049ae0b87"
title: "Successful Overpass the Hash Attempt"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/account_management/win_security_overpass_the_hash.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_overpass_the_hash.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "192a0330-c20b-4356-90b6-7b7049ae0b87"
  - "Successful Overpass the Hash Attempt"
attack_technique_ids:
  - "T1550.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Successful Overpass the Hash Attempt

Detects successful logon with logon type 9 (NewCredentials) which matches the Overpass the Hash behavior of e.g Mimikatz's sekurlsa::pth module.

## Metadata

- Rule ID: 192a0330-c20b-4356-90b6-7b7049ae0b87
- Status: test
- Level: high
- Author: Roberto Rodriguez (source), Dominik Schaudel (rule)
- Date: 2018-02-12
- Modified: 2021-11-27
- Source Path: rules/windows/builtin/security/account_management/win_security_overpass_the_hash.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1550-use_alternate_authentication_material|T1550.002]]

### Software Tags

- S0002

## Detection

```yaml
selection:
  EventID: 4624
  LogonType: 9
  LogonProcessName: seclogo
  AuthenticationPackageName: Negotiate
condition: selection
```

## False Positives

- Runas command-line tool using /netonly parameter

## References

- https://web.archive.org/web/20220419045003/https://cyberwardog.blogspot.com/2017/04/chronicles-of-threat-hunter-hunting-for.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_overpass_the_hash.yml)
