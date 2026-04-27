---
sigma_id: "92dae1ed-1c9d-4eff-a567-33acbd95b00e"
title: "Possible Impacket SecretDump Remote Activity - Zeek"
framework: "sigma"
generated: "true"
source_path: "rules/network/zeek/zeek_smb_converted_win_impacket_secretdump.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_smb_converted_win_impacket_secretdump.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "zeek / smb_files"
aliases:
  - "92dae1ed-1c9d-4eff-a567-33acbd95b00e"
  - "Possible Impacket SecretDump Remote Activity - Zeek"
attack_technique_ids:
  - "T1003.002"
  - "T1003.004"
  - "T1003.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Possible Impacket SecretDump Remote Activity - Zeek

Detect AD credential dumping using impacket secretdump HKTL. Based on the SIGMA rules/windows/builtin/win_impacket_secretdump.yml

## Metadata

- Rule ID: 92dae1ed-1c9d-4eff-a567-33acbd95b00e
- Status: test
- Level: high
- Author: Samir Bousseaden, @neu5ron
- Date: 2020-03-19
- Modified: 2021-11-27
- Source Path: rules/network/zeek/zeek_smb_converted_win_impacket_secretdump.yml

## Logsource

- product: zeek
- service: smb_files

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.002]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.004]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]

## Detection

```yaml
selection:
  path|contains|all:
  - \
  - ADMIN$
  name|contains: SYSTEM32\
  name|endswith: .tmp
condition: selection
```

## False Positives

- Unknown

## References

- https://web.archive.org/web/20230329153811/https://blog.menasec.net/2019/02/threat-huting-10-impacketsecretdump.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_smb_converted_win_impacket_secretdump.yml)
