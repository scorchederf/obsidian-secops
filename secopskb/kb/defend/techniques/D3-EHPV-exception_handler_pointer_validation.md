---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-EHPV"
d3fend_name: "Exception Handler Pointer Validation"
d3fend_ontology_id: "d3f:ExceptionHandlerPointerValidation"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AExceptionHandlerPointerValidation/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Validates that a referenced exception handler pointer is a valid exception handler.

## Workspace

- [[workspaces/defend/techniques/D3-EHPV-exception_handler_pointer_validation-note|Open workspace note]]

![[workspaces/defend/techniques/D3-EHPV-exception_handler_pointer_validation-note]]

## Parent Technique

- [[D3-AH-application_hardening|D3-AH: Application Hardening]]

## Knowledge Base Article

## How It Works
When a process encounters an exception, it calls an exception handler to deal with the exception.  The method by which this exception handler is determined varies by the operating system.  The exception handler is called, even if it is the default exception handler to terminate the program and display a message that the program stopped working.  In the case that no valid exception handler is found, the program would fail to proceed as normal and could be programmed to terminate.

In Windows, the address of the exception registration record is stored at the very start of the the Thread Information Block; the GS register points to this structure.

The exception registration record contains two pointers: a pointer to the next exception registration record should this handler fail to handle the exception, and a pointer to the handler.

A buffer overflow can overwrite the saved return pointer with an invalid location to execute memory; this often triggers the exception handler chain, which could also be corrupted by the buffer overflow.  Although Process Exception Handler Validation does not make sure that the exception handler pointer or the code at the exception handler was unaltered, or that the exception handler code is secure, this technique does ensure that the pointer is at least an exception handler that could be called by the program.

With Process Exception Handler Validation, before the handler is called, it checks the exception handler against a source of valid exception handlers.  If the requested handler is not in this list, other techniques such as those in Process Eviction might be invoked, such as Process Termination to end the current process, or Executable Blacklisting to blacklist the potentially vulnerable or malfunctioning executable.

### Runtime valid exception handler source generation
The source of valid exception handlers could be generated at runtime, with the risk of the information that is used to determine the validity of exception handlers being compromised.

### Compile-time
The source of valid exception handlers could also be generated at compile time or as a binary patch.  Given the source code, it would be rather straightforward to find the exceptions, as they are pointed in the catch statement of a try-catch clause and the compiler must already generate the code to call exceptions from this.

## Considerations
If the program file can be altered by the attacker, then the security could be bypassed by replacing it with any desired program, without even bypassing SEH.

If the attacker was already able to overwrite the code for a valid exception handler via other functionality in the program, this defense would not prevent arbitrary code execution.
If an exception handler recognized as valid is vulnerable, it would be executed anyway.

SafeSEH might be applied only to some executable files or modules, allowing an attacker to call any piece of code as an exception handler in the unprotected modules.

## Ontology Relationships

- [[D3-AH-application_hardening|D3-AH: Application Hardening]]

