---
sigma_id: "403c2cc0-7f6b-4925-9423-bfa573bed7eb"
title: "Suspicious PowerShell Download - Powershell Script"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_download.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "403c2cc0-7f6b-4925-9423-bfa573bed7eb"
  - "Suspicious PowerShell Download - Powershell Script"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious PowerShell Download - Powershell Script

Detects suspicious PowerShell download command

## Metadata

- Rule ID: 403c2cc0-7f6b-4925-9423-bfa573bed7eb
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2017-03-05
- Modified: 2022-12-02
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_download.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
webclient:
  ScriptBlockText|contains: System.Net.WebClient
download:
  ScriptBlockText|contains:
  - .DownloadFile(
  - .DownloadFileAsync(
  - .DownloadString(
  - .DownloadStringAsync(
condition: webclient and download
```

## False Positives

- PowerShell scripts that download content from the Internet

## References

- https://learn.microsoft.com/en-us/dotnet/api/system.net.webclient.downloadstring?view=net-8.0
- https://learn.microsoft.com/en-us/dotnet/api/system.net.webclient.downloadfile?view=net-8.0

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_download.yml)
