---
sigma_id: "3a8da4e0-36c1-40d2-8b29-b3e890d5172a"
title: "NTDS Exfiltration Filename Patterns"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_ntds_exfil_tools.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_ntds_exfil_tools.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "3a8da4e0-36c1-40d2-8b29-b3e890d5172a"
  - "NTDS Exfiltration Filename Patterns"
attack_technique_ids:
  - "T1003.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# NTDS Exfiltration Filename Patterns

Detects creation of files with specific name patterns seen used in various tools that export the NTDS.DIT for exfiltration.

## Metadata

- Rule ID: 3a8da4e0-36c1-40d2-8b29-b3e890d5172a
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-03-11
- Modified: 2023-05-05
- Source Path: rules/windows/file/file_event/file_event_win_ntds_exfil_tools.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]

## Detection

```yaml
selection:
  TargetFilename|endswith:
  - \All.cab
  - .ntds.cleartext
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/rapid7/metasploit-framework/blob/eb6535009f5fdafa954525687f09294918b5398d/modules/post/windows/gather/ntds_grabber.rb
- https://github.com/rapid7/metasploit-framework/blob/eb6535009f5fdafa954525687f09294918b5398d/data/post/powershell/NTDSgrab.ps1
- https://github.com/SecureAuthCorp/impacket/blob/7d2991d78836b376452ca58b3d14daa61b67cb40/impacket/examples/secretsdump.py#L2405

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_ntds_exfil_tools.yml)
