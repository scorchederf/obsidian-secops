---
sigma_id: "c8557060-9221-4448-8794-96320e6f3e74"
title: "Windows PowerShell User Agent"
framework: "sigma"
generated: "true"
source_path: "rules/web/proxy_generic/proxy_ua_powershell.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_ua_powershell.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "proxy"
aliases:
  - "c8557060-9221-4448-8794-96320e6f3e74"
  - "Windows PowerShell User Agent"
attack_technique_ids:
  - "T1071.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows PowerShell User Agent

Detects Windows PowerShell Web Access

## Metadata

- Rule ID: c8557060-9221-4448-8794-96320e6f3e74
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2017-03-13
- Modified: 2021-11-27
- Source Path: rules/web/proxy_generic/proxy_ua_powershell.yml

## Logsource

- category: proxy

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.001]]

## Detection

```yaml
selection:
  c-useragent|contains: ' WindowsPowerShell/'
condition: selection
```

## False Positives

- Administrative scripts that download files from the Internet
- Administrative scripts that retrieve certain website contents

## References

- https://msdn.microsoft.com/powershell/reference/5.1/microsoft.powershell.utility/Invoke-WebRequest

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_ua_powershell.yml)
