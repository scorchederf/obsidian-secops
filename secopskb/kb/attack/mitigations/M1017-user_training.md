---
mitre_id: "M1017"
mitre_name: "User Training"
mitre_type: "course-of-action"
mitre_stix_id: "course-of-action--2a4f6c11-a4a7-4cb9-b0ef-6ae1bb3a718a"
mitre_created: "2019-06-06T16:50:04.963Z"
mitre_modified: "2024-12-24T14:36:46.335Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/mitigations/M1017/"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

User Training involves educating employees and contractors on recognizing, reporting, and preventing cyber threats that rely on human interaction, such as phishing, social engineering, and other manipulative techniques. Comprehensive training programs create a human firewall by empowering users to be an active component of the organization's cybersecurity defenses. This mitigation can be implemented through the following measures:

Create Comprehensive Training Programs:

- Design training modules tailored to the organization's risk profile, covering topics such as phishing, password management, and incident reporting.
- Provide role-specific training for high-risk employees, such as helpdesk staff or executives.

Use Simulated Exercises:

- Conduct phishing simulations to measure user susceptibility and provide targeted follow-up training.
- Run social engineering drills to evaluate employee responses and reinforce protocols.

Leverage Gamification and Engagement:

- Introduce interactive learning methods such as quizzes, gamified challenges, and rewards for successful detection and reporting of threats.

Incorporate Security Policies into Onboarding:

- Include cybersecurity training as part of the onboarding process for new employees.
- Provide easy-to-understand materials outlining acceptable use policies and reporting procedures.

Regular Refresher Courses:

- Update training materials to include emerging threats and techniques used by adversaries.
- Ensure all employees complete periodic refresher courses to stay informed.

Emphasize Real-World Scenarios:

- Use case studies of recent attacks to demonstrate the consequences of successful phishing or social engineering.
- Discuss how specific employee actions can prevent or mitigate such attacks.

## Workspace

- [[workspaces/attack/mitigations/M1017-user_training-note|Open workspace note]]

![[workspaces/attack/mitigations/M1017-user_training-note]]

## Mitigates Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
    - [[T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]
    - [[T1003-os_credential_dumping#^t1003002-security-account-manager|T1003.002: Security Account Manager]]
    - [[T1003-os_credential_dumping#^t1003003-ntds|T1003.003: NTDS]]
    - [[T1003-os_credential_dumping#^t1003004-lsa-secrets|T1003.004: LSA Secrets]]
    - [[T1003-os_credential_dumping#^t1003005-cached-domain-credentials|T1003.005: Cached Domain Credentials]]
- [[T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]]
- [[T1036-masquerading|T1036: Masquerading]]
- [[T1036-masquerading|T1036: Masquerading]]
    - [[T1036-masquerading#^t1036007-double-file-extension|T1036.007: Double File Extension]]
- [[T1056-input_capture|T1056: Input Capture]]
    - [[T1056-input_capture#^t1056002-gui-input-capture|T1056.002: GUI Input Capture]]
- [[T1072-software_deployment_tools|T1072: Software Deployment Tools]]
- [[T1078-valid_accounts|T1078: Valid Accounts]]
- [[T1078-valid_accounts|T1078: Valid Accounts]]
    - [[T1078-valid_accounts#^t1078002-domain-accounts|T1078.002: Domain Accounts]]
    - [[T1078-valid_accounts#^t1078004-cloud-accounts|T1078.004: Cloud Accounts]]
- [[T1111-multi-factor_authentication_interception|T1111: Multi-Factor Authentication Interception]]
- [[T1176-software_extensions|T1176: Software Extensions]]
- [[T1176-software_extensions|T1176: Software Extensions]]
    - [[T1176-software_extensions#^t1176001-browser-extensions|T1176.001: Browser Extensions]]
    - [[T1176-software_extensions#^t1176002-ide-extensions|T1176.002: IDE Extensions]]
- [[T1185-browser_session_hijacking|T1185: Browser Session Hijacking]]
- [[T1189-drive-by_compromise|T1189: Drive-by Compromise]]
- [[T1204-user_execution|T1204: User Execution]]
- [[T1204-user_execution|T1204: User Execution]]
    - [[T1204-user_execution#^t1204001-malicious-link|T1204.001: Malicious Link]]
    - [[T1204-user_execution#^t1204002-malicious-file|T1204.002: Malicious File]]
    - [[T1204-user_execution#^t1204003-malicious-image|T1204.003: Malicious Image]]
    - [[T1204-user_execution#^t1204005-malicious-library|T1204.005: Malicious Library]]
- [[T1213-data_from_information_repositories|T1213: Data from Information Repositories]]
- [[T1213-data_from_information_repositories|T1213: Data from Information Repositories]]
    - [[T1213-data_from_information_repositories#^t1213001-confluence|T1213.001: Confluence]]
    - [[T1213-data_from_information_repositories#^t1213002-sharepoint|T1213.002: Sharepoint]]
    - [[T1213-data_from_information_repositories#^t1213003-code-repositories|T1213.003: Code Repositories]]
    - [[T1213-data_from_information_repositories#^t1213004-customer-relationship-management-software|T1213.004: Customer Relationship Management Software]]
    - [[T1213-data_from_information_repositories#^t1213005-messaging-applications|T1213.005: Messaging Applications]]
    - [[T1213-data_from_information_repositories#^t1213006-databases|T1213.006: Databases]]
- [[T1221-template_injection|T1221: Template Injection]]
- [[T1528-steal_application_access_token|T1528: Steal Application Access Token]]
- [[T1539-steal_web_session_cookie|T1539: Steal Web Session Cookie]]
- [[T1547-boot_or_logon_autostart_execution|T1547: Boot or Logon Autostart Execution]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547007-re-opened-applications|T1547.007: Re-opened Applications]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
    - [[T1552-unsecured_credentials#^t1552001-credentials-in-files|T1552.001: Credentials In Files]]
    - [[T1552-unsecured_credentials#^t1552008-chat-messages|T1552.008: Chat Messages]]
- [[T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]
    - [[T1555-credentials_from_password_stores#^t1555003-credentials-from-web-browsers|T1555.003: Credentials from Web Browsers]]
    - [[T1555-credentials_from_password_stores#^t1555005-password-managers|T1555.005: Password Managers]]
- [[T1556-modify_authentication_process|T1556: Modify Authentication Process]]
    - [[T1556-modify_authentication_process#^t1556001-domain-controller-authentication|T1556.001: Domain Controller Authentication]]
- [[T1557-adversary-in-the-middle|T1557: Adversary-in-the-Middle]]
- [[T1557-adversary-in-the-middle|T1557: Adversary-in-the-Middle]]
    - [[T1557-adversary-in-the-middle#^t1557002-arp-cache-poisoning|T1557.002: ARP Cache Poisoning]]
    - [[T1557-adversary-in-the-middle#^t1557004-evil-twin|T1557.004: Evil Twin]]
- [[T1566-phishing|T1566: Phishing]]
- [[T1566-phishing|T1566: Phishing]]
    - [[T1566-phishing#^t1566001-spearphishing-attachment|T1566.001: Spearphishing Attachment]]
    - [[T1566-phishing#^t1566002-spearphishing-link|T1566.002: Spearphishing Link]]
    - [[T1566-phishing#^t1566003-spearphishing-via-service|T1566.003: Spearphishing via Service]]
    - [[T1566-phishing#^t1566004-spearphishing-voice|T1566.004: Spearphishing Voice]]
- [[T1598-phishing_for_information|T1598: Phishing for Information]]
- [[T1598-phishing_for_information|T1598: Phishing for Information]]
    - [[T1598-phishing_for_information#^t1598001-spearphishing-service|T1598.001: Spearphishing Service]]
    - [[T1598-phishing_for_information#^t1598002-spearphishing-attachment|T1598.002: Spearphishing Attachment]]
    - [[T1598-phishing_for_information#^t1598003-spearphishing-link|T1598.003: Spearphishing Link]]
    - [[T1598-phishing_for_information#^t1598004-spearphishing-voice|T1598.004: Spearphishing Voice]]
- [[T1621-multi-factor_authentication_request_generation|T1621: Multi-Factor Authentication Request Generation]]
- [[T1656-impersonation|T1656: Impersonation]]
- [[T1657-financial_theft|T1657: Financial Theft]]
- [[T1667-email_bombing|T1667: Email Bombing]]

