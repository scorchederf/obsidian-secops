---
mitre_id: "T1056"
mitre_name: "Input Capture"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--bb5a00de-e086-4859-a231-fa793f6797e2"
mitre_created: "2017-05-31T21:30:48.323Z"
mitre_modified: "2025-10-24T17:49:17.884Z"
mitre_version: "1.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1056/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Network Devices"
  - "Windows"
mitre_tactic_ids:
  - "TA0009"
  - "TA0006"
d3fend_ids:
  - "D3-AVE"
  - "D3-HCI"
  - "D3-IDA"
  - "D3-IOPR"
  - "D3-MBT"
  - "D3-PCSV"
  - "D3-PSEP"
  - "D3-RH"
  - "D3-RS"
  - "D3-SAOR"
  - "D3-SBV"
  - "D3-SU"
  - "D3-SWI"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may use methods of capturing user input to obtain credentials or collect information. During normal system usage, users often provide credentials to various different locations, such as login pages/portals or system dialog boxes. Input capture mechanisms may be transparent to the user (e.g. [[T1056-input_capture#^t1056004-credential-api-hooking|T1056.004: Credential API Hooking]]) or rely on deceiving the user into providing input into what they believe to be a genuine service (e.g. [[T1056-input_capture#^t1056003-web-portal-capture|T1056.003: Web Portal Capture]]).

## Workspace

- [[workspaces/attack/techniques/T1056-input_capture-note|Open workspace note]]

![[workspaces/attack/techniques/T1056-input_capture-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/49aae26c_450e_448b_911d_b3c13d178dfc-linux_keylogging_with_pam_d|Linux Keylogging with Pam.d (high; linux / auditd)]]

### Atomic Tests

- [[kb/atomic/tests/0e59d59d_3265_4d35_bebd_bf5c1ec40db5-logging_bash_history_to_syslog|Logging bash history to syslog (sh; linux)]]
- [[kb/atomic/tests/2b162bfd_0928_4d4c_9ec3_4d9f88374b52-powershell_prompt_user_for_password|PowerShell - Prompt User for Password (powershell; windows)]]
- [[kb/atomic/tests/76628574_0bc1_4646_8fe2_8f4427b47d15-applescript_prompt_user_for_password|AppleScript - Prompt User for Password (bash; macos)]]
- [[kb/atomic/tests/7f85a946_a0ea_48aa_b6ac_8ff539278258-bash_session_based_keylogger|Bash session based keylogger (bash; linux)]]
- [[kb/atomic/tests/81d7d2ad_d644_4b6a_bea7_28ffe43becca-sshd_pam_keylogger|SSHD PAM keylogger (sh; linux)]]
- [[kb/atomic/tests/9c6bdb34_a89f_4b90_acb1_5970614c711b-living_off_the_land_terminal_input_capture_on_linux_with_pam_d|Living off the land Terminal Input Capture on Linux with pam.d (sh; linux)]]
- [[kb/atomic/tests/a668edb9_334e_48eb_8c2e_5413a40867af-auditd_keylogger|Auditd keylogger (sh; linux)]]
- [[kb/atomic/tests/aee3a097_4c5c_4fff_bbd3_0a705867ae29-macos_swift_keylogger|MacOS Swift Keylogger (bash; macos)]]
- [[kb/atomic/tests/b04284dc_3bd9_4840_8d21_61b8d31c99f2-logging_sh_history_to_syslog_messages|Logging sh history to syslog/messages (sh; linux)]]
- [[kb/atomic/tests/b7037b89_947a_427a_ba29_e7e9f09bc045-applescript_spoofing_a_credential_prompt_using_osascript|AppleScript - Spoofing a credential prompt using osascript (bash; macos)]]
- 2 more in the generated source index

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0009-collection|TA0009: Collection]]
- [[TA0006-credential_access|TA0006: Credential Access]]

## D3FEND

- [[D3-AVE-asset_vulnerability_enumeration|D3-AVE: Asset Vulnerability Enumeration]]
- [[D3-HCI-hardware_component_inventory|D3-HCI: Hardware Component Inventory]]
- [[D3-IDA-input_device_analysis|D3-IDA: Input Device Analysis]]
- [[D3-IOPR-io_port_restriction|D3-IOPR: IO Port Restriction]]
- [[D3-MBT-memory_boundary_tracking|D3-MBT: Memory Boundary Tracking]]
- [[D3-PCSV-process_code_segment_verification|D3-PCSV: Process Code Segment Verification]]
- [[D3-PSEP-process_segment_execution_prevention|D3-PSEP: Process Segment Execution Prevention]]
- [[D3-RH-radiation_hardening|D3-RH: Radiation Hardening]]
- [[D3-RS-restore_software|D3-RS: Restore Software]]
- [[D3-SAOR-segment_address_offset_randomization|D3-SAOR: Segment Address Offset Randomization]]
- [[D3-SBV-service_binary_verification|D3-SBV: Service Binary Verification]]
- [[D3-SU-software_update|D3-SU: Software Update]]
- [[D3-SWI-software_inventory|D3-SWI: Software Inventory]]

## Subtechniques

### T1056.001: Keylogging

^t1056001-keylogging

Adversaries may log user keystrokes to intercept credentials as the user types them. Keylogging is likely to be used to acquire credentials for new access opportunities when [[T1003-os_credential_dumping|T1003: OS Credential Dumping]] efforts are not effective, and may require an adversary to intercept keystrokes on a system for a substantial period of time before credentials can be successfully captured. In order to increase the likelihood of capturing credentials quickly, an adversary may also perform actions such as clearing browser cookies to force users to reauthenticate to systems.(Citation: Talos Kimsuky Nov 2021)

Keylogging is the most prevalent type of input capture, with many different ways of intercepting keystrokes.(Citation: Adventures of a Keystroke) Some methods include:

* Hooking API callbacks used for processing keystrokes. Unlike [[T1056-input_capture#^t1056004-credential-api-hooking|T1056.004: Credential API Hooking]], this focuses solely on API functions intended for processing keystroke data.
* Reading raw keystroke data from the hardware buffer.
* Windows Registry modifications.
* Custom drivers.
* [[T1601-modify_system_image|T1601: Modify System Image]] may provide adversaries with hooks into the operating system of network devices to read raw keystrokes for login sessions.(Citation: Cisco Blog Legacy Device Attacks) 

### T1056.002: GUI Input Capture

^t1056002-gui-input-capture

Adversaries may mimic common operating system GUI components to prompt users for credentials with a seemingly legitimate prompt. When programs are executed that need additional privileges than are present in the current user context, it is common for the operating system to prompt the user for proper credentials to authorize the elevated privileges for the task (ex: [[T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]).

Adversaries may mimic this functionality to prompt users for credentials with a seemingly legitimate prompt for a number of reasons that mimic normal usage, such as a fake installer requiring additional access or a fake malware removal suite.(Citation: OSX Malware Exploits MacKeeper) This type of prompt can be used to collect credentials via various languages such as [[T1059-command_and_scripting_interpreter#^t1059002-applescript|T1059.002: AppleScript]](Citation: LogRhythm Do You Trust Oct 2014)(Citation: OSX Keydnap malware)(Citation: Spoofing credential dialogs) and [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]].(Citation: LogRhythm Do You Trust Oct 2014)(Citation: Enigma Phishing for Credentials Jan 2015)(Citation: Spoofing credential dialogs) On Linux systems adversaries may launch dialog boxes prompting users for credentials from malicious shell scripts or the command line (i.e. [[T1059-command_and_scripting_interpreter#^t1059004-unix-shell|T1059.004: Unix Shell]]).(Citation: Spoofing credential dialogs)

Adversaries may also mimic common software authentication requests, such as those from browsers or email clients. This may also be paired with user activity monitoring (i.e., [[T1217-browser_information_discovery|T1217: Browser Information Discovery]] and/or [[T1010-application_window_discovery|T1010: Application Window Discovery]]) to spoof prompts when users are naturally accessing sensitive sites/data.

### T1056.003: Web Portal Capture

^t1056003-web-portal-capture

Adversaries may install code on externally facing portals, such as a VPN login page, to capture and transmit credentials of users who attempt to log into the service. For example, a compromised login page may log provided user credentials before logging the user in to the service.

This variation on input capture may be conducted post-compromise using legitimate administrative access as a backup measure to maintain network access through [[T1133-external_remote_services|T1133: External Remote Services]] and [[T1078-valid_accounts|T1078: Valid Accounts]] or as part of the initial compromise by exploitation of the externally facing web service.(Citation: Volexity Virtual Private Keylogging)

### T1056.004: Credential API Hooking

^t1056004-credential-api-hooking

Adversaries may hook into Windows application programming interface (API) functions and Linux system functions to collect user credentials. Malicious hooking mechanisms may capture API or function calls that include parameters that reveal user authentication credentials.(Citation: Microsoft TrojanSpy:Win32/Ursnif.gen!I Sept 2017) Unlike [[T1056-input_capture#^t1056001-keylogging|T1056.001: Keylogging]], this technique focuses specifically on API functions that include parameters that reveal user credentials. 

In Windows, hooking involves redirecting calls to these functions and can be implemented via:

* **Hooks procedures**, which intercept and execute designated code in response to events such as messages, keystrokes, and mouse inputs.(Citation: Microsoft Hook Overview)(Citation: Elastic Process Injection July 2017)
* **Import address table (IAT) hooking**, which use modifications to a process’s IAT, where pointers to imported API functions are stored.(Citation: Elastic Process Injection July 2017)(Citation: Adlice Software IAT Hooks Oct 2014)(Citation: MWRInfoSecurity Dynamic Hooking 2015)
* **Inline hooking**, which overwrites the first bytes in an API function to redirect code flow.(Citation: Elastic Process Injection July 2017)(Citation: HighTech Bridge Inline Hooking Sept 2011)(Citation: MWRInfoSecurity Dynamic Hooking 2015)

In Linux and macOS, adversaries may hook into system functions via the `LD_PRELOAD` (Linux) or `DYLD_INSERT_LIBRARIES` (macOS) environment variables, which enables loading shared libraries into a program’s address space. For example, an adversary may capture credentials by hooking into the `libc read` function leveraged by SSH or SCP.(Citation: Intezer Symbiote 2022)

## Tools

- [[nppspy|NPPSPY (S1131)]]

## Platforms

- Linux
- macOS
- Network Devices
- Windows

