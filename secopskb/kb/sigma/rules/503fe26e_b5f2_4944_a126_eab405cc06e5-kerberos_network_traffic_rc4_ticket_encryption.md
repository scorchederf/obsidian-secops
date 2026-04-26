---
sigma_id: "503fe26e-b5f2-4944-a126-eab405cc06e5"
title: "Kerberos Network Traffic RC4 Ticket Encryption"
framework: "sigma"
generated: "true"
source_path: "rules/network/zeek/zeek_susp_kerberos_rc4.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_susp_kerberos_rc4.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "zeek / kerberos"
aliases:
  - "503fe26e-b5f2-4944-a126-eab405cc06e5"
  - "Kerberos Network Traffic RC4 Ticket Encryption"
attack_technique_ids:
  - "T1558.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Kerberos Network Traffic RC4 Ticket Encryption

Detects kerberos TGS request using RC4 encryption which may be indicative of kerberoasting

## Metadata

- Rule ID: 503fe26e-b5f2-4944-a126-eab405cc06e5
- Status: test
- Level: medium
- Author: sigma
- Date: 2020-02-12
- Modified: 2021-11-27
- Source Path: rules/network/zeek/zeek_susp_kerberos_rc4.yml

## Logsource

- product: zeek
- service: kerberos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1558-steal_or_forge_kerberos_tickets|T1558.003]]

## Detection

```yaml
selection:
  request_type: TGS
  cipher: rc4-hmac
computer_acct:
  service|startswith: $
condition: selection and not computer_acct
```

## False Positives

- Normal enterprise SPN requests activity

## References

- https://adsecurity.org/?p=3458

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_susp_kerberos_rc4.yml)
