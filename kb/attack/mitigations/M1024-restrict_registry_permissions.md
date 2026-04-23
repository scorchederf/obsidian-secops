---
mitre_id: "M1024"
mitre_name: "Restrict Registry Permissions"
mitre_type: "course-of-action"
mitre_stix_id: "course-of-action--a2c36a5d-4058-475e-8e77-fff75e50d3b9"
mitre_created: "2019-06-06T20:58:59.577Z"
mitre_modified: "2024-12-24T13:34:49.309Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/mitigations/M1024/"
framework: "attack"
generated: "true"
build_date: "2026-04-23 22:40:56"
build_source: "script"
object_type: "mitigation"
tags:
  - "attack"
  - "mitigation"
  - "defense"
  - "countermeasure"
---

# M1024: Restrict Registry Permissions

Restricting registry permissions involves configuring access control settings for sensitive registry keys and hives to ensure that only authorized users or processes can make modifications. By limiting access, organizations can prevent unauthorized changes that adversaries might use for persistence, privilege escalation, or defense evasion. This mitigation can be implemented through the following measures:

Review and Adjust Permissions on Critical Keys

- Regularly review permissions on keys such as `Run`, `RunOnce`, and `Services` to ensure only authorized users have write access.
- Use tools like `icacls` or `PowerShell` to automate permission adjustments.

Enable Registry Auditing

- Enable auditing on sensitive keys to log access attempts.
- Use Event Viewer or SIEM solutions to analyze logs and detect suspicious activity.
- Example Audit Policy: `auditpol /set /subcategory:"Registry" /success:enable /failure:enable`

Protect Credential-Related Hives

- Limit access to hives like `SAM`,`SECURITY`, and `SYSTEM` to prevent credential dumping or other unauthorized access.
- Use LSA Protection to add an additional security layer for credential storage.

Restrict Registry Editor Usage

- Use Group Policy to restrict access to regedit.exe for non-administrative users.
- Block execution of registry editing tools on endpoints where they are unnecessary.

Deploy Baseline Configuration Tools

- Use tools like Microsoft Security Compliance Toolkit or CIS Benchmarks to apply and maintain secure registry configurations.

*Tools for Implementation* 

Registry Permission Tools:

- Registry Editor (regedit): Built-in tool to manage registry permissions.
- PowerShell: Automate permissions and manage keys. `Set-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "KeyName" -Value "Value"`
- icacls: Command-line tool to modify ACLs.

Monitoring Tools:

- Sysmon: Monitor and log registry events.
- Event Viewer: View registry access logs.

Policy Management Tools:

- Group Policy Management Console (GPMC): Enforce registry permissions via GPOs.
- Microsoft Endpoint Manager: Deploy configuration baselines for registry permissions.

## Mitigates Techniques

- [[T1037-boot_or_logon_initialization_scripts|T1037: Boot or Logon Initialization Scripts]]
- [[T1037-boot_or_logon_initialization_scripts|T1037: Boot or Logon Initialization Scripts]]
    - [[T1037-boot_or_logon_initialization_scripts#^t1037001-logon-script-(windows)|T1037.001: Logon Script (Windows)]]
- [[T1070-indicator_removal|T1070: Indicator Removal]]
    - [[T1070-indicator_removal#^t1070007-clear-network-connection-history-and-configurations|T1070.007: Clear Network Connection History and Configurations]]
- [[T1112-modify_registry|T1112: Modify Registry]]
- [[T1489-service_stop|T1489: Service Stop]]
- [[T1505-server_software_component|T1505: Server Software Component]]
- [[T1505-server_software_component|T1505: Server Software Component]]
    - [[T1505-server_software_component#^t1505005-terminal-services-dll|T1505.005: Terminal Services DLL]]
- [[T1547-boot_or_logon_autostart_execution|T1547: Boot or Logon Autostart Execution]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547003-time-providers|T1547.003: Time Providers]]
- [[T1553-subvert_trust_controls|T1553: Subvert Trust Controls]]
- [[T1553-subvert_trust_controls|T1553: Subvert Trust Controls]]
    - [[T1553-subvert_trust_controls#^t1553003-sip-and-trust-provider-hijacking|T1553.003: SIP and Trust Provider Hijacking]]
    - [[T1553-subvert_trust_controls#^t1553006-code-signing-policy-modification|T1553.006: Code Signing Policy Modification]]
- [[T1556-modify_authentication_process|T1556: Modify Authentication Process]]
- [[T1556-modify_authentication_process|T1556: Modify Authentication Process]]
    - [[T1556-modify_authentication_process#^t1556008-network-provider-dll|T1556.008: Network Provider DLL]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
    - [[T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]
    - [[T1562-impair_defenses#^t1562002-disable-windows-event-logging|T1562.002: Disable Windows Event Logging]]
    - [[T1562-impair_defenses#^t1562004-disable-or-modify-system-firewall|T1562.004: Disable or Modify System Firewall]]
- [[T1574-hijack_execution_flow|T1574: Hijack Execution Flow]]
- [[T1574-hijack_execution_flow|T1574: Hijack Execution Flow]]
    - [[T1574-hijack_execution_flow#^t1574011-services-registry-permissions-weakness|T1574.011: Services Registry Permissions Weakness]]
    - [[T1574-hijack_execution_flow#^t1574012-cor-profiler|T1574.012: COR_PROFILER]]

## Workspace

- [[kb/notes/attack/mitigations/m1024-notes|Open workspace note]]

