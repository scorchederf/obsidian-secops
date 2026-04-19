---
id: T1082
name: System Information Discovery
created: 2017-05-31 21:31:04.307000+00:00
modified: 2025-10-24 17:48:38.277000+00:00
type: attack-pattern
x_mitre_version: 3.0
x_mitre_domains: enterprise-attack
---

## Tactic

- [[discovery|Discovery]]

An adversary may attempt to get detailed information about the operating system and hardware, including version, patches, hotfixes, service packs, and architecture. Adversaries may use this information to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions. This behavior is distinct from [Local Storage Discovery](https://attack.mitre.org/techniques/T1680) which is an adversary's discovery of local drive, disks and/or volumes.

Tools such as [Systeminfo](https://attack.mitre.org/software/S0096) can be used to gather detailed system information. If running with privileged access, a breakdown of system data can be gathered through the <code>systemsetup</code> configuration tool on macOS. Adversaries may leverage a [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) on network devices to gather detailed system information (e.g. <code>show version</code>).(Citation: US-CERT-TA18-106A) On ESXi servers, threat actors may gather system information from various esxcli utilities, such as `system hostname get` and `system version get`.(Citation: Crowdstrike Hypervisor Jackpotting Pt 2 2021)(Citation: Varonis)

Infrastructure as a Service (IaaS) cloud providers such as AWS, GCP, and Azure allow access to instance and virtual machine information via APIs. Successful authenticated API calls can return data such as the operating system platform and status of a particular instance or the model view of a virtual machine.(Citation: Amazon Describe Instance)(Citation: Google Instances Resource)(Citation: Microsoft Virutal Machine API)

[System Information Discovery](https://attack.mitre.org/techniques/T1082) combined with information gathered from other forms of discovery and reconnaissance can drive payload development and concealment.(Citation: OSX.FairyTale)(Citation: 20 macOS Common Tools and Techniques) 

## Properties

- id: T1082
- name: System Information Discovery
- created: 2017-05-31 21:31:04.307000+00:00
- modified: 2025-10-24 17:48:38.277000+00:00
- type: attack-pattern
- x_mitre_version: 3.0
- x_mitre_domains: enterprise-attack

## Platforms

- ESXi
- IaaS
- Linux
- macOS
- Network Devices
- Windows

## Tools

- [[S0096-systeminfo|S0096: Systeminfo]]
- [[S0105-dsquery|S0105: dsquery]]
- [[S0106-cmd|S0106: cmd]]
- [[S0192-pupy|S0192: Pupy]]
- [[S0250-koadic|S0250: Koadic]]
- [[S0262-quasarrat|S0262: QuasarRAT]]
- [[S0363-empire|S0363: Empire]]
- [[S0378-poshc2|S0378: PoshC2]]
- [[S0445-shimratreporter|S0445: ShimRatReporter]]
- [[S0692-silenttrinity|S0692: SILENTTRINITY]]
- [[S1155-covenant|S1155: Covenant]]

