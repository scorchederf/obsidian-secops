---
sigma_id: "85de3a19-b675-4a51-bfc6-b11a5186c971"
title: "Potential Discovery Activity Using Find - MacOS"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_susp_find_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_susp_find_execution.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "85de3a19-b675-4a51-bfc6-b11a5186c971"
  - "Potential Discovery Activity Using Find - MacOS"
attack_technique_ids:
  - "T1083"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Discovery Activity Using Find - MacOS

Detects usage of "find" binary in a suspicious manner to perform discovery

## Metadata

- Rule ID: 85de3a19-b675-4a51-bfc6-b11a5186c971
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-12-28
- Source Path: rules/macos/process_creation/proc_creation_macos_susp_find_execution.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1083-file_and_directory_discovery|T1083]]

## Detection

```yaml
selection:
  Image|endswith: /find
  CommandLine|contains:
  - -perm -4000
  - -perm -2000
  - -perm 0777
  - -perm -222
  - -perm -o w
  - -perm -o x
  - -perm -u=s
  - -perm -g=s
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/SaiSathvik1/Linux-Privilege-Escalation-Notes

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_susp_find_execution.yml)
