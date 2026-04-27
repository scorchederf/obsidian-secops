---
sigma_id: "396ae3eb-4174-4b9b-880e-dc0364d78a19"
title: "Potential Persistence Via Outlook LoadMacroProviderOnBoot Setting"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_office_outlook_enable_load_macro_provider_on_boot.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_office_outlook_enable_load_macro_provider_on_boot.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "396ae3eb-4174-4b9b-880e-dc0364d78a19"
  - "Potential Persistence Via Outlook LoadMacroProviderOnBoot Setting"
attack_technique_ids:
  - "T1137"
  - "T1008"
  - "T1546"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the modification of Outlook setting "LoadMacroProviderOnBoot" which if enabled allows the automatic loading of any configured VBA project/module

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1137-office_application_startup|T1137: Office Application Startup]]
- [[kb/attack/techniques/T1008-fallback_channels|T1008: Fallback Channels]]
- [[kb/attack/techniques/T1546-event_triggered_execution|T1546: Event Triggered Execution]]

## Detection

```yaml
selection:
  TargetObject|endswith: \Outlook\LoadMacroProviderOnBoot
  Details|contains: '0x00000001'
condition: selection
```

## False Positives

- Unknown

## References

- https://speakerdeck.com/heirhabarov/hunting-for-persistence-via-microsoft-exchange-server-or-outlook?slide=53
- https://www.linkedin.com/pulse/outlook-backdoor-using-vba-samir-b-/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_office_outlook_enable_load_macro_provider_on_boot.yml)
