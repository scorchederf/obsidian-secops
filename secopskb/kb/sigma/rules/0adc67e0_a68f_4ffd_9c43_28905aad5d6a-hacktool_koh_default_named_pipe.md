---
sigma_id: "0adc67e0-a68f-4ffd-9c43-28905aad5d6a"
title: "HackTool - Koh Default Named Pipe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/pipe_created/pipe_created_hktl_koh_default_pipe.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/pipe_created/pipe_created_hktl_koh_default_pipe.yml"
build_date: "2026-04-26 15:01:45"
status: "test"
level: "critical"
logsource: "windows / pipe_created"
aliases:
  - "0adc67e0-a68f-4ffd-9c43-28905aad5d6a"
  - "HackTool - Koh Default Named Pipe"
attack_technique_ids:
  - "T1528"
  - "T1134.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - Koh Default Named Pipe

Detects creation of default named pipes used by the Koh tool

## Metadata

- Rule ID: 0adc67e0-a68f-4ffd-9c43-28905aad5d6a
- Status: test
- Level: critical
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-08
- Modified: 2023-08-07
- Source Path: rules/windows/pipe_created/pipe_created_hktl_koh_default_pipe.yml

## Logsource

- category: pipe_created
- definition: Note that you have to configure logging for Named Pipe Events in Sysmon config (Event ID 17 and Event ID 18). The basic configuration is in popular sysmon configuration (https://github.com/SwiftOnSecurity/sysmon-config), but it is worth verifying. You can also use other repo, e.g. https://github.com/Neo23x0/sysmon-config, https://github.com/olafhartong/sysmon-modular. How to test detection? You can check powershell script from this site https://svch0st.medium.com/guide-to-named-pipes-and-hunting-for-cobalt-strike-pipes-dc46b2c5f575
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1528-steal_application_access_token|T1528]]
- [[kb/attack/techniques/T1134-access_token_manipulation|T1134.001]]

## Detection

```yaml
selection:
  PipeName|contains:
  - \imposecost
  - \imposingcost
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/GhostPack/Koh/blob/0283d9f3f91cf74732ad377821986cfcb088e20a/Clients/BOF/KohClient.c#L12

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/pipe_created/pipe_created_hktl_koh_default_pipe.yml)
