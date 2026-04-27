---
sigma_id: "b6d235fc-1d38-4b12-adbe-325f06728f37"
title: "CMSTP Execution Registry Event"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_cmstp_execution_by_registry.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_cmstp_execution_by_registry.yml"
build_date: "2026-04-26 17:03:18"
status: "stable"
level: "high"
logsource: "windows / registry_event"
aliases:
  - "b6d235fc-1d38-4b12-adbe-325f06728f37"
  - "CMSTP Execution Registry Event"
attack_technique_ids:
  - "T1218.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# CMSTP Execution Registry Event

Detects various indicators of Microsoft Connection Manager Profile Installer execution

## Metadata

- Rule ID: b6d235fc-1d38-4b12-adbe-325f06728f37
- Status: stable
- Level: high
- Author: Nik Seetharaman
- Date: 2018-07-16
- Modified: 2020-12-23
- Source Path: rules/windows/registry/registry_event/registry_event_cmstp_execution_by_registry.yml

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.003]]

## Detection

```yaml
selection:
  TargetObject|contains: \cmmgr32.exe
condition: selection
```

## False Positives

- Legitimate CMSTP use (unlikely in modern enterprise environments)

## References

- https://web.archive.org/web/20190720093911/http://www.endurant.io/cmstp/detecting-cmstp-enabled-code-execution-and-uac-bypass-with-sysmon/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_cmstp_execution_by_registry.yml)
