---
mitre_id: "M1054"
mitre_name: "Software Configuration"
mitre_type: "course-of-action"
mitre_stix_id: "course-of-action--b5dbb4c5-b0b1-40b1-80b6-e9e84ab90067"
mitre_created: "2019-07-19T14:40:23.529Z"
mitre_modified: "2024-12-24T14:02:11.579Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/mitigations/M1054/"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Software configuration refers to making security-focused adjustments to the settings of applications, middleware, databases, or other software to mitigate potential threats. These changes help reduce the attack surface, enforce best practices, and protect sensitive data. This mitigation can be implemented through the following measures:

Conduct a Security Review of Application Settings:

- Review the software documentation to identify recommended security configurations.
- Compare default settings against organizational policies and compliance requirements.

Implement Access Controls and Permissions:

- Restrict access to sensitive features or data within the software.
- Enforce least privilege principles for all roles and accounts interacting with the software.

Enable Logging and Monitoring:

- Configure detailed logging for key application events such as authentication failures, configuration changes, or unusual activity.
- Integrate logs with a centralized monitoring solution, such as a SIEM.

Update and Patch Software Regularly:

- Ensure the software is kept up-to-date with the latest security patches to address known vulnerabilities.
- Use automated patch management tools to streamline the update process.

Disable Unnecessary Features or Services:

- Turn off unused functionality or components that could introduce vulnerabilities, such as debugging interfaces or deprecated APIs.

Test Configuration Changes:

- Perform configuration changes in a staging environment before applying them in production.
- Conduct regular audits to ensure that settings remain aligned with security policies.

*Tools for Implementation*

Configuration Management Tools:

- Ansible: Automates configuration changes across multiple applications and environments.
- Chef: Ensures consistent application settings through code-based configuration management.
- Puppet: Automates software configurations and audits changes for compliance.

Security Benchmarking Tools:

- CIS-CAT: Provides benchmarks and audits for secure software configurations.
- Aqua Security Trivy: Scans containerized applications for configuration issues.

Vulnerability Management Solutions:

- Nessus: Identifies misconfigurations and suggests corrective actions.

Logging and Monitoring Tools:

- Splunk: Aggregates and analyzes application logs to detect suspicious activity.

## Workspace

- [[workspaces/attack/mitigations/M1054-software_configuration-note|Open workspace note]]

![[workspaces/attack/mitigations/M1054-software_configuration-note]]

## Mitigates Techniques

- [[T1137-office_application_startup|T1137: Office Application Startup]]
- [[T1137-office_application_startup|T1137: Office Application Startup]]
    - [[T1137-office_application_startup#^t1137002-office-test|T1137.002: Office Test]]
- [[T1213-data_from_information_repositories|T1213: Data from Information Repositories]]
- [[T1213-data_from_information_repositories|T1213: Data from Information Repositories]]
    - [[T1213-data_from_information_repositories#^t1213004-customer-relationship-management-software|T1213.004: Customer Relationship Management Software]]
    - [[T1213-data_from_information_repositories#^t1213006-databases|T1213.006: Databases]]
- [[T1535-unused_unsupported_cloud_regions|T1535: Unused/Unsupported Cloud Regions]]
- [[T1537-transfer_data_to_cloud_account|T1537: Transfer Data to Cloud Account]]
- [[T1539-steal_web_session_cookie|T1539: Steal Web Session Cookie]]
- [[T1543-create_or_modify_system_process|T1543: Create or Modify System Process]]
- [[T1543-create_or_modify_system_process|T1543: Create or Modify System Process]]
    - [[T1543-create_or_modify_system_process#^t1543005-container-service|T1543.005: Container Service]]
- [[T1546-event_triggered_execution|T1546: Event Triggered Execution]]
    - [[T1546-event_triggered_execution#^t1546013-powershell-profile|T1546.013: PowerShell Profile]]
- [[T1550-use_alternate_authentication_material|T1550: Use Alternate Authentication Material]]
    - [[T1550-use_alternate_authentication_material#^t1550004-web-session-cookie|T1550.004: Web Session Cookie]]
- [[T1553-subvert_trust_controls|T1553: Subvert Trust Controls]]
- [[T1553-subvert_trust_controls|T1553: Subvert Trust Controls]]
    - [[T1553-subvert_trust_controls#^t1553004-install-root-certificate|T1553.004: Install Root Certificate]]
- [[T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]
    - [[T1555-credentials_from_password_stores#^t1555005-password-managers|T1555.005: Password Managers]]
- [[T1559-inter-process_communication|T1559: Inter-Process Communication]]
- [[T1559-inter-process_communication|T1559: Inter-Process Communication]]
    - [[T1559-inter-process_communication#^t1559002-dynamic-data-exchange|T1559.002: Dynamic Data Exchange]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
    - [[T1562-impair_defenses#^t1562006-indicator-blocking|T1562.006: Indicator Blocking]]
    - [[T1562-impair_defenses#^t1562009-safe-mode-boot|T1562.009: Safe Mode Boot]]
    - [[T1562-impair_defenses#^t1562010-downgrade-attack|T1562.010: Downgrade Attack]]
- [[T1566-phishing|T1566: Phishing]]
- [[T1566-phishing|T1566: Phishing]]
    - [[T1566-phishing#^t1566001-spearphishing-attachment|T1566.001: Spearphishing Attachment]]
    - [[T1566-phishing#^t1566002-spearphishing-link|T1566.002: Spearphishing Link]]
- [[T1590-gather_victim_network_information|T1590: Gather Victim Network Information]]
    - [[T1590-gather_victim_network_information#^t1590002-dns|T1590.002: DNS]]
- [[T1598-phishing_for_information|T1598: Phishing for Information]]
- [[T1598-phishing_for_information|T1598: Phishing for Information]]
    - [[T1598-phishing_for_information#^t1598002-spearphishing-attachment|T1598.002: Spearphishing Attachment]]
    - [[T1598-phishing_for_information#^t1598003-spearphishing-link|T1598.003: Spearphishing Link]]
- [[T1602-data_from_configuration_repository|T1602: Data from Configuration Repository]]
- [[T1602-data_from_configuration_repository|T1602: Data from Configuration Repository]]
    - [[T1602-data_from_configuration_repository#^t1602001-snmp-(mib-dump)|T1602.001: SNMP (MIB Dump)]]
    - [[T1602-data_from_configuration_repository#^t1602002-network-device-configuration-dump|T1602.002: Network Device Configuration Dump]]
- [[T1606-forge_web_credentials|T1606: Forge Web Credentials]]
- [[T1606-forge_web_credentials|T1606: Forge Web Credentials]]
    - [[T1606-forge_web_credentials#^t1606001-web-cookies|T1606.001: Web Cookies]]
- [[T1666-modify_cloud_resource_hierarchy|T1666: Modify Cloud Resource Hierarchy]]
- [[T1667-email_bombing|T1667: Email Bombing]]
- [[T1672-email_spoofing|T1672: Email Spoofing]]
- [[T1677-poisoned_pipeline_execution|T1677: Poisoned Pipeline Execution]]

