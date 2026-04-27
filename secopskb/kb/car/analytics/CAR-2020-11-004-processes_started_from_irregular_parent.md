---
car_id: "CAR-2020-11-004"
title: "Processes Started From Irregular Parent"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2020-11-004/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-11-004.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2020-11-004"
  - "Processes Started From Irregular Parent"
attack_technique_ids:
  - "T1055"
  - "T1055.012"
platforms:
  - "Windows"
implementation_types:
  - "Pseudocode"
  - "Splunk"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# CAR-2020-11-004: Processes Started From Irregular Parent

## Metadata

- CAR ID: CAR-2020-11-004
- Submission Date: 2020/11/30
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: Olaf Hartong

## Description

Adversaries may start legitimate processes and then use their memory space to run malicious code. This analytic looks for common Windows processes that have been abused this way in the past; when the processes are started for this purpose they may not have the standard parent that we would expect. This list is not exhaustive, and it is possible for cyber actors to avoid this discepency. These signatures only work if Sysmon reports the parent process, which may not always be the case if the parent dies before sysmon processes the event.

## ATT&CK Coverage

- [[kb/attack/techniques/T1055-process_injection|T1055]] (coverage: Low; tactics: TA0005)
  - [[kb/attack/techniques/T1055-process_injection|T1055.012]]

## Implementations

### Pseudocode

This is a pseudocode representation of the below splunk search.

- Data Model: CAR native

```pseudocode
processes = search Process:Create
mismatch_processes = filter processes where ( parent_exe exists AND
  (exe="smss.exe" AND (parent_exe!="smss.exe" AND parent_exe!="System") OR
  (exe="csrss.exe" AND (parent_exe!="smss.exe" AND parent_exe!="svchost.exe")) OR
  (exe="wininit.exe" AND parent_exe!="smss.exe") OR
  (exe="winlogon.exe" AND parent_exe!="smss.exe") OR
  (exe="lsass.exe" AND (parent_exe!="wininit.exe" AND parent_exe!="winlogon.exe")) OR
  (exe="LogonUI.exe" AND (parent_exe!="winlogon.exe" AND parent_exe!="wininit.exe")) OR
  (exe="services.exe" AND parent_exe!="wininit.exe") OR
  (exe="spoolsv.exe" AND parent_exe!="services.exe") OR
  (exe="taskhost.exe" AND (parent_exe!="services.exe" AND parent_exe!="svchost.exe")) OR
  (exe="taskhostw.exe" AND (parent_exe!="services.exe" AND parent_exe!="svchost.exe")) OR
  (exe="userinit.exe" AND (parent_exe!="dwm.exe" AND parent_exe!="winlogon.exe"))
output mismatch_processes
```

### Splunk

Looks for processes that do not have the expected parent. Common Splunk forwarder applications that break these rules are whitelisted; unique environments may require additional whitelist items.

- Data Model: Sysmon native

```splunk
(index=__your_sysmon_index__ EventCode=1) AND ParentImage!="?" AND ParentImage!="C:\\Program Files\\SplunkUniversalForwarder\\bin\\splunk-regmon.exe" AND ParentImage!="C:\\Program Files\\SplunkUniversalForwarder\\bin\\splunk-powershell.exe" AND
((Image="C:\\Windows\System32\\smss.exe" AND (ParentImage!="C:\\Windows\\System32\\smss.exe" AND ParentImage!="System")) OR
(Image="C:\\Windows\\System32\\csrss.exe" AND (ParentImage!="C:\\Windows\\System32\\smss.exe" AND ParentImage!="C:\\Windows\\System32\\svchost.exe")) OR
(Image="C:\\Windows\\System32\\wininit.exe" AND ParentImage!="C:\\Windows\\System32\\smss.exe") OR
(Image="C:\\Windows\\System32\\winlogon.exe" AND ParentImage!="C:\\Windows\\System32\\smss.exe") OR
(Image="C:\\Windows\\System32\\lsass.exe" and ParentImage!="C:\\Windows\\System32\\wininit.exe") OR
(Image="C:\\Windows\\System32\\LogonUI.exe" AND (ParentImage!="C:\\Windows\\System32\\winlogon.exe" AND ParentImage!="C:\\Windows\\System32\\wininit.exe")) OR
(Image="C:\\Windows\\System32\\services.exe" AND ParentImage!="C:\\Windows\\System32\\wininit.exe") OR
(Image="C:\\Windows\\System32\\spoolsv.exe" AND ParentImage!="C:\\Windows\\System32\\services.exe") OR
(Image="C:\\Windows\\System32\\taskhost.exe" AND (ParentImage!="C:\\Windows\\System32\\services.exe" AND ParentImage!="C:\\Windows\\System32\\svchost.exe")) OR
(Image="C:\\Windows\\System32\\taskhostw.exe" AND (ParentImage!="C:\\Windows\\System32\\services.exe" AND ParentImage!="C:\\Windows\\System32\\svchost.exe")) OR
(Image="C:\\Windows\System32\\userinit.exe" AND (ParentImage!="C:\\Windows\\System32\\dwm.exe" AND ParentImage!="C:\\Windows\\System32\\winlogon.exe")))
```

### LogPoint

Looks for processes that do not have the expected parent. Unique environments may require additional whitelist items.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=1 -parent_image="?" ((image="*\smss.exe" (-parent_image="*\smss.exe" -parent_image="*\System")) OR
(image="*\csrss.exe" (-parent_image="*\smss.exe" -parent_image="*\svchost.exe")) OR (image="*\wininit.exe" -parent_image="*\smss.exe") OR
(image="*\winlogon.exe" -parent_image="*\smss.exe") OR (image="*\lsass.exe"  (-parent_image="*\wininit.exe"  -parent_image="*\winlogon.exe")) OR
(image="*\LogonUI.exe"  (-parent_image="*\winlogon.exe"  -parent_image="*\wininit.exe")) OR (image="*\services.exe"  -parent_image="*\wininit.exe") OR
(image="*\spoolsv.exe"  -parent_image="*\services.exe") OR (image="*\taskhost.exe"  (-parent_image="*\services.exe"  -parent_image="*\svchost.exe")) OR
(image="*\taskhostw.exe"  (-parent_image="*\services.exe"  -parent_image="*\svchost.exe")) OR
(image="*\userinit.exe"  (-parent_image="*\dwm.exe"  -parent_image="*\winlogon.exe")))
```

## Data Model References

- process/create/exe
- process/create/parent_exe

## D3FEND Mappings

- [[kb/defend/techniques/D3-PLA-process_lineage_analysis|D3-PLA: Process Lineage Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2020-11-004/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-11-004.yaml)
