---
sigma_id: "60936b49-fca0-4f32-993d-7415edcf9a5d"
title: "New Application in AppCompat"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_new_application_appcompat.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_new_application_appcompat.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "informational"
logsource: "windows / registry_set"
aliases:
  - "60936b49-fca0-4f32-993d-7415edcf9a5d"
  - "New Application in AppCompat"
attack_technique_ids:
  - "T1204.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New Application in AppCompat

A General detection for a new application in AppCompat. This indicates an application executing for the first time on an endpoint.

## Metadata

- Rule ID: 60936b49-fca0-4f32-993d-7415edcf9a5d
- Status: test
- Level: informational
- Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
- Date: 2020-05-02
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_new_application_appcompat.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution|T1204.002]]

## Detection

```yaml
selection:
  TargetObject|contains: \AppCompatFlags\Compatibility Assistant\Store\
condition: selection
```

## False Positives

- This rule is to explore new applications on an endpoint. False positives depends on the organization.
- Newly setup system.
- Legitimate installation of new application.

## References

- https://github.com/OTRF/detection-hackathon-apt29/issues/1
- https://github.com/OTRF/ThreatHunter-Playbook/blob/2d4257f630f4c9770f78d0c1df059f891ffc3fec/docs/evals/apt29/detections/1.A.1_DFD6A782-9BDB-4550-AB6B-525E825B095E.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_new_application_appcompat.yml)
