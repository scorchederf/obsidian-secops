---
sigma_id: "fa4aaed5-4fe0-498d-bbc0-08e3346387ba"
title: "Copy Passwd Or Shadow From TMP Path"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_cp_passwd_or_shadow_tmp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_cp_passwd_or_shadow_tmp.yml"
build_date: "2026-04-26 17:03:18"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Copy Passwd Or Shadow From TMP Path

Detects when the file "passwd" or "shadow" is copied from tmp path

## Metadata

- Rule ID: fa4aaed5-4fe0-498d-bbc0-08e3346387ba
- Status: test
- Level: high
- Author: Joseliyo Sanchez, @Joseliyo_Jstnk
- Date: 2023-01-31
- Source Path: rules/linux/process_creation/proc_creation_lnx_cp_passwd_or_shadow_tmp.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.001]]

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
