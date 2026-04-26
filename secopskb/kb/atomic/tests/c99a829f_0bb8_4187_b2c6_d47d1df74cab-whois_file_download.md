---
atomic_guid: "c99a829f-0bb8-4187-b2c6-d47d1df74cab"
title: "whois file download"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "c99a829f-0bb8-4187-b2c6-d47d1df74cab"
  - "whois file download"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# whois file download

Download a remote file using the whois utility

## Metadata

- Atomic GUID: c99a829f-0bb8-4187-b2c6-d47d1df74cab
- Technique: T1105: Ingress Tool Transfer
- Platforms: linux, macos
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1105/T1105.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Input Arguments

### output_file

- description: Path of file to save output to
- type: path
- default: /tmp/T1105.whois.out

### query

- description: Query to send to remote server
- type: string
- default: Hello from Atomic Red Team test T1105

### remote_host

- description: Remote hostname or IP address
- type: string
- default: localhost

### remote_port

- description: Remote port to connect to
- type: integer
- default: 8443

### timeout

- description: Timeout period before ending process (seconds)
- type: integer
- default: 1

## Dependencies

The whois and timeout commands must be present

### Prerequisite Check

```text
which whois && which timeout
```

### Get Prerequisite

```text
echo "Please install timeout and the whois package"
```

## Executor

- elevation_required: False
- name: sh

### Command

```sh
timeout --preserve-status #{timeout} whois -h #{remote_host} -p #{remote_port} "#{query}" > #{output_file}
```

### Cleanup

```sh
rm -f #{output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
