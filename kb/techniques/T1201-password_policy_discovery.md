---
id: T1201
name: Password Policy Discovery
created: 2018-04-18 17:59:24.739000+00:00
modified: 2025-10-24 17:49:15.781000+00:00
type: attack-pattern
x_mitre_version: 1.7
x_mitre_domains: enterprise-attack
---

## Tactic

- [[discovery|Discovery]]

Adversaries may attempt to access detailed information about the password policy used within an enterprise network or cloud environment. Password policies are a way to enforce complex passwords that are difficult to guess or crack through [Brute Force](https://attack.mitre.org/techniques/T1110). This information may help the adversary to create a list of common passwords and launch dictionary and/or brute force attacks which adheres to the policy (e.g. if the minimum password length should be 8, then not trying passwords such as 'pass123'; not checking for more than 3-4 passwords per account if the lockout is set to 6 as to not lock out accounts).

Password policies can be set and discovered on Windows, Linux, and macOS systems via various command shell utilities such as <code>net accounts (/domain)</code>, <code>Get-ADDefaultDomainPasswordPolicy</code>, <code>chage -l <username></code>, <code>cat /etc/pam.d/common-password</code>, and <code>pwpolicy getaccountpolicies</code> (Citation: Superuser Linux Password Policies) (Citation: Jamf User Password Policies). Adversaries may also leverage a [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) on network devices to discover password policy information (e.g. <code>show aaa</code>, <code>show aaa common-criteria policy all</code>).(Citation: US-CERT-TA18-106A)

Password policies can be discovered in cloud environments using available APIs such as <code>GetAccountPasswordPolicy</code> in AWS (Citation: AWS GetPasswordPolicy).

## Properties

- id: T1201
- name: Password Policy Discovery
- created: 2018-04-18 17:59:24.739000+00:00
- modified: 2025-10-24 17:49:15.781000+00:00
- type: attack-pattern
- x_mitre_version: 1.7
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1027-password_policies|M1027: Password Policies]]

## Platforms

- Windows
- Linux
- macOS
- IaaS
- Network Devices
- Identity Provider
- SaaS
- Office Suite

## Tools

- [[S0039-net|S0039: Net]]
- [[S0378-poshc2|S0378: PoshC2]]
- [[S0488-crackmapexec|S0488: CrackMapExec]]

