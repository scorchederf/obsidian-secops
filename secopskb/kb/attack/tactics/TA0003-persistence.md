---
mitre_id: "TA0003"
mitre_name: "Persistence"
mitre_type: "x-mitre-tactic"
mitre_stix_id: "x-mitre-tactic--5bc1d813-693e-4823-9961-abf9af4b0e92"
mitre_created: "2018-10-17T00:14:20.652Z"
mitre_modified: "2025-04-25T14:45:33.492Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/tactics/TA0003/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "tactic"
tags:
  - "attack"
  - "tactic"
  - "offense"
mitre_shortname: "persistence"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

The adversary is trying to maintain their foothold.

Persistence consists of techniques that adversaries use to keep access to systems across restarts, changed credentials, and other interruptions that could cut off their access. Techniques used for persistence include any access, action, or configuration changes that let them maintain their foothold on systems, such as replacing or hijacking legitimate code or adding startup code. 

## Workspace

- [[workspaces/attack/tactics/TA0003-persistence-note|Open workspace note]]

![[workspaces/attack/tactics/TA0003-persistence-note]]

## Related Techniques

- [[T1037-boot_or_logon_initialization_scripts|T1037: Boot or Logon Initialization Scripts]]
    - [[T1037-boot_or_logon_initialization_scripts#^t1037001-logon-script-(windows)|T1037.001: Logon Script (Windows)]]
    - [[T1037-boot_or_logon_initialization_scripts#^t1037002-login-hook|T1037.002: Login Hook]]
    - [[T1037-boot_or_logon_initialization_scripts#^t1037003-network-logon-script|T1037.003: Network Logon Script]]
    - [[T1037-boot_or_logon_initialization_scripts#^t1037004-rc-scripts|T1037.004: RC Scripts]]
    - [[T1037-boot_or_logon_initialization_scripts#^t1037005-startup-items|T1037.005: Startup Items]]
- [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]]
    - [[T1053-scheduled_task_job#^t1053002-at|T1053.002: At]]
    - [[T1053-scheduled_task_job#^t1053003-cron|T1053.003: Cron]]
    - [[T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]
    - [[T1053-scheduled_task_job#^t1053006-systemd-timers|T1053.006: Systemd Timers]]
    - [[T1053-scheduled_task_job#^t1053007-container-orchestration-job|T1053.007: Container Orchestration Job]]
- [[T1078-valid_accounts|T1078: Valid Accounts]]
    - [[T1078-valid_accounts#^t1078001-default-accounts|T1078.001: Default Accounts]]
    - [[T1078-valid_accounts#^t1078002-domain-accounts|T1078.002: Domain Accounts]]
    - [[T1078-valid_accounts#^t1078003-local-accounts|T1078.003: Local Accounts]]
    - [[T1078-valid_accounts#^t1078004-cloud-accounts|T1078.004: Cloud Accounts]]
- [[T1098-account_manipulation|T1098: Account Manipulation]]
    - [[T1098-account_manipulation#^t1098001-additional-cloud-credentials|T1098.001: Additional Cloud Credentials]]
    - [[T1098-account_manipulation#^t1098002-additional-email-delegate-permissions|T1098.002: Additional Email Delegate Permissions]]
    - [[T1098-account_manipulation#^t1098003-additional-cloud-roles|T1098.003: Additional Cloud Roles]]
    - [[T1098-account_manipulation#^t1098004-ssh-authorized-keys|T1098.004: SSH Authorized Keys]]
    - [[T1098-account_manipulation#^t1098005-device-registration|T1098.005: Device Registration]]
    - [[T1098-account_manipulation#^t1098006-additional-container-cluster-roles|T1098.006: Additional Container Cluster Roles]]
    - [[T1098-account_manipulation#^t1098007-additional-local-or-domain-groups|T1098.007: Additional Local or Domain Groups]]
- [[T1112-modify_registry|T1112: Modify Registry]]
- [[T1133-external_remote_services|T1133: External Remote Services]]
- [[T1136-create_account|T1136: Create Account]]
    - [[T1136-create_account#^t1136001-local-account|T1136.001: Local Account]]
    - [[T1136-create_account#^t1136002-domain-account|T1136.002: Domain Account]]
    - [[T1136-create_account#^t1136003-cloud-account|T1136.003: Cloud Account]]
- [[T1137-office_application_startup|T1137: Office Application Startup]]
    - [[T1137-office_application_startup#^t1137001-office-template-macros|T1137.001: Office Template Macros]]
    - [[T1137-office_application_startup#^t1137002-office-test|T1137.002: Office Test]]
    - [[T1137-office_application_startup#^t1137003-outlook-forms|T1137.003: Outlook Forms]]
    - [[T1137-office_application_startup#^t1137004-outlook-home-page|T1137.004: Outlook Home Page]]
    - [[T1137-office_application_startup#^t1137005-outlook-rules|T1137.005: Outlook Rules]]
    - [[T1137-office_application_startup#^t1137006-add-ins|T1137.006: Add-ins]]
- [[T1176-software_extensions|T1176: Software Extensions]]
    - [[T1176-software_extensions#^t1176001-browser-extensions|T1176.001: Browser Extensions]]
    - [[T1176-software_extensions#^t1176002-ide-extensions|T1176.002: IDE Extensions]]
- [[T1197-bits_jobs|T1197: BITS Jobs]]
- [[T1205-traffic_signaling|T1205: Traffic Signaling]]
    - [[T1205-traffic_signaling#^t1205001-port-knocking|T1205.001: Port Knocking]]
    - [[T1205-traffic_signaling#^t1205002-socket-filters|T1205.002: Socket Filters]]
- [[T1505-server_software_component|T1505: Server Software Component]]
    - [[T1505-server_software_component#^t1505001-sql-stored-procedures|T1505.001: SQL Stored Procedures]]
    - [[T1505-server_software_component#^t1505002-transport-agent|T1505.002: Transport Agent]]
    - [[T1505-server_software_component#^t1505003-web-shell|T1505.003: Web Shell]]
    - [[T1505-server_software_component#^t1505004-iis-components|T1505.004: IIS Components]]
    - [[T1505-server_software_component#^t1505005-terminal-services-dll|T1505.005: Terminal Services DLL]]
    - [[T1505-server_software_component#^t1505006-vsphere-installation-bundles|T1505.006: vSphere Installation Bundles]]
- [[T1525-implant_internal_image|T1525: Implant Internal Image]]
- [[T1542-pre-os_boot|T1542: Pre-OS Boot]]
    - [[T1542-pre-os_boot#^t1542001-system-firmware|T1542.001: System Firmware]]
    - [[T1542-pre-os_boot#^t1542002-component-firmware|T1542.002: Component Firmware]]
    - [[T1542-pre-os_boot#^t1542003-bootkit|T1542.003: Bootkit]]
    - [[T1542-pre-os_boot#^t1542004-rommonkit|T1542.004: ROMMONkit]]
    - [[T1542-pre-os_boot#^t1542005-tftp-boot|T1542.005: TFTP Boot]]
- [[T1543-create_or_modify_system_process|T1543: Create or Modify System Process]]
    - [[T1543-create_or_modify_system_process#^t1543001-launch-agent|T1543.001: Launch Agent]]
    - [[T1543-create_or_modify_system_process#^t1543002-systemd-service|T1543.002: Systemd Service]]
    - [[T1543-create_or_modify_system_process#^t1543003-windows-service|T1543.003: Windows Service]]
    - [[T1543-create_or_modify_system_process#^t1543004-launch-daemon|T1543.004: Launch Daemon]]
    - [[T1543-create_or_modify_system_process#^t1543005-container-service|T1543.005: Container Service]]
- [[T1546-event_triggered_execution|T1546: Event Triggered Execution]]
    - [[T1546-event_triggered_execution#^t1546001-change-default-file-association|T1546.001: Change Default File Association]]
    - [[T1546-event_triggered_execution#^t1546002-screensaver|T1546.002: Screensaver]]
    - [[T1546-event_triggered_execution#^t1546003-windows-management-instrumentation-event-subscription|T1546.003: Windows Management Instrumentation Event Subscription]]
    - [[T1546-event_triggered_execution#^t1546004-unix-shell-configuration-modification|T1546.004: Unix Shell Configuration Modification]]
    - [[T1546-event_triggered_execution#^t1546005-trap|T1546.005: Trap]]
    - [[T1546-event_triggered_execution#^t1546006-lc-load-dylib-addition|T1546.006: LC_LOAD_DYLIB Addition]]
    - [[T1546-event_triggered_execution#^t1546007-netsh-helper-dll|T1546.007: Netsh Helper DLL]]
    - [[T1546-event_triggered_execution#^t1546008-accessibility-features|T1546.008: Accessibility Features]]
    - [[T1546-event_triggered_execution#^t1546009-appcert-dlls|T1546.009: AppCert DLLs]]
    - [[T1546-event_triggered_execution#^t1546010-appinit-dlls|T1546.010: AppInit DLLs]]
    - [[T1546-event_triggered_execution#^t1546011-application-shimming|T1546.011: Application Shimming]]
    - [[T1546-event_triggered_execution#^t1546012-image-file-execution-options-injection|T1546.012: Image File Execution Options Injection]]
    - [[T1546-event_triggered_execution#^t1546013-powershell-profile|T1546.013: PowerShell Profile]]
    - [[T1546-event_triggered_execution#^t1546014-emond|T1546.014: Emond]]
    - [[T1546-event_triggered_execution#^t1546015-component-object-model-hijacking|T1546.015: Component Object Model Hijacking]]
    - [[T1546-event_triggered_execution#^t1546016-installer-packages|T1546.016: Installer Packages]]
    - [[T1546-event_triggered_execution#^t1546017-udev-rules|T1546.017: Udev Rules]]
    - [[T1546-event_triggered_execution#^t1546018-python-startup-hooks|T1546.018: Python Startup Hooks]]
- [[T1547-boot_or_logon_autostart_execution|T1547: Boot or Logon Autostart Execution]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547001-registry-run-keys---startup-folder|T1547.001: Registry Run Keys / Startup Folder]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547002-authentication-package|T1547.002: Authentication Package]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547003-time-providers|T1547.003: Time Providers]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547004-winlogon-helper-dll|T1547.004: Winlogon Helper DLL]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547005-security-support-provider|T1547.005: Security Support Provider]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547006-kernel-modules-and-extensions|T1547.006: Kernel Modules and Extensions]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547007-re-opened-applications|T1547.007: Re-opened Applications]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547008-lsass-driver|T1547.008: LSASS Driver]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547009-shortcut-modification|T1547.009: Shortcut Modification]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547010-port-monitors|T1547.010: Port Monitors]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547012-print-processors|T1547.012: Print Processors]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547013-xdg-autostart-entries|T1547.013: XDG Autostart Entries]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547014-active-setup|T1547.014: Active Setup]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547015-login-items|T1547.015: Login Items]]
- [[T1554-compromise_host_software_binary|T1554: Compromise Host Software Binary]]
- [[T1556-modify_authentication_process|T1556: Modify Authentication Process]]
    - [[T1556-modify_authentication_process#^t1556001-domain-controller-authentication|T1556.001: Domain Controller Authentication]]
    - [[T1556-modify_authentication_process#^t1556002-password-filter-dll|T1556.002: Password Filter DLL]]
    - [[T1556-modify_authentication_process#^t1556003-pluggable-authentication-modules|T1556.003: Pluggable Authentication Modules]]
    - [[T1556-modify_authentication_process#^t1556004-network-device-authentication|T1556.004: Network Device Authentication]]
    - [[T1556-modify_authentication_process#^t1556005-reversible-encryption|T1556.005: Reversible Encryption]]
    - [[T1556-modify_authentication_process#^t1556006-multi-factor-authentication|T1556.006: Multi-Factor Authentication]]
    - [[T1556-modify_authentication_process#^t1556007-hybrid-identity|T1556.007: Hybrid Identity]]
    - [[T1556-modify_authentication_process#^t1556008-network-provider-dll|T1556.008: Network Provider DLL]]
    - [[T1556-modify_authentication_process#^t1556009-conditional-access-policies|T1556.009: Conditional Access Policies]]
- [[T1574-hijack_execution_flow|T1574: Hijack Execution Flow]]
    - [[T1574-hijack_execution_flow#^t1574001-dll|T1574.001: DLL]]
    - [[T1574-hijack_execution_flow#^t1574004-dylib-hijacking|T1574.004: Dylib Hijacking]]
    - [[T1574-hijack_execution_flow#^t1574005-executable-installer-file-permissions-weakness|T1574.005: Executable Installer File Permissions Weakness]]
    - [[T1574-hijack_execution_flow#^t1574006-dynamic-linker-hijacking|T1574.006: Dynamic Linker Hijacking]]
    - [[T1574-hijack_execution_flow#^t1574007-path-interception-by-path-environment-variable|T1574.007: Path Interception by PATH Environment Variable]]
    - [[T1574-hijack_execution_flow#^t1574008-path-interception-by-search-order-hijacking|T1574.008: Path Interception by Search Order Hijacking]]
    - [[T1574-hijack_execution_flow#^t1574009-path-interception-by-unquoted-path|T1574.009: Path Interception by Unquoted Path]]
    - [[T1574-hijack_execution_flow#^t1574010-services-file-permissions-weakness|T1574.010: Services File Permissions Weakness]]
    - [[T1574-hijack_execution_flow#^t1574011-services-registry-permissions-weakness|T1574.011: Services Registry Permissions Weakness]]
    - [[T1574-hijack_execution_flow#^t1574012-cor-profiler|T1574.012: COR_PROFILER]]
    - [[T1574-hijack_execution_flow#^t1574013-kernelcallbacktable|T1574.013: KernelCallbackTable]]
    - [[T1574-hijack_execution_flow#^t1574014-appdomainmanager|T1574.014: AppDomainManager]]
- [[T1653-power_settings|T1653: Power Settings]]
- [[T1668-exclusive_control|T1668: Exclusive Control]]
- [[T1671-cloud_application_integration|T1671: Cloud Application Integration]]

