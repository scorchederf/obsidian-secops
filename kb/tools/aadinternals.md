---
id: S0677
name: AADInternals
created: 2022-02-01 15:08:45.007000+00:00
modified: 2025-04-16 20:38:50.579000+00:00
type: tool
x_mitre_version: 1.2
x_mitre_domains: enterprise-attack
---

# AADInternals

[AADInternals](https://attack.mitre.org/software/S0677) is a PowerShell-based framework for administering, enumerating, and exploiting Azure Active Directory. The tool is publicly available on GitHub.(Citation: AADInternals Github)(Citation: AADInternals Documentation)

## Uses Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
    - [[T1003-os_credential_dumping#^t1003004-lsa-secrets|T1003.004: LSA Secrets]]
- [[T1048-exfiltration_over_alternative_protocol|T1048: Exfiltration Over Alternative Protocol]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
    - [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]
- [[T1069-permission_groups_discovery|T1069: Permission Groups Discovery]]
    - [[T1069-permission_groups_discovery#^t1069003-cloud-groups|T1069.003: Cloud Groups]]
- [[T1087-account_discovery|T1087: Account Discovery]]
    - [[T1087-account_discovery#^t1087004-cloud-account|T1087.004: Cloud Account]]
- [[T1098-account_manipulation|T1098: Account Manipulation]]
    - [[T1098-account_manipulation#^t1098005-device-registration|T1098.005: Device Registration]]
- [[T1112-modify_registry|T1112: Modify Registry]]
- [[T1136-create_account|T1136: Create Account]]
    - [[T1136-create_account#^t1136003-cloud-account|T1136.003: Cloud Account]]
- [[T1484-domain_or_tenant_policy_modification|T1484: Domain or Tenant Policy Modification]]
    - [[T1484-domain_or_tenant_policy_modification#^t1484002-trust-modification|T1484.002: Trust Modification]]
- [[T1526-cloud_service_discovery|T1526: Cloud Service Discovery]]
- [[T1528-steal_application_access_token|T1528: Steal Application Access Token]]
- [[T1530-data_from_cloud_storage|T1530: Data from Cloud Storage]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
    - [[T1552-unsecured_credentials#^t1552001-credentials-in-files|T1552.001: Credentials In Files]]
    - [[T1552-unsecured_credentials#^t1552004-private-keys|T1552.004: Private Keys]]
- [[T1556-modify_authentication_process|T1556: Modify Authentication Process]]
    - [[T1556-modify_authentication_process#^t1556006-multi-factor-authentication|T1556.006: Multi-Factor Authentication]]
    - [[T1556-modify_authentication_process#^t1556007-hybrid-identity|T1556.007: Hybrid Identity]]
- [[T1558-steal_or_forge_kerberos_tickets|T1558: Steal or Forge Kerberos Tickets]]
    - [[T1558-steal_or_forge_kerberos_tickets#^t1558002-silver-ticket|T1558.002: Silver Ticket]]
- [[T1566-phishing|T1566: Phishing]]
    - [[T1566-phishing#^t1566002-spearphishing-link|T1566.002: Spearphishing Link]]
- [[T1589-gather_victim_identity_information|T1589: Gather Victim Identity Information]]
    - [[T1589-gather_victim_identity_information#^t1589002-email-addresses|T1589.002: Email Addresses]]
- [[T1590-gather_victim_network_information|T1590: Gather Victim Network Information]]
    - [[T1590-gather_victim_network_information#^t1590001-domain-properties|T1590.001: Domain Properties]]
- [[T1598-phishing_for_information|T1598: Phishing for Information]]
    - [[T1598-phishing_for_information#^t1598003-spearphishing-link|T1598.003: Spearphishing Link]]
- [[T1606-forge_web_credentials|T1606: Forge Web Credentials]]
    - [[T1606-forge_web_credentials#^t1606002-saml-tokens|T1606.002: SAML Tokens]]
- [[T1649-steal_or_forge_authentication_certificates|T1649: Steal or Forge Authentication Certificates]]
- [[T1651-cloud_administration_command|T1651: Cloud Administration Command]]

