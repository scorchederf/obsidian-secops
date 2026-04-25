---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-IBCA"
d3fend_name: "Indirect Branch Call Analysis"
d3fend_ontology_id: "d3f:IndirectBranchCallAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AIndirectBranchCallAnalysis/"
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

Analyzing vendor specific branch call recording in order to detect ROP style attacks.

## Workspace

- [[notes/defend/techniques/D3-IBCA-indirect_branch_call_analysis-note|Open workspace note]]

![[notes/defend/techniques/D3-IBCA-indirect_branch_call_analysis-note]]

## Parent Technique

- [[D3-PA-process_analysis|D3-PA: Process Analysis]]

## Knowledge Base Article

## How it works

This technique is used to detect an attacker attempting to exploit and execute code on a target system's call stack using return-oriented programming (ROP). Modern processors that have the ability to maintain a list of the branching calls, e.g., Intel's Last Branch Recording (LBR), can be used to track and analyze indirect branching calls that are indicative of malicious activity.

In order to reduce the number of indirect branch calls to analyze to a manageable set it is assumed that malicious ROP activity will involve the use of system calls.  The technique observes indirect branch calls that are part of paths that lead to system calls, all others are ignored. Branching calls chained together is often referred to as gadgets and gadgets are often used in ROP attacks. Indirect branch calls that involve a transfer from user-space to kernel-space are of interest for this technique.

Identification of potential ROP exploit execution includes:

- Inspecting the LBR when a system function call is made

  - The LBR is configured to return only instruction of interest (ret, indirect jmp, indirect calls)


- Behavior is analyzed for
  - Ret instructions that appear to target areas not preceded by the call sites
  - Sequences of small code fragments that appear to be chained through the indirect branching calls (gadgets)


- Of interest are returns that appear to not render control back after calls
  - Typical ret-call are paired
  - gadgets will appear to have ret followed by instruction of next instruction of the following gadget


## Considerations

* May be operating system dependent since specific system calls are used to scope branching behavoir
* Processors need to support access to a Last Branch Recording list feature
* The size of the LBR stack can limit the expected size of the analyzed execution stack
* If processor does not support LBR then overhead costs for the analysis can be significant

## Ontology Relationships

- [[D3-PA-process_analysis|D3-PA: Process Analysis]]

