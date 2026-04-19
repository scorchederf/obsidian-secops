---
id: T1056
name: Input Capture
created: 2017-05-31 21:30:48.323000+00:00
modified: 2025-10-24 17:49:17.884000+00:00
type: attack-pattern
x_mitre_version: 1.4
x_mitre_domains: enterprise-attack
---

## Tactic

- [[collection|Collection]]

Adversaries may use methods of capturing user input to obtain credentials or collect information. During normal system usage, users often provide credentials to various different locations, such as login pages/portals or system dialog boxes. Input capture mechanisms may be transparent to the user (e.g. [Credential API Hooking](https://attack.mitre.org/techniques/T1056/004)) or rely on deceiving the user into providing input into what they believe to be a genuine service (e.g. [Web Portal Capture](https://attack.mitre.org/techniques/T1056/003)).

## Subtechniques

### T1056.001: Keylogging
^t1056001-keylogging

**Parent Technique**
- [[T1056-input_capture|T1056: Input Capture]]

**Tactic**
- [[collection|Collection]]

Adversaries may log user keystrokes to intercept credentials as the user types them. Keylogging is likely to be used to acquire credentials for new access opportunities when [OS Credential Dumping](https://attack.mitre.org/techniques/T1003) efforts are not effective, and may require an adversary to intercept keystrokes on a system for a substantial period of time before credentials can be successfully captured. In order to increase the likelihood of capturing credentials quickly, an adversary may also perform actions such as clearing browser cookies to force users to reauthenticate to systems.(Citation: Talos Kimsuky Nov 2021)

Keylogging is the most prevalent type of input capture, with many different ways of intercepting keystrokes.(Citation: Adventures of a Keystroke) Some methods include:

* Hooking API callbacks used for processing keystrokes. Unlike [Credential API Hooking](https://attack.mitre.org/techniques/T1056/004), this focuses solely on API functions intended for processing keystroke data.
* Reading raw keystroke data from the hardware buffer.
* Windows Registry modifications.
* Custom drivers.
* [Modify System Image](https://attack.mitre.org/techniques/T1601) may provide adversaries with hooks into the operating system of network devices to read raw keystrokes for login sessions.(Citation: Cisco Blog Legacy Device Attacks) 

#### Properties

- id: T1056.001
- name: Keylogging
- created: 2020-02-11 18:58:11.791000+00:00
- modified: 2025-10-24 17:48:21.756000+00:00
- type: attack-pattern
- x_mitre_version: 1.3
- x_mitre_domains: enterprise-attack

### T1056.002: GUI Input Capture
^t1056002-gui-input-capture

**Parent Technique**
- [[T1056-input_capture|T1056: Input Capture]]

**Tactic**
- [[collection|Collection]]

Adversaries may mimic common operating system GUI components to prompt users for credentials with a seemingly legitimate prompt. When programs are executed that need additional privileges than are present in the current user context, it is common for the operating system to prompt the user for proper credentials to authorize the elevated privileges for the task (ex: [Bypass User Account Control](https://attack.mitre.org/techniques/T1548/002)).

Adversaries may mimic this functionality to prompt users for credentials with a seemingly legitimate prompt for a number of reasons that mimic normal usage, such as a fake installer requiring additional access or a fake malware removal suite.(Citation: OSX Malware Exploits MacKeeper) This type of prompt can be used to collect credentials via various languages such as [AppleScript](https://attack.mitre.org/techniques/T1059/002)(Citation: LogRhythm Do You Trust Oct 2014)(Citation: OSX Keydnap malware)(Citation: Spoofing credential dialogs) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).(Citation: LogRhythm Do You Trust Oct 2014)(Citation: Enigma Phishing for Credentials Jan 2015)(Citation: Spoofing credential dialogs) On Linux systems adversaries may launch dialog boxes prompting users for credentials from malicious shell scripts or the command line (i.e. [Unix Shell](https://attack.mitre.org/techniques/T1059/004)).(Citation: Spoofing credential dialogs)

Adversaries may also mimic common software authentication requests, such as those from browsers or email clients. This may also be paired with user activity monitoring (i.e., [Browser Information Discovery](https://attack.mitre.org/techniques/T1217) and/or [Application Window Discovery](https://attack.mitre.org/techniques/T1010)) to spoof prompts when users are naturally accessing sensitive sites/data.

#### Properties

- id: T1056.002
- name: GUI Input Capture
- created: 2020-02-11 18:58:45.908000+00:00
- modified: 2025-10-24 17:49:10.643000+00:00
- type: attack-pattern
- x_mitre_version: 1.3
- x_mitre_domains: enterprise-attack

### T1056.003: Web Portal Capture
^t1056003-web-portal-capture

**Parent Technique**
- [[T1056-input_capture|T1056: Input Capture]]

**Tactic**
- [[collection|Collection]]

Adversaries may install code on externally facing portals, such as a VPN login page, to capture and transmit credentials of users who attempt to log into the service. For example, a compromised login page may log provided user credentials before logging the user in to the service.

This variation on input capture may be conducted post-compromise using legitimate administrative access as a backup measure to maintain network access through [External Remote Services](https://attack.mitre.org/techniques/T1133) and [Valid Accounts](https://attack.mitre.org/techniques/T1078) or as part of the initial compromise by exploitation of the externally facing web service.(Citation: Volexity Virtual Private Keylogging)

#### Properties

- id: T1056.003
- name: Web Portal Capture
- created: 2020-02-11 18:59:50.058000+00:00
- modified: 2025-10-24 17:48:54.254000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

### T1056.004: Credential API Hooking
^t1056004-credential-api-hooking

**Parent Technique**
- [[T1056-input_capture|T1056: Input Capture]]

**Tactic**
- [[collection|Collection]]

Adversaries may hook into Windows application programming interface (API) functions and Linux system functions to collect user credentials. Malicious hooking mechanisms may capture API or function calls that include parameters that reveal user authentication credentials.(Citation: Microsoft TrojanSpy:Win32/Ursnif.gen!I Sept 2017) Unlike [Keylogging](https://attack.mitre.org/techniques/T1056/001), this technique focuses specifically on API functions that include parameters that reveal user credentials. 

In Windows, hooking involves redirecting calls to these functions and can be implemented via:

* **Hooks procedures**, which intercept and execute designated code in response to events such as messages, keystrokes, and mouse inputs.(Citation: Microsoft Hook Overview)(Citation: Elastic Process Injection July 2017)
* **Import address table (IAT) hooking**, which use modifications to a process’s IAT, where pointers to imported API functions are stored.(Citation: Elastic Process Injection July 2017)(Citation: Adlice Software IAT Hooks Oct 2014)(Citation: MWRInfoSecurity Dynamic Hooking 2015)
* **Inline hooking**, which overwrites the first bytes in an API function to redirect code flow.(Citation: Elastic Process Injection July 2017)(Citation: HighTech Bridge Inline Hooking Sept 2011)(Citation: MWRInfoSecurity Dynamic Hooking 2015)

In Linux and macOS, adversaries may hook into system functions via the `LD_PRELOAD` (Linux) or `DYLD_INSERT_LIBRARIES` (macOS) environment variables, which enables loading shared libraries into a program’s address space. For example, an adversary may capture credentials by hooking into the `libc read` function leveraged by SSH or SCP.(Citation: Intezer Symbiote 2022)

#### Properties

- id: T1056.004
- name: Credential API Hooking
- created: 2020-02-11 19:01:15.930000+00:00
- modified: 2025-10-24 17:49:37.119000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

## Platforms

- Linux
- macOS
- Network Devices
- Windows

## Tools

- [[nppspy|NPPSPY]]

