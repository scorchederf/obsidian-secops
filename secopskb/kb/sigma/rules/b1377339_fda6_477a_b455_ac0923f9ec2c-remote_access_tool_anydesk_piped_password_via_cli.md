---
sigma_id: "b1377339-fda6-477a-b455-ac0923f9ec2c"
title: "Remote Access Tool - AnyDesk Piped Password Via CLI"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_remote_access_tools_anydesk_piped_password_via_cli.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_anydesk_piped_password_via_cli.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "b1377339-fda6-477a-b455-ac0923f9ec2c"
  - "Remote Access Tool - AnyDesk Piped Password Via CLI"
attack_technique_ids:
  - "T1219.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Access Tool - AnyDesk Piped Password Via CLI

Detects piping the password to an anydesk instance via CMD and the '--set-password' flag.

## Metadata

- Rule ID: b1377339-fda6-477a-b455-ac0923f9ec2c
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-09-28
- Modified: 2023-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_remote_access_tools_anydesk_piped_password_via_cli.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools|T1219.002]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - '/c '
  - 'echo '
  - .exe --set-password
condition: selection
```

## False Positives

- Legitimate piping of the password to anydesk
- Some FP could occur with similar tools that uses the same command line '--set-password'

## References

- https://redcanary.com/blog/misbehaving-rats/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_anydesk_piped_password_via_cli.yml)
