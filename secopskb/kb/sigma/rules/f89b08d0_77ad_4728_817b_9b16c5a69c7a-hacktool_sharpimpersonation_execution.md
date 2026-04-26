---
sigma_id: "f89b08d0-77ad-4728-817b-9b16c5a69c7a"
title: "HackTool - SharpImpersonation Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_sharp_impersonation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sharp_impersonation.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f89b08d0-77ad-4728-817b-9b16c5a69c7a"
  - "HackTool - SharpImpersonation Execution"
attack_technique_ids:
  - "T1134.001"
  - "T1134.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - SharpImpersonation Execution

Detects execution of the SharpImpersonation tool. Which can be used to manipulate tokens on a Windows computers remotely (PsExec/WmiExec) or interactively

## Metadata

- Rule ID: f89b08d0-77ad-4728-817b-9b16c5a69c7a
- Status: test
- Level: high
- Author: Sai Prashanth Pulisetti @pulisettis, Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-12-27
- Modified: 2023-02-13
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_sharp_impersonation.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1134-access_token_manipulation|T1134.001]]
- [[kb/attack/techniques/T1134-access_token_manipulation|T1134.003]]

## Detection

```yaml
selection_img:
- Image|endswith: \SharpImpersonation.exe
- OriginalFileName: SharpImpersonation.exe
selection_cli:
- CommandLine|contains|all:
  - ' user:'
  - ' binary:'
- CommandLine|contains|all:
  - ' user:'
  - ' shellcode:'
- CommandLine|contains:
  - ' technique:CreateProcessAsUserW'
  - ' technique:ImpersonateLoggedOnuser'
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://s3cur3th1ssh1t.github.io/SharpImpersonation-Introduction/
- https://github.com/S3cur3Th1sSh1t/SharpImpersonation

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sharp_impersonation.yml)
