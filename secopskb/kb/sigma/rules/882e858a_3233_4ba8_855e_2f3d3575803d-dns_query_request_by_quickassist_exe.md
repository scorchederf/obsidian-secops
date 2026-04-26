---
sigma_id: "882e858a-3233-4ba8-855e-2f3d3575803d"
title: "DNS Query Request By QuickAssist.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/dns_query/dns_query_win_quickassist.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_quickassist.yml"
build_date: "2026-04-26 14:14:23"
status: "experimental"
level: "low"
logsource: "windows / dns_query"
aliases:
  - "882e858a-3233-4ba8-855e-2f3d3575803d"
  - "DNS Query Request By QuickAssist.EXE"
attack_technique_ids:
  - "T1071.001"
  - "T1210"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DNS Query Request By QuickAssist.EXE

Detects DNS queries initiated by "QuickAssist.exe" to Microsoft Quick Assist primary endpoint that is used to establish a session.

## Metadata

- Rule ID: 882e858a-3233-4ba8-855e-2f3d3575803d
- Status: experimental
- Level: low
- Author: Muhammad Faisal (@faisalusuf)
- Date: 2024-12-19
- Source Path: rules/windows/dns_query/dns_query_win_quickassist.yml

## Logsource

- category: dns_query
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.001]]
- [[kb/attack/techniques/T1210-exploitation_of_remote_services|T1210]]

## Detection

```yaml
selection:
  Image|endswith: \QuickAssist.exe
  QueryName|endswith: remoteassistance.support.services.microsoft.com
condition: selection
```

## False Positives

- Legitimate use of Quick Assist in the environment.

## References

- https://www.microsoft.com/en-us/security/blog/2024/05/15/threat-actors-misusing-quick-assist-in-social-engineering-attacks-leading-to-ransomware/
- https://www.linkedin.com/posts/kevin-beaumont-security_ive-been-assisting-a-few-orgs-hit-with-successful-activity-7268055739116445701-xxjZ/
- https://x.com/cyb3rops/status/1862406110365245506
- https://learn.microsoft.com/en-us/windows/client-management/client-tools/quick-assist

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_quickassist.yml)
