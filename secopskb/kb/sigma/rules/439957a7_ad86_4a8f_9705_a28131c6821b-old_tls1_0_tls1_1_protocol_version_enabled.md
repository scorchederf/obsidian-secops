---
sigma_id: "439957a7-ad86-4a8f-9705-a28131c6821b"
title: "Old TLS1.0/TLS1.1 Protocol Version Enabled"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_tls_protocol_old_version_enabled.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_tls_protocol_old_version_enabled.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "439957a7-ad86-4a8f-9705-a28131c6821b"
  - "Old TLS1.0/TLS1.1 Protocol Version Enabled"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Old TLS1.0/TLS1.1 Protocol Version Enabled

Detects applications or users re-enabling old TLS versions by setting the "Enabled" value to "1" for the "Protocols" registry key.

## Metadata

- Rule ID: 439957a7-ad86-4a8f-9705-a28131c6821b
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-09-05
- Source Path: rules/windows/registry/registry_set/registry_set_tls_protocol_old_version_enabled.yml

## Logsource

- category: registry_set
- product: windows

## Detection

```yaml
selection:
  TargetObject|contains:
  - \Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\
  - \Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\
  TargetObject|endswith: \Enabled
  Details: DWORD (0x00000001)
condition: selection
```

## False Positives

- Legitimate enabling of the old tls versions due to incompatibility

## References

- https://techcommunity.microsoft.com/t5/windows-it-pro-blog/tls-1-0-and-tls-1-1-soon-to-be-disabled-in-windows/ba-p/3887947

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_tls_protocol_old_version_enabled.yml)
