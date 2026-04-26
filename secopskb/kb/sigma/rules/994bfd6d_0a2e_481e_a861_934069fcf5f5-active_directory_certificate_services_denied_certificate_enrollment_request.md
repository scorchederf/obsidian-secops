---
sigma_id: "994bfd6d-0a2e-481e-a861-934069fcf5f5"
title: "Active Directory Certificate Services Denied Certificate Enrollment Request"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/microsoft_windows_certification_authority/win_system_adcs_enrollment_request_denied.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/microsoft_windows_certification_authority/win_system_adcs_enrollment_request_denied.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "low"
logsource: "windows / system"
aliases:
  - "994bfd6d-0a2e-481e-a861-934069fcf5f5"
  - "Active Directory Certificate Services Denied Certificate Enrollment Request"
attack_technique_ids:
  - "T1553.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Active Directory Certificate Services Denied Certificate Enrollment Request

Detects denied requests by Active Directory Certificate Services.
Example of these requests denial include issues with permissions on the certificate template or invalid signatures.

## Metadata

- Rule ID: 994bfd6d-0a2e-481e-a861-934069fcf5f5
- Status: test
- Level: low
- Author: @SerkinValery
- Date: 2024-03-07
- Source Path: rules/windows/builtin/system/microsoft_windows_certification_authority/win_system_adcs_enrollment_request_denied.yml

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1553-subvert_trust_controls|T1553.004]]

## Detection

```yaml
selection:
  Provider_Name: Microsoft-Windows-CertificationAuthority
  EventID: 53
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd299871(v=ws.10)
- https://www.gradenegger.eu/en/details-of-the-event-with-id-53-of-the-source-microsoft-windows-certificationauthority/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/microsoft_windows_certification_authority/win_system_adcs_enrollment_request_denied.yml)
