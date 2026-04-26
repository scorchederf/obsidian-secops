---
sigma_id: "7638e5fe-600c-4289-a968-f49dd537ec7d"
title: "HackTool - NetExec Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_netexec.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_netexec.yml"
build_date: "2026-04-26 14:14:26"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "7638e5fe-600c-4289-a968-f49dd537ec7d"
  - "HackTool - NetExec Execution"
attack_technique_ids:
  - "T1018"
  - "T1021"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# HackTool - NetExec Execution

Detects execution of the hacktool NetExec.
NetExec (formerly CrackMapExec) is a widely used post-exploitation tool designed for Active Directory penetration testing and network enumeration
In enterprise environments, the use of NetExec is considered suspicious or potentially malicious because it enables attackers to enumerate hosts, exploit network services, and move laterally across systems.
Threat actors and red teams commonly use NetExec to identify vulnerable systems, harvest credentials, and execute commands remotely.

## Metadata

- Rule ID: 7638e5fe-600c-4289-a968-f49dd537ec7d
- Status: experimental
- Level: high
- Author: Chirag Damani
- Date: 2026-03-29
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_netexec.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1018-remote_system_discovery|T1018]]
- [[kb/attack/techniques/T1021-remote_services|T1021]]

## Detection

```yaml
selection:
  Image|endswith: \nxc.exe
  CommandLine|contains:
  - ' ftp '
  - ' ldap '
  - ' mssql '
  - ' nfs '
  - ' rdp '
  - ' smb '
  - ' ssh '
  - ' vnc '
  - ' winrm '
  - ' wmi '
condition: selection
```

## False Positives

- Legitimate use of NetExec by security professionals or system administrators for network assessment and management.

## References

- https://thedfirreport.com/2025/12/17/cats-got-your-files-lynx-ransomware/
- https://github.com/Pennyw0rth/NetExec
- https://www.netexec.wiki/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_netexec.yml)
