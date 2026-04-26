---
sigma_id: "ccb5742c-c248-4982-8c5c-5571b9275ad3"
title: "Recon Command Output Piped To Findstr.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_findstr_recon_pipe_output.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_findstr_recon_pipe_output.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "ccb5742c-c248-4982-8c5c-5571b9275ad3"
  - "Recon Command Output Piped To Findstr.EXE"
attack_technique_ids:
  - "T1057"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Recon Command Output Piped To Findstr.EXE

Detects the execution of a potential recon command where the results are piped to "findstr". This is meant to trigger on inline calls of "cmd.exe" via the "/c" or "/k" for example.
Attackers often time use this technique to extract specific information they require in their reconnaissance phase.

## Metadata

- Rule ID: ccb5742c-c248-4982-8c5c-5571b9275ad3
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), frack113
- Date: 2023-07-06
- Modified: 2025-10-08
- Source Path: rules/windows/process_creation/proc_creation_win_findstr_recon_pipe_output.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1057-process_discovery|T1057]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - ipconfig*|*find
  - net*|*find
  - netstat*|*find
  - ping*|*find
  - systeminfo*|*find
  - tasklist*|*find
  - whoami*|*find
filter_optional_xampp:
  CommandLine|contains|all:
  - cmd.exe /c TASKLIST /V |
  - FIND /I
  - \xampp\
  - \catalina_start.bat
condition: selection and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/02cb591f75064ffe1e0df9ac3ed5972a2e491c97/atomics/T1057/T1057.md#atomic-test-6---discover-specific-process---tasklist
- https://www.hhs.gov/sites/default/files/manage-engine-vulnerability-sector-alert-tlpclear.pdf
- https://www.trendmicro.com/en_us/research/22/d/spring4shell-exploited-to-deploy-cryptocurrency-miners.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_findstr_recon_pipe_output.yml)
