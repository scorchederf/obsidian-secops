---
sigma_id: "4cb57c2f-1f29-41f8-893d-8bed8e1c1d2f"
title: "System Shutdown/Reboot - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/execve/lnx_auditd_system_shutdown_reboot.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_system_shutdown_reboot.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "informational"
logsource: "linux / auditd"
aliases:
  - "4cb57c2f-1f29-41f8-893d-8bed8e1c1d2f"
  - "System Shutdown/Reboot - Linux"
attack_technique_ids:
  - "T1529"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# System Shutdown/Reboot - Linux

Adversaries may shutdown/reboot systems to interrupt access to, or aid in the destruction of, those systems.

## Metadata

- Rule ID: 4cb57c2f-1f29-41f8-893d-8bed8e1c1d2f
- Status: test
- Level: informational
- Author: Igor Fits, oscd.community
- Date: 2020-10-15
- Modified: 2022-11-26
- Source Path: rules/linux/auditd/execve/lnx_auditd_system_shutdown_reboot.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1529-system_shutdown_reboot|T1529]]

## Detection

```yaml
execve:
  type: EXECVE
shutdowncmd:
- shutdown
- reboot
- halt
- poweroff
init:
- init
- telinit
initselection:
- 0
- 6
condition: execve and (shutdowncmd or (init and initselection))
```

## False Positives

- Legitimate administrative activity

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1529/T1529.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_system_shutdown_reboot.yml)
