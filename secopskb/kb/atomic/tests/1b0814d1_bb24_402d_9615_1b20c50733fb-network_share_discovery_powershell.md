---
atomic_guid: "1b0814d1-bb24-402d-9615-1b20c50733fb"
title: "Network Share Discovery PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1135"
attack_technique_name: "Network Share Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1135/T1135.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "1b0814d1-bb24-402d-9615-1b20c50733fb"
  - "Network Share Discovery PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Network Share Discovery PowerShell

Network Share Discovery utilizing PowerShell. The computer name variable may need to be modified to point to a different host
Upon execution, available network shares will be displayed in the powershell session

## Metadata

- Atomic GUID: 1b0814d1-bb24-402d-9615-1b20c50733fb
- Technique: T1135: Network Share Discovery
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1135/T1135.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1135-network_share_discovery|T1135]]

## Executor

- name: powershell

### Command

```powershell
get-smbshare
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1135/T1135.yaml)
