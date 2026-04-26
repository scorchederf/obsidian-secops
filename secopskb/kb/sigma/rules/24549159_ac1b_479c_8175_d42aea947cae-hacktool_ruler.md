---
sigma_id: "24549159-ac1b-479c-8175-d42aea947cae"
title: "Hacktool Ruler"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_alert_ruler.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_alert_ruler.yml"
build_date: "2026-04-26 15:01:45"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "24549159-ac1b-479c-8175-d42aea947cae"
  - "Hacktool Ruler"
attack_technique_ids:
  - "T1087"
  - "T1114"
  - "T1059"
  - "T1550.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Hacktool Ruler

This events that are generated when using the hacktool Ruler by Sensepost

## Metadata

- Rule ID: 24549159-ac1b-479c-8175-d42aea947cae
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2017-05-31
- Modified: 2022-10-09
- Source Path: rules/windows/builtin/security/win_security_alert_ruler.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1087-account_discovery|T1087]]
- [[kb/attack/techniques/T1114-email_collection|T1114]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]
- [[kb/attack/techniques/T1550-use_alternate_authentication_material|T1550.002]]

## Detection

```yaml
selection1:
  EventID: 4776
  Workstation: RULER
selection2:
  EventID:
  - 4624
  - 4625
  WorkstationName: RULER
condition: (1 of selection*)
```

## False Positives

- Go utilities that use staaldraad awesome NTLM library

## References

- https://github.com/sensepost/ruler
- https://github.com/sensepost/ruler/issues/47
- https://github.com/staaldraad/go-ntlm/blob/cd032d41aa8ce5751c07cb7945400c0f5c81e2eb/ntlm/ntlmv1.go#L427
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4776
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4624

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_alert_ruler.yml)
