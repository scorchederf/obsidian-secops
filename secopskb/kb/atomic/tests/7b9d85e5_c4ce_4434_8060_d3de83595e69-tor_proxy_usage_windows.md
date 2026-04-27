---
atomic_guid: "7b9d85e5-c4ce-4434-8060-d3de83595e69"
title: "Tor Proxy Usage - Windows"
framework: "atomic"
generated: "true"
attack_technique_id: "T1090.003"
attack_technique_name: "Proxy: Multi-hop Proxy"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1090.003/T1090.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "7b9d85e5-c4ce-4434-8060-d3de83595e69"
  - "Tor Proxy Usage - Windows"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Tor Proxy Usage - Windows

This test is designed to launch the tor proxy service, which is what is utilized in the background by the Tor Browser and other applications with add-ons in order to provide onion routing functionality.
Upon successful execution, the tor proxy will be launched, run for 60 seconds, and then exit.

## Metadata

- Atomic GUID: 7b9d85e5-c4ce-4434-8060-d3de83595e69
- Technique: T1090.003: Proxy: Multi-hop Proxy
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1090.003/T1090.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1090-proxy|T1090.003]]

## Input Arguments

### TorExe

- description: Location of tor.exe file.
- type: string
- default: PathToAtomicsFolder\..\ExternalPayloads\tor\Tor\tor.exe

## Dependencies

tor.exe must be installed on the machine

### Prerequisite Check

```powershell
if (Test-Path "#{TorExe}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://archive.torproject.org/tor-package-archive/torbrowser/11.0.6/tor-win32-0.4.6.9.zip" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\tor.zip"
expand-archive -LiteralPath "PathToAtomicsFolder\..\ExternalPayloads\tor.zip" -DestinationPath "PathToAtomicsFolder\..\ExternalPayloads\tor"
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
invoke-expression 'cmd /c start powershell -Command {cmd /c "#{TorExe}"}'
sleep -s 60
stop-process -name "tor" | out-null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1090.003/T1090.003.yaml)
