---
sigma_id: "98dedfdd-8333-49d4-9f23-d7018cccae53"
title: "Enable LM Hash Storage - ProcCreation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_nolmhash.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_nolmhash.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "98dedfdd-8333-49d4-9f23-d7018cccae53"
  - "Enable LM Hash Storage - ProcCreation"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Enable LM Hash Storage - ProcCreation

Detects changes to the "NoLMHash" registry value in order to allow Windows to store LM Hashes.
By setting this registry value to "0" (DWORD), Windows will be allowed to store a LAN manager hash of your password in Active Directory and local SAM databases.

## Metadata

- Rule ID: 98dedfdd-8333-49d4-9f23-d7018cccae53
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-12-15
- Modified: 2023-12-22
- Source Path: rules/windows/process_creation/proc_creation_win_reg_nolmhash.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - \System\CurrentControlSet\Control\Lsa
  - NoLMHash
  - ' 0'
condition: selection
```

## False Positives

- Unknown

## References

- https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-347a
- https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/prevent-windows-store-lm-hash-password
- https://www.sans.org/blog/protecting-privileged-domain-accounts-lm-hashes-the-good-the-bad-and-the-ugly/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_nolmhash.yml)
