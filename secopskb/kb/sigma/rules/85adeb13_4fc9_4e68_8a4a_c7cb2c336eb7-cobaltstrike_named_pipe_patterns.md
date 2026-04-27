---
sigma_id: "85adeb13-4fc9-4e68-8a4a-c7cb2c336eb7"
title: "CobaltStrike Named Pipe Patterns"
framework: "sigma"
generated: "true"
source_path: "rules/windows/pipe_created/pipe_created_hktl_cobaltstrike_susp_pipe_patterns.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/pipe_created/pipe_created_hktl_cobaltstrike_susp_pipe_patterns.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / pipe_created"
aliases:
  - "85adeb13-4fc9-4e68-8a4a-c7cb2c336eb7"
  - "CobaltStrike Named Pipe Patterns"
attack_technique_ids:
  - "T1055"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# CobaltStrike Named Pipe Patterns

Detects the creation of a named pipe with a pattern found in CobaltStrike malleable C2 profiles

## Metadata

- Rule ID: 85adeb13-4fc9-4e68-8a4a-c7cb2c336eb7
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Christian Burkard (Nextron Systems)
- Date: 2021-07-30
- Modified: 2024-01-26
- Source Path: rules/windows/pipe_created/pipe_created_hktl_cobaltstrike_susp_pipe_patterns.yml

## Logsource

- category: pipe_created
- definition: Note that you have to configure logging for Named Pipe Events in Sysmon config (Event ID 17 and Event ID 18). The basic configuration is in popular sysmon configuration (https://github.com/SwiftOnSecurity/sysmon-config), but it is worth verifying. You can also use other repo, e.g. https://github.com/Neo23x0/sysmon-config, https://github.com/olafhartong/sysmon-modular You can also use other repo, e.g. https://github.com/Neo23x0/sysmon-config, https://github.com/olafhartong/sysmon-modular. How to test detection? You can always use Cobalt Strike, but also you can check powershell script from this site https://svch0st.medium.com/guide-to-named-pipes-and-hunting-for-cobalt-strike-pipes-dc46b2c5f575
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection|T1055]]

## Detection

```yaml
selection_malleable_profile_generic:
- PipeName|startswith:
  - \DserNamePipe
  - \f4c3
  - \f53f
  - \fullduplex_
  - \mojo.5688.8052.183894939787088877
  - \mojo.5688.8052.35780273329370473
  - \MsFteWds
  - \msrpc_
  - \mypipe-f
  - \mypipe-h
  - \ntsvcs
  - \PGMessagePipe
  - \rpc_
  - \scerpc
  - \SearchTextHarvester
  - \spoolss
  - \win_svc
  - \win\msrpc_
  - \windows.update.manager
  - \wkssvc
- PipeName:
  - \demoagent_11
  - \demoagent_22
selection_malleable_profile_catalog_change_listener:
  PipeName|startswith: \Winsock2\CatalogChangeListener-
  PipeName|endswith: -0,
filter_main_generic:
  PipeName:
  - \wkssvc
  - \spoolss
  - \scerpc
  - \ntsvcs
  - \SearchTextHarvester
  - \PGMessagePipe
  - \MsFteWds
filter_optional_websense:
  Image|contains:
  - :\Program Files\Websense\
  - :\Program Files (x86)\Websense\
  PipeName|startswith:
  - \DserNamePipeR
  - \DserNamePipeW
condition: 1 of selection_malleable_profile_* and not 1 of filter_main_* and not 1
  of filter_optional_*
```

## False Positives

- Chrome instances using the exact same pipe name "mojo.xxx"
- Websense Endpoint using the pipe name "DserNamePipe(R|W)\d{1,5}"

## References

- https://svch0st.medium.com/guide-to-named-pipes-and-hunting-for-cobalt-strike-pipes-dc46b2c5f575
- https://gist.github.com/MHaggis/6c600e524045a6d49c35291a21e10752

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/pipe_created/pipe_created_hktl_cobaltstrike_susp_pipe_patterns.yml)
