---
atomic_guid: "2a5a0601-f5fb-4e2e-aa09-73282ae6afca"
title: "Copy the users GnuPG directory with rsync"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.004"
attack_technique_name: "Unsecured Credentials: Private Keys"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.004/T1552.004.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "2a5a0601-f5fb-4e2e-aa09-73282ae6afca"
  - "Copy the users GnuPG directory with rsync"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Copy the users GnuPG (.gnupg) directory on a Mac or Linux system to a staging folder using the `rsync` command.

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

## Executor

- name: sh

### Command

```bash
mkdir #{output_folder}
find #{search_path} -type d -name '.gnupg' 2>/dev/null -exec rsync -Rr {} #{output_folder} \;
exit 0
```

### Cleanup

```bash
rm -rf #{output_folder}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.004/T1552.004.yaml)
