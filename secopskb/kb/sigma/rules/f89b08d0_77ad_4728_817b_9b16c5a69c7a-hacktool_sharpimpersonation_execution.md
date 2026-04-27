---
sigma_id: "f89b08d0-77ad-4728-817b-9b16c5a69c7a"
title: "HackTool - SharpImpersonation Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_sharp_impersonation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sharp_impersonation.yml"
build_date: "2026-04-27 19:13:51"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects execution of the SharpImpersonation tool. Which can be used to manipulate tokens on a Windows computers remotely (PsExec/WmiExec) or interactively

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1134-access_token_manipulation#^t1134001-token-impersonation-theft|T1134.001: Token Impersonation/Theft]]
- [[kb/attack/techniques/T1134-access_token_manipulation#^t1134003-make-and-impersonate-token|T1134.003: Make and Impersonate Token]]

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
