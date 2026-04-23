---
mitre_id: "T1082"
mitre_name: "System Information Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--354a7f88-63fb-41b5-a801-ce3b377b36f1"
mitre_created: "2017-05-31T21:31:04.307Z"
mitre_modified: "2025-10-24T17:48:38.277Z"
mitre_version: "3.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1082/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "ESXi"
  - "IaaS"
  - "Linux"
  - "macOS"
  - "Network Devices"
  - "Windows"
mitre_tactic_ids:
  - "TA0007"
---

# T1082: System Information Discovery

An adversary may attempt to get detailed information about the operating system and hardware, including version, patches, hotfixes, service packs, and architecture. Adversaries may use this information to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions. This behavior is distinct from [[T1680-local_storage_discovery|T1680: Local Storage Discovery]] which is an adversary's discovery of local drive, disks and/or volumes.

Tools such as [[systeminfo|Systeminfo]] can be used to gather detailed system information. If running with privileged access, a breakdown of system data can be gathered through the `systemsetup` configuration tool on macOS. Adversaries may leverage a [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]] on network devices to gather detailed system information (e.g. `show version`).(Citation: US-CERT-TA18-106A) On ESXi servers, threat actors may gather system information from various esxcli utilities, such as `system hostname get` and `system version get`.(Citation: Crowdstrike Hypervisor Jackpotting Pt 2 2021)(Citation: Varonis)

Infrastructure as a Service (IaaS) cloud providers such as AWS, GCP, and Azure allow access to instance and virtual machine information via APIs. Successful authenticated API calls can return data such as the operating system platform and status of a particular instance or the model view of a virtual machine.(Citation: Amazon Describe Instance)(Citation: Google Instances Resource)(Citation: Microsoft Virutal Machine API)

[[T1082-system_information_discovery|T1082: System Information Discovery]] combined with information gathered from other forms of discovery and reconnaissance can drive payload development and concealment.(Citation: OSX.FairyTale)(Citation: 20 macOS Common Tools and Techniques) 

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Tools

- [[systeminfo|Systeminfo]]
- [[dsquery|dsquery]]
- [[cmd|cmd]]
- [[pupy|Pupy]]
- [[koadic|Koadic]]
- [[quasarrat|QuasarRAT]]
- [[empire|Empire]]
- [[poshc2|PoshC2]]
- [[shimratreporter|ShimRatReporter]]
- [[silenttrinity|SILENTTRINITY]]
- [[covenant|Covenant]]

## Platforms

- ESXi
- IaaS
- Linux
- macOS
- Network Devices
- Windows

