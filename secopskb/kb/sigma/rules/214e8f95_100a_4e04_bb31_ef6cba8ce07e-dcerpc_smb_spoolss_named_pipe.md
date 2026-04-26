---
sigma_id: "214e8f95-100a-4e04-bb31-ef6cba8ce07e"
title: "DCERPC SMB Spoolss Named Pipe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_dce_rpc_smb_spoolss_named_pipe.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_dce_rpc_smb_spoolss_named_pipe.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "214e8f95-100a-4e04-bb31-ef6cba8ce07e"
  - "DCERPC SMB Spoolss Named Pipe"
attack_technique_ids:
  - "T1021.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DCERPC SMB Spoolss Named Pipe

Detects the use of the spoolss named pipe over SMB. This can be used to trigger the authentication via NTLM of any machine that has the spoolservice enabled.

## Metadata

- Rule ID: 214e8f95-100a-4e04-bb31-ef6cba8ce07e
- Status: test
- Level: medium
- Author: OTR (Open Threat Research)
- Date: 2018-11-28
- Modified: 2022-08-11
- Source Path: rules/windows/builtin/security/win_security_dce_rpc_smb_spoolss_named_pipe.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.002]]

## Detection

```yaml
selection:
  EventID: 5145
  ShareName: \\\\\*\\IPC$
  RelativeTargetName: spoolss
condition: selection
```

## False Positives

- Domain Controllers acting as printer servers too? :)

## References

- https://posts.specterops.io/hunting-in-active-directory-unconstrained-delegation-forests-trusts-71f2b33688e1
- https://dirkjanm.io/a-different-way-of-abusing-zerologon/
- https://twitter.com/_dirkjan/status/1309214379003588608

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_dce_rpc_smb_spoolss_named_pipe.yml)
