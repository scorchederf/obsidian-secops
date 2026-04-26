---
atomic_guid: "b95ce2eb-a093-4cd8-938d-5258cef656ea"
title: "Space After Filename"
framework: "atomic"
generated: "true"
attack_technique_id: "T1036.006"
attack_technique_name: "Masquerading: Space after Filename"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.006/T1036.006.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "b95ce2eb-a093-4cd8-938d-5258cef656ea"
  - "Space After Filename"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Space After Filename

Space after filename.

## Metadata

- Atomic GUID: b95ce2eb-a093-4cd8-938d-5258cef656ea
- Technique: T1036.006: Masquerading: Space after Filename
- Platforms: macos, linux
- Executor: sh
- Source Path: atomics/T1036.006/T1036.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1036-masquerading|T1036.006]]

## Executor

- name: sh

### Command

```bash
mkdir -p /tmp/atomic-test-T1036.006
cd /tmp/atomic-test-T1036.006
mkdir -p 'testdirwithspaceend '
[ "$(uname)" = 'FreeBSD' ] && /bin/echo "#\!/bin/sh" > "testdirwithspaceend /init " && echo 'echo "print(\"running T1035.006 with space after filename to masquerade init\")" | python3.9' >> "testdirwithspaceend /init " && echo "exit" >> "testdirwithspaceend /init " || /usr/bin/echo -e "%d\na\n#!/usr/bin/perl\nprint \"running T1035.006 with space after filename to masquerade init\\n\";\nqx/cp \/usr\/bin\/perl 'init  '/;\nqx/'.\/init  ' -e 'sleep 5'/;\n.\nwq\n" | ed 'testdirwithspaceend /init ' >/dev/null
chmod +x 'testdirwithspaceend /init '
'./testdirwithspaceend /init '
```

### Cleanup

```bash
rm -rf /tmp/atomic-test-T1036.006
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.006/T1036.006.yaml)
