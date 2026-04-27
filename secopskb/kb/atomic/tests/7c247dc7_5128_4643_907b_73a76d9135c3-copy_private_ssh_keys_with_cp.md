---
atomic_guid: "7c247dc7-5128-4643-907b-73a76d9135c3"
title: "Copy Private SSH Keys with CP"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.004"
attack_technique_name: "Unsecured Credentials: Private Keys"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.004/T1552.004.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "7c247dc7-5128-4643-907b-73a76d9135c3"
  - "Copy Private SSH Keys with CP"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Copy private SSH keys on a Linux system to a staging folder using the `cp` command.

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials#^t1552004-private-keys|T1552.004: Private Keys]]

## Input Arguments

### output_folder

- description: Output folder containing copies of SSH private key files
- type: path
- default: /tmp/art-staging

### search_path

- description: Path where to start searching from.
- type: path
- default: /

## Executor

- name: sh

### Command

```bash
mkdir #{output_folder}
find #{search_path} -name id_rsa 2>/dev/null -exec cp --parents {} #{output_folder} \;
exit 0
```

### Cleanup

```bash
rm -rf #{output_folder}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.004/T1552.004.yaml)
