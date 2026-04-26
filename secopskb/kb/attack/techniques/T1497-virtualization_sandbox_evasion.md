---
mitre_id: "T1497"
mitre_name: "Virtualization/Sandbox Evasion"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--82caa33e-d11a-433a-94ea-9b5a5fbef81d"
mitre_created: "2019-04-17T22:22:24.505Z"
mitre_modified: "2025-10-24T17:49:02.638Z"
mitre_version: "1.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1497/"
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
  - "TA0005"
  - "TA0007"
d3fend_ids:
  - "D3-AVE"
  - "D3-RS"
  - "D3-SCA"
  - "D3-SCF"
  - "D3-SU"
  - "D3-SWI"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may employ various means to detect and avoid virtualization and analysis environments. This may include changing behaviors based on the results of checks for the presence of artifacts indicative of a virtual machine environment (VME) or sandbox. If the adversary detects a VME, they may alter their malware to disengage from the victim or conceal the core functions of the implant. They may also search for VME artifacts before dropping secondary or additional payloads. Adversaries may use the information learned from [[T1497-virtualization_sandbox_evasion|T1497: Virtualization/Sandbox Evasion]] during automated discovery to shape follow-on behaviors.(Citation: Deloitte Environment Awareness)

Adversaries may use several methods to accomplish [[T1497-virtualization_sandbox_evasion|T1497: Virtualization/Sandbox Evasion]] such as checking for security monitoring tools (e.g., Sysinternals, Wireshark, etc.) or other system artifacts associated with analysis or virtualization. Adversaries may also check for legitimate user activity to help determine if it is in an analysis environment. Additional methods include use of sleep timers or loops within malware code to avoid operating within a temporary sandbox.(Citation: Unit 42 Pirpi July 2015)



## Workspace

- [[workspaces/attack/techniques/T1497-virtualization_sandbox_evasion-note|Open workspace note]]

![[workspaces/attack/techniques/T1497-virtualization_sandbox_evasion-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Atomic Tests

- [[kb/atomic/tests/2b73cd9b_b2fb_4357_b9d7_c73c41d9e945-check_if_system_integrity_protection_is_enabled|Check if System Integrity Protection is enabled (sh; macos)]]
- [[kb/atomic/tests/4a41089a_48e0_47aa_82cb_5b81a463bc78-detect_virtualization_environment_via_wmi_manufacturer_model_listing_windows|Detect Virtualization Environment via WMI Manufacturer/Model Listing (Windows) (powershell; windows)]]
- [[kb/atomic/tests/502a7dc4_9d6f_4d28_abf2_f0e84692562d-detect_virtualization_environment_windows|Detect Virtualization Environment (Windows) (powershell; windows)]]
- [[kb/atomic/tests/6beae646_eb4c_4730_95be_691a4094408c-detect_virtualization_environment_using_sysctl_hw_model|Detect Virtualization Environment using sysctl (hw.model) (sh; macos)]]
- [[kb/atomic/tests/8b87dd03_8204_478c_bac3_3959f6528de3-delay_execution_with_ping|Delay execution with ping (sh; linux, macos)]]
- [[kb/atomic/tests/a960185f_aef6_4547_8350_d1ce16680d09-detect_virtualization_environment_via_ioreg|Detect Virtualization Environment via ioreg (sh; macos)]]
- [[kb/atomic/tests/dfbd1a21_540d_4574_9731_e852bd6fe840-detect_virtualization_environment_linux|Detect Virtualization Environment (Linux) (sh; linux)]]
- [[kb/atomic/tests/e04d2e89_de15_4d90_92f9_a335c7337f0f-detect_virtualization_environment_using_system_profiler|Detect Virtualization Environment using system_profiler (sh; macos)]]
- [[kb/atomic/tests/e129d73b_3e03_4ae9_bf1e_67fc8921e0fd-detect_virtualization_environment_freebsd|Detect Virtualization Environment (FreeBSD) (sh; linux)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]
- [[TA0007-discovery|TA0007: Discovery]]

## D3FEND

- [[D3-AVE-asset_vulnerability_enumeration|D3-AVE: Asset Vulnerability Enumeration]]
- [[D3-RS-restore_software|D3-RS: Restore Software]]
- [[D3-SCA-system_call_analysis|D3-SCA: System Call Analysis]]
- [[D3-SCF-system_call_filtering|D3-SCF: System Call Filtering]]
- [[D3-SU-software_update|D3-SU: Software Update]]
- [[D3-SWI-software_inventory|D3-SWI: Software Inventory]]

## Subtechniques

### T1497.001: System Checks

^t1497001-system-checks

Adversaries may employ various system checks to detect and avoid virtualization and analysis environments. This may include changing behaviors based on the results of checks for the presence of artifacts indicative of a virtual machine environment (VME) or sandbox. If the adversary detects a VME, they may alter their malware to disengage from the victim or conceal the core functions of the implant. They may also search for VME artifacts before dropping secondary or additional payloads. Adversaries may use the information learned from [[T1497-virtualization_sandbox_evasion|T1497: Virtualization/Sandbox Evasion]] during automated discovery to shape follow-on behaviors.(Citation: Deloitte Environment Awareness)

Specific checks will vary based on the target and/or adversary, but may involve behaviors such as [[T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]], [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]], [[T1082-system_information_discovery|T1082: System Information Discovery]], and [[T1012-query_registry|T1012: Query Registry]] to obtain system information and search for VME artifacts. Adversaries may search for VME artifacts in memory, processes, file system, hardware, and/or the Registry. Adversaries may use scripting to automate these checks  into one script and then have the program exit if it determines the system to be a virtual environment. 

Checks could include generic system properties such as host/domain name and samples of network traffic. Adversaries may also check the network adapters addresses, CPU core count, and available memory/drive size. Once executed, malware may also use [[T1083-file_and_directory_discovery|T1083: File and Directory Discovery]] to check if it was saved in a folder or file with unexpected or even analysis-related naming artifacts such as `malware`, `sample`, or `hash`.

Other common checks may enumerate services running that are unique to these applications, installed programs on the system, manufacturer/product fields for strings relating to virtual machine applications, and VME-specific hardware/processor instructions.(Citation: McAfee Virtual Jan 2017) In applications like VMWare, adversaries can also use a special I/O port to send commands and receive output. 
 
Hardware checks, such as the presence of the fan, temperature, and audio devices, could also be used to gather evidence that can be indicative a virtual environment. Adversaries may also query for specific readings from these devices.(Citation: Unit 42 OilRig Sept 2018)

### T1497.002: User Activity Based Checks

^t1497002-user-activity-based-checks

Adversaries may employ various user activity checks to detect and avoid virtualization and analysis environments. This may include changing behaviors based on the results of checks for the presence of artifacts indicative of a virtual machine environment (VME) or sandbox. If the adversary detects a VME, they may alter their malware to disengage from the victim or conceal the core functions of the implant. They may also search for VME artifacts before dropping secondary or additional payloads. Adversaries may use the information learned from [[T1497-virtualization_sandbox_evasion|T1497: Virtualization/Sandbox Evasion]] during automated discovery to shape follow-on behaviors.(Citation: Deloitte Environment Awareness)

Adversaries may search for user activity on the host based on variables such as the speed/frequency of mouse movements and clicks (Citation: Sans Virtual Jan 2016) , browser history, cache, bookmarks, or number of files in common directories such as home or the desktop. Other methods may rely on specific user interaction with the system before the malicious code is activated, such as waiting for a document to close before activating a macro (Citation: Unit 42 Sofacy Nov 2018) or waiting for a user to double click on an embedded image to activate.(Citation: FireEye FIN7 April 2017) 

### T1497.003: Time Based Checks

^t1497003-time-based-checks

Adversaries may employ various time-based methods to detect virtualization and analysis environments, particularly those that attempt to manipulate time mechanisms to simulate longer elapses of time. This may include enumerating time-based properties, such as uptime or the system clock. 

Adversaries may use calls like `GetTickCount` and `GetSystemTimeAsFileTime` to discover if they are operating within a virtual machine or sandbox, or may be able to identify a sandbox accelerating time by sampling and calculating the expected value for an environment's timestamp before and after execution of a sleep function.(Citation: ISACA Malware Tricks)

## Platforms

- Linux
- macOS
- Windows

