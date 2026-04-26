---
sigma_id: "bb382fd5-b454-47ea-a264-1828e4c766d6"
title: "Shell Invocation via Apt - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_apt_shell_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_apt_shell_execution.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "bb382fd5-b454-47ea-a264-1828e4c766d6"
  - "Shell Invocation via Apt - Linux"
attack_technique_ids:
  - "T1083"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Shell Invocation via Apt - Linux

Detects the use of the "apt" and "apt-get" commands to execute a shell or proxy commands.
Such behavior may be associated with privilege escalation, unauthorized command execution, or to break out from restricted environments.

## Metadata

- Rule ID: bb382fd5-b454-47ea-a264-1828e4c766d6
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-12-28
- Modified: 2024-09-02
- Source Path: rules/linux/process_creation/proc_creation_lnx_apt_shell_execution.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1083-file_and_directory_discovery|T1083]]

## Detection

```yaml
selection:
  Image|endswith:
  - /apt
  - /apt-get
  CommandLine|contains: APT::Update::Pre-Invoke::=
condition: selection
```

## False Positives

- Unknown

## References

- https://gtfobins.github.io/gtfobins/apt/
- https://gtfobins.github.io/gtfobins/apt-get/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_apt_shell_execution.yml)
