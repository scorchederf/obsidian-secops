---
sigma_id: "cf610c15-ed71-46e1-bdf8-2bd1a99de6c4"
title: "Download File To Potentially Suspicious Directory Via Wget"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_wget_download_suspicious_directory.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_wget_download_suspicious_directory.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "cf610c15-ed71-46e1-bdf8-2bd1a99de6c4"
  - "Download File To Potentially Suspicious Directory Via Wget"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Download File To Potentially Suspicious Directory Via Wget

Detects the use of wget to download content to a suspicious directory

## Metadata

- Rule ID: cf610c15-ed71-46e1-bdf8-2bd1a99de6c4
- Status: test
- Level: medium
- Author: Joseliyo Sanchez, @Joseliyo_Jstnk
- Date: 2023-06-02
- Source Path: rules/linux/process_creation/proc_creation_lnx_wget_download_suspicious_directory.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection_img:
  Image|endswith: /wget
selection_output:
- CommandLine|re: \s-O\s
- CommandLine|contains: --output-document
selection_path:
  CommandLine|contains: /tmp/
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://blogs.jpcert.or.jp/en/2023/05/gobrat.html
- https://jstnk9.github.io/jstnk9/research/GobRAT-Malware/
- https://www.virustotal.com/gui/file/60bcd645450e4c846238cf0e7226dc40c84c96eba99f6b2cffcd0ab4a391c8b3/detection
- https://www.virustotal.com/gui/file/3e44c807a25a56f4068b5b8186eee5002eed6f26d665a8b791c472ad154585d1/detection

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_wget_download_suspicious_directory.yml)
