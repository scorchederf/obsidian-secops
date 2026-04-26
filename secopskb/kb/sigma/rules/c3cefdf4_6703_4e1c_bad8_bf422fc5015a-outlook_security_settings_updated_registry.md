---
sigma_id: "c3cefdf4-6703-4e1c-bad8-bf422fc5015a"
title: "Outlook Security Settings Updated - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_office_outlook_security_settings.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_office_outlook_security_settings.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "c3cefdf4-6703-4e1c-bad8-bf422fc5015a"
  - "Outlook Security Settings Updated - Registry"
attack_technique_ids:
  - "T1137"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Outlook Security Settings Updated - Registry

Detects changes to the registry values related to outlook security settings

## Metadata

- Rule ID: c3cefdf4-6703-4e1c-bad8-bf422fc5015a
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-12-28
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_office_outlook_security_settings.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1137-office_application_startup|T1137]]

## Detection

```yaml
selection:
  TargetObject|contains|all:
  - \SOFTWARE\Microsoft\Office\
  - \Outlook\Security\
condition: selection
```

## False Positives

- Administrative activity

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1137/T1137.md
- https://learn.microsoft.com/en-us/outlook/troubleshoot/security/information-about-email-security-settings

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_office_outlook_security_settings.yml)
