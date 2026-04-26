---
sigma_id: "993c2665-e6ef-40e3-a62a-e1a97686af79"
title: "Certificate Use With No Strong Mapping"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/microsoft_windows_kerberos_key_distribution_center/win_system_kdcsvc_cert_use_no_strong_mapping.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/microsoft_windows_kerberos_key_distribution_center/win_system_kdcsvc_cert_use_no_strong_mapping.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "windows / system"
aliases:
  - "993c2665-e6ef-40e3-a62a-e1a97686af79"
  - "Certificate Use With No Strong Mapping"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Certificate Use With No Strong Mapping

Detects a user certificate that was valid but could not be mapped to a user in a strong way (such as via explicit mapping, key trust mapping, or a SID)
This could be a sign of exploitation of the elevation of privilege vulnerabilities (CVE-2022-34691, CVE-2022-26931, CVE-2022-26923) that can occur when the KDC allows certificate spoofing by not requiring a strong mapping.
Events where the AccountName and CN of the Subject do not match, or where the CN ends in a dollar sign indicating a machine, may indicate certificate spoofing.

## Metadata

- Rule ID: 993c2665-e6ef-40e3-a62a-e1a97686af79
- Status: test
- Level: medium
- Author: @br4dy5
- Date: 2023-10-09
- Modified: 2025-09-22
- Source Path: rules/windows/builtin/system/microsoft_windows_kerberos_key_distribution_center/win_system_kdcsvc_cert_use_no_strong_mapping.yml

## Logsource

- product: windows
- service: system

## Detection

```yaml
selection:
  Provider_Name:
  - Kerberos-Key-Distribution-Center
  - Microsoft-Windows-Kerberos-Key-Distribution-Center
  EventID:
  - 39
  - 41
condition: selection
```

## False Positives

- If prevalent in the environment, filter on events where the AccountName and CN of the Subject do not reference the same user
- If prevalent in the environment, filter on CNs that end in a dollar sign indicating it is a machine name

## References

- https://support.microsoft.com/en-us/topic/kb5014754-certificate-based-authentication-changes-on-windows-domain-controllers-ad2c23b0-15d8-4340-a468-4d4f3b188f16

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/microsoft_windows_kerberos_key_distribution_center/win_system_kdcsvc_cert_use_no_strong_mapping.yml)
