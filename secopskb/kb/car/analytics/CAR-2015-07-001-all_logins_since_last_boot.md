---
car_id: "CAR-2015-07-001"
title: "All Logins Since Last Boot"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2015-07-001/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2015-07-001.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2015-07-001"
  - "All Logins Since Last Boot"
platforms:
  - "Windows"
  - "Linux"
  - "macOS"
implementation_types:
  - "pseudocode"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

# CAR-2015-07-001: All Logins Since Last Boot

## Metadata

- CAR ID: CAR-2015-07-001
- Submission Date: 2015/07/17
- Information Domain: Host
- Analytic Type: Situational Awareness
- Platforms: Windows, Linux, macOS
- Data Subtypes: Login
- Contributors: MITRE

## Description

Once a credential dumper like [mimikatz](https://attack.mitre.org/software/S0002) runs, every user logged on since boot is potentially compromised, because the credentials were accessed via the memory of `lsass.exe`. When such an event occurs, this analytic will give the forensic context to identify compromised users. Those users could potentially be used in later events for additional logons.

The time field indicates the first and last time a system reported a user logged into a given system. This means that activity could be intermittent between the times given and should not be considered a duration.


### Output Description

A list of hostnames and the users that had been logged into the system at some point after to the system's last restart.

## Implementations

### pseudocode

This analytic requires some means of accessing system logs to get records of boot times for hosts (in the example as `SystemLogs:Bootup`. It looks for the latest boot time to happen before some user-defined point in time. Once the boot time is identified, all of the important user login events can be gathered to create a list of potentially compromised accounts. This could be critical for identifying steps an adversary could have taken after stealing credentials with a tool that operates like [mimikatz](https://attack.mitre.org/software/S0002/).

```pseudocode
input target_host
input event_time

all_boots = search SystemLogs:BootUp where (hostname == target_host and time < event_time)
boot_time = max(all_boots.time)

user_logins = search UserSession:Login
host_logins = filter user_logins where (hostname == target_host and boot_time < time < event_time)
compromised_accounts = unique(user_logins.user)

output users
```

## Data Model References

- user_session/login/user

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2015-07-001/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2015-07-001.yaml)
