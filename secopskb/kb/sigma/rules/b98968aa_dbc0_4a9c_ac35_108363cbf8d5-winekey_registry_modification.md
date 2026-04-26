---
sigma_id: "b98968aa-dbc0-4a9c-ac35-108363cbf8d5"
title: "WINEKEY Registry Modification"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_runkey_winekey.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_runkey_winekey.yml"
build_date: "2026-04-26 14:14:39"
status: "test"
level: "high"
logsource: "windows / registry_event"
aliases:
  - "b98968aa-dbc0-4a9c-ac35-108363cbf8d5"
  - "WINEKEY Registry Modification"
attack_technique_ids:
  - "T1547"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# WINEKEY Registry Modification

Detects potential malicious modification of run keys by winekey or team9 backdoor

## Metadata

- Rule ID: b98968aa-dbc0-4a9c-ac35-108363cbf8d5
- Status: test
- Level: high
- Author: omkar72
- Date: 2020-10-30
- Modified: 2021-11-27
- Source Path: rules/windows/registry/registry_event/registry_event_runkey_winekey.yml

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547]]

## Detection

```yaml
selection:
  TargetObject|endswith: Software\Microsoft\Windows\CurrentVersion\Run\Backup Mgr
condition: selection
```

## False Positives

- Unknown

## References

- https://www.fireeye.com/blog/threat-research/2020/10/kegtap-and-singlemalt-with-a-ransomware-chaser.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_runkey_winekey.yml)
