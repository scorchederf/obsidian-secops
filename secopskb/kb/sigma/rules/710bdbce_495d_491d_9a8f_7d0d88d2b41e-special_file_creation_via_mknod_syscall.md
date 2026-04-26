---
sigma_id: "710bdbce-495d-491d-9a8f-7d0d88d2b41e"
title: "Special File Creation via Mknod Syscall"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/syscall/lnx_auditd_susp_special_file_creation_via_mknod_syscall.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/syscall/lnx_auditd_susp_special_file_creation_via_mknod_syscall.yml"
build_date: "2026-04-26 14:14:35"
status: "experimental"
level: "low"
logsource: "linux / auditd"
aliases:
  - "710bdbce-495d-491d-9a8f-7d0d88d2b41e"
  - "Special File Creation via Mknod Syscall"
attack_technique_ids:
  - "T1543.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Special File Creation via Mknod Syscall

Detects usage of the `mknod` syscall to create special files (e.g., character or block devices).
Attackers or malware might use `mknod` to create fake devices, interact with kernel interfaces,
or establish covert channels in Linux systems.
Monitoring the use of `mknod` is important because this syscall is rarely used by legitimate applications,
and it can be abused to bypass file system restrictions or create backdoors.

## Metadata

- Rule ID: 710bdbce-495d-491d-9a8f-7d0d88d2b41e
- Status: experimental
- Level: low
- Author: Milad Cheraghi
- Date: 2025-05-31
- Modified: 2025-12-05
- Source Path: rules/linux/auditd/syscall/lnx_auditd_susp_special_file_creation_via_mknod_syscall.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]

## Detection

```yaml
selection:
  type: SYSCALL
  SYSCALL: mknod
condition: selection
```

## False Positives

- Device creation by legitimate scripts or init systems (udevadm, MAKEDEV)
- Container runtimes or security tools during initialization

## References

- https://man7.org/linux/man-pages/man2/mknod.2.html
- https://hopeness.medium.com/master-the-linux-mknod-command-a-comprehensive-guide-1c150a546aa8

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/syscall/lnx_auditd_susp_special_file_creation_via_mknod_syscall.yml)
