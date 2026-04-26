---
sigma_id: "e34cfa0c-0a50-4210-9cb3-5632d08eb041"
title: "Potential GobRAT File Discovery Via Grep"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_malware_gobrat_grep_payload_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_malware_gobrat_grep_payload_discovery.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "e34cfa0c-0a50-4210-9cb3-5632d08eb041"
  - "Potential GobRAT File Discovery Via Grep"
attack_technique_ids:
  - "T1082"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential GobRAT File Discovery Via Grep

Detects the use of grep to discover specific files created by the GobRAT malware

## Metadata

- Rule ID: e34cfa0c-0a50-4210-9cb3-5632d08eb041
- Status: test
- Level: high
- Author: Joseliyo Sanchez, @Joseliyo_Jstnk
- Date: 2023-06-02
- Source Path: rules/linux/process_creation/proc_creation_lnx_malware_gobrat_grep_payload_discovery.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Detection

```yaml
selection:
  Image|endswith: /grep
  CommandLine|contains:
  - apached
  - frpc
  - sshd.sh
  - zone.arm
condition: selection
```

## False Positives

- Unknown

## References

- https://blogs.jpcert.or.jp/en/2023/05/gobrat.html
- https://www.virustotal.com/gui/file/60bcd645450e4c846238cf0e7226dc40c84c96eba99f6b2cffcd0ab4a391c8b3/detection
- https://www.virustotal.com/gui/file/3e44c807a25a56f4068b5b8186eee5002eed6f26d665a8b791c472ad154585d1/detection

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_malware_gobrat_grep_payload_discovery.yml)
