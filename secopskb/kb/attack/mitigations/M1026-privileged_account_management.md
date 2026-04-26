---
mitre_id: "M1026"
mitre_name: "Privileged Account Management"
mitre_type: "course-of-action"
mitre_stix_id: "course-of-action--9bb9e696-bff8-4ae1-9454-961fc7d91d5f"
mitre_created: "2019-06-06T21:09:47.115Z"
mitre_modified: "2024-12-18T18:44:23.306Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/mitigations/M1026/"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Privileged Account Management focuses on implementing policies, controls, and tools to securely manage privileged accounts (e.g., SYSTEM, root, or administrative accounts). This includes restricting access, limiting the scope of permissions, monitoring privileged account usage, and ensuring accountability through logging and auditing.This mitigation can be implemented through the following measures:

Account Permissions and Roles:

- Implement RBAC and least privilege principles to allocate permissions securely.
- Use tools like Active Directory Group Policies to enforce access restrictions.

Credential Security:

- Deploy password vaulting tools like CyberArk, HashiCorp Vault, or KeePass for secure storage and rotation of credentials.
- Enforce password policies for complexity, uniqueness, and expiration using tools like Microsoft Group Policy Objects (GPO).

Multi-Factor Authentication (MFA):

- Enforce MFA for all privileged accounts using Duo Security, Okta, or Microsoft Azure AD MFA.

Privileged Access Management (PAM):

- Use PAM solutions like CyberArk, BeyondTrust, or Thycotic to manage, monitor, and audit privileged access.

Auditing and Monitoring:

- Integrate activity monitoring into your SIEM (e.g., Splunk or QRadar) to detect and alert on anomalous privileged account usage.

Just-In-Time Access:

- Deploy JIT solutions like Azure Privileged Identity Management (PIM) or configure ephemeral roles in AWS and GCP to grant time-limited elevated permissions.

*Tools for Implementation*

Privileged Access Management (PAM):

- CyberArk, BeyondTrust, Thycotic, HashiCorp Vault.

Credential Management:

- Microsoft LAPS (Local Admin Password Solution), Password Safe, HashiCorp Vault, KeePass.

Multi-Factor Authentication:

- Duo Security, Okta, Microsoft Azure MFA, Google Authenticator.

Linux Privilege Management:

- sudo configuration, SELinux, AppArmor.

Just-In-Time Access:

- Azure Privileged Identity Management (PIM), AWS IAM Roles with session constraints, GCP Identity-Aware Proxy.

## Workspace

- [[workspaces/attack/mitigations/M1026-privileged_account_management-note|Open workspace note]]

![[workspaces/attack/mitigations/M1026-privileged_account_management-note]]

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
    - [[T1021-remote_services#^t1021001-remote-desktop-protocol|T1021.001: Remote Desktop Protocol]]
    - [[T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]]
    - [[T1021-remote_services#^t1021003-distributed-component-object-model|T1021.003: Distributed Component Object Model]]
    - [[T1021-remote_services#^t1021006-windows-remote-management|T1021.006: Windows Remote Management]]
    - [[T1021-remote_services#^t1021007-cloud-services|T1021.007: Cloud Services]]
- [[T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]]
- [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]]
- [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]]
    - [[T1053-scheduled_task_job#^t1053002-at|T1053.002: At]]
    - [[T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]
    - [[T1053-scheduled_task_job#^t1053006-systemd-timers|T1053.006: Systemd Timers]]
    - [[T1053-scheduled_task_job#^t1053007-container-orchestration-job|T1053.007: Container Orchestration Job]]
- [[T1055-process_injection|T1055: Process Injection]]
- [[T1055-process_injection|T1055: Process Injection]]
    - [[T1055-process_injection#^t1055008-ptrace-system-calls|T1055.008: Ptrace System Calls]]
- [[T1056-input_capture|T1056: Input Capture]]
    - [[T1056-input_capture#^t1056003-web-portal-capture|T1056.003: Web Portal Capture]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
    - [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]
    - [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]]
    - [[T1059-command_and_scripting_interpreter#^t1059009-cloud-api|T1059.009: Cloud API]]
    - [[T1059-command_and_scripting_interpreter#^t1059013-container-cli-api|T1059.013: Container CLI/API]]
- [[T1072-software_deployment_tools|T1072: Software Deployment Tools]]
- [[T1078-valid_accounts|T1078: Valid Accounts]]
- [[T1078-valid_accounts|T1078: Valid Accounts]]
    - [[T1078-valid_accounts#^t1078002-domain-accounts|T1078.002: Domain Accounts]]
    - [[T1078-valid_accounts#^t1078003-local-accounts|T1078.003: Local Accounts]]
    - [[T1078-valid_accounts#^t1078004-cloud-accounts|T1078.004: Cloud Accounts]]
- [[T1098-account_manipulation|T1098: Account Manipulation]]
- [[T1098-account_manipulation|T1098: Account Manipulation]]
    - [[T1098-account_manipulation#^t1098001-additional-cloud-credentials|T1098.001: Additional Cloud Credentials]]
    - [[T1098-account_manipulation#^t1098002-additional-email-delegate-permissions|T1098.002: Additional Email Delegate Permissions]]
    - [[T1098-account_manipulation#^t1098003-additional-cloud-roles|T1098.003: Additional Cloud Roles]]
- [[T1134-access_token_manipulation|T1134: Access Token Manipulation]]
- [[T1134-access_token_manipulation|T1134: Access Token Manipulation]]
    - [[T1134-access_token_manipulation#^t1134001-token-impersonation-theft|T1134.001: Token Impersonation/Theft]]
    - [[T1134-access_token_manipulation#^t1134002-create-process-with-token|T1134.002: Create Process with Token]]
    - [[T1134-access_token_manipulation#^t1134003-make-and-impersonate-token|T1134.003: Make and Impersonate Token]]
- [[T1136-create_account|T1136: Create Account]]
- [[T1136-create_account|T1136: Create Account]]
    - [[T1136-create_account#^t1136001-local-account|T1136.001: Local Account]]
    - [[T1136-create_account#^t1136002-domain-account|T1136.002: Domain Account]]
    - [[T1136-create_account#^t1136003-cloud-account|T1136.003: Cloud Account]]
- [[T1190-exploit_public-facing_application|T1190: Exploit Public-Facing Application]]
- [[T1210-exploitation_of_remote_services|T1210: Exploitation of Remote Services]]
- [[T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]
- [[T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]
    - [[T1218-system_binary_proxy_execution#^t1218007-msiexec|T1218.007: Msiexec]]
- [[T1222-file_and_directory_permissions_modification|T1222: File and Directory Permissions Modification]]
- [[T1222-file_and_directory_permissions_modification|T1222: File and Directory Permissions Modification]]
    - [[T1222-file_and_directory_permissions_modification#^t1222001-windows-file-and-directory-permissions-modification|T1222.001: Windows File and Directory Permissions Modification]]
    - [[T1222-file_and_directory_permissions_modification#^t1222002-linux-and-mac-file-and-directory-permissions-modification|T1222.002: Linux and Mac File and Directory Permissions Modification]]
- [[T1484-domain_or_tenant_policy_modification|T1484: Domain or Tenant Policy Modification]]
- [[T1484-domain_or_tenant_policy_modification|T1484: Domain or Tenant Policy Modification]]
    - [[T1484-domain_or_tenant_policy_modification#^t1484002-trust-modification|T1484.002: Trust Modification]]
- [[T1495-firmware_corruption|T1495: Firmware Corruption]]
- [[T1505-server_software_component|T1505: Server Software Component]]
- [[T1505-server_software_component|T1505: Server Software Component]]
    - [[T1505-server_software_component#^t1505001-sql-stored-procedures|T1505.001: SQL Stored Procedures]]
    - [[T1505-server_software_component#^t1505002-transport-agent|T1505.002: Transport Agent]]
    - [[T1505-server_software_component#^t1505004-iis-components|T1505.004: IIS Components]]
- [[T1525-implant_internal_image|T1525: Implant Internal Image]]
- [[T1542-pre-os_boot|T1542: Pre-OS Boot]]
- [[T1542-pre-os_boot|T1542: Pre-OS Boot]]
    - [[T1542-pre-os_boot#^t1542001-system-firmware|T1542.001: System Firmware]]
    - [[T1542-pre-os_boot#^t1542003-bootkit|T1542.003: Bootkit]]
    - [[T1542-pre-os_boot#^t1542005-tftp-boot|T1542.005: TFTP Boot]]
- [[T1543-create_or_modify_system_process|T1543: Create or Modify System Process]]
- [[T1543-create_or_modify_system_process|T1543: Create or Modify System Process]]
    - [[T1543-create_or_modify_system_process#^t1543002-systemd-service|T1543.002: Systemd Service]]
- [[T1546-event_triggered_execution|T1546: Event Triggered Execution]]
- [[T1546-event_triggered_execution|T1546: Event Triggered Execution]]
    - [[T1546-event_triggered_execution#^t1546003-windows-management-instrumentation-event-subscription|T1546.003: Windows Management Instrumentation Event Subscription]]
- [[T1547-boot_or_logon_autostart_execution|T1547: Boot or Logon Autostart Execution]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547006-kernel-modules-and-extensions|T1547.006: Kernel Modules and Extensions]]
- [[T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]
- [[T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]
    - [[T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]
    - [[T1548-abuse_elevation_control_mechanism#^t1548003-sudo-and-sudo-caching|T1548.003: Sudo and Sudo Caching]]
    - [[T1548-abuse_elevation_control_mechanism#^t1548006-tcc-manipulation|T1548.006: TCC Manipulation]]
- [[T1550-use_alternate_authentication_material|T1550: Use Alternate Authentication Material]]
- [[T1550-use_alternate_authentication_material|T1550: Use Alternate Authentication Material]]
    - [[T1550-use_alternate_authentication_material#^t1550002-pass-the-hash|T1550.002: Pass the Hash]]
    - [[T1550-use_alternate_authentication_material#^t1550003-pass-the-ticket|T1550.003: Pass the Ticket]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
    - [[T1552-unsecured_credentials#^t1552002-credentials-in-registry|T1552.002: Credentials in Registry]]
    - [[T1552-unsecured_credentials#^t1552007-container-api|T1552.007: Container API]]
- [[T1553-subvert_trust_controls|T1553: Subvert Trust Controls]]
- [[T1553-subvert_trust_controls|T1553: Subvert Trust Controls]]
    - [[T1553-subvert_trust_controls#^t1553006-code-signing-policy-modification|T1553.006: Code Signing Policy Modification]]
- [[T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]
- [[T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]
    - [[T1555-credentials_from_password_stores#^t1555006-cloud-secrets-management-stores|T1555.006: Cloud Secrets Management Stores]]
- [[T1556-modify_authentication_process|T1556: Modify Authentication Process]]
- [[T1556-modify_authentication_process|T1556: Modify Authentication Process]]
    - [[T1556-modify_authentication_process#^t1556001-domain-controller-authentication|T1556.001: Domain Controller Authentication]]
    - [[T1556-modify_authentication_process#^t1556003-pluggable-authentication-modules|T1556.003: Pluggable Authentication Modules]]
    - [[T1556-modify_authentication_process#^t1556004-network-device-authentication|T1556.004: Network Device Authentication]]
    - [[T1556-modify_authentication_process#^t1556005-reversible-encryption|T1556.005: Reversible Encryption]]
    - [[T1556-modify_authentication_process#^t1556007-hybrid-identity|T1556.007: Hybrid Identity]]
- [[T1558-steal_or_forge_kerberos_tickets|T1558: Steal or Forge Kerberos Tickets]]
- [[T1558-steal_or_forge_kerberos_tickets|T1558: Steal or Forge Kerberos Tickets]]
    - [[T1558-steal_or_forge_kerberos_tickets#^t1558001-golden-ticket|T1558.001: Golden Ticket]]
    - [[T1558-steal_or_forge_kerberos_tickets#^t1558002-silver-ticket|T1558.002: Silver Ticket]]
    - [[T1558-steal_or_forge_kerberos_tickets#^t1558003-kerberoasting|T1558.003: Kerberoasting]]
- [[T1559-inter-process_communication|T1559: Inter-Process Communication]]
- [[T1559-inter-process_communication|T1559: Inter-Process Communication]]
    - [[T1559-inter-process_communication#^t1559001-component-object-model|T1559.001: Component Object Model]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
    - [[T1562-impair_defenses#^t1562009-safe-mode-boot|T1562.009: Safe Mode Boot]]
- [[T1563-remote_service_session_hijacking|T1563: Remote Service Session Hijacking]]
- [[T1563-remote_service_session_hijacking|T1563: Remote Service Session Hijacking]]
    - [[T1563-remote_service_session_hijacking#^t1563001-ssh-hijacking|T1563.001: SSH Hijacking]]
    - [[T1563-remote_service_session_hijacking#^t1563002-rdp-hijacking|T1563.002: RDP Hijacking]]
- [[T1569-system_services|T1569: System Services]]
- [[T1569-system_services|T1569: System Services]]
    - [[T1569-system_services#^t1569002-service-execution|T1569.002: Service Execution]]
- [[T1599-network_boundary_bridging|T1599: Network Boundary Bridging]]
- [[T1599-network_boundary_bridging|T1599: Network Boundary Bridging]]
    - [[T1599-network_boundary_bridging#^t1599001-network-address-translation-traversal|T1599.001: Network Address Translation Traversal]]
- [[T1601-modify_system_image|T1601: Modify System Image]]
- [[T1601-modify_system_image|T1601: Modify System Image]]
    - [[T1601-modify_system_image#^t1601001-patch-system-image|T1601.001: Patch System Image]]
    - [[T1601-modify_system_image#^t1601002-downgrade-system-image|T1601.002: Downgrade System Image]]
- [[T1606-forge_web_credentials|T1606: Forge Web Credentials]]
- [[T1606-forge_web_credentials|T1606: Forge Web Credentials]]
    - [[T1606-forge_web_credentials#^t1606002-saml-tokens|T1606.002: SAML Tokens]]
- [[T1609-container_administration_command|T1609: Container Administration Command]]
- [[T1611-escape_to_host|T1611: Escape to Host]]
- [[T1612-build_image_on_host|T1612: Build Image on Host]]
- [[T1651-cloud_administration_command|T1651: Cloud Administration Command]]

