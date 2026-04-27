---
atomic_guid: "b05ac39b-515f-48e9-88e9-2f141b5bcad0"
title: "Copy the users GnuPG directory with rsync (freebsd)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.004"
attack_technique_name: "Unsecured Credentials: Private Keys"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.004/T1552.004.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "b05ac39b-515f-48e9-88e9-2f141b5bcad0"
  - "Copy the users GnuPG directory with rsync (freebsd)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Copy the users GnuPG (.gnupg) directory on a FreeBSD system to a staging folder using the `rsync` command.

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials#^t1552004-private-keys|T1552.004: Private Keys]]

## Input Arguments

### output_folder

- description: Output folder containing a copy of the .gnupg directory
- type: path
- default: /tmp/GnuPG

### search_path

- description: Path where to start searching from
- type: path
- default: /

## Dependencies

Check if rsync is installed.

### Prerequisite Check

```bash
if [ ! -x "$(command -v rsync)" ]; then exit 1; else exit 0; fi;
```

### Get Prerequisite

```bash
(which pkg && pkg install -y rsync)
```

## Executor

- name: sh

### Command

```bash
mkdir #{output_folder}
find #{search_path} -type d -name '.gnupg' 2>/dev/null -exec rsync -Rr {} #{output_folder} \;
```

### Cleanup

```bash
rm -rf #{output_folder}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.004/T1552.004.yaml)
