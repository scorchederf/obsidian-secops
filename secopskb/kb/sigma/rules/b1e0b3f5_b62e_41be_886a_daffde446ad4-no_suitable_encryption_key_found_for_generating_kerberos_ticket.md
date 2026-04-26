---
sigma_id: "b1e0b3f5-b62e-41be-886a-daffde446ad4"
title: "No Suitable Encryption Key Found For Generating Kerberos Ticket"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/microsoft_windows_kerberos_key_distribution_center/win_system_kdcsvc_tgs_no_suitable_encryption_key_found.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/microsoft_windows_kerberos_key_distribution_center/win_system_kdcsvc_tgs_no_suitable_encryption_key_found.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "low"
logsource: "windows / system"
aliases:
  - "b1e0b3f5-b62e-41be-886a-daffde446ad4"
  - "No Suitable Encryption Key Found For Generating Kerberos Ticket"
attack_technique_ids:
  - "T1558.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# No Suitable Encryption Key Found For Generating Kerberos Ticket

Detects errors when a target server doesn't have suitable keys for generating kerberos tickets.
This issue can occur for example when a service uses a user account or a computer account that is configured for only DES encryption on a computer that is running Windows 7 which has DES encryption for Kerberos authentication disabled.

## Metadata

- Rule ID: b1e0b3f5-b62e-41be-886a-daffde446ad4
- Status: test
- Level: low
- Author: @SerkinValery
- Date: 2024-03-07
- Modified: 2025-09-22
- Source Path: rules/windows/builtin/system/microsoft_windows_kerberos_key_distribution_center/win_system_kdcsvc_tgs_no_suitable_encryption_key_found.yml

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1558-steal_or_forge_kerberos_tickets|T1558.003]]

## Detection

```yaml
selection:
  Provider_Name:
  - Kerberos-Key-Distribution-Center
  - Microsoft-Windows-Kerberos-Key-Distribution-Center
  EventID:
  - 16
  - 27
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/dd348773(v=ws.10)
- https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/kdc-event-16-27-des-encryption-disabled

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/microsoft_windows_kerberos_key_distribution_center/win_system_kdcsvc_tgs_no_suitable_encryption_key_found.yml)
