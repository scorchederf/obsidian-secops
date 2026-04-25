---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-AH"
d3fend_name: "Application Hardening"
d3fend_ontology_id: "d3f:ApplicationHardening"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AApplicationHardening/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-25 14:47:22"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

Application Hardening makes an executable application more resilient to a class of exploits which either introduce new code or execute unwanted existing code. These techniques may be applied at compile-time or on an application binary.

## Workspace

- [[notes/defend/techniques/D3-AH-application_hardening-note|Open workspace note]]

![[notes/defend/techniques/D3-AH-application_hardening-note]]

## Child Techniques

- [[D3-ACH-application_configuration_hardening|D3-ACH: Application Configuration Hardening]]
- [[D3-CFI-control_flow_integrity|D3-CFI: Control Flow Integrity]]
- [[D3-DCE-dead_code_elimination|D3-DCE: Dead Code Elimination]]
- [[D3-EHPV-exception_handler_pointer_validation|D3-EHPV: Exception Handler Pointer Validation]]
- [[D3-PAN-pointer_authentication|D3-PAN: Pointer Authentication]]
- [[D3-PSEP-process_segment_execution_prevention|D3-PSEP: Process Segment Execution Prevention]]
- [[D3-SAOR-segment_address_offset_randomization|D3-SAOR: Segment Address Offset Randomization]]
- [[D3-SFCV-stack_frame_canary_validation|D3-SFCV: Stack Frame Canary Validation]]

## Knowledge Base Article

## Technique Overview

Exploits may, for example, rely on knowledge of addresses in a process's memory, they may alter memory contents, and they may cause a program to use instructions in a way that they were not intended.  By, for example, including code that dynamically changes the memory address of data or code on each run, introducing logic to validating the memory contents before certain potentially dangerous flows are executed, or monitoring a program for unusual sequence of instructions, this makes it harder for an attacker to craft a working exploit.

