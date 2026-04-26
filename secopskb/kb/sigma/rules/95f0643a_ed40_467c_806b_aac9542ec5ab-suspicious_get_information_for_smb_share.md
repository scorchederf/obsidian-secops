---
sigma_id: "95f0643a-ed40-467c-806b-aac9542ec5ab"
title: "Suspicious Get Information for SMB Share"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_smb_share_reco.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_smb_share_reco.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "low"
logsource: "windows / ps_script"
aliases:
  - "95f0643a-ed40-467c-806b-aac9542ec5ab"
  - "Suspicious Get Information for SMB Share"
attack_technique_ids:
  - "T1069.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Get Information for SMB Share

Adversaries may look for folders and drives shared on remote systems as a means of identifying sources of information to gather as
a precursor for Collection and to identify potential systems of interest for Lateral Movement.
Networks often contain shared network drives and folders that enable users to access file directories on various systems across a network.

## Metadata

- Rule ID: 95f0643a-ed40-467c-806b-aac9542ec5ab
- Status: test
- Level: low
- Author: frack113
- Date: 2021-12-15
- Modified: 2022-12-25
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_smb_share_reco.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.001]]

## Detection

```yaml
selection:
  ScriptBlockText|contains: get-smbshare
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1069.002/T1069.002.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_smb_share_reco.yml)
