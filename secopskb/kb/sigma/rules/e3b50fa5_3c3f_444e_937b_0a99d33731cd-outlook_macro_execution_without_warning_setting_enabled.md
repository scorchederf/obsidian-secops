---
sigma_id: "e3b50fa5-3c3f-444e-937b-0a99d33731cd"
title: "Outlook Macro Execution Without Warning Setting Enabled"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_office_outlook_enable_macro_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_office_outlook_enable_macro_execution.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "e3b50fa5-3c3f-444e-937b-0a99d33731cd"
  - "Outlook Macro Execution Without Warning Setting Enabled"
attack_technique_ids:
  - "T1137"
  - "T1008"
  - "T1546"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Outlook Macro Execution Without Warning Setting Enabled

Detects the modification of Outlook security setting to allow unprompted execution of macros.

## Metadata

- Rule ID: e3b50fa5-3c3f-444e-937b-0a99d33731cd
- Status: test
- Level: high
- Author: @ScoubiMtl
- Date: 2021-04-05
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_office_outlook_enable_macro_execution.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1137-office_application_startup|T1137]]
- [[kb/attack/techniques/T1008-fallback_channels|T1008]]
- [[kb/attack/techniques/T1546-event_triggered_execution|T1546]]

## Detection

```yaml
selection:
  TargetObject|endswith: \Outlook\Security\Level
  Details|contains: '0x00000001'
condition: selection
```

## False Positives

- Unlikely

## References

- https://www.mdsec.co.uk/2020/11/a-fresh-outlook-on-mail-based-persistence/
- https://speakerdeck.com/heirhabarov/hunting-for-persistence-via-microsoft-exchange-server-or-outlook?slide=53

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_office_outlook_enable_macro_execution.yml)
