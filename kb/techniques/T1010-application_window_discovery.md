---
id: T1010
name: Application Window Discovery
created: 2017-05-31 21:30:24.512000+00:00
modified: 2025-10-24 17:48:44.488000+00:00
type: attack-pattern
x_mitre_version: 1.3
x_mitre_domains: enterprise-attack
---

## Tactic

- [[discovery|Discovery]]

Adversaries may attempt to get a listing of open application windows. Window listings could convey information about how the system is used.(Citation: Prevailion DarkWatchman 2021) For example, information about application windows could be used identify potential data to collect as well as identifying security tooling ([Security Software Discovery](https://attack.mitre.org/techniques/T1518/001)) to evade.(Citation: ESET Grandoreiro April 2020)

Adversaries typically abuse system features for this type of enumeration. For example, they may gather information through native system features such as [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059) commands and [Native API](https://attack.mitre.org/techniques/T1106) functions.

## Properties

- id: T1010
- name: Application Window Discovery
- created: 2017-05-31 21:30:24.512000+00:00
- modified: 2025-10-24 17:48:44.488000+00:00
- type: attack-pattern
- x_mitre_version: 1.3
- x_mitre_domains: enterprise-attack

## Platforms

- Linux
- Windows
- macOS

## Tools

- [[S0692-silenttrinity|S0692: SILENTTRINITY]]

