---
atomic_guid: "5fefd767-ef54-4ac6-84d3-751ab85e8aba"
title: "Copy in loginwindow.plist for Re-Opened Applications"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.007"
attack_technique_name: "Boot or Logon Autostart Execution: Re-opened Applications"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.007/T1547.007.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "5fefd767-ef54-4ac6-84d3-751ab85e8aba"
  - "Copy in loginwindow.plist for Re-Opened Applications"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Copy in loginwindow.plist for Re-Opened Applications

Copy in new loginwindow.plist to launch Calculator.

## Metadata

- Atomic GUID: 5fefd767-ef54-4ac6-84d3-751ab85e8aba
- Technique: T1547.007: Boot or Logon Autostart Execution: Re-opened Applications
- Platforms: macos
- Executor: sh
- Source Path: atomics/T1547.007/T1547.007.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.007]]

## Input Arguments

### calc_plist_path

- description: path to binary plist with entry to open calculator
- type: path
- default: PathToAtomicsFolder/T1547.007/src/reopen_loginwindow_calc.plist

## Executor

- name: sh

### Command

```bash
cp #{calc_plist_path} ~/Library/Preferences/ByHost/com.apple.loginwindow.plist
```

### Cleanup

```bash
rm -f ~/Library/Preferences/ByHost/com.apple.loginwindow.plist
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.007/T1547.007.yaml)
