---
sigma_id: "4bc90587-e6ca-4b41-be0b-ed4d04e4ed0c"
title: "Suspicious Velociraptor Child Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_velociraptor_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_velociraptor_child_process.yml"
build_date: "2026-04-27 19:13:57"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "4bc90587-e6ca-4b41-be0b-ed4d04e4ed0c"
  - "Suspicious Velociraptor Child Process"
attack_technique_ids:
  - "T1219"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the suspicious use of the Velociraptor DFIR tool to execute other tools or download additional payloads, as seen in a campaign where it was abused for remote access and to stage further attacks.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools|T1219: Remote Access Tools]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith: \Velociraptor.exe
selection_child_vscode_tunnel:
  CommandLine|contains|all:
  - code.exe
  - tunnel
  - --accept-server-license-terms
selection_child_msiexec:
  CommandLine|contains|all:
  - msiexec
  - /i
  - http
selection_child_powershell:
  Image|endswith:
  - \powershell.exe
  - \powershell_ise.exe
  - \pwsh.exe
  CommandLine|contains:
  - 'Invoke-WebRequest '
  - 'IWR '
  - .DownloadFile
  - .DownloadString
condition: selection_parent and 1 of selection_child_*
```

## False Positives

- Legitimate administrators or incident responders might use Velociraptor to execute scripts or tools. However, the combination of Velociraptor spawning these specific processes with these command lines is suspicious. Tuning may be required to exclude known administrative actions or specific scripts.

## References

- https://news.sophos.com/en-us/2025/08/26/velociraptor-incident-response-tool-abused-for-remote-access/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_velociraptor_child_process.yml)
