---
sigma_id: "5588576c-5898-4fac-bcdd-7475a60e8f43"
title: "Suspicious DNS Query Indicating Kerberos Coercion via DNS Object SPN Spoofing - Network"
framework: "sigma"
generated: "true"
source_path: "rules/network/zeek/zeek_dns_kerberos_coercion_via_dns_object_spn_spoofing.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_dns_kerberos_coercion_via_dns_object_spn_spoofing.yml"
build_date: "2026-04-27 19:13:56"
status: "experimental"
level: "high"
logsource: "zeek / dns"
aliases:
  - "5588576c-5898-4fac-bcdd-7475a60e8f43"
  - "Suspicious DNS Query Indicating Kerberos Coercion via DNS Object SPN Spoofing - Network"
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

- product: zeek
- service: dns

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1557-adversary-in-the-middle#^t1557001-llmnr-nbt-ns-poisoning-and-smb-relay|T1557.001: LLMNR/NBT-NS Poisoning and SMB Relay]]
- [[kb/attack/techniques/T1187-forced_authentication|T1187: Forced Authentication]]

## Detection

```yaml
selection:
  query|contains|all:
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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_dns_kerberos_coercion_via_dns_object_spn_spoofing.yml)
