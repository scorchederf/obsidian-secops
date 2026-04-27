---
atomic_guid: "5f5b71da-e03f-42e7-ac98-d63f9e0465cb"
title: "Re-Opened Applications using LoginHook"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.007"
attack_technique_name: "Boot or Logon Autostart Execution: Re-opened Applications"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.007/T1547.007.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "5f5b71da-e03f-42e7-ac98-d63f9e0465cb"
  - "Re-Opened Applications using LoginHook"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Re-Opened Applications using LoginHook

Mac Defaults

[Reference](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CustomLogin.html)

## Metadata

- Atomic GUID: 5f5b71da-e03f-42e7-ac98-d63f9e0465cb
- Technique: T1547.007: Boot or Logon Autostart Execution: Re-opened Applications
- Platforms: macos
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1547.007/T1547.007.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.007]]

## Input Arguments

### script

- description: path to script
- type: path
- default: /path/to/script

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo defaults write com.apple.loginwindow LoginHook #{script}
```

### Cleanup

```bash
sudo defaults delete com.apple.loginwindow LoginHook
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.007/T1547.007.yaml)
