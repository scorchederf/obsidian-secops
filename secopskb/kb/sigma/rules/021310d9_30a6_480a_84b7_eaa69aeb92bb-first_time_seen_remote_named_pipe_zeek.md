---
sigma_id: "021310d9-30a6-480a-84b7-eaa69aeb92bb"
title: "First Time Seen Remote Named Pipe - Zeek"
framework: "sigma"
generated: "true"
source_path: "rules/network/zeek/zeek_smb_converted_win_lm_namedpipe.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_smb_converted_win_lm_namedpipe.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "zeek / smb_files"
aliases:
  - "021310d9-30a6-480a-84b7-eaa69aeb92bb"
  - "First Time Seen Remote Named Pipe - Zeek"
attack_technique_ids:
  - "T1021.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# First Time Seen Remote Named Pipe - Zeek

This detection excludes known namped pipes accessible remotely and notify on newly observed ones, may help to detect lateral movement and remote exec using named pipes

## Metadata

- Rule ID: 021310d9-30a6-480a-84b7-eaa69aeb92bb
- Status: test
- Level: high
- Author: Samir Bousseaden, @neu5ron, Tim Shelton
- Date: 2020-04-02
- Modified: 2022-12-27
- Source Path: rules/network/zeek/zeek_smb_converted_win_lm_namedpipe.yml

## Logsource

- product: zeek
- service: smb_files

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.002]]

## Detection

```yaml
selection:
  path: \\\\\*\\IPC$
filter_keywords:
- samr
- lsarpc
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
condition: selection and not 1 of filter_*
```

## False Positives

- Update the excluded named pipe to filter out any newly observed legit named pipe

## References

- https://twitter.com/menasec1/status/1104489274387451904

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_smb_converted_win_lm_namedpipe.yml)
