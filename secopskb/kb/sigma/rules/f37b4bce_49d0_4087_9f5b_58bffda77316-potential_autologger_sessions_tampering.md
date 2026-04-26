---
sigma_id: "f37b4bce-49d0-4087-9f5b-58bffda77316"
title: "Potential AutoLogger Sessions Tampering"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_disable_autologger_sessions.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disable_autologger_sessions.yml"
build_date: "2026-04-26 15:01:48"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "f37b4bce-49d0-4087-9f5b-58bffda77316"
  - "Potential AutoLogger Sessions Tampering"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential AutoLogger Sessions Tampering

Detects tampering with autologger trace sessions which is a technique used by attackers to disable logging

## Metadata

- Rule ID: f37b4bce-49d0-4087-9f5b-58bffda77316
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-01
- Modified: 2025-10-07
- Source Path: rules/windows/registry/registry_set/registry_set_disable_autologger_sessions.yml

## Logsource

- category: registry_set
- product: windows

## Detection

```yaml
selection_main:
  TargetObject|contains: \System\CurrentControlSet\Control\WMI\Autologger\
selection_values:
  TargetObject|contains:
  - \EventLog-
  - \Defender
  TargetObject|endswith:
  - \Enable
  - \Start
  Details: DWORD (0x00000000)
filter_main_wevtutil:
  Image: C:\Windows\system32\wevtutil.exe
filter_main_defender:
  Image|startswith:
  - C:\ProgramData\Microsoft\Windows Defender\Platform\
  - C:\Program Files\Windows Defender\
  - C:\Program Files (x86)\Windows Defender\
  Image|endswith: \MsMpEng.exe
  TargetObject|contains:
  - \DefenderApiLogger\
  - \DefenderAuditLogger\
condition: all of selection_* and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://twitter.com/MichalKoczwara/status/1553634816016498688
- https://thedfirreport.com/2021/10/18/icedid-to-xinglocker-ransomware-in-24-hours/
- https://i.blackhat.com/EU-21/Wednesday/EU-21-Teodorescu-Veni-No-Vidi-No-Vici-Attacks-On-ETW-Blind-EDRs.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disable_autologger_sessions.yml)
