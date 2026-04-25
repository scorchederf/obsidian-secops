---
mitre_id: "T1036"
mitre_name: "Masquerading"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--42e8de7b-37b2-4258-905a-6897815e58e0"
mitre_created: "2017-05-31T21:30:38.511Z"
mitre_modified: "2025-10-24T17:48:42.609Z"
mitre_version: "1.8"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1036/"
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
  - "Windows"
mitre_tactic_ids:
  - "TA0005"
d3fend_ids:
  - "D3-CF"
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
  - "D3-RF"
  - "D3-RFAM"
  - "D3-SCA"
  - "D3-SCF"
  - "D3-SFA"
  - "D3-SJA"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may attempt to manipulate features of their artifacts to make them appear legitimate or benign to users and/or security tools. Masquerading occurs when the name or location of an object, legitimate or malicious, is manipulated or abused for the sake of evading defenses and observation. This may include manipulating file metadata, tricking users into misidentifying the file type, and giving legitimate task or service names.

Renaming abusable system utilities to evade security monitoring is also a form of [[T1036-masquerading|T1036: Masquerading]].(Citation: LOLBAS Main Site)

## Workspace

- [[workspaces/attack/techniques/T1036-masquerading-note|Open workspace note]]

![[workspaces/attack/techniques/T1036-masquerading-note]]

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

## D3FEND

- [[D3-CF-content_filtering|D3-CF: Content Filtering]]
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
- [[D3-RF-restore_file|D3-RF: Restore File]]
- [[D3-RFAM-remote_file_access_mediation|D3-RFAM: Remote File Access Mediation]]
- [[D3-SCA-system_call_analysis|D3-SCA: System Call Analysis]]
- [[D3-SCF-system_call_filtering|D3-SCF: System Call Filtering]]
- [[D3-SFA-system_file_analysis|D3-SFA: System File Analysis]]
- [[D3-SJA-scheduled_job_analysis|D3-SJA: Scheduled Job Analysis]]

## Subtechniques

### T1036.001: Invalid Code Signature

^t1036001-invalid-code-signature

Adversaries may attempt to mimic features of valid code signatures to increase the chance of deceiving a user, analyst, or tool. Code signing provides a level of authenticity on a binary from the developer and a guarantee that the binary has not been tampered with. Adversaries can copy the metadata and signature information from a signed program, then use it as a template for an unsigned program. Files with invalid code signatures will fail digital signature validation checks, but they may appear more legitimate to users and security tools may improperly handle these files.(Citation: Threatexpress MetaTwin 2017)

Unlike [[T1553-subvert_trust_controls#^t1553002-code-signing|T1553.002: Code Signing]], this activity will not result in a valid signature.

### T1036.002: Right-to-Left Override

^t1036002-right-to-left-override

Adversaries may abuse the right-to-left override (RTLO or RLO) character (U+202E) to disguise a string and/or file name to make it appear benign. RTLO is a non-printing Unicode character that causes the text that follows it to be displayed in reverse. For example, a Windows screensaver executable named `March 25 \u202Excod.scr` will display as `March 25 rcs.docx`. A JavaScript file named `photo_high_re\u202Egnp.js` will be displayed as `photo_high_resj.png`.(Citation: Infosecinstitute RTLO Technique)

Adversaries may abuse the RTLO character as a means of tricking a user into executing what they think is a benign file type. A common use of this technique is with [[T1566-phishing#^t1566001-spearphishing-attachment|T1566.001: Spearphishing Attachment]]/[[T1204-user_execution#^t1204002-malicious-file|T1204.002: Malicious File]] since it can trick both end users and defenders if they are not aware of how their tools display and render the RTLO character. Use of the RTLO character has been seen in many targeted intrusion attempts and criminal activity.(Citation: Trend Micro PLEAD RTLO)(Citation: Kaspersky RTLO Cyber Crime) RTLO can be used in the Windows Registry as well, where regedit.exe displays the reversed characters but the command line tool reg.exe does not by default.

### T1036.003: Rename Legitimate Utilities

^t1036003-rename-legitimate-utilities

Adversaries may rename legitimate / system utilities to try to evade security mechanisms concerning the usage of those utilities. Security monitoring and control mechanisms may be in place for legitimate utilities adversaries are capable of abusing, including both built-in binaries and tools such as PSExec, AutoHotKey, and IronPython.(Citation: LOLBAS Main Site)(Citation: Huntress Python Malware 2025)(Citation: The DFIR Report AutoHotKey 2023)(Citation: Splunk Detect Renamed PSExec) It may be possible to bypass those security mechanisms by renaming the utility prior to utilization (ex: rename `rundll32.exe`).(Citation: Elastic Masquerade Ball) An alternative case occurs when a legitimate utility is copied or moved to a different directory and renamed to avoid detections based on these utilities executing from non-standard paths.(Citation: F-Secure CozyDuke)

### T1036.004: Masquerade Task or Service

^t1036004-masquerade-task-or-service

Adversaries may attempt to manipulate the name of a task or service to make it appear legitimate or benign. Tasks/services executed by the Task Scheduler or systemd will typically be given a name and/or description.(Citation: TechNet Schtasks)(Citation: Systemd Service Units) Windows services will have a service name as well as a display name. Many benign tasks and services exist that have commonly associated names. Adversaries may give tasks or services names that are similar or identical to those of legitimate ones.

Tasks or services contain other fields, such as a description, that adversaries may attempt to make appear legitimate.(Citation: Palo Alto Shamoon Nov 2016)(Citation: Fysbis Dr Web Analysis)

### T1036.005: Match Legitimate Resource Name or Location

^t1036005-match-legitimate-resource-name-or-location

Adversaries may match or approximate the name or location of legitimate files, Registry keys, or other resources when naming/placing them. This is done for the sake of evading defenses and observation. 

This may be done by placing an executable in a commonly trusted directory (ex: under System32) or giving it the name of a legitimate, trusted program (ex: `svchost.exe`). Alternatively, a Windows Registry key may be given a close approximation to a key used by a legitimate program. In containerized environments, a threat actor may create a resource in a trusted namespace or one that matches the naming convention of a container pod or cluster.(Citation: Aquasec Kubernetes Backdoor 2023)

### T1036.006: Space after Filename

^t1036006-space-after-filename

Adversaries can hide a program's true filetype by changing the extension of a file. With certain file types (specifically this does not work with .app extensions), appending a space to the end of a filename will change how the file is processed by the operating system.

For example, if there is a Mach-O executable file called `evil.bin`, when it is double clicked by a user, it will launch Terminal.app and execute. If this file is renamed to `evil.txt`, then when double clicked by a user, it will launch with the default text editing application (not executing the binary). However, if the file is renamed to `evil.txt` (note the space at the end), then when double clicked by a user, the true file type is determined by the OS and handled appropriately and the binary will be executed (Citation: Mac Backdoors are back).

Adversaries can use this feature to trick users into double clicking benign-looking files of any format and ultimately executing something malicious.

### T1036.007: Double File Extension

^t1036007-double-file-extension

Adversaries may abuse a double extension in the filename as a means of masquerading the true file type. A file name may include a secondary file type extension that may cause only the first extension to be displayed (ex: `File.txt.exe` may render in some views as just `File.txt`). However, the second extension is the true file type that determines how the file is opened and executed. The real file extension may be hidden by the operating system in the file browser (ex: explorer.exe), as well as in any software configured using or similar to the system’s policies.(Citation: PCMag DoubleExtension)(Citation: SOCPrime DoubleExtension) 

Adversaries may abuse double extensions to attempt to conceal dangerous file types of payloads. A very common usage involves tricking a user into opening what they think is a benign file type but is actually executable code. Such files often pose as email attachments and allow an adversary to gain [[TA0001-initial_access|TA0001: Initial Access]] into a user’s system via [[T1566-phishing#^t1566001-spearphishing-attachment|T1566.001: Spearphishing Attachment]] then [[T1204-user_execution|T1204: User Execution]]. For example, an executable file attachment named `Evil.txt.exe` may display as `Evil.txt` to a user. The user may then view it as a benign text file and open it, inadvertently executing the hidden malware.(Citation: SOCPrime DoubleExtension)

Common file types, such as text files (.txt, .doc, etc.) and image files (.jpg, .gif, etc.) are typically used as the first extension to appear benign. Executable extensions commonly regarded as dangerous, such as .exe, .lnk, .hta, and .scr, often appear as the second extension and true file type.

### T1036.008: Masquerade File Type

^t1036008-masquerade-file-type

Adversaries may masquerade malicious payloads as legitimate files through changes to the payload's formatting, including the file’s signature, extension, icon, and contents. Various file types have a typical standard format, including how they are encoded and organized. For example, a file’s signature (also known as header or magic bytes) is the beginning bytes of a file and is often used to identify the file’s type. For example, the header of a JPEG file,  is `0xFF 0xD8` and the file extension is either `.JPE`, `.JPEG` or `.JPG`. 

Adversaries may edit the header’s hex code and/or the file extension of a malicious payload in order to bypass file validation checks and/or input sanitization. This behavior is commonly used when payload files are transferred (e.g., [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]) and stored (e.g., [[T1608-stage_capabilities#^t1608001-upload-malware|T1608.001: Upload Malware]]) so that adversaries may move their malware without triggering detections. 

Common non-executable file types and extensions, such as text files (`.txt`) and image files (`.jpg`, `.gif`, etc.) may be typically treated as benign.  Based on this, adversaries may use a file extension to disguise malware, such as naming a PHP backdoor code with a file name of `test.gif`. A user may not know that a file is malicious due to the benign appearance and file extension.

Polyglot files, which are files that have multiple different file types and that function differently based on the application that will execute them, may also be used to disguise malicious malware and capabilities.(Citation: polygot_icedID)

### T1036.009: Break Process Trees

^t1036009-break-process-trees

An adversary may attempt to evade process tree-based analysis by modifying executed malware's parent process ID (PPID). If endpoint protection software leverages the “parent-child" relationship for detection, breaking this relationship could result in the adversary’s behavior not being associated with previous process tree activity. On Unix-based systems breaking this process tree is common practice for administrators to execute software using scripts and programs.(Citation: 3OHA double-fork 2022) 

On Linux systems, adversaries may execute a series of [[T1106-native_api|T1106: Native API]] calls to alter malware's process tree. For example, adversaries can execute their payload without any arguments, call the `fork()` API call twice, then have the parent process exit. This creates a grandchild process with no parent process that is immediately adopted by the `init` system process (PID 1), which successfully disconnects the execution of the adversary's payload from its previous process tree.

Another example is using the “daemon” syscall to detach from the current parent process and run in the background.(Citation: Sandfly BPFDoor 2022)(Citation: Microsoft XorDdos Linux Stealth 2022) 

### T1036.010: Masquerade Account Name

^t1036010-masquerade-account-name

Adversaries may match or approximate the names of legitimate accounts to make newly created ones appear benign. This will typically occur during [[T1136-create_account|T1136: Create Account]], although accounts may also be renamed at a later date. This may also coincide with [[T1531-account_access_removal|T1531: Account Access Removal]] if the actor first deletes an account before re-creating one with the same name.(Citation: Huntress MOVEit 2023)

Often, adversaries will attempt to masquerade as service accounts, such as those associated with legitimate software, data backups, or container cluster management.(Citation: Elastic CUBA Ransomware 2022)(Citation: Aquasec Kubernetes Attack 2023) They may also give accounts generic, trustworthy names, such as “admin”, “help”, or “root.”(Citation: Invictus IR Cloud Ransomware 2024) Sometimes adversaries may model account names off of those already existing in the system, as a follow-on behavior to [[T1087-account_discovery|T1087: Account Discovery]].  

Note that this is distinct from [[T1656-impersonation|T1656: Impersonation]], which describes impersonating specific trusted individuals or organizations, rather than user or service account names.  

### T1036.011: Overwrite Process Arguments

^t1036011-overwrite-process-arguments

Adversaries may modify a process's in-memory arguments to change its name in order to appear as a legitimate or benign process. On Linux, the operating system stores command-line arguments in the process’s stack and passes them to the `main()` function as the `argv` array. The first element, `argv[0]`, typically contains the process name or path - by default, the command used to actually start the process (e.g., `cat /etc/passwd`). By default, the Linux `/proc` filesystem uses this value to represent the process name. The `/proc/<PID>/cmdline` file reflects the contents of this memory, and tools like `ps` use it to display process information. Since arguments are stored in user-space memory at launch, this modification can be performed without elevated privileges. 

During runtime, adversaries can erase the memory used by all command-line arguments for a process, overwriting each argument string with null bytes. This removes evidence of how the process was originally launched. They can then write a spoofed string into the memory region previously occupied by `argv[0]` to mimic a benign command, such as `cat resolv.conf`. The new command-line string is reflected in `/proc/<PID>/cmdline` and displayed by tools like `ps`.(Citation: Sandfly BPFDoor 2022)(Citation: Microsoft XorDdos Linux Stealth 2022) 

### T1036.012: Browser Fingerprint

^t1036012-browser-fingerprint

Adversaries may attempt to blend in with legitimate traffic by spoofing browser and system attributes like operating system, system language, platform, user-agent string, resolution, time zone, etc.  The HTTP User-Agent request header is a string that lets servers and network peers identify the application, operating system, vendor, and/or version of the requesting user agent.(Citation: Mozilla User Agent)

Adversaries may gather this information through [[T1082-system_information_discovery|T1082: System Information Discovery]] or by users navigating to adversary-controlled websites, and then use that information to craft their web traffic to evade defenses.(Citation: Gummy Browsers: Targeted Browser Spoofing against State-of-the-Art Fingerprinting Techniques)

## Mitigations

- [[M1017-user_training|M1017: User Training]]
- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1022-restrict_file_and_directory_permissions|M1022: Restrict File and Directory Permissions]]
- [[M1038-execution_prevention|M1038: Execution Prevention]]
- [[M1040-behavior_prevention_on_endpoint|M1040: Behavior Prevention on Endpoint]]
- [[M1045-code_signing|M1045: Code Signing]]
- [[M1047-audit|M1047: Audit]]
- [[M1049-antivirus_antimalware|M1049: Antivirus/Antimalware]]

## Platforms

- Containers
- ESXi
- Linux
- macOS
- Windows

