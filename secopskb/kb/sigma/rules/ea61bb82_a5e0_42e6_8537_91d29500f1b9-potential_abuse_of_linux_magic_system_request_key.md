---
sigma_id: "ea61bb82-a5e0-42e6-8537-91d29500f1b9"
title: "Potential Abuse of Linux Magic System Request Key"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/path/lnx_auditd_magic_system_request_key.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/path/lnx_auditd_magic_system_request_key.yml"
build_date: "2026-04-26 14:14:31"
status: "experimental"
level: "medium"
logsource: "linux / auditd"
aliases:
  - "ea61bb82-a5e0-42e6-8537-91d29500f1b9"
  - "Potential Abuse of Linux Magic System Request Key"
attack_technique_ids:
  - "T1059.004"
  - "T1529"
  - "T1489"
  - "T1499"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Abuse of Linux Magic System Request Key

Detects the potential abuse of the Linux Magic SysRq (System Request) key by adversaries with root or sufficient privileges
to silently manipulate or destabilize a system. By writing to /proc/sysrq-trigger, they can crash the system, kill processes,
or disrupt forensic analysis—all while bypassing standard logging. Though intended for recovery and debugging, SysRq can be
misused as a stealthy post-exploitation tool. It is controlled via /proc/sys/kernel/sysrq or permanently through /etc/sysctl.conf.

## Metadata

- Rule ID: ea61bb82-a5e0-42e6-8537-91d29500f1b9
- Status: experimental
- Level: medium
- Author: Milad Cheraghi
- Date: 2025-05-23
- Source Path: rules/linux/auditd/path/lnx_auditd_magic_system_request_key.yml

## Logsource

- definition: Required auditd configuration:
-w /proc/sysrq-trigger -p wa -k sysrq
-w /proc/sys/kernel/sysrq -p wa -k sysrq

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.004]]
- [[kb/attack/techniques/T1529-system_shutdown_reboot|T1529]]
- [[kb/attack/techniques/T1489-service_stop|T1489]]
- [[kb/attack/techniques/T1499-endpoint_denial_of_service|T1499]]

## Detection

```yaml
selection:
  type: PATH
  name|endswith:
  - /sysrq
  - /sysctl.conf
  - /sysrq-trigger
condition: selection
```

## False Positives

- Legitimate administrative activity

## References

- https://www.kernel.org/doc/html/v4.10/_sources/admin-guide/sysrq.txt
- https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/4/html/reference_guide/s3-proc-sys-kernel
- https://www.splunk.com/en_us/blog/security/threat-update-awfulshred-script-wiper.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/path/lnx_auditd_magic_system_request_key.yml)
