---
sigma_id: "1543ae20-cbdf-4ec1-8d12-7664d667a825"
title: "Suspicious Commands Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/execve/lnx_auditd_susp_cmds.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_susp_cmds.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "linux / auditd"
aliases:
  - "1543ae20-cbdf-4ec1-8d12-7664d667a825"
  - "Suspicious Commands Linux"
attack_technique_ids:
  - "T1059.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Commands Linux

Detects relevant commands often related to malware or hacking activity

## Metadata

- Rule ID: 1543ae20-cbdf-4ec1-8d12-7664d667a825
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2017-12-12
- Modified: 2022-10-05
- Source Path: rules/linux/auditd/execve/lnx_auditd_susp_cmds.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.004]]

## Detection

```yaml
cmd1:
  type: EXECVE
  a0: chmod
  a1: 777
cmd2:
  type: EXECVE
  a0: chmod
  a1: u+s
cmd3:
  type: EXECVE
  a0: cp
  a1: /bin/ksh
cmd4:
  type: EXECVE
  a0: cp
  a1: /bin/sh
condition: 1 of cmd*
```

## False Positives

- Admin activity

## References

- Internal Research - mostly derived from exploit code including code in MSF

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_susp_cmds.yml)
