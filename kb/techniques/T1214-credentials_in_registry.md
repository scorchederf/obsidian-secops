---
id: T1214
name: Credentials in Registry
created: 2018-04-18 17:59:24.739000+00:00
modified: 2025-10-24 17:48:35.620000+00:00
type: attack-pattern
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[credential_access|Credential Access]]

The Windows Registry stores configuration information that can be used by the system or other programs. Adversaries may query the Registry looking for credentials and passwords that have been stored for use by other programs or services. Sometimes these credentials are used for automatic logons.

Example commands to find Registry keys related to password information: (Citation: Pentestlab Stored Credentials)

* Local Machine Hive: <code>reg query HKLM /f password /t REG_SZ /s</code>
* Current User Hive: <code>reg query HKCU /f password /t REG_SZ /s</code>

## Properties

- id: T1214
- name: Credentials in Registry
- created: 2018-04-18 17:59:24.739000+00:00
- modified: 2025-10-24 17:48:35.620000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Platforms

- Windows

