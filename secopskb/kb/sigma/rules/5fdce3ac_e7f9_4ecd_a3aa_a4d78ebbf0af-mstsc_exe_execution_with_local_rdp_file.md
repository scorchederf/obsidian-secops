---
sigma_id: "5fdce3ac-e7f9-4ecd-a3aa-a4d78ebbf0af"
title: "Mstsc.EXE Execution With Local RDP File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_mstsc_run_local_rdp_file.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mstsc_run_local_rdp_file.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "5fdce3ac-e7f9-4ecd-a3aa-a4d78ebbf0af"
  - "Mstsc.EXE Execution With Local RDP File"
attack_technique_ids:
  - "T1219.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Mstsc.EXE Execution With Local RDP File

Detects potential RDP connection via Mstsc using a local ".rdp" file

## Metadata

- Rule ID: 5fdce3ac-e7f9-4ecd-a3aa-a4d78ebbf0af
- Status: test
- Level: low
- Author: Nasreddine Bencherchali (Nextron Systems), Christopher Peacock @securepeacock
- Date: 2023-04-18
- Modified: 2023-04-30
- Source Path: rules/windows/process_creation/proc_creation_win_mstsc_run_local_rdp_file.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools|T1219.002]]

## Detection

```yaml
selection_img:
- Image|endswith: \mstsc.exe
- OriginalFileName: mstsc.exe
selection_cli:
  CommandLine|endswith:
  - .rdp
  - .rdp"
filter_optional_wsl:
  ParentImage: C:\Windows\System32\lxss\wslhost.exe
  CommandLine|contains: C:\ProgramData\Microsoft\WSL\wslg.rdp
condition: all of selection_* and not 1 of filter_optional_*
```

## False Positives

- Likely with legitimate usage of ".rdp" files

## References

- https://www.blackhillsinfosec.com/rogue-rdp-revisiting-initial-access-methods/
- https://web.archive.org/web/20230726144748/https://blog.thickmints.dev/mintsights/detecting-rogue-rdp/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mstsc_run_local_rdp_file.yml)
