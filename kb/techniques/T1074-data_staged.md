---
id: T1074
name: Data Staged
created: 2017-05-31 21:30:58.938000+00:00
modified: 2025-10-24 17:49:01.010000+00:00
type: attack-pattern
x_mitre_version: 1.5
x_mitre_domains: enterprise-attack
---

## Tactic

- [[collection|Collection]]

Adversaries may stage collected data in a central location or directory prior to Exfiltration. Data may be kept in separate files or combined into one file through techniques such as [Archive Collected Data](https://attack.mitre.org/techniques/T1560). Interactive command shells may be used, and common functionality within [cmd](https://attack.mitre.org/software/S0106) and bash may be used to copy data into a staging location.(Citation: PWC Cloud Hopper April 2017)

In cloud environments, adversaries may stage data within a particular instance or virtual machine before exfiltration. An adversary may [Create Cloud Instance](https://attack.mitre.org/techniques/T1578/002) and stage data in that instance.(Citation: Mandiant M-Trends 2020)

Adversaries may choose to stage data from a victim network in a centralized location prior to Exfiltration to minimize the number of connections made to their C2 server and better evade detection.

## Subtechniques

### T1074.001: Local Data Staging
^t1074001-local-data-staging

**Parent Technique**
- [[T1074-data_staged|T1074: Data Staged]]

**Tactic**
- [[collection|Collection]]

Adversaries may stage collected data in a central location or directory on the local system prior to Exfiltration. Data may be kept in separate files or combined into one file through techniques such as [Archive Collected Data](https://attack.mitre.org/techniques/T1560). Interactive command shells may be used, and common functionality within [cmd](https://attack.mitre.org/software/S0106) and bash may be used to copy data into a staging location.

Adversaries may also stage collected data in various available formats/locations of a system, including local storage databases/repositories or the Windows Registry.(Citation: Prevailion DarkWatchman 2021)

#### Properties

- id: T1074.001
- name: Local Data Staging
- created: 2020-03-13 21:13:10.467000+00:00
- modified: 2025-10-24 17:48:28.868000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1074.002: Remote Data Staging
^t1074002-remote-data-staging

**Parent Technique**
- [[T1074-data_staged|T1074: Data Staged]]

**Tactic**
- [[collection|Collection]]

Adversaries may stage data collected from multiple systems in a central location or directory on one system prior to Exfiltration. Data may be kept in separate files or combined into one file through techniques such as [Archive Collected Data](https://attack.mitre.org/techniques/T1560). Interactive command shells may be used, and common functionality within [cmd](https://attack.mitre.org/software/S0106) and bash may be used to copy data into a staging location.

In cloud environments, adversaries may stage data within a particular instance or virtual machine before exfiltration. An adversary may [Create Cloud Instance](https://attack.mitre.org/techniques/T1578/002) and stage data in that instance.(Citation: Mandiant M-Trends 2020)

By staging data on one system prior to Exfiltration, adversaries can minimize the number of connections made to their C2 server and better evade detection.

#### Properties

- id: T1074.002
- name: Remote Data Staging
- created: 2020-03-13 21:14:58.206000+00:00
- modified: 2025-10-24 17:48:38.453000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

## Platforms

- Windows
- IaaS
- Linux
- macOS
- ESXi

## Tools


