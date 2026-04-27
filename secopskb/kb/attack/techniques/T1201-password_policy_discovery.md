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
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
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
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may attempt to access detailed information about the password policy used within an enterprise network or cloud environment. Password policies are a way to enforce complex passwords that are difficult to guess or crack through [[T1110-brute_force|T1110: Brute Force]]. This information may help the adversary to create a list of common passwords and launch dictionary and/or brute force attacks which adheres to the policy (e.g. if the minimum password length should be 8, then not trying passwords such as 'pass123'; not checking for more than 3-4 passwords per account if the lockout is set to 6 as to not lock out accounts).

Password policies can be set and discovered on Windows, Linux, and macOS systems via various command shell utilities such as `net accounts (/domain)`, `Get-ADDefaultDomainPasswordPolicy`, `chage -l <username>`, `cat /etc/pam.d/common-password`, and `pwpolicy getaccountpolicies` (Citation: Superuser Linux Password Policies) (Citation: Jamf User Password Policies). Adversaries may also leverage a [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]] on network devices to discover password policy information (e.g. `show aaa`, `show aaa common-criteria policy all`).(Citation: US-CERT-TA18-106A)

Password policies can be discovered in cloud environments using available APIs such as `GetAccountPasswordPolicy` in AWS (Citation: AWS GetPasswordPolicy).

## Workspace

- [[workspaces/attack/techniques/T1201-password_policy_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1201-password_policy_discovery-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/42a993dd_bb3e_48c8_b372_4d6684c4106c-hacktool_crackmapexec_execution|HackTool - CrackMapExec Execution (high; windows / process_creation)]]

### Atomic Tests

- [[kb/atomic/tests/085fe567_ac84_47c7_ac4c_2688ce28265b-examine_password_complexity_policy_ubuntu|Examine password complexity policy - Ubuntu (bash; linux)]]
- [[kb/atomic/tests/15330820_d405_450b_bd08_16b5be5be9f4-examine_aws_password_policy|Examine AWS Password Policy (sh; iaas:aws)]]
- [[kb/atomic/tests/3177f4da_3d4b_4592_8bdc_aa23d0b2e843-get_domainpolicy_with_powerview|Get-DomainPolicy with PowerView (powershell; windows)]]
- [[kb/atomic/tests/4588d243_f24e_4549_b2e3_e627acc089f6-examine_local_password_policy_windows|Examine local password policy - Windows (command_prompt; windows)]]
- [[kb/atomic/tests/46c2c362_2679_4ef5_aec9_0e958e135be4-examine_domain_password_policy_windows|Examine domain password policy - Windows (command_prompt; windows)]]
- [[kb/atomic/tests/4b7fa042_9482_45e1_b348_4b756b2a0742-examine_password_policy_macos|Examine password policy - macOS (bash; macos)]]
- [[kb/atomic/tests/510cc97f_56ac_4cd3_a198_d3218c23d889-use_of_secedit_exe_to_export_the_local_security_policy_including_the_password_policy|Use of SecEdit.exe to export the local security policy (including the password policy) (command_prompt; windows)]]
- [[kb/atomic/tests/6ce12552_0adb_4f56_89ff_95ce268f6358-examine_password_complexity_policy_centos_rhel_6_x|Examine password complexity policy - CentOS/RHEL 6.x (bash; linux)]]
- [[kb/atomic/tests/78a12e65_efff_4617_bc01_88f17d71315d-examine_password_complexity_policy_centos_rhel_7_x|Examine password complexity policy - CentOS/RHEL 7.x (bash; linux)]]
- [[kb/atomic/tests/7c86c55c_70fa_4a05_83c9_3aa19b145d1a-examine_password_expiration_policy_all_linux|Examine password expiration policy - All Linux (bash; linux)]]
- 2 more in the generated source index

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Mitigations

- [[M1027-password_policies|M1027: Password Policies]]

## Tools
- [[crackmapexec|CrackMapExec (S0488)]]
- [[net|Net (S0039)]]
- [[poshc2|PoshC2 (S0378)]]


## Platforms

- Windows
- Linux
- macOS
- IaaS
- Network Devices
- Identity Provider
- SaaS
- Office Suite

