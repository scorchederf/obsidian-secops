---
sigma_id: "06d71506-7beb-4f22-8888-e2e5e2ca7fd8"
title: "Mimikatz Use"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/win_alert_mimikatz_keywords.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/win_alert_mimikatz_keywords.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "windows"
aliases:
  - "06d71506-7beb-4f22-8888-e2e5e2ca7fd8"
  - "Mimikatz Use"
attack_technique_ids:
  - "T1003.002"
  - "T1003.004"
  - "T1003.001"
  - "T1003.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This method detects mimikatz keywords in different Eventlogs (some of them only appear in older Mimikatz version that are however still used by different threat groups)

## Logsource

- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003002-security-account-manager|T1003.002: Security Account Manager]]
- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003004-lsa-secrets|T1003.004: LSA Secrets]]
- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]
- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003006-dcsync|T1003.006: DCSync]]

### Software Tags

- S0002

## Detection

```yaml
keywords:
- dpapi::masterkey
- eo.oe.kiwi
- event::clear
- event::drop
- gentilkiwi.com
- kerberos::golden
- kerberos::ptc
- kerberos::ptt
- kerberos::tgt
- Kiwi Legit Printer
- 'lsadump::'
- mimidrv.sys
- \mimilib.dll
- misc::printnightmare
- misc::shadowcopies
- misc::skeleton
- privilege::backup
- privilege::debug
- privilege::driver
- 'sekurlsa::'
filter:
  EventID: 15
condition: keywords and not filter
```

## False Positives

- Naughty administrators
- AV Signature updates
- Files with Mimikatz in their filename

## References

- https://tools.thehacker.recipes/mimikatz/modules

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/win_alert_mimikatz_keywords.yml)
