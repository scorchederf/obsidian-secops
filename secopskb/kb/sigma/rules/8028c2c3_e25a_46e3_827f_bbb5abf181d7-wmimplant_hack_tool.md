---
sigma_id: "8028c2c3-e25a-46e3-827f-bbb5abf181d7"
title: "WMImplant Hack Tool"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_wmimplant.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_wmimplant.yml"
build_date: "2026-04-26 14:14:39"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "8028c2c3-e25a-46e3-827f-bbb5abf181d7"
  - "WMImplant Hack Tool"
attack_technique_ids:
  - "T1047"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# WMImplant Hack Tool

Detects parameters used by WMImplant

## Metadata

- Rule ID: 8028c2c3-e25a-46e3-827f-bbb5abf181d7
- Status: test
- Level: high
- Author: NVISO
- Date: 2020-03-26
- Modified: 2022-12-25
- Source Path: rules/windows/powershell/powershell_script/posh_ps_wmimplant.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  ScriptBlockText|contains:
  - WMImplant
  - ' change_user '
  - ' gen_cli '
  - ' command_exec '
  - ' disable_wdigest '
  - ' disable_winrm '
  - ' enable_wdigest '
  - ' enable_winrm '
  - ' registry_mod '
  - ' remote_posh '
  - ' sched_job '
  - ' service_mod '
  - ' process_kill '
  - ' active_users '
  - ' basic_info '
  - ' power_off '
  - ' vacant_system '
  - ' logon_events '
condition: selection
```

## False Positives

- Administrative scripts that use the same keywords.

## References

- https://github.com/FortyNorthSecurity/WMImplant

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_wmimplant.yml)
