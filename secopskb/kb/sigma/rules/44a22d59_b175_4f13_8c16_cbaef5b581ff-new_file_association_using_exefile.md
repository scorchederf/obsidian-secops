---
sigma_id: "44a22d59-b175-4f13-8c16-cbaef5b581ff"
title: "New File Association Using Exefile"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_file_association_exefile.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_file_association_exefile.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "44a22d59-b175-4f13-8c16-cbaef5b581ff"
  - "New File Association Using Exefile"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the abuse of the exefile handler in new file association. Used for bypass of security products.

## Logsource

- category: registry_set
- product: windows

## Detection

```yaml
selection:
  TargetObject|contains: Classes\.
  Details: exefile
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/mrd0x/status/1461041276514623491

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_file_association_exefile.yml)
