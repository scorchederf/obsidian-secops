---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-SBV"
d3fend_name: "Service Binary Verification"
d3fend_ontology_id: "d3f:ServiceBinaryVerification"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AServiceBinaryVerification/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1056"
  - "T1056.003"
  - "T1072"
  - "T1212"
  - "T1564"
  - "T1564.006"
  - "T1574"
  - "T1574.005"
  - "T1574.010"
  - "T1649"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Analyzing changes in service binary files by comparing to a source of truth.

## Workspace

- [[workspaces/defend/techniques/D3-SBV-service_binary_verification-note|Open workspace note]]

![[workspaces/defend/techniques/D3-SBV-service_binary_verification-note]]

## Parent Technique

- [[D3-SFA-system_file_analysis|D3-SFA: System File Analysis]]

## Related ATT&CK Techniques

- [[T1056-input_capture|T1056: Input Capture]]
- [[T1056-input_capture#^t1056003-web-portal-capture|T1056.003: Web Portal Capture]]
- [[T1072-software_deployment_tools|T1072: Software Deployment Tools]]
- [[T1212-exploitation_for_credential_access|T1212: Exploitation for Credential Access]]
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]
- [[T1564-hide_artifacts#^t1564006-run-virtual-instance|T1564.006: Run Virtual Instance]]
- [[T1574-hijack_execution_flow|T1574: Hijack Execution Flow]]
- [[T1574-hijack_execution_flow#^t1574005-executable-installer-file-permissions-weakness|T1574.005: Executable Installer File Permissions Weakness]]
- [[T1574-hijack_execution_flow#^t1574010-services-file-permissions-weakness|T1574.010: Services File Permissions Weakness]]
- [[T1649-steal_or_forge_authentication_certificates|T1649: Steal or Forge Authentication Certificates]]

## Knowledge Base Article

## How it works
System service applications may originate from the operating system installation or third-party applications installed with administrative privileges. These services have an entry point of some executable file-- a binary or a script. Attackers sometimes modify these executables to launch their own code. Analyzing changes in these files may uncover unauthorized activity.

## Considerations
* These files change for legitimate reasons when the system or software updates.
* The source of truth must not be corrupted in order for this method to work.

## Ontology Relationships

- [[D3-SFA-system_file_analysis|D3-SFA: System File Analysis]]

