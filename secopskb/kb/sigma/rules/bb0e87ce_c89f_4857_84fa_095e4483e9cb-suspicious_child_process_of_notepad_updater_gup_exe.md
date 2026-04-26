---
sigma_id: "bb0e87ce-c89f-4857-84fa-095e4483e9cb"
title: "Suspicious Child Process of Notepad++ Updater - GUP.Exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_gup_susp_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_gup_susp_child_process.yml"
build_date: "2026-04-26 15:01:51"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "bb0e87ce-c89f-4857-84fa-095e4483e9cb"
  - "Suspicious Child Process of Notepad++ Updater - GUP.Exe"
attack_technique_ids:
  - "T1195.002"
  - "T1557"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Child Process of Notepad++ Updater - GUP.Exe

Detects suspicious child process creation by the Notepad++ updater process (gup.exe).
This could indicate potential exploitation of the updater component to deliver unwanted malware.

## Metadata

- Rule ID: bb0e87ce-c89f-4857-84fa-095e4483e9cb
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2026-02-03
- Source Path: rules/windows/process_creation/proc_creation_win_gup_susp_child_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1195-supply_chain_compromise|T1195.002]]
- [[kb/attack/techniques/T1557-adversary-in-the-middle|T1557]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith: \gup.exe
selection_child_img:
  Image|endswith:
  - \cmd.exe
  - \powershell.exe
  - \pwsh.exe
  - \cscript.exe
  - \wscript.exe
  - \mshta.exe
selection_child_cli:
  CommandLine|contains:
  - bitsadmin
  - certutil
  - curl
  - finger
  - forfiles
  - regsvr32
  - rundll32
  - wget
condition: selection_parent and 1 of selection_child_*
```

## False Positives

- Unlikely

## References

- https://notepad-plus-plus.org/news/v889-released/
- https://www.heise.de/en/news/Notepad-updater-installed-malware-11109726.html
- https://www.rapid7.com/blog/post/tr-chrysalis-backdoor-dive-into-lotus-blossoms-toolkit/
- https://www.validin.com/blog/exploring_notepad_plus_plus_network_indicators/
- https://securelist.com/notepad-supply-chain-attack/118708/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_gup_susp_child_process.yml)
