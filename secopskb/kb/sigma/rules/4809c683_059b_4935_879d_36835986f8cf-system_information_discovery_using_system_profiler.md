---
sigma_id: "4809c683-059b-4935-879d-36835986f8cf"
title: "System Information Discovery Using System_Profiler"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_system_profiler_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_system_profiler_discovery.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "4809c683-059b-4935-879d-36835986f8cf"
  - "System Information Discovery Using System_Profiler"
attack_technique_ids:
  - "T1082"
  - "T1497.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# System Information Discovery Using System_Profiler

Detects the execution of "system_profiler" with specific "Data Types" that have been seen being used by threat actors and malware. It provides system hardware and software configuration information.
This process is primarily used for system information discovery. However, "system_profiler" can also be used to determine if virtualization software is being run for defense evasion purposes.

## Metadata

- Rule ID: 4809c683-059b-4935-879d-36835986f8cf
- Status: test
- Level: medium
- Author: Stephen Lincoln `@slincoln_aiq` (AttackIQ)
- Date: 2024-01-02
- Source Path: rules/macos/process_creation/proc_creation_macos_system_profiler_discovery.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]
- [[kb/attack/techniques/T1497-virtualization_sandbox_evasion|T1497.001]]

## Detection

```yaml
selection_img:
- Image|endswith: /system_profiler
- CommandLine|contains: system_profiler
selection_cmd:
  CommandLine|contains:
  - SPApplicationsDataType
  - SPHardwareDataType
  - SPNetworkDataType
  - SPUSBDataType
condition: all of selection_*
```

## False Positives

- Legitimate administrative activities

## References

- https://www.trendmicro.com/en_za/research/20/k/new-macos-backdoor-connected-to-oceanlotus-surfaces.html
- https://www.sentinelone.com/wp-content/uploads/pdf-gen/1630910064/20-common-tools-techniques-used-by-macos-threat-actors-malware.pdf
- https://ss64.com/mac/system_profiler.html
- https://objective-see.org/blog/blog_0x62.html
- https://www.welivesecurity.com/2019/04/09/oceanlotus-macos-malware-update/
- https://gist.github.com/nasbench/9a1ba4bc7094ea1b47bc42bf172961af

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_system_profiler_discovery.yml)
