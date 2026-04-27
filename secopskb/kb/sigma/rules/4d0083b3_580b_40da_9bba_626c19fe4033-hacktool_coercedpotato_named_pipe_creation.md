---
sigma_id: "4d0083b3-580b-40da-9bba-626c19fe4033"
title: "HackTool - CoercedPotato Named Pipe Creation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/pipe_created/pipe_created_hktl_coercedpotato.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/pipe_created/pipe_created_hktl_coercedpotato.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / pipe_created"
aliases:
  - "4d0083b3-580b-40da-9bba-626c19fe4033"
  - "HackTool - CoercedPotato Named Pipe Creation"
attack_technique_ids:
  - "T1055"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# HackTool - CoercedPotato Named Pipe Creation

Detects the pattern of a pipe name as used by the hack tool CoercedPotato

## Metadata

- Rule ID: 4d0083b3-580b-40da-9bba-626c19fe4033
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2023-10-11
- Source Path: rules/windows/pipe_created/pipe_created_hktl_coercedpotato.yml

## Logsource

- category: pipe_created
- definition: Note that you have to configure logging for Named Pipe Events in Sysmon config (Event ID 17 and Event ID 18). The basic configuration is in popular sysmon configuration (https://github.com/SwiftOnSecurity/sysmon-config), but it is worth verifying. You can also use other repo, e.g. https://github.com/Neo23x0/sysmon-config, https://github.com/olafhartong/sysmon-modular. How to test detection? You can check powershell script from this site https://svch0st.medium.com/guide-to-named-pipes-and-hunting-for-cobalt-strike-pipes-dc46b2c5f575
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection|T1055]]

## Detection

```yaml
selection:
  PipeName|contains: \coerced\
condition: selection
```

## False Positives

- Unknown

## References

- https://blog.hackvens.fr/articles/CoercedPotato.html
- https://github.com/hackvens/CoercedPotato

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/pipe_created/pipe_created_hktl_coercedpotato.yml)
