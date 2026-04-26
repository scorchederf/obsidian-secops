---
sigma_id: "fe2f9663-41cb-47e2-b954-8a228f3b9dff"
title: "Linux Base64 Encoded Shebang In CLI"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_base64_shebang_cli.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_base64_shebang_cli.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "fe2f9663-41cb-47e2-b954-8a228f3b9dff"
  - "Linux Base64 Encoded Shebang In CLI"
attack_technique_ids:
  - "T1140"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Linux Base64 Encoded Shebang In CLI

Detects the presence of a base64 version of the shebang in the commandline, which could indicate a malicious payload about to be decoded

## Metadata

- Rule ID: fe2f9663-41cb-47e2-b954-8a228f3b9dff
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-09-15
- Source Path: rules/linux/process_creation/proc_creation_lnx_base64_shebang_cli.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1140-deobfuscate_decode_files_or_information|T1140]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - IyEvYmluL2Jhc2
  - IyEvYmluL2Rhc2
  - IyEvYmluL3pza
  - IyEvYmluL2Zpc2
  - IyEvYmluL3No
condition: selection
```

## False Positives

- Legitimate administration activities

## References

- https://www.trendmicro.com/pl_pl/research/20/i/the-evolution-of-malicious-shell-scripts.html
- https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_base64_shebang_cli.yml)
