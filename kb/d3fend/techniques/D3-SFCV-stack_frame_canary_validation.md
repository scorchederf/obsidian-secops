---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-SFCV"
d3fend_name: "Stack Frame Canary Validation"
d3fend_ontology_id: "d3f:StackFrameCanaryValidation"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AStackFrameCanaryValidation/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-23 22:40:56"
build_source: "script"
attack_technique_ids:
  - "T1068"
  - "T1203"
  - "T1210"
  - "T1211"
  - "T1212"
---

# D3-SFCV: Stack Frame Canary Validation

Comparing a value stored in a stack frame with a known good value in order to prevent or detect a memory segment overwrite.

## Parent Technique

- [[D3-AH-application_hardening|D3-AH: Application Hardening]]

## Related ATT&CK Techniques

- [[T1068-exploitation_for_privilege_escalation|T1068: Exploitation for Privilege Escalation]]
- [[T1203-exploitation_for_client_execution|T1203: Exploitation for Client Execution]]
- [[T1210-exploitation_of_remote_services|T1210: Exploitation of Remote Services]]
- [[T1211-exploitation_for_defense_evasion|T1211: Exploitation for Defense Evasion]]
- [[T1212-exploitation_for_credential_access|T1212: Exploitation for Credential Access]]

## Knowledge Base Article

## How it works

This defense must be applied at compile-time, or via a patch to the program binary.  Stack Frame Canary Verification inserts instructions at the prologue and epilogue of desired functions.  In the prologue, a canary value, typically with the same size as the register size, is stored in the system of record and on the stack.  Typically, the canary is loaded to where it has a memory address just below that of the saved instruction pointer and base pointer.  In the epilogue, the canary value stored on the stack and, is compared to the canary value in the system of record.  If the values are different, other techniques such as those in Process Eviction might be invoked, such as Process Termination to end the current process, or Executable Blacklisting to blacklist the potentially vulnerable or malfunctioning executable.

Stack Frame Canary Verification is commonly used to detect potential tampering of a saved register value on the stack before it has been restored.  Examples of registers with values commonly saved to the stack include the instruction pointer and the base pointer.

The canary should be stored between where the start of a buffer overrun is likely, and the data to protect, in cases where the buffer size increases it will overwrite the data to be protected.

On most processor architectures, including x86, x64, and ARM, a "push" operation to store data to the stack grows the stack towards a lower memory address.  As in these architectures, saved register values are stored to the stack at a point in time just before space is made for the local function variables, the saved register values have a higher address than that of the local function variables.  Values at increasing indexes of a buffer are written to increasing memory addresses; therefore, an overwrite in the local variable buffer could overwrite saved register values, and a stack canary between these two would be useful in detecting an overwrite.

On some other processor architectures such as the B5000, the stack grows towards increasing memory addresses, and some architectures, such as System Z and RCA1802A, stack direction can be chosen.  If the stack grows towards increasing memory addresses, while this architecture inherently provides more protection against a saved register being overwritten, other data including local function variables might be overwritten.


## Considerations

There are several ways that the protection provided by a canary could be rendered ineffective.

### Performing a malicious action before the canary is checked

If the attacker alters the memory in such a way that it performs a malicious action before the epilogue is called, then this protection will not be effective.  This includes altering the logic of the program by altering the values of local variables stored on the function stack, or by causing an exception and exploiting the exception mechanism such as the SEH (Structured Exception Handling) mechanism on Windows.

### Determining the canary value

Determining the canary value is possible through reading memory either for the code used to check the canary, or from the stored canary value itself in a stack frame.

### Changing the canary value

A vulnerability such as a write-what-where condition that allows one to write data after the canary in the stack, would allow control of the value of the saved instruction pointer without needing to know the canary value.

## Ontology Relationships

- [[D3-AH-application_hardening|D3-AH: Application Hardening]]

## Workspace

- [[kb/notes/d3fend/techniques/d3-sfcv-notes|Open workspace note]]

