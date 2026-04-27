---
sigma_id: "4368354e-1797-463c-bc39-a309effbe8d7"
title: "Powershell Add Name Resolution Policy Table Rule"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_add_dnsclient_rule.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_add_dnsclient_rule.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "4368354e-1797-463c-bc39-a309effbe8d7"
  - "Powershell Add Name Resolution Policy Table Rule"
attack_technique_ids:
  - "T1565"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects powershell scripts that adds a Name Resolution Policy Table (NRPT) rule for the specified namespace.
This will bypass the default DNS server and uses a specified server for answering the query.

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1565-data_manipulation|T1565: Data Manipulation]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - Add-DnsClientNrptRule
  - -Namesp
  - -NameSe
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/NathanMcNulty/status/1569497348841287681
- https://learn.microsoft.com/en-us/powershell/module/dnsclient/add-dnsclientnrptrule?view=windowsserver2022-ps

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_add_dnsclient_rule.yml)
