---
sigma_id: "b210394c-ba12-4f89-9117-44a2464b9511"
title: "SMB Create Remote File Admin Share"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_smb_file_creation_admin_shares.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_smb_file_creation_admin_shares.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "b210394c-ba12-4f89-9117-44a2464b9511"
  - "SMB Create Remote File Admin Share"
attack_technique_ids:
  - "T1021.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# SMB Create Remote File Admin Share

Look for non-system accounts SMB accessing a file with write (0x2) access mask via administrative share (i.e C$).

## Metadata

- Rule ID: b210394c-ba12-4f89-9117-44a2464b9511
- Status: test
- Level: high
- Author: Jose Rodriguez (@Cyb3rPandaH), OTR (Open Threat Research)
- Date: 2020-08-06
- Modified: 2025-10-17
- Source Path: rules/windows/builtin/security/win_security_smb_file_creation_admin_shares.yml

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
  ShareName|endswith: C$
  AccessMask: '0x2'
filter_main_subjectusername:
  SubjectUserName|endswith: $
filter_optional_local_ip:
  IpAddress: ::1
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://github.com/OTRF/ThreatHunter-Playbook/blob/f7a58156dbfc9b019f17f638b8c62d22e557d350/playbooks/WIN-201012004336.yaml
- https://securitydatasets.com/notebooks/atomic/windows/lateral_movement/SDWIN-200806015757.html?highlight=create%20file

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_smb_file_creation_admin_shares.yml)
