---
sigma_id: "58c0bff0-40a0-46e8-b5e8-b734b84d2017"
title: "Certificate Exported From Local Certificate Store"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/certificate_services_client_lifecycle_system/win_certificateservicesclient_lifecycle_system_cert_exported.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/certificate_services_client_lifecycle_system/win_certificateservicesclient_lifecycle_system_cert_exported.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "windows / certificateservicesclient-lifecycle-system"
aliases:
  - "58c0bff0-40a0-46e8-b5e8-b734b84d2017"
  - "Certificate Exported From Local Certificate Store"
attack_technique_ids:
  - "T1649"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Certificate Exported From Local Certificate Store

Detects when an application exports a certificate (and potentially the private key as well) from the local Windows certificate store.

## Metadata

- Rule ID: 58c0bff0-40a0-46e8-b5e8-b734b84d2017
- Status: test
- Level: medium
- Author: Zach Mathis
- Date: 2023-05-13
- Source Path: rules/windows/builtin/certificate_services_client_lifecycle_system/win_certificateservicesclient_lifecycle_system_cert_exported.yml

## Logsource

- product: windows
- service: certificateservicesclient-lifecycle-system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1649-steal_or_forge_authentication_certificates|T1649]]

## Detection

```yaml
selection:
  EventID: 1007
condition: selection
```

## False Positives

- Legitimate application requesting certificate exports will trigger this. Apply additional filters as needed

## References

- https://www.splunk.com/en_us/blog/security/breaking-the-chain-defending-against-certificate-services-abuse.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/certificate_services_client_lifecycle_system/win_certificateservicesclient_lifecycle_system_cert_exported.yml)
