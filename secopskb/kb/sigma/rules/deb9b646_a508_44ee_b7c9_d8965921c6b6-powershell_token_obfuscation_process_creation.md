---
sigma_id: "deb9b646-a508-44ee-b7c9-d8965921c6b6"
title: "Powershell Token Obfuscation - Process Creation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_token_obfuscation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_token_obfuscation.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "deb9b646-a508-44ee-b7c9-d8965921c6b6"
  - "Powershell Token Obfuscation - Process Creation"
attack_technique_ids:
  - "T1027.009"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Powershell Token Obfuscation - Process Creation

Detects TOKEN OBFUSCATION technique from Invoke-Obfuscation

## Metadata

- Rule ID: deb9b646-a508-44ee-b7c9-d8965921c6b6
- Status: test
- Level: high
- Author: frack113
- Date: 2022-12-27
- Modified: 2024-08-11
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_token_obfuscation.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027.009]]

## Detection

```yaml
selection:
- CommandLine|re: \w+`(\w+|-|.)`[\w+|\s]
- CommandLine|re: '"(\{\d\})+"\s*-f'
- CommandLine|re: (?i)\$\{`?e`?n`?v`?:`?p`?a`?t`?h`?\}
filter_main_envpath:
  CommandLine|contains: ${env:path}
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://github.com/danielbohannon/Invoke-Obfuscation

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_token_obfuscation.yml)
