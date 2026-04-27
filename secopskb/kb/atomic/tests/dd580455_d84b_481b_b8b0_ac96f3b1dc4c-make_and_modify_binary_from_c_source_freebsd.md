---
atomic_guid: "dd580455-d84b-481b-b8b0-ac96f3b1dc4c"
title: "Make and modify binary from C source (freebsd)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.001"
attack_technique_name: "Abuse Elevation Control Mechanism: Setuid and Setgid"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.001/T1548.001.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "dd580455-d84b-481b-b8b0-ac96f3b1dc4c"
  - "Make and modify binary from C source (freebsd)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Make, change owner, and change file attributes on a C source code file

## ATT&CK Mapping

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism#^t1548001-setuid-and-setgid|T1548.001: Setuid and Setgid]]

## Input Arguments

### payload

- description: hello.c payload
- type: path
- default: PathToAtomicsFolder/T1548.001/src/hello.c

## Executor

- elevation_required: True
- name: sh

### Command

```bash
cp #{payload} /tmp/hello.c
chown root /tmp/hello.c
make /tmp/hello
chown root /tmp/hello
chmod u+s /tmp/hello
/tmp/hello
```

### Cleanup

```bash
rm /tmp/hello
rm /tmp/hello.c
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.001/T1548.001.yaml)
