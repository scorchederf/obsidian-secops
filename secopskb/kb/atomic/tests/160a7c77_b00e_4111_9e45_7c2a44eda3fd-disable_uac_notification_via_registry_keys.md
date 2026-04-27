---
atomic_guid: "160a7c77-b00e-4111-9e45-7c2a44eda3fd"
title: "Disable UAC notification via registry keys"
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.002"
attack_technique_name: "Abuse Elevation Control Mechanism: Bypass User Account Control"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "160a7c77-b00e-4111-9e45-7c2a44eda3fd"
  - "Disable UAC notification via registry keys"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Disable UAC notification via registry keys

This atomic regarding UACDisableNotify pertains to the notification behavior of UAC. UAC is a critical security feature in Windows that prevents unauthorized changes to the operating system. It prompts the user for permission or an administrator password before allowing actions that could affect the system's operation or change settings that affect other users. The BlotchyQuasar RAT defense evasion activities that the adversary to disable UAC notifications makes it easier for malware and malicious software to execute with elevated privileges. [Article](https://securityintelligence.com/x-force/x-force-hive0129-targeting-financial-institutions-latam-banking-trojan/)

## Metadata

- Atomic GUID: 160a7c77-b00e-4111-9e45-7c2a44eda3fd
- Technique: T1548.002: Abuse Elevation Control Mechanism: Bypass User Account Control
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1548.002/T1548.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Executor

- name: command_prompt

### Command

```cmd
reg add "HKLM\SOFTWARE\Microsoft\Security Center" /v UACDisableNotify /t REG_DWORD /d 1 /f
```

### Cleanup

```cmd
reg add "HKLM\SOFTWARE\Microsoft\Security Center" /v UACDisableNotify /t REG_DWORD /d 0 /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml)
