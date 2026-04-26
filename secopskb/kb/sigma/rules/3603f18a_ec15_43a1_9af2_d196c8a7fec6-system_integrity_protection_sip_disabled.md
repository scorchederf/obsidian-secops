---
sigma_id: "3603f18a-ec15-43a1-9af2-d196c8a7fec6"
title: "System Integrity Protection (SIP) Disabled"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_csrutil_disable.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_csrutil_disable.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "3603f18a-ec15-43a1-9af2-d196c8a7fec6"
  - "System Integrity Protection (SIP) Disabled"
attack_technique_ids:
  - "T1518.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# System Integrity Protection (SIP) Disabled

Detects the use of csrutil to disable the Configure System Integrity Protection (SIP). This technique is used in post-exploit scenarios.

## Metadata

- Rule ID: 3603f18a-ec15-43a1-9af2-d196c8a7fec6
- Status: test
- Level: medium
- Author: Joseliyo Sanchez, @Joseliyo_Jstnk
- Date: 2024-01-02
- Source Path: rules/macos/process_creation/proc_creation_macos_csrutil_disable.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1518-software_discovery|T1518.001]]

## Detection

```yaml
selection:
  Image|endswith: /csrutil
  CommandLine|contains: disable
condition: selection
```

## False Positives

- Unknown

## References

- https://ss64.com/osx/csrutil.html
- https://objective-see.org/blog/blog_0x6D.html
- https://www.welivesecurity.com/2017/10/20/osx-proton-supply-chain-attack-elmedia/
- https://www.virustotal.com/gui/file/05a2adb266ec6c0ba9ed176d87d8530e71e845348c13caf9f60049760c312cd3/behavior

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_csrutil_disable.yml)
