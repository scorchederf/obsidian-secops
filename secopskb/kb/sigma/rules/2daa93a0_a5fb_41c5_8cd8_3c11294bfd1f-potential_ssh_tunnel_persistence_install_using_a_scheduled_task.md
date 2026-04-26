---
sigma_id: "2daa93a0-a5fb-41c5-8cd8-3c11294bfd1f"
title: "Potential SSH Tunnel Persistence Install Using A Scheduled Task"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_schtasks_openssh_tunnelling.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_openssh_tunnelling.yml"
build_date: "2026-04-26 17:03:21"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "2daa93a0-a5fb-41c5-8cd8-3c11294bfd1f"
  - "Potential SSH Tunnel Persistence Install Using A Scheduled Task"
attack_technique_ids:
  - "T1053.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential SSH Tunnel Persistence Install Using A Scheduled Task

Detects the creation of new scheduled tasks via commandline, using Schtasks.exe. This rule detects tasks creating that call OpenSSH, which may indicate the creation of reverse SSH tunnel to the attacker's server.

## Metadata

- Rule ID: 2daa93a0-a5fb-41c5-8cd8-3c11294bfd1f
- Status: experimental
- Level: high
- Author: Rory Duncan
- Date: 2025-07-14
- Source Path: rules/windows/process_creation/proc_creation_win_schtasks_openssh_tunnelling.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]

## Detection

```yaml
selection_img:
- Image|endswith: \schtasks.exe
- OriginalFileName: schtasks.exe
selection_cli_sshd:
  CommandLine|contains|all:
  - ' /create '
  - sshd.exe
  - -f
selection_cli_ssh:
  CommandLine|contains|all:
  - ' /create '
  - ssh.exe
  - -i
condition: selection_img and 1 of selection_cli_*
```

## False Positives

- Unknown

## References

- https://thedfirreport.com/2023/10/30/netsupport-intrusion-results-in-domain-compromise/
- https://www.kroll.com/en/insights/publications/cyber/cactus-ransomware-prickly-new-variant-evades-detection

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_openssh_tunnelling.yml)
