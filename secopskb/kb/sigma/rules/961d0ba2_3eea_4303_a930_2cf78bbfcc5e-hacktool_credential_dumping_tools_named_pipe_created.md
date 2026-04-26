---
sigma_id: "961d0ba2-3eea-4303-a930-2cf78bbfcc5e"
title: "HackTool - Credential Dumping Tools Named Pipe Created"
framework: "sigma"
generated: "true"
source_path: "rules/windows/pipe_created/pipe_created_hktl_generic_cred_dump_tools_pipes.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/pipe_created/pipe_created_hktl_generic_cred_dump_tools_pipes.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "critical"
logsource: "windows / pipe_created"
aliases:
  - "961d0ba2-3eea-4303-a930-2cf78bbfcc5e"
  - "HackTool - Credential Dumping Tools Named Pipe Created"
attack_technique_ids:
  - "T1003.001"
  - "T1003.002"
  - "T1003.004"
  - "T1003.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - Credential Dumping Tools Named Pipe Created

Detects well-known credential dumping tools execution via specific named pipe creation

## Metadata

- Rule ID: 961d0ba2-3eea-4303-a930-2cf78bbfcc5e
- Status: test
- Level: critical
- Author: Teymur Kheirkhabarov, oscd.community
- Date: 2019-11-01
- Modified: 2023-08-07
- Source Path: rules/windows/pipe_created/pipe_created_hktl_generic_cred_dump_tools_pipes.yml

## Logsource

- category: pipe_created
- definition: Note that you have to configure logging for Named Pipe Events in Sysmon config (Event ID 17 and Event ID 18). The basic configuration is in popular sysmon configuration (https://github.com/SwiftOnSecurity/sysmon-config), but it is worth verifying. You can also use other repo, e.g. https://github.com/Neo23x0/sysmon-config, https://github.com/olafhartong/sysmon-modular. How to test detection? You can check powershell script from this site https://svch0st.medium.com/guide-to-named-pipes-and-hunting-for-cobalt-strike-pipes-dc46b2c5f575
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.002]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.004]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.005]]

## Detection

```yaml
selection:
  PipeName|contains:
  - \cachedump
  - \lsadump
  - \wceservicepipe
condition: selection
```

## False Positives

- Legitimate Administrator using tool for password recovery

## References

- https://www.slideshare.net/heirhabarov/hunting-for-credentials-dumping-in-windows-environment
- https://image.slidesharecdn.com/zeronights2017kheirkhabarov-171118103000/75/hunting-for-credentials-dumping-in-windows-environment-57-2048.jpg?cb=1666035799

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/pipe_created/pipe_created_hktl_generic_cred_dump_tools_pipes.yml)
