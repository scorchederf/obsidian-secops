---
sigma_id: "a07f0359-4c90-4dc4-a681-8ffea40b4f47"
title: "Service Binary in Suspicious Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_creation_service_susp_folder.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_creation_service_susp_folder.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "a07f0359-4c90-4dc4-a681-8ffea40b4f47"
  - "Service Binary in Suspicious Folder"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Service Binary in Suspicious Folder

Detect the creation of a service with a service binary located in a suspicious directory

## Metadata

- Rule ID: a07f0359-4c90-4dc4-a681-8ffea40b4f47
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), frack113
- Date: 2022-05-02
- Modified: 2025-10-07
- Source Path: rules/windows/registry/registry_set/registry_set_creation_service_susp_folder.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection_service_start:
  TargetObject|startswith: HKLM\System\CurrentControlSet\Services\
  TargetObject|endswith: \Start
  Image|contains:
  - \Users\Public\
  - \Perflogs\
  - \ADMIN$\
  - \Temp\
  Details:
  - DWORD (0x00000000)
  - DWORD (0x00000001)
  - DWORD (0x00000002)
selection_service_imagepath:
  TargetObject|startswith: HKLM\System\CurrentControlSet\Services\
  TargetObject|endswith: \ImagePath
  Details|contains:
  - \Users\Public\
  - \Perflogs\
  - \ADMIN$\
  - \Temp\
filter_optional_avast:
  Image|contains|all:
  - \Common Files\
  - \Temp\
filter_optional_mbamservice:
  TargetObject|endswith: \CurrentControlSet\Services\MBAMInstallerService\ImagePath
  Details|endswith: \AppData\Local\Temp\MBAMInstallerService.exe"
  Image: C:\Windows\system32\services.exe
condition: 1 of selection_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.001/T1562.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_creation_service_susp_folder.yml)
