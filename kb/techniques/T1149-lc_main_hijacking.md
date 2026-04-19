---
id: T1149
name: LC_MAIN Hijacking
created: 2017-12-14 16:46:06.044000+00:00
modified: 2025-10-24 17:49:10.098000+00:00
type: attack-pattern
x_mitre_version: 2.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[defense_evasion|Defense Evasion]]

**This technique has been deprecated and should no longer be used.**

As of OS X 10.8, mach-O binaries introduced a new header called LC_MAIN that points to the binary’s entry point for execution. Previously, there were two headers to achieve this same effect: LC_THREAD and LC_UNIXTHREAD  (Citation: Prolific OSX Malware History). The entry point for a binary can be hijacked so that initial execution flows to a malicious addition (either another section or a code cave) and then goes back to the initial entry point so that the victim doesn’t know anything was different  (Citation: Methods of Mac Malware Persistence). By modifying a binary in this way, application whitelisting can be bypassed because the file name or application path is still the same.

## Properties

- id: T1149
- name: LC_MAIN Hijacking
- created: 2017-12-14 16:46:06.044000+00:00
- modified: 2025-10-24 17:49:10.098000+00:00
- type: attack-pattern
- x_mitre_version: 2.1
- x_mitre_domains: enterprise-attack

## Platforms

- macOS

