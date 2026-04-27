---
sigma_id: "e7a21b5f-d8c4-4ae5-b8d9-93c5d3f28e1c"
title: "Suspicious DNS Query Indicating Kerberos Coercion via DNS Object SPN Spoofing"
framework: "sigma"
generated: "true"
source_path: "rules/windows/dns_query/dns_query_win_kerberos_coercion_via_dns_object_spoofing.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_kerberos_coercion_via_dns_object_spoofing.yml"
build_date: "2026-04-27 19:13:56"
status: "experimental"
level: "high"
logsource: "windows / dns_query"
aliases:
  - "e7a21b5f-d8c4-4ae5-b8d9-93c5d3f28e1c"
  - "Suspicious DNS Query Indicating Kerberos Coercion via DNS Object SPN Spoofing"
attack_technique_ids:
  - "T1557.001"
  - "T1187"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects DNS queries containing patterns associated with Kerberos coercion attacks via DNS object spoofing.
The pattern "1UWhRCAAAAA..BAAAA" is a base64-encoded signature that corresponds to a marshaled CREDENTIAL_TARGET_INFORMATION structure.
Attackers can use this technique to coerce authentication from victim systems to attacker-controlled hosts.
It is one of the strong indicators of a Kerberos coercion attack, where adversaries manipulate DNS records
to spoof Service Principal Names (SPNs) and redirect authentication requests like CVE-2025-33073.

## Logsource

- category: dns_query
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1557-adversary-in-the-middle#^t1557001-llmnr-nbt-ns-poisoning-and-smb-relay|T1557.001: LLMNR/NBT-NS Poisoning and SMB Relay]]
- [[kb/attack/techniques/T1187-forced_authentication|T1187: Forced Authentication]]

## Detection

```yaml
selection:
  QueryName|contains|all:
  - UWhRCA
  - BAAAA
condition: selection
```

## False Positives

- Unknown

## References

- https://www.synacktiv.com/publications/ntlm-reflection-is-dead-long-live-ntlm-reflection-an-in-depth-analysis-of-cve-2025
- https://googleprojectzero.blogspot.com/2021/10/using-kerberos-for-authentication-relay.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_kerberos_coercion_via_dns_object_spoofing.yml)
