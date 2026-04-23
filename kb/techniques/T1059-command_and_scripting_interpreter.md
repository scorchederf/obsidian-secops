---
mitre_id: "T1059"
mitre_name: "Command and Scripting Interpreter"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--7385dfaf-6886-4229-9ecd-6fd678040830"
mitre_created: "2017-05-31T21:30:49.546Z"
mitre_modified: "2025-10-24T17:48:57.520Z"
mitre_version: "2.6"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1059/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "ESXi"
  - "IaaS"
  - "Identity Provider"
  - "Linux"
  - "macOS"
  - "Network Devices"
  - "Office Suite"
  - "Windows"
mitre_tactic_ids:
  - "TA0002"
---

# T1059: Command and Scripting Interpreter

Adversaries may abuse command and script interpreters to execute commands, scripts, or binaries. These interfaces and languages provide ways of interacting with computer systems and are a common feature across many different platforms. Most systems come with some built-in command-line interface and scripting capabilities, for example, macOS and Linux distributions include some flavor of [[T1059-command_and_scripting_interpreter#^t1059004-unix-shell|T1059.004: Unix Shell]] while Windows installations include the [[T1059-command_and_scripting_interpreter#^t1059003-windows-command-shell|T1059.003: Windows Command Shell]] and [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]].

There are also cross-platform interpreters such as [[T1059-command_and_scripting_interpreter#^t1059006-python|T1059.006: Python]], as well as those commonly associated with client applications such as [[T1059-command_and_scripting_interpreter#^t1059007-javascript|T1059.007: JavaScript]] and [[T1059-command_and_scripting_interpreter#^t1059005-visual-basic|T1059.005: Visual Basic]].

Adversaries may abuse these technologies in various ways as a means of executing arbitrary commands. Commands and scripts can be embedded in [[TA0001-initial_access|TA0001: Initial Access]] payloads delivered to victims as lure documents or as secondary payloads downloaded from an existing C2. Adversaries may also execute commands through interactive terminals/shells, as well as utilize various [[T1021-remote_services|T1021: Remote Services]] in order to achieve remote Execution.(Citation: Powershell Remote Commands)(Citation: Cisco IOS Software Integrity Assurance - Command History)(Citation: Remote Shell Execution in Python)

## Tactics

- [[TA0002-execution|TA0002: Execution]]

## Subtechniques

### T1059.001: PowerShell

^t1059001-powershell

Adversaries may abuse PowerShell commands and scripts for execution. PowerShell is a powerful interactive command-line interface and scripting environment included in the Windows operating system.(Citation: TechNet PowerShell) Adversaries can use PowerShell to perform a number of actions, including discovery of information and execution of code. Examples include the `Start-Process` cmdlet which can be used to run an executable and the `Invoke-Command` cmdlet which runs a command locally or on a remote computer (though administrator permissions are required to use PowerShell to connect to remote systems).

PowerShell may also be used to download and run executables from the Internet, which can be executed from disk or in memory without touching disk.

A number of PowerShell-based offensive testing tools are available, including [[empire|Empire]],  [[powersploit|PowerSploit]], [[poshc2|PoshC2]], and PSAttack.(Citation: Github PSAttack)

PowerShell commands/scripts can also be executed without directly invoking the `powershell.exe` binary through interfaces to PowerShell's underlying `System.Management.Automation` assembly DLL exposed through the .NET framework and Windows Common Language Interface (CLI).(Citation: Sixdub PowerPick Jan 2016)(Citation: SilentBreak Offensive PS Dec 2015)(Citation: Microsoft PSfromCsharp APR 2014)

### T1059.002: AppleScript

^t1059002-applescript

Adversaries may abuse AppleScript for execution. AppleScript is a macOS scripting language designed to control applications and parts of the OS via inter-application messages called AppleEvents.(Citation: Apple AppleScript) These AppleEvent messages can be sent independently or easily scripted with AppleScript. These events can locate open windows, send keystrokes, and interact with almost any open application locally or remotely.

Scripts can be run from the command-line via `osascript /path/to/script` or `osascript -e "script here"`. Aside from the command line, scripts can be executed in numerous ways including Mail rules, Calendar.app alarms, and Automator workflows. AppleScripts can also be executed as plain text shell scripts by adding `#!/usr/bin/osascript` to the start of the script file.(Citation: SentinelOne AppleScript)

AppleScripts do not need to call `osascript` to execute. However, they may be executed from within mach-O binaries by using the macOS [[T1106-native_api|T1106: Native API]]s `NSAppleScript` or `OSAScript`, both of which execute code independent of the `/usr/bin/osascript` command line utility.

Adversaries may abuse AppleScript to execute various behaviors, such as interacting with an open SSH connection, moving to remote machines, and even presenting users with fake dialog boxes. These events cannot start applications remotely (they can start them locally), but they can interact with applications if they're already running remotely. On macOS 10.10 Yosemite and higher, AppleScript has the ability to execute [[T1106-native_api|T1106: Native API]]s, which otherwise would require compilation and execution in a mach-O binary file format.(Citation: SentinelOne macOS Red Team) Since this is a scripting language, it can be used to launch more common techniques as well such as a reverse shell via [[T1059-command_and_scripting_interpreter#^t1059006-python|T1059.006: Python]].(Citation: Macro Malware Targets Macs)

### T1059.003: Windows Command Shell

^t1059003-windows-command-shell

Adversaries may abuse the Windows command shell for execution. The Windows command shell ([[cmd|cmd]]) is the primary command prompt on Windows systems. The Windows command prompt can be used to control almost any aspect of a system, with various permission levels required for different subsets of commands. The command prompt can be invoked remotely via [[T1021-remote_services|T1021: Remote Services]] such as [[T1021-remote_services#^t1021004-ssh|T1021.004: SSH]].(Citation: SSH in Windows)

Batch files (ex: .bat or .cmd) also provide the shell with a list of sequential commands to run, as well as normal scripting operations such as conditionals and loops. Common uses of batch files include long or repetitive tasks, or the need to run the same set of commands on multiple systems.

Adversaries may leverage [[cmd|cmd]] to execute various commands and payloads. Common uses include [[cmd|cmd]] to execute a single command, or abusing [[cmd|cmd]] interactively with input and output forwarded over a command and control channel.

### T1059.004: Unix Shell

^t1059004-unix-shell

Adversaries may abuse Unix shell commands and scripts for execution. Unix shells are the primary command prompt on Linux, macOS, and ESXi systems, though many variations of the Unix shell exist (e.g. sh, ash, bash, zsh, etc.) depending on the specific OS or distribution.(Citation: DieNet Bash)(Citation: Apple ZShell) Unix shells can control every aspect of a system, with certain commands requiring elevated privileges.

Unix shells also support scripts that enable sequential execution of commands as well as other typical programming operations such as conditionals and loops. Common uses of shell scripts include long or repetitive tasks, or the need to run the same set of commands on multiple systems.

Adversaries may abuse Unix shells to execute various commands or payloads. Interactive shells may be accessed through command and control channels or during lateral movement such as with [[T1021-remote_services#^t1021004-ssh|T1021.004: SSH]]. Adversaries may also leverage shell scripts to deliver and execute multiple commands on victims or as part of payloads used for persistence.

Some systems, such as embedded devices, lightweight Linux distributions, and ESXi servers, may leverage stripped-down Unix shells via Busybox, a small executable that contains a variety of tools, including a simple shell.

### T1059.005: Visual Basic

^t1059005-visual-basic

Adversaries may abuse Visual Basic (VB) for execution. VB is a programming language created by Microsoft with interoperability with many Windows technologies such as [[T1559-inter-process_communication#^t1559001-component-object-model|T1559.001: Component Object Model]] and the [[T1106-native_api|T1106: Native API]] through the Windows API. Although tagged as legacy with no planned future evolutions, VB is integrated and supported in the .NET Framework and cross-platform .NET Core.(Citation: VB .NET Mar 2020)(Citation: VB Microsoft)

Derivative languages based on VB have also been created, such as Visual Basic for Applications (VBA) and VBScript. VBA is an event-driven programming language built into Microsoft Office, as well as several third-party applications.(Citation: Microsoft VBA)(Citation: Wikipedia VBA) VBA enables documents to contain macros used to automate the execution of tasks and other functionality on the host. VBScript is a default scripting language on Windows hosts and can also be used in place of [[T1059-command_and_scripting_interpreter#^t1059007-javascript|T1059.007: JavaScript]] on HTML Application (HTA) webpages served to Internet Explorer (though most modern browsers do not come with VBScript support).(Citation: Microsoft VBScript)

Adversaries may use VB payloads to execute malicious commands. Common malicious usage includes automating execution of behaviors with VBScript or embedding VBA content into [[T1566-phishing#^t1566001-spearphishing-attachment|T1566.001: Spearphishing Attachment]] payloads (which may also involve [[T1553-subvert_trust_controls#^t1553005-mark-of-the-web-bypass|T1553.005: Mark-of-the-Web Bypass]] to enable execution).(Citation: Default VBS macros Blocking )

### T1059.006: Python

^t1059006-python

Adversaries may abuse Python commands and scripts for execution. Python is a very popular scripting/programming language, with capabilities to perform many functions. Python can be executed interactively from the command-line (via the `python.exe` interpreter) or via scripts (.py) that can be written and distributed to different systems. Python code can also be compiled into binary executables.(Citation: Zscaler APT31 Covid-19 October 2020)

Python comes with many built-in packages to interact with the underlying system, such as file operations and device I/O. Adversaries can use these libraries to download and execute commands or other scripts as well as perform various malicious behaviors.

### T1059.007: JavaScript

^t1059007-javascript

Adversaries may abuse various implementations of JavaScript for execution. JavaScript (JS) is a platform-independent scripting language (compiled just-in-time at runtime) commonly associated with scripts in webpages, though JS can be executed in runtime environments outside the browser.(Citation: NodeJS)

JScript is the Microsoft implementation of the same scripting standard. JScript is interpreted via the Windows Script engine and thus integrated with many components of Windows such as the [[T1559-inter-process_communication#^t1559001-component-object-model|T1559.001: Component Object Model]] and Internet Explorer HTML Application (HTA) pages.(Citation: JScrip May 2018)(Citation: Microsoft JScript 2007)(Citation: Microsoft Windows Scripts)

JavaScript for Automation (JXA) is a macOS scripting language based on JavaScript, included as part of Apple’s Open Scripting Architecture (OSA), that was introduced in OSX 10.10. Apple’s OSA provides scripting capabilities to control applications, interface with the operating system, and bridge access into the rest of Apple’s internal APIs. As of OSX 10.10, OSA only supports two languages, JXA and [[T1059-command_and_scripting_interpreter#^t1059002-applescript|T1059.002: AppleScript]]. Scripts can be executed via the command line utility `osascript`, they can be compiled into applications or script files via `osacompile`, and they can be compiled and executed in memory of other programs by leveraging the OSAKit Framework.(Citation: Apple About Mac Scripting 2016)(Citation: SpecterOps JXA 2020)(Citation: SentinelOne macOS Red Team)(Citation: Red Canary Silver Sparrow Feb2021)(Citation: MDSec macOS JXA and VSCode)

Adversaries may abuse various implementations of JavaScript to execute various behaviors. Common uses include hosting malicious scripts on websites as part of a [[T1189-drive-by_compromise|T1189: Drive-by Compromise]] or downloading and executing these script files as secondary payloads. Since these payloads are text-based, it is also very common for adversaries to obfuscate their content as part of [[T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]].

### T1059.008: Network Device CLI

^t1059008-network-device-cli

Adversaries may abuse scripting or built-in command line interpreters (CLI) on network devices to execute malicious command and payloads. The CLI is the primary means through which users and administrators interact with the device in order to view system information, modify device operations, or perform diagnostic and administrative functions. CLIs typically contain various permission levels required for different commands. 

Scripting interpreters automate tasks and extend functionality beyond the command set included in the network OS. The CLI and scripting interpreter are accessible through a direct console connection, or through remote means, such as telnet or [[T1021-remote_services#^t1021004-ssh|T1021.004: SSH]].

Adversaries can use the network CLI to change how network devices behave and operate. The CLI may be used to manipulate traffic flows to intercept or manipulate data, modify startup configuration parameters to load malicious system software, or to disable security features or logging to avoid detection.(Citation: Cisco Synful Knock Evolution)

### T1059.009: Cloud API

^t1059009-cloud-api

Adversaries may abuse cloud APIs to execute malicious commands. APIs available in cloud environments provide various functionalities and are a feature-rich method for programmatic access to nearly all aspects of a tenant. These APIs may be utilized through various methods such as command line interpreters (CLIs), in-browser Cloud Shells, [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]] modules like Azure for PowerShell(Citation: Microsoft - Azure PowerShell), or software developer kits (SDKs) available for languages such as [[T1059-command_and_scripting_interpreter#^t1059006-python|T1059.006: Python]].  

Cloud API functionality may allow for administrative access across all major services in a tenant such as compute, storage, identity and access management (IAM), networking, and security policies.

With proper permissions (often via use of credentials such as [[T1550-use_alternate_authentication_material#^t1550001-application-access-token|T1550.001: Application Access Token]] and [[T1550-use_alternate_authentication_material#^t1550004-web-session-cookie|T1550.004: Web Session Cookie]]), adversaries may abuse cloud APIs to invoke various functions that execute malicious actions. For example, CLI and PowerShell functionality may be accessed through binaries installed on cloud-hosted or on-premises hosts or accessed through a browser-based cloud shell offered by many cloud platforms (such as AWS, Azure, and GCP). These cloud shells are often a packaged unified environment to use CLI and/or scripting modules hosted as a container in the cloud environment.  

### T1059.010: AutoHotKey & AutoIT

^t1059010-autohotkey-&-autoit

Adversaries may execute commands and perform malicious tasks using AutoIT and AutoHotKey automation scripts. AutoIT and AutoHotkey (AHK) are scripting languages that enable users to automate Windows tasks. These automation scripts can be used to perform a wide variety of actions, such as clicking on buttons, entering text, and opening and closing programs.(Citation: AutoIT)(Citation: AutoHotKey)

Adversaries may use AHK (`.ahk`) and AutoIT (`.au3`) scripts to execute malicious code on a victim's system. For example, adversaries have used for AHK to execute payloads and other modular malware such as keyloggers. Adversaries have also used custom AHK files containing embedded malware as [[T1566-phishing|T1566: Phishing]] payloads.(Citation: Splunk DarkGate)

These scripts may also be compiled into self-contained executable payloads (`.exe`).(Citation: AutoIT)(Citation: AutoHotKey)

### T1059.011: Lua

^t1059011-lua

Adversaries may abuse Lua commands and scripts for execution. Lua is a cross-platform scripting and programming language primarily designed for embedded use in applications. Lua can be executed on the command-line (through the stand-alone lua interpreter), via scripts (`.lua`), or from Lua-embedded programs (through the `struct lua_State`).(Citation: Lua main page)(Citation: Lua state)

Lua scripts may be executed by adversaries for malicious purposes. Adversaries may incorporate, abuse, or replace existing Lua interpreters to allow for malicious Lua command execution at runtime.(Citation: PoetRat Lua)(Citation: Lua Proofpoint Sunseed)(Citation: Cyphort EvilBunny)(Citation: Kaspersky Lua)

### T1059.012: Hypervisor CLI

^t1059012-hypervisor-cli

Adversaries may abuse hypervisor command line interpreters (CLIs) to execute malicious commands. Hypervisor CLIs typically enable a wide variety of functionality for managing both the hypervisor itself and the guest virtual machines it hosts. 

For example, on ESXi systems, tools such as `esxcli` and `vim-cmd` allow administrators to configure firewall rules and log forwarding on the hypervisor, list virtual machines, start and stop virtual machines, and more.(Citation: Broadcom ESXCLI Reference)(Citation: Crowdstrike Hypervisor Jackpotting Pt 2 2021)(Citation: LOLESXi) Adversaries may be able to leverage these tools in order to support further actions, such as [[T1083-file_and_directory_discovery|T1083: File and Directory Discovery]] or [[T1486-data_encrypted_for_impact|T1486: Data Encrypted for Impact]].

### T1059.013: Container CLI/API

^t1059013-container-cli-api

Adversaries may abuse built-in CLI tools or API calls to execute malicious commands in containerized environments.

The Docker CLI is used for managing containers via an exposed API point from the `dockerd` daemon. Some common examples of Docker CLI include Docker Desktop CLI and Docker Compose, but users are also able to use SDKs to interact with the API. For example, Docker SDK for Python can be used to run commands within a Python application.(Citation: Docker Desktop CLI)

Adversaries may leverage the Docker CLI, API, or SDK to pull or build Docker images (i.e., [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]], [[T1612-build_image_on_host|T1612: Build Image on Host]]), run containers (i.e., [[T1610-deploy_container|T1610: Deploy Container]]), or execute commands inside running containers (i.e., [[T1609-container_administration_command|T1609: Container Administration Command]]). In some cases, threat actors may pull legitimate images that include scripts or tools that they can leverage - for example, using an image that includes the `curl` command to download payloads.(Citation: Intezer) Adversaries may also utilize `docker inspect` and `docker ps` to scan for cloud environment variables and other running containers (i.e., [[T1613-container_and_resource_discovery|T1613: Container and Resource Discovery]]).(Citation: Cisco Talos Blog)(Citation: aquasec)

Kubernetes is responsible for the management and orchestration of containers across clusters. The Kubernetes control plane, which manages the state of the cluster and is responsible for scheduling, communication, and resource monitoring, can be invoked directly via the API or indirectly via CLI tools such as `kubectl`. It may also be accessed within client libraries such as Go or Python. By utilizing the API, administrators can interact with resources within the cluster such as listing or creating pods, which is a group of one or more containers. Adversaries call the API server via `curl` or other tools, allowing them to obtain further information about the environment such as pods, deployments, daemonsets, namespaces, or sysvars.(Citation: aquasec) They may also run various commands regarding resource management.

## Mitigations

- [[M1021-restrict_web-based_content|M1021: Restrict Web-Based Content]]
- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1033-limit_software_installation|M1033: Limit Software Installation]]
- [[M1038-execution_prevention|M1038: Execution Prevention]]
- [[M1040-behavior_prevention_on_endpoint|M1040: Behavior Prevention on Endpoint]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]
- [[M1045-code_signing|M1045: Code Signing]]
- [[M1047-audit|M1047: Audit]]
- [[M1049-antivirus_antimalware|M1049: Antivirus/Antimalware]]

## Tools

- [[empire|Empire]]
- [[imminent_monitor|Imminent Monitor]]
- [[donut|Donut]]

## Platforms

- ESXi
- IaaS
- Identity Provider
- Linux
- macOS
- Network Devices
- Office Suite
- Windows

