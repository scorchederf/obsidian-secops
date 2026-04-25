---
mitre_id: "M1048"
mitre_name: "Application Isolation and Sandboxing"
mitre_type: "course-of-action"
mitre_stix_id: "course-of-action--b9f0c069-abbe-4a07-a245-2481219a1463"
mitre_created: "2019-06-11T17:06:56.230Z"
mitre_modified: "2025-05-09T16:23:40.086Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/mitigations/M1048/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 14:47:22"
build_source: "script"
object_type: "mitigation"
tags:
  - "attack"
  - "mitigation"
  - "defense"
  - "countermeasure"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

Application Isolation and Sandboxing refers to the technique of restricting the execution of code to a controlled and isolated environment (e.g., a virtual environment, container, or sandbox). This method prevents potentially malicious code from affecting the rest of the system or network by limiting access to sensitive resources and critical operations. The goal is to contain threats and minimize their impact. This mitigation can be implemented through the following measures:

Browser Sandboxing:

- Use Case: Implement browser sandboxing to isolate untrusted web content and prevent malicious web pages or scripts from accessing sensitive system resources or initiating unauthorized downloads.
- Implementation: Use browsers with built-in sandboxing features (e.g., Google Chrome, Microsoft Edge) or deploy enhanced browser security frameworks that limit the execution scope of active content. Consider controls that monitor or restrict script-based file generation and downloads commonly abused in evasion techniques like HTML smuggling.

Application Virtualization:

- Use Case: Deploy critical or high-risk applications in a virtualized environment to ensure any compromise does not affect the host system.
- Implementation: Use application virtualization platforms to run applications in isolated environments.

Email Attachment Sandboxing:

- Use Case: Route email attachments to a sandbox environment to detect and block malware before delivering emails to end-users.
- Implementation: Integrate security solutions with sandbox capabilities to analyze email attachments.

Endpoint Sandboxing:

- Use Case: Run all downloaded files and applications in a restricted environment to monitor their behavior for malicious activity.
- Implementation: Use endpoint protection tools for sandboxing at the endpoint level.

## Workspace

- [[notes/attack/mitigations/M1048-application_isolation_and_sandboxing-note|Open workspace note]]

![[notes/attack/mitigations/M1048-application_isolation_and_sandboxing-note]]

## Mitigates Techniques

- [[T1021-remote_services|T1021: Remote Services]]
    - [[T1021-remote_services#^t1021003-distributed-component-object-model|T1021.003: Distributed Component Object Model]]
- [[T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]]
    - [[T1027-obfuscated_files_or_information#^t1027006-html-smuggling|T1027.006: HTML Smuggling]]
    - [[T1027-obfuscated_files_or_information#^t1027017-svg-smuggling|T1027.017: SVG Smuggling]]
- [[T1068-exploitation_for_privilege_escalation|T1068: Exploitation for Privilege Escalation]]
- [[T1189-drive-by_compromise|T1189: Drive-by Compromise]]
- [[T1190-exploit_public-facing_application|T1190: Exploit Public-Facing Application]]
- [[T1203-exploitation_for_client_execution|T1203: Exploitation for Client Execution]]
- [[T1210-exploitation_of_remote_services|T1210: Exploitation of Remote Services]]
- [[T1211-exploitation_for_defense_evasion|T1211: Exploitation for Defense Evasion]]
- [[T1212-exploitation_for_credential_access|T1212: Exploitation for Credential Access]]
- [[T1559-inter-process_communication|T1559: Inter-Process Communication]]
- [[T1559-inter-process_communication|T1559: Inter-Process Communication]]
    - [[T1559-inter-process_communication#^t1559001-component-object-model|T1559.001: Component Object Model]]
    - [[T1559-inter-process_communication#^t1559002-dynamic-data-exchange|T1559.002: Dynamic Data Exchange]]
- [[T1611-escape_to_host|T1611: Escape to Host]]

