---
car_id: "CAR-2013-05-009"
title: "Running executables with same hash and different names"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2013-05-009/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-05-009.yaml"
build_date: "2026-04-27 19:03:49"
aliases:
  - "CAR-2013-05-009"
  - "Running executables with same hash and different names"
attack_technique_ids:
  - "T1036"
  - "T1036.003"
platforms:
  - "Windows"
  - "Linux"
  - "macOS"
implementation_types:
  - "splunk"
  - "Sigma"
  - "DNIF"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Executables are generally not renamed, thus a given hash of an executable should only have ever one name. Identifying instances where multiple process names share the same hash may find cases where tools are copied by attackers to different folders or hosts to [avoid detection](https://attack.mitre.org/tactics/TA0005).

Although this analytic was initially based on MD5 hashes, it is equally applicable to any hashing convention.

### Output Description

A list of hashes and the different executables associated with each one

## ATT&CK Coverage

- [[kb/attack/techniques/T1036-masquerading|T1036: Masquerading]] (coverage: Moderate; tactics: TA0005)
  - [[kb/attack/techniques/T1036-masquerading#^t1036003-rename-legitimate-utilities|T1036.003: Rename Legitimate Utilities]]

## Implementations

### splunk

This is a basic Splunk search that will output all of the sysmon-reported process images and their respective hashes, for cases where an image has more than one set of hashes. Thus, this will output a large amount of data and should be filtered by the analyst in order to make the results more useful.

- Data Model: Sysmon native

```splunk
index=__your_sysmon_index__ EventCode=1|stats dc(Hashes) as Num_Hashes values(Hashes) as "Hashes" by Image|where Num_Hashes > 1
```

### Sigma

[Sigma includes](https://github.com/Neo23x0/sigma/blob/master/rules/windows/process_creation/win_renamed_binary.yml) a Sysmon-specific rule for detecting this, using the OriginalFilename field.

### Sigma

[Sigma includes](https://github.com/Neo23x0/sigma/blob/master/rules/windows/process_creation/win_powershell_renamed_ps.yml) a rule specifically for detecting instances of Powershell being renamed.

### Sigma

[Sigma includes](https://github.com/Neo23x0/sigma/blob/master/rules/windows/process_creation/win_renamed_paexec.yml) a rule specifically for detecting instances of paexec being renamed.

### DNIF

DNIF version of the above pseudocode.

- Data Model: Sysmon native

```dnif
_fetch * from event where $LogName=WINDOWS-SYSMON AND $EventID=1 group count_unique $App, $HashMD5 limit 100
>>_agg count_unique $HashMD5
>>_checkif int_compare count_unique > 1 include
```

### LogPoint

LogPoint version of the above pseudocode.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=1
| chart distinct_count(hash) as cnt by image
| search cnt > 1
```

## Data Model References

- process/create/exe
- process/create/md5_hash

## D3FEND Mappings

- [[kb/defend/techniques/D3-SBV-service_binary_verification|D3-SBV: Service Binary Verification]]
- [[kb/defend/techniques/D3-SFA-system_file_analysis|D3-SFA: System File Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2013-05-009/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-05-009.yaml)
