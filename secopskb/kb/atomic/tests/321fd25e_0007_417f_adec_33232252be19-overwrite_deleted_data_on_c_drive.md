---
atomic_guid: "321fd25e-0007-417f-adec-33232252be19"
title: "Overwrite deleted data on C drive"
framework: "atomic"
generated: "true"
attack_technique_id: "T1485"
attack_technique_name: "Data Destruction"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1485/T1485.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "321fd25e-0007-417f-adec-33232252be19"
  - "Overwrite deleted data on C drive"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Overwrite deleted data on C drive

RansomEXX malware removes all deleted files using windows built-in cipher.exe to prevent forensic recover.
This process is very slow and test execution may timeout. 
https://www.cybereason.com/blog/cybereason-vs.-ransomexx-ransomware
https://support.microsoft.com/en-us/topic/cipher-exe-security-tool-for-the-encrypting-file-system-56c85edd-85cf-ac07-f2f7-ca2d35dab7e4

## Metadata

- Atomic GUID: 321fd25e-0007-417f-adec-33232252be19
- Technique: T1485: Data Destruction
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1485/T1485.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1485-data_destruction|T1485]]

## Executor

- name: command_prompt

### Command

```cmd
cipher.exe /w:C:
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1485/T1485.yaml)
