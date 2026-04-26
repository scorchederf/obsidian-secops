---
sigma_id: "949f1ffb-6e85-4f00-ae1e-c3c5b190d605"
title: "Explorer Process Tree Break"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_explorer_break_process_tree.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_explorer_break_process_tree.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "949f1ffb-6e85-4f00-ae1e-c3c5b190d605"
  - "Explorer Process Tree Break"
attack_technique_ids:
  - "T1036"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Explorer Process Tree Break

Detects a command line process that uses explorer.exe to launch arbitrary commands or binaries,
which is similar to cmd.exe /c, only it breaks the process tree and makes its parent a new instance of explorer spawning from "svchost"

## Metadata

- Rule ID: 949f1ffb-6e85-4f00-ae1e-c3c5b190d605
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems), @gott_cyber
- Date: 2019-06-29
- Modified: 2025-10-31
- Source Path: rules/windows/process_creation/proc_creation_win_explorer_break_process_tree.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036]]

## Detection

```yaml
selection_factory:
  CommandLine|contains: /factory,{75dff2b7-6936-4c06-a8bb-676a7b00b24b}
selection_root:
  CommandLine|contains: explorer.exe
  CommandLine|contains|windash: ' /root,'
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://twitter.com/CyberRaiju/status/1273597319322058752
- https://twitter.com/bohops/status/1276357235954909188?s=12
- https://twitter.com/nas_bench/status/1535322450858233858
- https://securityboulevard.com/2019/09/deobfuscating-ostap-trickbots-34000-line-javascript-downloader/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_explorer_break_process_tree.yml)
