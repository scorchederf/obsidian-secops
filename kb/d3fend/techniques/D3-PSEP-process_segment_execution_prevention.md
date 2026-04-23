---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-PSEP"
d3fend_name: "Process Segment Execution Prevention"
d3fend_ontology_id: "d3f:ProcessSegmentExecutionPrevention"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AProcessSegmentExecutionPrevention/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-23 22:40:56"
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

# D3-PSEP: Process Segment Execution Prevention

Preventing execution of any address in a memory region other than the code segment.

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

During execution of a process, the instruction pointer register should only point to addresses in a code segment (also called the .text segment), as this is the sole segment which should contain program code.

When this technique detects an attempt to execute something that has been designated as non-executable, other techniques such as those in **Process Eviction** might be invoked, such as **Process Termination** to end the current process, or **Executable Blacklisting** to blacklist the potentially vulnerable or malfunctioning executable.

### Software-based implementations
The software-based implementation in Windows XP SP2 might not check that every time the instruction pointer is changed, and does not check on each jump or return.  Before calling an exception handler, Windows XP SP2 software-enforced DEP checks whether the exception handler is located in a memory region marked as executable.  If the program was also built with SafeSEH, this implementation also checks before changing control to the exception handler whether it is a registered exception handler in the program's file on disk.

### Hardware-based implementations
The NX (No Execute) or XD (Execute Disable) bit on the processor specifies whether a certain part of memory is executable.  Early implementations set this bit by the memory segment, while modern implementations which are built on the flat memory model often store this bit in each entry of the page table, to control execution by the page.


## Considerations

Non-hardware process data segment execution prevention is more susceptible to being able to be turned off for a page of memory.

Different implementations of this defense have been in place since the 1980s, but implementation stalled when larger 16-bit programs began stuffing code in the segments usually reserved for data. Many modern programs follow the best practice of separation of code and data, are able to run under this defense.

ROP or ret2libc/return-to-function attacks could bypass this defense, as although they may pass attacker-controlled data or stack frames to a function, they abuse functions that are legitimately located in the .text segment (code segment) of the program.  For those, more advanced defenses such as a table of valid jump addresses, function call analysis, or return depth analysis could be used.

## Ontology Relationships

- [[D3-AH-application_hardening|D3-AH: Application Hardening]]

## Workspace

- [[kb/notes/d3fend/techniques/d3-psep-notes|Open workspace note]]

