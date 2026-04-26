---
sigma_id: "bac9fb54-2da7-44e9-988f-11e9a5edbc0c"
title: "Potential Password Spraying Attempt Using Dsacls.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_dsacls_password_spray.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dsacls_password_spray.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "bac9fb54-2da7-44e9-988f-11e9a5edbc0c"
  - "Potential Password Spraying Attempt Using Dsacls.EXE"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Password Spraying Attempt Using Dsacls.EXE

Detects possible password spraying attempts using Dsacls

## Metadata

- Rule ID: bac9fb54-2da7-44e9-988f-11e9a5edbc0c
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-20
- Modified: 2023-02-04
- Source Path: rules/windows/process_creation/proc_creation_win_dsacls_password_spray.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith: \dsacls.exe
- OriginalFileName: DSACLS.EXE
selection_cli:
  CommandLine|contains|all:
  - '/user:'
  - '/passwd:'
condition: all of selection*
```

## False Positives

- Legitimate use of dsacls to bind to an LDAP session

## References

- https://www.ired.team/offensive-security-experiments/active-directory-kerberos-abuse/using-dsacls-to-check-ad-object-permissions#password-spraying-anyone
- https://ss64.com/nt/dsacls.html
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc771151(v=ws.11)

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dsacls_password_spray.yml)
