---
id: T1037
name: Boot or Logon Initialization Scripts
created: 2017-05-31 21:30:38.910000+00:00
modified: 2025-10-24 17:48:20.077000+00:00
type: attack-pattern
x_mitre_version: 2.4
x_mitre_domains: enterprise-attack
---

## Tactic

- [[privilege_escalation|Privilege Escalation]]

Adversaries may use scripts automatically executed at boot or logon initialization to establish persistence.(Citation: Mandiant APT29 Eye Spy Email Nov 22)(Citation: Anomali Rocke March 2019) Initialization scripts can be used to perform administrative functions, which may often execute other programs or send information to an internal logging server. These scripts can vary based on operating system and whether applied locally or remotely.  

Adversaries may use these scripts to maintain persistence on a single system. Depending on the access configuration of the logon scripts, either local credentials or an administrator account may be necessary. 

An adversary may also be able to escalate their privileges since some boot or logon initialization scripts run with higher privileges.

## Subtechniques

### T1037.001: Logon Script (Windows)
^t1037001-logon-script-(windows)

**Parent Technique**
- [[T1037-boot_or_logon_initialization_scripts|T1037: Boot or Logon Initialization Scripts]]

**Tactic**
- [[privilege_escalation|Privilege Escalation]]

Adversaries may use Windows logon scripts automatically executed at logon initialization to establish persistence. Windows allows logon scripts to be run whenever a specific user or group of users log into a system.(Citation: TechNet Logon Scripts) This is done via adding a path to a script to the <code>HKCU\Environment\UserInitMprLogonScript</code> Registry key.(Citation: Hexacorn Logon Scripts)

Adversaries may use these scripts to maintain persistence on a single system. Depending on the access configuration of the logon scripts, either local credentials or an administrator account may be necessary. 

#### Properties

- id: T1037.001
- name: Logon Script (Windows)
- created: 2020-01-10 03:43:37.211000+00:00
- modified: 2025-10-24 17:49:33.610000+00:00
- type: attack-pattern
- x_mitre_version: 1.0
- x_mitre_domains: enterprise-attack

### T1037.002: Login Hook
^t1037002-login-hook

**Parent Technique**
- [[T1037-boot_or_logon_initialization_scripts|T1037: Boot or Logon Initialization Scripts]]

**Tactic**
- [[privilege_escalation|Privilege Escalation]]

Adversaries may use a Login Hook to establish persistence executed upon user logon. A login hook is a plist file that points to a specific script to execute with root privileges upon user logon. The plist file is located in the <code>/Library/Preferences/com.apple.loginwindow.plist</code> file and can be modified using the <code>defaults</code> command-line utility. This behavior is the same for logout hooks where a script can be executed upon user logout. All hooks require administrator permissions to modify or create hooks.(Citation: Login Scripts Apple Dev)(Citation: LoginWindowScripts Apple Dev) 

Adversaries can add or insert a path to a malicious script in the <code>com.apple.loginwindow.plist</code> file, using the <code>LoginHook</code> or <code>LogoutHook</code> key-value pair. The malicious script is executed upon the next user login. If a login hook already exists, adversaries can add additional commands to an existing login hook. There can be only one login and logout hook on a system at a time.(Citation: S1 macOs Persistence)(Citation: Wardle Persistence Chapter)

**Note:** Login hooks were deprecated in 10.11 version of macOS in favor of [Launch Daemon](https://attack.mitre.org/techniques/T1543/004) and [Launch Agent](https://attack.mitre.org/techniques/T1543/001) 

#### Properties

- id: T1037.002
- name: Login Hook
- created: 2020-01-10 16:01:15.995000+00:00
- modified: 2025-10-24 17:48:42.963000+00:00
- type: attack-pattern
- x_mitre_version: 2.0
- x_mitre_domains: enterprise-attack

### T1037.003: Network Logon Script
^t1037003-network-logon-script

**Parent Technique**
- [[T1037-boot_or_logon_initialization_scripts|T1037: Boot or Logon Initialization Scripts]]

**Tactic**
- [[privilege_escalation|Privilege Escalation]]

Adversaries may use network logon scripts automatically executed at logon initialization to establish persistence. Network logon scripts can be assigned using Active Directory or Group Policy Objects.(Citation: Petri Logon Script AD) These logon scripts run with the privileges of the user they are assigned to. Depending on the systems within the network, initializing one of these scripts could apply to more than one or potentially all systems.  
 
Adversaries may use these scripts to maintain persistence on a network. Depending on the access configuration of the logon scripts, either local credentials or an administrator account may be necessary.

#### Properties

- id: T1037.003
- name: Network Logon Script
- created: 2020-01-10 18:01:03.666000+00:00
- modified: 2025-10-24 17:49:21.921000+00:00
- type: attack-pattern
- x_mitre_version: 1.0
- x_mitre_domains: enterprise-attack

### T1037.004: RC Scripts
^t1037004-rc-scripts

**Parent Technique**
- [[T1037-boot_or_logon_initialization_scripts|T1037: Boot or Logon Initialization Scripts]]

**Tactic**
- [[privilege_escalation|Privilege Escalation]]

Adversaries may establish persistence by modifying RC scripts, which are executed during a Unix-like system’s startup. These files allow system administrators to map and start custom services at startup for different run levels. RC scripts require root privileges to modify.

Adversaries may establish persistence by adding a malicious binary path or shell commands to <code>rc.local</code>, <code>rc.common</code>, and other RC scripts specific to the Unix-like distribution.(Citation: IranThreats Kittens Dec 2017)(Citation: Intezer HiddenWasp Map 2019) Upon reboot, the system executes the script's contents as root, resulting in persistence.

Adversary abuse of RC scripts is especially effective for lightweight Unix-like distributions using the root user as default, such as ESXi hypervisors, IoT, or embedded systems.(Citation: intezer-kaiji-malware) As ESXi servers store most system files in memory and therefore discard changes on shutdown, leveraging `/etc/rc.local.d/local.sh` is one of the few mechanisms for enabling persistence across reboots.(Citation: Juniper Networks ESXi Backdoor 2022)

Several Unix-like systems have moved to Systemd and deprecated the use of RC scripts. This is now a deprecated mechanism in macOS in favor of Launchd.(Citation: Apple Developer Doco Archive Launchd)(Citation: Startup Items) This technique can be used on Mac OS X Panther v10.3 and earlier versions which still execute the RC scripts.(Citation: Methods of Mac Malware Persistence) To maintain backwards compatibility some systems, such as Ubuntu, will execute the RC scripts if they exist with the correct file permissions.(Citation: Ubuntu Manpage systemd rc)

#### Properties

- id: T1037.004
- name: RC Scripts
- created: 2020-01-15 16:25:22.260000+00:00
- modified: 2025-10-24 17:49:28.955000+00:00
- type: attack-pattern
- x_mitre_version: 2.2
- x_mitre_domains: enterprise-attack

### T1037.005: Startup Items
^t1037005-startup-items

**Parent Technique**
- [[T1037-boot_or_logon_initialization_scripts|T1037: Boot or Logon Initialization Scripts]]

**Tactic**
- [[privilege_escalation|Privilege Escalation]]

Adversaries may use startup items automatically executed at boot initialization to establish persistence. Startup items execute during the final phase of the boot process and contain shell scripts or other executable files along with configuration information used by the system to determine the execution order for all startup items.(Citation: Startup Items)

This is technically a deprecated technology (superseded by [Launch Daemon](https://attack.mitre.org/techniques/T1543/004)), and thus the appropriate folder, <code>/Library/StartupItems</code> isn’t guaranteed to exist on the system by default, but does appear to exist by default on macOS Sierra. A startup item is a directory whose executable and configuration property list (plist), <code>StartupParameters.plist</code>, reside in the top-level directory. 

An adversary can create the appropriate folders/files in the StartupItems directory to register their own persistence mechanism.(Citation: Methods of Mac Malware Persistence) Additionally, since StartupItems run during the bootup phase of macOS, they will run as the elevated root user.

#### Properties

- id: T1037.005
- name: Startup Items
- created: 2020-01-15 18:00:33.603000+00:00
- modified: 2025-10-24 17:49:19.678000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1022-restrict_file_and_directory_permissions|M1022: Restrict File and Directory Permissions]]
- [[M1024-restrict_registry_permissions|M1024: Restrict Registry Permissions]]

## Platforms

- macOS
- Windows
- Linux
- Network Devices
- ESXi

## Tools


