---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-PA"
d3fend_name: "Process Analysis"
d3fend_ontology_id: "d3f:ProcessAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AProcessAnalysis/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

Process Analysis consists of observing a running application process and analyzing it to watch for certain behaviors or conditions which may indicate adversary activity. Analysis can occur inside of the process or through a third-party monitoring application. Examples include monitoring system and privileged calls, monitoring process initiation chains, and memory boundary allocations.

## Workspace

- [[workspaces/defend/techniques/D3-PA-process_analysis-note|Open workspace note]]

![[workspaces/defend/techniques/D3-PA-process_analysis-note]]

## Child Techniques

- [[D3-DQSA-database_query_string_analysis|D3-DQSA: Database Query String Analysis]]
- [[D3-FAPA-file_access_pattern_analysis|D3-FAPA: File Access Pattern Analysis]]
- [[D3-IBCA-indirect_branch_call_analysis|D3-IBCA: Indirect Branch Call Analysis]]
- [[D3-PCSV-process_code_segment_verification|D3-PCSV: Process Code Segment Verification]]
- [[D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]
- [[D3-PSMD-process_self-modification_detection|D3-PSMD: Process Self-Modification Detection]]
- [[D3-SCA-system_call_analysis|D3-SCA: System Call Analysis]]
- [[D3-SEA-script_execution_analysis|D3-SEA: Script Execution Analysis]]
- [[D3-SSC-shadow_stack_comparisons|D3-SSC: Shadow Stack Comparisons]]

