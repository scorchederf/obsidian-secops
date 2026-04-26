---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-BSE"
d3fend_name: "Byte Sequence Emulation"
d3fend_ontology_id: "d3f:ByteSequenceEmulation"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AByteSequenceEmulation/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Analyzing sequences of bytes and determining if they likely represent malicious shellcode.

## Workspace

- [[workspaces/defend/techniques/D3-BSE-byte_sequence_emulation-note|Open workspace note]]

![[workspaces/defend/techniques/D3-BSE-byte_sequence_emulation-note]]

## Parent Technique

- [[D3-NTA-network_traffic_analysis|D3-NTA: Network Traffic Analysis]]

## Knowledge Base Article

## How it works

Bytes are analyzed as if they are machine code instructions, and such instructions that are a common component of known shellcode are noted, such as stack pivots, reads from a Memory Address Table, and system calls for functions that disable protections or execute code.  For example, the x86 instruction `b0 0b: mov $11, %ax`, with no further alterations to the `%ax` register, followed by `cd 80: syscall` executes the system call `execve()` in the Linux kernel, which replaces the current process with another one specified -- this is a common action in shellcode, so this sequence would be flagged.

This technique detects shellcode despite whether or not it would cause a buffer overflow in the target binary.

If the sequence of bytes contains a sequence similar to that used in malicious shellcode, the entire byte sequence is flagged and a follow-on technique may be invoked.

## Considerations

### False Negatives
If the shellcode instructions are far apart, simple implementations might not detect the shellcode.

Due to the nature of assembly instructions not having a defined start or end, implementations which do not process all start sequences (for example, when they a find byte sequence of interest, continue scanning forwards from the end of it) might not detect the shellcode.

This technique might not detect more complex or obfuscated instructions.  For that purpose, Dynamic Analysis or Emulated File Analysis could assist by analyzing the actual instruction function.

This technique may not detect self-modifying code.  To make it harder for a process to modify itself, Process Segment Execution Prevention should be used, while noting its considerations.

This technique might not detect malicious shellcode which reuses instructions in the target binary for malicious effect, as memory references in the presumed assembly code are not dereferenced.  Dynamic Analysis and Emulated File Analysis, when set up properly to fork from the running target binary, might detect this.  Process Segment Execution Prevention combined with Segment Address Offset Randomization frequently makes introduction of shellcode through overwriting a saved return pointer more difficult.  Call stack depth analysis might detect excessive reuse of instructions in the target binary.  Shadow Stack Frames might detect that a stack frame's return address has changed and Stack Frame Canary Verification might detect that the stack frame's return address was overwritten.  Other heuristic methods might detect jump-oriented programming shellcode.

With inserting code directly, that it is not a buffer overflow, and just some place where code is executed either to a file or a write-what-where, the buffer overflow mitigations do not help.  Behavioral analysis could detect this, or proper access control could mitigate this.

### False Positives

Byte sequences containing code that is never used as machine code are still analyzed and flagged for anomalies, and [eventually](http://mathforum.org/library/drmath/view/55871.html), it is likely that an attack sequence will arise from the sheer volume of bytes transmitted.

## Ontology Relationships

- [[D3-NTA-network_traffic_analysis|D3-NTA: Network Traffic Analysis]]

