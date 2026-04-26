---
sigma_id: "e497a24e-9345-4a62-9803-b06d7d7cb132"
title: "ASLR Disabled Via Sysctl or Direct Syscall - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/lnx_auditd_disable_aslr_protection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/lnx_auditd_disable_aslr_protection.yml"
build_date: "2026-04-26 17:03:18"
status: "experimental"
level: "high"
logsource: "linux / auditd"
aliases:
  - "e497a24e-9345-4a62-9803-b06d7d7cb132"
  - "ASLR Disabled Via Sysctl or Direct Syscall - Linux"
attack_technique_ids:
  - "T1562.001"
  - "T1055.009"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# ASLR Disabled Via Sysctl or Direct Syscall - Linux

Detects actions that disable Address Space Layout Randomization (ASLR) in Linux, including:
  - Use of the `personality` syscall with the ADDR_NO_RANDOMIZE flag (0x0040000)
  - Modification of the /proc/sys/kernel/randomize_va_space file
  - Execution of the `sysctl` command to set `kernel.randomize_va_space=0`
Disabling ASLR is often used by attackers during exploit development or to bypass memory protection mechanisms.
A successful use of these methods can reduce the effectiveness of ASLR and make memory corruption attacks more reliable.

## Metadata

- Rule ID: e497a24e-9345-4a62-9803-b06d7d7cb132
- Status: experimental
- Level: high
- Author: Milad Cheraghi
- Date: 2025-05-26
- Modified: 2025-12-05
- Source Path: rules/linux/auditd/lnx_auditd_disable_aslr_protection.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]
- [[kb/attack/techniques/T1055-process_injection|T1055.009]]

## Detection

```yaml
selection_syscall:
  type: SYSCALL
  SYSCALL: personality
  a0: 40000
selection_sysctl:
  type: EXECVE
  a0: sysctl
  a1: -w
  a2: kernel.randomize_va_space=0
condition: 1 of selection_*
```

## False Positives

- Debugging or legitimate software testing

## References

- https://github.com/CheraghiMilad/bypass-Neo23x0-auditd-config/blob/f1c478a37911a5447d5ffcd580f22b167bf3df14/personality-syscall/README.md
- https://man7.org/linux/man-pages/man2/personality.2.html
- https://manual.cs50.io/2/personality
- https://linux-audit.com/linux-aslr-and-kernelrandomize_va_space-setting/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/lnx_auditd_disable_aslr_protection.yml)
