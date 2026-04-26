---
sigma_id: "ee37eb7c-a4e7-4cd5-8fa4-efa27f1c3f31"
title: "PUA - Ngrok Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_ngrok.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_ngrok.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "ee37eb7c-a4e7-4cd5-8fa4-efa27f1c3f31"
  - "PUA - Ngrok Execution"
attack_technique_ids:
  - "T1572"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PUA - Ngrok Execution

Detects the use of Ngrok, a utility used for port forwarding and tunneling, often used by threat actors to make local protected services publicly available.
Involved domains are bin.equinox.io for download and *.ngrok.io for connections.

## Metadata

- Rule ID: ee37eb7c-a4e7-4cd5-8fa4-efa27f1c3f31
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2021-05-14
- Modified: 2023-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_pua_ngrok.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1572-protocol_tunneling|T1572]]

## Detection

```yaml
selection1:
  CommandLine|contains:
  - ' tcp 139'
  - ' tcp 445'
  - ' tcp 3389'
  - ' tcp 5985'
  - ' tcp 5986'
selection2:
  CommandLine|contains|all:
  - ' start '
  - --all
  - --config
  - .yml
selection3:
  Image|endswith: ngrok.exe
  CommandLine|contains:
  - ' tcp '
  - ' http '
  - ' authtoken '
selection4:
  CommandLine|contains:
  - '.exe authtoken '
  - .exe start --all
condition: 1 of selection*
```

## False Positives

- Another tool that uses the command line switches of Ngrok
- Ngrok http 3978 (https://learn.microsoft.com/en-us/azure/bot-service/bot-service-debug-channel-ngrok?view=azure-bot-service-4.0)

## References

- https://ngrok.com/docs
- https://www.fireeye.com/blog/threat-research/2021/05/shining-a-light-on-darkside-ransomware-operations.html
- https://stackoverflow.com/questions/42442320/ssh-tunnel-to-ngrok-and-initiate-rdp
- https://www.virustotal.com/gui/file/58d21840d915aaf4040ceb89522396124c82f325282f805d1085527e1e2ccfa1/detection
- https://cybleinc.com/2021/02/15/ngrok-platform-abused-by-hackers-to-deliver-a-new-wave-of-phishing-attacks/
- https://twitter.com/xorJosh/status/1598646907802451969
- https://www.softwaretestinghelp.com/how-to-use-ngrok/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_ngrok.yml)
