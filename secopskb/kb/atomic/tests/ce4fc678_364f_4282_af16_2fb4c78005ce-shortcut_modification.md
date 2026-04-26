---
atomic_guid: "ce4fc678-364f-4282-af16-2fb4c78005ce"
title: "Shortcut Modification"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.009"
attack_technique_name: "Boot or Logon Autostart Execution: Shortcut Modification"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.009/T1547.009.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "ce4fc678-364f-4282-af16-2fb4c78005ce"
  - "Shortcut Modification"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Shortcut Modification

This test to simulate shortcut modification and then execute. example shortcut (*.lnk , .url) strings check with powershell;
gci -path "C:\Users" -recurse -include *.url -ea SilentlyContinue | Select-String -Pattern "exe" | FL.
Upon execution, calc.exe will be launched.

## Metadata

- Atomic GUID: ce4fc678-364f-4282-af16-2fb4c78005ce
- Technique: T1547.009: Boot or Logon Autostart Execution: Shortcut Modification
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1547.009/T1547.009.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.009]]

## Input Arguments

### shortcut_file_path

- description: shortcut modified and execute
- type: path
- default: %temp%\T1547.009_modified_shortcut.url

## Executor

- name: command_prompt

### Command

```commandprompt
echo [InternetShortcut] > #{shortcut_file_path}
echo URL=C:\windows\system32\calc.exe >> #{shortcut_file_path}
#{shortcut_file_path}
```

### Cleanup

```commandprompt
del -f #{shortcut_file_path} >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.009/T1547.009.yaml)
