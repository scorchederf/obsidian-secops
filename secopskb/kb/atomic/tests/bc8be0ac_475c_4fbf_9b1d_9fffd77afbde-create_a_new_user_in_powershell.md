---
atomic_guid: "bc8be0ac-475c-4fbf-9b1d-9fffd77afbde"
title: "Create a new user in PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1136.001"
attack_technique_name: "Create Account: Local Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.001/T1136.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "bc8be0ac-475c-4fbf-9b1d-9fffd77afbde"
  - "Create a new user in PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Create a new user in PowerShell

Creates a new user in PowerShell. Upon execution, details about the new account will be displayed in the powershell session. To verify the
new account, run "net user" in powershell or CMD and observe that there is a new user named "T1136.001_PowerShell"

## Metadata

- Atomic GUID: bc8be0ac-475c-4fbf-9b1d-9fffd77afbde
- Technique: T1136.001: Create Account: Local Account
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1136.001/T1136.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1136-create_account|T1136.001]]

## Input Arguments

### username

- description: Username of the user to create
- type: string
- default: T1136.001_PowerShell

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
New-LocalUser -Name "#{username}" -NoPassword
```

### Cleanup

```powershell
Remove-LocalUser -Name "#{username}" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.001/T1136.001.yaml)
