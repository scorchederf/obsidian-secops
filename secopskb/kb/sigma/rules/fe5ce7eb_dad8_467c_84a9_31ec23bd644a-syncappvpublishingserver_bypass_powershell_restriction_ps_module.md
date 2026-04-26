---
sigma_id: "fe5ce7eb-dad8-467c-84a9-31ec23bd644a"
title: "SyncAppvPublishingServer Bypass Powershell Restriction - PS Module"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_module/posh_pm_syncappvpublishingserver_exe.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_syncappvpublishingserver_exe.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / ps_module"
aliases:
  - "fe5ce7eb-dad8-467c-84a9-31ec23bd644a"
  - "SyncAppvPublishingServer Bypass Powershell Restriction - PS Module"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# SyncAppvPublishingServer Bypass Powershell Restriction - PS Module

Detects SyncAppvPublishingServer process execution which usually utilized by adversaries to bypass PowerShell execution restrictions.

## Metadata

- Rule ID: fe5ce7eb-dad8-467c-84a9-31ec23bd644a
- Status: test
- Level: medium
- Author: Ensar Şamil, @sblmsrsn, OSCD Community
- Date: 2020-10-05
- Modified: 2022-12-02
- Source Path: rules/windows/powershell/powershell_module/posh_pm_syncappvpublishingserver_exe.yml

## Logsource

- category: ps_module
- definition: 0ad03ef1-f21b-4a79-8ce8-e6900c54b65b
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  ContextInfo|contains: SyncAppvPublishingServer.exe
condition: selection
```

## False Positives

- App-V clients

## References

- https://lolbas-project.github.io/lolbas/Binaries/Syncappvpublishingserver/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_syncappvpublishingserver_exe.yml)
