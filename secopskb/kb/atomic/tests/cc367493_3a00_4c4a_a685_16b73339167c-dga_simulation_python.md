---
atomic_guid: "cc367493-3a00-4c4a-a685-16b73339167c"
title: "DGA Simulation (Python)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1568.002"
attack_technique_name: "Dynamic Resolution: Domain Generation Algorithms"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1568.002/T1568.002.yaml"
build_date: "2026-04-27 19:12:28"
executor: "bash"
aliases:
  - "cc367493-3a00-4c4a-a685-16b73339167c"
  - "DGA Simulation (Python)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Simulates Domain Generation Algorithm (DGA) traffic by generating pseudo-random domains based on the current date and querying them using dig. 
This is designed to trigger DNS analytics and NGIDS.

## ATT&CK Mapping

- [[kb/attack/techniques/T1568-dynamic_resolution#^t1568002-domain-generation-algorithms|T1568.002: Domain Generation Algorithms]]

## Input Arguments

### python_script_path

- description: Full path to the DGA python script
- type: string
- default: PathToAtomicsFolder/T1568.002/src/T1568.002.py

## Dependencies

#{python_script_path} must exist on system.

### Prerequisite Check

```bash
if [ -f "#{python_script_path}" ]; then exit 0; else exit 1; fi
```

### Get Prerequisite

```bash
mkdir -p "$(dirname "#{python_script_path}")"
curl -sL "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1568.002/src/T1568.002.py" -o "#{python_script_path}"
```

Python 3 must be installed to run the script.

### Prerequisite Check

```bash
which python3
```

### Get Prerequisite

```bash
sudo apt-get update && sudo apt-get install -y python3
```

## Executor

- elevation_required: False
- name: bash

### Command

```bash
python3 "#{python_script_path}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1568.002/T1568.002.yaml)
