---
sigma_id: "7692f583-bd30-4008-8615-75dab3f08a99"
title: "Enable BPF Kprobes Tracing"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_bpf_kprob_tracing_enabled.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_bpf_kprob_tracing_enabled.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "7692f583-bd30-4008-8615-75dab3f08a99"
  - "Enable BPF Kprobes Tracing"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Enable BPF Kprobes Tracing

Detects common command used to enable bpf kprobes tracing

## Metadata

- Rule ID: 7692f583-bd30-4008-8615-75dab3f08a99
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-25
- Source Path: rules/linux/process_creation/proc_creation_lnx_bpf_kprob_tracing_enabled.yml

## Logsource

- category: process_creation
- product: linux

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - echo 1 >
  - /sys/kernel/debug/tracing/events/kprobes/
  CommandLine|contains:
  - /myprobe/enable
  - /myretprobe/enable
condition: selection
```

## False Positives

- Unknown

## References

- https://embracethered.com/blog/posts/2021/offensive-bpf-bpftrace/
- https://bpftrace.org/
- https://www.kernel.org/doc/html/v5.0/trace/kprobetrace.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_bpf_kprob_tracing_enabled.yml)
