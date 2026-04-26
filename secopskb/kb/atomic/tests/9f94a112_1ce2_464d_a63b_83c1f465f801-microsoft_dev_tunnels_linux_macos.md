---
atomic_guid: "9f94a112-1ce2-464d-a63b-83c1f465f801"
title: "Microsoft Dev tunnels (Linux/macOS)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1572"
attack_technique_name: "Protocol Tunneling"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1572/T1572.yaml"
build_date: "2026-04-26 14:38:40"
executor: "bash"
aliases:
  - "9f94a112-1ce2-464d-a63b-83c1f465f801"
  - "Microsoft Dev tunnels (Linux/macOS)"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Microsoft Dev tunnels (Linux/macOS)

Dev Tunnels enables insiders as well as threat actors to expose local ports over the internet via Microsoft dev tunnels.

This atomic will generate a dev tunnel binding it to the local service running on the provided port. Can be used to expose local services, web applications and local files etc.
Reference:
- [Microsoft Docs](https://learn.microsoft.com/en-us/tunnels/dev-tunnels-overview)
- [LOT Tunnels](https://lottunnels.github.io/lottunnels/Binaries/devtunnels/)

## Metadata

- Atomic GUID: 9f94a112-1ce2-464d-a63b-83c1f465f801
- Technique: T1572: Protocol Tunneling
- Platforms: linux, macos
- Executor: bash
- Source Path: atomics/T1572/T1572.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1572-protocol_tunneling|T1572]]

## Input Arguments

### binary_path

- description: path to download devtunnel
- type: string
- default: PathToAtomicsFolder/../ExternalPayloads/devtunnel

### download_url

- description: link to download devtunnel
- type: string
- default: https://aka.ms/TunnelsCliDownload/linux-x64

### port

- description: port number for tunnel
- type: integer
- default: 8080

## Dependencies

Download devtunnel

### Prerequisite Check

```text
test -f #{binary_path}
```

### Get Prerequisite

```text
mkdir -p $(dirname #{binary_path})
curl -L "#{download_url}" -o "#{binary_path}"
chmod +x #{binary_path}
```

Login to Microsoft Dev tunnels

### Prerequisite Check

```text
#{binary_path} user show | grep -q "Not logged in" && exit 1 || exit 0
```

### Get Prerequisite

```text
echo "Login to devtunnel using the following command: #{binary_path} user login"
```

## Executor

- name: bash

### Command

```bash
#{binary_path} host -p #{port} &
```

### Cleanup

```bash
pkill -9 $(basename "#{binary_path}")
#{binary_path} user logout
rm #{binary_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1572/T1572.yaml)
