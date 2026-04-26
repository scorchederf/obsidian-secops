---
sigma_id: "403ed92c-b7ec-4edd-9947-5b535ee12d46"
title: "Crontab Enumeration"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_crontab_enumeration.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_crontab_enumeration.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "low"
logsource: "linux / process_creation"
aliases:
  - "403ed92c-b7ec-4edd-9947-5b535ee12d46"
  - "Crontab Enumeration"
attack_technique_ids:
  - "T1007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Crontab Enumeration

Detects usage of crontab to list the tasks of the user

## Metadata

- Rule ID: 403ed92c-b7ec-4edd-9947-5b535ee12d46
- Status: test
- Level: low
- Author: Joseliyo Sanchez, @Joseliyo_Jstnk
- Date: 2023-06-02
- Source Path: rules/linux/process_creation/proc_creation_lnx_crontab_enumeration.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1007-system_service_discovery|T1007]]

## Detection

```yaml
selection:
  Image|endswith: /crontab
  CommandLine|contains: ' -l'
condition: selection
```

## False Positives

- Legitimate use of crontab

## References

- https://blogs.jpcert.or.jp/en/2023/05/gobrat.html
- https://jstnk9.github.io/jstnk9/research/GobRAT-Malware/
- https://www.virustotal.com/gui/file/60bcd645450e4c846238cf0e7226dc40c84c96eba99f6b2cffcd0ab4a391c8b3/detection
- https://www.virustotal.com/gui/file/3e44c807a25a56f4068b5b8186eee5002eed6f26d665a8b791c472ad154585d1/detection

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_crontab_enumeration.yml)
