---
atomic_guid: "ce4fc678-364f-4282-af16-2fb4c78005ce"
title: "Shortcut Modification"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.009"
attack_technique_name: "Boot or Logon Autostart Execution: Shortcut Modification"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.009/T1547.009.yaml"
build_date: "2026-04-27 19:12:27"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test to simulate shortcut modification and then execute. example shortcut (*.lnk , .url) strings check with powershell;
gci -path "C:\Users" -recurse -include *.url -ea SilentlyContinue | Select-String -Pattern "exe" | FL.
Upon execution, calc.exe will be launched.

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution#^t1547009-shortcut-modification|T1547.009: Shortcut Modification]]

## Input Arguments

### shortcut_file_path

- description: shortcut modified and execute
- type: path
- default: %temp%\T1547.009_modified_shortcut.url

## Executor

- name: command_prompt

### Command

```cmd
echo [InternetShortcut] > #{shortcut_file_path}
echo URL=C:\windows\system32\calc.exe >> #{shortcut_file_path}
#{shortcut_file_path}
```

### Cleanup

```cmd
del -f #{shortcut_file_path} >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.009/T1547.009.yaml)
