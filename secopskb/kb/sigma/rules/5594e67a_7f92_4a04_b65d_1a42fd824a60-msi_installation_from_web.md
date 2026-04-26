---
sigma_id: "5594e67a-7f92-4a04-b65d-1a42fd824a60"
title: "MSI Installation From Web"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/application/msiinstaller/win_msi_install_from_web.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/msiinstaller/win_msi_install_from_web.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "windows / application"
aliases:
  - "5594e67a-7f92-4a04-b65d-1a42fd824a60"
  - "MSI Installation From Web"
attack_technique_ids:
  - "T1218"
  - "T1218.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# MSI Installation From Web

Detects installation of a remote msi file from web.

## Metadata

- Rule ID: 5594e67a-7f92-4a04-b65d-1a42fd824a60
- Status: test
- Level: medium
- Author: Stamatis Chatzimangou
- Date: 2022-10-23
- Source Path: rules/windows/builtin/application/msiinstaller/win_msi_install_from_web.yml

## Logsource

- product: windows
- service: application

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.007]]

## Detection

```yaml
selection:
  Provider_Name: MsiInstaller
  EventID:
  - 1040
  - 1042
  Data|contains: ://
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/_st0pp3r_/status/1583922009842802689

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/msiinstaller/win_msi_install_from_web.yml)
