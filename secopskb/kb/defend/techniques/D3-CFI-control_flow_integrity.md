---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-CFI"
d3fend_name: "Control Flow Integrity"
d3fend_ontology_id: "d3f:ControlFlowIntegrity"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AControlFlowIntegrity/"
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

Enforcing legal control flow transfers during application process execution.

## Workspace

- [[notes/defend/techniques/D3-CFI-control_flow_integrity-note|Open workspace note]]

![[notes/defend/techniques/D3-CFI-control_flow_integrity-note]]

## Parent Technique

- [[D3-AH-application_hardening|D3-AH: Application Hardening]]

## Knowledge Base Article

## How it works

Control flow integrity (CFI) restricts the destinations of control flow transfer instructions---particularly indirect function branches such as indirect function calls, jumps, and returns---such that execution can only proceed along paths determined to be valid at compile-time or load-time.

CFI is typically implemented by instrumenting a program during compilation or binary rewriting. A control flow graph is constructed that defines the legitimate targets for each indirect control flow transfer. At runtime, before an indirect branch is taken, a check is performed to ensure that the target address is a member of the allowed target set. If the check fails, a defensive response such as process termination or exception handling is triggered.

Implementations vary in granularity and enforcement mechanism:
- Compiler-based CFI inserts runtime checks that validate indirect call targets against type or signature-based constraints.
- Operating system–assisted CFI maintains a bitmap or table of valid indirect call targets and verifies them at runtime before allowing execution to continue.
- Hardware-assisted CFI enforces control flow integrity using architectural features such as shadow stacks and specific CPU instructions.

By preventing execution from jumping to attacker-controlled or unintended code locations, CFI mitigates a wide range of exploitation techniques, including return-oriented programming (ROP), jump-oriented programming (JOP), and function pointer overwrite attacks.

## Considerations

While control flow integrity significantly raises the bar for control flow hijacking attacks, several considerations affect its effectiveness:
- Granularity trade-offs: coarse-grained CFI allows larger target sets and may permit some unintended control flow paths, while fine-grained CFI offers stronger guarantees at the cost of performance and complexity.
- Performance overhead: runtime checks or hardware enforcement may introduce execution overhead, particularly in applications with frequent indirect branches.
- Compatibility limitations: some legacy code patterns, dynamic code generation, or just-in-time (JIT) compilation workflows may require special handling or reduced CFI enforcement.
- Data-only attacks: CFI does not prevent attacks that manipulate program behavior without altering control flow, such as logic corruption or data-oriented programming.
- Bypass techniques: if an attacker can redirect execution to a valid but unintended target within the allowed control flow graph, exploitation may still be possible.

CFI is most effective when combined with complementary defenses such as stack canaries, memory safety checks, address space layout randomization (ASLR), and hardware-backed memory protections.

## Ontology Relationships

- [[D3-AH-application_hardening|D3-AH: Application Hardening]]

