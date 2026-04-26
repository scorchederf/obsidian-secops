---
sigma_id: "6ff08e55-ea53-4f27-94a1-eff92e6d9d5c"
title: "System Information Discovery Via Sysctl - MacOS"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_sysctl_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_sysctl_discovery.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "6ff08e55-ea53-4f27-94a1-eff92e6d9d5c"
  - "System Information Discovery Via Sysctl - MacOS"
attack_technique_ids:
  - "T1497.001"
  - "T1082"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# System Information Discovery Via Sysctl - MacOS

Detects the execution of "sysctl" with specific arguments that have been used by threat actors and malware. It provides system hardware information.
This process is primarily used to detect and avoid virtualization and analysis environments.

## Metadata

- Rule ID: 6ff08e55-ea53-4f27-94a1-eff92e6d9d5c
- Status: test
- Level: medium
- Author: Pratinav Chandra
- Date: 2024-05-27
- Source Path: rules/macos/process_creation/proc_creation_macos_sysctl_discovery.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1497-virtualization_sandbox_evasion|T1497.001]]
- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Detection

```yaml
selection_img:
- Image|endswith: /sysctl
- CommandLine|contains: sysctl
selection_cmd:
  CommandLine|contains:
  - hw.
  - kern.
  - machdep.
condition: all of selection_*
```

## False Positives

- Legitimate administrative activities

## References

- https://www.loobins.io/binaries/sysctl/#
- https://evasions.checkpoint.com/techniques/macos.html
- https://www.welivesecurity.com/2019/04/09/oceanlotus-macos-malware-update/
- https://www.sentinelone.com/labs/20-common-tools-techniques-used-by-macos-threat-actors-malware/
- https://objective-see.org/blog/blog_0x1E.html
- https://www.virustotal.com/gui/file/1c547a064494a35d6b5e6b459de183ab2720a22725e082bed6f6629211f7abc1/behavior
- https://www.virustotal.com/gui/file/b4b1fc65f87b3dcfa35e2dbe8e0a34ad9d8a400bec332025c0a2e200671038aa/behavior

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_sysctl_discovery.yml)
