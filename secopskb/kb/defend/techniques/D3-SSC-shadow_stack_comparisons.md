---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-SSC"
d3fend_name: "Shadow Stack Comparisons"
d3fend_ontology_id: "d3f:ShadowStackComparisons"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AShadowStackComparisons/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1068"
  - "T1203"
  - "T1210"
  - "T1211"
  - "T1212"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Comparing a call stack in system memory with a shadow call stack maintained by the processor to determine unauthorized shellcode activity.

## Workspace

- [[workspaces/defend/techniques/D3-SSC-shadow_stack_comparisons-note|Open workspace note]]

![[workspaces/defend/techniques/D3-SSC-shadow_stack_comparisons-note]]

## Parent Technique

- [[D3-PA-process_analysis|D3-PA: Process Analysis]]

## Related ATT&CK Techniques

- [[T1068-exploitation_for_privilege_escalation|T1068: Exploitation for Privilege Escalation]]
- [[T1203-exploitation_for_client_execution|T1203: Exploitation for Client Execution]]
- [[T1210-exploitation_of_remote_services|T1210: Exploitation of Remote Services]]
- [[T1211-exploitation_for_defense_evasion|T1211: Exploitation for Defense Evasion]]
- [[T1212-exploitation_for_credential_access|T1212: Exploitation for Credential Access]]

## Knowledge Base Article

## How it works
This technique compares the call stack stored in system memory with the shadow call stack maintained in the cache memory of the processor.  Mismatches between the two are compared since a return oriented programming attack may only be able to control or spoof the call stack and not the shadow call stack. Mismatches are counted and if the number of mismatches exceeds a certain threshold it is an indication of unauthorized activity and a security response action is performed.

## Considerations
If the threshold for detecting a stack anomaly is low, it may not detect a return-oriented attack with just one gadget, such as a return-to-libc or return-to-plt attack.  Additionally, this technique may not detect JOP (Jump-oriented programming), as the return instruction is not executed.

## Ontology Relationships

- [[D3-PA-process_analysis|D3-PA: Process Analysis]]

