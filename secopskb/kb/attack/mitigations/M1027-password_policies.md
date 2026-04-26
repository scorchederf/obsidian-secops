---
mitre_id: "M1027"
mitre_name: "Password Policies"
mitre_type: "course-of-action"
mitre_stix_id: "course-of-action--90c218c3-fbf8-4830-98a7-e8cfb7eaa485"
mitre_created: "2019-06-06T21:10:35.792Z"
mitre_modified: "2024-12-18T18:08:17.479Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/mitigations/M1027/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "mitigation"
tags:
  - "attack"
  - "mitigation"
  - "defense"
  - "countermeasure"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Set and enforce secure password policies for accounts to reduce the likelihood of unauthorized access. Strong password policies include enforcing password complexity, requiring regular password changes, and preventing password reuse. This mitigation can be implemented through the following measures:

Windows Systems:

- Use Group Policy Management Console (GPMC) to configure:
    - Minimum password length (e.g., 12+ characters).
    - Password complexity requirements.
    - Password history (e.g., disallow last 24 passwords).
    - Account lockout duration and thresholds.

Linux Systems:

- Configure Pluggable Authentication Modules (PAM):
- Use `pam_pwquality` to enforce complexity and length requirements.
- Implement `pam_tally2` or `pam_faillock` for account lockouts.
- Use `pwunconv` to disable password reuse.

Password Managers:

- Enforce usage of enterprise password managers (e.g., Bitwarden, 1Password, LastPass) to generate and store strong passwords.

Password Blacklisting:

- Use tools like Have I Been Pwned password checks or NIST-based blacklist solutions to prevent users from setting compromised passwords.

Regular Auditing:

- Periodically audit password policies and account configurations to ensure compliance using tools like LAPS (Local Admin Password Solution) and vulnerability scanners.

*Tools for Implementation*

Windows:

- Group Policy Management Console (GPMC): Enforce password policies.
- Microsoft Local Administrator Password Solution (LAPS): Enforce random, unique admin passwords.

Linux/macOS:

- PAM Modules (pam_pwquality, pam_tally2, pam_faillock): Enforce password rules.
- Lynis: Audit password policies and system configurations.

Cross-Platform:

- Password Managers (Bitwarden, 1Password, KeePass): Manage and enforce strong passwords.
- Have I Been Pwned API: Prevent the use of breached passwords.
- NIST SP 800-63B compliant tools: Enforce password guidelines and blacklisting.

## Workspace

- [[workspaces/attack/mitigations/M1027-password_policies-note|Open workspace note]]

![[workspaces/attack/mitigations/M1027-password_policies-note]]

## Mitigates Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
    - [[T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]
    - [[T1003-os_credential_dumping#^t1003002-security-account-manager|T1003.002: Security Account Manager]]
    - [[T1003-os_credential_dumping#^t1003003-ntds|T1003.003: NTDS]]
    - [[T1003-os_credential_dumping#^t1003004-lsa-secrets|T1003.004: LSA Secrets]]
    - [[T1003-os_credential_dumping#^t1003005-cached-domain-credentials|T1003.005: Cached Domain Credentials]]
    - [[T1003-os_credential_dumping#^t1003006-dcsync|T1003.006: DCSync]]
    - [[T1003-os_credential_dumping#^t1003007-proc-filesystem|T1003.007: Proc Filesystem]]
    - [[T1003-os_credential_dumping#^t1003008--etc-passwd-and--etc-shadow|T1003.008: /etc/passwd and /etc/shadow]]
- [[T1021-remote_services|T1021: Remote Services]]
- [[T1021-remote_services|T1021: Remote Services]]
    - [[T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]]
- [[T1072-software_deployment_tools|T1072: Software Deployment Tools]]
- [[T1078-valid_accounts|T1078: Valid Accounts]]
- [[T1078-valid_accounts|T1078: Valid Accounts]]
    - [[T1078-valid_accounts#^t1078001-default-accounts|T1078.001: Default Accounts]]
    - [[T1078-valid_accounts#^t1078002-domain-accounts|T1078.002: Domain Accounts]]
    - [[T1078-valid_accounts#^t1078003-local-accounts|T1078.003: Local Accounts]]
    - [[T1078-valid_accounts#^t1078004-cloud-accounts|T1078.004: Cloud Accounts]]
- [[T1110-brute_force|T1110: Brute Force]]
- [[T1110-brute_force|T1110: Brute Force]]
    - [[T1110-brute_force#^t1110001-password-guessing|T1110.001: Password Guessing]]
    - [[T1110-brute_force#^t1110002-password-cracking|T1110.002: Password Cracking]]
    - [[T1110-brute_force#^t1110003-password-spraying|T1110.003: Password Spraying]]
    - [[T1110-brute_force#^t1110004-credential-stuffing|T1110.004: Credential Stuffing]]
- [[T1187-forced_authentication|T1187: Forced Authentication]]
- [[T1201-password_policy_discovery|T1201: Password Policy Discovery]]
- [[T1550-use_alternate_authentication_material|T1550: Use Alternate Authentication Material]]
- [[T1550-use_alternate_authentication_material|T1550: Use Alternate Authentication Material]]
    - [[T1550-use_alternate_authentication_material#^t1550003-pass-the-ticket|T1550.003: Pass the Ticket]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
    - [[T1552-unsecured_credentials#^t1552001-credentials-in-files|T1552.001: Credentials In Files]]
    - [[T1552-unsecured_credentials#^t1552002-credentials-in-registry|T1552.002: Credentials in Registry]]
    - [[T1552-unsecured_credentials#^t1552004-private-keys|T1552.004: Private Keys]]
- [[T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]
- [[T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]
    - [[T1555-credentials_from_password_stores#^t1555001-keychain|T1555.001: Keychain]]
    - [[T1555-credentials_from_password_stores#^t1555003-credentials-from-web-browsers|T1555.003: Credentials from Web Browsers]]
    - [[T1555-credentials_from_password_stores#^t1555005-password-managers|T1555.005: Password Managers]]
- [[T1556-modify_authentication_process|T1556: Modify Authentication Process]]
- [[T1556-modify_authentication_process|T1556: Modify Authentication Process]]
    - [[T1556-modify_authentication_process#^t1556005-reversible-encryption|T1556.005: Reversible Encryption]]
- [[T1558-steal_or_forge_kerberos_tickets|T1558: Steal or Forge Kerberos Tickets]]
- [[T1558-steal_or_forge_kerberos_tickets|T1558: Steal or Forge Kerberos Tickets]]
    - [[T1558-steal_or_forge_kerberos_tickets#^t1558002-silver-ticket|T1558.002: Silver Ticket]]
    - [[T1558-steal_or_forge_kerberos_tickets#^t1558003-kerberoasting|T1558.003: Kerberoasting]]
    - [[T1558-steal_or_forge_kerberos_tickets#^t1558004-as-rep-roasting|T1558.004: AS-REP Roasting]]
- [[T1563-remote_service_session_hijacking|T1563: Remote Service Session Hijacking]]
- [[T1563-remote_service_session_hijacking|T1563: Remote Service Session Hijacking]]
    - [[T1563-remote_service_session_hijacking#^t1563001-ssh-hijacking|T1563.001: SSH Hijacking]]
- [[T1599-network_boundary_bridging|T1599: Network Boundary Bridging]]
- [[T1599-network_boundary_bridging|T1599: Network Boundary Bridging]]
    - [[T1599-network_boundary_bridging#^t1599001-network-address-translation-traversal|T1599.001: Network Address Translation Traversal]]
- [[T1601-modify_system_image|T1601: Modify System Image]]
- [[T1601-modify_system_image|T1601: Modify System Image]]
    - [[T1601-modify_system_image#^t1601001-patch-system-image|T1601.001: Patch System Image]]
    - [[T1601-modify_system_image#^t1601002-downgrade-system-image|T1601.002: Downgrade System Image]]

