---
atomic_guid: "864bb0b2-6bb5-489a-b43b-a77b3a16d68a"
title: "Copy Private SSH Keys with rsync"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.004"
attack_technique_name: "Unsecured Credentials: Private Keys"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.004/T1552.004.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "864bb0b2-6bb5-489a-b43b-a77b3a16d68a"
  - "Copy Private SSH Keys with rsync"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Copy Private SSH Keys with rsync

Copy private SSH keys on a Linux or macOS system to a staging folder using the `rsync` command.

## Metadata

- Atomic GUID: 864bb0b2-6bb5-489a-b43b-a77b3a16d68a
- Technique: T1552.004: Unsecured Credentials: Private Keys
- Platforms: macos, linux
- Executor: sh
- Source Path: atomics/T1552.004/T1552.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.004]]

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
find #{search_path} -name id_rsa 2>/dev/null -exec rsync -R {} #{output_folder} \;
exit 0
```

### Cleanup

```bash
rm -rf #{output_folder}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.004/T1552.004.yaml)
