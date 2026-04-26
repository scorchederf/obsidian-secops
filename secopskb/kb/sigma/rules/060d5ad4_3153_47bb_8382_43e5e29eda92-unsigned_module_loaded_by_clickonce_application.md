---
sigma_id: "060d5ad4-3153-47bb-8382-43e5e29eda92"
title: "Unsigned Module Loaded by ClickOnce Application"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_susp_clickonce_unsigned_module_loaded.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_susp_clickonce_unsigned_module_loaded.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "060d5ad4-3153-47bb-8382-43e5e29eda92"
  - "Unsigned Module Loaded by ClickOnce Application"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Unsigned Module Loaded by ClickOnce Application

Detects unsigned module load by ClickOnce application.

## Metadata

- Rule ID: 060d5ad4-3153-47bb-8382-43e5e29eda92
- Status: test
- Level: medium
- Author: @SerkinValery
- Date: 2023-06-08
- Source Path: rules/windows/image_load/image_load_susp_clickonce_unsigned_module_loaded.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection_path:
  Image|contains: \AppData\Local\Apps\2.0\
selection_sig_status:
- Signed: 'false'
- SignatureStatus: Expired
condition: all of selection_*
```

## False Positives

- Unlikely

## References

- https://posts.specterops.io/less-smartscreen-more-caffeine-ab-using-clickonce-for-trusted-code-execution-1446ea8051c5

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_susp_clickonce_unsigned_module_loaded.yml)
