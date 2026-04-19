---
id: T1055
name: Process Injection
created: 2017-05-31 21:30:47.843000+00:00
modified: 2025-10-24 17:48:43.053000+00:00
type: attack-pattern
x_mitre_version: 1.4
x_mitre_domains: enterprise-attack
---

## Tactic

- [[defense_evasion|Defense Evasion]]

Adversaries may inject code into processes in order to evade process-based defenses as well as possibly elevate privileges. Process injection is a method of executing arbitrary code in the address space of a separate live process. Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via process injection may also evade detection from security products since the execution is masked under a legitimate process. 

There are many different ways to inject code into a process, many of which abuse legitimate functionalities. These implementations exist for every major OS but are typically platform specific. 

More sophisticated samples may perform multiple process injections to segment modules and further evade detection, utilizing named pipes or other inter-process communication (IPC) mechanisms as a communication channel. 

## Properties

- id: T1055
- name: Process Injection
- created: 2017-05-31 21:30:47.843000+00:00
- modified: 2025-10-24 17:48:43.053000+00:00
- type: attack-pattern
- x_mitre_version: 1.4
- x_mitre_domains: enterprise-attack

## Subtechniques

### T1055.001: Dynamic-link Library Injection

^t1055001-dynamic-link-library-injection

**Parent Technique**
- [[T1055-process_injection|T1055: Process Injection]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may inject dynamic-link libraries (DLLs) into processes in order to evade process-based defenses as well as possibly elevate privileges. DLL injection is a method of executing arbitrary code in the address space of a separate live process.  

DLL injection is commonly performed by writing the path to a DLL in the virtual address space of the target process before loading the DLL by invoking a new thread. The write can be performed with native Windows API calls such as <code>VirtualAllocEx</code> and <code>WriteProcessMemory</code>, then invoked with <code>CreateRemoteThread</code> (which calls the <code>LoadLibrary</code> API responsible for loading the DLL). (Citation: Elastic Process Injection July 2017) 

Variations of this method such as reflective DLL injection (writing a self-mapping DLL into a process) and memory module (map DLL when writing into process) overcome the address relocation issue as well as the additional APIs to invoke execution (since these methods load and execute the files in memory by manually preforming the function of <code>LoadLibrary</code>).(Citation: Elastic HuntingNMemory June 2017)(Citation: Elastic Process Injection July 2017) 

Another variation of this method, often referred to as Module Stomping/Overloading or DLL Hollowing, may be leveraged to conceal injected code within a process. This method involves loading a legitimate DLL into a remote process then manually overwriting the module's <code>AddressOfEntryPoint</code> before starting a new thread in the target process.(Citation: Module Stomping for Shellcode Injection) This variation allows attackers to hide malicious injected code by potentially backing its execution with a legitimate DLL file on disk.(Citation: Hiding Malicious Code with Module Stomping) 

Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via DLL injection may also evade detection from security products since the execution is masked under a legitimate process. 

#### Properties

- id: T1055.001
- name: Dynamic-link Library Injection
- created: 2020-01-14 01:26:08.145000+00:00
- modified: 2025-10-24 17:49:36.680000+00:00
- type: attack-pattern
- x_mitre_version: 1.4
- x_mitre_domains: enterprise-attack

### T1055.002: Portable Executable Injection

^t1055002-portable-executable-injection

**Parent Technique**
- [[T1055-process_injection|T1055: Process Injection]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may inject portable executables (PE) into processes in order to evade process-based defenses as well as possibly elevate privileges. PE injection is a method of executing arbitrary code in the address space of a separate live process. 

PE injection is commonly performed by copying code (perhaps without a file on disk) into the virtual address space of the target process before invoking it via a new thread. The write can be performed with native Windows API calls such as <code>VirtualAllocEx</code> and <code>WriteProcessMemory</code>, then invoked with <code>CreateRemoteThread</code> or additional code (ex: shellcode). The displacement of the injected code does introduce the additional requirement for functionality to remap memory references. (Citation: Elastic Process Injection July 2017) 

Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via PE injection may also evade detection from security products since the execution is masked under a legitimate process. 

#### Properties

- id: T1055.002
- name: Portable Executable Injection
- created: 2020-01-14 01:27:31.344000+00:00
- modified: 2025-10-24 17:49:01.839000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1055.003: Thread Execution Hijacking

^t1055003-thread-execution-hijacking

**Parent Technique**
- [[T1055-process_injection|T1055: Process Injection]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may inject malicious code into hijacked processes in order to evade process-based defenses as well as possibly elevate privileges. Thread Execution Hijacking is a method of executing arbitrary code in the address space of a separate live process. 

Thread Execution Hijacking is commonly performed by suspending an existing process then unmapping/hollowing its memory, which can then be replaced with malicious code or the path to a DLL. A handle to an existing victim process is first created with native Windows API calls such as <code>OpenThread</code>. At this point the process can be suspended then written to, realigned to the injected code, and resumed via <code>SuspendThread </code>, <code>VirtualAllocEx</code>, <code>WriteProcessMemory</code>, <code>SetThreadContext</code>, then <code>ResumeThread</code> respectively.(Citation: Elastic Process Injection July 2017)

This is very similar to [Process Hollowing](https://attack.mitre.org/techniques/T1055/012) but targets an existing process rather than creating a process in a suspended state.  

Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via Thread Execution Hijacking may also evade detection from security products since the execution is masked under a legitimate process. 

#### Properties

- id: T1055.003
- name: Thread Execution Hijacking
- created: 2020-01-14 01:28:32.166000+00:00
- modified: 2025-10-24 17:48:42.433000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1055.004: Asynchronous Procedure Call

^t1055004-asynchronous-procedure-call

**Parent Technique**
- [[T1055-process_injection|T1055: Process Injection]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may inject malicious code into processes via the asynchronous procedure call (APC) queue in order to evade process-based defenses as well as possibly elevate privileges. APC injection is a method of executing arbitrary code in the address space of a separate live process. 

APC injection is commonly performed by attaching malicious code to the APC Queue (Citation: Microsoft APC) of a process's thread. Queued APC functions are executed when the thread enters an alterable state.(Citation: Microsoft APC) A handle to an existing victim process is first created with native Windows API calls such as <code>OpenThread</code>. At this point <code>QueueUserAPC</code> can be used to invoke a function (such as <code>LoadLibrayA</code> pointing to a malicious DLL). 

A variation of APC injection, dubbed "Early Bird injection", involves creating a suspended process in which malicious code can be written and executed before the process' entry point (and potentially subsequent anti-malware hooks) via an APC. (Citation: CyberBit Early Bird Apr 2018) AtomBombing (Citation: ENSIL AtomBombing Oct 2016) is another variation that utilizes APCs to invoke malicious code previously written to the global atom table.(Citation: Microsoft Atom Table)

Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via APC injection may also evade detection from security products since the execution is masked under a legitimate process. 

#### Properties

- id: T1055.004
- name: Asynchronous Procedure Call
- created: 2020-01-14 01:29:43.786000+00:00
- modified: 2025-10-24 17:49:00.298000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1055.005: Thread Local Storage

^t1055005-thread-local-storage

**Parent Technique**
- [[T1055-process_injection|T1055: Process Injection]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may inject malicious code into processes via thread local storage (TLS) callbacks in order to evade process-based defenses as well as possibly elevate privileges. TLS callback injection is a method of executing arbitrary code in the address space of a separate live process. 

TLS callback injection involves manipulating pointers inside a portable executable (PE) to redirect a process to malicious code before reaching the code's legitimate entry point. TLS callbacks are normally used by the OS to setup and/or cleanup data used by threads. Manipulating TLS callbacks may be performed by allocating and writing to specific offsets within a process’ memory space using other [Process Injection](https://attack.mitre.org/techniques/T1055) techniques such as [Process Hollowing](https://attack.mitre.org/techniques/T1055/012).(Citation: FireEye TLS Nov 2017)

Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via TLS callback injection may also evade detection from security products since the execution is masked under a legitimate process. 

#### Properties

- id: T1055.005
- name: Thread Local Storage
- created: 2020-01-14 01:30:41.092000+00:00
- modified: 2025-10-24 17:49:32.111000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1055.008: Ptrace System Calls

^t1055008-ptrace-system-calls

**Parent Technique**
- [[T1055-process_injection|T1055: Process Injection]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may inject malicious code into processes via ptrace (process trace) system calls in order to evade process-based defenses as well as possibly elevate privileges. Ptrace system call injection is a method of executing arbitrary code in the address space of a separate live process. 

Ptrace system call injection involves attaching to and modifying a running process. The ptrace system call enables a debugging process to observe and control another process (and each individual thread), including changing memory and register values.(Citation: PTRACE man) Ptrace system call injection is commonly performed by writing arbitrary code into a running process (ex: <code>malloc</code>) then invoking that memory with <code>PTRACE_SETREGS</code> to set the register containing the next instruction to execute. Ptrace system call injection can also be done with <code>PTRACE_POKETEXT</code>/<code>PTRACE_POKEDATA</code>, which copy data to a specific address in the target processes’ memory (ex: the current address of the next instruction). (Citation: PTRACE man)(Citation: Medium Ptrace JUL 2018) 

Ptrace system call injection may not be possible targeting processes that are non-child processes and/or have higher-privileges.(Citation: BH Linux Inject) 

Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via ptrace system call injection may also evade detection from security products since the execution is masked under a legitimate process. 

#### Properties

- id: T1055.008
- name: Ptrace System Calls
- created: 2020-01-14 01:33:19.065000+00:00
- modified: 2025-10-24 17:49:33.344000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1055.009: Proc Memory

^t1055009-proc-memory

**Parent Technique**
- [[T1055-process_injection|T1055: Process Injection]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may inject malicious code into processes via the /proc filesystem in order to evade process-based defenses as well as possibly elevate privileges. Proc memory injection is a method of executing arbitrary code in the address space of a separate live process. 

Proc memory injection involves enumerating the memory of a process via the /proc filesystem (<code>/proc/[pid]</code>) then crafting a return-oriented programming (ROP) payload with available gadgets/instructions. Each running process has its own directory, which includes memory mappings. Proc memory injection is commonly performed by overwriting the target processes’ stack using memory mappings provided by the /proc filesystem. This information can be used to enumerate offsets (including the stack) and gadgets (or instructions within the program that can be used to build a malicious payload) otherwise hidden by process memory protections such as address space layout randomization (ASLR). Once enumerated, the target processes’ memory map within <code>/proc/[pid]/maps</code> can be overwritten using dd.(Citation: Uninformed Needle)(Citation: GDS Linux Injection)(Citation: DD Man) 

Other techniques such as [Dynamic Linker Hijacking](https://attack.mitre.org/techniques/T1574/006) may be used to populate a target process with more available gadgets. Similar to [Process Hollowing](https://attack.mitre.org/techniques/T1055/012), proc memory injection may target child processes (such as a backgrounded copy of sleep).(Citation: GDS Linux Injection) 

Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via proc memory injection may also evade detection from security products since the execution is masked under a legitimate process. 

#### Properties

- id: T1055.009
- name: Proc Memory
- created: 2020-01-14 01:34:10.588000+00:00
- modified: 2025-10-24 17:49:25.806000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

### T1055.011: Extra Window Memory Injection

^t1055011-extra-window-memory-injection

**Parent Technique**
- [[T1055-process_injection|T1055: Process Injection]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly elevate privileges. EWM injection is a method of executing arbitrary code in the address space of a separate live process. 

Before creating a window, graphical Windows-based processes must prescribe to or register a windows class, which stipulate appearance and behavior (via windows procedures, which are functions that handle input/output of data).(Citation: Microsoft Window Classes) Registration of new windows classes can include a request for up to 40 bytes of EWM to be appended to the allocated memory of each instance of that class. This EWM is intended to store data specific to that window and has specific application programming interface (API) functions to set and get its value. (Citation: Microsoft GetWindowLong function) (Citation: Microsoft SetWindowLong function)

Although small, the EWM is large enough to store a 32-bit pointer and is often used to point to a windows procedure. Malware may possibly utilize this memory location in part of an attack chain that includes writing code to shared sections of the process’s memory, placing a pointer to the code in EWM, then invoking execution by returning execution control to the address in the process’s EWM.

Execution granted through EWM injection may allow access to both the target process's memory and possibly elevated privileges. Writing payloads to shared sections also avoids the use of highly monitored API calls such as <code>WriteProcessMemory</code> and <code>CreateRemoteThread</code>.(Citation: Elastic Process Injection July 2017) More sophisticated malware samples may also potentially bypass protection mechanisms such as data execution prevention (DEP) by triggering a combination of windows procedures and other system functions that will rewrite the malicious payload inside an executable portion of the target process.  (Citation: MalwareTech Power Loader Aug 2013) (Citation: WeLiveSecurity Gapz and Redyms Mar 2013)

Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via EWM injection may also evade detection from security products since the execution is masked under a legitimate process. 

#### Properties

- id: T1055.011
- name: Extra Window Memory Injection
- created: 2020-01-14 17:18:32.126000+00:00
- modified: 2025-10-24 17:48:19.059000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

### T1055.012: Process Hollowing

^t1055012-process-hollowing

**Parent Technique**
- [[T1055-process_injection|T1055: Process Injection]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may inject malicious code into suspended and hollowed processes in order to evade process-based defenses. Process hollowing is a method of executing arbitrary code in the address space of a separate live process.  

Process hollowing is commonly performed by creating a process in a suspended state then unmapping/hollowing its memory, which can then be replaced with malicious code. A victim process can be created with native Windows API calls such as <code>CreateProcess</code>, which includes a flag to suspend the processes primary thread. At this point the process can be unmapped using APIs calls such as <code>ZwUnmapViewOfSection</code> or <code>NtUnmapViewOfSection</code>  before being written to, realigned to the injected code, and resumed via <code>VirtualAllocEx</code>, <code>WriteProcessMemory</code>, <code>SetThreadContext</code>, then <code>ResumeThread</code> respectively.(Citation: Leitch Hollowing)(Citation: Elastic Process Injection July 2017)

This is very similar to [Thread Local Storage](https://attack.mitre.org/techniques/T1055/005) but creates a new process rather than targeting an existing process. This behavior will likely not result in elevated privileges since the injected process was spawned from (and thus inherits the security context) of the injecting process. However, execution via process hollowing may also evade detection from security products since the execution is masked under a legitimate process. 

#### Properties

- id: T1055.012
- name: Process Hollowing
- created: 2020-01-14 17:21:54.470000+00:00
- modified: 2025-10-24 17:49:14.559000+00:00
- type: attack-pattern
- x_mitre_version: 1.4
- x_mitre_domains: enterprise-attack

### T1055.013: Process Doppelgänging

^t1055013-process-doppelgänging

**Parent Technique**
- [[T1055-process_injection|T1055: Process Injection]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may inject malicious code into process via process doppelgänging in order to evade process-based defenses as well as possibly elevate privileges. Process doppelgänging is a method of executing arbitrary code in the address space of a separate live process. 

Windows Transactional NTFS (TxF) was introduced in Vista as a method to perform safe file operations. (Citation: Microsoft TxF) To ensure data integrity, TxF enables only one transacted handle to write to a file at a given time. Until the write handle transaction is terminated, all other handles are isolated from the writer and may only read the committed version of the file that existed at the time the handle was opened. (Citation: Microsoft Basic TxF Concepts) To avoid corruption, TxF performs an automatic rollback if the system or application fails during a write transaction. (Citation: Microsoft Where to use TxF)

Although deprecated, the TxF application programming interface (API) is still enabled as of Windows 10. (Citation: BlackHat Process Doppelgänging Dec 2017)

Adversaries may abuse TxF to a perform a file-less variation of [Process Injection](https://attack.mitre.org/techniques/T1055). Similar to [Process Hollowing](https://attack.mitre.org/techniques/T1055/012), process doppelgänging involves replacing the memory of a legitimate process, enabling the veiled execution of malicious code that may evade defenses and detection. Process doppelgänging's use of TxF also avoids the use of highly-monitored API functions such as <code>NtUnmapViewOfSection</code>, <code>VirtualProtectEx</code>, and <code>SetThreadContext</code>. (Citation: BlackHat Process Doppelgänging Dec 2017)

Process Doppelgänging is implemented in 4 steps (Citation: BlackHat Process Doppelgänging Dec 2017):

* Transact – Create a TxF transaction using a legitimate executable then overwrite the file with malicious code. These changes will be isolated and only visible within the context of the transaction.
* Load – Create a shared section of memory and load the malicious executable.
* Rollback – Undo changes to original executable, effectively removing malicious code from the file system.
* Animate – Create a process from the tainted section of memory and initiate execution.

This behavior will likely not result in elevated privileges since the injected process was spawned from (and thus inherits the security context) of the injecting process. However, execution via process doppelgänging may evade detection from security products since the execution is masked under a legitimate process. 

#### Properties

- id: T1055.013
- name: Process Doppelgänging
- created: 2020-01-14 17:19:50.978000+00:00
- modified: 2025-10-24 17:48:56.422000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

### T1055.014: VDSO Hijacking

^t1055014-vdso-hijacking

**Parent Technique**
- [[T1055-process_injection|T1055: Process Injection]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may inject malicious code into processes via VDSO hijacking in order to evade process-based defenses as well as possibly elevate privileges. Virtual dynamic shared object (vdso) hijacking is a method of executing arbitrary code in the address space of a separate live process. 

VDSO hijacking involves redirecting calls to dynamically linked shared libraries. Memory protections may prevent writing executable code to a process via [Ptrace System Calls](https://attack.mitre.org/techniques/T1055/008). However, an adversary may hijack the syscall interface code stubs mapped into a process from the vdso shared object to execute syscalls to open and map a malicious shared object. This code can then be invoked by redirecting the execution flow of the process via patched memory address references stored in a process' global offset table (which store absolute addresses of mapped library functions).(Citation: ELF Injection May 2009)(Citation: Backtrace VDSO)(Citation: VDSO Aug 2005)(Citation: Syscall 2014)

Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via VDSO hijacking may also evade detection from security products since the execution is masked under a legitimate process.  

#### Properties

- id: T1055.014
- name: VDSO Hijacking
- created: 2020-01-14 01:35:00.781000+00:00
- modified: 2025-10-24 17:49:08.040000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1055.015: ListPlanting

^t1055015-listplanting

**Parent Technique**
- [[T1055-process_injection|T1055: Process Injection]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may abuse list-view controls to inject malicious code into hijacked processes in order to evade process-based defenses as well as possibly elevate privileges. ListPlanting is a method of executing arbitrary code in the address space of a separate live process.(Citation: Hexacorn Listplanting) Code executed via ListPlanting may also evade detection from security products since the execution is masked under a legitimate process.

List-view controls are user interface windows used to display collections of items.(Citation: Microsoft List View Controls) Information about an application's list-view settings are stored within the process' memory in a <code>SysListView32</code> control.

ListPlanting (a form of message-passing "shatter attack") may be performed by copying code into the virtual address space of a process that uses a list-view control then using that code as a custom callback for sorting the listed items.(Citation: Modexp Windows Process Injection) Adversaries must first copy code into the target process’ memory space, which can be performed various ways including by directly obtaining a handle to the <code>SysListView32</code> child of the victim process window (via Windows API calls such as <code>FindWindow</code> and/or <code>EnumWindows</code>) or other [Process Injection](https://attack.mitre.org/techniques/T1055) methods.

Some variations of ListPlanting may allocate memory in the target process but then use window messages to copy the payload, to avoid the use of the highly monitored <code>WriteProcessMemory</code> function. For example, an adversary can use the <code>PostMessage</code> and/or <code>SendMessage</code> API functions to send <code>LVM_SETITEMPOSITION</code> and <code>LVM_GETITEMPOSITION</code> messages, effectively copying a payload 2 bytes at a time to the allocated memory.(Citation: ESET InvisiMole June 2020) 

Finally, the payload is triggered by sending the <code>LVM_SORTITEMS</code> message to the <code>SysListView32</code> child of the process window, with the payload within the newly allocated buffer passed and executed as the <code>ListView_SortItems</code> callback.

#### Properties

- id: T1055.015
- name: ListPlanting
- created: 2021-11-22 15:02:15.190000+00:00
- modified: 2025-10-24 17:49:33.701000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1040-behavior_prevention_on_endpoint|M1040: Behavior Prevention on Endpoint]]

## Platforms

- Linux
- macOS
- Windows

## Tools

- [[S0040-htran|S0040: HTRAN]]
- [[S0332-remcos|S0332: Remcos]]
- [[S0363-empire|S0363: Empire]]
- [[S0378-poshc2|S0378: PoshC2]]
- [[S0581-ironnetinjector|S0581: IronNetInjector]]
- [[S0633-sliver|S0633: Sliver]]
- [[S0692-silenttrinity|S0692: SILENTTRINITY]]
- [[S0695-donut|S0695: Donut]]
- [[S1050-pcshare|S1050: PcShare]]

