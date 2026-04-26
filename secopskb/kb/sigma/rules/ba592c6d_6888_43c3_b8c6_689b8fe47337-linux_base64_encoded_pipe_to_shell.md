---
sigma_id: "ba592c6d-6888-43c3-b8c6-689b8fe47337"
title: "Linux Base64 Encoded Pipe to Shell"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_base64_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_base64_execution.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "ba592c6d-6888-43c3-b8c6-689b8fe47337"
  - "Linux Base64 Encoded Pipe to Shell"
attack_technique_ids:
  - "T1140"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Linux Base64 Encoded Pipe to Shell

Detects suspicious process command line that uses base64 encoded input for execution with a shell

## Metadata

- Rule ID: ba592c6d-6888-43c3-b8c6-689b8fe47337
- Status: test
- Level: medium
- Author: pH-T (Nextron Systems)
- Date: 2022-07-26
- Modified: 2023-06-16
- Source Path: rules/linux/process_creation/proc_creation_lnx_base64_execution.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1140-deobfuscate_decode_files_or_information|T1140]]

## Detection

```yaml
selection_base64:
  CommandLine|contains: 'base64 '
selection_exec:
- CommandLine|contains:
  - '| bash '
  - '| sh '
  - '|bash '
  - '|sh '
- CommandLine|endswith:
  - ' |sh'
  - '| bash'
  - '| sh'
  - '|bash'
condition: all of selection_*
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/arget13/DDexec
- https://www.mandiant.com/resources/blog/barracuda-esg-exploited-globally

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_base64_execution.yml)
