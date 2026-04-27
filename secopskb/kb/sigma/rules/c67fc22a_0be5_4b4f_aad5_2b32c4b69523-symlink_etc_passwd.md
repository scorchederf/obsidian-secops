---
sigma_id: "c67fc22a-0be5-4b4f-aad5-2b32c4b69523"
title: "Symlink Etc Passwd"
framework: "sigma"
generated: "true"
source_path: "rules/linux/builtin/lnx_symlink_etc_passwd.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_symlink_etc_passwd.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "linux"
aliases:
  - "c67fc22a-0be5-4b4f-aad5-2b32c4b69523"
  - "Symlink Etc Passwd"
attack_technique_ids:
  - "T1204.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious command lines that look as if they would create symbolic links to /etc/passwd

## Logsource

- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution#^t1204001-malicious-link|T1204.001: Malicious Link]]

## Detection

```yaml
keywords:
- ln -s -f /etc/passwd
- ln -s /etc/passwd
condition: keywords
```

## False Positives

- Unknown

## References

- https://www.qualys.com/2021/05/04/21nails/21nails.txt

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_symlink_etc_passwd.yml)
