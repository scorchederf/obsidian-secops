---
mitre_id: "T1074"
mitre_name: "Data Staged"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--7dd95ff6-712e-4056-9626-312ea4ab4c5e"
mitre_created: "2017-05-31T21:30:58.938Z"
mitre_modified: "2025-10-24T17:49:01.010Z"
mitre_version: "1.5"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1074/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
  - "IaaS"
  - "Linux"
  - "macOS"
  - "ESXi"
mitre_tactic_ids:
  - "TA0009"
---

# T1074: Data Staged

Adversaries may stage collected data in a central location or directory prior to Exfiltration. Data may be kept in separate files or combined into one file through techniques such as [[T1560-archive_collected_data|T1560: Archive Collected Data]]. Interactive command shells may be used, and common functionality within [[cmd|cmd]] and bash may be used to copy data into a staging location.(Citation: PWC Cloud Hopper April 2017)

In cloud environments, adversaries may stage data within a particular instance or virtual machine before exfiltration. An adversary may [[T1578-modify_cloud_compute_infrastructure#^t1578002-create-cloud-instance|T1578.002: Create Cloud Instance]] and stage data in that instance.(Citation: Mandiant M-Trends 2020)

Adversaries may choose to stage data from a victim network in a centralized location prior to Exfiltration to minimize the number of connections made to their C2 server and better evade detection.

## Tactics

- [[TA0009-collection|TA0009: Collection]]

## Subtechniques

### T1074.001: Local Data Staging

^t1074001-local-data-staging

Adversaries may stage collected data in a central location or directory on the local system prior to Exfiltration. Data may be kept in separate files or combined into one file through techniques such as [[T1560-archive_collected_data|T1560: Archive Collected Data]]. Interactive command shells may be used, and common functionality within [[cmd|cmd]] and bash may be used to copy data into a staging location.

Adversaries may also stage collected data in various available formats/locations of a system, including local storage databases/repositories or the Windows Registry.(Citation: Prevailion DarkWatchman 2021)

### T1074.002: Remote Data Staging

^t1074002-remote-data-staging

Adversaries may stage data collected from multiple systems in a central location or directory on one system prior to Exfiltration. Data may be kept in separate files or combined into one file through techniques such as [[T1560-archive_collected_data|T1560: Archive Collected Data]]. Interactive command shells may be used, and common functionality within [[cmd|cmd]] and bash may be used to copy data into a staging location.

In cloud environments, adversaries may stage data within a particular instance or virtual machine before exfiltration. An adversary may [[T1578-modify_cloud_compute_infrastructure#^t1578002-create-cloud-instance|T1578.002: Create Cloud Instance]] and stage data in that instance.(Citation: Mandiant M-Trends 2020)

By staging data on one system prior to Exfiltration, adversaries can minimize the number of connections made to their C2 server and better evade detection.

## Platforms

- Windows
- IaaS
- Linux
- macOS
- ESXi

