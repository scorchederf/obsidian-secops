---
sigma_id: "e8ebd53a-30c2-45bd-81bb-74befba07bdb"
title: "HTTP Logging Disabled On IIS Server"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/iis-configuration/win_iis_logging_http_disabled.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/iis-configuration/win_iis_logging_http_disabled.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / iis-configuration"
aliases:
  - "e8ebd53a-30c2-45bd-81bb-74befba07bdb"
  - "HTTP Logging Disabled On IIS Server"
attack_technique_ids:
  - "T1562.002"
  - "T1505.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HTTP Logging Disabled On IIS Server

Detects changes to of the IIS server configuration in order to disable HTTP logging for successful requests.

## Metadata

- Rule ID: e8ebd53a-30c2-45bd-81bb-74befba07bdb
- Status: test
- Level: high
- Author: frack113
- Date: 2024-10-06
- Source Path: rules/windows/builtin/iis-configuration/win_iis_logging_http_disabled.yml

## Logsource

- product: windows
- service: iis-configuration

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.002]]
- [[kb/attack/techniques/T1505-server_software_component|T1505.004]]

## Detection

```yaml
selection:
  EventID: 29
  Configuration: /system.webServer/httpLogging/@dontLog
  NewValue: 'true'
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/iis/manage/provisioning-and-managing-iis/configure-logging-in-iis
- https://www.microsoft.com/en-us/security/blog/2022/12/12/iis-modules-the-evolution-of-web-shells-and-how-to-detect-them/
- https://learn.microsoft.com/en-us/iis/configuration/system.webserver/httplogging

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/iis-configuration/win_iis_logging_http_disabled.yml)
