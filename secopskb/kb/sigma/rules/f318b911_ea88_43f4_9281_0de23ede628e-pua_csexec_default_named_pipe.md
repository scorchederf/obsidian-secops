---
sigma_id: "f318b911-ea88-43f4-9281-0de23ede628e"
title: "PUA - CSExec Default Named Pipe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/pipe_created/pipe_created_pua_csexec_default_pipe.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/pipe_created/pipe_created_pua_csexec_default_pipe.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / pipe_created"
aliases:
  - "f318b911-ea88-43f4-9281-0de23ede628e"
  - "PUA - CSExec Default Named Pipe"
attack_technique_ids:
  - "T1021.002"
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PUA - CSExec Default Named Pipe

Detects default CSExec pipe creation

## Metadata

- Rule ID: f318b911-ea88-43f4-9281-0de23ede628e
- Status: test
- Level: medium
- Author: Nikita Nazarov, oscd.community, Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-08-07
- Modified: 2023-11-30
- Source Path: rules/windows/pipe_created/pipe_created_pua_csexec_default_pipe.yml

## Logsource

- category: pipe_created
- definition: Note that you have to configure logging for Named Pipe Events in Sysmon config (Event ID 17 and Event ID 18). The basic configuration is in popular sysmon configuration (https://github.com/SwiftOnSecurity/sysmon-config), but it is worth verifying. You can also use other repo, e.g. https://github.com/Neo23x0/sysmon-config, https://github.com/olafhartong/sysmon-modular. How to test detection? You can check powershell script from this site https://svch0st.medium.com/guide-to-named-pipes-and-hunting-for-cobalt-strike-pipes-dc46b2c5f575
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.002]]
- [[kb/attack/techniques/T1569-system_services|T1569.002]]

## Detection

```yaml
selection:
  PipeName|contains: \csexecsvc
condition: selection
```

## False Positives

- Legitimate Administrator activity

## References

- https://drive.google.com/file/d/1lKya3_mLnR3UQuCoiYruO3qgu052_iS_/view
- https://github.com/malcomvetter/CSExec

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/pipe_created/pipe_created_pua_csexec_default_pipe.yml)
