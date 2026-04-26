---
sigma_id: "d679950c-abb7-43a6-80fb-2a480c4fc450"
title: "PDQ Deploy Remote Adminstartion Tool Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pdqdeploy_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pdqdeploy_execution.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "d679950c-abb7-43a6-80fb-2a480c4fc450"
  - "PDQ Deploy Remote Adminstartion Tool Execution"
attack_technique_ids:
  - "T1072"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PDQ Deploy Remote Adminstartion Tool Execution

Detect use of PDQ Deploy remote admin tool

## Metadata

- Rule ID: d679950c-abb7-43a6-80fb-2a480c4fc450
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-10-01
- Modified: 2023-01-30
- Source Path: rules/windows/process_creation/proc_creation_win_pdqdeploy_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1072-software_deployment_tools|T1072]]

## Detection

```yaml
selection:
- Description: PDQ Deploy Console
- Product: PDQ Deploy
- Company: PDQ.com
- OriginalFileName: PDQDeployConsole.exe
condition: selection
```

## False Positives

- Legitimate use

## References

- https://github.com/redcanaryco/atomic-red-team/blob/9e5b12c4912c07562aec7500447b11fa3e17e254/atomics/T1072/T1072.md
- https://www.pdq.com/pdq-deploy/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pdqdeploy_execution.yml)
