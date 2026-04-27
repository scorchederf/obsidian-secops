---
sigma_id: "72124974-a68b-4366-b990-d30e0b2a190d"
title: "Metasploit SMB Authentication"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_metasploit_authentication.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_metasploit_authentication.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "72124974-a68b-4366-b990-d30e0b2a190d"
  - "Metasploit SMB Authentication"
attack_technique_ids:
  - "T1021.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Metasploit SMB Authentication

Alerts on Metasploit host's authentications on the domain.

## Metadata

- Rule ID: 72124974-a68b-4366-b990-d30e0b2a190d
- Status: test
- Level: high
- Author: Chakib Gzenayi (@Chak092), Hosni Mribah
- Date: 2020-05-06
- Modified: 2024-01-25
- Source Path: rules/windows/builtin/security/win_security_metasploit_authentication.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.002]]

## Detection

```yaml
selection1:
  EventID:
  - 4625
  - 4624
  LogonType: 3
  AuthenticationPackageName: NTLM
  WorkstationName|re: ^[A-Za-z0-9]{16}$
selection2:
  EventID: 4776
  Workstation|re: ^[A-Za-z0-9]{16}$
condition: 1 of selection*
```

## False Positives

- Linux hostnames composed of 16 characters.

## References

- https://github.com/rapid7/metasploit-framework/blob/1416b5776d963f21b7b5b45d19f3e961201e0aed/lib/rex/proto/smb/client.rb

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_metasploit_authentication.yml)
