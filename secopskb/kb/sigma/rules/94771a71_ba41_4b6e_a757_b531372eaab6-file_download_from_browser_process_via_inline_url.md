---
sigma_id: "94771a71-ba41-4b6e-a757-b531372eaab6"
title: "File Download From Browser Process Via Inline URL"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_browsers_inline_file_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_browsers_inline_file_download.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "94771a71-ba41-4b6e-a757-b531372eaab6"
  - "File Download From Browser Process Via Inline URL"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# File Download From Browser Process Via Inline URL

Detects execution of a browser process with a URL argument pointing to a file with a potentially interesting extension. This can be abused to download arbitrary files or to hide from the user for example by launching the browser in a minimized state.

## Metadata

- Rule ID: 94771a71-ba41-4b6e-a757-b531372eaab6
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-01-11
- Modified: 2025-10-27
- Source Path: rules/windows/process_creation/proc_creation_win_browsers_inline_file_download.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection_img:
  Image|endswith:
  - \brave.exe
  - \chrome.exe
  - \msedge.exe
  - \opera.exe
  - \vivaldi.exe
selection_http:
  CommandLine|contains: http
selection_extensions:
- CommandLine|endswith:
  - .7z
  - .dat
  - .dll
  - .exe
  - .hta
  - .ps1
  - .psm1
  - .txt
  - .vbe
  - .vbs
  - .zip
- CommandLine|contains:
  - .7z"
  - .dat"
  - .dll"
  - .hta"
  - .ps1"
  - .psm1"
  - .txt"
  - .vbe"
  - .vbs"
  - .zip"
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://twitter.com/mrd0x/status/1478116126005641220
- https://lolbas-project.github.io/lolbas/Binaries/Msedge/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_browsers_inline_file_download.yml)
