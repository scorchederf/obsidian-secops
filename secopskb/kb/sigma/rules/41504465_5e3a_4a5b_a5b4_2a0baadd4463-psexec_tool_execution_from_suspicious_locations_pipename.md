---
sigma_id: "41504465-5e3a-4a5b-a5b4-2a0baadd4463"
title: "PsExec Tool Execution From Suspicious Locations - PipeName"
framework: "sigma"
generated: "true"
source_path: "rules/windows/pipe_created/pipe_created_sysinternals_psexec_default_pipe_susp_location.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/pipe_created/pipe_created_sysinternals_psexec_default_pipe_susp_location.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / pipe_created"
aliases:
  - "41504465-5e3a-4a5b-a5b4-2a0baadd4463"
  - "PsExec Tool Execution From Suspicious Locations - PipeName"
attack_technique_ids:
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PsExec Tool Execution From Suspicious Locations - PipeName

Detects PsExec default pipe creation where the image executed is located in a suspicious location. Which could indicate that the tool is being used in an attack

## Metadata

- Rule ID: 41504465-5e3a-4a5b-a5b4-2a0baadd4463
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-04
- Modified: 2023-09-20
- Source Path: rules/windows/pipe_created/pipe_created_sysinternals_psexec_default_pipe_susp_location.yml

## Logsource

- category: pipe_created
- definition: Note that you have to configure logging for Named Pipe Events in Sysmon config (Event ID 17 and Event ID 18). The basic configuration is in popular sysmon configuration (https://github.com/SwiftOnSecurity/sysmon-config), but it is worth verifying. You can also use other repo, e.g. https://github.com/Neo23x0/sysmon-config, https://github.com/olafhartong/sysmon-modular. How to test detection? You can check powershell script from this site https://svch0st.medium.com/guide-to-named-pipes-and-hunting-for-cobalt-strike-pipes-dc46b2c5f575
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1569-system_services|T1569.002]]

### Software Tags

- S0029

## Detection

```yaml
selection:
  PipeName: \PSEXESVC
  Image|contains:
  - :\Users\Public\
  - :\Windows\Temp\
  - \AppData\Local\Temp\
  - \Desktop\
  - \Downloads\
condition: selection
```

## False Positives

- Rare legitimate use of psexec from the locations mentioned above. This will require initial tuning based on your environment.

## References

- https://www.jpcert.or.jp/english/pub/sr/ir_research.html
- https://jpcertcc.github.io/ToolAnalysisResultSheet

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/pipe_created/pipe_created_sysinternals_psexec_default_pipe_susp_location.yml)
