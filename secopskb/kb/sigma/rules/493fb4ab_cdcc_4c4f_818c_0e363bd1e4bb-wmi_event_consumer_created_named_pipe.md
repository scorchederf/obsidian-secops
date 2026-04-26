---
sigma_id: "493fb4ab-cdcc-4c4f-818c-0e363bd1e4bb"
title: "WMI Event Consumer Created Named Pipe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/pipe_created/pipe_created_scrcons_wmi_consumer_namedpipe.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/pipe_created/pipe_created_scrcons_wmi_consumer_namedpipe.yml"
build_date: "2026-04-26 14:14:39"
status: "test"
level: "medium"
logsource: "windows / pipe_created"
aliases:
  - "493fb4ab-cdcc-4c4f-818c-0e363bd1e4bb"
  - "WMI Event Consumer Created Named Pipe"
attack_technique_ids:
  - "T1047"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# WMI Event Consumer Created Named Pipe

Detects the WMI Event Consumer service scrcons.exe creating a named pipe

## Metadata

- Rule ID: 493fb4ab-cdcc-4c4f-818c-0e363bd1e4bb
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2021-09-01
- Modified: 2023-11-30
- Source Path: rules/windows/pipe_created/pipe_created_scrcons_wmi_consumer_namedpipe.yml

## Logsource

- category: pipe_created
- definition: Note that you have to configure logging for Named Pipe Events in Sysmon config (Event ID 17 and Event ID 18). The basic configuration is in popular sysmon configuration (https://github.com/SwiftOnSecurity/sysmon-config), but it is worth verifying. You can also use other repo, e.g. https://github.com/Neo23x0/sysmon-config, https://github.com/olafhartong/sysmon-modular. How to test detection? You can check powershell script from this site https://svch0st.medium.com/guide-to-named-pipes-and-hunting-for-cobalt-strike-pipes-dc46b2c5f575
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]

## Detection

```yaml
selection:
  Image|endswith: \scrcons.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/RiccardoAncarani/LiquidSnake

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/pipe_created/pipe_created_scrcons_wmi_consumer_namedpipe.yml)
