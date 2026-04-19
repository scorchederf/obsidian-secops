---
id: T1161
name: LC_LOAD_DYLIB Addition
created: 2017-12-14 16:46:06.044000+00:00
modified: 2025-10-24 17:48:20.839000+00:00
type: attack-pattern
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[persistence|Persistence]]

Mach-O binaries have a series of headers that are used to perform certain operations when a binary is loaded. The LC_LOAD_DYLIB header in a Mach-O binary tells macOS and OS X which dynamic libraries (dylibs) to load during execution time. These can be added ad-hoc to the compiled binary as long adjustments are made to the rest of the fields and dependencies (Citation: Writing Bad Malware for OSX). There are tools available to perform these changes. Any changes will invalidate digital signatures on binaries because the binary is being modified. Adversaries can remediate this issue by simply removing the LC_CODE_SIGNATURE command from the binary so that the signature isn’t checked at load time (Citation: Malware Persistence on OS X).

## Properties

- id: T1161
- name: LC_LOAD_DYLIB Addition
- created: 2017-12-14 16:46:06.044000+00:00
- modified: 2025-10-24 17:48:20.839000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Platforms

- macOS

