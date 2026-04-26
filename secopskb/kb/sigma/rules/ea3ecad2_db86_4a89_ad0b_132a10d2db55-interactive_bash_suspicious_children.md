---
sigma_id: "ea3ecad2-db86-4a89-ad0b-132a10d2db55"
title: "Interactive Bash Suspicious Children"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_susp_interactive_bash.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_interactive_bash.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "ea3ecad2-db86-4a89-ad0b-132a10d2db55"
  - "Interactive Bash Suspicious Children"
attack_technique_ids:
  - "T1059.004"
  - "T1036"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Interactive Bash Suspicious Children

Detects suspicious interactive bash as a parent to rather uncommon child processes

## Metadata

- Rule ID: ea3ecad2-db86-4a89-ad0b-132a10d2db55
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2022-03-14
- Source Path: rules/linux/process_creation/proc_creation_lnx_susp_interactive_bash.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.004]]
- [[kb/attack/techniques/T1036-masquerading|T1036]]

## Detection

```yaml
selection:
  ParentCommandLine: bash -i
anomaly1:
  CommandLine|contains:
  - '-c import '
  - base64
  - pty.spawn
anomaly2:
  Image|endswith:
  - whoami
  - iptables
  - /ncat
  - /nc
  - /netcat
condition: selection and 1 of anomaly*
```

## False Positives

- Legitimate software that uses these patterns

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_interactive_bash.yml)
