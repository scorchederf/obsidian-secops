---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-CI"
d3fend_name: "Configuration Inventory"
d3fend_ontology_id: "d3f:ConfigurationInventory"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AConfigurationInventory/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-25 14:47:22"
build_source: "script"
attack_technique_ids:
  - "T1037"
  - "T1037.004"
  - "T1037.005"
  - "T1114"
  - "T1114.003"
  - "T1134"
  - "T1134.005"
  - "T1137"
  - "T1137.001"
  - "T1137.002"
  - "T1137.004"
  - "T1137.005"
  - "T1218"
  - "T1218.002"
  - "T1222"
  - "T1222.001"
  - "T1222.002"
  - "T1484"
  - "T1484.001"
  - "T1484.002"
  - "T1490"
  - "T1518"
  - "T1518.001"
  - "T1526"
  - "T1538"
  - "T1546"
  - "T1546.001"
  - "T1546.002"
  - "T1546.007"
  - "T1546.008"
  - "T1546.009"
  - "T1546.010"
  - "T1546.011"
  - "T1546.014"
  - "T1547"
  - "T1547.001"
  - "T1547.002"
  - "T1547.003"
  - "T1547.004"
  - "T1547.005"
  - "T1547.010"
  - "T1548"
  - "T1548.001"
  - "T1548.002"
  - "T1548.005"
  - "T1552"
  - "T1552.005"
  - "T1552.006"
  - "T1553"
  - "T1553.003"
  - "T1556"
  - "T1556.002"
  - "T1556.009"
  - "T1562"
  - "T1562.002"
  - "T1562.003"
  - "T1562.004"
  - "T1562.007"
  - "T1562.008"
  - "T1562.009"
  - "T1564"
  - "T1564.008"
  - "T1574"
  - "T1574.011"
  - "T1574.012"
  - "T1578"
  - "T1578.002"
  - "T1578.003"
  - "T1578.004"
  - "T1578.005"
  - "T1614"
  - "T1614.001"
  - "T1615"
  - "T1666"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

Configuration inventory identifies and records the configuration of software and hardware and their components throughout the organization.

## Workspace

- [[notes/defend/techniques/D3-CI-configuration_inventory-note|Open workspace note]]

![[notes/defend/techniques/D3-CI-configuration_inventory-note]]

## Parent Technique

- [[D3-AI-asset_inventory|D3-AI: Asset Inventory]]

## Related ATT&CK Techniques

- [[T1037-boot_or_logon_initialization_scripts|T1037: Boot or Logon Initialization Scripts]]
- [[T1037-boot_or_logon_initialization_scripts#^t1037004-rc-scripts|T1037.004: RC Scripts]]
- [[T1037-boot_or_logon_initialization_scripts#^t1037005-startup-items|T1037.005: Startup Items]]
- [[T1114-email_collection|T1114: Email Collection]]
- [[T1114-email_collection#^t1114003-email-forwarding-rule|T1114.003: Email Forwarding Rule]]
- [[T1134-access_token_manipulation|T1134: Access Token Manipulation]]
- [[T1134-access_token_manipulation#^t1134005-sid-history-injection|T1134.005: SID-History Injection]]
- [[T1137-office_application_startup|T1137: Office Application Startup]]
- [[T1137-office_application_startup#^t1137001-office-template-macros|T1137.001: Office Template Macros]]
- [[T1137-office_application_startup#^t1137002-office-test|T1137.002: Office Test]]
- [[T1137-office_application_startup#^t1137004-outlook-home-page|T1137.004: Outlook Home Page]]
- [[T1137-office_application_startup#^t1137005-outlook-rules|T1137.005: Outlook Rules]]
- [[T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]
- [[T1218-system_binary_proxy_execution#^t1218002-control-panel|T1218.002: Control Panel]]
- [[T1222-file_and_directory_permissions_modification|T1222: File and Directory Permissions Modification]]
- [[T1222-file_and_directory_permissions_modification#^t1222001-windows-file-and-directory-permissions-modification|T1222.001: Windows File and Directory Permissions Modification]]
- [[T1222-file_and_directory_permissions_modification#^t1222002-linux-and-mac-file-and-directory-permissions-modification|T1222.002: Linux and Mac File and Directory Permissions Modification]]
- [[T1484-domain_or_tenant_policy_modification|T1484: Domain or Tenant Policy Modification]]
- [[T1484-domain_or_tenant_policy_modification#^t1484001-group-policy-modification|T1484.001: Group Policy Modification]]
- [[T1484-domain_or_tenant_policy_modification#^t1484002-trust-modification|T1484.002: Trust Modification]]
- [[T1490-inhibit_system_recovery|T1490: Inhibit System Recovery]]
- [[T1518-software_discovery|T1518: Software Discovery]]
- [[T1518-software_discovery#^t1518001-security-software-discovery|T1518.001: Security Software Discovery]]
- [[T1526-cloud_service_discovery|T1526: Cloud Service Discovery]]
- [[T1538-cloud_service_dashboard|T1538: Cloud Service Dashboard]]
- [[T1546-event_triggered_execution|T1546: Event Triggered Execution]]
- [[T1546-event_triggered_execution#^t1546001-change-default-file-association|T1546.001: Change Default File Association]]
- [[T1546-event_triggered_execution#^t1546002-screensaver|T1546.002: Screensaver]]
- [[T1546-event_triggered_execution#^t1546007-netsh-helper-dll|T1546.007: Netsh Helper DLL]]
- [[T1546-event_triggered_execution#^t1546008-accessibility-features|T1546.008: Accessibility Features]]
- [[T1546-event_triggered_execution#^t1546009-appcert-dlls|T1546.009: AppCert DLLs]]
- [[T1546-event_triggered_execution#^t1546010-appinit-dlls|T1546.010: AppInit DLLs]]
- [[T1546-event_triggered_execution#^t1546011-application-shimming|T1546.011: Application Shimming]]
- [[T1546-event_triggered_execution#^t1546014-emond|T1546.014: Emond]]
- [[T1547-boot_or_logon_autostart_execution|T1547: Boot or Logon Autostart Execution]]
- [[T1547-boot_or_logon_autostart_execution#^t1547001-registry-run-keys---startup-folder|T1547.001: Registry Run Keys / Startup Folder]]
- [[T1547-boot_or_logon_autostart_execution#^t1547002-authentication-package|T1547.002: Authentication Package]]
- [[T1547-boot_or_logon_autostart_execution#^t1547003-time-providers|T1547.003: Time Providers]]
- [[T1547-boot_or_logon_autostart_execution#^t1547004-winlogon-helper-dll|T1547.004: Winlogon Helper DLL]]
- [[T1547-boot_or_logon_autostart_execution#^t1547005-security-support-provider|T1547.005: Security Support Provider]]
- [[T1547-boot_or_logon_autostart_execution#^t1547010-port-monitors|T1547.010: Port Monitors]]
- [[T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]
- [[T1548-abuse_elevation_control_mechanism#^t1548001-setuid-and-setgid|T1548.001: Setuid and Setgid]]
- [[T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]
- [[T1548-abuse_elevation_control_mechanism#^t1548005-temporary-elevated-cloud-access|T1548.005: Temporary Elevated Cloud Access]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
- [[T1552-unsecured_credentials#^t1552005-cloud-instance-metadata-api|T1552.005: Cloud Instance Metadata API]]
- [[T1552-unsecured_credentials#^t1552006-group-policy-preferences|T1552.006: Group Policy Preferences]]
- [[T1553-subvert_trust_controls|T1553: Subvert Trust Controls]]
- [[T1553-subvert_trust_controls#^t1553003-sip-and-trust-provider-hijacking|T1553.003: SIP and Trust Provider Hijacking]]
- [[T1556-modify_authentication_process|T1556: Modify Authentication Process]]
- [[T1556-modify_authentication_process#^t1556002-password-filter-dll|T1556.002: Password Filter DLL]]
- [[T1556-modify_authentication_process#^t1556009-conditional-access-policies|T1556.009: Conditional Access Policies]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
- [[T1562-impair_defenses#^t1562002-disable-windows-event-logging|T1562.002: Disable Windows Event Logging]]
- [[T1562-impair_defenses#^t1562003-impair-command-history-logging|T1562.003: Impair Command History Logging]]
- [[T1562-impair_defenses#^t1562004-disable-or-modify-system-firewall|T1562.004: Disable or Modify System Firewall]]
- [[T1562-impair_defenses#^t1562007-disable-or-modify-cloud-firewall|T1562.007: Disable or Modify Cloud Firewall]]
- [[T1562-impair_defenses#^t1562008-disable-or-modify-cloud-logs|T1562.008: Disable or Modify Cloud Logs]]
- [[T1562-impair_defenses#^t1562009-safe-mode-boot|T1562.009: Safe Mode Boot]]
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]
- [[T1564-hide_artifacts#^t1564008-email-hiding-rules|T1564.008: Email Hiding Rules]]
- [[T1574-hijack_execution_flow|T1574: Hijack Execution Flow]]
- [[T1574-hijack_execution_flow#^t1574011-services-registry-permissions-weakness|T1574.011: Services Registry Permissions Weakness]]
- [[T1574-hijack_execution_flow#^t1574012-cor-profiler|T1574.012: COR_PROFILER]]
- [[T1578-modify_cloud_compute_infrastructure|T1578: Modify Cloud Compute Infrastructure]]
- [[T1578-modify_cloud_compute_infrastructure#^t1578002-create-cloud-instance|T1578.002: Create Cloud Instance]]
- [[T1578-modify_cloud_compute_infrastructure#^t1578003-delete-cloud-instance|T1578.003: Delete Cloud Instance]]
- [[T1578-modify_cloud_compute_infrastructure#^t1578004-revert-cloud-instance|T1578.004: Revert Cloud Instance]]
- [[T1578-modify_cloud_compute_infrastructure#^t1578005-modify-cloud-compute-configurations|T1578.005: Modify Cloud Compute Configurations]]
- [[T1614-system_location_discovery|T1614: System Location Discovery]]
- [[T1614-system_location_discovery#^t1614001-system-language-discovery|T1614.001: System Language Discovery]]
- [[T1615-group_policy_discovery|T1615: Group Policy Discovery]]
- [[T1666-modify_cloud_resource_hierarchy|T1666: Modify Cloud Resource Hierarchy]]

## Knowledge Base Article

## How it works

The organization retrieves configuration information through means of SNMP (MIB records), WBEM (CIM records), other protocols, or custom scripts and captures that information in a repository, typically known as a Configuration Management Database (CMDB)."

## Ontology Relationships

- [[D3-AI-asset_inventory|D3-AI: Asset Inventory]]

