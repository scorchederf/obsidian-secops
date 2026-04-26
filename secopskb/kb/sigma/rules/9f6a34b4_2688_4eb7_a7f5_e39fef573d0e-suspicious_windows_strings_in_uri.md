---
sigma_id: "9f6a34b4-2688-4eb7-a7f5-e39fef573d0e"
title: "Suspicious Windows Strings In URI"
framework: "sigma"
generated: "true"
source_path: "rules/web/webserver_generic/web_susp_windows_path_uri.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/webserver_generic/web_susp_windows_path_uri.yml"
build_date: "2026-04-26 15:01:52"
status: "test"
level: "high"
logsource: "webserver"
aliases:
  - "9f6a34b4-2688-4eb7-a7f5-e39fef573d0e"
  - "Suspicious Windows Strings In URI"
attack_technique_ids:
  - "T1505.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Windows Strings In URI

Detects suspicious Windows strings in URI which could indicate possible exfiltration or webshell communication

## Metadata

- Rule ID: 9f6a34b4-2688-4eb7-a7f5-e39fef573d0e
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-06
- Modified: 2023-01-02
- Source Path: rules/web/webserver_generic/web_susp_windows_path_uri.yml

## Logsource

- category: webserver

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1505-server_software_component|T1505.003]]

## Detection

```yaml
selection:
  cs-uri-query|contains:
  - =C:/Users
  - =C:/Program%20Files
  - =C:/Windows
  - =C%3A%5CUsers
  - =C%3A%5CProgram%20Files
  - =C%3A%5CWindows
condition: selection
```

## False Positives

- Legitimate application and websites that use windows paths in their URL

## References

- https://thedfirreport.com/2022/06/06/will-the-real-msiexec-please-stand-up-exploit-leads-to-data-exfiltration/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/webserver_generic/web_susp_windows_path_uri.yml)
