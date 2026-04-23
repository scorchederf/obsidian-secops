---
mitre_id: "M1047"
mitre_name: "Audit"
mitre_type: "course-of-action"
mitre_stix_id: "course-of-action--cc2399fd-3cd3-4319-8d0a-fbd6420cdaf8"
mitre_created: "2019-06-11T17:06:14.029Z"
mitre_modified: "2024-12-10T16:28:27.046Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/mitigations/M1047/"
framework: "attack"
generated: "true"
build_date: "2026-04-23 22:40:56"
build_source: "script"
object_type: "mitigation"
tags:
  - "attack"
  - "mitigation"
  - "defense"
  - "countermeasure"
---

# M1047: Audit

Auditing is the process of recording activity and systematically reviewing and analyzing the activity and system configurations. The primary purpose of auditing is to detect anomalies and identify potential threats or weaknesses in the environment. Proper auditing configurations can also help to meet compliance requirements. The process of auditing encompasses regular analysis of user behaviors and system logs in support of proactive security measures.

Auditing is applicable to all systems used within an organization, from the front door of a building to accessing a file on a fileserver. It is considered more critical for regulated industries such as, healthcare, finance and government where compliance requirements demand stringent tracking of user and system activates.This mitigation can be implemented through the following measures: 

System Audit:

- Use Case: Regularly assess system configurations to ensure compliance with organizational security policies.
- Implementation: Use tools to scan for deviations from established benchmarks.

Permission Audits:

- Use Case: Review file and folder permissions to minimize the risk of unauthorized access or privilege escalation.
- Implementation: Run access reviews to identify users or groups with excessive permissions.

Software Audits:

- Use Case: Identify outdated, unsupported, or insecure software that could serve as an attack vector.
- Implementation: Use inventory and vulnerability scanning tools to detect outdated versions and recommend secure alternatives.

Configuration Audits:

- Use Case: Evaluate system and network configurations to ensure secure settings (e.g., disabled SMBv1, enabled MFA).
- Implementation: Implement automated configuration scanning tools like SCAP (Security Content Automation Protocol) to identify non-compliant systems.

Network Audits:

- Use Case: Examine network traffic, firewall rules, and endpoint communications to identify unauthorized or insecure connections.
- Implementation: Utilize tools such as Wireshark, or Zeek to monitor and log suspicious network behavior.

## Mitigates Techniques

- [[T1021-remote_services|T1021: Remote Services]]
- [[T1021-remote_services|T1021: Remote Services]]
    - [[T1021-remote_services#^t1021001-remote-desktop-protocol|T1021.001: Remote Desktop Protocol]]
    - [[T1021-remote_services#^t1021005-vnc|T1021.005: VNC]]
- [[T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]]
- [[T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]]
    - [[T1027-obfuscated_files_or_information#^t1027011-fileless-storage|T1027.011: Fileless Storage]]
- [[T1036-masquerading|T1036: Masquerading]]
- [[T1036-masquerading|T1036: Masquerading]]
    - [[T1036-masquerading#^t1036010-masquerade-account-name|T1036.010: Masquerade Account Name]]
    - [[T1036-masquerading#^t1036012-browser-fingerprint|T1036.012: Browser Fingerprint]]
- [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]]
- [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]]
    - [[T1053-scheduled_task_job#^t1053002-at|T1053.002: At]]
    - [[T1053-scheduled_task_job#^t1053003-cron|T1053.003: Cron]]
    - [[T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
    - [[T1059-command_and_scripting_interpreter#^t1059006-python|T1059.006: Python]]
    - [[T1059-command_and_scripting_interpreter#^t1059011-lua|T1059.011: Lua]]
- [[T1070-indicator_removal|T1070: Indicator Removal]]
    - [[T1070-indicator_removal#^t1070008-clear-mailbox-data|T1070.008: Clear Mailbox Data]]
- [[T1087-account_discovery|T1087: Account Discovery]]
    - [[T1087-account_discovery#^t1087004-cloud-account|T1087.004: Cloud Account]]
- [[T1095-non-application_layer_protocol|T1095: Non-Application Layer Protocol]]
- [[T1114-email_collection|T1114: Email Collection]]
- [[T1114-email_collection|T1114: Email Collection]]
    - [[T1114-email_collection#^t1114003-email-forwarding-rule|T1114.003: Email Forwarding Rule]]
- [[T1176-software_extensions|T1176: Software Extensions]]
- [[T1176-software_extensions|T1176: Software Extensions]]
    - [[T1176-software_extensions#^t1176001-browser-extensions|T1176.001: Browser Extensions]]
    - [[T1176-software_extensions#^t1176002-ide-extensions|T1176.002: IDE Extensions]]
- [[T1204-user_execution|T1204: User Execution]]
    - [[T1204-user_execution#^t1204003-malicious-image|T1204.003: Malicious Image]]
- [[T1213-data_from_information_repositories|T1213: Data from Information Repositories]]
- [[T1213-data_from_information_repositories|T1213: Data from Information Repositories]]
    - [[T1213-data_from_information_repositories#^t1213001-confluence|T1213.001: Confluence]]
    - [[T1213-data_from_information_repositories#^t1213002-sharepoint|T1213.002: Sharepoint]]
    - [[T1213-data_from_information_repositories#^t1213003-code-repositories|T1213.003: Code Repositories]]
    - [[T1213-data_from_information_repositories#^t1213004-customer-relationship-management-software|T1213.004: Customer Relationship Management Software]]
    - [[T1213-data_from_information_repositories#^t1213005-messaging-applications|T1213.005: Messaging Applications]]
    - [[T1213-data_from_information_repositories#^t1213006-databases|T1213.006: Databases]]
- [[T1482-domain_trust_discovery|T1482: Domain Trust Discovery]]
- [[T1484-domain_or_tenant_policy_modification|T1484: Domain or Tenant Policy Modification]]
- [[T1484-domain_or_tenant_policy_modification|T1484: Domain or Tenant Policy Modification]]
    - [[T1484-domain_or_tenant_policy_modification#^t1484001-group-policy-modification|T1484.001: Group Policy Modification]]
- [[T1505-server_software_component|T1505: Server Software Component]]
- [[T1505-server_software_component|T1505: Server Software Component]]
    - [[T1505-server_software_component#^t1505001-sql-stored-procedures|T1505.001: SQL Stored Procedures]]
    - [[T1505-server_software_component#^t1505002-transport-agent|T1505.002: Transport Agent]]
    - [[T1505-server_software_component#^t1505004-iis-components|T1505.004: IIS Components]]
    - [[T1505-server_software_component#^t1505005-terminal-services-dll|T1505.005: Terminal Services DLL]]
    - [[T1505-server_software_component#^t1505006-vsphere-installation-bundles|T1505.006: vSphere Installation Bundles]]
- [[T1525-implant_internal_image|T1525: Implant Internal Image]]
- [[T1528-steal_application_access_token|T1528: Steal Application Access Token]]
- [[T1530-data_from_cloud_storage|T1530: Data from Cloud Storage]]
- [[T1539-steal_web_session_cookie|T1539: Steal Web Session Cookie]]
- [[T1542-pre-os_boot|T1542: Pre-OS Boot]]
- [[T1542-pre-os_boot|T1542: Pre-OS Boot]]
    - [[T1542-pre-os_boot#^t1542004-rommonkit|T1542.004: ROMMONkit]]
    - [[T1542-pre-os_boot#^t1542005-tftp-boot|T1542.005: TFTP Boot]]
- [[T1543-create_or_modify_system_process|T1543: Create or Modify System Process]]
- [[T1543-create_or_modify_system_process|T1543: Create or Modify System Process]]
    - [[T1543-create_or_modify_system_process#^t1543003-windows-service|T1543.003: Windows Service]]
    - [[T1543-create_or_modify_system_process#^t1543004-launch-daemon|T1543.004: Launch Daemon]]
- [[T1546-event_triggered_execution|T1546: Event Triggered Execution]]
    - [[T1546-event_triggered_execution#^t1546006-lc-load-dylib-addition|T1546.006: LC_LOAD_DYLIB Addition]]
- [[T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]
- [[T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]
    - [[T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]
    - [[T1548-abuse_elevation_control_mechanism#^t1548006-tcc-manipulation|T1548.006: TCC Manipulation]]
- [[T1550-use_alternate_authentication_material|T1550: Use Alternate Authentication Material]]
- [[T1550-use_alternate_authentication_material|T1550: Use Alternate Authentication Material]]
    - [[T1550-use_alternate_authentication_material#^t1550001-application-access-token|T1550.001: Application Access Token]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
    - [[T1552-unsecured_credentials#^t1552001-credentials-in-files|T1552.001: Credentials In Files]]
    - [[T1552-unsecured_credentials#^t1552002-credentials-in-registry|T1552.002: Credentials in Registry]]
    - [[T1552-unsecured_credentials#^t1552004-private-keys|T1552.004: Private Keys]]
    - [[T1552-unsecured_credentials#^t1552006-group-policy-preferences|T1552.006: Group Policy Preferences]]
    - [[T1552-unsecured_credentials#^t1552008-chat-messages|T1552.008: Chat Messages]]
- [[T1556-modify_authentication_process|T1556: Modify Authentication Process]]
- [[T1556-modify_authentication_process|T1556: Modify Authentication Process]]
    - [[T1556-modify_authentication_process#^t1556006-multi-factor-authentication|T1556.006: Multi-Factor Authentication]]
    - [[T1556-modify_authentication_process#^t1556007-hybrid-identity|T1556.007: Hybrid Identity]]
    - [[T1556-modify_authentication_process#^t1556008-network-provider-dll|T1556.008: Network Provider DLL]]
- [[T1558-steal_or_forge_kerberos_tickets|T1558: Steal or Forge Kerberos Tickets]]
- [[T1558-steal_or_forge_kerberos_tickets|T1558: Steal or Forge Kerberos Tickets]]
    - [[T1558-steal_or_forge_kerberos_tickets#^t1558004-as-rep-roasting|T1558.004: AS-REP Roasting]]
    - [[T1558-steal_or_forge_kerberos_tickets#^t1558005-ccache-files|T1558.005: Ccache Files]]
- [[T1560-archive_collected_data|T1560: Archive Collected Data]]
- [[T1560-archive_collected_data|T1560: Archive Collected Data]]
    - [[T1560-archive_collected_data#^t1560001-archive-via-utility|T1560.001: Archive via Utility]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
    - [[T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]
    - [[T1562-impair_defenses#^t1562002-disable-windows-event-logging|T1562.002: Disable Windows Event Logging]]
    - [[T1562-impair_defenses#^t1562004-disable-or-modify-system-firewall|T1562.004: Disable or Modify System Firewall]]
    - [[T1562-impair_defenses#^t1562007-disable-or-modify-cloud-firewall|T1562.007: Disable or Modify Cloud Firewall]]
    - [[T1562-impair_defenses#^t1562012-disable-or-modify-linux-audit-system|T1562.012: Disable or Modify Linux Audit System]]
    - [[T1562-impair_defenses#^t1562013-disable-or-modify-network-device-firewall|T1562.013: Disable or Modify Network Device Firewall]]
- [[T1563-remote_service_session_hijacking|T1563: Remote Service Session Hijacking]]
    - [[T1563-remote_service_session_hijacking#^t1563002-rdp-hijacking|T1563.002: RDP Hijacking]]
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]
    - [[T1564-hide_artifacts#^t1564006-run-virtual-instance|T1564.006: Run Virtual Instance]]
    - [[T1564-hide_artifacts#^t1564008-email-hiding-rules|T1564.008: Email Hiding Rules]]
- [[T1566-phishing|T1566: Phishing]]
- [[T1566-phishing|T1566: Phishing]]
    - [[T1566-phishing#^t1566001-spearphishing-attachment|T1566.001: Spearphishing Attachment]]
    - [[T1566-phishing#^t1566002-spearphishing-link|T1566.002: Spearphishing Link]]
    - [[T1566-phishing#^t1566003-spearphishing-via-service|T1566.003: Spearphishing via Service]]
- [[T1574-hijack_execution_flow|T1574: Hijack Execution Flow]]
- [[T1574-hijack_execution_flow|T1574: Hijack Execution Flow]]
    - [[T1574-hijack_execution_flow#^t1574001-dll|T1574.001: DLL]]
    - [[T1574-hijack_execution_flow#^t1574005-executable-installer-file-permissions-weakness|T1574.005: Executable Installer File Permissions Weakness]]
    - [[T1574-hijack_execution_flow#^t1574007-path-interception-by-path-environment-variable|T1574.007: Path Interception by PATH Environment Variable]]
    - [[T1574-hijack_execution_flow#^t1574008-path-interception-by-search-order-hijacking|T1574.008: Path Interception by Search Order Hijacking]]
    - [[T1574-hijack_execution_flow#^t1574009-path-interception-by-unquoted-path|T1574.009: Path Interception by Unquoted Path]]
    - [[T1574-hijack_execution_flow#^t1574010-services-file-permissions-weakness|T1574.010: Services File Permissions Weakness]]
- [[T1578-modify_cloud_compute_infrastructure|T1578: Modify Cloud Compute Infrastructure]]
- [[T1578-modify_cloud_compute_infrastructure|T1578: Modify Cloud Compute Infrastructure]]
    - [[T1578-modify_cloud_compute_infrastructure#^t1578001-create-snapshot|T1578.001: Create Snapshot]]
    - [[T1578-modify_cloud_compute_infrastructure#^t1578002-create-cloud-instance|T1578.002: Create Cloud Instance]]
    - [[T1578-modify_cloud_compute_infrastructure#^t1578003-delete-cloud-instance|T1578.003: Delete Cloud Instance]]
    - [[T1578-modify_cloud_compute_infrastructure#^t1578005-modify-cloud-compute-configurations|T1578.005: Modify Cloud Compute Configurations]]
- [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]]
- [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]]
    - [[T1593-search_open_websites_domains#^t1593003-code-repositories|T1593.003: Code Repositories]]
- [[T1606-forge_web_credentials|T1606: Forge Web Credentials]]
- [[T1606-forge_web_credentials|T1606: Forge Web Credentials]]
    - [[T1606-forge_web_credentials#^t1606001-web-cookies|T1606.001: Web Cookies]]
    - [[T1606-forge_web_credentials#^t1606002-saml-tokens|T1606.002: SAML Tokens]]
- [[T1610-deploy_container|T1610: Deploy Container]]
- [[T1612-build_image_on_host|T1612: Build Image on Host]]
- [[T1649-steal_or_forge_authentication_certificates|T1649: Steal or Forge Authentication Certificates]]
- [[T1653-power_settings|T1653: Power Settings]]
- [[T1666-modify_cloud_resource_hierarchy|T1666: Modify Cloud Resource Hierarchy]]
- [[T1671-cloud_application_integration|T1671: Cloud Application Integration]]

## Workspace

- [[kb/notes/attack/mitigations/m1047-notes|Open workspace note]]

