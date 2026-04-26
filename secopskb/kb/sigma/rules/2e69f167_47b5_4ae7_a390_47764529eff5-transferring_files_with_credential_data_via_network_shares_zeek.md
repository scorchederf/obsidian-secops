---
sigma_id: "2e69f167-47b5-4ae7-a390-47764529eff5"
title: "Transferring Files with Credential Data via Network Shares - Zeek"
framework: "sigma"
generated: "true"
source_path: "rules/network/zeek/zeek_smb_converted_win_transferring_files_with_credential_data.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_smb_converted_win_transferring_files_with_credential_data.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "zeek / smb_files"
aliases:
  - "2e69f167-47b5-4ae7-a390-47764529eff5"
  - "Transferring Files with Credential Data via Network Shares - Zeek"
attack_technique_ids:
  - "T1003.002"
  - "T1003.001"
  - "T1003.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Transferring Files with Credential Data via Network Shares - Zeek

Transferring files with well-known filenames (sensitive files with credential data) using network shares

## Metadata

- Rule ID: 2e69f167-47b5-4ae7-a390-47764529eff5
- Status: test
- Level: medium
- Author: @neu5ron, Teymur Kheirkhabarov, oscd.community
- Date: 2020-04-02
- Modified: 2021-11-27
- Source Path: rules/network/zeek/zeek_smb_converted_win_transferring_files_with_credential_data.yml

## Logsource

- product: zeek
- service: smb_files

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.002]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]

## Detection

```yaml
selection:
  name:
  - \mimidrv
  - \lsass
  - \windows\minidump\
  - \hiberfil
  - \sqldmpr
  - \sam
  - \ntds.dit
  - \security
condition: selection
```

## False Positives

- Transferring sensitive files for legitimate administration work by legitimate administrator

## References

- https://www.slideshare.net/heirhabarov/hunting-for-credentials-dumping-in-windows-environment

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_smb_converted_win_transferring_files_with_credential_data.yml)
