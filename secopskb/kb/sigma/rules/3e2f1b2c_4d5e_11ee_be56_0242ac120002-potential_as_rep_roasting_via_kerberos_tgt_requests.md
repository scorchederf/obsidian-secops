---
sigma_id: "3e2f1b2c-4d5e-11ee-be56-0242ac120002"
title: "Potential AS-REP Roasting via Kerberos TGT Requests"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_kerberos_asrep_roasting.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_kerberos_asrep_roasting.yml"
build_date: "2026-04-26 14:14:31"
status: "experimental"
level: "medium"
logsource: "windows / security"
aliases:
  - "3e2f1b2c-4d5e-11ee-be56-0242ac120002"
  - "Potential AS-REP Roasting via Kerberos TGT Requests"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential AS-REP Roasting via Kerberos TGT Requests

Detects suspicious Kerberos TGT requests with pre-authentication disabled (Pre-Authentication Type = 0) and Ticket Encryption Type (0x17) i.e, RC4-HMAC.
This may indicate an AS-REP Roasting attack, where attackers request AS-REP messages for accounts without pre-authentication and attempt to crack the encrypted ticket offline to recover user passwords.

## Metadata

- Rule ID: 3e2f1b2c-4d5e-11ee-be56-0242ac120002
- Status: experimental
- Level: medium
- Author: ANosir
- Date: 2025-05-22
- Modified: 2025-07-04
- Source Path: rules/windows/builtin/security/win_security_kerberos_asrep_roasting.yml

## Logsource

- product: windows
- service: security

## Detection

```yaml
selection:
  EventID: 4768
  TicketEncryptionType: '0x17'
  ServiceName: krbtgt
  PreAuthType: 0
condition: selection
```

## False Positives

- Legacy systems or applications that legitimately use RC4 encryption
- Misconfigured accounts with pre-authentication disabled

## References

- https://medium.com/system-weakness/detecting-as-rep-roasting-attacks-b5b3965f9714
- https://www.picussecurity.com/resource/blog/as-rep-roasting-attack-explained-mitre-attack-t1558.004

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_kerberos_asrep_roasting.yml)
