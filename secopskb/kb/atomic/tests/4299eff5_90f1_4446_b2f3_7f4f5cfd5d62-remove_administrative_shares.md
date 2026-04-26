---
atomic_guid: "4299eff5-90f1-4446-b2f3-7f4f5cfd5d62"
title: "Remove Administrative Shares"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.005"
attack_technique_name: "Indicator Removal on Host: Network Share Connection Removal"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.005/T1070.005.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "4299eff5-90f1-4446-b2f3-7f4f5cfd5d62"
  - "Remove Administrative Shares"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Remove Administrative Shares

Administrative shares are hidden network shares created by Microsoft’s Windows NT operating systems that grant system administrators 
remote access to every disk volume on a network-connected system. As Microsoft puts it, “Missing administrative shares typically 
indicate that the computer in question has been compromised by malicious software.
https://threatpost.com/conti-ransomware-gang-has-full-log4shell-attack-chain/177173/

## Metadata

- Atomic GUID: 4299eff5-90f1-4446-b2f3-7f4f5cfd5d62
- Technique: T1070.005: Indicator Removal on Host: Network Share Connection Removal
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1070.005/T1070.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.005]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
for %i in (C$ IPC$ ADMIN$) do net share %i /delete
```

### Cleanup

```commandprompt
net share ADMIN$ /UNLIMITED >nul 2>&1
net share C$=C:\ >nul 2>&1
net share IPC$ >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.005/T1070.005.yaml)
