---
sigma_id: "7f3a9c2d-4e8b-4a7f-9d3e-5c6f8a9b2e1d"
title: "OpenEDR Spawning Command Shell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_comodo_ssh_shellhost_cmd_spawn.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_comodo_ssh_shellhost_cmd_spawn.yml"
build_date: "2026-04-26 14:14:30"
status: "experimental"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "7f3a9c2d-4e8b-4a7f-9d3e-5c6f8a9b2e1d"
  - "OpenEDR Spawning Command Shell"
attack_technique_ids:
  - "T1059.003"
  - "T1021.004"
  - "T1219"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# OpenEDR Spawning Command Shell

Detects the OpenEDR ssh-shellhost.exe spawning a command shell (cmd.exe) or PowerShell with PTY (pseudo-terminal) capabilities.
This may indicate remote command execution through OpenEDR's remote management features, which could be legitimate administrative activity or potential abuse of the remote access tool.
Threat actors may leverage OpenEDR's remote shell capabilities to execute commands on compromised systems, facilitating lateral movement or other command-and-control operations.

## Metadata

- Rule ID: 7f3a9c2d-4e8b-4a7f-9d3e-5c6f8a9b2e1d
- Status: experimental
- Level: medium
- Author: @kostastsale
- Date: 2026-02-19
- Source Path: rules/windows/process_creation/proc_creation_win_comodo_ssh_shellhost_cmd_spawn.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.003]]
- [[kb/attack/techniques/T1021-remote_services|T1021.004]]
- [[kb/attack/techniques/T1219-remote_access_tools|T1219]]

## Detection

```yaml
selection_img:
  ParentImage|endswith: \ITSMService.exe
  Image|endswith: \ssh-shellhost.exe
  CommandLine|contains: --pty
selection_cli_shell:
  CommandLine|contains:
  - bash
  - cmd
  - powershell
  - pwsh
condition: all of selection_*
```

## False Positives

- Legitimate use of OpenEDR for remote command execution

## References

- https://kostas-ts.medium.com/detecting-abuse-of-openedrs-permissive-edr-trial-a-security-researcher-s-perspective-fc55bf53972c

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_comodo_ssh_shellhost_cmd_spawn.yml)
