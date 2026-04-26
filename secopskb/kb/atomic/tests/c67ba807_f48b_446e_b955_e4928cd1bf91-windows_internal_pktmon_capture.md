---
atomic_guid: "c67ba807-f48b-446e-b955-e4928cd1bf91"
title: "Windows Internal pktmon capture"
framework: "atomic"
generated: "true"
attack_technique_id: "T1040"
attack_technique_name: "Network Sniffing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1040/T1040.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "c67ba807-f48b-446e-b955-e4928cd1bf91"
  - "Windows Internal pktmon capture"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows Internal pktmon capture

Will start a packet capture and store log file as t1040.etl.
https://lolbas-project.github.io/lolbas/Binaries/Pktmon/

## Metadata

- Atomic GUID: c67ba807-f48b-446e-b955-e4928cd1bf91
- Technique: T1040: Network Sniffing
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1040/T1040.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1040-network_sniffing|T1040]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
pktmon.exe start --etw  -f %TEMP%\t1040.etl
TIMEOUT /T 5 >nul 2>&1
pktmon.exe stop
```

### Cleanup

```commandprompt
del %TEMP%\t1040.etl
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1040/T1040.yaml)
