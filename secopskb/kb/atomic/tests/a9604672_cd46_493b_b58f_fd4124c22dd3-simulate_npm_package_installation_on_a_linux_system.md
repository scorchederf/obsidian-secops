---
atomic_guid: "a9604672-cd46-493b-b58f-fd4124c22dd3"
title: "Simulate npm package installation on a Linux system"
framework: "atomic"
generated: "true"
attack_technique_id: "T1195.002"
attack_technique_name: "Compromise Software Supply Chain"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1195.002/T1195.002.yaml"
build_date: "2026-04-26 14:38:40"
executor: "bash"
aliases:
  - "a9604672-cd46-493b-b58f-fd4124c22dd3"
  - "Simulate npm package installation on a Linux system"
platforms:
  - "containers"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Simulate npm package installation on a Linux system

Launches a short‑lived Kubernetes pod using the Node 18 image, initializes a minimal npm project in /tmp/test, and installs the specified npm package without audit/fund/package‑lock options, simulating potentially suspicious package retrieval (e.g., typosquatting/dependency confusion) from within a container. The pod is deleted after execution.

## Metadata

- Atomic GUID: a9604672-cd46-493b-b58f-fd4124c22dd3
- Technique: T1195.002: Compromise Software Supply Chain
- Platforms: containers, linux
- Executor: bash
- Elevation Required: False
- Source Path: atomics/T1195.002/T1195.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1195-supply_chain_compromise|T1195.002]]

## Input Arguments

### image_name

- description: Name of the image
- type: string
- default: node:18

### package_name

- description: NPM package to install
- type: string
- default: tinycolor

### pod_name

- description: Name of the pod
- type: string
- default: atomic-npm-install

## Dependencies

kubectl must be installed and configured

### Prerequisite Check

```text
which kubectl
```

### Get Prerequisite

```text
echo "kubectl must be installed"
```

## Executor

- elevation_required: False
- name: bash

### Command

```bash
kubectl run #{pod_name} --image=#{image_name} --restart=Never --attach --rm -i -- bash -lc "mkdir -p /tmp/test && cd /tmp/test && npm init -y >/dev/null 2>&1 && echo '--- package.json before install ---' && cat package.json && npm install #{package_name} --no-audit --no-fund --no-package-lock && echo '--- package.json after install ---' && cat package.json"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1195.002/T1195.002.yaml)
