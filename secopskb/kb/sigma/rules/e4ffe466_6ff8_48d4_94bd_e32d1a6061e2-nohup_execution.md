---
sigma_id: "e4ffe466-6ff8-48d4-94bd-e32d1a6061e2"
title: "Nohup Execution"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_nohup.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_nohup.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "e4ffe466-6ff8-48d4-94bd-e32d1a6061e2"
  - "Nohup Execution"
attack_technique_ids:
  - "T1059.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Nohup Execution

Detects usage of nohup which could be leveraged by an attacker to keep a process running or break out from restricted environments

## Metadata

- Rule ID: e4ffe466-6ff8-48d4-94bd-e32d1a6061e2
- Status: test
- Level: medium
- Author: Christopher Peacock @SecurePeacock, SCYTHE @scythe_io
- Date: 2022-06-06
- Source Path: rules/linux/process_creation/proc_creation_lnx_nohup.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.004]]

## Detection

```yaml
selection:
  Image|endswith: /nohup
condition: selection
```

## False Positives

- Administrators or installed processes that leverage nohup

## References

- https://gtfobins.github.io/gtfobins/nohup/
- https://en.wikipedia.org/wiki/Nohup
- https://www.computerhope.com/unix/unohup.htm

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_nohup.yml)
