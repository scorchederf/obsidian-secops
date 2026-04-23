---
mitre_id: "T1554"
mitre_name: "Compromise Host Software Binary"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--960c3c86-1480-4d72-b4e0-8c242e84a5c5"
mitre_created: "2020-02-11T18:18:34.279Z"
mitre_modified: "2025-10-24T17:49:07.572Z"
mitre_version: "2.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1554/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
  - "ESXi"
mitre_tactic_ids:
  - "TA0003"
---

# T1554: Compromise Host Software Binary

Adversaries may modify host software binaries to establish persistent access to systems. Software binaries/executables provide a wide range of system commands or services, programs, and libraries. Common software binaries are SSH clients, FTP clients, email clients, web browsers, and many other user or server applications.

Adversaries may establish persistence though modifications to host software binaries. For example, an adversary may replace or otherwise infect a legitimate application binary (or support files) with a backdoor. Since these binaries may be routinely executed by applications or the user, the adversary can leverage this for persistent access to the host. An adversary may also modify a software binary such as an SSH client in order to persistently collect credentials during logins (i.e., [[T1556-modify_authentication_process|T1556: Modify Authentication Process]]).(Citation: Google Cloud Mandiant UNC3886 2024)

An adversary may also modify an existing binary by patching in malicious functionality (e.g., IAT Hooking/Entry point patching)(Citation: Unit42 Banking Trojans Hooking 2022) prior to the binary’s legitimate execution. For example, an adversary may modify the entry point of a binary to point to malicious code patched in by the adversary before resuming normal execution flow.(Citation: ESET FontOnLake Analysis 2021)

After modifying a binary, an adversary may attempt to [[T1562-impair_defenses|T1562: Impair Defenses]] by preventing it from updating (e.g., via the `yum-versionlock` command or `versionlock.list` file in Linux systems that use the yum package manager).(Citation: Google Cloud Mandiant UNC3886 2024)

## Tactics

- [[TA0003-persistence|TA0003: Persistence]]

## Mitigations

- [[M1045-code_signing|M1045: Code Signing]]

## Platforms

- Linux
- macOS
- Windows
- ESXi

