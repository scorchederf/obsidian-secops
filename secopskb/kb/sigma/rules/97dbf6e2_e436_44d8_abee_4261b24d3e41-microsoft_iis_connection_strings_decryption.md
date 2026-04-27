---
sigma_id: "97dbf6e2-e436-44d8-abee-4261b24d3e41"
title: "Microsoft IIS Connection Strings Decryption"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_iis_connection_strings_decryption.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_iis_connection_strings_decryption.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "97dbf6e2-e436-44d8-abee-4261b24d3e41"
  - "Microsoft IIS Connection Strings Decryption"
attack_technique_ids:
  - "T1003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects use of aspnet_regiis to decrypt Microsoft IIS connection strings. An attacker with Microsoft IIS web server access via a webshell or alike can decrypt and dump any hardcoded connection strings, such as the MSSQL service account password using aspnet_regiis command.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003: OS Credential Dumping]]

## Detection

```yaml
selection_name:
- Image|endswith: \aspnet_regiis.exe
- OriginalFileName: aspnet_regiis.exe
selection_args:
  CommandLine|contains|all:
  - connectionStrings
  - ' -pdf'
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://www.elastic.co/guide/en/security/current/microsoft-iis-connection-strings-decryption.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_iis_connection_strings_decryption.yml)
