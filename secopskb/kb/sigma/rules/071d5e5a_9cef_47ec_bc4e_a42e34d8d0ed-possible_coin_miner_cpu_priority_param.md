---
sigma_id: "071d5e5a-9cef-47ec-bc4e-a42e34d8d0ed"
title: "Possible Coin Miner CPU Priority Param"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/execve/lnx_auditd_coinminer.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_coinminer.yml"
build_date: "2026-04-26 15:01:47"
status: "test"
level: "critical"
logsource: "linux / auditd"
aliases:
  - "071d5e5a-9cef-47ec-bc4e-a42e34d8d0ed"
  - "Possible Coin Miner CPU Priority Param"
attack_technique_ids:
  - "T1068"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Possible Coin Miner CPU Priority Param

Detects command line parameter very often used with coin miners

## Metadata

- Rule ID: 071d5e5a-9cef-47ec-bc4e-a42e34d8d0ed
- Status: test
- Level: critical
- Author: Florian Roth (Nextron Systems)
- Date: 2021-10-09
- Modified: 2022-12-25
- Source Path: rules/linux/auditd/execve/lnx_auditd_coinminer.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1068-exploitation_for_privilege_escalation|T1068]]

## Detection

```yaml
cmd1:
  a1|startswith: --cpu-priority
cmd2:
  a2|startswith: --cpu-priority
cmd3:
  a3|startswith: --cpu-priority
cmd4:
  a4|startswith: --cpu-priority
cmd5:
  a5|startswith: --cpu-priority
cmd6:
  a6|startswith: --cpu-priority
cmd7:
  a7|startswith: --cpu-priority
condition: 1 of cmd*
```

## False Positives

- Other tools that use a --cpu-priority flag

## References

- https://xmrig.com/docs/miner/command-line-options

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_coinminer.yml)
