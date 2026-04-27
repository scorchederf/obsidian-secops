---
atomic_guid: "46959285-906d-40fa-9437-5a439accd878"
title: "Discover Private SSH Keys"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.004"
attack_technique_name: "Unsecured Credentials: Private Keys"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.004/T1552.004.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "46959285-906d-40fa-9437-5a439accd878"
  - "Discover Private SSH Keys"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Discover private SSH keys on a FreeBSD, macOS or Linux system.

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials#^t1552004-private-keys|T1552.004: Private Keys]]

## Input Arguments

### output_file

- description: Output file containing locations of SSH key files
- type: path
- default: /tmp/keyfile_locations.txt

### search_path

- description: Path where to start searching from.
- type: path
- default: /

## Executor

- name: sh

### Command

```bash
find #{search_path} -name id_rsa 2>/dev/null >> #{output_file}
exit 0
```

### Cleanup

```bash
rm #{output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.004/T1552.004.yaml)
