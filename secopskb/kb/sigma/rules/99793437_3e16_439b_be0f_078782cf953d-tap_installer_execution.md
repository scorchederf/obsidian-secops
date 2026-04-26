---
sigma_id: "99793437-3e16-439b-be0f-078782cf953d"
title: "Tap Installer Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_tapinstall_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_tapinstall_execution.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "99793437-3e16-439b-be0f-078782cf953d"
  - "Tap Installer Execution"
attack_technique_ids:
  - "T1048"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Tap Installer Execution

Well-known TAP software installation. Possible preparation for data exfiltration using tunneling techniques

## Metadata

- Rule ID: 99793437-3e16-439b-be0f-078782cf953d
- Status: test
- Level: medium
- Author: Daniil Yugoslavskiy, Ian Davis, oscd.community
- Date: 2019-10-24
- Modified: 2023-12-11
- Source Path: rules/windows/process_creation/proc_creation_win_tapinstall_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048]]

## Detection

```yaml
selection:
  Image|endswith: \tapinstall.exe
filter_optional_avast:
  Image|contains:
  - :\Program Files\Avast Software\SecureLine VPN\
  - :\Program Files (x86)\Avast Software\SecureLine VPN\
filter_optional_openvpn:
  Image|contains: :\Program Files\OpenVPN Connect\drivers\tap\
filter_optional_protonvpn:
  Image|contains: :\Program Files (x86)\Proton Technologies\ProtonVPNTap\installer\
condition: selection and not 1 of filter_optional_*
```

## False Positives

- Legitimate OpenVPN TAP installation

## References

- https://community.openvpn.net/openvpn/wiki/ManagingWindowsTAPDrivers

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_tapinstall_execution.yml)
