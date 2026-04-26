---
sigma_id: "7c81fec3-1c1d-43b0-996a-46753041b1b6"
title: "UAC Bypass via Event Viewer"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_uac_bypass_eventvwr.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_uac_bypass_eventvwr.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "7c81fec3-1c1d-43b0-996a-46753041b1b6"
  - "UAC Bypass via Event Viewer"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# UAC Bypass via Event Viewer

Detects UAC bypass method using Windows event viewer

## Metadata

- Rule ID: 7c81fec3-1c1d-43b0-996a-46753041b1b6
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2017-03-19
- Modified: 2023-09-28
- Source Path: rules/windows/registry/registry_set/registry_set_uac_bypass_eventvwr.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection:
  TargetObject|endswith: \mscfile\shell\open\command
condition: selection
```

## False Positives

- Unknown

## References

- https://enigma0x3.net/2016/08/15/fileless-uac-bypass-using-eventvwr-exe-and-registry-hijacking/
- https://www.hybrid-analysis.com/sample/e122bc8bf291f15cab182a5d2d27b8db1e7019e4e96bb5cdbd1dfe7446f3f51f?environmentId=100

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_uac_bypass_eventvwr.yml)
