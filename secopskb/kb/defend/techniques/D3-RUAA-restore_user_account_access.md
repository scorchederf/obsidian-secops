---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-RUAA"
d3fend_name: "Restore User Account Access"
d3fend_ontology_id: "d3f:RestoreUserAccountAccess"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ARestoreUserAccountAccess/"
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
  - "T1136"
  - "T1136.001"
  - "T1136.002"
  - "T1136.003"
  - "T1531"
  - "T1548"
  - "T1548.005"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Restoring a user account's access to resources.

## Workspace

- [[workspaces/defend/techniques/D3-RUAA-restore_user_account_access-note|Open workspace note]]

![[workspaces/defend/techniques/D3-RUAA-restore_user_account_access-note]]

## Parent Technique

- [[D3-RA-restore_access|D3-RA: Restore Access]]

## Child Techniques

- [[D3-ULA-unlock_account|D3-ULA: Unlock Account]]

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
- [[T1136-create_account|T1136: Create Account]]
- [[T1136-create_account#^t1136001-local-account|T1136.001: Local Account]]
- [[T1136-create_account#^t1136002-domain-account|T1136.002: Domain Account]]
- [[T1136-create_account#^t1136003-cloud-account|T1136.003: Cloud Account]]
- [[T1531-account_access_removal|T1531: Account Access Removal]]
- [[T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]
- [[T1548-abuse_elevation_control_mechanism#^t1548005-temporary-elevated-cloud-access|T1548.005: Temporary Elevated Cloud Access]]

## Ontology Relationships

- [[D3-RA-restore_access|D3-RA: Restore Access]]

