---
sigma_id: "9c8acf1a-cbf9-4db6-b63c-74baabe03e59"
title: "NTLM Brute Force"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/ntlm/win_susp_ntlm_brute_force.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/ntlm/win_susp_ntlm_brute_force.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / ntlm"
aliases:
  - "9c8acf1a-cbf9-4db6-b63c-74baabe03e59"
  - "NTLM Brute Force"
attack_technique_ids:
  - "T1110"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# NTLM Brute Force

Detects common NTLM brute force device names

## Metadata

- Rule ID: 9c8acf1a-cbf9-4db6-b63c-74baabe03e59
- Status: test
- Level: medium
- Author: Jerry Shockley '@jsh0x'
- Date: 2022-02-02
- Source Path: rules/windows/builtin/ntlm/win_susp_ntlm_brute_force.yml

## Logsource

- definition: Requires events from Microsoft-Windows-NTLM/Operational
- product: windows
- service: ntlm

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1110-brute_force|T1110]]

## Detection

```yaml
selection:
  EventID: 8004
devicename:
  WorkstationName:
  - Rdesktop
  - Remmina
  - Freerdp
  - Windows7
  - Windows8
  - Windows2012
  - Windows2016
  - Windows2019
condition: selection and devicename
```

## False Positives

- Systems with names equal to the spoofed ones used by the brute force tools

## References

- https://www.varonis.com/blog/investigate-ntlm-brute-force

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/ntlm/win_susp_ntlm_brute_force.yml)
