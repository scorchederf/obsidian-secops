---
sigma_id: "195626f3-5f1b-4403-93b7-e6cfd4d6a078"
title: "Suspicious SSL Connection"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_ssl_keyword.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_ssl_keyword.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "low"
logsource: "windows / ps_script"
aliases:
  - "195626f3-5f1b-4403-93b7-e6cfd4d6a078"
  - "Suspicious SSL Connection"
attack_technique_ids:
  - "T1573"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious SSL Connection

Adversaries may employ a known encryption algorithm to conceal command and control traffic rather than relying on any inherent protections provided by a communication protocol.

## Metadata

- Rule ID: 195626f3-5f1b-4403-93b7-e6cfd4d6a078
- Status: test
- Level: low
- Author: frack113
- Date: 2022-01-23
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_ssl_keyword.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1573-encrypted_channel|T1573]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - System.Net.Security.SslStream
  - Net.Security.RemoteCertificateValidationCallback
  - .AuthenticateAsClient
condition: selection
```

## False Positives

- Legitimate administrative script

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1573/T1573.md#atomic-test-1---openssl-c2
- https://medium.com/walmartglobaltech/openssl-server-reverse-shell-from-windows-client-aee2dbfa0926

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_ssl_keyword.yml)
