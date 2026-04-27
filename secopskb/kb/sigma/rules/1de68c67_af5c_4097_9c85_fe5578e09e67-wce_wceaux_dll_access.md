---
sigma_id: "1de68c67-af5c-4097-9c85-fe5578e09e67"
title: "WCE wceaux.dll Access"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_mal_wceaux_dll.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_mal_wceaux_dll.yml"
build_date: "2026-04-27 19:13:59"
status: "test"
level: "critical"
logsource: "windows / security"
aliases:
  - "1de68c67-af5c-4097-9c85-fe5578e09e67"
  - "WCE wceaux.dll Access"
attack_technique_ids:
  - "T1003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects wceaux.dll access while WCE pass-the-hash remote command execution on source host

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003: OS Credential Dumping]]

### Software Tags

- S0005

## Detection

```yaml
selection:
  EventID:
  - 4656
  - 4663
  ObjectName|endswith: \wceaux.dll
condition: selection
```

## False Positives

- Unknown

## References

- https://www.jpcert.or.jp/english/pub/sr/ir_research.html
- https://jpcertcc.github.io/ToolAnalysisResultSheet

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_mal_wceaux_dll.yml)
