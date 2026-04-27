---
car_id: "CAR-2020-08-002"
title: "NTFS Alternate Data Stream Execution - LOLBAS"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2020-08-002/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-08-002.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2020-08-002"
  - "NTFS Alternate Data Stream Execution - LOLBAS"
attack_technique_ids:
  - "T1564"
  - "T1564.004"
platforms:
  - "Windows"
implementation_types:
  - "pseudocode"
  - "splunk"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# CAR-2020-08-002: NTFS Alternate Data Stream Execution - LOLBAS

## Metadata

- CAR ID: CAR-2020-08-002
- Submission Date: 2020/08/03
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: MITRE

## Description

NTFS Alternate Data Streams (ADSs) may be used by adversaries as a means of evading security tools by storing malicious data or binaries in file attribute metadata. ADSs are also powerful because their contents can be directly executed by various Windows tools; accordingly, this analytic looks at common ways of executing ADSs using Living off the Land Binaries and Scripts (LOLBAS).

## ATT&CK Coverage

- [[kb/attack/techniques/T1564-hide_artifacts|T1564]] (coverage: Low; tactics: TA0005)
  - [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

## Implementations

### pseudocode

This is generic pseudocode that lines up with the below Splunk queries.

- Data Model: CAR native

```pseudocode
processes = search Process:Create
ads_processes = filter processes where (
exe == "control.exe OR appvlp.exe OR cmd.exe OR ftp.exe OR bash.exe OR mavinject.exe OR bitsadmin.exe" and command_line.matches("__some_regex__")
)
output ads_processes
```

### splunk

This Splunk query looks for invocations of control.exe used to execute NTFS alternate data streams.

- Data Model: Sysmon native

```splunk
index=__sysmon_index__ EventCode=1 (Image=C:\\Windows\System32\\control.exe OR Image=C:\\Windows\SysWOW64\\control.exe) | regex CommandLine="(\w+(\.\w+)?):(\w+\.dll)"
```

### splunk

This Splunk query looks for invocations of appvlp.exe used to execute NTFS alternate data streams.

- Data Model: Sysmon native

```splunk
index=__sysmon_index__ EventCode=1 (Image="C:\\Program Files\\Microsoft Office\\root\\Client\\AppVLP.exe" OR Image="C:\\Program Files (x86)\\Microsoft Office\\root\\Client\\AppVLP.exe") | regex CommandLine="(\w+(\.\w+)?):(\w+(\.\w+)?)"
```

### splunk

This Splunk query looks for invocations of cmd.exe used to execute NTFS alternate data streams.

- Data Model: Sysmon native

```splunk
index=__sysmon_index__ EventCode=1 (Image=C:\\Windows\\System32\\cmd.exe OR Image=C:\\Windows\\SysWOW64\\cmd.exe) | regex CommandLine="-\s+<.*\b(\w+(\.\w+)?):(\w+(\.\w+)?)"
```

### splunk

This Splunk query looks for invocations of ftp.exe used to execute NTFS alternate data streams.

- Data Model: Sysmon native

```splunk
index=__sysmon_index__ EventCode=1 (Image=C:\\Windows\\System32\\ftp.exe OR Image=C:\\Windows\\SysWOW64\\ftp.exe) | regex CommandLine="-s:(\w+(\.\w+)?):(\w+(\.\w+)?)"
```

### splunk

This Splunk query looks for invocations of bash.exe used to execute NTFS alternate data streams.

- Data Model: Sysmon native

```splunk
index=__sysmon_index__ EventCode=1 (Image=C:\\Windows\\System32\\bash.exe OR C:\\Windows\\SysWOW64\\bash.exe) | regex CommandLine="-c.*(\w+(\.\w+)?):(\w+(\.\w+)?)"
```

### splunk

This Splunk query looks for invocations of mavinject.exe used to execute NTFS alternate data streams.

- Data Model: Sysmon native

```splunk
index=__sysmon_index__ EventCode=1 (Image=C:\\Windows\\System32\\mavinject.exe OR C:\\Windows\\SysWOW64\\mavinject.exe) | regex CommandLine="\d+\s+\/INJECTRUNNING.*\b(\w+(\.\w+)?):(\w+(\.\w+)?)"
```

### splunk

This Splunk query looks for invocations of bitsadmin.exe used to execute NTFS alternate data streams.

- Data Model: Sysmon native

```splunk
index=__sysmon_index__ EventCode=1 (Image=C:\\Windows\\System32\\bitsadmin.exe OR C:\\Windows\\SysWOW64\\bitsadmin.exe) | regex CommandLine="\/create.*\/addfile.*\/SetNotifyCmdLine.*\b(\w+\.\w+):(\w+(\.\w+)?)"
```

## Data Model References

- process/create/exe
- process/create/command_line

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2020-08-002/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-08-002.yaml)
