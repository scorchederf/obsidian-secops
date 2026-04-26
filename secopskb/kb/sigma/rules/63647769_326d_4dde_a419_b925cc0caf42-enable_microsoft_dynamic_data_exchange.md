---
sigma_id: "63647769-326d-4dde-a419-b925cc0caf42"
title: "Enable Microsoft Dynamic Data Exchange"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_office_enable_dde.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_office_enable_dde.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "63647769-326d-4dde-a419-b925cc0caf42"
  - "Enable Microsoft Dynamic Data Exchange"
attack_technique_ids:
  - "T1559.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Enable Microsoft Dynamic Data Exchange

Enable Dynamic Data Exchange protocol (DDE) in all supported editions of Microsoft Word or Excel.

## Metadata

- Rule ID: 63647769-326d-4dde-a419-b925cc0caf42
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-02-26
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_office_enable_dde.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1559-inter-process_communication|T1559.002]]

## Detection

```yaml
selection_word:
  TargetObject|endswith: \Word\Security\AllowDDE
  Details:
  - DWORD (0x00000001)
  - DWORD (0x00000002)
selection_excel:
  TargetObject|endswith:
  - \Excel\Security\DisableDDEServerLaunch
  - \Excel\Security\DisableDDEServerLookup
  Details: DWORD (0x00000000)
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://msrc.microsoft.com/update-guide/vulnerability/ADV170021

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_office_enable_dde.yml)
