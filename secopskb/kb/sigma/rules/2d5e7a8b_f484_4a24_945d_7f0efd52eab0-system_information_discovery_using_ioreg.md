---
sigma_id: "2d5e7a8b-f484-4a24-945d-7f0efd52eab0"
title: "System Information Discovery Using Ioreg"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_ioreg_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_ioreg_discovery.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "2d5e7a8b-f484-4a24-945d-7f0efd52eab0"
  - "System Information Discovery Using Ioreg"
attack_technique_ids:
  - "T1082"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# System Information Discovery Using Ioreg

Detects the use of "ioreg" which will show I/O Kit registry information.
This process is used for system information discovery.
It has been observed in-the-wild by calling this process directly or using bash and grep to look for specific strings.

## Metadata

- Rule ID: 2d5e7a8b-f484-4a24-945d-7f0efd52eab0
- Status: test
- Level: medium
- Author: Joseliyo Sanchez, @Joseliyo_Jstnk
- Date: 2023-12-20
- Modified: 2024-01-02
- Source Path: rules/macos/process_creation/proc_creation_macos_ioreg_discovery.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Detection

```yaml
selection_img:
- Image|endswith: /ioreg
- CommandLine|contains: ioreg
selection_cmd1:
  CommandLine|contains:
  - -l
  - -c
selection_cmd2:
  CommandLine|contains:
  - AppleAHCIDiskDriver
  - IOPlatformExpertDevice
  - Oracle
  - Parallels
  - USB Vendor Name
  - VirtualBox
  - VMware
condition: all of selection_*
```

## False Positives

- Legitimate administrative activities

## References

- https://www.virustotal.com/gui/file/0373d78db6c3c0f6f6dcc409821bf89e1ad8c165d6f95c5c80ecdce2219627d7/behavior
- https://www.virustotal.com/gui/file/4ffdc72d1ff1ee8228e31691020fc275afd1baee5a985403a71ca8c7bd36e2e4/behavior
- https://www.virustotal.com/gui/file/5907d59ec1303cfb5c0a0f4aaca3efc0830707d86c732ba6b9e842b5730b95dc/behavior
- https://www.trendmicro.com/en_ph/research/20/k/new-macos-backdoor-connected-to-oceanlotus-surfaces.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_ioreg_discovery.yml)
