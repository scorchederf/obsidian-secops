---
atomic_guid: "89a7dd26-e510-4c9f-9b15-f3bae333360f"
title: "Space After Filename (Manual)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1036.006"
attack_technique_name: "Masquerading: Space after Filename"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.006/T1036.006.yaml"
build_date: "2026-04-26 17:02:12"
executor: "manual"
aliases:
  - "89a7dd26-e510-4c9f-9b15-f3bae333360f"
  - "Space After Filename (Manual)"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Space After Filename (Manual)

Space After Filename

## Metadata

- Atomic GUID: 89a7dd26-e510-4c9f-9b15-f3bae333360f
- Technique: T1036.006: Masquerading: Space after Filename
- Platforms: macos
- Executor: manual
- Source Path: atomics/T1036.006/T1036.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1036-masquerading|T1036.006]]

## Executor

- name: manual
- steps: 1. echo '#!/bin/bash\necho "print \"hello, world!\"" | /usr/bin/python\nexit' > execute.txt && chmod +x execute.txt

2. mv execute.txt "execute.txt "

3. ./execute.txt\ 


## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.006/T1036.006.yaml)
