---
id: x-mitre-tactic--5e29b093-294e-49e9-a803-dab3d73b77dd
name: Privilege Escalation
created: 2018-10-17 00:14:20.652000+00:00
modified: 2025-04-25 14:45:33.853000+00:00
type: x-mitre-tactic
x_mitre_version: 1.0
x_mitre_domains: enterprise-attack
---

# Privilege Escalation

The adversary is trying to gain higher-level permissions.

Privilege Escalation consists of techniques that adversaries use to gain higher-level permissions on a system or network. Adversaries can often enter and explore a network with unprivileged access but require elevated permissions to follow through on their objectives. Common approaches are to take advantage of system weaknesses, misconfigurations, and vulnerabilities. Examples of elevated access include: 

* SYSTEM/root level
* local administrator
* user account with admin-like access 
* user accounts with access to specific system or perform specific function

These techniques often overlap with Persistence techniques, as OS features that let an adversary persist can execute in an elevated context.  

## Properties

- id: x-mitre-tactic--5e29b093-294e-49e9-a803-dab3d73b77dd
- name: Privilege Escalation
- created: 2018-10-17 00:14:20.652000+00:00
- modified: 2025-04-25 14:45:33.853000+00:00
- type: x-mitre-tactic
- x_mitre_version: 1.0
- x_mitre_domains: enterprise-attack

## Related Techniques

- [[T1013-port_monitors|T1013: Port Monitors]]
- [[T1015-accessibility_features|T1015: Accessibility Features]]
- [[T1034-path_interception|T1034: Path Interception]]
- [[T1037-boot_or_logon_initialization_scripts|T1037: Boot or Logon Initialization Scripts]]
    - [[T1037-boot_or_logon_initialization_scripts#^t1037001-logon-script-(windows)|T1037.001: Logon Script (Windows)]]
    - [[T1037-boot_or_logon_initialization_scripts#^t1037002-login-hook|T1037.002: Login Hook]]
    - [[T1037-boot_or_logon_initialization_scripts#^t1037003-network-logon-script|T1037.003: Network Logon Script]]
    - [[T1037-boot_or_logon_initialization_scripts#^t1037004-rc-scripts|T1037.004: RC Scripts]]
    - [[T1037-boot_or_logon_initialization_scripts#^t1037005-startup-items|T1037.005: Startup Items]]
- [[T1038-dll_search_order_hijacking|T1038: DLL Search Order Hijacking]]
- [[T1044-file_system_permissions_weakness|T1044: File System Permissions Weakness]]
- [[T1050-new_service|T1050: New Service]]
- [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]]
    - [[T1053-scheduled_task_job#^t1053002-at|T1053.002: At]]
    - [[T1053-scheduled_task_job#^t1053003-cron|T1053.003: Cron]]
    - [[T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]
    - [[T1053-scheduled_task_job#^t1053006-systemd-timers|T1053.006: Systemd Timers]]
    - [[T1053-scheduled_task_job#^t1053007-container-orchestration-job|T1053.007: Container Orchestration Job]]
- [[T1055-process_injection|T1055: Process Injection]]
    - [[T1055-process_injection#^t1055001-dynamic-link-library-injection|T1055.001: Dynamic-link Library Injection]]
    - [[T1055-process_injection#^t1055002-portable-executable-injection|T1055.002: Portable Executable Injection]]
    - [[T1055-process_injection#^t1055003-thread-execution-hijacking|T1055.003: Thread Execution Hijacking]]
    - [[T1055-process_injection#^t1055004-asynchronous-procedure-call|T1055.004: Asynchronous Procedure Call]]
    - [[T1055-process_injection#^t1055005-thread-local-storage|T1055.005: Thread Local Storage]]
    - [[T1055-process_injection#^t1055008-ptrace-system-calls|T1055.008: Ptrace System Calls]]
    - [[T1055-process_injection#^t1055009-proc-memory|T1055.009: Proc Memory]]
    - [[T1055-process_injection#^t1055011-extra-window-memory-injection|T1055.011: Extra Window Memory Injection]]
    - [[T1055-process_injection#^t1055012-process-hollowing|T1055.012: Process Hollowing]]
    - [[T1055-process_injection#^t1055013-process-doppelgänging|T1055.013: Process Doppelgänging]]
    - [[T1055-process_injection#^t1055014-vdso-hijacking|T1055.014: VDSO Hijacking]]
    - [[T1055-process_injection#^t1055015-listplanting|T1055.015: ListPlanting]]
- [[T1058-service_registry_permissions_weakness|T1058: Service Registry Permissions Weakness]]
- [[T1068-exploitation_for_privilege_escalation|T1068: Exploitation for Privilege Escalation]]
- [[T1078-valid_accounts|T1078: Valid Accounts]]
    - [[T1078-valid_accounts#^t1078001-default-accounts|T1078.001: Default Accounts]]
    - [[T1078-valid_accounts#^t1078002-domain-accounts|T1078.002: Domain Accounts]]
    - [[T1078-valid_accounts#^t1078003-local-accounts|T1078.003: Local Accounts]]
    - [[T1078-valid_accounts#^t1078004-cloud-accounts|T1078.004: Cloud Accounts]]
- [[T1088-bypass_user_account_control|T1088: Bypass User Account Control]]
- [[T1098-account_manipulation|T1098: Account Manipulation]]
    - [[T1098-account_manipulation#^t1098001-additional-cloud-credentials|T1098.001: Additional Cloud Credentials]]
    - [[T1098-account_manipulation#^t1098002-additional-email-delegate-permissions|T1098.002: Additional Email Delegate Permissions]]
    - [[T1098-account_manipulation#^t1098003-additional-cloud-roles|T1098.003: Additional Cloud Roles]]
    - [[T1098-account_manipulation#^t1098004-ssh-authorized-keys|T1098.004: SSH Authorized Keys]]
    - [[T1098-account_manipulation#^t1098005-device-registration|T1098.005: Device Registration]]
    - [[T1098-account_manipulation#^t1098006-additional-container-cluster-roles|T1098.006: Additional Container Cluster Roles]]
    - [[T1098-account_manipulation#^t1098007-additional-local-or-domain-groups|T1098.007: Additional Local or Domain Groups]]
- [[T1100-web_shell|T1100: Web Shell]]
- [[T1103-appinit_dlls|T1103: AppInit DLLs]]
- [[T1134-access_token_manipulation|T1134: Access Token Manipulation]]
    - [[T1134-access_token_manipulation#^t1134001-token-impersonation-theft|T1134.001: Token Impersonation/Theft]]
    - [[T1134-access_token_manipulation#^t1134002-create-process-with-token|T1134.002: Create Process with Token]]
    - [[T1134-access_token_manipulation#^t1134003-make-and-impersonate-token|T1134.003: Make and Impersonate Token]]
    - [[T1134-access_token_manipulation#^t1134004-parent-pid-spoofing|T1134.004: Parent PID Spoofing]]
    - [[T1134-access_token_manipulation#^t1134005-sid-history-injection|T1134.005: SID-History Injection]]
- [[T1138-application_shimming|T1138: Application Shimming]]
- [[T1150-plist_modification|T1150: Plist Modification]]
- [[T1157-dylib_hijacking|T1157: Dylib Hijacking]]
- [[T1160-launch_daemon|T1160: Launch Daemon]]
- [[T1165-startup_items|T1165: Startup Items]]
- [[T1166-setuid_and_setgid|T1166: Setuid and Setgid]]
- [[T1169-sudo|T1169: Sudo]]
- [[T1178-sid-history_injection|T1178: SID-History Injection]]
- [[T1179-hooking|T1179: Hooking]]
- [[T1181-extra_window_memory_injection|T1181: Extra Window Memory Injection]]
- [[T1182-appcert_dlls|T1182: AppCert DLLs]]
- [[T1183-image_file_execution_options_injection|T1183: Image File Execution Options Injection]]
- [[T1206-sudo_caching|T1206: Sudo Caching]]
- [[T1484-domain_or_tenant_policy_modification|T1484: Domain or Tenant Policy Modification]]
    - [[T1484-domain_or_tenant_policy_modification#^t1484001-group-policy-modification|T1484.001: Group Policy Modification]]
    - [[T1484-domain_or_tenant_policy_modification#^t1484002-trust-modification|T1484.002: Trust Modification]]
- [[T1502-parent_pid_spoofing|T1502: Parent PID Spoofing]]
- [[T1504-powershell_profile|T1504: PowerShell Profile]]
- [[T1514-elevated_execution_with_prompt|T1514: Elevated Execution with Prompt]]
- [[T1519-emond|T1519: Emond]]
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
- [[T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]
    - [[T1548-abuse_elevation_control_mechanism#^t1548001-setuid-and-setgid|T1548.001: Setuid and Setgid]]
    - [[T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]
    - [[T1548-abuse_elevation_control_mechanism#^t1548003-sudo-and-sudo-caching|T1548.003: Sudo and Sudo Caching]]
    - [[T1548-abuse_elevation_control_mechanism#^t1548004-elevated-execution-with-prompt|T1548.004: Elevated Execution with Prompt]]
    - [[T1548-abuse_elevation_control_mechanism#^t1548005-temporary-elevated-cloud-access|T1548.005: Temporary Elevated Cloud Access]]
    - [[T1548-abuse_elevation_control_mechanism#^t1548006-tcc-manipulation|T1548.006: TCC Manipulation]]
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
- [[T1611-escape_to_host|T1611: Escape to Host]]
