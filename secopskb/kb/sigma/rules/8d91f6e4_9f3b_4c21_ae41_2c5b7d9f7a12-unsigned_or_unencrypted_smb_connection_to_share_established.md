---
sigma_id: "8d91f6e4-9f3b-4c21-ae41-2c5b7d9f7a12"
title: "Unsigned or Unencrypted SMB Connection to Share Established"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/smbserver/connectivity/win_smbserver_connectivity_unsigned_and_unencrypted_share_connection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/smbserver/connectivity/win_smbserver_connectivity_unsigned_and_unencrypted_share_connection.yml"
build_date: "2026-04-26 14:14:38"
status: "experimental"
level: "medium"
logsource: "windows / smbserver-connectivity"
aliases:
  - "8d91f6e4-9f3b-4c21-ae41-2c5b7d9f7a12"
  - "Unsigned or Unencrypted SMB Connection to Share Established"
attack_technique_ids:
  - "T1021.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Unsigned or Unencrypted SMB Connection to Share Established

Detects SMB server connections to shares without signing or encryption enabled.
This could indicate potential lateral movement activity using unsecured SMB shares.

## Metadata

- Rule ID: 8d91f6e4-9f3b-4c21-ae41-2c5b7d9f7a12
- Status: experimental
- Level: medium
- Author: Mohamed Abdelghani
- Date: 2025-10-19
- Source Path: rules/windows/builtin/smbserver/connectivity/win_smbserver_connectivity_unsigned_and_unencrypted_share_connection.yml

## Logsource

- product: windows
- service: smbserver-connectivity

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.002]]

## Detection

```yaml
selection_shares:
  EventID: 4000
  ShareName|contains:
  - IPC$
  - ADMIN$
  - C$
selection_status:
- SigningUsed: 'false'
- EncyptionUsed: 'false'
filter_main_local_ips:
- ClientAddress|cidr:
  - 127.0.0.0/8
  - 169.254.0.0/16
  - ::1/128
  - fe80::/10
  - fc00::/7
- ClientAddress|contains:
  - '00000000000000000000000000000001'
  - FE80000000000000
  - FC00000000000000
  - 0200????7F
  - 0200????A9FE
condition: all of selection_* and not 1 of filter_main_*
```

## False Positives

- Connections from local or private IP addresses to SMB shares without signing or encryption enabled for older systems or misconfigured environments. Apply additional tuning as needed.

## References

- https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/overview-server-message-block-signing

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/smbserver/connectivity/win_smbserver_connectivity_unsigned_and_unencrypted_share_connection.yml)
