---
id: T1554
name: Compromise Host Software Binary
created: 2020-02-11 18:18:34.279000+00:00
modified: 2025-10-24 17:49:07.572000+00:00
type: attack-pattern
x_mitre_version: 2.2
x_mitre_domains: enterprise-attack
---

## Tactic

- [[persistence|Persistence]]

Adversaries may modify host software binaries to establish persistent access to systems. Software binaries/executables provide a wide range of system commands or services, programs, and libraries. Common software binaries are SSH clients, FTP clients, email clients, web browsers, and many other user or server applications.

Adversaries may establish persistence though modifications to host software binaries. For example, an adversary may replace or otherwise infect a legitimate application binary (or support files) with a backdoor. Since these binaries may be routinely executed by applications or the user, the adversary can leverage this for persistent access to the host. An adversary may also modify a software binary such as an SSH client in order to persistently collect credentials during logins (i.e., [Modify Authentication Process](https://attack.mitre.org/techniques/T1556)).(Citation: Google Cloud Mandiant UNC3886 2024)

An adversary may also modify an existing binary by patching in malicious functionality (e.g., IAT Hooking/Entry point patching)(Citation: Unit42 Banking Trojans Hooking 2022) prior to the binary’s legitimate execution. For example, an adversary may modify the entry point of a binary to point to malicious code patched in by the adversary before resuming normal execution flow.(Citation: ESET FontOnLake Analysis 2021)

After modifying a binary, an adversary may attempt to [Impair Defenses](https://attack.mitre.org/techniques/T1562) by preventing it from updating (e.g., via the `yum-versionlock` command or `versionlock.list` file in Linux systems that use the yum package manager).(Citation: Google Cloud Mandiant UNC3886 2024)

## Properties

- id: T1554
- name: Compromise Host Software Binary
- created: 2020-02-11 18:18:34.279000+00:00
- modified: 2025-10-24 17:49:07.572000+00:00
- type: attack-pattern
- x_mitre_version: 2.2
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1045-code_signing|M1045: Code Signing]]

## Platforms

- Linux
- macOS
- Windows
- ESXi

## Tools


