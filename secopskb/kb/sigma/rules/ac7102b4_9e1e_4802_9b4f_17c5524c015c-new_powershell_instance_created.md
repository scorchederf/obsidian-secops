---
sigma_id: "ac7102b4-9e1e-4802-9b4f-17c5524c015c"
title: "New PowerShell Instance Created"
framework: "sigma"
generated: "true"
source_path: "rules/windows/pipe_created/pipe_created_powershell_execution_pipe.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/pipe_created/pipe_created_powershell_execution_pipe.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "informational"
logsource: "windows / pipe_created"
aliases:
  - "ac7102b4-9e1e-4802-9b4f-17c5524c015c"
  - "New PowerShell Instance Created"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New PowerShell Instance Created

Detects the execution of PowerShell via the creation of a named pipe starting with PSHost

## Metadata

- Rule ID: ac7102b4-9e1e-4802-9b4f-17c5524c015c
- Status: test
- Level: informational
- Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
- Date: 2019-09-12
- Modified: 2023-11-30
- Source Path: rules/windows/pipe_created/pipe_created_powershell_execution_pipe.yml

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
condition: selection
```

## False Positives

- Likely

## References

- https://threathunterplaybook.com/hunts/windows/190610-PwshAlternateHosts/notebook.html
- https://threathunterplaybook.com/hunts/windows/190410-LocalPwshExecution/notebook.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/pipe_created/pipe_created_powershell_execution_pipe.yml)
