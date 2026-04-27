---
sigma_id: "4b3cb710-5e83-4715-8c45-8b2b5b3e5751"
title: "Modification of ld.so.preload"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/path/lnx_auditd_ld_so_preload_mod.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/path/lnx_auditd_ld_so_preload_mod.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "linux / auditd"
aliases:
  - "4b3cb710-5e83-4715-8c45-8b2b5b3e5751"
  - "Modification of ld.so.preload"
attack_technique_ids:
  - "T1574.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Identifies modification of ld.so.preload for shared object injection. This technique is used by attackers to load arbitrary code into processes.

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow#^t1574006-dynamic-linker-hijacking|T1574.006: Dynamic Linker Hijacking]]

## Detection

```yaml
selection:
  type: PATH
  name: /etc/ld.so.preload
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1574.006/T1574.006.md
- https://eqllib.readthedocs.io/en/latest/analytics/fd9b987a-1101-4ed3-bda6-a70300eaf57e.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/path/lnx_auditd_ld_so_preload_mod.yml)
