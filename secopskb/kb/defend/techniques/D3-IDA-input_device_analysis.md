---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-IDA"
d3fend_name: "Input Device Analysis"
d3fend_ontology_id: "d3f:InputDeviceAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AInputDeviceAnalysis/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1056"
  - "T1056.001"
  - "T1123"
  - "T1125"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Operating system level mechanisms to prevent abusive input device exploitation.

## Workspace

- [[workspaces/defend/techniques/D3-IDA-input_device_analysis-note|Open workspace note]]

![[workspaces/defend/techniques/D3-IDA-input_device_analysis-note]]

## Parent Technique

- [[D3-OSM-operating_system_monitoring|D3-OSM: Operating System Monitoring]]

## Related ATT&CK Techniques

- [[T1056-input_capture|T1056: Input Capture]]
- [[T1056-input_capture#^t1056001-keylogging|T1056.001: Keylogging]]
- [[T1123-audio_capture|T1123: Audio Capture]]
- [[T1125-video_capture|T1125: Video Capture]]

## Knowledge Base Article

## How it works

Input Device Hardening techniques filter certain commands, or disable related operating system functionality.

### Analytics

All of these values can be analyzed and compared to a baseline:

* Amount of input
* Duration of a single input
* Durations between inputs
* Value of input

Context can also include:

* User which is logged in, to include attributes such as physical location of the user
* Date and time
* System which is processing the input
* Source device of input, to include its properties (eg. manufacturer), configuration (eg. keyboard layout) and behavioral attributes of this device (eg. first use)
* Source system of input (local or remote system)
* Other hardware devices attached to the system


### Actions

Actions can include:

* Disabling the source device
* Sending an alert
* Locking the current session (eg. system screen lock, or returning to an authentication screen in a web app) and requiring one or more methods of authentication to continue
* Administratively disabling credentials for the account or the entire account -- the technique *Account Locking*


### Examples
A malicious input device sends many keystrokes with approximately the same delay between each.  This does not match the normal cadence of input, and the device is disabled.

Input to type the session user's name takes abnormally longer for each keystroke.  The system is locked to the password prompt screen.

A system receives key press events from two different devices -- one device sends keystrokes after the other has been idle for a long time.

A system receives physical input in a user session, while that user has sent input from a device located out of the country in the past hour.

Network traffic is suddenly routed through a new external device, and nearly the same volume of network traffic is subsequently sent out the previously existing interface.  The new external device is disabled, and an alert is raised to investigate the network configuration for a potential compromise.


## Considerations

Given some example of legitimate behavioral input patterns, attackers could mimic those input patterns, a technique which has been used in popular culture in the creation of Deepfake videos and [This Person Does Not Exist](https://thispersondoesnotexist.com).

## Ontology Relationships

- [[D3-OSM-operating_system_monitoring|D3-OSM: Operating System Monitoring]]

