---
atomic_guid: "f94b5ad9-911c-4eff-9718-fd21899db4f7"
title: "Network Share Discovery"
framework: "atomic"
generated: "true"
attack_technique_id: "T1135"
attack_technique_name: "Network Share Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1135/T1135.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "f94b5ad9-911c-4eff-9718-fd21899db4f7"
  - "Network Share Discovery"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Network Share Discovery

Network Share Discovery

## Metadata

- Atomic GUID: f94b5ad9-911c-4eff-9718-fd21899db4f7
- Technique: T1135: Network Share Discovery
- Platforms: macos
- Executor: sh
- Source Path: atomics/T1135/T1135.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1135-network_share_discovery|T1135]]

## Input Arguments

### computer_name

- description: Computer name to find a mount on.
- type: string
- default: computer1

## Executor

- name: sh

### Command

```bash
df -aH
smbutil view -g //#{computer_name}
showmount #{computer_name}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1135/T1135.yaml)
