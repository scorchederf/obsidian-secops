---
atomic_guid: "fdd45306-74f6-4ade-9a97-0a4895961228"
title: "Leverage Virtual Channels to execute custom DLL during successful RDP session"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547"
attack_technique_name: "Boot or Logon Autostart Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547/T1547.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "fdd45306-74f6-4ade-9a97-0a4895961228"
  - "Leverage Virtual Channels to execute custom DLL during successful RDP session"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Virtual Channels can be leveraged to alter RDP behavior using dedicated Addins.The mechanism is implemented using DLLs which can be executed during RDP session automatically. 
The DLLs are loaded in the host system only after successful connection is established with the remote system.
Once the test is run, amsi.dll will be loaded on the host system during successful RDP session.
Blog :https://learn.microsoft.com/en-us/windows/win32/termserv/terminal-services-virtual-channels?redirectedfrom=MSDN

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547: Boot or Logon Autostart Execution]]

## Input Arguments

### Subkey_Added

- description: New Sub key added in the registry path
- type: String
- default: Malware

### dll_inf

- description: custom DLL to be executed
- type: Path
- default: C:\Windows\System32\amsi.dll

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg add "HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default\Addins\#{Subkey_Added}" /v Name /t REG_SZ /d "#{dll_inf}" /f
```

### Cleanup

```cmd
reg delete "HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default\Addins\#{Subkey_Added}" /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547/T1547.yaml)
