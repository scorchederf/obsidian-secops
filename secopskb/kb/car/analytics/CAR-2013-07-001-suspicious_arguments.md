---
car_id: "CAR-2013-07-001"
title: "Suspicious Arguments"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2013-07-001/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-07-001.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2013-07-001"
  - "Suspicious Arguments"
attack_technique_ids:
  - "T1003"
  - "T1003.001"
  - "T1021"
  - "T1105"
platforms:
  - "Windows"
  - "Linux"
  - "macOS"
implementation_types:
  - "pseudocode"
  - "splunk"
  - "EQL"
  - "DNIF"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

# CAR-2013-07-001: Suspicious Arguments

## Metadata

- CAR ID: CAR-2013-07-001
- Submission Date: 2013/07/05
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows, Linux, macOS
- Data Subtypes: Process
- Contributors: MITRE

## Description

Malicious actors may rename built-in commands or external tools, such as those provided by SysInternals, to better [blend in](https://attack.mitre.org/tactics/TA0005) with the environment. In those cases, the file path name is arbitrary and may blend in well with the background. If the arguments are closely inspected, it may be possible to infer what tools are running and understand what an adversary is doing. When any legitimate software shares the same command lines, it must be whitelisted according to the expected parameters.

Any tool of interest with commonly known command line usage can be detecting by command line analysis. Known substrings of command lines include

-   PuTTY
-   port forwarding `-R * -pw`
-   secure copy (scp) `-pw * * *@*`
-   mimikatz `sekurlsa::`
-   RAR `* -hp *`
-   Archive`* a *`
    Additionally, it may be useful to find IP addresses in the command line
-   `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`
    Logically this analytic makes use of [[kb/car/analytics/CAR-2014-03-005-remotely_launched_executables_via_services|CAR-2014-03-005]].

## ATT&CK Coverage

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]] (coverage: Low; tactics: TA0006)
  - [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]
- [[kb/attack/techniques/T1021-remote_services|T1021]] (coverage: Moderate; tactics: TA0008)
- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]] (coverage: Moderate; tactics: TA0011, TA0008)

## Implementations

### pseudocode

Identify process launches that contain substrings that belong to known tools and do not match the expected process names. These will help to indicate instances of tools that have been renamed.

```pseudocode
process = search Process:Create
port_fwd = filter process where (command_line match "-R .* -pw")
scp = filter process where (command_line match "-pw .* .* .*@.*"
mimikatz = filter process where (command_line match "sekurlsa")
rar = filter process where (command_line match " -hp ")
archive = filter process where (command_line match ".* a .*")
ip_addr = filter process where (command_line match \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})

output port_fwd, scp, mimikatz, rar, archive, ip_addr
```

### splunk

Splunk version of the above pseudocode, excluding the IP address search.

- Data Model: Sysmon native

```splunk
index=__your_sysmon_index__ EventCode=1 (CommandLine="* -R * -pw*" OR CommandLine="* -pw * *@*" OR CommandLine="*sekurlsa*" OR CommandLine="* -hp *" OR CommandLine="* a *")
```

### EQL

EQL version of the above pseudocode, excluding the IP address search.

- Data Model: EQL native

```eql
process where subtype.create and
  (command_line == "* -R * -pw*" or command_line == "* -pw * *@*" or command_line == "*sekurlsa*" or command_line == "* -hp *" or command_line == "* a *")
```

### splunk

Splunk version of the above pseudocode, solely for the IP address search. Note that this will likely result in many false positives, since things like software version numbers can also be valid IPv4 addresses.

- Data Model: Sysmon native

```splunk
index=__your_sysmon_index__ EventCode=1 |regex CommandLine=".*\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}\b.*"
```

### DNIF

DNIF version of the above pseudocode.

- Data Model: Sysmon native

```dnif
_fetch * from event where $LogName=WINDOWS-SYSMON AND $EventID=1 AND $Process=regex(.*(\-r.*\-pw|\-pw.*\@|sekurlsa|\-hp| a |\\d\{1\,3\}\\\.\\d\{1\,3\}\\\.\\d\{1\,3\}).*)i limit 100
```

### LogPoint

LogPoint version of the above pseudocode.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=1 (command="* -R * -pw*" OR command="* -pw * *@*" OR command="*sekurlsa*" OR command="* -hp *" OR command="* a *")
```

## Data Model References

- process/create/command_line
- process/create/exe

## Unit Tests

Download and run Putty from the command line to connect to an SSH server using remote port forwarding. Note that this requires specifying your remote system password on the command line, where it will be logged and visible. It is highly recommended that you specify an incorrect password and not complete the login, or use a temporary password.

- Configurations: Windows 7

```text
putty.exe -pw <password> -R <port>:<host> <user>@<host>
```

Download 7zip or other archiving software you plan to monitor. Create an innocuous text file for testing, or substitute an existing file.

- Configurations: Windows 7

```text
7z.exe a test.zip test.txt
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2013-07-001/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-07-001.yaml)
