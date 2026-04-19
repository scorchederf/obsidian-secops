---
id: T1673
name: Virtual Machine Discovery
created: 2025-03-27 15:32:17.400000+00:00
modified: 2025-04-15 21:24:32.155000+00:00
type: attack-pattern
x_mitre_version: 1.0
x_mitre_domains: enterprise-attack
---

## Tactic

- [[discovery|Discovery]]

An adversary may attempt to enumerate running virtual machines (VMs) after gaining access to a host or hypervisor. For example, adversaries may enumerate a list of VMs on an ESXi hypervisor using a [Hypervisor CLI](https://attack.mitre.org/techniques/T1059/012) such as `esxcli` or `vim-cmd` (e.g. `esxcli vm process list or vim-cmd vmsvc/getallvms`).(Citation: Crowdstrike Hypervisor Jackpotting Pt 2 2021)(Citation: TrendMicro Play) Adversaries may also directly leverage a graphical user interface, such as VMware vCenter, in order to view virtual machines on a host. 

Adversaries may use the information from [Virtual Machine Discovery](https://attack.mitre.org/techniques/T1673) during discovery to shape follow-on behaviors. Subsequently discovered VMs may be leveraged for follow-on activities such as [Service Stop](https://attack.mitre.org/techniques/T1489) or [Data Encrypted for Impact](https://attack.mitre.org/techniques/T1486).(Citation: Crowdstrike Hypervisor Jackpotting Pt 2 2021)

## Platforms

- ESXi
- Linux
- macOS
- Windows

## Tools


