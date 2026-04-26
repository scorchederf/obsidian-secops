---
atomic_guid: "a5b2f6a0-24b4-493e-9590-c699f75723ca"
title: "Packet Capture Windows Command Prompt"
framework: "atomic"
generated: "true"
attack_technique_id: "T1040"
attack_technique_name: "Network Sniffing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1040/T1040.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "a5b2f6a0-24b4-493e-9590-c699f75723ca"
  - "Packet Capture Windows Command Prompt"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Packet Capture Windows Command Prompt

Perform a packet capture using the windows command prompt. This will require a host that has Wireshark/Tshark
installed.

Upon successful execution, tshark will execute and capture 5 packets on interface "Ethernet".

## Metadata

- Atomic GUID: a5b2f6a0-24b4-493e-9590-c699f75723ca
- Technique: T1040: Network Sniffing
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1040/T1040.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1040-network_sniffing|T1040]]

## Input Arguments

### interface

- description: Specify interface to perform PCAP on.
- type: string
- default: Ethernet

### npcap_path

- description: path to npcap.sys
- type: path
- default: C:\Program Files\Npcap\npcap.sys

### npcap_url

- description: npcap installed download URL
- type: url
- default: https://nmap.org/npcap/dist/npcap-1.31.exe

### tshark_path

- description: path to tshark.exe
- type: path
- default: c:\program files\wireshark\tshark.exe

### wireshark_url

- description: wireshark installer download URL
- type: url
- default: https://1.eu.dl.wireshark.org/win64/Wireshark-latest-x64.exe

## Dependencies

tshark must be installed and in the default path of "c:\Program Files\Wireshark\Tshark.exe".

### Prerequisite Check

```text
if (test-path "#{tshark_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest -OutFile "PathToAtomicsFolder\..\ExternalPayloads\wireshark_installer.exe" #{wireshark_url}
Start-Process "PathToAtomicsFolder\..\ExternalPayloads\wireshark_installer.exe" /S
```

npcap must be installed.

### Prerequisite Check

```text
if (test-path "#{npcap_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest -OutFile "PathToAtomicsFolder\..\ExternalPayloads\npcap_installer.exe" #{npcap_url}
Start-Process "PathToAtomicsFolder\..\ExternalPayloads\npcap_installer.exe"
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
"c:\Program Files\Wireshark\tshark.exe" -i #{interface} -c 5
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1040/T1040.yaml)
