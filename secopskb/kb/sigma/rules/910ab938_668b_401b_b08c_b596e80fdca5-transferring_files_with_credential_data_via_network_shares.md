---
sigma_id: "910ab938-668b-401b-b08c-b596e80fdca5"
title: "Transferring Files with Credential Data via Network Shares"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_transf_files_with_cred_data_via_network_shares.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_transf_files_with_cred_data_via_network_shares.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "910ab938-668b-401b-b08c-b596e80fdca5"
  - "Transferring Files with Credential Data via Network Shares"
attack_technique_ids:
  - "T1003.002"
  - "T1003.001"
  - "T1003.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Transferring Files with Credential Data via Network Shares

Transferring files with well-known filenames (sensitive files with credential data) using network shares

## Metadata

- Rule ID: 910ab938-668b-401b-b08c-b596e80fdca5
- Status: test
- Level: medium
- Author: Teymur Kheirkhabarov, oscd.community
- Date: 2019-10-22
- Modified: 2025-07-11
- Source Path: rules/windows/builtin/security/win_security_transf_files_with_cred_data_via_network_shares.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.002]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]

## Detection

```yaml
selection_eid:
  EventID: 5145
selection_object:
- RelativeTargetName|contains:
  - \mimidrv
  - \lsass
  - \windows\minidump\
  - \hiberfil
  - \sqldmpr
- RelativeTargetName:
  - Windows\NTDS\ntds.dit
  - Windows\System32\config\SAM
  - Windows\System32\config\SECURITY
  - Windows\System32\config\SYSTEM
condition: all of selection_*
```

## False Positives

- Transferring sensitive files for legitimate administration work by legitimate administrator

## References

- https://www.slideshare.net/heirhabarov/hunting-for-credentials-dumping-in-windows-environment

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_transf_files_with_cred_data_via_network_shares.yml)
