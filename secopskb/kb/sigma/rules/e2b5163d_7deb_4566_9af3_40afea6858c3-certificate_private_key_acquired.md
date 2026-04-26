---
sigma_id: "e2b5163d-7deb-4566-9af3-40afea6858c3"
title: "Certificate Private Key Acquired"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/capi2/win_capi2_acquire_certificate_private_key.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/capi2/win_capi2_acquire_certificate_private_key.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "windows / capi2"
aliases:
  - "e2b5163d-7deb-4566-9af3-40afea6858c3"
  - "Certificate Private Key Acquired"
attack_technique_ids:
  - "T1649"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Certificate Private Key Acquired

Detects when an application acquires a certificate private key

## Metadata

- Rule ID: e2b5163d-7deb-4566-9af3-40afea6858c3
- Status: test
- Level: medium
- Author: Zach Mathis
- Date: 2023-05-13
- Source Path: rules/windows/builtin/capi2/win_capi2_acquire_certificate_private_key.yml

## Logsource

- definition: Requirements: The CAPI2 Operational log needs to be enabled
- product: windows
- service: capi2

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1649-steal_or_forge_authentication_certificates|T1649]]

## Detection

```yaml
selection:
  EventID: 70
condition: selection
```

## False Positives

- Legitimate application requesting certificate exports will trigger this. Apply additional filters as needed

## References

- https://www.splunk.com/en_us/blog/security/breaking-the-chain-defending-against-certificate-services-abuse.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/capi2/win_capi2_acquire_certificate_private_key.yml)
