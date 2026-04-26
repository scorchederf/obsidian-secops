---
sigma_id: "d4488827-73af-4f8d-9244-7b7662ef046e"
title: "Change User Agents with WebRequest"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_invoke_webrequest_useragent.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_invoke_webrequest_useragent.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "d4488827-73af-4f8d-9244-7b7662ef046e"
  - "Change User Agents with WebRequest"
attack_technique_ids:
  - "T1071.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Change User Agents with WebRequest

Adversaries may communicate using application layer protocols associated with web traffic to avoid detection/network filtering by blending in with existing traffic.
Commands to the remote system, and often the results of those commands, will be embedded within the protocol traffic between the client and server.

## Metadata

- Rule ID: d4488827-73af-4f8d-9244-7b7662ef046e
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-23
- Modified: 2025-07-18
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_invoke_webrequest_useragent.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.001]]

## Detection

```yaml
selection_webrequest:
  ScriptBlockText|contains:
  - Invoke-WebRequest
  - Invoke-RestMethod
  - ' irm '
  - 'iwr '
selection_useragent:
  ScriptBlockText|contains: '-UserAgent '
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1071.001/T1071.001.md#t1071001---web-protocols

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_invoke_webrequest_useragent.yml)
