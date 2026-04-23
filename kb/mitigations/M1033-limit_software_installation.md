---
mitre_id: "M1033"
mitre_name: "Limit Software Installation"
mitre_type: "course-of-action"
mitre_stix_id: "course-of-action--23843cff-f7b9-4659-a7b7-713ef347f547"
mitre_created: "2019-06-11T16:26:52.202Z"
mitre_modified: "2024-12-18T16:17:46.153Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/mitigations/M1033/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
---

# M1033: Limit Software Installation

Prevent users or groups from installing unauthorized or unapproved software to reduce the risk of introducing malicious or vulnerable applications. This can be achieved through allowlists, software restriction policies, endpoint management tools, and least privilege access principles. This mitigation can be implemented through the following measures:

Application Whitelisting

- Implement Microsoft AppLocker or Windows Defender Application Control (WDAC) to create and enforce allowlists for approved software.
- Whitelist applications based on file hash, path, or digital signatures.

Restrict User Permissions

- Remove local administrator rights for all non-IT users.
- Use Role-Based Access Control (RBAC) to restrict installation permissions to privileged accounts only.

Software Restriction Policies (SRP)

- Use GPO to configure SRP to deny execution of binaries from directories such as `%AppData%`, `%Temp%`, and external drives.
- Restrict specific file types (`.exe`, `.bat`, `.msi`, `.js`, `.vbs`) to trusted directories only.

Endpoint Management Solutions

- Deploy tools like Microsoft Intune, SCCM, or Jamf for centralized software management.
- Maintain a list of approved software, versions, and updates across the enterprise.

Monitor Software Installation Events

- Enable logging of software installation events and monitor Windows Event ID 4688 and Event ID 11707 for software installs.
- Use SIEM or EDR tools to alert on attempts to install unapproved software.

Implement Software Inventory Management

- Use tools like OSQuery or Wazuh to scan for unauthorized software on endpoints and servers.
- Conduct regular audits to detect and remove unapproved software.

*Tools for Implementation*

Application Whitelisting:

- Microsoft AppLocker
- Windows Defender Application Control (WDAC)

Endpoint Management:

- Microsoft Intune
- SCCM (System Center Configuration Manager)
- Jamf Pro (macOS)
- Puppet or Ansible for automation

Software Restriction Policies:

- Group Policy Object (GPO)
- Microsoft Software Restriction Policies (SRP)

Monitoring and Logging:

- Splunk
- OSQuery
- Wazuh (open-source SIEM and XDR)
- EDRs

Inventory Management and Auditing:

- OSQuery
- Wazuh

## Mitigates Techniques

- [[T1021-remote_services|T1021: Remote Services]]
- [[T1021-remote_services#^t1021005-vnc|T1021.005: VNC]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
- [[T1059-command_and_scripting_interpreter#^t1059006-python|T1059.006: Python]]
- [[T1059-command_and_scripting_interpreter#^t1059011-lua|T1059.011: Lua]]
- [[T1072-software_deployment_tools|T1072: Software Deployment Tools]]
- [[T1176-software_extensions|T1176: Software Extensions]]
- [[T1176-software_extensions|T1176: Software Extensions]]
- [[T1176-software_extensions#^t1176001-browser-extensions|T1176.001: Browser Extensions]]
- [[T1176-software_extensions#^t1176002-ide-extensions|T1176.002: IDE Extensions]]
- [[T1195-supply_chain_compromise|T1195: Supply Chain Compromise]]
- [[T1195-supply_chain_compromise|T1195: Supply Chain Compromise]]
- [[T1195-supply_chain_compromise#^t1195001-compromise-software-dependencies-and-development-tools|T1195.001: Compromise Software Dependencies and Development Tools]]
- [[T1204-user_execution|T1204: User Execution]]
- [[T1204-user_execution|T1204: User Execution]]
- [[T1204-user_execution#^t1204005-malicious-library|T1204.005: Malicious Library]]
- [[T1543-create_or_modify_system_process|T1543: Create or Modify System Process]]
- [[T1543-create_or_modify_system_process|T1543: Create or Modify System Process]]
- [[T1543-create_or_modify_system_process#^t1543002-systemd-service|T1543.002: Systemd Service]]
- [[T1547-boot_or_logon_autostart_execution|T1547: Boot or Logon Autostart Execution]]
- [[T1547-boot_or_logon_autostart_execution#^t1547013-xdg-autostart-entries|T1547.013: XDG Autostart Entries]]
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]
- [[T1564-hide_artifacts#^t1564003-hidden-window|T1564.003: Hidden Window]]

