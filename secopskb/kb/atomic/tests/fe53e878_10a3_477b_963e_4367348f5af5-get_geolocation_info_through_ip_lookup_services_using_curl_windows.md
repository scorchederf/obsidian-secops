---
atomic_guid: "fe53e878-10a3-477b-963e-4367348f5af5"
title: "Get geolocation info through IP-Lookup services using curl Windows"
framework: "atomic"
generated: "true"
attack_technique_id: "T1614"
attack_technique_name: "System Location Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1614/T1614.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "fe53e878-10a3-477b-963e-4367348f5af5"
  - "Get geolocation info through IP-Lookup services using curl Windows"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Get geolocation info through IP-Lookup services using curl Windows

Get geolocation info through IP-Lookup services using curl Windows. The default URL of the IP-Lookup service is https://ipinfo.io/. References: https://securelist.com/transparent-tribe-part-1/98127/ and https://news.sophos.com/en-us/2016/05/03/location-based-ransomware-threat-research/

## Metadata

- Atomic GUID: fe53e878-10a3-477b-963e-4367348f5af5
- Technique: T1614: System Location Discovery
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1614/T1614.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1614-system_location_discovery|T1614]]

## Input Arguments

### curl_path

- description: path to curl.exe
- type: path
- default: C:\Windows\System32\Curl.exe

### ip_lookup_url

- description: URL of the IP-Lookup service
- type: url
- default: https://ipinfo.io/

## Dependencies

Curl must be installed on system.

### Prerequisite Check

```text
if (Test-Path #{curl_path}) {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://curl.se/windows/dl-8.4.0_6/curl-8.4.0_6-win64-mingw.zip" -Outfile "PathToAtomicsFolder\..\ExternalPayloads\curl.zip"
Expand-Archive -Path "PathToAtomicsFolder\..\ExternalPayloads\curl.zip" -DestinationPath "PathToAtomicsFolder\..\ExternalPayloads\curl"
Copy-Item "PathToAtomicsFolder\..\ExternalPayloads\curl\curl-8.4.0_6-win64-mingw\bin\curl.exe" C:\Windows\System32\Curl.exe
```

## Executor

- elevation_required: False
- name: command_prompt

### Command

```commandprompt
#{curl_path} -k #{ip_lookup_url}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1614/T1614.yaml)
