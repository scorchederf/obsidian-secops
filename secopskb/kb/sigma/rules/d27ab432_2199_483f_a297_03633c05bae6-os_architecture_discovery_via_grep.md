---
sigma_id: "d27ab432-2199-483f-a297-03633c05bae6"
title: "OS Architecture Discovery Via Grep"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_grep_os_arch_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_grep_os_arch_discovery.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "low"
logsource: "linux / process_creation"
aliases:
  - "d27ab432-2199-483f-a297-03633c05bae6"
  - "OS Architecture Discovery Via Grep"
attack_technique_ids:
  - "T1082"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# OS Architecture Discovery Via Grep

Detects the use of grep to identify information about the operating system architecture. Often combined beforehand with the execution of "uname" or "cat /proc/cpuinfo"

## Metadata

- Rule ID: d27ab432-2199-483f-a297-03633c05bae6
- Status: test
- Level: low
- Author: Joseliyo Sanchez, @Joseliyo_Jstnk
- Date: 2023-06-02
- Source Path: rules/linux/process_creation/proc_creation_lnx_grep_os_arch_discovery.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Detection

```yaml
selection_process:
  Image|endswith: /grep
selection_architecture:
  CommandLine|endswith:
  - aarch64
  - arm
  - i386
  - i686
  - mips
  - x86_64
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://blogs.jpcert.or.jp/en/2023/05/gobrat.html
- https://jstnk9.github.io/jstnk9/research/GobRAT-Malware/
- https://www.virustotal.com/gui/file/60bcd645450e4c846238cf0e7226dc40c84c96eba99f6b2cffcd0ab4a391c8b3/detection
- https://www.virustotal.com/gui/file/3e44c807a25a56f4068b5b8186eee5002eed6f26d665a8b791c472ad154585d1/detection

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_grep_os_arch_discovery.yml)
