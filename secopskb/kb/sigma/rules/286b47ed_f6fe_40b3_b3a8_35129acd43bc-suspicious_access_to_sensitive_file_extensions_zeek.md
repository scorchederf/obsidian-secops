---
sigma_id: "286b47ed-f6fe-40b3-b3a8-35129acd43bc"
title: "Suspicious Access to Sensitive File Extensions - Zeek"
framework: "sigma"
generated: "true"
source_path: "rules/network/zeek/zeek_smb_converted_win_susp_raccess_sensitive_fext.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_smb_converted_win_susp_raccess_sensitive_fext.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "zeek / smb_files"
aliases:
  - "286b47ed-f6fe-40b3-b3a8-35129acd43bc"
  - "Suspicious Access to Sensitive File Extensions - Zeek"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Access to Sensitive File Extensions - Zeek

Detects known sensitive file extensions via Zeek

## Metadata

- Rule ID: 286b47ed-f6fe-40b3-b3a8-35129acd43bc
- Status: test
- Level: medium
- Author: Samir Bousseaden, @neu5ron
- Date: 2020-04-02
- Modified: 2025-10-17
- Source Path: rules/network/zeek/zeek_smb_converted_win_susp_raccess_sensitive_fext.yml

## Logsource

- product: zeek
- service: smb_files

## Detection

```yaml
selection:
  name|endswith:
  - .pst
  - .ost
  - .msg
  - .nst
  - .oab
  - .edb
  - .nsf
  - .bak
  - .dmp
  - .kirbi
  - .rdp
condition: selection
```

## False Positives

- Help Desk operator doing backup or re-imaging end user machine or backup software
- Users working with these data types or exchanging message files

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_smb_converted_win_susp_raccess_sensitive_fext.yml)
