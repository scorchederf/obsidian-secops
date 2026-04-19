---
id: T1564
name: Hide Artifacts
created: 2020-02-26 17:41:25.933000+00:00
modified: 2025-10-24 17:48:31.407000+00:00
type: attack-pattern
x_mitre_version: 1.4
x_mitre_domains: enterprise-attack
---

## Tactic

- [[defense_evasion|Defense Evasion]]

Adversaries may attempt to hide artifacts associated with their behaviors to evade detection. Operating systems may have features to hide various artifacts, such as important system files and administrative task execution, to avoid disrupting user work environments and prevent users from changing files or features on the system. Adversaries may abuse these features to hide artifacts such as files, directories, user accounts, or other system activity to evade detection.(Citation: Sofacy Komplex Trojan)(Citation: Cybereason OSX Pirrit)(Citation: MalwareBytes ADS July 2015)

Adversaries may also attempt to hide artifacts associated with malicious behavior by creating computing regions that are isolated from common security instrumentation, such as through the use of virtualization technology.(Citation: Sophos Ragnar May 2020)

## Subtechniques

### T1564.001: Hidden Files and Directories

^t1564001-hidden-files-and-directories

**Parent Technique**
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may set files and directories to be hidden to evade detection mechanisms. To prevent normal users from accidentally changing special files on a system, most operating systems have the concept of a ‘hidden’ file. These files don’t show up when a user browses the file system with a GUI or when using normal commands on the command line. Users must explicitly ask to show the hidden files either via a series of Graphical User Interface (GUI) prompts or with command line switches (<code>dir /a</code> for Windows and <code>ls –a</code> for Linux and macOS).

On Linux and Mac, users can mark specific files as hidden simply by putting a “.” as the first character in the file or folder name  (Citation: Sofacy Komplex Trojan) (Citation: Antiquated Mac Malware). Files and folders that start with a period, ‘.’, are by default hidden from being viewed in the Finder application and standard command-line utilities like “ls”. Users must specifically change settings to have these files viewable.

Files on macOS can also be marked with the UF_HIDDEN flag which prevents them from being seen in Finder.app, but still allows them to be seen in Terminal.app (Citation: WireLurker). On Windows, users can mark specific files as hidden by using the attrib.exe binary. Many applications create these hidden files and folders to store information so that it doesn’t clutter up the user’s workspace. For example, SSH utilities create a .ssh folder that’s hidden and contains the user’s known hosts and keys.

Additionally, adversaries may name files in a manner that would allow the file to be hidden such as naming a file only a “space” character.

Adversaries can use this to their advantage to hide files and folders anywhere on the system and evading a typical user or system analysis that does not incorporate investigation of hidden files.

### T1564.002: Hidden Users

^t1564002-hidden-users

**Parent Technique**
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may use hidden users to hide the presence of user accounts they create or modify. Administrators may want to hide users when there are many user accounts on a given system or if they want to hide their administrative or other management accounts from other users. 

In macOS, adversaries can create or modify a user to be hidden through manipulating plist files, folder attributes, and user attributes. To prevent a user from being shown on the login screen and in System Preferences, adversaries can set the userID to be under 500 and set the key value <code>Hide500Users</code> to <code>TRUE</code> in the <code>/Library/Preferences/com.apple.loginwindow</code> plist file.(Citation: Cybereason OSX Pirrit) Every user has a userID associated with it. When the <code>Hide500Users</code> key value is set to <code>TRUE</code>, users with a userID under 500 do not appear on the login screen and in System Preferences. Using the command line, adversaries can use the <code>dscl</code> utility to create hidden user accounts by setting the <code>IsHidden</code> attribute to <code>1</code>. Adversaries can also hide a user’s home folder by changing the <code>chflags</code> to hidden.(Citation: Apple Support Hide a User Account) 

Adversaries may similarly hide user accounts in Windows. Adversaries can set the <code>HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList</code> Registry key value to <code>0</code> for a specific user to prevent that user from being listed on the logon screen.(Citation: FireEye SMOKEDHAM June 2021)(Citation: US-CERT TA18-074A)

On Linux systems, adversaries may hide user accounts from the login screen, also referred to as the greeter. The method an adversary may use depends on which Display Manager the distribution is currently using. For example, on an Ubuntu system using the GNOME Display Manger (GDM), accounts may be hidden from the greeter using the <code>gsettings</code> command (ex: <code>sudo -u gdm gsettings set org.gnome.login-screen disable-user-list true</code>).(Citation: Hide GDM User Accounts) Display Managers are not anchored to specific distributions and may be changed by a user or adversary.

### T1564.003: Hidden Window

^t1564003-hidden-window

**Parent Technique**
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may use hidden windows to conceal malicious activity from the plain sight of users. In some cases, windows that would typically be displayed when an application carries out an operation can be hidden. This may be utilized by system administrators to avoid disrupting user work environments when carrying out administrative tasks. 

Adversaries may abuse these functionalities to hide otherwise visible windows from users so as not to alert the user to adversary activity on the system.(Citation: Antiquated Mac Malware)

On macOS, the configurations for how applications run are listed in property list (plist) files. One of the tags in these files can be <code>apple.awt.UIElement</code>, which allows for Java applications to prevent the application's icon from appearing in the Dock. A common use for this is when applications run in the system tray, but don't also want to show up in the Dock.

Similarly, on Windows there are a variety of features in scripting languages, such as [PowerShell](https://attack.mitre.org/techniques/T1059/001), Jscript, and [Visual Basic](https://attack.mitre.org/techniques/T1059/005) to make windows hidden. One example of this is <code>powershell.exe -WindowStyle Hidden</code>.(Citation: PowerShell About 2019)

The Windows Registry can also be edited to hide application windows from the current user. For example, by setting the `WindowPosition` subkey in the `HKEY_CURRENT_USER\Console\%SystemRoot%_System32_WindowsPowerShell_v1.0_PowerShell.exe` Registry key to a maximum value, PowerShell windows will open off screen and be hidden.(Citation: Cantoris Computing)

In addition, Windows supports the `CreateDesktop()` API that can create a hidden desktop window with its own corresponding <code>explorer.exe</code> process.(Citation: Hidden VNC)(Citation: Anatomy of an hVNC Attack)  All applications running on the hidden desktop window, such as a hidden VNC (hVNC) session,(Citation: Hidden VNC) will be invisible to other desktops windows.

Adversaries may also leverage cmd.exe(Citation: Cybereason - Hidden Malicious Remote Access) as a parent process, and then utilize a LOLBin, such as DeviceCredentialDeployment.exe,(Citation: LOLBAS Project GitHub Device Cred Dep)(Citation: SecureList BlueNoroff Device Cred Dev) to hide windows.

### T1564.004: NTFS File Attributes

^t1564004-ntfs-file-attributes

**Parent Technique**
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may use NTFS file attributes to hide their malicious data in order to evade detection. Every New Technology File System (NTFS) formatted partition contains a Master File Table (MFT) that maintains a record for every file/directory on the partition. (Citation: SpectorOps Host-Based Jul 2017) Within MFT entries are file attributes, (Citation: Microsoft NTFS File Attributes Aug 2010) such as Extended Attributes (EA) and Data [known as Alternate Data Streams (ADSs) when more than one Data attribute is present], that can be used to store arbitrary data (and even complete files). (Citation: SpectorOps Host-Based Jul 2017) (Citation: Microsoft File Streams) (Citation: MalwareBytes ADS July 2015) (Citation: Microsoft ADS Mar 2014)

Adversaries may store malicious data or binaries in file attribute metadata instead of directly in files. This may be done to evade some defenses, such as static indicator scanning tools and anti-virus. (Citation: Journey into IR ZeroAccess NTFS EA) (Citation: MalwareBytes ADS July 2015)

### T1564.005: Hidden File System

^t1564005-hidden-file-system

**Parent Technique**
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may use a hidden file system to conceal malicious activity from users and security tools. File systems provide a structure to store and access data from physical storage. Typically, a user engages with a file system through applications that allow them to access files and directories, which are an abstraction from their physical location (ex: disk sector). Standard file systems include FAT, NTFS, ext4, and APFS. File systems can also contain other structures, such as the Volume Boot Record (VBR) and Master File Table (MFT) in NTFS.(Citation: MalwareTech VFS Nov 2014)

Adversaries may use their own abstracted file system, separate from the standard file system present on the infected system. In doing so, adversaries can hide the presence of malicious components and file input/output from security tools. Hidden file systems, sometimes referred to as virtual file systems, can be implemented in numerous ways. One implementation would be to store a file system in reserved disk space unused by disk structures or standard file system partitions.(Citation: MalwareTech VFS Nov 2014)(Citation: FireEye Bootkits) Another implementation could be for an adversary to drop their own portable partition image as a file on top of the standard file system.(Citation: ESET ComRAT May 2020) Adversaries may also fragment files across the existing file system structure in non-standard ways.(Citation: Kaspersky Equation QA)

### T1564.006: Run Virtual Instance

^t1564006-run-virtual-instance

**Parent Technique**
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may carry out malicious operations using a virtual instance to avoid detection. A wide variety of virtualization technologies exist that allow for the emulation of a computer or computing environment. By running malicious code inside of a virtual instance, adversaries can hide artifacts associated with their behavior from security tools that are unable to monitor activity inside the virtual instance.(Citation: CyberCX Akira Ransomware) Additionally, depending on the virtual networking implementation (ex: bridged adapter), network traffic generated by the virtual instance can be difficult to trace back to the compromised host as the IP address and hostname might not match known values.(Citation: SingHealth Breach Jan 2019)

Adversaries may utilize native support for virtualization (ex: Hyper-V), deploy lightweight emulators (ex: QEMU), or drop the necessary files to run a virtual instance (ex: VirtualBox binaries).(Citation: Securonix CronTrap 2024) After running a virtual instance, adversaries may create a shared folder between the guest and host with permissions that enable the virtual instance to interact with the host file system.(Citation: Sophos Ragnar May 2020)

Threat actors may also leverage temporary virtualized environments such as the Windows Sandbox, which supports the use of `.wsb` configuration files for defining execution parameters. For example, the `<MappedFolder>` property supports the creation of a shared folder, while the `<LogonCommand>` property allows the specification of a payload.(Citation: ESET MirrorFace 2025)(Citation: ITOCHU Hack the Sandbox)(Citation: ITOCHU Sandbox PPT)

In VMWare environments, adversaries may leverage the vCenter console to create new virtual machines. However, they may also create virtual machines directly on ESXi servers by running a valid `.vmx` file with the `/bin/vmx` utility. Adding this command to `/etc/rc.local.d/local.sh` (i.e., [RC Scripts](https://attack.mitre.org/techniques/T1037/004)) will cause the VM to persistently restart.(Citation: vNinja Rogue VMs 2024) Creating a VM this way prevents it from appearing in the vCenter console or in the output to the `vim-cmd vmsvc/getallvms` command on the ESXi server, thereby hiding it from typical administrative activities.(Citation: MITRE VMware Abuse 2024)

### T1564.007: VBA Stomping

^t1564007-vba-stomping

**Parent Technique**
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may hide malicious Visual Basic for Applications (VBA) payloads embedded within MS Office documents by replacing the VBA source code with benign data.(Citation: FireEye VBA stomp Feb 2020)

MS Office documents with embedded VBA content store source code inside of module streams. Each module stream has a <code>PerformanceCache</code> that stores a separate compiled version of the VBA source code known as p-code. The p-code is executed when the MS Office version specified in the <code>_VBA_PROJECT</code> stream (which contains the version-dependent description of the VBA project) matches the version of the host MS Office application.(Citation: Evil Clippy May 2019)(Citation: Microsoft _VBA_PROJECT Stream)

An adversary may hide malicious VBA code by overwriting the VBA source code location with zero’s, benign code, or random bytes while leaving the previously compiled malicious p-code. Tools that scan for malicious VBA source code may be bypassed as the unwanted code is hidden in the compiled p-code. If the VBA source code is removed, some tools might even think that there are no macros present. If there is a version match between the <code>_VBA_PROJECT</code> stream and host MS Office application, the p-code will be executed, otherwise the benign VBA source code will be decompressed and recompiled to p-code, thus removing malicious p-code and potentially bypassing dynamic analysis.(Citation: Walmart Roberts Oct 2018)(Citation: FireEye VBA stomp Feb 2020)(Citation: pcodedmp Bontchev)

### T1564.008: Email Hiding Rules

^t1564008-email-hiding-rules

**Parent Technique**
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may use email rules to hide inbound emails in a compromised user's mailbox. Many email clients allow users to create inbox rules for various email functions, including moving emails to other folders, marking emails as read, or deleting emails. Rules may be created or modified within email clients or through external features such as the <code>New-InboxRule</code> or <code>Set-InboxRule</code> [PowerShell](https://attack.mitre.org/techniques/T1059/001) cmdlets on Windows systems.(Citation: Microsoft Inbox Rules)(Citation: MacOS Email Rules)(Citation: Microsoft New-InboxRule)(Citation: Microsoft Set-InboxRule)

Adversaries may utilize email rules within a compromised user's mailbox to delete and/or move emails to less noticeable folders. Adversaries may do this to hide security alerts, C2 communication, or responses to [Internal Spearphishing](https://attack.mitre.org/techniques/T1534) emails sent from the compromised account.

Any user or administrator within the organization (or adversary with valid credentials) may be able to create rules to automatically move or delete emails. These rules can be abused to impair/delay detection had the email content been immediately seen by a user or defender. Malicious rules commonly filter out emails based on key words (such as <code>malware</code>, <code>suspicious</code>, <code>phish</code>, and <code>hack</code>) found in message bodies and subject lines. (Citation: Microsoft Cloud App Security)

In some environments, administrators may be able to enable email rules that operate organization-wide rather than on individual inboxes. For example, Microsoft Exchange supports transport rules that evaluate all mail an organization receives against user-specified conditions, then performs a user-specified action on mail that adheres to those conditions.(Citation: Microsoft Mail Flow Rules 2023) Adversaries that abuse such features may be able to automatically modify or delete all emails related to specific topics (such as internal security incident notifications).

### T1564.009: Resource Forking

^t1564009-resource-forking

**Parent Technique**
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may abuse resource forks to hide malicious code or executables to evade detection and bypass security applications. A resource fork provides applications a structured way to store resources such as thumbnail images, menu definitions, icons, dialog boxes, and code.(Citation: macOS Hierarchical File System Overview) Usage of a resource fork is identifiable when displaying a file’s extended attributes, using <code>ls -l@</code> or <code>xattr -l</code> commands. Resource forks have been deprecated and replaced with the application bundle structure. Non-localized resources are placed at the top level directory of an application bundle, while localized resources are placed in the <code>/Resources</code> folder.(Citation: Resource and Data Forks)(Citation: ELC Extended Attributes)

Adversaries can use resource forks to hide malicious data that may otherwise be stored directly in files. Adversaries can execute content with an attached resource fork, at a specified offset, that is moved to an executable location then invoked. Resource fork content may also be obfuscated/encrypted until execution.(Citation: sentinellabs resource named fork 2020)(Citation: tau bundlore erika noerenberg 2020)

### T1564.010: Process Argument Spoofing

^t1564010-process-argument-spoofing

**Parent Technique**
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may attempt to hide process command-line arguments by overwriting process memory. Process command-line arguments are stored in the process environment block (PEB), a data structure used by Windows to store various information about/used by a process. The PEB includes the process command-line arguments that are referenced when executing the process. When a process is created, defensive tools/sensors that monitor process creations may retrieve the process arguments from the PEB.(Citation: Microsoft PEB 2021)(Citation: Xpn Argue Like Cobalt 2019)

Adversaries may manipulate a process PEB to evade defenses. For example, [Process Hollowing](https://attack.mitre.org/techniques/T1055/012) can be abused to spawn a process in a suspended state with benign arguments. After the process is spawned and the PEB is initialized (and process information is potentially logged by tools/sensors), adversaries may override the PEB to modify the command-line arguments (ex: using the [Native API](https://attack.mitre.org/techniques/T1106) <code>WriteProcessMemory()</code> function) then resume process execution with malicious arguments.(Citation: Cobalt Strike Arguments 2019)(Citation: Xpn Argue Like Cobalt 2019)(Citation: Nviso Spoof Command Line 2020)

Adversaries may also execute a process with malicious command-line arguments then patch the memory with benign arguments that may bypass subsequent process memory analysis.(Citation: FireEye FiveHands April 2021)

This behavior may also be combined with other tricks (such as [Parent PID Spoofing](https://attack.mitre.org/techniques/T1134/004)) to manipulate or further evade process-based detections.

### T1564.011: Ignore Process Interrupts

^t1564011-ignore-process-interrupts

**Parent Technique**
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may evade defensive mechanisms by executing commands that hide from process interrupt signals. Many operating systems use signals to deliver messages to control process behavior. Command interpreters often include specific commands/flags that ignore errors and other hangups, such as when the user of the active session logs off.(Citation: Linux Signal Man)  These interrupt signals may also be used by defensive tools and/or analysts to pause or terminate specified running processes. 

Adversaries may invoke processes using `nohup`, [PowerShell](https://attack.mitre.org/techniques/T1059/001) `-ErrorAction SilentlyContinue`, or similar commands that may be immune to hangups.(Citation: nohup Linux Man)(Citation: Microsoft PowerShell SilentlyContinue) This may enable malicious commands and malware to continue execution through system events that would otherwise terminate its execution, such as users logging off or the termination of its C2 network connection.

Hiding from process interrupt signals may allow malware to continue execution, but unlike [Trap](https://attack.mitre.org/techniques/T1546/005) this does not establish [Persistence](https://attack.mitre.org/tactics/TA0003) since the process will not be re-invoked once actually terminated.

### T1564.012: File/Path Exclusions

^t1564012-file-path-exclusions

**Parent Technique**
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may attempt to hide their file-based artifacts by writing them to specific folders or file names excluded from antivirus (AV) scanning and other defensive capabilities. AV and other file-based scanners often include exclusions to optimize performance as well as ease installation and legitimate use of applications. These exclusions may be contextual (e.g., scans are only initiated in response to specific triggering events/alerts), but are also often hardcoded strings referencing specific folders and/or files assumed to be trusted and legitimate.(Citation: Microsoft File Folder Exclusions)

Adversaries may abuse these exclusions to hide their file-based artifacts. For example, rather than  tampering with tool settings to add a new exclusion (i.e., [Disable or Modify Tools](https://attack.mitre.org/techniques/T1562/001)), adversaries may drop their file-based payloads in default or otherwise well-known exclusions. Adversaries may also use [Security Software Discovery](https://attack.mitre.org/techniques/T1518/001) and other [Discovery](https://attack.mitre.org/tactics/TA0007)/[Reconnaissance](https://attack.mitre.org/tactics/TA0043) activities to both discover and verify existing exclusions in a victim environment.

### T1564.013: Bind Mounts

^t1564013-bind-mounts

**Parent Technique**
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may abuse bind mounts on file structures to hide their activity and artifacts from native utilities. A bind mount maps a directory or file from one location on the filesystem to another, similar to a shortcut on Windows. It’s commonly used to provide access to specific files or directories across different environments, such as inside containers or chroot environments, and requires sudo access. 

Adversaries may use bind mounts to map either an empty directory or a benign `/proc` directory to a malicious process’s `/proc` directory. Using the commands `mount –o bind /proc/benign-process /proc/malicious-process` (or `mount –B`), the malicious process's `/proc` directory is overlayed with the contents of a benign process's `/proc` directory. When system utilities query process activity, such as `ps` and `top`, the kernel follows the bind mount and presents the benign directory’s contents instead of the malicious process's actual `/proc` directory. As a result, these utilities display information that appears to come from the benign process, effectively hiding the malicious process's metadata, executable, or other artifacts from detection.(Citation: Cado Security Commando Cat 2024)(Citation: Ahn Lab CoinMiner 2023)

### T1564.014: Extended Attributes

^t1564014-extended-attributes

**Parent Technique**
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may abuse extended attributes (xattrs) on macOS and Linux to hide their malicious data in order to evade detection. Extended attributes are key-value pairs of file and directory metadata used by both macOS and Linux. They are not visible through standard tools like `Finder`,  `ls`, or `cat` and require utilities such as `xattr` (macOS) or `getfattr` (Linux) for inspection. Operating systems and applications use xattrs for tagging, integrity checks, and access control. On Linux, xattrs are organized into namespaces such as `user.` (user permissions), `trusted.` (root permissions), `security.`, and `system.`, each with specific permissions. On macOS, xattrs are flat strings without namespace prefixes, commonly prefixed with `com.apple.*` (e.g., `com.apple.quarantine`, `com.apple.metadata:_kMDItemUserTags`) and used by system features like Gatekeeper and Spotlight.(Citation: Establishing persistence using extended attributes on Linux)

An adversary may leverage xattrs by embedding a second-stage payload into the extended attribute of a legitimate file. On macOS, a payload can be embedded into a custom attribute using the `xattr` command. A separate loader can retrieve the attribute with `xattr -p`, decode the content, and execute it using a scripting interpreter. On Linux, an adversary may use `setfattr` to write a payload into the `user.` namespace of a legitimate file. A loader script can later extract the payload with `getfattr --only-values`, decode it, and execute it using bash or another interpreter. In both cases, because the primary file content remains unchanged, security tools and integrity checks that do not inspect extended attributes will observe the original file hash, allowing the malicious payload to evade detection.(Citation: Low GroupIB xattrs nov 2024)

## Mitigations

- [[M1013-application_developer_guidance|M1013: Application Developer Guidance]]
- [[M1033-limit_software_installation|M1033: Limit Software Installation]]
- [[M1047-audit|M1047: Audit]]
- [[M1049-antivirus_antimalware|M1049: Antivirus/Antimalware]]

## Platforms

- Linux
- Office Suite
- Windows
- macOS
- ESXi

