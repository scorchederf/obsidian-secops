---
sigma_id: "9db37458-4df2-46a5-95ab-307e7f29e675"
title: "Exchange Set OabVirtualDirectory ExternalUrl Property"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/msexchange/win_exchange_set_oabvirtualdirectory_externalurl.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/msexchange/win_exchange_set_oabvirtualdirectory_externalurl.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / msexchange-management"
aliases:
  - "9db37458-4df2-46a5-95ab-307e7f29e675"
  - "Exchange Set OabVirtualDirectory ExternalUrl Property"
attack_technique_ids:
  - "T1505.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Exchange Set OabVirtualDirectory ExternalUrl Property

Rule to detect an adversary setting OabVirtualDirectory External URL property to a script in Exchange Management log

## Metadata

- Rule ID: 9db37458-4df2-46a5-95ab-307e7f29e675
- Status: test
- Level: high
- Author: Jose Rodriguez @Cyb3rPandaH
- Date: 2021-03-15
- Modified: 2023-01-23
- Source Path: rules/windows/builtin/msexchange/win_exchange_set_oabvirtualdirectory_externalurl.yml

## Logsource

- product: windows
- service: msexchange-management

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1505-server_software_component|T1505.003]]

## Detection

```yaml
keywords:
  '|all':
  - Set-OabVirtualDirectory
  - ExternalUrl
  - Page_Load
  - script
condition: keywords
```

## False Positives

- Unknown

## References

- https://twitter.com/OTR_Community/status/1371053369071132675

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/msexchange/win_exchange_set_oabvirtualdirectory_externalurl.yml)
