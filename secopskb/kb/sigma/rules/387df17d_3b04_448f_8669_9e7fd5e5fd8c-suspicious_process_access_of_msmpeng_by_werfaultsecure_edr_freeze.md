---
sigma_id: "387df17d-3b04-448f-8669-9e7fd5e5fd8c"
title: "Suspicious Process Access of MsMpEng by WerFaultSecure - EDR-Freeze"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_access/proc_access_win_werfaultsecure_msmpeng_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_werfaultsecure_msmpeng_access.yml"
build_date: "2026-04-26 17:03:23"
status: "experimental"
level: "high"
logsource: "windows / process_access"
aliases:
  - "387df17d-3b04-448f-8669-9e7fd5e5fd8c"
  - "Suspicious Process Access of MsMpEng by WerFaultSecure - EDR-Freeze"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious Process Access of MsMpEng by WerFaultSecure - EDR-Freeze

Detects process access events where WerFaultSecure accesses MsMpEng.exe with dbgcore.dll or dbghelp.dll in the call trace, indicating potential EDR freeze techniques.
This technique leverages WerFaultSecure.exe running as a Protected Process Light (PPL) with WinTCB protection level to call MiniDumpWriteDump and suspend EDR/AV processes, allowing malicious activity to execute undetected during the suspension period.

## Metadata

- Rule ID: 387df17d-3b04-448f-8669-9e7fd5e5fd8c
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-11-27
- Source Path: rules/windows/process_access/proc_access_win_werfaultsecure_msmpeng_access.yml

## Logsource

- category: process_access
- definition: Requires Sysmon Event ID 10 (ProcessAccess) with CallTrace enabled.
Example sysmon config snippet with grouping, as logging individual ProcessAccess events can generate excessive logs:
<ProcessAccess onmatch="include">
    <Rule groupRelation="and">
    <TargetImage condition="end with">\MsMpEng.exe</TargetImage>
    <SourceImage condition="end with">\WerFaultSecure.exe</SourceImage>
    </Rule>
</ProcessAccess>

- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  SourceImage|endswith: \WerFaultSecure.exe
  TargetImage|endswith: \MsMpEng.exe
  CallTrace|contains:
  - \dbgcore.dll
  - \dbghelp.dll
condition: selection
```

## False Positives

- Legitimate Windows Error Reporting operations

## References

- https://blog.axelarator.net/hunting-for-edr-freeze/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_werfaultsecure_msmpeng_access.yml)
