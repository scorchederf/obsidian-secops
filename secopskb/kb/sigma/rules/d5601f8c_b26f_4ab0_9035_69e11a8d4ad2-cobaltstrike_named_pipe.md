---
sigma_id: "d5601f8c-b26f-4ab0-9035-69e11a8d4ad2"
title: "CobaltStrike Named Pipe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/pipe_created/pipe_created_hktl_cobaltstrike.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/pipe_created/pipe_created_hktl_cobaltstrike.yml"
build_date: "2026-04-26 15:01:43"
status: "test"
level: "critical"
logsource: "windows / pipe_created"
aliases:
  - "d5601f8c-b26f-4ab0-9035-69e11a8d4ad2"
  - "CobaltStrike Named Pipe"
attack_technique_ids:
  - "T1055"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# CobaltStrike Named Pipe

Detects the creation of a named pipe as used by CobaltStrike

## Metadata

- Rule ID: d5601f8c-b26f-4ab0-9035-69e11a8d4ad2
- Status: test
- Level: critical
- Author: Florian Roth (Nextron Systems), Wojciech Lesicki
- Date: 2021-05-25
- Modified: 2022-10-31
- Source Path: rules/windows/pipe_created/pipe_created_hktl_cobaltstrike.yml

## Logsource

- category: pipe_created
- definition: Note that you have to configure logging for Named Pipe Events in Sysmon config (Event ID 17 and Event ID 18). The basic configuration is in popular sysmon configuration (https://github.com/SwiftOnSecurity/sysmon-config), but it is worth verifying. You can also use other repo, e.g. https://github.com/Neo23x0/sysmon-config, https://github.com/olafhartong/sysmon-modular. How to test detection? You can always use Cobalt Strike, but also you can check powershell script from this site https://svch0st.medium.com/guide-to-named-pipes-and-hunting-for-cobalt-strike-pipes-dc46b2c5f575
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection|T1055]]

## Detection

```yaml
selection_MSSE:
  PipeName|contains|all:
  - \MSSE-
  - -server
selection_postex:
  PipeName|startswith: \postex_
selection_status:
  PipeName|startswith: \status_
selection_msagent:
  PipeName|startswith: \msagent_
selection_mojo:
  PipeName|startswith: \mojo_
selection_interprocess:
  PipeName|startswith: \interprocess_
selection_samr:
  PipeName|startswith: \samr_
selection_netlogon:
  PipeName|startswith: \netlogon_
selection_srvsvc:
  PipeName|startswith: \srvsvc_
selection_lsarpc:
  PipeName|startswith: \lsarpc_
selection_wkssvc:
  PipeName|startswith: \wkssvc_
condition: 1 of selection*
```

## False Positives

- Unknown

## References

- https://twitter.com/d4rksystem/status/1357010969264873472
- https://labs.f-secure.com/blog/detecting-cobalt-strike-default-modules-via-named-pipe-analysis/
- https://github.com/SigmaHQ/sigma/issues/253
- https://blog.cobaltstrike.com/2021/02/09/learn-pipe-fitting-for-all-of-your-offense-projects/
- https://redcanary.com/threat-detection-report/threats/cobalt-strike/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/pipe_created/pipe_created_hktl_cobaltstrike.yml)
