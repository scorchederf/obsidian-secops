---
sigma_id: "53821412-17b0-4147-ade0-14faae67d54b"
title: "System Integrity Protection (SIP) Enumeration"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_csrutil_status.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_csrutil_status.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "low"
logsource: "macos / process_creation"
aliases:
  - "53821412-17b0-4147-ade0-14faae67d54b"
  - "System Integrity Protection (SIP) Enumeration"
attack_technique_ids:
  - "T1518.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# System Integrity Protection (SIP) Enumeration

Detects the use of csrutil to view the Configure System Integrity Protection (SIP) status. This technique is used in post-exploit scenarios.

## Metadata

- Rule ID: 53821412-17b0-4147-ade0-14faae67d54b
- Status: test
- Level: low
- Author: Joseliyo Sanchez, @Joseliyo_Jstnk
- Date: 2024-01-02
- Source Path: rules/macos/process_creation/proc_creation_macos_csrutil_status.yml

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
  CommandLine|contains: status
condition: selection
```

## False Positives

- Legitimate administration activities

## References

- https://ss64.com/osx/csrutil.html
- https://objective-see.org/blog/blog_0x6D.html
- https://www.welivesecurity.com/2017/10/20/osx-proton-supply-chain-attack-elmedia/
- https://www.virustotal.com/gui/file/05a2adb266ec6c0ba9ed176d87d8530e71e845348c13caf9f60049760c312cd3/behavior

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_csrutil_status.yml)
