---
sigma_id: "6763c6c8-bd01-4687-bc8d-4fa52cf8ba08"
title: "Outlook EnableUnsafeClientMailRules Setting Enabled - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_office_outlook_enable_unsafe_client_mail_rules.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_office_outlook_enable_unsafe_client_mail_rules.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "6763c6c8-bd01-4687-bc8d-4fa52cf8ba08"
  - "Outlook EnableUnsafeClientMailRules Setting Enabled - Registry"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects an attacker trying to enable the outlook security setting "EnableUnsafeClientMailRules" which allows outlook to run applications or execute macros

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112: Modify Registry]]

## Detection

```yaml
selection:
  TargetObject|endswith: \Outlook\Security\EnableUnsafeClientMailRules
  Details: DWORD (0x00000001)
condition: selection
```

## False Positives

- Unknown

## References

- https://support.microsoft.com/en-us/topic/how-to-control-the-rule-actions-to-start-an-application-or-run-a-macro-in-outlook-2016-and-outlook-2013-e4964b72-173c-959d-5d7b-ead562979048
- https://speakerdeck.com/heirhabarov/hunting-for-persistence-via-microsoft-exchange-server-or-outlook?slide=44

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_office_outlook_enable_unsafe_client_mail_rules.yml)
