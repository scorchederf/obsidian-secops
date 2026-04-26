---
sigma_id: "b207d563-a1d9-4275-b349-77d1eb55aa6d"
title: "System Info Discovery via Sysinfo Syscall"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/syscall/lnx_auditd_susp_discovery_sysinfo_syscall.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/syscall/lnx_auditd_susp_discovery_sysinfo_syscall.yml"
build_date: "2026-04-26 14:14:37"
status: "experimental"
level: "low"
logsource: "linux / auditd"
aliases:
  - "b207d563-a1d9-4275-b349-77d1eb55aa6d"
  - "System Info Discovery via Sysinfo Syscall"
attack_technique_ids:
  - "T1057"
  - "T1082"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# System Info Discovery via Sysinfo Syscall

Detects use of the sysinfo system call in Linux, which provides a snapshot of key system statistics such as uptime, load averages, memory usage, and the number of running processes.
Malware or reconnaissance tools might leverage sysinfo to fingerprint the system - gathering data to determine if it's a viable target.

## Metadata

- Rule ID: b207d563-a1d9-4275-b349-77d1eb55aa6d
- Status: experimental
- Level: low
- Author: Milad Cheraghi
- Date: 2025-05-30
- Modified: 2025-12-05
- Source Path: rules/linux/auditd/syscall/lnx_auditd_susp_discovery_sysinfo_syscall.yml

## Logsource

- definition: Required auditd configuration:
-a always,exit -F arch=b64 -S sysinfo -k discovery_sysinfo_syscall
-a always,exit -F arch=b32 -S sysinfo -k discovery_sysinfo_syscall

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1057-process_discovery|T1057]]
- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Detection

```yaml
selection:
  type: SYSCALL
  SYSCALL: sysinfo
filter_optional_splunk:
  exe|endswith: /bin/splunkd
condition: selection and not 1 of filter_optional_*
```

## False Positives

- Legitimate administrative activity

## References

- https://github.com/CheraghiMilad/bypass-Neo23x0-auditd-config/blob/f1c478a37911a5447d5ffcd580f22b167bf3df14/sysinfo-syscall/README.md
- https://man7.org/linux/man-pages/man2/sysinfo.2.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/syscall/lnx_auditd_susp_discovery_sysinfo_syscall.yml)
