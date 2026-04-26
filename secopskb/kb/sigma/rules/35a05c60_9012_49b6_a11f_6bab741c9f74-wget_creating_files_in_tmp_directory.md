---
sigma_id: "35a05c60-9012-49b6-a11f-6bab741c9f74"
title: "Wget Creating Files in Tmp Directory"
framework: "sigma"
generated: "true"
source_path: "rules/linux/file_event/file_event_lnx_wget_download_file_in_tmp_dir.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/file_event/file_event_lnx_wget_download_file_in_tmp_dir.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "linux / file_event"
aliases:
  - "35a05c60-9012-49b6-a11f-6bab741c9f74"
  - "Wget Creating Files in Tmp Directory"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Wget Creating Files in Tmp Directory

Detects the use of wget to download content in a temporary directory such as "/tmp" or "/var/tmp"

## Metadata

- Rule ID: 35a05c60-9012-49b6-a11f-6bab741c9f74
- Status: test
- Level: medium
- Author: Joseliyo Sanchez, @Joseliyo_Jstnk
- Date: 2023-06-02
- Source Path: rules/linux/file_event/file_event_lnx_wget_download_file_in_tmp_dir.yml

## Logsource

- category: file_event
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection:
  Image|endswith: /wget
  TargetFilename|startswith:
  - /tmp/
  - /var/tmp/
condition: selection
```

## False Positives

- Legitimate downloads of files in the tmp folder.

## References

- https://blogs.jpcert.or.jp/en/2023/05/gobrat.html
- https://jstnk9.github.io/jstnk9/research/GobRAT-Malware/
- https://www.virustotal.com/gui/file/60bcd645450e4c846238cf0e7226dc40c84c96eba99f6b2cffcd0ab4a391c8b3/detection
- https://www.virustotal.com/gui/file/3e44c807a25a56f4068b5b8186eee5002eed6f26d665a8b791c472ad154585d1/detection

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/file_event/file_event_lnx_wget_download_file_in_tmp_dir.yml)
