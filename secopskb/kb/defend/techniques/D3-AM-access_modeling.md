---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-AM"
d3fend_name: "Access Modeling"
d3fend_ontology_id: "d3f:AccessModeling"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AAccessModeling/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1078"
  - "T1078.001"
  - "T1078.002"
  - "T1078.003"
  - "T1078.004"
  - "T1087"
  - "T1087.001"
  - "T1087.002"
  - "T1087.004"
  - "T1098"
  - "T1098.001"
  - "T1098.002"
  - "T1098.003"
  - "T1098.004"
  - "T1098.005"
  - "T1098.006"
  - "T1098.007"
  - "T1134"
  - "T1134.005"
  - "T1136"
  - "T1136.001"
  - "T1136.002"
  - "T1136.003"
  - "T1222"
  - "T1222.001"
  - "T1222.002"
  - "T1484"
  - "T1484.001"
  - "T1484.002"
  - "T1531"
  - "T1548"
  - "T1548.001"
  - "T1548.005"
  - "T1552"
  - "T1552.006"
  - "T1556"
  - "T1556.009"
  - "T1615"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Access modeling captures and records the access permissions granted to identities (e.g., administrators, users, groups, systems) and optionally includes details on how these identities are stored, managed, and shared across systems.

## Workspace

- [[workspaces/defend/techniques/D3-AM-access_modeling-note|Open workspace note]]

![[workspaces/defend/techniques/D3-AM-access_modeling-note]]

## Parent Technique

- [[D3-OAM-operational_activity_mapping|D3-OAM: Operational Activity Mapping]]

## Related ATT&CK Techniques

- [[T1078-valid_accounts|T1078: Valid Accounts]]
- [[T1078-valid_accounts#^t1078001-default-accounts|T1078.001: Default Accounts]]
- [[T1078-valid_accounts#^t1078002-domain-accounts|T1078.002: Domain Accounts]]
- [[T1078-valid_accounts#^t1078003-local-accounts|T1078.003: Local Accounts]]
- [[T1078-valid_accounts#^t1078004-cloud-accounts|T1078.004: Cloud Accounts]]
- [[T1087-account_discovery|T1087: Account Discovery]]
- [[T1087-account_discovery#^t1087001-local-account|T1087.001: Local Account]]
- [[T1087-account_discovery#^t1087002-domain-account|T1087.002: Domain Account]]
- [[T1087-account_discovery#^t1087004-cloud-account|T1087.004: Cloud Account]]
- [[T1098-account_manipulation|T1098: Account Manipulation]]
- [[T1098-account_manipulation#^t1098001-additional-cloud-credentials|T1098.001: Additional Cloud Credentials]]
- [[T1098-account_manipulation#^t1098002-additional-email-delegate-permissions|T1098.002: Additional Email Delegate Permissions]]
- [[T1098-account_manipulation#^t1098003-additional-cloud-roles|T1098.003: Additional Cloud Roles]]
- [[T1098-account_manipulation#^t1098004-ssh-authorized-keys|T1098.004: SSH Authorized Keys]]
- [[T1098-account_manipulation#^t1098005-device-registration|T1098.005: Device Registration]]
- [[T1098-account_manipulation#^t1098006-additional-container-cluster-roles|T1098.006: Additional Container Cluster Roles]]
- [[T1098-account_manipulation#^t1098007-additional-local-or-domain-groups|T1098.007: Additional Local or Domain Groups]]
- [[T1134-access_token_manipulation|T1134: Access Token Manipulation]]
- [[T1134-access_token_manipulation#^t1134005-sid-history-injection|T1134.005: SID-History Injection]]
- [[T1136-create_account|T1136: Create Account]]
- [[T1136-create_account#^t1136001-local-account|T1136.001: Local Account]]
- [[T1136-create_account#^t1136002-domain-account|T1136.002: Domain Account]]
- [[T1136-create_account#^t1136003-cloud-account|T1136.003: Cloud Account]]
- [[T1222-file_and_directory_permissions_modification|T1222: File and Directory Permissions Modification]]
- [[T1222-file_and_directory_permissions_modification#^t1222001-windows-file-and-directory-permissions-modification|T1222.001: Windows File and Directory Permissions Modification]]
- [[T1222-file_and_directory_permissions_modification#^t1222002-linux-and-mac-file-and-directory-permissions-modification|T1222.002: Linux and Mac File and Directory Permissions Modification]]
- [[T1484-domain_or_tenant_policy_modification|T1484: Domain or Tenant Policy Modification]]
- [[T1484-domain_or_tenant_policy_modification#^t1484001-group-policy-modification|T1484.001: Group Policy Modification]]
- [[T1484-domain_or_tenant_policy_modification#^t1484002-trust-modification|T1484.002: Trust Modification]]
- [[T1531-account_access_removal|T1531: Account Access Removal]]
- [[T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]
- [[T1548-abuse_elevation_control_mechanism#^t1548001-setuid-and-setgid|T1548.001: Setuid and Setgid]]
- [[T1548-abuse_elevation_control_mechanism#^t1548005-temporary-elevated-cloud-access|T1548.005: Temporary Elevated Cloud Access]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
- [[T1552-unsecured_credentials#^t1552006-group-policy-preferences|T1552.006: Group Policy Preferences]]
- [[T1556-modify_authentication_process|T1556: Modify Authentication Process]]
- [[T1556-modify_authentication_process#^t1556009-conditional-access-policies|T1556.009: Conditional Access Policies]]
- [[T1615-group_policy_discovery|T1615: Group Policy Discovery]]

## Ontology Relationships

- [[D3-OAM-operational_activity_mapping|D3-OAM: Operational Activity Mapping]]

