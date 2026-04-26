---
sigma_id: "e7be6119-fc37-43f0-ad4f-1f3f99be2f9f"
title: "Copying Sensitive Files with Credential Data"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_esentutl_sensitive_file_copy.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_esentutl_sensitive_file_copy.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "e7be6119-fc37-43f0-ad4f-1f3f99be2f9f"
  - "Copying Sensitive Files with Credential Data"
attack_technique_ids:
  - "T1003.002"
  - "T1003.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Copying Sensitive Files with Credential Data

Files with well-known filenames (sensitive files with credential data) copying

## Metadata

- Rule ID: e7be6119-fc37-43f0-ad4f-1f3f99be2f9f
- Status: test
- Level: high
- Author: Teymur Kheirkhabarov, Daniil Yugoslavskiy, oscd.community
- Date: 2019-10-22
- Modified: 2024-06-04
- Source Path: rules/windows/process_creation/proc_creation_win_esentutl_sensitive_file_copy.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.002]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]

### Software Tags

- S0404

## Detection

```yaml
selection_esent_img:
- Image|endswith: \esentutl.exe
- OriginalFileName: \esentutl.exe
selection_esent_cli:
  CommandLine|contains|windash:
  - vss
  - ' /m '
  - ' /y '
selection_susp_paths:
  CommandLine|contains:
  - \config\RegBack\sam
  - \config\RegBack\security
  - \config\RegBack\system
  - \config\sam
  - \config\security
  - '\config\system '
  - \repair\sam
  - \repair\security
  - \repair\system
  - \windows\ntds\ntds.dit
condition: all of selection_esent_* or selection_susp_paths
```

## False Positives

- Copying sensitive files for legitimate use (eg. backup) or forensic investigation by legitimate incident responder or forensic investigator.

## References

- https://room362.com/post/2013/2013-06-10-volume-shadow-copy-ntdsdit-domain-hashes-remotely-part-1/
- https://www.slideshare.net/heirhabarov/hunting-for-credentials-dumping-in-windows-environment
- https://dfironthemountain.wordpress.com/2018/12/06/locked-file-access-using-esentutl-exe/
- https://github.com/LOLBAS-Project/LOLBAS/blob/2cc01b01132b5c304027a658c698ae09dd6a92bf/yml/OSBinaries/Esentutl.yml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_esentutl_sensitive_file_copy.yml)
