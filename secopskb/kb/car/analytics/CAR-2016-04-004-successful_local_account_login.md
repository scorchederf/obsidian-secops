---
car_id: "CAR-2016-04-004"
title: "Successful Local Account Login"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2016-04-004/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2016-04-004.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2016-04-004"
  - "Successful Local Account Login"
attack_technique_ids:
  - "T1550"
  - "T1550.002"
platforms:
  - "Windows"
implementation_types:
  - "pseudocode"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

# CAR-2016-04-004: Successful Local Account Login

## Metadata

- CAR ID: CAR-2016-04-004
- Submission Date: 2016/04/18
- Information Domain: Host
- Analytic Type: Situational Awareness
- Platforms: Windows
- Data Subtypes: Login
- Contributors: MITRE/NSA

## Description

The successful use of [Pass The Hash](https://attack.mitre.org/techniques/T1550/002/) for lateral movement between workstations would trigger event ID 4624, with an event level of Information, from the security log. This behavior would be a LogonType of 3 using NTLM authentication where it is not a domain logon and not the ANONYMOUS LOGON account.

## ATT&CK Coverage

- [[kb/attack/techniques/T1550-use_alternate_authentication_material|T1550]] (coverage: Moderate; tactics: TA0008)
  - [[kb/attack/techniques/T1550-use_alternate_authentication_material|T1550.002]]

## Implementations

### pseudocode

This analytic will look for remote logins, using a non domain login, from one host to another, using NTL authentication where the account is not "ANONYMOUS LOGON".

```pseudocode
EventCode == 4624 and [target_user_name] != "ANONYMOUS LOGON" and
[authentication_package_name] == "NTLM"
```

## Unit Tests

As an adminstrator, create a new user. Then, logon to the host with that new user. This is generate the event.

- Configurations: Windows 7

```text
net user 'test' 'test' /add
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-LAM-local_account_monitoring|D3-LAM: Local Account Monitoring]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2016-04-004/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2016-04-004.yaml)
