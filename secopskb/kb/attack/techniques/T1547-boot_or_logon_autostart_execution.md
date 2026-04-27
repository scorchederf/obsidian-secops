---
mitre_id: "T1547"
mitre_name: "Boot or Logon Autostart Execution"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--1ecb2399-e8ba-4f6b-8ba7-5c27d49405cf"
mitre_created: "2020-01-23T17:46:59.535Z"
mitre_modified: "2025-10-24T17:48:29.846Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1547/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
  - "Network Devices"
mitre_tactic_ids:
  - "TA0003"
  - "TA0004"
d3fend_ids:
  - "D3-AVE"
  - "D3-CF"
  - "D3-CI"
  - "D3-CM"
  - "D3-CQ"
  - "D3-DA"
  - "D3-DF"
  - "D3-EAL"
  - "D3-EDL"
  - "D3-EFA"
  - "D3-FA"
  - "D3-FE"
  - "D3-FEV"
  - "D3-FIM"
  - "D3-LFP"
  - "D3-RC"
  - "D3-RF"
  - "D3-RFAM"
  - "D3-RS"
  - "D3-SICA"
  - "D3-SU"
  - "D3-SWI"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may configure system settings to automatically execute a program during system boot or logon to maintain persistence or gain higher-level privileges on compromised systems. Operating systems may have mechanisms for automatically running a program on system boot or account logon.(Citation: Microsoft Run Key)(Citation: MSDN Authentication Packages)(Citation: Microsoft TimeProvider)(Citation: Cylance Reg Persistence Sept 2013)(Citation: Linux Kernel Programming) These mechanisms may include automatically executing programs that are placed in specially designated directories or are referenced by repositories that store configuration information, such as the Windows Registry. An adversary may achieve the same goal by modifying or extending features of the kernel.

Since some boot or logon autostart programs run with higher privileges, an adversary may leverage these to elevate privileges.

## Workspace

- [[workspaces/attack/techniques/T1547-boot_or_logon_autostart_execution-note|Open workspace note]]

![[workspaces/attack/techniques/T1547-boot_or_logon_autostart_execution-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### CAR Analytics

- [[kb/car/analytics/CAR-2013-01-002-autorun_differences|CAR-2013-01-002: Autorun Differences]]
- [[kb/car/analytics/CAR-2013-03-001-reg_exe_called_from_command_shell|CAR-2013-03-001: Reg.exe called from Command Shell]]
- [[kb/car/analytics/CAR-2020-05-003-rare_lolbas_command_lines|CAR-2020-05-003: Rare LolBAS Command Lines]]
- [[kb/car/analytics/CAR-2021-11-002-registry_edit_with_modification_of_userinit_shell_or_notify|CAR-2021-11-002: Registry Edit with Modification of Userinit, Shell or Notify]]
- [[kb/car/analytics/CAR-2021-12-002-modification_of_default_startup_folder_in_the_registry_key_common_startup|CAR-2021-12-002: Modification of Default Startup Folder in the Registry Key 'Common Startup']]

### Sigma Rules

- [[kb/sigma/rules/02ee49e2_e294_4d0f_9278_f5b3212fc588-new_run_key_pointing_to_suspicious_folder|New RUN Key Pointing to Suspicious Folder (high; windows / registry_set)]]
- [[kb/sigma/rules/106d7cbd_80ff_4985_b682_a7043e5acb72-loading_of_kernel_module_via_insmod|Loading of Kernel Module via Insmod (high; linux / auditd)]]
- [[kb/sigma/rules/277efb8f_60be_4f10_b4d3_037802f37167-registry_persistence_mechanisms_in_recycle_bin|Registry Persistence Mechanisms in Recycle Bin (high; windows / registry_event)]]
- [[kb/sigma/rules/28208707_fe31_437f_9a7f_4b1108b94d2e-suspicious_startup_folder_persistence|Suspicious Startup Folder Persistence (high; windows / file_event)]]
- [[kb/sigma/rules/318557a5_150c_4c8d_b70e_a9910e199857-file_creation_in_suspicious_directory_by_msdt_exe|File Creation In Suspicious Directory By Msdt.EXE (high; windows / file_event)]]
- [[kb/sigma/rules/46490193_1b22_4c29_bdd6_5bf63907216f-vbscript_payload_stored_in_registry|VBScript Payload Stored in Registry (high; windows / registry_set)]]
- [[kb/sigma/rules/509e84b9_a71a_40e0_834f_05470369bd1e-default_rdp_port_changed_to_non_standard_port|Default RDP Port Changed to Non Standard Port (high; windows / registry_set)]]
- [[kb/sigma/rules/674202d0_b22a_4af4_ae5f_2eda1f3da1af-bypass_uac_using_event_viewer|Bypass UAC Using Event Viewer (high; windows / registry_set)]]
- [[kb/sigma/rules/74a2b37d_fea4_41e0_9ac7_c9fbcf1f60cc-winrar_creating_files_in_startup_locations|WinRAR Creating Files in Startup Locations (high; windows / file_event)]]
- [[kb/sigma/rules/8c3c76ca_8f8b_4b1d_aaf3_81aebcd367c9-creation_exe_for_service_with_unquoted_path|Creation Exe for Service with Unquoted Path (high; windows / file_event)]]
- 15 more in the generated source index

### Atomic Tests

- [[kb/atomic/tests/04d55cef_f283_40ba_ae2a_316bc3b5e78c-hklm_re_execute_internet_explorer_core_fonts_stubpath_payload_by_decreasing_version_number|HKLM - re-execute 'Internet Explorer Core Fonts' StubPath payload by decreasing version number (powershell; windows)]]
- [[kb/atomic/tests/14fdc3f1_6fc3_4556_8d36_aa89d9d42d02-secedit_used_to_create_a_run_key_in_the_hklm_hive|secedit used to create a Run key in the HKLM Hive (command_prompt; windows)]]
- [[kb/atomic/tests/1d958c61_09c6_4d9e_b26b_4130314e520e-hklm_modify_default_system_shell_winlogon_shell_key_value|HKLM - Modify default System Shell - Winlogon Shell KEY Value  (powershell; windows)]]
- [[kb/atomic/tests/24e55612_85f6_4bd6_ae74_a73d02e3441d-add_executable_shortcut_link_to_user_startup_folder|Add Executable Shortcut Link to User Startup Folder (powershell; windows)]]
- [[kb/atomic/tests/29e0afca_8d1d_471a_8d34_25512fc48315-edit_an_existing_time_provider|Edit an existing time provider (powershell; windows)]]
- [[kb/atomic/tests/2cb98256_625e_4da9_9d44_f2e5f90b8bd5-suspicious_vbs_file_run_from_startup_folder|Suspicious vbs file run from startup Folder (powershell; windows)]]
- [[kb/atomic/tests/39e417dd_4fed_4d9c_ae3a_ba433b4d0e9a-hklm_add_malicious_stubpath_value_to_existing_active_setup_entry|HKLM - Add malicious StubPath value to existing Active Setup Entry (powershell; windows)]]
- [[kb/atomic/tests/554cbd88_cde1_4b56_8168_0be552eed9eb-reg_key_runonce|Reg Key RunOnce (command_prompt; windows)]]
- [[kb/atomic/tests/5b6768e4_44d2_44f0_89da_a01d1430fd5e-suspicious_bat_file_run_from_startup_folder|Suspicious bat file run from startup Folder (powershell; windows)]]
- [[kb/atomic/tests/5cb0b071_8a5a_412f_839d_116beb2ed9f7-driver_installation_using_pnputil_exe|Driver Installation Using pnputil.exe (powershell; windows)]]
- 40 more in the generated source index

### LOLBAS Entries

- [[kb/lolbas/entries/osbinaries-pnputil_exe|Pnputil.exe (Execute)]]
- [[kb/lolbas/entries/othermsbinaries-update_exe|Update.exe (Download, AWL Bypass, Execute)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0003-persistence|TA0003: Persistence]]
- [[TA0004-privilege_escalation|TA0004: Privilege Escalation]]

## D3FEND

- [[D3-AVE-asset_vulnerability_enumeration|D3-AVE: Asset Vulnerability Enumeration]]
- [[D3-CF-content_filtering|D3-CF: Content Filtering]]
- [[D3-CI-configuration_inventory|D3-CI: Configuration Inventory]]
- [[D3-CM-content_modification|D3-CM: Content Modification]]
- [[D3-CQ-content_quarantine|D3-CQ: Content Quarantine]]
- [[D3-DA-dynamic_analysis|D3-DA: Dynamic Analysis]]
- [[D3-DF-decoy_file|D3-DF: Decoy File]]
- [[D3-EAL-executable_allowlisting|D3-EAL: Executable Allowlisting]]
- [[D3-EDL-executable_denylisting|D3-EDL: Executable Denylisting]]
- [[D3-EFA-emulated_file_analysis|D3-EFA: Emulated File Analysis]]
- [[D3-FA-file_analysis|D3-FA: File Analysis]]
- [[D3-FE-file_encryption|D3-FE: File Encryption]]
- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]
- [[D3-FIM-file_integrity_monitoring|D3-FIM: File Integrity Monitoring]]
- [[D3-LFP-local_file_permissions|D3-LFP: Local File Permissions]]
- [[D3-RC-restore_configuration|D3-RC: Restore Configuration]]
- [[D3-RF-restore_file|D3-RF: Restore File]]
- [[D3-RFAM-remote_file_access_mediation|D3-RFAM: Remote File Access Mediation]]
- [[D3-RS-restore_software|D3-RS: Restore Software]]
- [[D3-SICA-system_init_config_analysis|D3-SICA: System Init Config Analysis]]
- [[D3-SU-software_update|D3-SU: Software Update]]
- [[D3-SWI-software_inventory|D3-SWI: Software Inventory]]

## Subtechniques

### T1547.001: Registry Run Keys / Startup Folder

^t1547001-registry-run-keys---startup-folder

Adversaries may achieve persistence by adding a program to a startup folder or referencing it with a Registry run key. Adding an entry to the "run keys" in the Registry or startup folder will cause the program referenced to be executed when a user logs in.(Citation: Microsoft Run Key) These programs will be executed under the context of the user and will have the account's associated permissions level.

The following run keys are created by default on Windows systems:

* `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`
* `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce`
* `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run`
* `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce`

Run keys may exist under multiple hives.(Citation: Microsoft Wow6432Node 2018)(Citation: Malwarebytes Wow6432Node 2016) The `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnceEx` is also available but is not created by default on Windows Vista and newer. Registry run key entries can reference programs directly or list them as a dependency.(Citation: Microsoft Run Key) For example, it is possible to load a DLL at logon using a "Depend" key with RunOnceEx: `reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnceEx\0001\Depend /v 1 /d "C:\temp\evil[.]dll"` (Citation: Oddvar Moe RunOnceEx Mar 2018)

Placing a program within a startup folder will also cause that program to execute when a user logs in. There is a startup folder location for individual user accounts as well as a system-wide startup folder that will be checked regardless of which user account logs in. The startup folder path for the current user is `C:\Users\\[Username]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`. The startup folder path for all users is `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`.

The following Registry keys can be used to set startup folder items for persistence:

* `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders`
* `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders`
* `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders`
* `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders`

The following Registry keys can control automatic startup of services during boot:

* `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce`
* `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce`
* `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunServices`
* `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunServices`

Using policy settings to specify startup programs creates corresponding values in either of two Registry keys:

* `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run`
* `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run`

Programs listed in the load value of the registry key `HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\Windows` run automatically for the currently logged-on user.

By default, the multistring `BootExecute` value of the registry key `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager` is set to `autocheck autochk *`. This value causes Windows, at startup, to check the file-system integrity of the hard disks if the system has been shut down abnormally. Adversaries can add other programs or processes to this registry value which will automatically launch at boot.

Adversaries can use these configuration locations to execute malware, such as remote access tools, to maintain persistence through system reboots. Adversaries may also use [[T1036-masquerading|T1036: Masquerading]] to make the Registry entries look as if they are associated with legitimate programs.

### T1547.002: Authentication Package

^t1547002-authentication-package

Adversaries may abuse authentication packages to execute DLLs when the system boots. Windows authentication package DLLs are loaded by the Local Security Authority (LSA) process at system start. They provide support for multiple logon processes and multiple security protocols to the operating system.(Citation: MSDN Authentication Packages)

Adversaries can use the autostart mechanism provided by LSA authentication packages for persistence by placing a reference to a binary in the Windows Registry location `HKLM\SYSTEM\CurrentControlSet\Control\Lsa\` with the key value of `"Authentication Packages"=&lt;target binary&gt;`. The binary will then be executed by the system when the authentication packages are loaded.

### T1547.003: Time Providers

^t1547003-time-providers

Adversaries may abuse time providers to execute DLLs when the system boots. The Windows Time service (W32Time) enables time synchronization across and within domains.(Citation: Microsoft W32Time Feb 2018) W32Time time providers are responsible for retrieving time stamps from hardware/network resources and outputting these values to other network clients.(Citation: Microsoft TimeProvider)

Time providers are implemented as dynamic-link libraries (DLLs) that are registered in the subkeys of `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\W32Time\TimeProviders\`.(Citation: Microsoft TimeProvider) The time provider manager, directed by the service control manager, loads and starts time providers listed and enabled under this key at system startup and/or whenever parameters are changed.(Citation: Microsoft TimeProvider)

Adversaries may abuse this architecture to establish persistence, specifically by creating a new arbitrarily named subkey  pointing to a malicious DLL in the `DllName` value. Administrator privileges are required for time provider registration, though execution will run in context of the Local Service account.(Citation: Github W32Time Oct 2017)

### T1547.004: Winlogon Helper DLL

^t1547004-winlogon-helper-dll

Adversaries may abuse features of Winlogon to execute DLLs and/or executables when a user logs in. Winlogon.exe is a Windows component responsible for actions at logon/logoff as well as the secure attention sequence (SAS) triggered by Ctrl-Alt-Delete. Registry entries in `HKLM\Software[\\Wow6432Node\\]\Microsoft\Windows NT\CurrentVersion\Winlogon\` and `HKCU\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\` are used to manage additional helper programs and functionalities that support Winlogon.(Citation: Cylance Reg Persistence Sept 2013) 

Malicious modifications to these Registry keys may cause Winlogon to load and execute malicious DLLs and/or executables. Specifically, the following subkeys have been known to be possibly vulnerable to abuse: (Citation: Cylance Reg Persistence Sept 2013)

* Winlogon\Notify - points to notification package DLLs that handle Winlogon events
* Winlogon\Userinit - points to userinit.exe, the user initialization program executed when a user logs on
* Winlogon\Shell - points to explorer.exe, the system shell executed when a user logs on

Adversaries may take advantage of these features to repeatedly execute malicious code and establish persistence.

### T1547.005: Security Support Provider

^t1547005-security-support-provider

Adversaries may abuse security support providers (SSPs) to execute DLLs when the system boots. Windows SSP DLLs are loaded into the Local Security Authority (LSA) process at system start. Once loaded into the LSA, SSP DLLs have access to encrypted and plaintext passwords that are stored in Windows, such as any logged-on user's Domain password or smart card PINs.

The SSP configuration is stored in two Registry keys: `HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Security Packages` and `HKLM\SYSTEM\CurrentControlSet\Control\Lsa\OSConfig\Security Packages`. An adversary may modify these Registry keys to add new SSPs, which will be loaded the next time the system boots, or when the AddSecurityPackage Windows API function is called.(Citation: Graeber 2014)

### T1547.006: Kernel Modules and Extensions

^t1547006-kernel-modules-and-extensions

Adversaries may modify the kernel to automatically execute programs on system boot. Loadable Kernel Modules (LKMs) are pieces of code that can be loaded and unloaded into the kernel upon demand. They extend the functionality of the kernel without the need to reboot the system. For example, one type of module is the device driver, which allows the kernel to access hardware connected to the system.(Citation: Linux Kernel Programming) 

When used maliciously, LKMs can be a type of kernel-mode [[T1014-rootkit|T1014: Rootkit]] that run with the highest operating system privilege (Ring 0).(Citation: Linux Kernel Module Programming Guide) Common features of LKM based rootkits include: hiding itself, selective hiding of files, processes and network activity, as well as log tampering, providing authenticated backdoors, and enabling root access to non-privileged users.(Citation: iDefense Rootkit Overview)

Kernel extensions, also called kext, are used in macOS to load functionality onto a system similar to LKMs for Linux. Since the kernel is responsible for enforcing security and the kernel extensions run as apart of the kernel, kexts are not governed by macOS security policies. Kexts are loaded and unloaded through `kextload` and `kextunload` commands. Kexts need to be signed with a developer ID that is granted privileges by Apple allowing it to sign Kernel extensions. Developers without these privileges may still sign kexts but they will not load unless SIP is disabled. If SIP is enabled, the kext signature is verified before being added to the AuxKC.(Citation: System and kernel extensions in macOS)

Since macOS Catalina 10.15, kernel extensions have been deprecated in favor of System Extensions. However, kexts are still allowed as "Legacy System Extensions" since there is no System Extension for Kernel Programming Interfaces.(Citation: Apple Kernel Extension Deprecation)

Adversaries can use LKMs and kexts to conduct [[TA0003-persistence|TA0003: Persistence]] and/or [[TA0004-privilege_escalation|TA0004: Privilege Escalation]] on a system. Examples have been found in the wild, and there are some relevant open source projects as well.(Citation: Volatility Phalanx2)(Citation: CrowdStrike Linux Rootkit)(Citation: GitHub Reptile)(Citation: GitHub Diamorphine)(Citation: RSAC 2015 San Francisco Patrick Wardle)(Citation: Synack Secure Kernel Extension Broken)(Citation: Securelist Ventir)(Citation: Trend Micro Skidmap)

### T1547.007: Re-opened Applications

^t1547007-re-opened-applications

Adversaries may modify plist files to automatically run an application when a user logs in. When a user logs out or restarts via the macOS Graphical User Interface (GUI), a prompt is provided to the user with a checkbox to "Reopen windows when logging back in".(Citation: Re-Open windows on Mac) When selected, all applications currently open are added to a property list file named `com.apple.loginwindow.[UUID].plist` within the `~/Library/Preferences/ByHost` directory.(Citation: Methods of Mac Malware Persistence)(Citation: Wardle Persistence Chapter) Applications listed in this file are automatically reopened upon the user’s next logon.

Adversaries can establish [[TA0003-persistence|TA0003: Persistence]] by adding a malicious application path to the `com.apple.loginwindow.[UUID].plist` file to execute payloads when a user logs in.

### T1547.008: LSASS Driver

^t1547008-lsass-driver

Adversaries may modify or add LSASS drivers to obtain persistence on compromised systems. The Windows security subsystem is a set of components that manage and enforce the security policy for a computer or domain. The Local Security Authority (LSA) is the main component responsible for local security policy and user authentication. The LSA includes multiple dynamic link libraries (DLLs) associated with various other security functions, all of which run in the context of the LSA Subsystem Service (LSASS) lsass.exe process.(Citation: Microsoft Security Subsystem)

Adversaries may target LSASS drivers to obtain persistence. By either replacing or adding illegitimate drivers (e.g., [[T1574-hijack_execution_flow|T1574: Hijack Execution Flow]]), an adversary can use LSA operations to continuously execute malicious payloads.

### T1547.009: Shortcut Modification

^t1547009-shortcut-modification

Adversaries may create or modify shortcuts that can execute a program during system boot or user login. Shortcuts or symbolic links are used to reference other files or programs that will be opened or executed when the shortcut is clicked or executed by a system startup process.

Adversaries may abuse shortcuts in the startup folder to execute their tools and achieve persistence.(Citation: Shortcut for Persistence ) Although often used as payloads in an infection chain (e.g. [[T1566-phishing#^t1566001-spearphishing-attachment|T1566.001: Spearphishing Attachment]]), adversaries may also create a new shortcut as a means of indirection, while also abusing [[T1036-masquerading|T1036: Masquerading]] to make the malicious shortcut appear as a legitimate program. Adversaries can also edit the target path or entirely replace an existing shortcut so their malware will be executed instead of the intended legitimate program.

Shortcuts can also be abused to establish persistence by implementing other methods. For example, LNK browser extensions may be modified (e.g. [[T1176-software_extensions#^t1176001-browser-extensions|T1176.001: Browser Extensions]]) to persistently launch malware.

### T1547.010: Port Monitors

^t1547010-port-monitors

Adversaries may use port monitors to run an adversary supplied DLL during system boot for persistence or privilege escalation. A port monitor can be set through the `AddMonitor` API call to set a DLL to be loaded at startup.(Citation: AddMonitor) This DLL can be located in `C:\Windows\System32` and will be loaded and run by the print spooler service, `spoolsv.exe`, under SYSTEM level permissions on boot.(Citation: Bloxham) 

Alternatively, an arbitrary DLL can be loaded if permissions allow writing a fully-qualified pathname for that DLL to the `Driver` value of an existing or new arbitrarily named subkey of `HKLM\SYSTEM\CurrentControlSet\Control\Print\Monitors`. The Registry key contains entries for the following:

* Local Port
* Standard TCP/IP Port
* USB Monitor
* WSD Port


### T1547.012: Print Processors

^t1547012-print-processors

Adversaries may abuse print processors to run malicious DLLs during system boot for persistence and/or privilege escalation. Print processors are DLLs that are loaded by the print spooler service, `spoolsv.exe`, during boot.(Citation: Microsoft Intro Print Processors)

Adversaries may abuse the print spooler service by adding print processors that load malicious DLLs at startup. A print processor can be installed through the `AddPrintProcessor` API call with an account that has `SeLoadDriverPrivilege` enabled. Alternatively, a print processor can be registered to the print spooler service by adding the `HKLM\SYSTEM\\[CurrentControlSet or ControlSet001]\Control\Print\Environments\\[Windows architecture: e.g., Windows x64]\Print Processors\\[user defined]\Driver` Registry key that points to the DLL.

For the malicious print processor to be correctly installed, the payload must be located in the dedicated system print-processor directory, that can be found with the `GetPrintProcessorDirectory` API call, or referenced via a relative path from this directory.(Citation: Microsoft AddPrintProcessor May 2018) After the print processors are installed, the print spooler service, which starts during boot, must be restarted in order for them to run.(Citation: ESET PipeMon May 2020)

The print spooler service runs under SYSTEM level permissions, therefore print processors installed by an adversary may run under elevated privileges.

### T1547.013: XDG Autostart Entries

^t1547013-xdg-autostart-entries

Adversaries may add or modify XDG Autostart Entries to execute malicious programs or commands when a user’s desktop environment is loaded at login. XDG Autostart entries are available for any XDG-compliant Linux system. XDG Autostart entries use Desktop Entry files (`.desktop`) to configure the user’s desktop environment upon user login. These configuration files determine what applications launch upon user login, define associated applications to open specific file types, and define applications used to open removable media.(Citation: Free Desktop Application Autostart Feb 2006)(Citation: Free Desktop Entry Keys)

Adversaries may abuse this feature to establish persistence by adding a path to a malicious binary or command to the `Exec` directive in the `.desktop` configuration file. When the user’s desktop environment is loaded at user login, the `.desktop` files located in the XDG Autostart directories are automatically executed. System-wide Autostart entries are located in the `/etc/xdg/autostart` directory while the user entries are located in the `~/.config/autostart` directory.

Adversaries may combine this technique with [[T1036-masquerading|T1036: Masquerading]] to blend malicious Autostart entries with legitimate programs.(Citation: Red Canary Netwire Linux 2022)

### T1547.014: Active Setup

^t1547014-active-setup

Adversaries may achieve persistence by adding a Registry key to the Active Setup of the local machine. Active Setup is a Windows mechanism that is used to execute programs when a user logs in. The value stored in the Registry key will be executed after a user logs into the computer.(Citation: Klein Active Setup 2010) These programs will be executed under the context of the user and will have the account's associated permissions level.

Adversaries may abuse Active Setup by creating a key under `HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components\` and setting a malicious value for `StubPath`. This value will serve as the program that will be executed when a user logs into the computer.(Citation: Mandiant Glyer APT 2010)(Citation: Citizenlab Packrat 2015)(Citation: FireEye CFR Watering Hole 2012)(Citation: SECURELIST Bright Star 2015)(Citation: paloalto Tropic Trooper 2016)

Adversaries can abuse these components to execute malware, such as remote access tools, to maintain persistence through system reboots. Adversaries may also use [[T1036-masquerading|T1036: Masquerading]] to make the Registry entries look as if they are associated with legitimate programs.

### T1547.015: Login Items

^t1547015-login-items

Adversaries may add login items to execute upon user login to gain persistence or escalate privileges. Login items are applications, documents, folders, or server connections that are automatically launched when a user logs in.(Citation: Open Login Items Apple) Login items can be added via a shared file list or Service Management Framework.(Citation: Adding Login Items) Shared file list login items can be set using scripting languages such as [[T1059-command_and_scripting_interpreter#^t1059002-applescript|T1059.002: AppleScript]], whereas the Service Management Framework uses the API call `SMLoginItemSetEnabled`.

Login items installed using the Service Management Framework leverage `launchd`, are not visible in the System Preferences, and can only be removed by the application that created them.(Citation: Adding Login Items)(Citation: SMLoginItemSetEnabled Schroeder 2013) Login items created using a shared file list are visible in System Preferences, can hide the application when it launches, and are executed through LaunchServices, not launchd, to open applications, documents, or URLs without using Finder.(Citation: Launch Services Apple Developer) Users and applications use login items to configure their user environment to launch commonly used services or applications, such as email, chat, and music applications.

Adversaries can utilize [[T1059-command_and_scripting_interpreter#^t1059002-applescript|T1059.002: AppleScript]] and [[T1106-native_api|T1106: Native API]] calls to create a login item to spawn malicious executables.(Citation: ELC Running at startup) Prior to version 10.5 on macOS, adversaries can add login items by using [[T1059-command_and_scripting_interpreter#^t1059002-applescript|T1059.002: AppleScript]] to send an Apple events to the “System Events” process, which has an AppleScript dictionary for manipulating login items.(Citation: Login Items AE) Adversaries can use a command such as `tell application “System Events” to make login item at end with properties /path/to/executable`.(Citation: Startup Items Eclectic)(Citation: hexed osx.dok analysis 2019)(Citation: Add List Remove Login Items Apple Script) This command adds the path of the malicious executable to the login item file list located in `~/Library/Application Support/com.apple.backgroundtaskmanagementagent/backgrounditems.btm`.(Citation: Startup Items Eclectic) Adversaries can also use login items to launch executables that can be used to control the victim system remotely or as a means to gain privilege escalation by prompting for user credentials.(Citation: objsee mac malware 2017)(Citation: CheckPoint Dok)(Citation: objsee netwire backdoor 2019)

## Platforms

- Linux
- macOS
- Windows
- Network Devices

