---
mitre_id: "M1052"
mitre_name: "User Account Control"
mitre_type: "course-of-action"
mitre_stix_id: "course-of-action--2c2ad92a-d710-41ab-a996-1db143bb4808"
mitre_created: "2019-06-11T17:14:35.170Z"
mitre_modified: "2024-12-24T14:26:43.340Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/mitigations/M1052/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "mitigation"
tags:
  - "attack"
  - "mitigation"
  - "defense"
  - "countermeasure"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

User Account Control (UAC) is a security feature in Microsoft Windows that prevents unauthorized changes to the operating system. UAC prompts users to confirm or provide administrator credentials when an action requires elevated privileges. Proper configuration of UAC reduces the risk of privilege escalation attacks. This mitigation can be implemented through the following measures:

Enable UAC Globally:

- Ensure UAC is enabled through Group Policy by setting `User Account Control: Run all administrators in Admin Approval Mode` to `Enabled`.

Require Credential Prompt:

- Use Group Policy to configure UAC to prompt for administrative credentials instead of just confirmation (`User Account Control: Behavior of the elevation prompt`).

Restrict Built-in Administrator Account:

Set `Admin Approval Mode` for the built-in Administrator account to `Enabled` in Group Policy.

Secure the UAC Prompt:

- Configure UAC prompts to display on the secure desktop (`User Account Control: Switch to the secure desktop when prompting for elevation`).

Prevent UAC Bypass:

- Block untrusted applications from triggering UAC prompts by configuring `User Account Control: Only elevate executables that are signed and validated`.
- Use EDR tools to detect and block known UAC bypass techniques.

Monitor UAC-Related Events:

- Use Windows Event Viewer to monitor for event ID 4688 (process creation) and look for suspicious processes attempting to invoke UAC elevation.

*Tools for Implementation*

Built-in Windows Tools:

- Group Policy Editor: Configure UAC settings centrally for enterprise environments.
- Registry Editor: Modify UAC-related settings directly, such as `EnableLUA` and `ConsentPromptBehaviorAdmin`.

Endpoint Security Solutions:

- Microsoft Defender for Endpoint: Detects and blocks UAC bypass techniques.
- Sysmon: Logs process creations and monitors UAC elevation attempts for suspicious activity.

Third-Party Security Tools:

- Process Monitor (Sysinternals): Tracks real-time processes interacting with UAC.
- EventSentry: Monitors Windows Event Logs for UAC-related alerts.

## Workspace

- [[workspaces/attack/mitigations/M1052-user_account_control-note|Open workspace note]]

![[workspaces/attack/mitigations/M1052-user_account_control-note]]

## Mitigates Techniques

- [[T1546-event_triggered_execution|T1546: Event Triggered Execution]]
    - [[T1546-event_triggered_execution#^t1546011-application-shimming|T1546.011: Application Shimming]]
- [[T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]
- [[T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]
    - [[T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]
- [[T1550-use_alternate_authentication_material|T1550: Use Alternate Authentication Material]]
    - [[T1550-use_alternate_authentication_material#^t1550002-pass-the-hash|T1550.002: Pass the Hash]]
- [[T1574-hijack_execution_flow|T1574: Hijack Execution Flow]]
- [[T1574-hijack_execution_flow|T1574: Hijack Execution Flow]]
    - [[T1574-hijack_execution_flow#^t1574005-executable-installer-file-permissions-weakness|T1574.005: Executable Installer File Permissions Weakness]]
    - [[T1574-hijack_execution_flow#^t1574010-services-file-permissions-weakness|T1574.010: Services File Permissions Weakness]]

