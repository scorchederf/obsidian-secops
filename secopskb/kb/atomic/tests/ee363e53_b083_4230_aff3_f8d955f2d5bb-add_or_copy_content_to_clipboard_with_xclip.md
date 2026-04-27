---
atomic_guid: "ee363e53-b083-4230-aff3-f8d955f2d5bb"
title: "Add or copy content to clipboard with xClip"
framework: "atomic"
generated: "true"
attack_technique_id: "T1115"
attack_technique_name: "Clipboard Data"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1115/T1115.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "ee363e53-b083-4230-aff3-f8d955f2d5bb"
  - "Add or copy content to clipboard with xClip"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Utilize Linux Xclip to copy history and place in clipboard then output to a history.txt file. Successful execution will capture history and output to a file on disk.

## ATT&CK Mapping

- [[kb/attack/techniques/T1115-clipboard_data|T1115: Clipboard Data]]

## Executor

- name: sh

### Command

```bash
apt install xclip -y
history | tail -n 30 | xclip -sel clip
xclip -o > history.txt
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1115/T1115.yaml)
