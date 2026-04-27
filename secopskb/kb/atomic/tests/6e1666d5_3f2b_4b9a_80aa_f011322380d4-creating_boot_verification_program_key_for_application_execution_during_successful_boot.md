---
atomic_guid: "6e1666d5-3f2b-4b9a-80aa-f011322380d4"
title: "Creating Boot Verification Program Key for application execution during successful boot"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.001"
attack_technique_name: "Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "6e1666d5-3f2b-4b9a-80aa-f011322380d4"
  - "Creating Boot Verification Program Key for application execution during successful boot"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Microsoft allows users to define a custom boot verification program for those situations by creating the registry key “HKLM\System\CurrentControlSet\Control\BootVerificationProgram” and setting the value of ImagePath to the path of boot verification program.Threat Actor
can abuse by creating this registry key and providing a malicious application to be executed during successful boot

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution#^t1547001-registry-run-keys---startup-folder|T1547.001: Registry Run Keys / Startup Folder]]

## Input Arguments

### malicious_file

- description: Application to be executed during successful boot
- type: string
- default: C:\Program Files\Internet Explorer\iexplore.exe

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg add HKLM\System\CurrentControlSet\Control\BootVerificationProgram /v ImagePath /t REG_SZ /d "#{malicious_file}"
```

### Cleanup

```cmd
reg delete HKLM\System\CurrentControlSet\Control\BootVerificationProgram /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml)
