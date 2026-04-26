---
sigma_id: "bb76d96b-821c-47cf-944b-7ce377864492"
title: "Suspicious NTLM Authentication on the Printer Spooler Service"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_ntlmrelay.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_ntlmrelay.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "bb76d96b-821c-47cf-944b-7ce377864492"
  - "Suspicious NTLM Authentication on the Printer Spooler Service"
attack_technique_ids:
  - "T1212"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious NTLM Authentication on the Printer Spooler Service

Detects a privilege elevation attempt by coercing NTLM authentication on the Printer Spooler service

## Metadata

- Rule ID: bb76d96b-821c-47cf-944b-7ce377864492
- Status: test
- Level: high
- Author: Elastic (idea), Tobias Michalski (Nextron Systems)
- Date: 2022-05-04
- Modified: 2023-02-09
- Source Path: rules/windows/process_creation/proc_creation_win_rundll32_ntlmrelay.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1212-exploitation_for_credential_access|T1212]]

## Detection

```yaml
selection_img:
- Image|endswith: \rundll32.exe
- OriginalFileName: RUNDLL32.EXE
selection_cli:
  CommandLine|contains|all:
  - C:\windows\system32\davclnt.dll,DavSetCookie
  - http
  CommandLine|contains:
  - spoolss
  - srvsvc
  - /print/pipe/
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://twitter.com/med0x2e/status/1520402518685200384
- https://github.com/elastic/detection-rules/blob/dd224fb3f81d0b4bf8593c5f02a029d647ba2b2d/rules/windows/credential_access_relay_ntlm_auth_via_http_spoolss.toml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_ntlmrelay.yml)
