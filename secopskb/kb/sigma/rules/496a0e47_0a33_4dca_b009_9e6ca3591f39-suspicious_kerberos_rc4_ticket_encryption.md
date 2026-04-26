---
sigma_id: "496a0e47-0a33-4dca-b009-9e6ca3591f39"
title: "Suspicious Kerberos RC4 Ticket Encryption"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_susp_rc4_kerberos.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_rc4_kerberos.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "496a0e47-0a33-4dca-b009-9e6ca3591f39"
  - "Suspicious Kerberos RC4 Ticket Encryption"
attack_technique_ids:
  - "T1558.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Kerberos RC4 Ticket Encryption

Detects service ticket requests using RC4 encryption type

## Metadata

- Rule ID: 496a0e47-0a33-4dca-b009-9e6ca3591f39
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2017-02-06
- Modified: 2022-06-19
- Source Path: rules/windows/builtin/security/win_security_susp_rc4_kerberos.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1558-steal_or_forge_kerberos_tickets|T1558.003]]

## Detection

```yaml
selection:
  EventID: 4769
  TicketOptions: '0x40810000'
  TicketEncryptionType: '0x17'
reduction:
  ServiceName|endswith: $
condition: selection and not reduction
```

## False Positives

- Service accounts used on legacy systems (e.g. NetApp)
- Windows Domains with DFL 2003 and legacy systems

## References

- https://adsecurity.org/?p=3458
- https://www.trimarcsecurity.com/single-post/TrimarcResearch/Detecting-Kerberoasting-Activity

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_rc4_kerberos.yml)
