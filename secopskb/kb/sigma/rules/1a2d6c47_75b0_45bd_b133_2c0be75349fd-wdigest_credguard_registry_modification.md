---
sigma_id: "1a2d6c47-75b0-45bd-b133-2c0be75349fd"
title: "Wdigest CredGuard Registry Modification"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_disable_wdigest_credential_guard.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_disable_wdigest_credential_guard.yml"
build_date: "2026-04-26 14:14:39"
status: "test"
level: "high"
logsource: "windows / registry_event"
aliases:
  - "1a2d6c47-75b0-45bd-b133-2c0be75349fd"
  - "Wdigest CredGuard Registry Modification"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Wdigest CredGuard Registry Modification

Detects potential malicious modification of the property value of IsCredGuardEnabled from
HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest to disable Cred Guard on a system.
This is usually used with UseLogonCredential to manipulate the caching credentials.

## Metadata

- Rule ID: 1a2d6c47-75b0-45bd-b133-2c0be75349fd
- Status: test
- Level: high
- Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
- Date: 2019-08-25
- Modified: 2021-11-27
- Source Path: rules/windows/registry/registry_event/registry_event_disable_wdigest_credential_guard.yml

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
  TargetObject|endswith: \IsCredGuardEnabled
condition: selection
```

## False Positives

- Unknown

## References

- https://teamhydra.blog/2020/08/25/bypassing-credential-guard/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_disable_wdigest_credential_guard.yml)
