---
mitre_id: "T1674"
mitre_name: "Input Injection"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--63e3d25c-d57d-407d-8e6a-2cecd71f90be"
mitre_created: "2025-03-27T18:14:06.330Z"
mitre_modified: "2025-04-15T19:58:36.409Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1674/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
  - "macOS"
  - "Linux"
mitre_tactic_ids:
  - "TA0002"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may simulate keystrokes on a victim’s computer by various means to perform any type of action on behalf of the user, such as launching the command interpreter using keyboard shortcuts,  typing an inline script to be executed, or interacting directly with a GUI-based application.  These actions can be preprogrammed into adversary tooling or executed through physical devices such as Human Interface Devices (HIDs).

For example, adversaries have used tooling that monitors the Windows message loop to detect when a user visits bank-specific URLs. If detected, the tool then simulates keystrokes to open the developer console or select the address bar, pastes malicious JavaScript from the clipboard, and executes it - enabling manipulation of content within the browser, such as replacing bank account numbers during transactions.(Citation: BleepingComputer BackSwap)(Citation: welivesecurity BackSwap)

Adversaries have also used malicious USB devices to emulate keystrokes that launch PowerShell, leading to the download and execution of malware from adversary-controlled servers.(Citation: BleepingComputer USB)

## Workspace

- [[workspaces/attack/techniques/T1674-input_injection-note|Open workspace note]]

![[workspaces/attack/techniques/T1674-input_injection-note]]

## Tactics

- [[TA0002-execution|TA0002: Execution]]

## Mitigations

- [[M1034-limit_hardware_installation|M1034: Limit Hardware Installation]]
- [[M1038-execution_prevention|M1038: Execution Prevention]]

## Platforms

- Windows
- macOS
- Linux

