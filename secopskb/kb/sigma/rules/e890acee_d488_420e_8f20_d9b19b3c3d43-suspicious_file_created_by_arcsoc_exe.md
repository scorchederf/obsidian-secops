---
sigma_id: "e890acee-d488-420e-8f20-d9b19b3c3d43"
title: "Suspicious File Created by ArcSOC.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_arcsoc_susp_file_created.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_arcsoc_susp_file_created.yml"
build_date: "2026-04-27 19:13:56"
status: "experimental"
level: "high"
logsource: "windows / file_event"
aliases:
  - "e890acee-d488-420e-8f20-d9b19b3c3d43"
  - "Suspicious File Created by ArcSOC.exe"
attack_technique_ids:
  - "T1127"
  - "T1105"
  - "T1133"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects instances where the ArcGIS Server process ArcSOC.exe, which hosts REST services running on an ArcGIS
server, creates a file with suspicious file type, indicating that it may be an executable, script file,
or otherwise unusual.

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]
- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]
- [[kb/attack/techniques/T1133-external_remote_services|T1133: External Remote Services]]

## Detection

```yaml
selection:
  Image|endswith: \ArcSOC.exe
  TargetFilename|endswith:
  - .ahk
  - .aspx
  - .au3
  - .bat
  - .cmd
  - .dll
  - .exe
  - .hta
  - .js
  - .ps1
  - .py
  - .vbe
  - .vbs
  - .wsf
condition: selection
```

## False Positives

- Unlikely

## References

- https://reliaquest.com/blog/threat-spotlight-inside-flax-typhoons-arcgis-compromise/
- https://enterprise.arcgis.com/en/server/12.0/administer/windows/inside-an-arcgis-server-site.htm

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_arcsoc_susp_file_created.yml)
