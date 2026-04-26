---
sigma_id: "bae2865c-5565-470d-b505-9496c87d0c30"
title: "SMB Spoolss Name Piped Usage"
framework: "sigma"
generated: "true"
source_path: "rules/network/zeek/zeek_dce_rpc_smb_spoolss_named_pipe.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_dce_rpc_smb_spoolss_named_pipe.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "zeek / smb_files"
aliases:
  - "bae2865c-5565-470d-b505-9496c87d0c30"
  - "SMB Spoolss Name Piped Usage"
attack_technique_ids:
  - "T1021.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# SMB Spoolss Name Piped Usage

Detects the use of the spoolss named pipe over SMB. This can be used to trigger the authentication via NTLM of any machine that has the spoolservice enabled.

## Metadata

- Rule ID: bae2865c-5565-470d-b505-9496c87d0c30
- Status: test
- Level: medium
- Author: OTR (Open Threat Research), @neu5ron
- Date: 2018-11-28
- Modified: 2022-10-09
- Source Path: rules/network/zeek/zeek_dce_rpc_smb_spoolss_named_pipe.yml

## Logsource

- product: zeek
- service: smb_files

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.002]]

## Detection

```yaml
selection:
  path|endswith: IPC$
  name: spoolss
condition: selection
```

## False Positives

- Domain Controllers that are sometimes, commonly although should not be, acting as printer servers too

## References

- https://posts.specterops.io/hunting-in-active-directory-unconstrained-delegation-forests-trusts-71f2b33688e1
- https://dirkjanm.io/a-different-way-of-abusing-zerologon/
- https://twitter.com/_dirkjan/status/1309214379003588608

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_dce_rpc_smb_spoolss_named_pipe.yml)
