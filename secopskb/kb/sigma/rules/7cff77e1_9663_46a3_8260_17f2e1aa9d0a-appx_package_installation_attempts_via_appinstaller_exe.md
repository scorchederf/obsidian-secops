---
sigma_id: "7cff77e1-9663-46a3-8260-17f2e1aa9d0a"
title: "AppX Package Installation Attempts Via AppInstaller.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/dns_query/dns_query_win_appinstaller.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_appinstaller.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / dns_query"
aliases:
  - "7cff77e1-9663-46a3-8260-17f2e1aa9d0a"
  - "AppX Package Installation Attempts Via AppInstaller.EXE"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AppX Package Installation Attempts Via AppInstaller.EXE

Detects DNS queries made by "AppInstaller.EXE". The AppInstaller is the default handler for the "ms-appinstaller" URI. It attempts to load/install a package from the referenced URL

## Metadata

- Rule ID: 7cff77e1-9663-46a3-8260-17f2e1aa9d0a
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-11-24
- Modified: 2023-11-09
- Source Path: rules/windows/dns_query/dns_query_win_appinstaller.yml

## Logsource

- category: dns_query
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection:
  Image|startswith: C:\Program Files\WindowsApps\Microsoft.DesktopAppInstaller_
  Image|endswith: \AppInstaller.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/notwhickey/status/1333900137232523264
- https://lolbas-project.github.io/lolbas/Binaries/AppInstaller/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_appinstaller.yml)
