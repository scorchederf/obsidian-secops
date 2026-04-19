---
id: T1491
name: Defacement
created: 2019-04-08 17:51:41.390000+00:00
modified: 2025-10-24 17:48:49.761000+00:00
type: attack-pattern
x_mitre_version: 1.4
x_mitre_domains: enterprise-attack
---

## Tactic

- [[impact|Impact]]

Adversaries may modify visual content available internally or externally to an enterprise network, thus affecting the integrity of the original content. Reasons for [Defacement](https://attack.mitre.org/techniques/T1491) include delivering messaging, intimidation, or claiming (possibly false) credit for an intrusion. Disturbing or offensive images may be used as a part of [Defacement](https://attack.mitre.org/techniques/T1491) in order to cause user discomfort, or to pressure compliance with accompanying messages. 


## Subtechniques

### T1491.001: Internal Defacement
^t1491001-internal-defacement

**Parent Technique**
- [[T1491-defacement|T1491: Defacement]]

**Tactic**
- [[impact|Impact]]

An adversary may deface systems internal to an organization in an attempt to intimidate or mislead users, thus discrediting the integrity of the systems. This may take the form of modifications to internal websites or server login messages, or directly to user systems with the replacement of the desktop wallpaper.(Citation: Novetta Blockbuster)(Citation: Varonis) Disturbing or offensive images may be used as a part of [Internal Defacement](https://attack.mitre.org/techniques/T1491/001) in order to cause user discomfort, or to pressure compliance with accompanying messages. Since internally defacing systems exposes an adversary's presence, it often takes place after other intrusion goals have been accomplished.(Citation: Novetta Blockbuster Destructive Malware)

#### Properties

- id: T1491.001
- name: Internal Defacement
- created: 2020-02-20 14:31:34.778000+00:00
- modified: 2025-10-24 17:49:05.030000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1491.002: External Defacement
^t1491002-external-defacement

**Parent Technique**
- [[T1491-defacement|T1491: Defacement]]

**Tactic**
- [[impact|Impact]]

An adversary may deface systems external to an organization in an attempt to deliver messaging, intimidate, or otherwise mislead an organization or users. [External Defacement](https://attack.mitre.org/techniques/T1491/002) may ultimately cause users to distrust the systems and to question/discredit the system’s integrity. Externally-facing websites are a common victim of defacement; often targeted by adversary and hacktivist groups in order to push a political message or spread propaganda.(Citation: FireEye Cyber Threats to Media Industries)(Citation: Kevin Mandia Statement to US Senate Committee on Intelligence)(Citation: Anonymous Hackers Deface Russian Govt Site) [External Defacement](https://attack.mitre.org/techniques/T1491/002) may be used as a catalyst to trigger events, or as a response to actions taken by an organization or government. Similarly, website defacement may also be used as setup, or a precursor, for future attacks such as [Drive-by Compromise](https://attack.mitre.org/techniques/T1189).(Citation: Trend Micro Deep Dive Into Defacement)

#### Properties

- id: T1491.002
- name: External Defacement
- created: 2020-02-20 14:34:08.496000+00:00
- modified: 2025-10-24 17:48:23.460000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1053-data_backup|M1053: Data Backup]]

## Platforms

- Windows
- IaaS
- Linux
- macOS
- ESXi

