---
sigma_id: "9c8afa4d-0022-48f0-9456-3712466f9701"
title: "Tap Driver Installation - Security"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_tap_driver_installation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_tap_driver_installation.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "low"
logsource: "windows / security"
aliases:
  - "9c8afa4d-0022-48f0-9456-3712466f9701"
  - "Tap Driver Installation - Security"
attack_technique_ids:
  - "T1048"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Tap Driver Installation - Security

Detects the installation of a well-known TAP driver service. This could be a sign of potential preparation for data exfiltration using tunnelling techniques.

## Metadata

- Rule ID: 9c8afa4d-0022-48f0-9456-3712466f9701
- Status: test
- Level: low
- Author: Daniil Yugoslavskiy, Ian Davis, oscd.community
- Date: 2019-10-24
- Modified: 2022-11-29
- Source Path: rules/windows/builtin/security/win_security_tap_driver_installation.yml

## Logsource

- definition: Requirements: The System Security Extension audit subcategory need to be enabled to log the EID 4697
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048]]

## Detection

```yaml
selection:
  EventID: 4697
  ServiceFileName|contains: tap0901
condition: selection
```

## False Positives

- Legitimate OpenVPN TAP installation

## References

- https://community.openvpn.net/openvpn/wiki/ManagingWindowsTAPDrivers

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_tap_driver_installation.yml)
