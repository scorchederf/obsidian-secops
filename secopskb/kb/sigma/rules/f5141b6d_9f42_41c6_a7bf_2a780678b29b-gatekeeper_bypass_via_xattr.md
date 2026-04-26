---
sigma_id: "f5141b6d-9f42-41c6-a7bf-2a780678b29b"
title: "Gatekeeper Bypass via Xattr"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_xattr_gatekeeper_bypass.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_xattr_gatekeeper_bypass.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "low"
logsource: "macos / process_creation"
aliases:
  - "f5141b6d-9f42-41c6-a7bf-2a780678b29b"
  - "Gatekeeper Bypass via Xattr"
attack_technique_ids:
  - "T1553.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Gatekeeper Bypass via Xattr

Detects macOS Gatekeeper bypass via xattr utility

## Metadata

- Rule ID: f5141b6d-9f42-41c6-a7bf-2a780678b29b
- Status: test
- Level: low
- Author: Daniil Yugoslavskiy, oscd.community
- Date: 2020-10-19
- Modified: 2024-04-18
- Source Path: rules/macos/process_creation/proc_creation_macos_xattr_gatekeeper_bypass.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1553-subvert_trust_controls|T1553.001]]

## Detection

```yaml
selection:
  Image|endswith: /xattr
  CommandLine|contains|all:
  - -d
  - com.apple.quarantine
condition: selection
```

## False Positives

- Legitimate activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/1fed40dc7e48f16ed44dcdd9c73b9222a70cca85/atomics/T1553.001/T1553.001.md
- https://www.loobins.io/binaries/xattr/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_xattr_gatekeeper_bypass.yml)
