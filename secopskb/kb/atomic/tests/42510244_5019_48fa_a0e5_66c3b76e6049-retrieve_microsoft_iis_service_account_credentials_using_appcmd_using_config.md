---
atomic_guid: "42510244-5019-48fa-a0e5-66c3b76e6049"
title: "Retrieve Microsoft IIS Service Account Credentials Using AppCmd (using config)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003"
attack_technique_name: "OS Credential Dumping"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003/T1003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "42510244-5019-48fa-a0e5-66c3b76e6049"
  - "Retrieve Microsoft IIS Service Account Credentials Using AppCmd (using config)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Retrieve Microsoft IIS Service Account Credentials Using AppCmd (using config)

AppCmd.exe is a command line utility which is used for managing an IIS web server. The config command within the tool reveals the service account credentials configured for the webserver. An adversary may use these credentials for other malicious purposes.
[Reference](https://twitter.com/0gtweet/status/1588815661085917186?cxt=HHwWhIDUyaDbzYwsAAAA)

## Metadata

- Atomic GUID: 42510244-5019-48fa-a0e5-66c3b76e6049
- Technique: T1003: OS Credential Dumping
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1003/T1003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]]

## Dependencies

IIS must be installed prior to running the test

### Prerequisite Check

```powershell
if ((Get-WindowsFeature Web-Server).InstallState -eq "Installed") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
Install-WindowsFeature -name Web-Server -IncludeManagementTools
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
C:\Windows\System32\inetsrv\appcmd.exe list apppool /config
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003/T1003.yaml)
