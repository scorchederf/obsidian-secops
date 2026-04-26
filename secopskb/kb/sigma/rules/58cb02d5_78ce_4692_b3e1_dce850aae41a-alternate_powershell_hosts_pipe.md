---
sigma_id: "58cb02d5-78ce-4692-b3e1-dce850aae41a"
title: "Alternate PowerShell Hosts Pipe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/pipe_created/pipe_created_powershell_alternate_host_pipe.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/pipe_created/pipe_created_powershell_alternate_host_pipe.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / pipe_created"
aliases:
  - "58cb02d5-78ce-4692-b3e1-dce850aae41a"
  - "Alternate PowerShell Hosts Pipe"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Alternate PowerShell Hosts Pipe

Detects alternate PowerShell hosts potentially bypassing detections looking for powershell.exe

## Metadata

- Rule ID: 58cb02d5-78ce-4692-b3e1-dce850aae41a
- Status: test
- Level: medium
- Author: Roberto Rodriguez @Cyb3rWard0g, Tim Shelton
- Date: 2019-09-12
- Modified: 2025-10-07
- Source Path: rules/windows/pipe_created/pipe_created_powershell_alternate_host_pipe.yml

## Logsource

- category: pipe_created
- definition: Note that you have to configure logging for Named Pipe Events in Sysmon config (Event ID 17 and Event ID 18). The basic configuration is in popular sysmon configuration (https://github.com/SwiftOnSecurity/sysmon-config), but it is worth verifying. You can also use other repo, e.g. https://github.com/Neo23x0/sysmon-config, https://github.com/olafhartong/sysmon-modular. How to test detection? You can check powershell script from this site https://svch0st.medium.com/guide-to-named-pipes-and-hunting-for-cobalt-strike-pipes-dc46b2c5f575
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  PipeName|startswith: \PSHost
filter_main_generic:
- Image|contains:
  - :\Program Files\PowerShell\7-preview\pwsh.exe
  - :\Program Files\PowerShell\7\pwsh.exe
  - :\Windows\system32\dsac.exe
  - :\Windows\system32\inetsrv\w3wp.exe
  - :\Windows\System32\sdiagnhost.exe
  - :\Windows\system32\ServerManager.exe
  - :\Windows\system32\wbem\wmiprvse.exe
  - :\Windows\System32\WindowsPowerShell\v1.0\powershell_ise.exe
  - :\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
  - :\Windows\System32\wsmprovhost.exe
  - :\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell_ise.exe
  - :\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe
- Image|contains|all:
  - C:\Program Files\WindowsApps\Microsoft.PowerShellPreview
  - \pwsh.exe
- Image|contains|all:
  - \AppData\Local\Microsoft\WindowsApps\Microsoft.PowerShellPreview
  - \pwsh.exe
filter_optional_sqlserver:
  Image|startswith:
  - C:\Program Files (x86)\
  - C:\Program Files\
  Image|contains: \Microsoft SQL Server\
  Image|endswith: \Tools\Binn\SQLPS.exe
filter_optional_azure_connected_machine_agent:
  Image|startswith: C:\Program Files\AzureConnectedMachineAgent\GCArcService
  Image|endswith: \GC\gc_worker.exe
filter_optional_citrix:
  Image|startswith: C:\Program Files\Citrix\
filter_optional_exchange:
  Image|startswith: C:\Program Files\Microsoft\Exchange Server\
filter_main_null:
  Image: null
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Programs using PowerShell directly without invocation of a dedicated interpreter.

## References

- https://threathunterplaybook.com/hunts/windows/190610-PwshAlternateHosts/notebook.html
- https://threathunterplaybook.com/hunts/windows/190410-LocalPwshExecution/notebook.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/pipe_created/pipe_created_powershell_alternate_host_pipe.yml)
