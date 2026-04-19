---
id: T1063
name: Security Software Discovery
created: 2017-05-31 21:30:51.330000+00:00
modified: 2025-10-24 17:48:31.974000+00:00
type: attack-pattern
x_mitre_version: 2.2
x_mitre_domains: enterprise-attack
---

## Tactic

- [[discovery|Discovery]]

Adversaries may attempt to get a listing of security software, configurations, defensive tools, and sensors that are installed on the system. This may include things such as local firewall rules and anti-virus. Adversaries may use the information from [Security Software Discovery](https://attack.mitre.org/techniques/T1063) during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.


### Windows

Example commands that can be used to obtain security software information are [netsh](https://attack.mitre.org/software/S0108), <code>reg query</code> with [Reg](https://attack.mitre.org/software/S0075), <code>dir</code> with [cmd](https://attack.mitre.org/software/S0106), and [Tasklist](https://attack.mitre.org/software/S0057), but other indicators of discovery behavior may be more specific to the type of software or security system the adversary is looking for.

### Mac

It's becoming more common to see macOS malware perform checks for LittleSnitch and KnockKnock software.

## Platforms

- macOS
- Windows

