---
id: T1070
name: Indicator Removal
created: 2017-05-31 21:30:55.892000+00:00
modified: 2025-10-24 17:48:59.237000+00:00
type: attack-pattern
x_mitre_version: 2.4
x_mitre_domains: enterprise-attack
---

## Tactic

- [[defense_evasion|Defense Evasion]]

Adversaries may delete or modify artifacts generated within systems to remove evidence of their presence or hinder defenses. Various artifacts may be created by an adversary or something that can be attributed to an adversary’s actions. Typically these artifacts are used as defensive indicators related to monitored events, such as strings from downloaded files, logs that are generated from user actions, and other data analyzed by defenders. Location, format, and type of artifact (such as command or login history) are often specific to each platform.

Removal of these indicators may interfere with event collection, reporting, or other processes used to detect intrusion activity. This may compromise the integrity of security solutions by causing notable events to go unreported. This activity may also impede forensic analysis and incident response, due to lack of sufficient data to determine what occurred.

## Properties

- id: T1070
- name: Indicator Removal
- created: 2017-05-31 21:30:55.892000+00:00
- modified: 2025-10-24 17:48:59.237000+00:00
- type: attack-pattern
- x_mitre_version: 2.4
- x_mitre_domains: enterprise-attack

## Subtechniques

### T1070.001: Clear Windows Event Logs

^t1070001-clear-windows-event-logs

**Parent Technique**
- [[T1070-indicator_removal|T1070: Indicator Removal]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may clear Windows Event Logs to hide the activity of an intrusion. Windows Event Logs are a record of a computer's alerts and notifications. There are three system-defined sources of events: System, Application, and Security, with five event types: Error, Warning, Information, Success Audit, and Failure Audit.


With administrator privileges, the event logs can be cleared with the following utility commands:

* <code>wevtutil cl system</code>
* <code>wevtutil cl application</code>
* <code>wevtutil cl security</code>

These logs may also be cleared through other mechanisms, such as the event viewer GUI or [PowerShell](https://attack.mitre.org/techniques/T1059/001). For example, adversaries may use the PowerShell command <code>Remove-EventLog -LogName Security</code> to delete the Security EventLog and after reboot, disable future logging.  Note: events may still be generated and logged in the .evtx file between the time the command is run and the reboot.(Citation: disable_win_evt_logging)

Adversaries may also attempt to clear logs by directly deleting the stored log files within `C:\Windows\System32\winevt\logs\`.

#### Properties

- id: T1070.001
- name: Clear Windows Event Logs
- created: 2020-01-28 17:05:14.707000+00:00
- modified: 2025-10-24 17:48:52.287000+00:00
- type: attack-pattern
- x_mitre_version: 1.5
- x_mitre_domains: enterprise-attack

### T1070.002: Clear Linux or Mac System Logs

^t1070002-clear-linux-or-mac-system-logs

**Parent Technique**
- [[T1070-indicator_removal|T1070: Indicator Removal]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may clear system logs to hide evidence of an intrusion. macOS and Linux both keep track of system or user-initiated actions via system logs. The majority of native system logging is stored under the <code>/var/log/</code> directory. Subfolders in this directory categorize logs by their related functions, such as:(Citation: Linux Logs)

* <code>/var/log/messages:</code>: General and system-related messages
* <code>/var/log/secure</code> or <code>/var/log/auth.log</code>: Authentication logs
* <code>/var/log/utmp</code> or <code>/var/log/wtmp</code>: Login records
* <code>/var/log/kern.log</code>: Kernel logs
* <code>/var/log/cron.log</code>: Crond logs
* <code>/var/log/maillog</code>: Mail server logs
* <code>/var/log/httpd/</code>: Web server access and error logs


#### Properties

- id: T1070.002
- name: Clear Linux or Mac System Logs
- created: 2020-01-28 17:11:54.034000+00:00
- modified: 2025-10-24 17:48:34.441000+00:00
- type: attack-pattern
- x_mitre_version: 1.0
- x_mitre_domains: enterprise-attack

### T1070.003: Clear Command History

^t1070003-clear-command-history

**Parent Technique**
- [[T1070-indicator_removal|T1070: Indicator Removal]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

In addition to clearing system logs, an adversary may clear the command history of a compromised account to conceal the actions undertaken during an intrusion. Various command interpreters keep track of the commands users type in their terminal so that users can retrace what they've done.

On Linux and macOS, these command histories can be accessed in a few different ways. While logged in, this command history is tracked in a file pointed to by the environment variable <code>HISTFILE</code>. When a user logs off a system, this information is flushed to a file in the user's home directory called <code>~/.bash_history</code>. The benefit of this is that it allows users to go back to commands they've used before in different sessions. Adversaries may delete their commands from these logs by manually clearing the history (<code>history -c</code>) or deleting the bash history file <code>rm ~/.bash_history</code>.  

Adversaries may also leverage a [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) on network devices to clear command history data (<code>clear logging</code> and/or <code>clear history</code>).(Citation: US-CERT-TA18-106A) On ESXi servers, command history may be manually removed from the `/var/log/shell.log` file.(Citation: Broadcom ESXi Shell Audit)

On Windows hosts, PowerShell has two different command history providers: the built-in history and the command history managed by the <code>PSReadLine</code> module. The built-in history only tracks the commands used in the current session. This command history is not available to other sessions and is deleted when the session ends.

The <code>PSReadLine</code> command history tracks the commands used in all PowerShell sessions and writes them to a file (<code>$env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt</code> by default). This history file is available to all sessions and contains all past history since the file is not deleted when the session ends.(Citation: Microsoft PowerShell Command History)

Adversaries may run the PowerShell command <code>Clear-History</code> to flush the entire command history from a current PowerShell session. This, however, will not delete/flush the <code>ConsoleHost_history.txt</code> file. Adversaries may also delete the <code>ConsoleHost_history.txt</code> file or edit its contents to hide PowerShell commands they have run.(Citation: Sophos PowerShell command audit)(Citation: Sophos PowerShell Command History Forensics)

#### Properties

- id: T1070.003
- name: Clear Command History
- created: 2020-01-31 12:32:08.228000+00:00
- modified: 2025-10-24 17:48:40.313000+00:00
- type: attack-pattern
- x_mitre_version: 1.6
- x_mitre_domains: enterprise-attack

### T1070.004: File Deletion

^t1070004-file-deletion

**Parent Technique**
- [[T1070-indicator_removal|T1070: Indicator Removal]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may delete files left behind by the actions of their intrusion activity. Malware, tools, or other non-native files dropped or created on a system by an adversary (ex: [Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105)) may leave traces to indicate to what was done within a network and how. Removal of these files can occur during an intrusion, or as part of a post-intrusion process to minimize the adversary's footprint.

There are tools available from the host operating system to perform cleanup, but adversaries may use other tools as well.(Citation: Microsoft SDelete July 2016) Examples of built-in [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059) functions include <code>del</code> on Windows, <code>rm</code> or <code>unlink</code> on Linux and macOS, and `rm` on ESXi.

#### Properties

- id: T1070.004
- name: File Deletion
- created: 2020-01-31 12:35:36.479000+00:00
- modified: 2025-10-24 17:49:27.978000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1070.005: Network Share Connection Removal

^t1070005-network-share-connection-removal

**Parent Technique**
- [[T1070-indicator_removal|T1070: Indicator Removal]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may remove share connections that are no longer useful in order to clean up traces of their operation. Windows shared drive and [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) connections can be removed when no longer needed. [Net](https://attack.mitre.org/software/S0039) is an example utility that can be used to remove network share connections with the <code>net use \\system\share /delete</code> command. (Citation: Technet Net Use)

#### Properties

- id: T1070.005
- name: Network Share Connection Removal
- created: 2020-01-31 12:39:18.816000+00:00
- modified: 2025-10-24 17:49:11.691000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1070.006: Timestomp

^t1070006-timestomp

**Parent Technique**
- [[T1070-indicator_removal|T1070: Indicator Removal]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may modify file time attributes to hide new files or changes to existing files. Timestomping is a technique that modifies the timestamps of a file (the modify, access, create, and change times), often to mimic files that are in the same folder and blend malicious files with legitimate files.

In Windows systems, both the `$STANDARD_INFORMATION` (`$SI`) and `$FILE_NAME` (`$FN`) attributes record times in a Master File Table (MFT) file.(Citation: Inversecos Timestomping 2022) `$SI` (dates/time stamps) is displayed to the end user, including in the File System view, while `$FN` is dealt with by the kernel.(Citation: Magnet Forensics)

Modifying the `$SI` attribute is the most common method of timestomping because it can be modified at the user level using API calls. `$FN` timestomping, however, typically requires interacting with the system kernel or moving or renaming a file.(Citation: Inversecos Timestomping 2022)

Adversaries modify timestamps on files so that they do not appear conspicuous to forensic investigators or file analysis tools. In order to evade detections that rely on identifying discrepancies between the `$SI` and `$FN` attributes, adversaries may also engage in “double timestomping” by modifying times on both attributes simultaneously.(Citation: Double Timestomping)

In Linux systems and on ESXi servers, threat actors may attempt to perform timestomping using commands such as `touch -a -m -t <timestamp> <filename>` (which sets access and modification times to a specific value) or `touch -r <filename> <filename>` (which sets access and modification times to match those of another file).(Citation: Inversecos Linux Timestomping)(Citation: Juniper Networks ESXi Backdoor 2022)

Timestomping may be used along with file name [Masquerading](https://attack.mitre.org/techniques/T1036) to hide malware and tools.(Citation: WindowsIR Anti-Forensic Techniques)

#### Properties

- id: T1070.006
- name: Timestomp
- created: 2020-01-31 12:42:44.103000+00:00
- modified: 2025-10-24 17:48:43.937000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1070.007: Clear Network Connection History and Configurations

^t1070007-clear-network-connection-history-and-configurations

**Parent Technique**
- [[T1070-indicator_removal|T1070: Indicator Removal]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may clear or remove evidence of malicious network connections in order to clean up traces of their operations. Configuration settings as well as various artifacts that highlight connection history may be created on a system and/or in application logs from behaviors that require network connections, such as [Remote Services](https://attack.mitre.org/techniques/T1021) or [External Remote Services](https://attack.mitre.org/techniques/T1133). Defenders may use these artifacts to monitor or otherwise analyze network connections created by adversaries.

Network connection history may be stored in various locations. For example, RDP connection history may be stored in Windows Registry values under (Citation: Microsoft RDP Removal):

* <code>HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default</code>
* <code>HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Servers</code>

Windows may also store information about recent RDP connections in files such as <code>C:\Users\\%username%\Documents\Default.rdp</code> and `C:\Users\%username%\AppData\Local\Microsoft\Terminal
Server Client\Cache\`.(Citation: Moran RDPieces) Similarly, macOS and Linux hosts may store information highlighting connection history in system logs (such as those stored in `/Library/Logs` and/or `/var/log/`).(Citation: Apple Culprit Access)(Citation: FreeDesktop Journal)(Citation: Apple Unified Log Analysis Remote Login and Screen Sharing)

Malicious network connections may also require changes to third-party applications or network configuration settings, such as [Disable or Modify System Firewall](https://attack.mitre.org/techniques/T1562/004) or tampering to enable [Proxy](https://attack.mitre.org/techniques/T1090). Adversaries may delete or modify this data to conceal indicators and/or impede defensive analysis.

#### Properties

- id: T1070.007
- name: Clear Network Connection History and Configurations
- created: 2022-06-15 18:00:04.219000+00:00
- modified: 2025-04-16 20:37:16.734000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1070.008: Clear Mailbox Data

^t1070008-clear-mailbox-data

**Parent Technique**
- [[T1070-indicator_removal|T1070: Indicator Removal]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may modify mail and mail application data to remove evidence of their activity. Email applications allow users and other programs to export and delete mailbox data via command line tools or use of APIs. Mail application data can be emails, email metadata, or logs generated by the application or operating system, such as export requests. 

Adversaries may manipulate emails and mailbox data to remove logs, artifacts, and metadata, such as evidence of [Phishing](https://attack.mitre.org/techniques/T1566)/[Internal Spearphishing](https://attack.mitre.org/techniques/T1534), [Email Collection](https://attack.mitre.org/techniques/T1114), [Mail Protocols](https://attack.mitre.org/techniques/T1071/003) for command and control, or email-based exfiltration such as [Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048). For example, to remove evidence on Exchange servers adversaries have used the <code>ExchangePowerShell</code> [PowerShell](https://attack.mitre.org/techniques/T1059/001) module, including <code>Remove-MailboxExportRequest</code> to remove evidence of mailbox exports.(Citation: Volexity SolarWinds)(Citation: ExchangePowerShell Module) On Linux and macOS, adversaries may also delete emails through a command line utility called <code>mail</code>  or use [AppleScript](https://attack.mitre.org/techniques/T1059/002) to interact with APIs on macOS.(Citation: Cybereason Cobalt Kitty 2017)(Citation: mailx man page)

Adversaries may also remove emails and metadata/headers indicative of spam or suspicious activity (for example, through the use of organization-wide transport rules) to reduce the likelihood of malicious emails being detected by security products.(Citation: Microsoft OAuth Spam 2022)

#### Properties

- id: T1070.008
- name: Clear Mailbox Data
- created: 2022-07-08 21:04:03.739000+00:00
- modified: 2025-04-15 21:56:59.810000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1070.009: Clear Persistence

^t1070009-clear-persistence

**Parent Technique**
- [[T1070-indicator_removal|T1070: Indicator Removal]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may clear artifacts associated with previously established persistence on a host system to remove evidence of their activity. This may involve various actions, such as removing services, deleting executables, [Modify Registry](https://attack.mitre.org/techniques/T1112), [Plist File Modification](https://attack.mitre.org/techniques/T1647), or other methods of cleanup to prevent defenders from collecting evidence of their persistent presence.(Citation: Cylance Dust Storm) Adversaries may also delete accounts previously created to maintain persistence (i.e. [Create Account](https://attack.mitre.org/techniques/T1136)).(Citation: Talos - Cisco Attack 2022)

In some instances, artifacts of persistence may also be removed once an adversary’s persistence is executed in order to prevent errors with the new instance of the malware.(Citation: NCC Group Team9 June 2020)

#### Properties

- id: T1070.009
- name: Clear Persistence
- created: 2022-07-29 19:32:11.552000+00:00
- modified: 2025-04-16 20:37:21.515000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1070.010: Relocate Malware

^t1070010-relocate-malware

**Parent Technique**
- [[T1070-indicator_removal|T1070: Indicator Removal]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Once a payload is delivered, adversaries may reproduce copies of the same malware on the victim system to remove evidence of their presence and/or avoid defenses. Copying malware payloads to new locations may also be combined with [File Deletion](https://attack.mitre.org/techniques/T1070/004) to cleanup older artifacts.

Relocating malware may be a part of many actions intended to evade defenses. For example, adversaries may copy and rename payloads to better blend into the local environment (i.e., [Match Legitimate Resource Name or Location](https://attack.mitre.org/techniques/T1036/005)).(Citation: DFIR Report Trickbot June 2023) Payloads may also be repositioned to target [File/Path Exclusions](https://attack.mitre.org/techniques/T1564/012) as well as specific locations associated with establishing [Persistence](https://attack.mitre.org/tactics/TA0003).(Citation: Latrodectus APR 2024)

Relocating malicious payloads may also hinder defensive analysis, especially to separate these payloads from earlier events (such as [User Execution](https://attack.mitre.org/techniques/T1204) and [Phishing](https://attack.mitre.org/techniques/T1566)) that may have generated alerts or otherwise drawn attention from defenders. Moving payloads into target directories does not alter the Creation timestamp, thereby evading detection logic reliant on modifications to this artifact (i.e., [Timestomp](https://attack.mitre.org/techniques/T1070/006)).

#### Properties

- id: T1070.010
- name: Relocate Malware
- created: 2024-05-31 11:07:57.406000+00:00
- modified: 2025-10-05 16:08:40.119000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1022-restrict_file_and_directory_permissions|M1022: Restrict File and Directory Permissions]]
- [[M1029-remote_data_storage|M1029: Remote Data Storage]]
- [[M1041-encrypt_sensitive_information|M1041: Encrypt Sensitive Information]]

## Platforms

- Containers
- ESXi
- Linux
- macOS
- Network Devices
- Office Suite
- Windows

## Tools

- [[S0527-cspy_downloader|S0527: CSPY Downloader]]
- [[S0692-silenttrinity|S0692: SILENTTRINITY]]
- [[S0695-donut|S0695: Donut]]

