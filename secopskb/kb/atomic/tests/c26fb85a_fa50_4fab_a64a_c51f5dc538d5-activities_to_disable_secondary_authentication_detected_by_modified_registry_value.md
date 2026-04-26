---
atomic_guid: "c26fb85a-fa50-4fab-a64a-c51f5dc538d5"
title: "Activities To Disable Secondary Authentication Detected By Modified Registry Value."
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "c26fb85a-fa50-4fab-a64a-c51f5dc538d5"
  - "Activities To Disable Secondary Authentication Detected By Modified Registry Value."
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Activities To Disable Secondary Authentication Detected By Modified Registry Value.

Detect the disable secondary authentication activities that adversary attempt to bypass MFA and to get the unauthorized access to the system or sensitive data.
See the related article (https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.SecondaryAuthenticationFactor::MSSecondaryAuthFactor_AllowSecondaryAuthenticationDevice).

## Metadata

- Atomic GUID: c26fb85a-fa50-4fab-a64a-c51f5dc538d5
- Technique: T1112: Modify Registry
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1112/T1112.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Executor

- name: command_prompt

### Command

```cmd
reg add "HKLM\SOFTWARE\Policies\Microsoft\SecondaryAuthenticationFactor" /v "AllowSecondaryAuthenticationDevice" /t REG_DWORD /d 0 /f
```

### Cleanup

```cmd
reg add "HKLM\SOFTWARE\Policies\Microsoft\SecondaryAuthenticationFactor" /v "AllowSecondaryAuthenticationDevice" /t REG_DWORD /d 1 /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
