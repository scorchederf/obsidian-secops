---
id: T1123
name: Audio Capture
created: 2017-05-31 21:31:34.528000+00:00
modified: 2025-10-24 17:48:24.702000+00:00
type: attack-pattern
x_mitre_version: 1.0
x_mitre_domains: enterprise-attack
---

## Tactic

- [[collection|Collection]]

An adversary can leverage a computer's peripheral devices (e.g., microphones and webcams) or applications (e.g., voice and video call services) to capture audio recordings for the purpose of listening into sensitive conversations to gather information.(Citation: ESET Attor Oct 2019)

Malware or scripts may be used to interact with the devices through an available API provided by the operating system or an application to capture audio. Audio files may be written to disk and exfiltrated later.

## Properties

- id: T1123
- name: Audio Capture
- created: 2017-05-31 21:31:34.528000+00:00
- modified: 2025-10-24 17:48:24.702000+00:00
- type: attack-pattern
- x_mitre_version: 1.0
- x_mitre_domains: enterprise-attack

## Platforms

- Linux
- macOS
- Windows

## Tools

- [[S0192-pupy|S0192: Pupy]]
- [[S0194-powersploit|S0194: PowerSploit]]
- [[S0332-remcos|S0332: Remcos]]
- [[S0434-imminent_monitor|S0434: Imminent Monitor]]

