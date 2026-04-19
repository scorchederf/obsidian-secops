---
id: T1036
name: Masquerading
created: 2017-05-31 21:30:38.511000+00:00
modified: 2025-10-24 17:48:42.609000+00:00
type: attack-pattern
x_mitre_version: 1.8
x_mitre_domains: enterprise-attack
---

## Tactic

- [[defense_evasion|Defense Evasion]]

Adversaries may attempt to manipulate features of their artifacts to make them appear legitimate or benign to users and/or security tools. Masquerading occurs when the name or location of an object, legitimate or malicious, is manipulated or abused for the sake of evading defenses and observation. This may include manipulating file metadata, tricking users into misidentifying the file type, and giving legitimate task or service names.

Renaming abusable system utilities to evade security monitoring is also a form of [Masquerading](https://attack.mitre.org/techniques/T1036).(Citation: LOLBAS Main Site)

## Subtechniques

### T1036.001: Invalid Code Signature

^t1036001-invalid-code-signature

**Parent Technique**
- [[T1036-masquerading|T1036: Masquerading]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may attempt to mimic features of valid code signatures to increase the chance of deceiving a user, analyst, or tool. Code signing provides a level of authenticity on a binary from the developer and a guarantee that the binary has not been tampered with. Adversaries can copy the metadata and signature information from a signed program, then use it as a template for an unsigned program. Files with invalid code signatures will fail digital signature validation checks, but they may appear more legitimate to users and security tools may improperly handle these files.(Citation: Threatexpress MetaTwin 2017)

Unlike [Code Signing](https://attack.mitre.org/techniques/T1553/002), this activity will not result in a valid signature.

### T1036.002: Right-to-Left Override

^t1036002-right-to-left-override

**Parent Technique**
- [[T1036-masquerading|T1036: Masquerading]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may abuse the right-to-left override (RTLO or RLO) character (U+202E) to disguise a string and/or file name to make it appear benign. RTLO is a non-printing Unicode character that causes the text that follows it to be displayed in reverse. For example, a Windows screensaver executable named <code>March 25 \u202Excod.scr</code> will display as <code>March 25 rcs.docx</code>. A JavaScript file named <code>photo_high_re\u202Egnp.js</code> will be displayed as <code>photo_high_resj.png</code>.(Citation: Infosecinstitute RTLO Technique)

Adversaries may abuse the RTLO character as a means of tricking a user into executing what they think is a benign file type. A common use of this technique is with [Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001)/[Malicious File](https://attack.mitre.org/techniques/T1204/002) since it can trick both end users and defenders if they are not aware of how their tools display and render the RTLO character. Use of the RTLO character has been seen in many targeted intrusion attempts and criminal activity.(Citation: Trend Micro PLEAD RTLO)(Citation: Kaspersky RTLO Cyber Crime) RTLO can be used in the Windows Registry as well, where regedit.exe displays the reversed characters but the command line tool reg.exe does not by default.

### T1036.003: Rename Legitimate Utilities

^t1036003-rename-legitimate-utilities

**Parent Technique**
- [[T1036-masquerading|T1036: Masquerading]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may rename legitimate / system utilities to try to evade security mechanisms concerning the usage of those utilities. Security monitoring and control mechanisms may be in place for legitimate utilities adversaries are capable of abusing, including both built-in binaries and tools such as PSExec, AutoHotKey, and IronPython.(Citation: LOLBAS Main Site)(Citation: Huntress Python Malware 2025)(Citation: The DFIR Report AutoHotKey 2023)(Citation: Splunk Detect Renamed PSExec) It may be possible to bypass those security mechanisms by renaming the utility prior to utilization (ex: rename <code>rundll32.exe</code>).(Citation: Elastic Masquerade Ball) An alternative case occurs when a legitimate utility is copied or moved to a different directory and renamed to avoid detections based on these utilities executing from non-standard paths.(Citation: F-Secure CozyDuke)

### T1036.004: Masquerade Task or Service

^t1036004-masquerade-task-or-service

**Parent Technique**
- [[T1036-masquerading|T1036: Masquerading]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may attempt to manipulate the name of a task or service to make it appear legitimate or benign. Tasks/services executed by the Task Scheduler or systemd will typically be given a name and/or description.(Citation: TechNet Schtasks)(Citation: Systemd Service Units) Windows services will have a service name as well as a display name. Many benign tasks and services exist that have commonly associated names. Adversaries may give tasks or services names that are similar or identical to those of legitimate ones.

Tasks or services contain other fields, such as a description, that adversaries may attempt to make appear legitimate.(Citation: Palo Alto Shamoon Nov 2016)(Citation: Fysbis Dr Web Analysis)

### T1036.005: Match Legitimate Resource Name or Location

^t1036005-match-legitimate-resource-name-or-location

**Parent Technique**
- [[T1036-masquerading|T1036: Masquerading]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may match or approximate the name or location of legitimate files, Registry keys, or other resources when naming/placing them. This is done for the sake of evading defenses and observation. 

This may be done by placing an executable in a commonly trusted directory (ex: under System32) or giving it the name of a legitimate, trusted program (ex: `svchost.exe`). Alternatively, a Windows Registry key may be given a close approximation to a key used by a legitimate program. In containerized environments, a threat actor may create a resource in a trusted namespace or one that matches the naming convention of a container pod or cluster.(Citation: Aquasec Kubernetes Backdoor 2023)

### T1036.006: Space after Filename

^t1036006-space-after-filename

**Parent Technique**
- [[T1036-masquerading|T1036: Masquerading]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries can hide a program's true filetype by changing the extension of a file. With certain file types (specifically this does not work with .app extensions), appending a space to the end of a filename will change how the file is processed by the operating system.

For example, if there is a Mach-O executable file called <code>evil.bin</code>, when it is double clicked by a user, it will launch Terminal.app and execute. If this file is renamed to <code>evil.txt</code>, then when double clicked by a user, it will launch with the default text editing application (not executing the binary). However, if the file is renamed to <code>evil.txt </code> (note the space at the end), then when double clicked by a user, the true file type is determined by the OS and handled appropriately and the binary will be executed (Citation: Mac Backdoors are back).

Adversaries can use this feature to trick users into double clicking benign-looking files of any format and ultimately executing something malicious.

### T1036.007: Double File Extension

^t1036007-double-file-extension

**Parent Technique**
- [[T1036-masquerading|T1036: Masquerading]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may abuse a double extension in the filename as a means of masquerading the true file type. A file name may include a secondary file type extension that may cause only the first extension to be displayed (ex: <code>File.txt.exe</code> may render in some views as just <code>File.txt</code>). However, the second extension is the true file type that determines how the file is opened and executed. The real file extension may be hidden by the operating system in the file browser (ex: explorer.exe), as well as in any software configured using or similar to the system’s policies.(Citation: PCMag DoubleExtension)(Citation: SOCPrime DoubleExtension) 

Adversaries may abuse double extensions to attempt to conceal dangerous file types of payloads. A very common usage involves tricking a user into opening what they think is a benign file type but is actually executable code. Such files often pose as email attachments and allow an adversary to gain [Initial Access](https://attack.mitre.org/tactics/TA0001) into a user’s system via [Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001) then [User Execution](https://attack.mitre.org/techniques/T1204). For example, an executable file attachment named <code>Evil.txt.exe</code> may display as <code>Evil.txt</code> to a user. The user may then view it as a benign text file and open it, inadvertently executing the hidden malware.(Citation: SOCPrime DoubleExtension)

Common file types, such as text files (.txt, .doc, etc.) and image files (.jpg, .gif, etc.) are typically used as the first extension to appear benign. Executable extensions commonly regarded as dangerous, such as .exe, .lnk, .hta, and .scr, often appear as the second extension and true file type.

### T1036.008: Masquerade File Type

^t1036008-masquerade-file-type

**Parent Technique**
- [[T1036-masquerading|T1036: Masquerading]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may masquerade malicious payloads as legitimate files through changes to the payload's formatting, including the file’s signature, extension, icon, and contents. Various file types have a typical standard format, including how they are encoded and organized. For example, a file’s signature (also known as header or magic bytes) is the beginning bytes of a file and is often used to identify the file’s type. For example, the header of a JPEG file,  is <code> 0xFF 0xD8</code> and the file extension is either `.JPE`, `.JPEG` or `.JPG`. 

Adversaries may edit the header’s hex code and/or the file extension of a malicious payload in order to bypass file validation checks and/or input sanitization. This behavior is commonly used when payload files are transferred (e.g., [Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105)) and stored (e.g., [Upload Malware](https://attack.mitre.org/techniques/T1608/001)) so that adversaries may move their malware without triggering detections. 

Common non-executable file types and extensions, such as text files (`.txt`) and image files (`.jpg`, `.gif`, etc.) may be typically treated as benign.  Based on this, adversaries may use a file extension to disguise malware, such as naming a PHP backdoor code with a file name of <code>test.gif</code>. A user may not know that a file is malicious due to the benign appearance and file extension.

Polyglot files, which are files that have multiple different file types and that function differently based on the application that will execute them, may also be used to disguise malicious malware and capabilities.(Citation: polygot_icedID)

### T1036.009: Break Process Trees

^t1036009-break-process-trees

**Parent Technique**
- [[T1036-masquerading|T1036: Masquerading]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

An adversary may attempt to evade process tree-based analysis by modifying executed malware's parent process ID (PPID). If endpoint protection software leverages the “parent-child" relationship for detection, breaking this relationship could result in the adversary’s behavior not being associated with previous process tree activity. On Unix-based systems breaking this process tree is common practice for administrators to execute software using scripts and programs.(Citation: 3OHA double-fork 2022) 

On Linux systems, adversaries may execute a series of [Native API](https://attack.mitre.org/techniques/T1106) calls to alter malware's process tree. For example, adversaries can execute their payload without any arguments, call the `fork()` API call twice, then have the parent process exit. This creates a grandchild process with no parent process that is immediately adopted by the `init` system process (PID 1), which successfully disconnects the execution of the adversary's payload from its previous process tree.

Another example is using the “daemon” syscall to detach from the current parent process and run in the background.(Citation: Sandfly BPFDoor 2022)(Citation: Microsoft XorDdos Linux Stealth 2022) 

### T1036.010: Masquerade Account Name

^t1036010-masquerade-account-name

**Parent Technique**
- [[T1036-masquerading|T1036: Masquerading]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may match or approximate the names of legitimate accounts to make newly created ones appear benign. This will typically occur during [Create Account](https://attack.mitre.org/techniques/T1136), although accounts may also be renamed at a later date. This may also coincide with [Account Access Removal](https://attack.mitre.org/techniques/T1531) if the actor first deletes an account before re-creating one with the same name.(Citation: Huntress MOVEit 2023)

Often, adversaries will attempt to masquerade as service accounts, such as those associated with legitimate software, data backups, or container cluster management.(Citation: Elastic CUBA Ransomware 2022)(Citation: Aquasec Kubernetes Attack 2023) They may also give accounts generic, trustworthy names, such as “admin”, “help”, or “root.”(Citation: Invictus IR Cloud Ransomware 2024) Sometimes adversaries may model account names off of those already existing in the system, as a follow-on behavior to [Account Discovery](https://attack.mitre.org/techniques/T1087).  

Note that this is distinct from [Impersonation](https://attack.mitre.org/techniques/T1656), which describes impersonating specific trusted individuals or organizations, rather than user or service account names.  

### T1036.011: Overwrite Process Arguments

^t1036011-overwrite-process-arguments

**Parent Technique**
- [[T1036-masquerading|T1036: Masquerading]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may modify a process's in-memory arguments to change its name in order to appear as a legitimate or benign process. On Linux, the operating system stores command-line arguments in the process’s stack and passes them to the `main()` function as the `argv` array. The first element, `argv[0]`, typically contains the process name or path - by default, the command used to actually start the process (e.g., `cat /etc/passwd`). By default, the Linux `/proc` filesystem uses this value to represent the process name. The `/proc/<PID>/cmdline` file reflects the contents of this memory, and tools like `ps` use it to display process information. Since arguments are stored in user-space memory at launch, this modification can be performed without elevated privileges. 

During runtime, adversaries can erase the memory used by all command-line arguments for a process, overwriting each argument string with null bytes. This removes evidence of how the process was originally launched. They can then write a spoofed string into the memory region previously occupied by `argv[0]` to mimic a benign command, such as `cat resolv.conf`. The new command-line string is reflected in `/proc/<PID>/cmdline` and displayed by tools like `ps`.(Citation: Sandfly BPFDoor 2022)(Citation: Microsoft XorDdos Linux Stealth 2022) 

### T1036.012: Browser Fingerprint

^t1036012-browser-fingerprint

**Parent Technique**
- [[T1036-masquerading|T1036: Masquerading]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may attempt to blend in with legitimate traffic by spoofing browser and system attributes like operating system, system language, platform, user-agent string, resolution, time zone, etc.  The HTTP User-Agent request header is a string that lets servers and network peers identify the application, operating system, vendor, and/or version of the requesting user agent.(Citation: Mozilla User Agent)

Adversaries may gather this information through [System Information Discovery](https://attack.mitre.org/techniques/T1082) or by users navigating to adversary-controlled websites, and then use that information to craft their web traffic to evade defenses.(Citation: Gummy Browsers: Targeted Browser Spoofing against State-of-the-Art Fingerprinting Techniques)

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

