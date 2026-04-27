---
sigma_id: "2f77047c-e6e9-4c11-b088-a3de399524cd"
title: "Potential Persistence Via Security Descriptors - ScriptBlock"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_ace_tampering.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_ace_tampering.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "2f77047c-e6e9-4c11-b088-a3de399524cd"
  - "Potential Persistence Via Security Descriptors - ScriptBlock"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects usage of certain functions and keywords that are used to manipulate security descriptors in order to potentially set a backdoor. As seen used in the DAMP project.

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - win32_Trustee
  - win32_Ace
  - .AccessMask
  - .AceType
  - .SetSecurityDescriptor
  ScriptBlockText|contains:
  - \Lsa\JD
  - \Lsa\Skew1
  - \Lsa\Data
  - \Lsa\GBG
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/HarmJ0y/DAMP

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_ace_tampering.yml)
