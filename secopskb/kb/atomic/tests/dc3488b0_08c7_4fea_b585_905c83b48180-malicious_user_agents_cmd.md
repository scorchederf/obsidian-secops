---
atomic_guid: "dc3488b0-08c7-4fea-b585-905c83b48180"
title: "Malicious User Agents - CMD"
framework: "atomic"
generated: "true"
attack_technique_id: "T1071.001"
attack_technique_name: "Application Layer Protocol: Web Protocols"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1071.001/T1071.001.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "dc3488b0-08c7-4fea-b585-905c83b48180"
  - "Malicious User Agents - CMD"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test simulates an infected host beaconing to command and control. Upon execution, no out put will be displayed. 
Use an application such as Wireshark to record the session and observe user agent strings and responses.

Inspired by APTSimulator - https://github.com/NextronSystems/APTSimulator/blob/master/test-sets/command-and-control/malicious-user-agents.bat

## ATT&CK Mapping

- [[kb/attack/techniques/T1071-application_layer_protocol#^t1071001-web-protocols|T1071.001: Web Protocols]]

## Input Arguments

### curl_path

- description: path to curl.exe
- type: path
- default: C:\Windows\System32\Curl.exe

### domain

- description: Default domain to simulate against
- type: string
- default: www.google.com

## Dependencies

Curl must be installed on system

### Prerequisite Check

```powershell
if (Test-Path #{curl_path}) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://curl.se/windows/dl-8.6.0_2/curl-8.6.0_2-win32-mingw.zip" -Outfile "PathToAtomicsFolder\..\ExternalPayloads\curl.zip"
Expand-Archive -Path "PathToAtomicsFolder\..\ExternalPayloads\curl.zip" -DestinationPath "PathToAtomicsFolder\..\ExternalPayloads\curl"
Copy-Item "PathToAtomicsFolder\..\ExternalPayloads\curl\curl-8.6.0_2-win32-mingw\bin\curl.exe" #{curl_path}
Remove-Item "PathToAtomicsFolder\..\ExternalPayloads\curl"
Remove-Item "PathToAtomicsFolder\..\ExternalPayloads\curl.zip"
```

## Executor

- name: command_prompt

### Command

```cmd
#{curl_path} -s -A "HttpBrowser/1.0" -m3 #{domain} >nul 2>&1
#{curl_path} -s -A "Wget/1.9+cvs-stable (Red Hat modified)" -m3 #{domain} >nul 2>&1
#{curl_path} -s -A "Opera/8.81 (Windows NT 6.0; U; en)" -m3 #{domain} >nul 2>&1
#{curl_path} -s -A "*<|>*" -m3 #{domain} >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1071.001/T1071.001.yaml)
