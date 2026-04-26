---
atomic_guid: "2b73cd9b-b2fb-4357-b9d7-c73c41d9e945"
title: "Check if System Integrity Protection is enabled"
framework: "atomic"
generated: "true"
attack_technique_id: "T1497.001"
attack_technique_name: "Virtualization/Sandbox Evasion: System Checks"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1497.001/T1497.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "2b73cd9b-b2fb-4357-b9d7-c73c41d9e945"
  - "Check if System Integrity Protection is enabled"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Check if System Integrity Protection is enabled

The latest versions of macOS have the System Integrity Protection feature (SIP). If a sandbox uses a non-signed 
kernel extension for monitoring purposes the, SIP feature must be disabled to load this kind of kernel extension.
Malware may check if the SIP is enabled.
Reference: https://evasions.checkpoint.com/src/MacOS/macos.html#sip

## Metadata

- Atomic GUID: 2b73cd9b-b2fb-4357-b9d7-c73c41d9e945
- Technique: T1497.001: Virtualization/Sandbox Evasion: System Checks
- Platforms: macos
- Executor: sh
- Source Path: atomics/T1497.001/T1497.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1497-virtualization_sandbox_evasion|T1497.001]]

## Executor

- name: sh

### Command

```bash
if [ "$(csrutil status | grep -v 'enabled')" != "" ]; then echo 'Possible Virtualization Environment detected'; fi;
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1497.001/T1497.001.yaml)
