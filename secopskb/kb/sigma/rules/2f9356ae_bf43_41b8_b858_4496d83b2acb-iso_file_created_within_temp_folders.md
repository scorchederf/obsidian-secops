---
sigma_id: "2f9356ae-bf43-41b8-b858-4496d83b2acb"
title: "ISO File Created Within Temp Folders"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_iso_file_mount.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_iso_file_mount.yml"
build_date: "2026-04-27 19:13:52"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "2f9356ae-bf43-41b8-b858-4496d83b2acb"
  - "ISO File Created Within Temp Folders"
attack_technique_ids:
  - "T1566.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the creation of a ISO file in the Outlook temp folder or in the Appdata temp folder. Typical of Qakbot TTP from end-July 2022.

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1566-phishing#^t1566001-spearphishing-attachment|T1566.001: Spearphishing Attachment]]

## Detection

```yaml
selection_1:
  TargetFilename|contains|all:
  - \AppData\Local\Temp\
  - .zip\
  TargetFilename|endswith: .iso
selection_2:
  TargetFilename|contains: \AppData\Local\Microsoft\Windows\INetCache\Content.Outlook\
  TargetFilename|endswith: .iso
condition: 1 of selection*
```

## False Positives

- Potential FP by sysadmin opening a zip file containing a legitimate ISO file

## References

- https://twitter.com/Sam0x90/status/1552011547974696960
- https://securityaffairs.co/wordpress/133680/malware/dll-sideloading-spread-qakbot.html
- https://github.com/redcanaryco/atomic-red-team/blob/0f229c0e42bfe7ca736a14023836d65baa941ed2/atomics/T1553.005/T1553.005.md#atomic-test-1---mount-iso-image

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_iso_file_mount.yml)
