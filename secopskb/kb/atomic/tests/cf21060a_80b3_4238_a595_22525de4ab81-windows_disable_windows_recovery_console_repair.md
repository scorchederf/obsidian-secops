---
atomic_guid: "cf21060a-80b3-4238-a595-22525de4ab81"
title: "Windows - Disable Windows Recovery Console Repair"
framework: "atomic"
generated: "true"
attack_technique_id: "T1490"
attack_technique_name: "Inhibit System Recovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1490/T1490.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "cf21060a-80b3-4238-a595-22525de4ab81"
  - "Windows - Disable Windows Recovery Console Repair"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows - Disable Windows Recovery Console Repair

Disables repair by the Windows Recovery Console on boot. This technique is used by numerous ransomware families and APT malware such as Olympic Destroyer.
Upon execution, "The operation completed successfully." will be displayed in the powershell session.

## Metadata

- Atomic GUID: cf21060a-80b3-4238-a595-22525de4ab81
- Technique: T1490: Inhibit System Recovery
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1490/T1490.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
bcdedit.exe /set {default} bootstatuspolicy ignoreallfailures
bcdedit.exe /set {default} recoveryenabled no
```

### Cleanup

```cmd
bcdedit.exe /set {default} bootstatuspolicy DisplayAllFailures >nul 2>&1
bcdedit.exe /set {default} recoveryenabled yes >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1490/T1490.yaml)
