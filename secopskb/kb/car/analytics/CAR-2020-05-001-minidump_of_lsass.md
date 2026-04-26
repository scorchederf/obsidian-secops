---
car_id: "CAR-2020-05-001"
title: "MiniDump of LSASS"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2020-05-001/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-05-001.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2020-05-001"
  - "MiniDump of LSASS"
attack_technique_ids:
  - "T1003"
  - "T1003.003"
platforms:
  - "Windows"
implementation_types:
  - "Splunk"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CAR-2020-05-001: MiniDump of LSASS

## Metadata

- CAR ID: CAR-2020-05-001
- Submission Date: 2020/05/04
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: Cyber National Mission Force (CNMF)

## Description

This analytic detects the minidump variant of credential dumping where a process opens lsass.exe in order to extract credentials using the Win32 API call [MiniDumpWriteDump](https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/nf-minidumpapiset-minidumpwritedump). Tools like [SafetyKatz](https://github.com/GhostPack/SafetyKatz), [SafetyDump](https://github.com/m0rv4i/SafetyDump), and [Outflank-Dumpert](https://github.com/outflanknl/Dumpert) default to this variant and may be detected by this analytic, though keep in mind that not all options for using those tools will result in this specific behavior.

The analytic is based on a [Sigma analytic](https://github.com/NVISO-BE/sigma-public/blob/master/rules/windows/sysmon/sysmon_lsass_memdump.yml) contributed by Samir Bousseaden and written up in a [blog on MENASEC](https://blog.menasec.net/2019/02/threat-hunting-21-procdump-or-taskmgr.html). It looks for a call trace that includes either dbghelp.dll or dbgcore.dll, which export the relevant functions/permissions to perform the dump. It also detects using the Windows Task Manager (taskmgr.exe) to dump lsass, which is described in [CAR-2019-08-001](/analytics/CAR-2019-08-001/). In this iteration of the Sigma analytic, the `GrantedAccess` filter isn't included because it didn't seem to filter out any false positives and introduces the potential for evasion.

This analytic was tested both in a lab and in a production environment with a very low false-positive rate. werfault.exe and tasklist.exe, both standard Windows processes, showed up multiple times as false positives.

NOTE - this analytic has no corresponding pseudocode implementation because the CAR data model doesn't currently support process access events.

## ATT&CK Coverage

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]] (coverage: Low; tactics: TA0006)
  - [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]

## Implementations

### Splunk

This Splunk query looks for process access events where lsass.exe is accessed with a specific call trace that indicates the use of MiniDumpWriteDump.

- Data Model: Sysmon native

```splunk
index=__your_sysmon_index__ EventCode=10 TargetImage="C:\\windows\\system32\\lsass.exe" (CallTrace="*dbghelp.dll*" OR CallTrace="*dbgcore.dll*")| table _time host SourceProcessId SourceImage
```

### LogPoint

LogPoint version of the above pseudocodes.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=10 image="C:\Windows\system32\lsass.exe" call_trace IN ["*dbghelp.dll*", "*dbgcore.dll*"]
| fields log_ts host source_process_id source_image
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-SCA-system_call_analysis|D3-SCA: System Call Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2020-05-001/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-05-001.yaml)
