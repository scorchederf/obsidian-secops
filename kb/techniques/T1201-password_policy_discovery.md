---
mitre_id: "T1201"
mitre_name: "Password Policy Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--b6075259-dba3-44e9-87c7-e954f37ec0d5"
mitre_created: "2018-04-18T17:59:24.739Z"
mitre_modified: "2025-10-24T17:49:15.781Z"
mitre_version: "1.7"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1201/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
  - "Linux"
  - "macOS"
  - "IaaS"
  - "Network Devices"
  - "Identity Provider"
  - "SaaS"
  - "Office Suite"
mitre_tactic_ids:
  - "TA0007"
---

# T1201: Password Policy Discovery

Adversaries may attempt to access detailed information about the password policy used within an enterprise network or cloud environment. Password policies are a way to enforce complex passwords that are difficult to guess or crack through [[T1110-brute_force|T1110: Brute Force]]. This information may help the adversary to create a list of common passwords and launch dictionary and/or brute force attacks which adheres to the policy (e.g. if the minimum password length should be 8, then not trying passwords such as 'pass123'; not checking for more than 3-4 passwords per account if the lockout is set to 6 as to not lock out accounts).

Password policies can be set and discovered on Windows, Linux, and macOS systems via various command shell utilities such as `net accounts (/domain)`, `Get-ADDefaultDomainPasswordPolicy`, `chage -l <username>`, `cat /etc/pam.d/common-password`, and `pwpolicy getaccountpolicies` (Citation: Superuser Linux Password Policies) (Citation: Jamf User Password Policies). Adversaries may also leverage a [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]] on network devices to discover password policy information (e.g. `show aaa`, `show aaa common-criteria policy all`).(Citation: US-CERT-TA18-106A)

Password policies can be discovered in cloud environments using available APIs such as `GetAccountPasswordPolicy` in AWS (Citation: AWS GetPasswordPolicy).

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Mitigations

- [[M1027-password_policies|M1027: Password Policies]]

## Tools

- [[net|Net]]
- [[poshc2|PoshC2]]
- [[crackmapexec|CrackMapExec]]

## Platforms

- Windows
- Linux
- macOS
- IaaS
- Network Devices
- Identity Provider
- SaaS
- Office Suite

