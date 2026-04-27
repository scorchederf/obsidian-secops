---
sigma_id: "c420410f-c2d8-4010-856b-dffe21866437"
title: "Enable LM Hash Storage"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_system_lsa_nolmhash.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_system_lsa_nolmhash.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "c420410f-c2d8-4010-856b-dffe21866437"
  - "Enable LM Hash Storage"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects changes to the "NoLMHash" registry value in order to allow Windows to store LM Hashes.
By setting this registry value to "0" (DWORD), Windows will be allowed to store a LAN manager hash of your password in Active Directory and local SAM databases.

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112: Modify Registry]]

## Detection

```yaml
selection:
  TargetObject|endswith: System\CurrentControlSet\Control\Lsa\NoLMHash
  Details: DWORD (0x00000000)
condition: selection
```

## False Positives

- Unknown

## References

- https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-347a
- https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/prevent-windows-store-lm-hash-password
- https://www.sans.org/blog/protecting-privileged-domain-accounts-lm-hashes-the-good-the-bad-and-the-ugly/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_system_lsa_nolmhash.yml)
