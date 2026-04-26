---
atomic_guid: "552b4db3-8850-412c-abce-ab5cc8a86604"
title: "Get geolocation info through IP-Lookup services using curl freebsd, linux or macos"
framework: "atomic"
generated: "true"
attack_technique_id: "T1614"
attack_technique_name: "System Location Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1614/T1614.yaml"
build_date: "2026-04-26 17:02:13"
executor: "bash"
aliases:
  - "552b4db3-8850-412c-abce-ab5cc8a86604"
  - "Get geolocation info through IP-Lookup services using curl freebsd, linux or macos"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Get geolocation info through IP-Lookup services using curl freebsd, linux or macos

Get geolocation info through IP-Lookup services using curl Windows. The default URL of the IP-Lookup service is https://ipinfo.io/. References: https://securelist.com/transparent-tribe-part-1/98127/ and https://news.sophos.com/en-us/2016/05/03/location-based-ransomware-threat-research/

## Metadata

- Atomic GUID: 552b4db3-8850-412c-abce-ab5cc8a86604
- Technique: T1614: System Location Discovery
- Platforms: macos, linux
- Executor: bash
- Elevation Required: False
- Source Path: atomics/T1614/T1614.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1614-system_location_discovery|T1614]]

## Input Arguments

### ip_lookup_url

- description: URL of the IP-Lookup service
- type: url
- default: https://ipinfo.io/

## Executor

- elevation_required: False
- name: bash

### Command

```bash
curl -k #{ip_lookup_url}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1614/T1614.yaml)
