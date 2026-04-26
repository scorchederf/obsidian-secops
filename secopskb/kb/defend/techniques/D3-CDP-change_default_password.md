---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-CDP"
d3fend_name: "Change Default Password"
d3fend_ontology_id: "d3f:ChangeDefaultPassword"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AChangeDefaultPassword/"
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
  - "T1110"
  - "T1110.001"
  - "T1110.002"
  - "T1110.003"
  - "T1136"
  - "T1136.001"
  - "T1136.002"
  - "T1136.003"
  - "T1531"
  - "T1548"
  - "T1548.005"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

Changing the default password means replacing the factory-set credentials with a strong, unique password before the device is deployed, preventing unauthorized access.

## Workspace

- [[workspaces/defend/techniques/D3-CDP-change_default_password-note|Open workspace note]]

![[workspaces/defend/techniques/D3-CDP-change_default_password-note]]

## Parent Technique

- [[D3-SPP-strong_password_policy|D3-SPP: Strong Password Policy]]

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
- [[T1110-brute_force|T1110: Brute Force]]
- [[T1110-brute_force#^t1110001-password-guessing|T1110.001: Password Guessing]]
- [[T1110-brute_force#^t1110002-password-cracking|T1110.002: Password Cracking]]
- [[T1110-brute_force#^t1110003-password-spraying|T1110.003: Password Spraying]]
- [[T1136-create_account|T1136: Create Account]]
- [[T1136-create_account#^t1136001-local-account|T1136.001: Local Account]]
- [[T1136-create_account#^t1136002-domain-account|T1136.002: Domain Account]]
- [[T1136-create_account#^t1136003-cloud-account|T1136.003: Cloud Account]]
- [[T1531-account_access_removal|T1531: Account Access Removal]]
- [[T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]
- [[T1548-abuse_elevation_control_mechanism#^t1548005-temporary-elevated-cloud-access|T1548.005: Temporary Elevated Cloud Access]]

## Knowledge Base Article

## How it works
Change the default password as soon as a new device is received. The default credentials are normally documented in an instruction manual that is either packaged with the device, published online through official means, or published online through unofficial means.

## Considerations
* These should be changed before a device is brought online so that an adversary cannot take advantage of these default credentials.
* Strong and complex passwords are preferred if the technology allows.

## Ontology Relationships

- [[D3-SPP-strong_password_policy|D3-SPP: Strong Password Policy]]

