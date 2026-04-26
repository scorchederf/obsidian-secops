---
sigma_id: "6c6d9280-e6d0-4b9d-80ac-254701b64916"
title: "Potential NTLM Coercion Via Certutil.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_certutil_ntlm_coercion.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_certutil_ntlm_coercion.yml"
build_date: "2026-04-26 15:01:48"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "6c6d9280-e6d0-4b9d-80ac-254701b64916"
  - "Potential NTLM Coercion Via Certutil.EXE"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential NTLM Coercion Via Certutil.EXE

Detects possible NTLM coercion via certutil using the 'syncwithWU' flag

## Metadata

- Rule ID: 6c6d9280-e6d0-4b9d-80ac-254701b64916
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-09-01
- Modified: 2023-02-14
- Source Path: rules/windows/process_creation/proc_creation_win_certutil_ntlm_coercion.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith: \certutil.exe
- OriginalFileName: CertUtil.exe
selection_cli:
  CommandLine|contains|all:
  - ' -syncwithWU '
  - ' \\\\'
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/LOLBAS-Project/LOLBAS/issues/243

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_certutil_ntlm_coercion.yml)
