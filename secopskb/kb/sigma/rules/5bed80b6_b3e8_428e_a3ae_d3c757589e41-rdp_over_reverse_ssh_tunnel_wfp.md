---
sigma_id: "5bed80b6-b3e8-428e-a3ae-d3c757589e41"
title: "RDP over Reverse SSH Tunnel WFP"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_rdp_reverse_tunnel.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_rdp_reverse_tunnel.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "5bed80b6-b3e8-428e-a3ae-d3c757589e41"
  - "RDP over Reverse SSH Tunnel WFP"
attack_technique_ids:
  - "T1090.001"
  - "T1090.002"
  - "T1021.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# RDP over Reverse SSH Tunnel WFP

Detects svchost hosting RDP termsvcs communicating with the loopback address

## Metadata

- Rule ID: 5bed80b6-b3e8-428e-a3ae-d3c757589e41
- Status: test
- Level: high
- Author: Samir Bousseaden
- Date: 2019-02-16
- Modified: 2022-09-02
- Source Path: rules/windows/builtin/security/win_security_rdp_reverse_tunnel.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1090-proxy|T1090.001]]
- [[kb/attack/techniques/T1090-proxy|T1090.002]]
- [[kb/attack/techniques/T1021-remote_services|T1021.001]]

## Detection

```yaml
selection:
  EventID: 5156
sourceRDP:
  SourcePort: 3389
  DestAddress:
  - 127.*
  - ::1
destinationRDP:
  DestPort: 3389
  SourceAddress:
  - 127.*
  - ::1
filter_app_container:
  FilterOrigin: AppContainer Loopback
filter_thor:
  Application|endswith:
  - \thor.exe
  - \thor64.exe
condition: selection and ( sourceRDP or destinationRDP ) and not 1 of filter*
```

## False Positives

- Programs that connect locally to the RDP port

## References

- https://twitter.com/SBousseaden/status/1096148422984384514
- https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES/blob/44fbe85f72ee91582876b49678f9a26292a155fb/Command%20and%20Control/DE_RDP_Tunnel_5156.evtx

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_rdp_reverse_tunnel.yml)
