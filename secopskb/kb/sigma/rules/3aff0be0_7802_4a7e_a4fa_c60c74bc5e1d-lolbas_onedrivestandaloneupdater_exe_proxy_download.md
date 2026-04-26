---
sigma_id: "3aff0be0-7802-4a7e-a4fa-c60c74bc5e1d"
title: "Lolbas OneDriveStandaloneUpdater.exe Proxy Download"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_lolbin_onedrivestandaloneupdater.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_lolbin_onedrivestandaloneupdater.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "3aff0be0-7802-4a7e-a4fa-c60c74bc5e1d"
  - "Lolbas OneDriveStandaloneUpdater.exe Proxy Download"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Lolbas OneDriveStandaloneUpdater.exe Proxy Download

Detects setting a custom URL for OneDriveStandaloneUpdater.exe to download a file from the Internet without executing any
anomalous executables with suspicious arguments. The downloaded file will be in C:\Users\redacted\AppData\Local\Microsoft\OneDrive\StandaloneUpdaterreSignInSettingsConfig.json

## Metadata

- Rule ID: 3aff0be0-7802-4a7e-a4fa-c60c74bc5e1d
- Status: test
- Level: high
- Author: frack113
- Date: 2022-05-28
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_lolbin_onedrivestandaloneupdater.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection:
  TargetObject|contains: \SOFTWARE\Microsoft\OneDrive\UpdateOfficeConfig\UpdateRingSettingURLFromOC
condition: selection
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/OneDriveStandaloneUpdater/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_lolbin_onedrivestandaloneupdater.yml)
