---
sigma_id: "4358e5a5-7542-4dcb-b9f3-87667371839b"
title: "ISO or Image Mount Indicator in Recent Files"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_iso_file_recent.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_iso_file_recent.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "4358e5a5-7542-4dcb-b9f3-87667371839b"
  - "ISO or Image Mount Indicator in Recent Files"
attack_technique_ids:
  - "T1566.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# ISO or Image Mount Indicator in Recent Files

Detects the creation of recent element file that points to an .ISO, .IMG, .VHD or .VHDX file as often used in phishing attacks.
This can be a false positive on server systems but on workstations users should rarely mount .iso or .img files.

## Metadata

- Rule ID: 4358e5a5-7542-4dcb-b9f3-87667371839b
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2022-02-11
- Source Path: rules/windows/file/file_event/file_event_win_iso_file_recent.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1566-phishing|T1566.001]]

## Detection

```yaml
selection:
  TargetFilename|endswith:
  - .iso.lnk
  - .img.lnk
  - .vhd.lnk
  - .vhdx.lnk
  TargetFilename|contains: \Microsoft\Windows\Recent\
condition: selection
```

## False Positives

- Cases in which a user mounts an image file for legitimate reasons

## References

- https://www.microsoft.com/security/blog/2021/05/27/new-sophisticated-email-based-attack-from-nobelium/
- https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/malicious-spam-campaign-uses-iso-image-files-to-deliver-lokibot-and-nanocore
- https://blog.emsisoft.com/en/32373/beware-new-wave-of-malware-spreads-via-iso-file-email-attachments/
- https://insights.sei.cmu.edu/blog/the-dangers-of-vhd-and-vhdx-files/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_iso_file_recent.yml)
