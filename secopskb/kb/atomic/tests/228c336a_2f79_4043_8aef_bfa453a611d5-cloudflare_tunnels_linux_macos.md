---
atomic_guid: "228c336a-2f79-4043-8aef-bfa453a611d5"
title: "Cloudflare tunnels (Linux/macOS)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1572"
attack_technique_name: "Protocol Tunneling"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1572/T1572.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "228c336a-2f79-4043-8aef-bfa453a611d5"
  - "Cloudflare tunnels (Linux/macOS)"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Cloudflare tunnels (Linux/macOS)

Cloudflared can be used for exposing local development environment/services/files over the internet.
This atomic will generate a dev tunnel binding it to the local service running on the provided port.
Reference:
- [Cloudflared Docs](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/)
- [LOT Tunnels](https://lottunnels.github.io/lottunnels/Binaries/cloudflared/)

## Metadata

- Atomic GUID: 228c336a-2f79-4043-8aef-bfa453a611d5
- Technique: T1572: Protocol Tunneling
- Platforms: linux, macos
- Executor: sh
- Source Path: atomics/T1572/T1572.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1572-protocol_tunneling|T1572]]

## Input Arguments

### additional_args

- description: Additional arguments to pass to cloudflared
- type: string

### binary_path

- description: path to download cloudflared
- type: string
- default: PathToAtomicsFolder/../ExternalPayloads/cloudflared

### cloudflared_artifact_base_url

- description: Base URL to download cloudflared
- type: string
- default: https://github.com/cloudflare/cloudflared/releases/latest/download

### url_to_tunnel

- description: IP and port to expose
- type: string
- default: localhost:8080

## Dependencies

Download cloudflared

### Prerequisite Check

```text
test -f "#{binary_path}" && exit 0 || exit 1
```

### Get Prerequisite

```text
ARCH_SUFFIX=$(uname -m | grep -q "arm64\|aarch64" && echo "arm64" || echo "amd64")
if [ "$(uname)" = "Darwin" ]
then curl -L "#{cloudflared_artifact_base_url}/cloudflared-darwin-${ARCH_SUFFIX}.tgz" -o "$(dirname #{binary_path})/cloudflared-darwin-${ARCH_SUFFIX}.tgz" 
  cd "$(dirname #{binary_path})"
  tar -xzf "cloudflared-darwin-${ARCH_SUFFIX}.tgz"
  rm -f "cloudflared-darwin-${ARCH_SUFFIX}.tgz"
  chmod +x "#{binary_path}"
elif [ "$(expr substr $(uname) 1 5)" = "Linux" ]
then mkdir -p $(dirname #{binary_path})
  curl -L "#{cloudflared_artifact_base_url}/cloudflared-linux-${ARCH_SUFFIX}" -o "#{binary_path}"
  chmod +x "#{binary_path}"
fi
```

## Executor

- name: sh

### Command

```sh
nohup #{binary_path} tunnel --url #{url_to_tunnel} #{additional_args} >/dev/null 2>&1 &
```

### Cleanup

```sh
pkill -9 $(basename "#{binary_path}")
rm -f "#{binary_path}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1572/T1572.yaml)
