---
id: M1015
name: Active Directory Configuration
created: 2019-06-06 16:39:58.291000+00:00
modified: 2024-12-10 15:57:59.336000+00:00
type: course-of-action
---

# Active Directory Configuration

Implement robust Active Directory (AD) configurations using group policies to secure user accounts, control access, and minimize the attack surface. AD configurations enable centralized control over account settings, logon policies, and permissions, reducing the risk of unauthorized access and lateral movement within the network. This mitigation can be implemented through the following measures:

Account Configuration:

- Implementation: Use domain accounts instead of local accounts to leverage AD’s centralized management, including group policies, auditing, and access control.
- Use Case: For IT staff managing shared resources, provision domain accounts that allow IT teams to log in centrally, reducing the risk of unmanaged, rogue local accounts on individual machines.

Interactive Logon Restrictions:

- Implementation: Configure group policies to restrict interactive logons (e.g., direct physical or RDP logons) for service accounts or privileged accounts that do not require such access.
- Use Case: Prevent service accounts, such as SQL Server accounts, from having interactive logon privileges. This reduces the risk of these accounts being leveraged for lateral movement if compromised.

Remote Desktop Settings:

- Implementation: Limit Remote Desktop Protocol (RDP) access to specific, authorized accounts. Use group policies to enforce this, allowing only necessary users to establish RDP sessions.
- Use Case: On sensitive servers (e.g., domain controllers or financial databases), restrict RDP access to administrative accounts only, while all other users are denied access.

Dedicated Administrative Accounts:

- Implementation: Create domain-wide administrative accounts that are restricted from interactive logons, designed solely for high-level tasks (e.g., software installation, patching).
- Use Case: Create separate administrative accounts for different purposes, such as one set of accounts for installations and another for managing repository access. This limits exposure and helps reduce attack vectors.

Authentication Silos:

- Implementation: Configure Authentication Silos in AD, using group policies to create access zones with restrictions based on membership, such as the Protected Users security group. This restricts access to critical accounts and minimizes exposure to potential threats.
- Use Case: Place high-risk or high-value accounts, such as executive or administrative accounts, in an Authentication Silo with extra controls, limiting their exposure to only necessary systems. This reduces the risk of credential misuse or abuse if these accounts are compromised.

**Tools for Implementation**:

- Active Directory Group Policies: Use Group Policy Management Console (GPMC) to configure, deploy, and enforce policies across AD environments.
- PowerShell: Automate account configuration, logon restrictions, and policy application using PowerShell scripts.
- AD Administrative Center: Manage Authentication Silos and configure high-level policies for critical user groups within AD.

## Mitigates Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
    - [[T1003-os_credential_dumping#^t1003005-cached-domain-credentials|T1003.005: Cached Domain Credentials]]
    - [[T1003-os_credential_dumping#^t1003006-dcsync|T1003.006: DCSync]]
- [[T1072-software_deployment_tools|T1072: Software Deployment Tools]]
- [[T1078-valid_accounts|T1078: Valid Accounts]]
    - [[T1078-valid_accounts#^t1078004-cloud-accounts|T1078.004: Cloud Accounts]]
- [[T1134-access_token_manipulation|T1134: Access Token Manipulation]]
    - [[T1134-access_token_manipulation#^t1134005-sid-history-injection|T1134.005: SID-History Injection]]
- [[T1550-use_alternate_authentication_material|T1550: Use Alternate Authentication Material]]
    - [[T1550-use_alternate_authentication_material#^t1550003-pass-the-ticket|T1550.003: Pass the Ticket]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
    - [[T1552-unsecured_credentials#^t1552006-group-policy-preferences|T1552.006: Group Policy Preferences]]
- [[T1558-steal_or_forge_kerberos_tickets|T1558: Steal or Forge Kerberos Tickets]]
    - [[T1558-steal_or_forge_kerberos_tickets#^t1558001-golden-ticket|T1558.001: Golden Ticket]]
- [[T1606-forge_web_credentials|T1606: Forge Web Credentials]]
    - [[T1606-forge_web_credentials#^t1606002-saml-tokens|T1606.002: SAML Tokens]]
- [[T1649-steal_or_forge_authentication_certificates|T1649: Steal or Forge Authentication Certificates]]

