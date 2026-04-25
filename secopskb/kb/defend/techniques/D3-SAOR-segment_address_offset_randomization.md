---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-SAOR"
d3fend_name: "Segment Address Offset Randomization"
d3fend_ontology_id: "d3f:SegmentAddressOffsetRandomization"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ASegmentAddressOffsetRandomization/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-25 14:47:22"
build_source: "script"
attack_technique_ids:
  - "T1033"
  - "T1055"
  - "T1055.012"
  - "T1056"
  - "T1056.004"
  - "T1068"
  - "T1189"
  - "T1190"
  - "T1203"
  - "T1210"
  - "T1211"
  - "T1212"
  - "T1218"
  - "T1218.013"
  - "T1620"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

Randomizing the base (start) address of one or more segments of memory during the initialization of a process.

## Workspace

- [[notes/defend/techniques/D3-SAOR-segment_address_offset_randomization-note|Open workspace note]]

![[notes/defend/techniques/D3-SAOR-segment_address_offset_randomization-note]]

## Parent Technique

- [[D3-AH-application_hardening|D3-AH: Application Hardening]]

## Related ATT&CK Techniques

- [[T1033-system_owner_user_discovery|T1033: System Owner/User Discovery]]
- [[T1055-process_injection|T1055: Process Injection]]
- [[T1055-process_injection#^t1055012-process-hollowing|T1055.012: Process Hollowing]]
- [[T1056-input_capture|T1056: Input Capture]]
- [[T1056-input_capture#^t1056004-credential-api-hooking|T1056.004: Credential API Hooking]]
- [[T1068-exploitation_for_privilege_escalation|T1068: Exploitation for Privilege Escalation]]
- [[T1189-drive-by_compromise|T1189: Drive-by Compromise]]
- [[T1190-exploit_public-facing_application|T1190: Exploit Public-Facing Application]]
- [[T1203-exploitation_for_client_execution|T1203: Exploitation for Client Execution]]
- [[T1210-exploitation_of_remote_services|T1210: Exploitation of Remote Services]]
- [[T1211-exploitation_for_defense_evasion|T1211: Exploitation for Defense Evasion]]
- [[T1212-exploitation_for_credential_access|T1212: Exploitation for Credential Access]]
- [[T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]
- [[T1218-system_binary_proxy_execution#^t1218013-mavinject|T1218.013: Mavinject]]
- [[T1620-reflective_code_loading|T1620: Reflective Code Loading]]

## Knowledge Base Article

## How it works

Many application exploits rely on an attacker specifying a location in memory, which points to data or code used by the attacker.  If the addresses are changed each time the program is run, then it becomes more difficult for the attacker to determine the location that will contain the code they wish to run.

Imported modules may be similarly realigned if their default memory addresses conflict with other modules, in a process known as "rebasing."  Just as not all code is built for participation in ASLR, not all modules can be rebased; instead, modules must indicate whether they implement support for rebasing.  Such information to relocate the executable is typically stored in the ".reloc" segment -- each of the addresses pointed to in this segment has its address increased by the amount of the offset.
(An alternative method for relocation would be to add an amount to a global variable each time -- leading to less overhead in the module load, but more for each access.  Still another implementation could instead contain code to deference each changeable memory location on the fly, so that each of the references do not need to be updated.


## Considerations

As the offset for each segment is constant, it is possible to guess at the value of the address given the address of another variable.  Alternatively, memory pointers may be kept around, which contain the address of another variable.
Another bypass technique is known as an "egg hunt," whereby the attacker searches for a rather unique piece of the data or code in memory to determine its likely address.

The program needs to store these addresses for the functions somewhere.  In Linux, the PLT contains a "trampoline" to these addresses.  If an attacker desires to jump to the start of an existing function, they can jump directly to the trampoline anyway, and may have the opportunity to provide their own stack frame to the function with a write to the stack. If they overwrite a saved stack pointer which is loaded back into memory, or execute a function, that changes the address of a stack pointer.

If an attacker wants to inject some data into the program, for example as a parameter to a known function that is not under ASLR or a pointer to a trampoline function in the PLT, then they can repeat the data until they exceed the range of ASLR coverage, which on 32-bit systems is accomplishable in a few seconds with a heap spray.  Microsoft's EMET and Windows 10 Exploit Guard can pre-allocate particular addresses that are commonly used in heap sprays.  However, in many products, there does not seem to be nearly a complete coverage of such addresses, which only need to be executable and in the range of the heap; 0x0c0c0c0c is such an address that is commonly used for the x86 processor architecture, as when executed it only performs a numeric operation to a register four times.

## Ontology Relationships

- [[D3-AH-application_hardening|D3-AH: Application Hardening]]

