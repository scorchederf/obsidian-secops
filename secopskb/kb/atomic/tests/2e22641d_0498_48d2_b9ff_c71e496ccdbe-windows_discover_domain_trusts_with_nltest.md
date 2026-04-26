---
atomic_guid: "2e22641d-0498-48d2-b9ff-c71e496ccdbe"
title: "Windows - Discover domain trusts with nltest"
framework: "atomic"
generated: "true"
attack_technique_id: "T1482"
attack_technique_name: "Domain Trust Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1482/T1482.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "2e22641d-0498-48d2-b9ff-c71e496ccdbe"
  - "Windows - Discover domain trusts with nltest"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows - Discover domain trusts with nltest

Uses the nltest command to discover domain trusts.
Requires the installation of nltest via Windows RSAT or the Windows Server AD DS role.
This technique has been used by the Trickbot malware family.

## Metadata

- Atomic GUID: 2e22641d-0498-48d2-b9ff-c71e496ccdbe
- Technique: T1482: Domain Trust Discovery
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1482/T1482.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1482-domain_trust_discovery|T1482]]

## Dependencies

nltest.exe from RSAT must be present on disk

### Prerequisite Check

```untitled
WHERE nltest.exe >NUL 2>&1
```

### Get Prerequisite

```untitled
echo Sorry RSAT must be installed manually
```

## Executor

- name: command_prompt

### Command

```cmd
nltest /domain_trusts
nltest /trusted_domains
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1482/T1482.yaml)
