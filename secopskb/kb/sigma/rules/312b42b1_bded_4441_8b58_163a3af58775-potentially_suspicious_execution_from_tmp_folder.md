---
sigma_id: "312b42b1-bded-4441-8b58-163a3af58775"
title: "Potentially Suspicious Execution From Tmp Folder"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_susp_execution_tmp_folder.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_execution_tmp_folder.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "312b42b1-bded-4441-8b58-163a3af58775"
  - "Potentially Suspicious Execution From Tmp Folder"
attack_technique_ids:
  - "T1036"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious Execution From Tmp Folder

Detects a potentially suspicious execution of a process located in the '/tmp/' folder

## Metadata

- Rule ID: 312b42b1-bded-4441-8b58-163a3af58775
- Status: test
- Level: medium
- Author: Joseliyo Sanchez, @Joseliyo_Jstnk
- Date: 2023-06-02
- Modified: 2025-08-05
- Source Path: rules/linux/process_creation/proc_creation_lnx_susp_execution_tmp_folder.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036]]

## Detection

```yaml
selection:
  Image|startswith: /tmp/
filter_optional_nextcloud:
  Image|endswith: /usr/bin/nextcloud
condition: selection and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://blogs.jpcert.or.jp/en/2023/05/gobrat.html
- https://jstnk9.github.io/jstnk9/research/GobRAT-Malware/
- https://www.virustotal.com/gui/file/60bcd645450e4c846238cf0e7226dc40c84c96eba99f6b2cffcd0ab4a391c8b3/detection
- https://www.virustotal.com/gui/file/3e44c807a25a56f4068b5b8186eee5002eed6f26d665a8b791c472ad154585d1/detection

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_execution_tmp_folder.yml)
