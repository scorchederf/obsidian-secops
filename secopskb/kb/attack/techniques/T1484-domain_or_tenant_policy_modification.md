---
mitre_id: "T1484"
mitre_name: "Domain or Tenant Policy Modification"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--ebb42bbe-62d7-47d7-a55f-3b08b61d792d"
mitre_created: "2019-03-07T14:10:32.650Z"
mitre_modified: "2025-10-24T17:49:33.897Z"
mitre_version: "3.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1484/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
  - "Identity Provider"
mitre_tactic_ids:
  - "TA0005"
  - "TA0004"
d3fend_ids:
  - "D3-AM"
  - "D3-CI"
  - "D3-NTPM"
  - "D3-RC"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may modify the configuration settings of a domain or identity tenant to evade defenses and/or escalate privileges in centrally managed environments. Such services provide a centralized means of managing identity resources such as devices and accounts, and often include configuration settings that may apply between domains or tenants such as trust relationships, identity syncing, or identity federation.

Modifications to domain or tenant settings may include altering domain Group Policy Objects (GPOs) in Microsoft Active Directory (AD) or changing trust settings for domains, including federation trusts relationships between domains or tenants.

With sufficient permissions, adversaries can modify domain or tenant policy settings. Since configuration settings for these services apply to a large number of identity resources, there are a great number of potential attacks malicious outcomes that can stem from this abuse. Examples of such abuse include:  

* modifying GPOs to push a malicious [[T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]] to computers throughout the domain environment(Citation: ADSecurity GPO Persistence 2016)(Citation: Wald0 Guide to GPOs)(Citation: Harmj0y Abusing GPO Permissions)
* modifying domain trusts to include an adversary-controlled domain, allowing adversaries to  forge access tokens that will subsequently be accepted by victim domain resources(Citation: Microsoft - Customer Guidance on Recent Nation-State Cyber Attacks)
* changing configuration settings within the AD environment to implement a [[T1207-rogue_domain_controller|T1207: Rogue Domain Controller]].
* adding new, adversary-controlled federated identity providers to identity tenants, allowing adversaries to authenticate as any user managed by the victim tenant (Citation: Okta Cross-Tenant Impersonation 2023)

Adversaries may temporarily modify domain or tenant policy, carry out a malicious action(s), and then revert the change to remove suspicious indicators.

## Workspace

- [[workspaces/attack/techniques/T1484-domain_or_tenant_policy_modification-note|Open workspace note]]

![[workspaces/attack/techniques/T1484-domain_or_tenant_policy_modification-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/9494bff8_959f_4440_bbce_fb87a208d517-changes_to_device_registration_policy|Changes to Device Registration Policy (high; azure / auditlogs)]]

### Atomic Tests

- [[kb/atomic/tests/8906c5d0_3ee5_4f63_897a_f6cafd3fdbb7-add_federation_to_azure_ad|Add Federation to Azure AD (powershell; azure-ad)]]
- [[kb/atomic/tests/9ab80952_74ee_43da_a98c_1e740a985f28-lockbit_black_modify_group_policy_settings_cmd|LockBit Black - Modify Group policy settings -cmd (command_prompt; windows)]]
- [[kb/atomic/tests/b51eae65_5441_4789_b8e8_64783c26c1d1-lockbit_black_modify_group_policy_settings_powershell|LockBit Black - Modify Group policy settings -Powershell (powershell; windows)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]
- [[TA0004-privilege_escalation|TA0004: Privilege Escalation]]

## D3FEND

- [[D3-AM-access_modeling|D3-AM: Access Modeling]]
- [[D3-CI-configuration_inventory|D3-CI: Configuration Inventory]]
- [[D3-NTPM-network_traffic_policy_mapping|D3-NTPM: Network Traffic Policy Mapping]]
- [[D3-RC-restore_configuration|D3-RC: Restore Configuration]]

## Subtechniques

### T1484.001: Group Policy Modification

^t1484001-group-policy-modification

Adversaries may modify Group Policy Objects (GPOs) to subvert the intended discretionary access controls for a domain, usually with the intention of escalating privileges on the domain. Group policy allows for centralized management of user and computer settings in Active Directory (AD). GPOs are containers for group policy settings made up of files stored within a predictable network path `\<DOMAIN>\SYSVOL\<DOMAIN>\Policies\`.(Citation: TechNet Group Policy Basics)(Citation: ADSecurity GPO Persistence 2016) 

Like other objects in AD, GPOs have access controls associated with them. By default all user accounts in the domain have permission to read GPOs. It is possible to delegate GPO access control permissions, e.g. write access, to specific users or groups in the domain.

Malicious GPO modifications can be used to implement many other malicious behaviors such as [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]], [[T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]], [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]], [[T1136-create_account|T1136: Create Account]], [[T1569-system_services#^t1569002-service-execution|T1569.002: Service Execution]],  and more.(Citation: ADSecurity GPO Persistence 2016)(Citation: Wald0 Guide to GPOs)(Citation: Harmj0y Abusing GPO Permissions)(Citation: Mandiant M Trends 2016)(Citation: Microsoft Hacking Team Breach) Since GPOs can control so many user and machine settings in the AD environment, there are a great number of potential attacks that can stem from this GPO abuse.(Citation: Wald0 Guide to GPOs)

For example, publicly available scripts such as `New-GPOImmediateTask` can be leveraged to automate the creation of a malicious [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]] by modifying GPO settings, in this case modifying `&lt;GPO_PATH&gt;\Machine\Preferences\ScheduledTasks\ScheduledTasks.xml`.(Citation: Wald0 Guide to GPOs)(Citation: Harmj0y Abusing GPO Permissions) In some cases an adversary might modify specific user rights like SeEnableDelegationPrivilege, set in `&lt;GPO_PATH&gt;\MACHINE\Microsoft\Windows NT\SecEdit\GptTmpl.inf`, to achieve a subtle AD backdoor with complete control of the domain because the user account under the adversary's control would then be able to modify GPOs.(Citation: Harmj0y SeEnableDelegationPrivilege Right)

### T1484.002: Trust Modification

^t1484002-trust-modification

Adversaries may add new domain trusts, modify the properties of existing domain trusts, or otherwise change the configuration of trust relationships between domains and tenants to evade defenses and/or elevate privileges.Trust details, such as whether or not user identities are federated, allow authentication and authorization properties to apply between domains or tenants for the purpose of accessing shared resources.(Citation: Microsoft - Azure AD Federation) These trust objects may include accounts, credentials, and other authentication material applied to servers, tokens, and domains.

Manipulating these trusts may allow an adversary to escalate privileges and/or evade defenses by modifying settings to add objects which they control. For example, in Microsoft Active Directory (AD) environments, this may be used to forge [[T1606-forge_web_credentials#^t1606002-saml-tokens|T1606.002: SAML Tokens]] without the need to compromise the signing certificate to forge new credentials. Instead, an adversary can manipulate domain trusts to add their own signing certificate. An adversary may also convert an AD domain to a federated domain using Active Directory Federation Services (AD FS), which may enable malicious trust modifications such as altering the claim issuance rules to log in any valid set of credentials as a specified user.(Citation: AADInternals zure AD Federated Domain) 

An adversary may also add a new federated identity provider to an identity tenant such as Okta or AWS IAM Identity Center, which may enable the adversary to authenticate as any user of the tenant.(Citation: Okta Cross-Tenant Impersonation 2023) This may enable the threat actor to gain broad access into a variety of cloud-based services that leverage the identity tenant. For example, in AWS environments, an adversary that creates a new identity provider for an AWS Organization will be able to federate into all of the AWS Organization member accounts without creating identities for each of the member accounts.(Citation: AWS RE:Inforce Threat Detection 2024)

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1047-audit|M1047: Audit]]

## Platforms

- Windows
- Identity Provider

