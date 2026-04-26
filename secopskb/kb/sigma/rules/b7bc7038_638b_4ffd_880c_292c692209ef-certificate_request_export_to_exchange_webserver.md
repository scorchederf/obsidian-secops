---
sigma_id: "b7bc7038-638b-4ffd-880c-292c692209ef"
title: "Certificate Request Export to Exchange Webserver"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/msexchange/win_exchange_proxyshell_certificate_generation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/msexchange/win_exchange_proxyshell_certificate_generation.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "critical"
logsource: "windows / msexchange-management"
aliases:
  - "b7bc7038-638b-4ffd-880c-292c692209ef"
  - "Certificate Request Export to Exchange Webserver"
attack_technique_ids:
  - "T1505.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Certificate Request Export to Exchange Webserver

Detects a write of an Exchange CSR to an untypical directory or with aspx name suffix which can be used to place a webshell

## Metadata

- Rule ID: b7bc7038-638b-4ffd-880c-292c692209ef
- Status: test
- Level: critical
- Author: Max Altgelt (Nextron Systems)
- Date: 2021-08-23
- Modified: 2023-01-23
- Source Path: rules/windows/builtin/msexchange/win_exchange_proxyshell_certificate_generation.yml

## Logsource

- product: windows
- service: msexchange-management

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1505-server_software_component|T1505.003]]

## Detection

```yaml
keywords_export_command:
  '|all':
  - New-ExchangeCertificate
  - ' -GenerateRequest'
  - ' -BinaryEncoded'
  - ' -RequestFile'
keywords_export_params:
- \\\\localhost\\C$
- \\\\127.0.0.1\\C$
- C:\\inetpub
- .aspx
condition: keywords_export_command and keywords_export_params
```

## False Positives

- Unlikely

## References

- https://twitter.com/GossiTheDog/status/1429175908905127938

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/msexchange/win_exchange_proxyshell_certificate_generation.yml)
