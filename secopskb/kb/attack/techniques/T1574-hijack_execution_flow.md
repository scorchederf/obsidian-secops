---
mitre_id: "T1574"
mitre_name: "Hijack Execution Flow"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--aedfca76-3b30-4866-b2aa-0f1d7fd1e4b6"
mitre_created: "2020-03-12T20:38:12.465Z"
mitre_modified: "2025-10-24T17:49:13.820Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1574/"
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
mitre_tactic_ids:
  - "TA0003"
  - "TA0004"
  - "TA0005"
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
  - "D3-SBV"
  - "D3-SFA"
  - "D3-SICA"
  - "D3-SU"
  - "D3-SWI"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may execute their own malicious payloads by hijacking the way operating systems run programs. Hijacking execution flow can be for the purposes of persistence, since this hijacked execution may reoccur over time. Adversaries may also use these mechanisms to elevate privileges or evade defenses, such as application control or other restrictions on execution.

There are many ways an adversary may hijack the flow of execution, including by manipulating how the operating system locates programs to be executed. How the operating system locates libraries to be used by a program can also be intercepted. Locations where the operating system looks for programs/resources, such as file directories and in the case of Windows the Registry, could also be poisoned to include malicious payloads.

## Workspace

- [[workspaces/attack/techniques/T1574-hijack_execution_flow-note|Open workspace note]]

![[workspaces/attack/techniques/T1574-hijack_execution_flow-note]]

## Tactics

- [[TA0003-persistence|TA0003: Persistence]]
- [[TA0004-privilege_escalation|TA0004: Privilege Escalation]]
- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

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
- [[D3-SBV-service_binary_verification|D3-SBV: Service Binary Verification]]
- [[D3-SFA-system_file_analysis|D3-SFA: System File Analysis]]
- [[D3-SICA-system_init_config_analysis|D3-SICA: System Init Config Analysis]]
- [[D3-SU-software_update|D3-SU: Software Update]]
- [[D3-SWI-software_inventory|D3-SWI: Software Inventory]]

## Subtechniques

### T1574.001: DLL

^t1574001-dll

Adversaries may abuse dynamic-link library files (DLLs) in order to achieve persistence, escalate privileges, and evade defenses. DLLs are libraries that contain code and data that can be simultaneously utilized by multiple programs. While DLLs are not malicious by nature, they can be abused through mechanisms such as side-loading, hijacking search order, and phantom DLL hijacking.(Citation: unit 42)

Specific ways DLLs are abused by adversaries include:

### DLL Sideloading
Adversaries may execute their own malicious payloads by side-loading DLLs. Side-loading involves hijacking which DLL a program loads by planting and then invoking a legitimate application that executes their payload(s).

Side-loading positions both the victim application and malicious payload(s) alongside each other. Adversaries likely use side-loading as a means of masking actions they perform under a legitimate, trusted, and potentially elevated system or software process. Benign executables used to side-load payloads may not be flagged during delivery and/or execution. Adversary payloads may also be encrypted/packed or otherwise obfuscated until loaded into the memory of the trusted process.

Adversaries may also side-load other packages, such as BPLs (Borland Package Library).(Citation: kroll bpl)

Adversaries may chain DLL sideloading multiple times to fragment functionality hindering analysis. Adversaries using multiple DLL files can split the loader functions across different DLLs, with a main DLL loading the separated export functions. (Citation: Virus Bulletin) Spreading loader functions across multiple DLLs makes analysis harder, since all files must be collected to fully understand the malware’s behavior.  Another method implements a “loader-for-a-loader”, where a malicious DLL’s sole role is to load a second DLL (or a chain of DLLs) that contain the real payload. (Citation: Sophos)

### DLL Search Order Hijacking
Adversaries may execute their own malicious payloads by hijacking the search order that Windows uses to load DLLs. This search order is a sequence of special and standard search locations that a program checks when loading a DLL. An adversary can plant a trojan DLL in a directory that will be prioritized by the DLL search order over the location of a legitimate library. This will cause Windows to load the malicious DLL when it is called for by the victim program.(Citation: unit 42)

### DLL Redirection
Adversaries may directly modify the search order via DLL redirection, which after being enabled (in the Registry or via the creation of a redirection file) may cause a program to load a DLL from a different location.(Citation: Microsoft redirection)(Citation: Microsoft - manifests/assembly)

### Phantom DLL Hijacking
Adversaries may leverage phantom DLL hijacking by targeting references to non-existent DLL files. They may be able to load their own malicious DLL by planting it with the correct name in the location of the missing module.(Citation: Hexacorn DLL Hijacking)(Citation: Hijack DLLs CrowdStrike)

### DLL Substitution
Adversaries may target existing, valid DLL files and substitute them with their own malicious DLLs, planting them with the same name and in the same location as the valid DLL file.(Citation: Wietze Beukema DLL Hijacking)

Programs that fall victim to DLL hijacking may appear to behave normally because malicious DLLs may be configured to also load the legitimate DLLs they were meant to replace, evading defenses.

Remote DLL hijacking can occur when a program sets its current directory to a remote location, such as a Web share, before loading a DLL.(Citation: dll pre load owasp)(Citation: microsoft remote preloading)

If a valid DLL is configured to run at a higher privilege level, then the adversary-controlled DLL that is loaded will also be executed at the higher level. In this case, the technique could be used for privilege escalation.

### T1574.004: Dylib Hijacking

^t1574004-dylib-hijacking

Adversaries may execute their own payloads by placing a malicious dynamic library (dylib) with an expected name in a path a victim application searches at runtime. The dynamic loader will try to find the dylibs based on the sequential order of the search paths. Paths to dylibs may be prefixed with `@rpath`, which allows developers to use relative paths to specify an array of search paths used at runtime based on the location of the executable.  Additionally, if weak linking is used, such as the `LC_LOAD_WEAK_DYLIB` function, an application will still execute even if an expected dylib is not present. Weak linking enables developers to run an application on multiple macOS versions as new APIs are added.

Adversaries may gain execution by inserting malicious dylibs with the name of the missing dylib in the identified path.(Citation: Wardle Dylib Hijack Vulnerable Apps)(Citation: Wardle Dylib Hijacking OSX 2015)(Citation: Github EmpireProject HijackScanner)(Citation: Github EmpireProject CreateHijacker Dylib) Dylibs are loaded into an application's address space allowing the malicious dylib to inherit the application's privilege level and resources. Based on the application, this could result in privilege escalation and uninhibited network access. This method may also evade detection from security products since the execution is masked under a legitimate process.(Citation: Writing Bad Malware for OSX)(Citation: wardle artofmalware volume1)(Citation: MalwareUnicorn macOS Dylib Injection MachO)

### T1574.005: Executable Installer File Permissions Weakness

^t1574005-executable-installer-file-permissions-weakness

Adversaries may execute their own malicious payloads by hijacking the binaries used by an installer. These processes may automatically execute specific binaries as part of their functionality or to perform other actions. If the permissions on the file system directory containing a target binary, or permissions on the binary itself, are improperly set, then the target binary may be overwritten with another binary using user-level permissions and executed by the original process. If the original process and thread are running under a higher permissions level, then the replaced binary will also execute under higher-level permissions, which could include SYSTEM.

Another variation of this technique can be performed by taking advantage of a weakness that is common in executable, self-extracting installers. During the installation process, it is common for installers to use a subdirectory within the `%TEMP%` directory to unpack binaries such as DLLs, EXEs, or other payloads. When installers create subdirectories and files they often do not set appropriate permissions to restrict write access, which allows for execution of untrusted code placed in the subdirectories or overwriting of binaries used in the installation process. This behavior is related to and may take advantage of [[T1574-hijack_execution_flow#^t1574001-dll|T1574.001: DLL]] search order hijacking.

Adversaries may use this technique to replace legitimate binaries with malicious ones as a means of executing code at a higher permissions level. Some installers may also require elevated privileges that will result in privilege escalation when executing adversary controlled code. This behavior is related to [[T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]. Several examples of this weakness in existing common installers have been reported to software vendors.(Citation: mozilla_sec_adv_2012)  (Citation: Executable Installers are Vulnerable) If the executing process is set to run at a specific time or during a certain event (e.g., system bootup) then this technique can also be used for persistence.

### T1574.006: Dynamic Linker Hijacking

^t1574006-dynamic-linker-hijacking

Adversaries may execute their own malicious payloads by hijacking environment variables the dynamic linker uses to load shared libraries. During the execution preparation phase of a program, the dynamic linker loads specified absolute paths of shared libraries from various environment variables and files, such as `LD_PRELOAD` on Linux or `DYLD_INSERT_LIBRARIES` on macOS.(Citation: TheEvilBit DYLD_INSERT_LIBRARIES)(Citation: Timac DYLD_INSERT_LIBRARIES)(Citation: Gabilondo DYLD_INSERT_LIBRARIES Catalina Bypass) Libraries specified in environment variables are loaded first, taking precedence over system libraries with the same function name.(Citation: Man LD.SO)(Citation: TLDP Shared Libraries)(Citation: Apple Doco Archive Dynamic Libraries) Each platform's linker uses an extensive list of environment variables at different points in execution. These variables are often used by developers to debug binaries without needing to recompile, deconflict mapped symbols, and implement custom functions in the original library.(Citation: Baeldung LD_PRELOAD)

Hijacking dynamic linker variables may grant access to the victim process's memory, system/network resources, and possibly elevated privileges. On Linux, adversaries may set `LD_PRELOAD` to point to malicious libraries that match the name of legitimate libraries which are requested by a victim program, causing the operating system to load the adversary's malicious code upon execution of the victim program. For example, adversaries have used `LD_PRELOAD` to inject a malicious library into every descendant process of the `sshd` daemon, resulting in execution under a legitimate process. When the executing sub-process calls the `execve` function, for example, the malicious library’s `execve` function is executed rather than the system function `execve` contained in the system library on disk. This allows adversaries to [[T1564-hide_artifacts|T1564: Hide Artifacts]] from detection, as hooking system functions such as `execve` and `readdir` enables malware to scrub its own artifacts from the results of commands such as `ls`, `ldd`, `iptables`, and `dmesg`.(Citation: ESET Ebury Oct 2017)(Citation: Intezer Symbiote 2022)(Citation: Elastic Security Labs Pumakit 2024)

Hijacking dynamic linker variables may grant access to the victim process's memory, system/network resources, and possibly elevated privileges.

### T1574.007: Path Interception by PATH Environment Variable

^t1574007-path-interception-by-path-environment-variable

Adversaries may execute their own malicious payloads by hijacking environment variables used to load libraries. The PATH environment variable contains a list of directories (User and System) that the OS searches sequentially through in search of the binary that was called from a script or the command line. 

Adversaries can place a malicious program in an earlier entry in the list of directories stored in the PATH environment variable, resulting in the operating system executing the malicious binary rather than the legitimate binary when it searches sequentially through that PATH listing.

For example, on Windows if an adversary places a malicious program named "net.exe" in `C:\example path`, which by default precedes `C:\Windows\system32\net.exe` in the PATH environment variable, when "net" is executed from the command-line the `C:\example path` will be called instead of the system's legitimate executable at `C:\Windows\system32\net.exe`. Some methods of executing a program rely on the PATH environment variable to determine the locations that are searched when the path for the program is not given, such as executing programs from a [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]].(Citation: ExpressVPN PATH env Windows 2021)

Adversaries may also directly modify the $PATH variable specifying the directories to be searched.  An adversary can modify the `$PATH` variable to point to a directory they have write access. When a program using the $PATH variable is called, the OS searches the specified directory and executes the malicious binary. On macOS, this can also be performed through modifying the $HOME variable. These variables can be modified using the command-line, launchctl, [[T1546-event_triggered_execution#^t1546004-unix-shell-configuration-modification|T1546.004: Unix Shell Configuration Modification]], or modifying the `/etc/paths.d` folder contents.(Citation: uptycs Fake POC linux malware 2023)(Citation: nixCraft macOS PATH variables)(Citation: Elastic Rules macOS launchctl 2022)

### T1574.008: Path Interception by Search Order Hijacking

^t1574008-path-interception-by-search-order-hijacking

Adversaries may execute their own malicious payloads by hijacking the search order used to load other programs. Because some programs do not call other programs using the full path, adversaries may place their own file in the directory where the calling program is located, causing the operating system to launch their malicious software at the request of the calling program.

Search order hijacking occurs when an adversary abuses the order in which Windows searches for programs that are not given a path. Unlike [[T1574-hijack_execution_flow#^t1574001-dll|T1574.001: DLL]] search order hijacking, the search order differs depending on the method that is used to execute the program. (Citation: Microsoft CreateProcess) (Citation: Windows NT Command Shell) (Citation: Microsoft WinExec) However, it is common for Windows to search in the directory of the initiating program before searching through the Windows system directory. An adversary who finds a program vulnerable to search order hijacking (i.e., a program that does not specify the path to an executable) may take advantage of this vulnerability by creating a program named after the improperly specified program and placing it within the initiating program's directory.

For example, "example.exe" runs "cmd.exe" with the command-line argument `net user`. An adversary may place a program called "net.exe" within the same directory as example.exe, "net.exe" will be run instead of the Windows system utility net. In addition, if an adversary places a program called "net.com" in the same directory as "net.exe", then `cmd.exe /C net user` will execute "net.com" instead of "net.exe" due to the order of executable extensions defined under PATHEXT. (Citation: Microsoft Environment Property)

Search order hijacking is also a common practice for hijacking DLL loads and is covered in [[T1574-hijack_execution_flow#^t1574001-dll|T1574.001: DLL]].

### T1574.009: Path Interception by Unquoted Path

^t1574009-path-interception-by-unquoted-path

Adversaries may execute their own malicious payloads by hijacking vulnerable file path references. Adversaries can take advantage of paths that lack surrounding quotations by placing an executable in a higher level directory within the path, so that Windows will choose the adversary's executable to launch.

Service paths (Citation: Microsoft CurrentControlSet Services) and shortcut paths may also be vulnerable to path interception if the path has one or more spaces and is not surrounded by quotation marks (e.g., `C:\unsafe path with space\program.exe` vs. `"C:\safe path with space\program.exe"`). (Citation: Help eliminate unquoted path) (stored in Windows Registry keys) An adversary can place an executable in a higher level directory of the path, and Windows will resolve that executable instead of the intended executable. For example, if the path in a shortcut is `C:\program files\myapp.exe`, an adversary may create a program at `C:\program.exe` that will be run instead of the intended program. (Citation: Windows Unquoted Services) (Citation: Windows Privilege Escalation Guide)

This technique can be used for persistence if executables are called on a regular basis, as well as privilege escalation if intercepted executables are started by a higher privileged process.

### T1574.010: Services File Permissions Weakness

^t1574010-services-file-permissions-weakness

Adversaries may execute their own malicious payloads by hijacking the binaries used by services. Adversaries may use flaws in the permissions of Windows services to replace the binary that is executed upon service start. These service processes may automatically execute specific binaries as part of their functionality or to perform other actions. If the permissions on the file system directory containing a target binary, or permissions on the binary itself are improperly set, then the target binary may be overwritten with another binary using user-level permissions and executed by the original process. If the original process and thread are running under a higher permissions level, then the replaced binary will also execute under higher-level permissions, which could include SYSTEM.

Adversaries may use this technique to replace legitimate binaries with malicious ones as a means of executing code at a higher permissions level. If the executing process is set to run at a specific time or during a certain event (e.g., system bootup) then this technique can also be used for persistence.

### T1574.011: Services Registry Permissions Weakness

^t1574011-services-registry-permissions-weakness

Adversaries may execute their own malicious payloads by hijacking the Registry entries used by services. Flaws in the permissions for Registry keys related to services can allow adversaries to redirect the originally specified executable to one they control, launching their own code when a service starts. Windows stores local service configuration information in the Registry under `HKLM\SYSTEM\CurrentControlSet\Services`. The information stored under a service's Registry keys can be manipulated to modify a service's execution parameters through tools such as the service controller, sc.exe,  [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]], or [[reg|Reg (S0075)]]. Access to Registry keys is controlled through access control lists and user permissions. (Citation: Registry Key Security)(Citation: malware_hides_service)

If the permissions for users and groups are not properly set and allow access to the Registry keys for a service, adversaries may change the service's binPath/ImagePath to point to a different executable under their control. When the service starts or is restarted, the adversary-controlled program will execute, allowing the adversary to establish persistence and/or privilege escalation to the account context the service is set to execute under (local/domain account, SYSTEM, LocalService, or NetworkService).

Adversaries may also alter other Registry keys in the service’s Registry tree. For example, the `FailureCommand` key may be changed so that the service is executed in an elevated context anytime the service fails or is intentionally corrupted.(Citation: Kansa Service related collectors)(Citation: Tweet Registry Perms Weakness)

The `Performance` key contains the name of a driver service's performance DLL and the names of several exported functions in the DLL.(Citation: microsoft_services_registry_tree) If the `Performance` key is not already present and if an adversary-controlled user has the `Create Subkey` permission, adversaries may create the `Performance` key in the service’s Registry tree to point to a malicious DLL.(Citation: insecure_reg_perms)

Adversaries may also add the `Parameters` key, which can reference malicious drivers file paths. This technique has been identified to be a method of abuse by configuring DLL file paths within the `Parameters` key of a given services registry configuration. By placing and configuring the `Parameters` key to reference a malicious DLL, adversaries can ensure that their code is loaded persistently whenever the associated service or library is invoked.

For example, the registry path(Citation: MDSec) `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WinSock2\Parameters`(Citation: hexacorn)(Citation: gendigital) contains the `AutodiaDLL` value, which specifies the DLL to be loaded for autodial funcitionality. An adversary could set the `AutodiaDLL` to point to a hijacked or malicious DLL:

`"AutodialDLL"="c:\temp\foo.dll"`

This ensures persistence, as it causes the DLL (in this case, foo.dll) to be loaded each time the Winsock 2 library is invoked.

### T1574.012: COR_PROFILER

^t1574012-cor-profiler

Adversaries may leverage the COR_PROFILER environment variable to hijack the execution flow of programs that load the .NET CLR. The COR_PROFILER is a .NET Framework feature which allows developers to specify an unmanaged (or external of .NET) profiling DLL to be loaded into each .NET process that loads the Common Language Runtime (CLR). These profilers are designed to monitor, troubleshoot, and debug managed code executed by the .NET CLR.(Citation: Microsoft Profiling Mar 2017)(Citation: Microsoft COR_PROFILER Feb 2013)

The COR_PROFILER environment variable can be set at various scopes (system, user, or process) resulting in different levels of influence. System and user-wide environment variable scopes are specified in the Registry, where a [[T1559-inter-process_communication#^t1559001-component-object-model|T1559.001: Component Object Model]] (COM) object can be registered as a profiler DLL. A process scope COR_PROFILER can also be created in-memory without modifying the Registry. Starting with .NET Framework 4, the profiling DLL does not need to be registered as long as the location of the DLL is specified in the COR_PROFILER_PATH environment variable.(Citation: Microsoft COR_PROFILER Feb 2013)

Adversaries may abuse COR_PROFILER to establish persistence that executes a malicious DLL in the context of all .NET processes every time the CLR is invoked. The COR_PROFILER can also be used to elevate privileges (ex: [[T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]) if the victim .NET process executes at a higher permission level, as well as to hook and [[T1562-impair_defenses|T1562: Impair Defenses]] provided by .NET processes.(Citation: RedCanary Mockingbird May 2020)(Citation: Red Canary COR_PROFILER May 2020)(Citation: Almond COR_PROFILER Apr 2019)(Citation: GitHub OmerYa Invisi-Shell)(Citation: subTee .NET Profilers May 2017)

### T1574.013: KernelCallbackTable

^t1574013-kernelcallbacktable

Adversaries may abuse the `KernelCallbackTable` of a process to hijack its execution flow in order to run their own payloads.(Citation: Lazarus APT January 2022)(Citation: FinFisher exposed ) The `KernelCallbackTable` can be found in the Process Environment Block (PEB) and is initialized to an array of graphic functions available to a GUI process once `user32.dll` is loaded.(Citation: Windows Process Injection KernelCallbackTable)

An adversary may hijack the execution flow of a process using the `KernelCallbackTable` by replacing an original callback function with a malicious payload. Modifying callback functions can be achieved in various ways involving related behaviors such as [[T1620-reflective_code_loading|T1620: Reflective Code Loading]] or [[T1055-process_injection|T1055: Process Injection]] into another process.

A pointer to the memory address of the `KernelCallbackTable` can be obtained by locating the PEB (ex: via a call to the `NtQueryInformationProcess()` [[T1106-native_api|T1106: Native API]] function).(Citation: NtQueryInformationProcess) Once the pointer is located, the `KernelCallbackTable` can be duplicated, and a function in the table (e.g., `fnCOPYDATA`) set to the address of a malicious payload (ex: via `WriteProcessMemory()`). The PEB is then updated with the new address of the table. Once the tampered function is invoked, the malicious payload will be triggered.(Citation: Lazarus APT January 2022)

The tampered function is typically invoked using a Windows message. After the process is hijacked and malicious code is executed, the `KernelCallbackTable` may also be restored to its original state by the rest of the malicious payload.(Citation: Lazarus APT January 2022) Use of the `KernelCallbackTable` to hijack execution flow may evade detection from security products since the execution can be masked under a legitimate process.

### T1574.014: AppDomainManager

^t1574014-appdomainmanager

Adversaries may execute their own malicious payloads by hijacking how the .NET `AppDomainManager` loads assemblies. The .NET framework uses the `AppDomainManager` class to create and manage one or more isolated runtime environments (called application domains) inside a process to host the execution of .NET applications. Assemblies (`.exe` or `.dll` binaries compiled to run as .NET code) may be loaded into an application domain as executable code.(Citation: Microsoft App Domains) 

Known as "AppDomainManager injection," adversaries may execute arbitrary code by hijacking how .NET applications load assemblies. For example, malware may create a custom application domain inside a target process to load and execute an arbitrary assembly. Alternatively, configuration files (`.config`) or process environment variables that define .NET runtime settings may be tampered with to instruct otherwise benign .NET applications to load a malicious assembly (identified by name) into the target process.(Citation: PenTestLabs AppDomainManagerInject)(Citation: PwC Yellow Liderc)(Citation: Rapid7 AppDomain Manager Injection)

## Mitigations

- [[M1013-application_developer_guidance|M1013: Application Developer Guidance]]
- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1022-restrict_file_and_directory_permissions|M1022: Restrict File and Directory Permissions]]
- [[M1024-restrict_registry_permissions|M1024: Restrict Registry Permissions]]
- [[M1038-execution_prevention|M1038: Execution Prevention]]
- [[M1040-behavior_prevention_on_endpoint|M1040: Behavior Prevention on Endpoint]]
- [[M1044-restrict_library_loading|M1044: Restrict Library Loading]]
- [[M1047-audit|M1047: Audit]]
- [[M1051-update_software|M1051: Update Software]]
- [[M1052-user_account_control|M1052: User Account Control]]

## Platforms

- Linux
- macOS
- Windows

