---
sigma_id: "6d3a3952-6530-44a3-8554-cf17c116c615"
title: "Potentially Suspicious JWT Token Search Via CLI"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_jwt_token_search.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_jwt_token_search.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "6d3a3952-6530-44a3-8554-cf17c116c615"
  - "Potentially Suspicious JWT Token Search Via CLI"
attack_technique_ids:
  - "T1528"
  - "T1552.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious JWT Token Search Via CLI

Detects potentially suspicious search for JWT tokens via CLI by looking for the string "eyJ0eX" or "eyJhbG".
JWT tokens are often used for access-tokens across various applications and services like Microsoft 365, Azure, AWS, Google Cloud, and others.
Threat actors may search for these tokens to steal them for lateral movement or privilege escalation.

## Metadata

- Rule ID: 6d3a3952-6530-44a3-8554-cf17c116c615
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), kagebunsher
- Date: 2022-10-25
- Modified: 2025-10-21
- Source Path: rules/windows/process_creation/proc_creation_win_susp_jwt_token_search.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1528-steal_application_access_token|T1528]]
- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.001]]

## Detection

```yaml
selection_tools:
  CommandLine|contains:
  - 'find '
  - find.exe
  - findstr
  - 'select-string '
  - strings
selection_jwt_string:
  CommandLine|contains:
  - eyJ0eXAiOi
  - eyJhbGciOi
  - ' eyJ0eX'
  - ' "eyJ0eX"'
  - ' ''eyJ0eX'''
  - ' eyJhbG'
  - ' "eyJhbG"'
  - ' ''eyJhbG'''
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://mrd0x.com/stealing-tokens-from-office-applications/
- https://www.scip.ch/en/?labs.20240523

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_jwt_token_search.yml)
