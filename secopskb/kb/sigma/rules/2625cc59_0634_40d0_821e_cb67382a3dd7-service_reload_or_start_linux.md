---
sigma_id: "2625cc59-0634-40d0-821e-cb67382a3dd7"
title: "Service Reload or Start - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/execve/lnx_auditd_susp_service_reload_or_restart.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_susp_service_reload_or_restart.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "low"
logsource: "linux / auditd"
aliases:
  - "2625cc59-0634-40d0-821e-cb67382a3dd7"
  - "Service Reload or Start - Linux"
attack_technique_ids:
  - "T1543.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Service Reload or Start - Linux

Detects the start, reload or restart of a service.

## Metadata

- Rule ID: 2625cc59-0634-40d0-821e-cb67382a3dd7
- Status: test
- Level: low
- Author: Jakob Weinzettl, oscd.community, CheraghiMilad
- Date: 2019-09-23
- Modified: 2025-03-03
- Source Path: rules/linux/auditd/execve/lnx_auditd_susp_service_reload_or_restart.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.002]]

## Detection

```yaml
selection:
  type: EXECVE
  a0|contains:
  - systemctl
  - service
  a1|contains:
  - reload
  - start
condition: selection
```

## False Positives

- Installation of legitimate service.
- Legitimate reconfiguration of service.
- Command line contains daemon-reload.

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1543.002/T1543.002.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_susp_service_reload_or_restart.yml)
