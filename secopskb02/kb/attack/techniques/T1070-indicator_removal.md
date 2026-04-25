---
mitre_id: "T1070"
mitre_name: "Indicator Removal"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--799ace7f-e227-4411-baa0-8868704f2a69"
mitre_created: "2017-05-31T21:30:55.892Z"
mitre_modified: "2025-10-24T17:48:59.237Z"
mitre_version: "2.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1070/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Containers"
  - "ESXi"
  - "Linux"
  - "macOS"
  - "Network Devices"
  - "Office Suite"
  - "Windows"
mitre_tactic_ids:
  - "TA0005"
d3fend_ids:
  - "D3-AEM"
  - "D3-CF"
  - "D3-CM"
  - "D3-CQ"
  - "D3-DF"
  - "D3-DNR"
  - "D3-FA"
  - "D3-FE"
  - "D3-FEV"
  - "D3-FIM"
  - "D3-LFP"
  - "D3-NRAM"
  - "D3-OPM"
  - "D3-RF"
  - "D3-RFAM"
  - "D3-SFA"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may delete or modify artifacts generated within systems to remove evidence of their presence or hinder defenses. Various artifacts may be created by an adversary or something that can be attributed to an adversary’s actions. Typically these artifacts are used as defensive indicators related to monitored events, such as strings from downloaded files, logs that are generated from user actions, and other data analyzed by defenders. Location, format, and type of artifact (such as command or login history) are often specific to each platform.

Removal of these indicators may interfere with event collection, reporting, or other processes used to detect intrusion activity. This may compromise the integrity of security solutions by causing notable events to go unreported. This activity may also impede forensic analysis and incident response, due to lack of sufficient data to determine what occurred.

## Workspace

- [[workspaces/attack/techniques/T1070-indicator_removal-note|Open workspace note]]

![[workspaces/attack/techniques/T1070-indicator_removal-note]]

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

## D3FEND

- [[D3-AEM-application_exception_monitoring|D3-AEM: Application Exception Monitoring]]
- [[D3-CF-content_filtering|D3-CF: Content Filtering]]
- [[D3-CM-content_modification|D3-CM: Content Modification]]
- [[D3-CQ-content_quarantine|D3-CQ: Content Quarantine]]
- [[D3-DF-decoy_file|D3-DF: Decoy File]]
- [[D3-DNR-decoy_network_resource|D3-DNR: Decoy Network Resource]]
- [[D3-FA-file_analysis|D3-FA: File Analysis]]
- [[D3-FE-file_encryption|D3-FE: File Encryption]]
- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]
- [[D3-FIM-file_integrity_monitoring|D3-FIM: File Integrity Monitoring]]
- [[D3-LFP-local_file_permissions|D3-LFP: Local File Permissions]]
- [[D3-NRAM-network_resource_access_mediation|D3-NRAM: Network Resource Access Mediation]]
- [[D3-OPM-operational_process_monitoring|D3-OPM: Operational Process Monitoring]]
- [[D3-RF-restore_file|D3-RF: Restore File]]
- [[D3-RFAM-remote_file_access_mediation|D3-RFAM: Remote File Access Mediation]]
- [[D3-SFA-system_file_analysis|D3-SFA: System File Analysis]]

## Subtechniques

### T1070.001: Clear Windows Event Logs

^t1070001-clear-windows-event-logs

Adversaries may clear Windows Event Logs to hide the activity of an intrusion. Windows Event Logs are a record of a computer's alerts and notifications. There are three system-defined sources of events: System, Application, and Security, with five event types: Error, Warning, Information, Success Audit, and Failure Audit.


With administrator privileges, the event logs can be cleared with the following utility commands:

* `wevtutil cl system`
* `wevtutil cl application`
* `wevtutil cl security`

These logs may also be cleared through other mechanisms, such as the event viewer GUI or [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]. For example, adversaries may use the PowerShell command `Remove-EventLog -LogName Security` to delete the Security EventLog and after reboot, disable future logging.  Note: events may still be generated and logged in the .evtx file between the time the command is run and the reboot.(Citation: disable_win_evt_logging)

Adversaries may also attempt to clear logs by directly deleting the stored log files within `C:\Windows\System32\winevt\logs\`.

### T1070.002: Clear Linux or Mac System Logs

^t1070002-clear-linux-or-mac-system-logs

Adversaries may clear system logs to hide evidence of an intrusion. macOS and Linux both keep track of system or user-initiated actions via system logs. The majority of native system logging is stored under the `/var/log/` directory. Subfolders in this directory categorize logs by their related functions, such as:(Citation: Linux Logs)

* `/var/log/messages:`: General and system-related messages
* `/var/log/secure` or `/var/log/auth.log`: Authentication logs
* `/var/log/utmp` or `/var/log/wtmp`: Login records
* `/var/log/kern.log`: Kernel logs
* `/var/log/cron.log`: Crond logs
* `/var/log/maillog`: Mail server logs
* `/var/log/httpd/`: Web server access and error logs


### T1070.003: Clear Command History

^t1070003-clear-command-history

In addition to clearing system logs, an adversary may clear the command history of a compromised account to conceal the actions undertaken during an intrusion. Various command interpreters keep track of the commands users type in their terminal so that users can retrace what they've done.

On Linux and macOS, these command histories can be accessed in a few different ways. While logged in, this command history is tracked in a file pointed to by the environment variable `HISTFILE`. When a user logs off a system, this information is flushed to a file in the user's home directory called `~/.bash_history`. The benefit of this is that it allows users to go back to commands they've used before in different sessions. Adversaries may delete their commands from these logs by manually clearing the history (`history -c`) or deleting the bash history file `rm ~/.bash_history`.  

Adversaries may also leverage a [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]] on network devices to clear command history data (`clear logging` and/or `clear history`).(Citation: US-CERT-TA18-106A) On ESXi servers, command history may be manually removed from the `/var/log/shell.log` file.(Citation: Broadcom ESXi Shell Audit)

On Windows hosts, PowerShell has two different command history providers: the built-in history and the command history managed by the `PSReadLine` module. The built-in history only tracks the commands used in the current session. This command history is not available to other sessions and is deleted when the session ends.

The `PSReadLine` command history tracks the commands used in all PowerShell sessions and writes them to a file (`$env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt` by default). This history file is available to all sessions and contains all past history since the file is not deleted when the session ends.(Citation: Microsoft PowerShell Command History)

Adversaries may run the PowerShell command `Clear-History` to flush the entire command history from a current PowerShell session. This, however, will not delete/flush the `ConsoleHost_history.txt` file. Adversaries may also delete the `ConsoleHost_history.txt` file or edit its contents to hide PowerShell commands they have run.(Citation: Sophos PowerShell command audit)(Citation: Sophos PowerShell Command History Forensics)

### T1070.004: File Deletion

^t1070004-file-deletion

Adversaries may delete files left behind by the actions of their intrusion activity. Malware, tools, or other non-native files dropped or created on a system by an adversary (ex: [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]) may leave traces to indicate to what was done within a network and how. Removal of these files can occur during an intrusion, or as part of a post-intrusion process to minimize the adversary's footprint.

There are tools available from the host operating system to perform cleanup, but adversaries may use other tools as well.(Citation: Microsoft SDelete July 2016) Examples of built-in [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]] functions include `del` on Windows, `rm` or `unlink` on Linux and macOS, and `rm` on ESXi.

### T1070.005: Network Share Connection Removal

^t1070005-network-share-connection-removal

Adversaries may remove share connections that are no longer useful in order to clean up traces of their operation. Windows shared drive and [[T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]] connections can be removed when no longer needed. [[net|Net (S0039)]] is an example utility that can be used to remove network share connections with the `net use \\system\share /delete` command. (Citation: Technet Net Use)

### T1070.006: Timestomp

^t1070006-timestomp

Adversaries may modify file time attributes to hide new files or changes to existing files. Timestomping is a technique that modifies the timestamps of a file (the modify, access, create, and change times), often to mimic files that are in the same folder and blend malicious files with legitimate files.

In Windows systems, both the `$STANDARD_INFORMATION` (`$SI`) and `$FILE_NAME` (`$FN`) attributes record times in a Master File Table (MFT) file.(Citation: Inversecos Timestomping 2022) `$SI` (dates/time stamps) is displayed to the end user, including in the File System view, while `$FN` is dealt with by the kernel.(Citation: Magnet Forensics)

Modifying the `$SI` attribute is the most common method of timestomping because it can be modified at the user level using API calls. `$FN` timestomping, however, typically requires interacting with the system kernel or moving or renaming a file.(Citation: Inversecos Timestomping 2022)

Adversaries modify timestamps on files so that they do not appear conspicuous to forensic investigators or file analysis tools. In order to evade detections that rely on identifying discrepancies between the `$SI` and `$FN` attributes, adversaries may also engage in “double timestomping” by modifying times on both attributes simultaneously.(Citation: Double Timestomping)

In Linux systems and on ESXi servers, threat actors may attempt to perform timestomping using commands such as `touch -a -m -t <timestamp> <filename>` (which sets access and modification times to a specific value) or `touch -r <filename> <filename>` (which sets access and modification times to match those of another file).(Citation: Inversecos Linux Timestomping)(Citation: Juniper Networks ESXi Backdoor 2022)

Timestomping may be used along with file name [[T1036-masquerading|T1036: Masquerading]] to hide malware and tools.(Citation: WindowsIR Anti-Forensic Techniques)

### T1070.007: Clear Network Connection History and Configurations

^t1070007-clear-network-connection-history-and-configurations

Adversaries may clear or remove evidence of malicious network connections in order to clean up traces of their operations. Configuration settings as well as various artifacts that highlight connection history may be created on a system and/or in application logs from behaviors that require network connections, such as [[T1021-remote_services|T1021: Remote Services]] or [[T1133-external_remote_services|T1133: External Remote Services]]. Defenders may use these artifacts to monitor or otherwise analyze network connections created by adversaries.

Network connection history may be stored in various locations. For example, RDP connection history may be stored in Windows Registry values under (Citation: Microsoft RDP Removal):

* `HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default`
* `HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Servers`

Windows may also store information about recent RDP connections in files such as `C:\Users\\%username%\Documents\Default.rdp` and `C:\Users\%username%\AppData\Local\Microsoft\Terminal
Server Client\Cache\`.(Citation: Moran RDPieces) Similarly, macOS and Linux hosts may store information highlighting connection history in system logs (such as those stored in `/Library/Logs` and/or `/var/log/`).(Citation: Apple Culprit Access)(Citation: FreeDesktop Journal)(Citation: Apple Unified Log Analysis Remote Login and Screen Sharing)

Malicious network connections may also require changes to third-party applications or network configuration settings, such as [[T1562-impair_defenses#^t1562004-disable-or-modify-system-firewall|T1562.004: Disable or Modify System Firewall]] or tampering to enable [[T1090-proxy|T1090: Proxy]]. Adversaries may delete or modify this data to conceal indicators and/or impede defensive analysis.

### T1070.008: Clear Mailbox Data

^t1070008-clear-mailbox-data

Adversaries may modify mail and mail application data to remove evidence of their activity. Email applications allow users and other programs to export and delete mailbox data via command line tools or use of APIs. Mail application data can be emails, email metadata, or logs generated by the application or operating system, such as export requests. 

Adversaries may manipulate emails and mailbox data to remove logs, artifacts, and metadata, such as evidence of [[T1566-phishing|T1566: Phishing]]/[[T1534-internal_spearphishing|T1534: Internal Spearphishing]], [[T1114-email_collection|T1114: Email Collection]], [[T1071-application_layer_protocol#^t1071003-mail-protocols|T1071.003: Mail Protocols]] for command and control, or email-based exfiltration such as [[T1048-exfiltration_over_alternative_protocol|T1048: Exfiltration Over Alternative Protocol]]. For example, to remove evidence on Exchange servers adversaries have used the `ExchangePowerShell` [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]] module, including `Remove-MailboxExportRequest` to remove evidence of mailbox exports.(Citation: Volexity SolarWinds)(Citation: ExchangePowerShell Module) On Linux and macOS, adversaries may also delete emails through a command line utility called `mail`  or use [[T1059-command_and_scripting_interpreter#^t1059002-applescript|T1059.002: AppleScript]] to interact with APIs on macOS.(Citation: Cybereason Cobalt Kitty 2017)(Citation: mailx man page)

Adversaries may also remove emails and metadata/headers indicative of spam or suspicious activity (for example, through the use of organization-wide transport rules) to reduce the likelihood of malicious emails being detected by security products.(Citation: Microsoft OAuth Spam 2022)

### T1070.009: Clear Persistence

^t1070009-clear-persistence

Adversaries may clear artifacts associated with previously established persistence on a host system to remove evidence of their activity. This may involve various actions, such as removing services, deleting executables, [[T1112-modify_registry|T1112: Modify Registry]], [[T1647-plist_file_modification|T1647: Plist File Modification]], or other methods of cleanup to prevent defenders from collecting evidence of their persistent presence.(Citation: Cylance Dust Storm) Adversaries may also delete accounts previously created to maintain persistence (i.e. [[T1136-create_account|T1136: Create Account]]).(Citation: Talos - Cisco Attack 2022)

In some instances, artifacts of persistence may also be removed once an adversary’s persistence is executed in order to prevent errors with the new instance of the malware.(Citation: NCC Group Team9 June 2020)

### T1070.010: Relocate Malware

^t1070010-relocate-malware

Once a payload is delivered, adversaries may reproduce copies of the same malware on the victim system to remove evidence of their presence and/or avoid defenses. Copying malware payloads to new locations may also be combined with [[T1070-indicator_removal#^t1070004-file-deletion|T1070.004: File Deletion]] to cleanup older artifacts.

Relocating malware may be a part of many actions intended to evade defenses. For example, adversaries may copy and rename payloads to better blend into the local environment (i.e., [[T1036-masquerading#^t1036005-match-legitimate-resource-name-or-location|T1036.005: Match Legitimate Resource Name or Location]]).(Citation: DFIR Report Trickbot June 2023) Payloads may also be repositioned to target [[T1564-hide_artifacts#^t1564012-file-path-exclusions|T1564.012: File/Path Exclusions]] as well as specific locations associated with establishing [[TA0003-persistence|TA0003: Persistence]].(Citation: Latrodectus APR 2024)

Relocating malicious payloads may also hinder defensive analysis, especially to separate these payloads from earlier events (such as [[T1204-user_execution|T1204: User Execution]] and [[T1566-phishing|T1566: Phishing]]) that may have generated alerts or otherwise drawn attention from defenders. Moving payloads into target directories does not alter the Creation timestamp, thereby evading detection logic reliant on modifications to this artifact (i.e., [[T1070-indicator_removal#^t1070006-timestomp|T1070.006: Timestomp]]).

## Mitigations

- [[M1022-restrict_file_and_directory_permissions|M1022: Restrict File and Directory Permissions]]
- [[M1029-remote_data_storage|M1029: Remote Data Storage]]
- [[M1041-encrypt_sensitive_information|M1041: Encrypt Sensitive Information]]

## Tools

- [[cspy_downloader|CSPY Downloader (S0527)]]
- [[silenttrinity|SILENTTRINITY (S0692)]]
- [[donut|Donut (S0695)]]

## Platforms

- Containers
- ESXi
- Linux
- macOS
- Network Devices
- Office Suite
- Windows

