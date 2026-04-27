---
sigma_id: "637f689e-b4a5-4a86-be0e-0100a0a33ba2"
title: "HackTool - EfsPotato Named Pipe Creation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/pipe_created/pipe_created_hktl_efspotato.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/pipe_created/pipe_created_hktl_efspotato.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / pipe_created"
aliases:
  - "637f689e-b4a5-4a86-be0e-0100a0a33ba2"
  - "HackTool - EfsPotato Named Pipe Creation"
attack_technique_ids:
  - "T1055"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the pattern of a pipe name as used by the hack tool EfsPotato

## Logsource

- category: pipe_created
- definition: Note that you have to configure logging for Named Pipe Events in Sysmon config (Event ID 17 and Event ID 18). The basic configuration is in popular sysmon configuration (https://github.com/SwiftOnSecurity/sysmon-config), but it is worth verifying. You can also use other repo, e.g. https://github.com/Neo23x0/sysmon-config, https://github.com/olafhartong/sysmon-modular. How to test detection? You can check powershell script from this site https://svch0st.medium.com/guide-to-named-pipes-and-hunting-for-cobalt-strike-pipes-dc46b2c5f575
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection|T1055: Process Injection]]

## Detection

```yaml
selection:
  PipeName|contains:
  - \pipe\
  - \pipe\srvsvc
filter_optional_ctx:
  PipeName|contains: \CtxShare
filter_optional_default:
  PipeName|startswith: \pipe\
condition: selection and not 1 of filter_optional_*
```

## False Positives

- \pipe\LOCAL\Monitorian

## References

- https://twitter.com/SBousseaden/status/1429530155291193354?s=20
- https://github.com/zcgonvh/EfsPotato

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/pipe_created/pipe_created_hktl_efspotato.yml)
