---
sigma_id: "00eee2a5-fdb0-4746-a21d-e43fbdea5681"
title: "Linux Doas Conf File Creation"
framework: "sigma"
generated: "true"
source_path: "rules/linux/file_event/file_event_lnx_doas_conf_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/file_event/file_event_lnx_doas_conf_creation.yml"
build_date: "2026-04-26 14:14:28"
status: "stable"
level: "medium"
logsource: "linux / file_event"
aliases:
  - "00eee2a5-fdb0-4746-a21d-e43fbdea5681"
  - "Linux Doas Conf File Creation"
attack_technique_ids:
  - "T1548"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Linux Doas Conf File Creation

Detects the creation of doas.conf file in linux host platform.

## Metadata

- Rule ID: 00eee2a5-fdb0-4746-a21d-e43fbdea5681
- Status: stable
- Level: medium
- Author: Sittikorn S, Teoderick Contreras
- Date: 2022-01-20
- Modified: 2022-12-31
- Source Path: rules/linux/file_event/file_event_lnx_doas_conf_creation.yml

## Logsource

- category: file_event
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548]]

## Detection

```yaml
selection:
  TargetFilename|endswith: /etc/doas.conf
condition: selection
```

## False Positives

- Unlikely

## References

- https://research.splunk.com/endpoint/linux_doas_conf_file_creation/
- https://www.makeuseof.com/how-to-install-and-use-doas/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/file_event/file_event_lnx_doas_conf_creation.yml)
