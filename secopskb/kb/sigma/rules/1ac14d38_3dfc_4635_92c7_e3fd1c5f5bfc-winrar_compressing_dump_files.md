---
sigma_id: "1ac14d38-3dfc-4635-92c7-e3fd1c5f5bfc"
title: "Winrar Compressing Dump Files"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_winrar_exfil_dmp_files.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_winrar_exfil_dmp_files.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "1ac14d38-3dfc-4635-92c7-e3fd1c5f5bfc"
  - "Winrar Compressing Dump Files"
attack_technique_ids:
  - "T1560.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Winrar Compressing Dump Files

Detects execution of WinRAR in order to compress a file with a ".dmp"/".dump" extension, which could be a step in a process of dump file exfiltration.

## Metadata

- Rule ID: 1ac14d38-3dfc-4635-92c7-e3fd1c5f5bfc
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2022-01-04
- Modified: 2023-09-12
- Source Path: rules/windows/process_creation/proc_creation_win_winrar_exfil_dmp_files.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1560-archive_collected_data|T1560.001]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \rar.exe
  - \winrar.exe
- Description: Command line RAR
selection_extension:
  CommandLine|contains:
  - .dmp
  - .dump
  - .hdmp
condition: all of selection_*
```

## False Positives

- Legitimate use of WinRAR with a command line in which ".dmp" or ".dump" appears accidentally
- Legitimate use of WinRAR to compress WER ".dmp" files for troubleshooting

## References

- https://www.crowdstrike.com/blog/overwatch-exposes-aquatic-panda-in-possession-of-log-4-shell-exploit-tools/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_winrar_exfil_dmp_files.yml)
