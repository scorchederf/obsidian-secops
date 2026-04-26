---
sigma_id: "dddfebae-c46f-439c-af7a-fdb6bde90218"
title: "SyncAppvPublishingServer Execution to Bypass Powershell Restriction"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_syncappvpublishingserver_exe.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_syncappvpublishingserver_exe.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "dddfebae-c46f-439c-af7a-fdb6bde90218"
  - "SyncAppvPublishingServer Execution to Bypass Powershell Restriction"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# SyncAppvPublishingServer Execution to Bypass Powershell Restriction

Detects SyncAppvPublishingServer process execution which usually utilized by adversaries to bypass PowerShell execution restrictions.

## Metadata

- Rule ID: dddfebae-c46f-439c-af7a-fdb6bde90218
- Status: test
- Level: medium
- Author: Ensar Şamil, @sblmsrsn, OSCD Community
- Date: 2020-10-05
- Modified: 2022-12-25
- Source Path: rules/windows/powershell/powershell_script/posh_ps_syncappvpublishingserver_exe.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  ScriptBlockText|contains: SyncAppvPublishingServer.exe
condition: selection
```

## False Positives

- App-V clients

## References

- https://lolbas-project.github.io/lolbas/Binaries/Syncappvpublishingserver/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_syncappvpublishingserver_exe.yml)
