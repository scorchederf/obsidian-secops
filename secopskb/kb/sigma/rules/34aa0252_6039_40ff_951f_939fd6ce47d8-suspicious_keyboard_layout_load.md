---
sigma_id: "34aa0252-6039-40ff-951f-939fd6ce47d8"
title: "Suspicious Keyboard Layout Load"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_susp_keyboard_layout_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_susp_keyboard_layout_load.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "34aa0252-6039-40ff-951f-939fd6ce47d8"
  - "Suspicious Keyboard Layout Load"
attack_technique_ids:
  - "T1588.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Keyboard Layout Load

Detects the keyboard preload installation with a suspicious keyboard layout, e.g. Chinese, Iranian or Vietnamese layout load in user session on systems maintained by US staff only

## Metadata

- Rule ID: 34aa0252-6039-40ff-951f-939fd6ce47d8
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2019-10-12
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_susp_keyboard_layout_load.yml

## Logsource

- category: registry_set
- definition: Requirements: Sysmon config that monitors \Keyboard Layout\Preload subkey of the HKLU hives - see https://github.com/SwiftOnSecurity/sysmon-config/pull/92/files
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1588-obtain_capabilities|T1588.002]]

## Detection

```yaml
selection_registry:
  TargetObject|contains:
  - \Keyboard Layout\Preload\
  - \Keyboard Layout\Substitutes\
  Details|contains:
  - 00000429
  - 00050429
  - 0000042a
condition: selection_registry
```

## False Positives

- Administrators or users that actually use the selected keyboard layouts (heavily depends on the organisation's user base)

## References

- https://renenyffenegger.ch/notes/Windows/registry/tree/HKEY_CURRENT_USER/Keyboard-Layout/Preload/index
- https://github.com/SwiftOnSecurity/sysmon-config/pull/92/files

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_susp_keyboard_layout_load.yml)
