---
id: T1018
name: Remote System Discovery
created: 2017-05-31 21:30:28.187000+00:00
modified: 2025-10-24 17:49:31.319000+00:00
type: attack-pattern
x_mitre_version: 3.6
x_mitre_domains: enterprise-attack
---

## Tactic

- [[discovery|Discovery]]

Adversaries may attempt to get a listing of other systems by IP address, hostname, or other logical identifier on a network that may be used for Lateral Movement from the current system. Functionality could exist within remote access tools to enable this, but utilities available on the operating system could also be used such as  [Ping](https://attack.mitre.org/software/S0097), <code>net view</code> using [Net](https://attack.mitre.org/software/S0039), or, on ESXi servers, `esxcli network diag ping`.

Adversaries may also analyze data from local host files (ex: <code>C:\Windows\System32\Drivers\etc\hosts</code> or <code>/etc/hosts</code>) or other passive means (such as local [Arp](https://attack.mitre.org/software/S0099) cache entries) in order to discover the presence of remote systems in an environment.

Adversaries may also target discovery of network infrastructure as well as leverage [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) commands on network devices to gather detailed information about systems within a network (e.g. <code>show cdp neighbors</code>, <code>show arp</code>).(Citation: US-CERT-TA18-106A)(Citation: CISA AR21-126A FIVEHANDS May 2021)  


## Properties

- id: T1018
- name: Remote System Discovery
- created: 2017-05-31 21:30:28.187000+00:00
- modified: 2025-10-24 17:49:31.319000+00:00
- type: attack-pattern
- x_mitre_version: 3.6
- x_mitre_domains: enterprise-attack

## Platforms

- ESXi
- Linux
- macOS
- Network Devices
- Windows

## Tools

- [[S0039-net|S0039: Net]]
- [[S0097-ping|S0097: Ping]]
- [[S0099-arp|S0099: Arp]]
- [[S0359-nltest|S0359: Nltest]]
- [[S0488-crackmapexec|S0488: CrackMapExec]]
- [[S0521-bloodhound|S0521: BloodHound]]
- [[S0552-adfind|S0552: AdFind]]
- [[S0590-nbtscan|S0590: NBTscan]]
- [[S0684-roadtools|S0684: ROADTools]]
- [[S0692-silenttrinity|S0692: SILENTTRINITY]]

