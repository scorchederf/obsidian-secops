---
sigma_id: "f8341cb2-ee25-43fa-a975-d8a5a9714b39"
title: "BPFtrace Unsafe Option Usage"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_bpftrace_unsafe_option_usage.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_bpftrace_unsafe_option_usage.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "f8341cb2-ee25-43fa-a975-d8a5a9714b39"
  - "BPFtrace Unsafe Option Usage"
attack_technique_ids:
  - "T1059.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# BPFtrace Unsafe Option Usage

Detects the usage of the unsafe bpftrace option

## Metadata

- Rule ID: f8341cb2-ee25-43fa-a975-d8a5a9714b39
- Status: test
- Level: medium
- Author: Andreas Hunkeler (@Karneades)
- Date: 2022-02-11
- Source Path: rules/linux/process_creation/proc_creation_lnx_bpftrace_unsafe_option_usage.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.004]]

## Detection

```yaml
selection:
  Image|endswith: bpftrace
  CommandLine|contains: --unsafe
condition: selection
```

## False Positives

- Legitimate usage of the unsafe option

## References

- https://embracethered.com/blog/posts/2021/offensive-bpf-bpftrace/
- https://bpftrace.org/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_bpftrace_unsafe_option_usage.yml)
