---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-PCSV"
d3fend_name: "Process Code Segment Verification"
d3fend_ontology_id: "d3f:ProcessCodeSegmentVerification"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AProcessCodeSegmentVerification/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1055"
  - "T1055.012"
  - "T1056"
  - "T1056.004"
  - "T1068"
  - "T1203"
  - "T1210"
  - "T1211"
  - "T1212"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Comparing the "text" or "code" memory segments to a source of truth.

## Workspace

- [[workspaces/defend/techniques/D3-PCSV-process_code_segment_verification-note|Open workspace note]]

![[workspaces/defend/techniques/D3-PCSV-process_code_segment_verification-note]]

## Parent Technique

- [[D3-PA-process_analysis|D3-PA: Process Analysis]]

## Related ATT&CK Techniques

- [[T1055-process_injection|T1055: Process Injection]]
- [[T1055-process_injection#^t1055012-process-hollowing|T1055.012: Process Hollowing]]
- [[T1056-input_capture|T1056: Input Capture]]
- [[T1056-input_capture#^t1056004-credential-api-hooking|T1056.004: Credential API Hooking]]
- [[T1068-exploitation_for_privilege_escalation|T1068: Exploitation for Privilege Escalation]]
- [[T1203-exploitation_for_client_execution|T1203: Exploitation for Client Execution]]
- [[T1210-exploitation_of_remote_services|T1210: Exploitation of Remote Services]]
- [[T1211-exploitation_for_defense_evasion|T1211: Exploitation for Defense Evasion]]
- [[T1212-exploitation_for_credential_access|T1212: Exploitation for Credential Access]]

## Knowledge Base Article

## How it works
A process code segment is an executable portion of computer memory allocated to a particular process. Process Code Segment Verification implements verification to compare a process code segment to some expected value.

### Verification logic
Verification can occur during application startup, or continuously during execution. The logic which verifies the process code may be separate in a third-party process, embedded in the application itself at compile time, or dynamically linked at runtime.

### System of record
Examples of systems of record:

 * On-disk application binary files or checksums
 * Remotely stored binary data or checksums
 * Embedded binary data or checksums

### Post Verification Actions
If the verification function determines a process code segment may have been altered, a capability may invoke Eviction techniques  as **Process Termination** to end the current process, or **Executable Blacklisting** to prevent the executable from launching in the future.

## Considerations

### False positives

False positives commonly occur in the case that the layout of code in the process segment is legitimately modified:

*  Operating system features or third-party security software may modify the layout of process code, for example in the defensive technique **Segment Address Offset Randomization**, or in the case that a module is rebased.  In both of these cases, the alteration occurs before the code is fully loaded into memory, and it would be possible to avoid the false positive by securely feeding this constant offset and any relocation data into the verification logic.

* Process code segments may be written to modify themselves or other process code segments; however, this goes against widely-accepted current practices in software development.

### False negatives

False negatives can occur via alteration of the verification logic or source of truth, or insufficient verification logic.

* Verification techniques which are executed only locally may be defeated by altering the local verification logic.

* Verification that is run only on a recurring basis could be evaded if the malicious alteration is completed before verification is run.

* Verification that requests an operation to be performed on a subset of the code segment could be evaded by performing that operation on a copy of the relevant bytes of the code segment.

* Verification based on a system of record that can be altered may fail if that system of record is modifiable by a malicious user.

## Ontology Relationships

- [[D3-PA-process_analysis|D3-PA: Process Analysis]]

