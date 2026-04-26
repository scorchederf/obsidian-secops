---
sigma_id: "9577edbb-851f-4243-8c91-1d5b50c1a39b"
title: "Atbroker Registry Change"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_susp_atbroker_change.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_susp_atbroker_change.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / registry_event"
aliases:
  - "9577edbb-851f-4243-8c91-1d5b50c1a39b"
  - "Atbroker Registry Change"
attack_technique_ids:
  - "T1218"
  - "T1547"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Atbroker Registry Change

Detects creation/modification of Assistive Technology applications and persistence with usage of 'at'

## Metadata

- Rule ID: 9577edbb-851f-4243-8c91-1d5b50c1a39b
- Status: test
- Level: medium
- Author: Mateusz Wydra, oscd.community
- Date: 2020-10-13
- Modified: 2023-01-19
- Source Path: rules/windows/registry/registry_event/registry_event_susp_atbroker_change.yml

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]
- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547]]

## Detection

```yaml
selection:
  TargetObject|contains:
  - Software\Microsoft\Windows NT\CurrentVersion\Accessibility\ATs
  - Software\Microsoft\Windows NT\CurrentVersion\Accessibility\Configuration
filter_atbroker:
  Image: C:\Windows\system32\atbroker.exe
  TargetObject|contains: \Microsoft\Windows NT\CurrentVersion\Accessibility\Configuration
  Details: (Empty)
filter_uninstallers:
  Image|startswith: C:\Windows\Installer\MSI
  TargetObject|contains: Software\Microsoft\Windows NT\CurrentVersion\Accessibility\ATs
condition: selection and not 1 of filter_*
```

## False Positives

- Creation of non-default, legitimate at usage

## References

- http://www.hexacorn.com/blog/2016/07/22/beyond-good-ol-run-key-part-42/
- https://lolbas-project.github.io/lolbas/Binaries/Atbroker/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_susp_atbroker_change.yml)
