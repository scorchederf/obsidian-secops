---
atomic_guid: "9e55750e-4cbf-4013-9627-e9a045b541bf"
title: "Remote Desktop Services Discovery via PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1046"
attack_technique_name: "Network Service Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1046/T1046.yaml"
build_date: "2026-04-27 19:12:26"
executor: "powershell"
aliases:
  - "9e55750e-4cbf-4013-9627-e9a045b541bf"
  - "Remote Desktop Services Discovery via PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Availability of remote desktop services can be checked using get- cmdlet of PowerShell

## ATT&CK Mapping

- [[kb/attack/techniques/T1046-network_service_discovery|T1046: Network Service Discovery]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Get-Service -Name "Remote Desktop Services", "Remote Desktop Configuration"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1046/T1046.yaml)
