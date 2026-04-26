---
sigma_id: "106d7cbd-80ff-4985-b682-a7043e5acb72"
title: "Loading of Kernel Module via Insmod"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/syscall/lnx_auditd_load_module_insmod.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/syscall/lnx_auditd_load_module_insmod.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "high"
logsource: "linux / auditd"
aliases:
  - "106d7cbd-80ff-4985-b682-a7043e5acb72"
  - "Loading of Kernel Module via Insmod"
attack_technique_ids:
  - "T1547.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Loading of Kernel Module via Insmod

Detects loading of kernel modules with insmod command.
Loadable Kernel Modules (LKMs) are pieces of code that can be loaded and unloaded into the kernel upon demand.
Adversaries may use LKMs to obtain persistence within the system or elevate the privileges.

## Metadata

- Rule ID: 106d7cbd-80ff-4985-b682-a7043e5acb72
- Status: test
- Level: high
- Author: Pawel Mazur
- Date: 2021-11-02
- Modified: 2022-12-25
- Source Path: rules/linux/auditd/syscall/lnx_auditd_load_module_insmod.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.006]]

## Detection

```yaml
selection:
  type: SYSCALL
  comm: insmod
  exe: /usr/bin/kmod
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1547.006/T1547.006.md
- https://linux.die.net/man/8/insmod
- https://man7.org/linux/man-pages/man8/kmod.8.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/syscall/lnx_auditd_load_module_insmod.yml)
