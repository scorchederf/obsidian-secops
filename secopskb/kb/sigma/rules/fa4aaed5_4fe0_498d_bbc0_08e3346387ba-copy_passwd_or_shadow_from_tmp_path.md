---
sigma_id: "fa4aaed5-4fe0-498d-bbc0-08e3346387ba"
title: "Copy Passwd Or Shadow From TMP Path"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_cp_passwd_or_shadow_tmp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_cp_passwd_or_shadow_tmp.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "fa4aaed5-4fe0-498d-bbc0-08e3346387ba"
  - "Copy Passwd Or Shadow From TMP Path"
attack_technique_ids:
  - "T1552.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects when the file "passwd" or "shadow" is copied from tmp path

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials#^t1552001-credentials-in-files|T1552.001: Credentials In Files]]

## Detection

```yaml
selection_img:
  Image|endswith: /cp
selection_path:
  CommandLine|contains: /tmp/
selection_file:
  CommandLine|contains:
  - passwd
  - shadow
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://blogs.blackberry.com/
- https://twitter.com/Joseliyo_Jstnk/status/1620131033474822144

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_cp_passwd_or_shadow_tmp.yml)
