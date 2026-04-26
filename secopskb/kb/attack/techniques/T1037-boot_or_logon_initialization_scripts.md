---
mitre_id: "T1037"
mitre_name: "Boot or Logon Initialization Scripts"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--03259939-0b57-482f-8eb5-87c0e0d54334"
mitre_created: "2017-05-31T21:30:38.910Z"
mitre_modified: "2025-10-24T17:48:20.077Z"
mitre_version: "2.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1037/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "macOS"
  - "Windows"
  - "Linux"
  - "Network Devices"
  - "ESXi"
mitre_tactic_ids:
  - "TA0003"
  - "TA0004"
d3fend_ids:
  - "D3-CF"
  - "D3-CI"
  - "D3-CM"
  - "D3-CQ"
  - "D3-DA"
  - "D3-DF"
  - "D3-DNR"
  - "D3-EAL"
  - "D3-EDL"
  - "D3-EFA"
  - "D3-FA"
  - "D3-FE"
  - "D3-FEV"
  - "D3-FIM"
  - "D3-LFP"
  - "D3-NRAM"
  - "D3-RC"
  - "D3-RF"
  - "D3-RFAM"
  - "D3-SICA"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may use scripts automatically executed at boot or logon initialization to establish persistence.(Citation: Mandiant APT29 Eye Spy Email Nov 22)(Citation: Anomali Rocke March 2019) Initialization scripts can be used to perform administrative functions, which may often execute other programs or send information to an internal logging server. These scripts can vary based on operating system and whether applied locally or remotely.  

Adversaries may use these scripts to maintain persistence on a single system. Depending on the access configuration of the logon scripts, either local credentials or an administrator account may be necessary. 

An adversary may also be able to escalate their privileges since some boot or logon initialization scripts run with higher privileges.

## Workspace

- [[workspaces/attack/techniques/T1037-boot_or_logon_initialization_scripts-note|Open workspace note]]

![[workspaces/attack/techniques/T1037-boot_or_logon_initialization_scripts-note]]

## Tactics

- [[TA0003-persistence|TA0003: Persistence]]
- [[TA0004-privilege_escalation|TA0004: Privilege Escalation]]

## D3FEND

- [[D3-CF-content_filtering|D3-CF: Content Filtering]]
- [[D3-CI-configuration_inventory|D3-CI: Configuration Inventory]]
- [[D3-CM-content_modification|D3-CM: Content Modification]]
- [[D3-CQ-content_quarantine|D3-CQ: Content Quarantine]]
- [[D3-DA-dynamic_analysis|D3-DA: Dynamic Analysis]]
- [[D3-DF-decoy_file|D3-DF: Decoy File]]
- [[D3-DNR-decoy_network_resource|D3-DNR: Decoy Network Resource]]
- [[D3-EAL-executable_allowlisting|D3-EAL: Executable Allowlisting]]
- [[D3-EDL-executable_denylisting|D3-EDL: Executable Denylisting]]
- [[D3-EFA-emulated_file_analysis|D3-EFA: Emulated File Analysis]]
- [[D3-FA-file_analysis|D3-FA: File Analysis]]
- [[D3-FE-file_encryption|D3-FE: File Encryption]]
- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]
- [[D3-FIM-file_integrity_monitoring|D3-FIM: File Integrity Monitoring]]
- [[D3-LFP-local_file_permissions|D3-LFP: Local File Permissions]]
- [[D3-NRAM-network_resource_access_mediation|D3-NRAM: Network Resource Access Mediation]]
- [[D3-RC-restore_configuration|D3-RC: Restore Configuration]]
- [[D3-RF-restore_file|D3-RF: Restore File]]
- [[D3-RFAM-remote_file_access_mediation|D3-RFAM: Remote File Access Mediation]]
- [[D3-SICA-system_init_config_analysis|D3-SICA: System Init Config Analysis]]

## Subtechniques

### T1037.001: Logon Script (Windows)

^t1037001-logon-script-(windows)

Adversaries may use Windows logon scripts automatically executed at logon initialization to establish persistence. Windows allows logon scripts to be run whenever a specific user or group of users log into a system.(Citation: TechNet Logon Scripts) This is done via adding a path to a script to the `HKCU\Environment\UserInitMprLogonScript` Registry key.(Citation: Hexacorn Logon Scripts)

Adversaries may use these scripts to maintain persistence on a single system. Depending on the access configuration of the logon scripts, either local credentials or an administrator account may be necessary. 

### T1037.002: Login Hook

^t1037002-login-hook

Adversaries may use a Login Hook to establish persistence executed upon user logon. A login hook is a plist file that points to a specific script to execute with root privileges upon user logon. The plist file is located in the `/Library/Preferences/com.apple.loginwindow.plist` file and can be modified using the `defaults` command-line utility. This behavior is the same for logout hooks where a script can be executed upon user logout. All hooks require administrator permissions to modify or create hooks.(Citation: Login Scripts Apple Dev)(Citation: LoginWindowScripts Apple Dev) 

Adversaries can add or insert a path to a malicious script in the `com.apple.loginwindow.plist` file, using the `LoginHook` or `LogoutHook` key-value pair. The malicious script is executed upon the next user login. If a login hook already exists, adversaries can add additional commands to an existing login hook. There can be only one login and logout hook on a system at a time.(Citation: S1 macOs Persistence)(Citation: Wardle Persistence Chapter)

**Note:** Login hooks were deprecated in 10.11 version of macOS in favor of [[T1543-create_or_modify_system_process#^t1543004-launch-daemon|T1543.004: Launch Daemon]] and [[T1543-create_or_modify_system_process#^t1543001-launch-agent|T1543.001: Launch Agent]] 

### T1037.003: Network Logon Script

^t1037003-network-logon-script

Adversaries may use network logon scripts automatically executed at logon initialization to establish persistence. Network logon scripts can be assigned using Active Directory or Group Policy Objects.(Citation: Petri Logon Script AD) These logon scripts run with the privileges of the user they are assigned to. Depending on the systems within the network, initializing one of these scripts could apply to more than one or potentially all systems.  
 
Adversaries may use these scripts to maintain persistence on a network. Depending on the access configuration of the logon scripts, either local credentials or an administrator account may be necessary.

### T1037.004: RC Scripts

^t1037004-rc-scripts

Adversaries may establish persistence by modifying RC scripts, which are executed during a Unix-like system’s startup. These files allow system administrators to map and start custom services at startup for different run levels. RC scripts require root privileges to modify.

Adversaries may establish persistence by adding a malicious binary path or shell commands to `rc.local`, `rc.common`, and other RC scripts specific to the Unix-like distribution.(Citation: IranThreats Kittens Dec 2017)(Citation: Intezer HiddenWasp Map 2019) Upon reboot, the system executes the script's contents as root, resulting in persistence.

Adversary abuse of RC scripts is especially effective for lightweight Unix-like distributions using the root user as default, such as ESXi hypervisors, IoT, or embedded systems.(Citation: intezer-kaiji-malware) As ESXi servers store most system files in memory and therefore discard changes on shutdown, leveraging `/etc/rc.local.d/local.sh` is one of the few mechanisms for enabling persistence across reboots.(Citation: Juniper Networks ESXi Backdoor 2022)

Several Unix-like systems have moved to Systemd and deprecated the use of RC scripts. This is now a deprecated mechanism in macOS in favor of Launchd.(Citation: Apple Developer Doco Archive Launchd)(Citation: Startup Items) This technique can be used on Mac OS X Panther v10.3 and earlier versions which still execute the RC scripts.(Citation: Methods of Mac Malware Persistence) To maintain backwards compatibility some systems, such as Ubuntu, will execute the RC scripts if they exist with the correct file permissions.(Citation: Ubuntu Manpage systemd rc)

### T1037.005: Startup Items

^t1037005-startup-items

Adversaries may use startup items automatically executed at boot initialization to establish persistence. Startup items execute during the final phase of the boot process and contain shell scripts or other executable files along with configuration information used by the system to determine the execution order for all startup items.(Citation: Startup Items)

This is technically a deprecated technology (superseded by [[T1543-create_or_modify_system_process#^t1543004-launch-daemon|T1543.004: Launch Daemon]]), and thus the appropriate folder, `/Library/StartupItems` isn’t guaranteed to exist on the system by default, but does appear to exist by default on macOS Sierra. A startup item is a directory whose executable and configuration property list (plist), `StartupParameters.plist`, reside in the top-level directory. 

An adversary can create the appropriate folders/files in the StartupItems directory to register their own persistence mechanism.(Citation: Methods of Mac Malware Persistence) Additionally, since StartupItems run during the bootup phase of macOS, they will run as the elevated root user.

## Mitigations

- [[M1022-restrict_file_and_directory_permissions|M1022: Restrict File and Directory Permissions]]
- [[M1024-restrict_registry_permissions|M1024: Restrict Registry Permissions]]

## Platforms

- macOS
- Windows
- Linux
- Network Devices
- ESXi

