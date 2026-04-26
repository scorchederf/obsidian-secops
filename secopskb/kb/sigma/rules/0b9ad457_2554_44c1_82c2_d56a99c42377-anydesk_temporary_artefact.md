---
sigma_id: "0b9ad457-2554-44c1-82c2-d56a99c42377"
title: "Anydesk Temporary Artefact"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_anydesk_artefact.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_anydesk_artefact.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "0b9ad457-2554-44c1-82c2-d56a99c42377"
  - "Anydesk Temporary Artefact"
attack_technique_ids:
  - "T1219.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Anydesk Temporary Artefact

An adversary may use legitimate desktop support and remote access software, such as Team Viewer, Go2Assist, LogMein, AmmyyAdmin, etc, to establish an interactive command and control channel to target systems within networks.
These services are commonly used as legitimate technical support software, and may be allowed by application control within a target environment.
Remote access tools like VNC, Ammyy, and Teamviewer are used frequently when compared with other legitimate software commonly used by adversaries. (Citation: Symantec Living off the Land)

## Metadata

- Rule ID: 0b9ad457-2554-44c1-82c2-d56a99c42377
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-02-11
- Modified: 2024-07-20
- Source Path: rules/windows/file/file_event/file_event_win_anydesk_artefact.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools|T1219.002]]

## Detection

```yaml
selection:
  TargetFilename|contains:
  - \AppData\Roaming\AnyDesk\user.conf
  - \AppData\Roaming\AnyDesk\system.conf
condition: selection
```

## False Positives

- Legitimate use

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1219/T1219.md#atomic-test-2---anydesk-files-detected-test-on-windows

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_anydesk_artefact.yml)
