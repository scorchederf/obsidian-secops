---
mitre_id: "T1123"
mitre_name: "Audio Capture"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--1035cdf2-3e5f-446f-a7a7-e8f6d7925967"
mitre_created: "2017-05-31T21:31:34.528Z"
mitre_modified: "2025-10-24T17:48:24.702Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1123/"
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
  - "TA0009"
d3fend_ids:
  - "D3-HCI"
  - "D3-IDA"
  - "D3-IOPR"
  - "D3-RH"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

An adversary can leverage a computer's peripheral devices (e.g., microphones and webcams) or applications (e.g., voice and video call services) to capture audio recordings for the purpose of listening into sensitive conversations to gather information.(Citation: ESET Attor Oct 2019)

Malware or scripts may be used to interact with the devices through an available API provided by the operating system or an application to capture audio. Audio files may be written to disk and exfiltrated later.

## Workspace

- [[workspaces/attack/techniques/T1123-audio_capture-note|Open workspace note]]

![[workspaces/attack/techniques/T1123-audio_capture-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/62120148_6b7a_42be_8b91_271c04e281a3-suspicious_camera_and_microphone_access|Suspicious Camera and Microphone Access (high; windows / registry_event)]]
- [[kb/sigma/rules/e30de276_68ec_435c_ab99_ef3befec6c61-opencanary_sip_request|OpenCanary - SIP Request (high; opencanary / application)]]

### Atomic Tests

- [[kb/atomic/tests/7a21cce2_6ada_4f7c_afd9_e1e9c481e44a-registry_artefact_when_application_use_microphone|Registry artefact when application use microphone (command_prompt; windows)]]
- [[kb/atomic/tests/9c3ad250_b185_4444_b5a9_d69218a10c95-using_device_audio_capture_commandlet|using device audio capture commandlet (powershell; windows)]]
- [[kb/atomic/tests/c7a0bb71_70ce_4a53_b115_881f241b795b-using_quicktime_player|using Quicktime Player (sh; macos)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0009-collection|TA0009: Collection]]

## D3FEND

- [[D3-HCI-hardware_component_inventory|D3-HCI: Hardware Component Inventory]]
- [[D3-IDA-input_device_analysis|D3-IDA: Input Device Analysis]]
- [[D3-IOPR-io_port_restriction|D3-IOPR: IO Port Restriction]]
- [[D3-RH-radiation_hardening|D3-RH: Radiation Hardening]]

## Tools
- [[imminent_monitor|Imminent Monitor (S0434)]]
- [[powersploit|PowerSploit (S0194)]]
- [[pupy|Pupy (S0192)]]
- [[remcos|Remcos (S0332)]]


## Platforms

- Linux
- macOS
- Windows

