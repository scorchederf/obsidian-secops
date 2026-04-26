---
sigma_id: "eca5e022-d368-4043-98e5-9736fb01f72f"
title: "Clear or Disable Kernel Ring Buffer Logs via Syslog Syscall"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/syscall/lnx_auditd_clean_disable_dmesg_logs_via_syslog.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/syscall/lnx_auditd_clean_disable_dmesg_logs_via_syslog.yml"
build_date: "2026-04-26 14:14:22"
status: "experimental"
level: "medium"
logsource: "linux / auditd"
aliases:
  - "eca5e022-d368-4043-98e5-9736fb01f72f"
  - "Clear or Disable Kernel Ring Buffer Logs via Syslog Syscall"
attack_technique_ids:
  - "T1070.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Clear or Disable Kernel Ring Buffer Logs via Syslog Syscall

Detects the use of the `syslog` syscall with action code 5 (SYSLOG_ACTION_CLEAR),
(4 is SYSLOG_ACTION_READ_CLEAR and 6 is SYSLOG_ACTION_CONSOLE_OFF) which clears the kernel
ring buffer (dmesg logs). This can be used by attackers to hide traces after exploitation
or privilege escalation. A common technique is running `dmesg -c`, which triggers this syscall internally.

## Metadata

- Rule ID: eca5e022-d368-4043-98e5-9736fb01f72f
- Status: experimental
- Level: medium
- Author: Milad Cheraghi
- Date: 2025-05-27
- Modified: 2025-12-05
- Source Path: rules/linux/auditd/syscall/lnx_auditd_clean_disable_dmesg_logs_via_syslog.yml

## Logsource

- definition: Required auditd configuration:
-a always,exit -F arch=b64 -S syslog -F a0=4 -k clear_dmesg_logs
-a always,exit -F arch=b64 -S syslog -F a0=5 -k clear_dmesg_logs
-a always,exit -F arch=b64 -S syslog -F a0=6 -k disable_dmesg_logs
-a always,exit -F arch=b32 -S syslog -F a0=4 -k clear_dmesg_logs
-a always,exit -F arch=b32 -S syslog -F a0=5 -k clear_dmesg_logs
-a always,exit -F arch=b32 -S syslog -F a0=6 -k disable_dmesg_logs

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.002]]

## Detection

```yaml
selection:
  type: SYSCALL
  SYSCALL: syslog
  a0:
  - 4
  - 5
  - 6
condition: selection
```

## False Positives

- System administrators or scripts that intentionally clear logs
- Debugging scripts

## References

- https://man7.org/linux/man-pages/man2/syslog.2.html
- https://man7.org/linux/man-pages/man1/dmesg.1.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/syscall/lnx_auditd_clean_disable_dmesg_logs_via_syslog.yml)
