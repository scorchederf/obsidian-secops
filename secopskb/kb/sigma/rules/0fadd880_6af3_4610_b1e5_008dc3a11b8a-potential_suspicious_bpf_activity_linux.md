---
sigma_id: "0fadd880-6af3-4610-b1e5-008dc3a11b8a"
title: "Potential Suspicious BPF Activity - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/builtin/lnx_potential_susp_ebpf_activity.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_potential_susp_ebpf_activity.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "high"
logsource: "linux"
aliases:
  - "0fadd880-6af3-4610-b1e5-008dc3a11b8a"
  - "Potential Suspicious BPF Activity - Linux"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Suspicious BPF Activity - Linux

Detects the presence of "bpf_probe_write_user" BPF helper-generated warning messages. Which could be a sign of suspicious eBPF activity on the system.

## Metadata

- Rule ID: 0fadd880-6af3-4610-b1e5-008dc3a11b8a
- Status: test
- Level: high
- Author: Red Canary (idea), Nasreddine Bencherchali
- Date: 2023-01-25
- Source Path: rules/linux/builtin/lnx_potential_susp_ebpf_activity.yml

## Logsource

- product: linux

## Detection

```yaml
selection:
- bpf_probe_write_user
condition: selection
```

## False Positives

- Unknown

## References

- https://redcanary.com/blog/ebpf-malware/
- https://man7.org/linux/man-pages/man7/bpf-helpers.7.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_potential_susp_ebpf_activity.yml)
