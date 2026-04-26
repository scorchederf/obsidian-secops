---
sigma_id: "575dce0c-8139-4e30-9295-1ee75969f7fe"
title: "Potential Reconnaissance Activity Via GatherNetworkInfo.VBS"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_gather_network_info.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_gather_network_info.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "575dce0c-8139-4e30-9295-1ee75969f7fe"
  - "Potential Reconnaissance Activity Via GatherNetworkInfo.VBS"
attack_technique_ids:
  - "T1615"
  - "T1059.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Reconnaissance Activity Via GatherNetworkInfo.VBS

Detects execution of the built-in script located in "C:\Windows\System32\gatherNetworkInfo.vbs". Which can be used to gather information about the target machine

## Metadata

- Rule ID: 575dce0c-8139-4e30-9295-1ee75969f7fe
- Status: test
- Level: medium
- Author: blueteamer8699
- Date: 2022-01-03
- Modified: 2023-02-08
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_gather_network_info.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1615-group_policy_discovery|T1615]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.005]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \cscript.exe
  - \wscript.exe
- OriginalFileName:
  - cscript.exe
  - wscript.exe
selection_cli:
  CommandLine|contains: gatherNetworkInfo.vbs
condition: all of selection_*
```

## False Positives

- Administrative activity

## References

- https://posts.slayerlabs.com/living-off-the-land/#gathernetworkinfovbs
- https://www.mandiant.com/resources/blog/trojanized-windows-installers-ukrainian-government

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_gather_network_info.yml)
