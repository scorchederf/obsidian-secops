---
sigma_id: "6cc5fceb-9a71-4c23-aeeb-963abe0b279c"
title: "Suspicious Use of /dev/tcp"
framework: "sigma"
generated: "true"
source_path: "rules/linux/builtin/lnx_susp_dev_tcp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_susp_dev_tcp.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "linux"
aliases:
  - "6cc5fceb-9a71-4c23-aeeb-963abe0b279c"
  - "Suspicious Use of /dev/tcp"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Use of /dev/tcp

Detects suspicious command with /dev/tcp

## Metadata

- Rule ID: 6cc5fceb-9a71-4c23-aeeb-963abe0b279c
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-12-10
- Modified: 2023-01-06
- Source Path: rules/linux/builtin/lnx_susp_dev_tcp.yml

## Logsource

- product: linux

## Detection

```yaml
keywords:
- cat </dev/tcp/
- exec 3<>/dev/tcp/
- echo >/dev/tcp/
- bash -i >& /dev/tcp/
- sh -i >& /dev/udp/
- 0<&196;exec 196<>/dev/tcp/
- exec 5<>/dev/tcp/
- (sh)0>/dev/tcp/
- bash -c 'bash -i >& /dev/tcp/
- echo -e '#!/bin/bash\nbash -i >& /dev/tcp/
condition: keywords
```

## False Positives

- Unknown

## References

- https://www.andreafortuna.org/2021/03/06/some-useful-tips-about-dev-tcp/
- https://book.hacktricks.xyz/shells/shells/linux
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1046/T1046.md#atomic-test-1---port-scan

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_susp_dev_tcp.yml)
