---
sigma_id: "d6a9b252-c666-4de6-8806-5561bbbd3bdc"
title: "Wdigest Enable UseLogonCredential"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_wdigest_enable_uselogoncredential.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_wdigest_enable_uselogoncredential.yml"
build_date: "2026-04-26 14:14:39"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "d6a9b252-c666-4de6-8806-5561bbbd3bdc"
  - "Wdigest Enable UseLogonCredential"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Wdigest Enable UseLogonCredential

Detects potential malicious modification of the property value of UseLogonCredential from HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest to enable clear-text credentials

## Metadata

- Rule ID: d6a9b252-c666-4de6-8806-5561bbbd3bdc
- Status: test
- Level: high
- Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
- Date: 2019-09-12
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_wdigest_enable_uselogoncredential.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
  TargetObject|endswith: WDigest\UseLogonCredential
  Details: DWORD (0x00000001)
condition: selection
```

## False Positives

- Unknown

## References

- https://threathunterplaybook.com/hunts/windows/190510-RegModWDigestDowngrade/notebook.html
- https://support.microsoft.com/en-us/topic/microsoft-security-advisory-update-to-improve-credentials-protection-and-management-may-13-2014-93434251-04ac-b7f3-52aa-9f951c14b649
- https://github.com/redcanaryco/atomic-red-team/blob/73fcfa1d4863f6a4e17f90e54401de6e30a312bb/atomics/T1112/T1112.md#atomic-test-3---modify-registry-to-store-logon-credentials

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_wdigest_enable_uselogoncredential.yml)
