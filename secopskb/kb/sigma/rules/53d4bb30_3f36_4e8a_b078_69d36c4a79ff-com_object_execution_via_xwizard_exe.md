---
sigma_id: "53d4bb30-3f36-4e8a-b078-69d36c4a79ff"
title: "COM Object Execution via Xwizard.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_xwizard_runwizard_com_object_exec.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_xwizard_runwizard_com_object_exec.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "53d4bb30-3f36-4e8a-b078-69d36c4a79ff"
  - "COM Object Execution via Xwizard.EXE"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# COM Object Execution via Xwizard.EXE

Detects the execution of Xwizard tool with the "RunWizard" flag and a GUID like argument.
This utility can be abused in order to run custom COM object created in the registry.

## Metadata

- Rule ID: 53d4bb30-3f36-4e8a-b078-69d36c4a79ff
- Status: test
- Level: medium
- Author: Ensar Şamil, @sblmsrsn, @oscd_initiative, Nasreddine Bencherchali (Nextron Systems)
- Date: 2020-10-07
- Modified: 2024-08-15
- Source Path: rules/windows/process_creation/proc_creation_win_xwizard_runwizard_com_object_exec.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  CommandLine: RunWizard
  CommandLine|re: \{[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\}
condition: selection
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Xwizard/
- https://www.elastic.co/guide/en/security/current/execution-of-com-object-via-xwizard.html
- https://www.hexacorn.com/blog/2017/07/31/the-wizard-of-x-oppa-plugx-style/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_xwizard_runwizard_com_object_exec.yml)
