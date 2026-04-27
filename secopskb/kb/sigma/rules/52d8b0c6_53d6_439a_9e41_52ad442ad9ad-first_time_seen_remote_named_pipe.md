---
sigma_id: "52d8b0c6-53d6-439a-9e41-52ad442ad9ad"
title: "First Time Seen Remote Named Pipe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_lm_namedpipe.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_lm_namedpipe.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "52d8b0c6-53d6-439a-9e41-52ad442ad9ad"
  - "First Time Seen Remote Named Pipe"
attack_technique_ids:
  - "T1021.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This detection excludes known namped pipes accessible remotely and notify on newly observed ones, may help to detect lateral movement and remote exec using named pipes

## Logsource

- definition: The advanced audit policy setting "Object Access > Audit Detailed File Share" must be configured for Success/Failure
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]]

## Detection

```yaml
selection1:
  EventID: 5145
  ShareName: \\\\\*\\IPC$
false_positives:
  RelativeTargetName:
  - atsvc
  - samr
  - lsarpc
  - lsass
  - winreg
  - netlogon
  - srvsvc
  - protected_storage
  - wkssvc
  - browser
  - netdfs
  - svcctl
  - spoolss
  - ntsvcs
  - LSM_API_service
  - HydraLsPipe
  - TermSrv_API_service
  - MsFteWds
  - sql\query
  - eventlog
condition: selection1 and not false_positives
```

## False Positives

- Update the excluded named pipe to filter out any newly observed legit named pipe

## References

- https://twitter.com/menasec1/status/1104489274387451904

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_lm_namedpipe.yml)
