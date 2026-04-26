---
sigma_id: "9e1a1fdf-ee58-40ce-8e15-b66ca5a80e1f"
title: "Previously Installed IIS Module Was Removed"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/iis-configuration/win_iis_module_removed.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/iis-configuration/win_iis_module_removed.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "low"
logsource: "windows / iis-configuration"
aliases:
  - "9e1a1fdf-ee58-40ce-8e15-b66ca5a80e1f"
  - "Previously Installed IIS Module Was Removed"
attack_technique_ids:
  - "T1562.002"
  - "T1505.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Previously Installed IIS Module Was Removed

Detects the removal of a previously installed IIS module.

## Metadata

- Rule ID: 9e1a1fdf-ee58-40ce-8e15-b66ca5a80e1f
- Status: test
- Level: low
- Author: Nasreddine Bencherchali
- Date: 2024-10-06
- Source Path: rules/windows/builtin/iis-configuration/win_iis_module_removed.yml

## Logsource

- product: windows
- service: iis-configuration

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.002]]
- [[kb/attack/techniques/T1505-server_software_component|T1505.004]]

## Detection

```yaml
selection:
  EventID: 29
  Configuration|contains: /system.webServer/modules/remove
condition: selection
```

## False Positives

- Legitimate administrator activity

## References

- https://learn.microsoft.com/en-us/iis/manage/provisioning-and-managing-iis/configure-logging-in-iis
- https://www.microsoft.com/en-us/security/blog/2022/12/12/iis-modules-the-evolution-of-web-shells-and-how-to-detect-them/
- https://www.microsoft.com/en-us/security/blog/2022/07/26/malicious-iis-extensions-quietly-open-persistent-backdoors-into-servers/
- https://learn.microsoft.com/en-us/iis/get-started/introduction-to-iis/iis-modules-overview

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/iis-configuration/win_iis_module_removed.yml)
