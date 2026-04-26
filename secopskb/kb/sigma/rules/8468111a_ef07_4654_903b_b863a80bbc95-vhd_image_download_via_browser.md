---
sigma_id: "8468111a-ef07-4654-903b-b863a80bbc95"
title: "VHD Image Download Via Browser"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_vhd_download_via_browsers.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_vhd_download_via_browsers.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "8468111a-ef07-4654-903b-b863a80bbc95"
  - "VHD Image Download Via Browser"
attack_technique_ids:
  - "T1587.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# VHD Image Download Via Browser

Detects creation of ".vhd"/".vhdx" files by browser processes.
Malware can use mountable Virtual Hard Disk ".vhd" files to encapsulate payloads and evade security controls.

## Metadata

- Rule ID: 8468111a-ef07-4654-903b-b863a80bbc95
- Status: test
- Level: medium
- Author: frack113, Christopher Peacock '@securepeacock', SCYTHE '@scythe_io'
- Date: 2021-10-25
- Modified: 2023-05-05
- Source Path: rules/windows/file/file_event/file_event_win_vhd_download_via_browsers.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1587-develop_capabilities|T1587.001]]

## Detection

```yaml
selection:
  Image|endswith:
  - \brave.exe
  - \chrome.exe
  - \firefox.exe
  - \iexplore.exe
  - \maxthon.exe
  - \MicrosoftEdge.exe
  - \msedge.exe
  - \msedgewebview2.exe
  - \opera.exe
  - \safari.exe
  - \seamonkey.exe
  - \vivaldi.exe
  - \whale.exe
  TargetFilename|contains: .vhd
condition: selection
```

## False Positives

- Legitimate downloads of ".vhd" files would also trigger this

## References

- https://redcanary.com/blog/intelligence-insights-october-2021/
- https://www.kaspersky.com/blog/lazarus-vhd-ransomware/36559/
- https://securelist.com/lazarus-on-the-hunt-for-big-game/97757/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_vhd_download_via_browsers.yml)
