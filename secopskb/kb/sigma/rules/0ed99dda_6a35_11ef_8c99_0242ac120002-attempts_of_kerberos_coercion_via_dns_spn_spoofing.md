---
sigma_id: "0ed99dda-6a35-11ef-8c99-0242ac120002"
title: "Attempts of Kerberos Coercion Via DNS SPN Spoofing"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_kerberos_coercion_via_dns_spn_spoofing.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_kerberos_coercion_via_dns_spn_spoofing.yml"
build_date: "2026-04-27 19:13:50"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "0ed99dda-6a35-11ef-8c99-0242ac120002"
  - "Attempts of Kerberos Coercion Via DNS SPN Spoofing"
attack_technique_ids:
  - "T1557.001"
  - "T1187"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the presence of "UWhRC....AAYBAAAA" pattern in command line.
The pattern "1UWhRCAAAAA..BAAAA" is a base64-encoded signature that corresponds to a marshaled CREDENTIAL_TARGET_INFORMATION structure.
Attackers can use this technique to coerce authentication from victim systems to attacker-controlled hosts.
It is one of the strong indicators of a Kerberos coercion attack, where adversaries manipulate DNS records
to spoof Service Principal Names (SPNs) and redirect authentication requests like in CVE-2025-33073.
If you see this pattern in the command line, it is likely an attempt to add spoofed Service Principal Names (SPNs) to DNS records,
or checking for the presence of such records through the `nslookup` command.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1557-adversary-in-the-middle#^t1557001-llmnr-nbt-ns-poisoning-and-smb-relay|T1557.001: LLMNR/NBT-NS Poisoning and SMB Relay]]
- [[kb/attack/techniques/T1187-forced_authentication|T1187: Forced Authentication]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_kerberos_coercion_via_dns_spn_spoofing.yml)
