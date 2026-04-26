---
sigma_id: "f6451de4-df0a-41fa-8d72-b39f54a08db5"
title: "PUA - PAExec Default Named Pipe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/pipe_created/pipe_created_pua_paexec_default_pipe.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/pipe_created/pipe_created_pua_paexec_default_pipe.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / pipe_created"
aliases:
  - "f6451de4-df0a-41fa-8d72-b39f54a08db5"
  - "PUA - PAExec Default Named Pipe"
attack_technique_ids:
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PUA - PAExec Default Named Pipe

Detects PAExec default named pipe

## Metadata

- Rule ID: f6451de4-df0a-41fa-8d72-b39f54a08db5
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-10-26
- Source Path: rules/windows/pipe_created/pipe_created_pua_paexec_default_pipe.yml

## Logsource

- category: pipe_created
- definition: Note that you have to configure logging for Named Pipe Events in Sysmon config (Event ID 17 and Event ID 18). The basic configuration is in popular sysmon configuration (https://github.com/SwiftOnSecurity/sysmon-config), but it is worth verifying. You can also use other repo, e.g. https://github.com/Neo23x0/sysmon-config, https://github.com/olafhartong/sysmon-modular. How to test detection? You can check powershell script from this site https://svch0st.medium.com/guide-to-named-pipes-and-hunting-for-cobalt-strike-pipes-dc46b2c5f575
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1569-system_services|T1569.002]]

## Detection

```yaml
selection:
  PipeName|startswith: \PAExec
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/microsoft/Microsoft-365-Defender-Hunting-Queries/blob/efa17a600b43c897b4b7463cc8541daa1987eeb4/Command%20and%20Control/C2-NamedPipe.md
- https://github.com/poweradminllc/PAExec

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/pipe_created/pipe_created_pua_paexec_default_pipe.yml)
