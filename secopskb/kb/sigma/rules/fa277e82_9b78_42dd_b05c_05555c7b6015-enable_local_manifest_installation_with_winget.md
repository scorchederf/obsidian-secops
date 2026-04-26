---
sigma_id: "fa277e82-9b78-42dd-b05c-05555c7b6015"
title: "Enable Local Manifest Installation With Winget"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_winget_enable_local_manifest.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_winget_enable_local_manifest.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "fa277e82-9b78-42dd-b05c-05555c7b6015"
  - "Enable Local Manifest Installation With Winget"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Enable Local Manifest Installation With Winget

Detects changes to the AppInstaller (winget) policy. Specifically the activation of the local manifest installation, which allows a user to install new packages via custom manifests.

## Metadata

- Rule ID: fa277e82-9b78-42dd-b05c-05555c7b6015
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-04-17
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_winget_enable_local_manifest.yml

## Logsource

- category: registry_set
- product: windows

## Detection

```yaml
selection:
  TargetObject|endswith: \AppInstaller\EnableLocalManifestFiles
  Details: DWORD (0x00000001)
condition: selection
```

## False Positives

- Administrators or developers might enable this for testing purposes or to install custom private packages

## References

- https://github.com/nasbench/Misc-Research/tree/b9596e8109dcdb16ec353f316678927e507a5b8d/LOLBINs/Winget

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_winget_enable_local_manifest.yml)
