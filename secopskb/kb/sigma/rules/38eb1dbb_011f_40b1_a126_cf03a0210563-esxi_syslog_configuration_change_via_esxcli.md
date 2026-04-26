---
sigma_id: "38eb1dbb-011f-40b1-a126-cf03a0210563"
title: "ESXi Syslog Configuration Change Via ESXCLI"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_esxcli_syslog_config_change.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_esxcli_syslog_config_change.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "38eb1dbb-011f-40b1-a126-cf03a0210563"
  - "ESXi Syslog Configuration Change Via ESXCLI"
attack_technique_ids:
  - "T1562.001"
  - "T1562.003"
  - "T1059.012"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# ESXi Syslog Configuration Change Via ESXCLI

Detects changes to the ESXi syslog configuration via "esxcli"

## Metadata

- Rule ID: 38eb1dbb-011f-40b1-a126-cf03a0210563
- Status: test
- Level: medium
- Author: Cedric Maurugeon
- Date: 2023-09-04
- Source Path: rules/linux/process_creation/proc_creation_lnx_esxcli_syslog_config_change.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]
- [[kb/attack/techniques/T1562-impair_defenses|T1562.003]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.012]]

## Detection

```yaml
selection:
  Image|endswith: /esxcli
  CommandLine|contains|all:
  - system
  - syslog
  - config
  CommandLine|contains: ' set'
condition: selection
```

## False Positives

- Legitimate administrative activities

## References

- https://support.solarwinds.com/SuccessCenter/s/article/Configure-ESXi-Syslog-to-LEM?language=en_US
- https://developer.broadcom.com/xapis/esxcli-command-reference/7.0.0/namespace/esxcli_system.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_esxcli_syslog_config_change.yml)
