---
sigma_id: "dc4576d4-7467-424f-9eee-fd2b02855fe0"
title: "Suspicious Cabinet File Execution Via Msdt.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_msdt_susp_cab_options.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msdt_susp_cab_options.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "dc4576d4-7467-424f-9eee-fd2b02855fe0"
  - "Suspicious Cabinet File Execution Via Msdt.EXE"
attack_technique_ids:
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Cabinet File Execution Via Msdt.EXE

Detects execution of msdt.exe using the "cab" flag which could indicates suspicious diagcab files with embedded answer files leveraging CVE-2022-30190

## Metadata

- Rule ID: dc4576d4-7467-424f-9eee-fd2b02855fe0
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), GossiTheDog, frack113
- Date: 2022-06-21
- Modified: 2024-03-13
- Source Path: rules/windows/process_creation/proc_creation_win_msdt_susp_cab_options.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detection

```yaml
selection_img:
- Image|endswith: \msdt.exe
- OriginalFileName: msdt.exe
selection_cmd:
  CommandLine|contains|windash: ' -cab '
condition: all of selection_*
```

## False Positives

- Legitimate usage of ".diagcab" files

## References

- https://twitter.com/nas_bench/status/1537896324837781506
- https://github.com/GossiTheDog/ThreatHunting/blob/e85884abbf05d5b41efc809ea6532b10b45bd05c/AdvancedHuntingQueries/DogWalk-DiagCab
- https://github.com/elastic/protections-artifacts/commit/746086721fd385d9f5c6647cada1788db4aea95f#diff-9015912909545e72ed42cbac4d1e96295e8964579c406d23fd9c47a8091576a0
- https://irsl.medium.com/the-trouble-with-microsofts-troubleshooters-6e32fc80b8bd

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msdt_susp_cab_options.yml)
