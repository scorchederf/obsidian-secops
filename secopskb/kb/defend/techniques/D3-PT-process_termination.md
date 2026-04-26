---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-PT"
d3fend_name: "Process Termination"
d3fend_ontology_id: "d3f:ProcessTermination"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AProcessTermination/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1003"
  - "T1003.001"
  - "T1003.002"
  - "T1003.004"
  - "T1033"
  - "T1053"
  - "T1053.002"
  - "T1053.003"
  - "T1053.005"
  - "T1053.006"
  - "T1053.007"
  - "T1212"
  - "T1505"
  - "T1505.002"
  - "T1505.003"
  - "T1546"
  - "T1546.007"
  - "T1550"
  - "T1550.001"
  - "T1550.002"
  - "T1550.003"
  - "T1550.004"
  - "T1556"
  - "T1556.001"
  - "T1556.002"
  - "T1556.003"
  - "T1556.004"
  - "T1556.005"
  - "T1556.006"
  - "T1556.007"
  - "T1556.008"
  - "T1556.009"
  - "T1562"
  - "T1562.001"
  - "T1621"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Terminating a running application process on a computer system.

## Workspace

- [[workspaces/defend/techniques/D3-PT-process_termination-note|Open workspace note]]

![[workspaces/defend/techniques/D3-PT-process_termination-note]]

## Parent Technique

- [[D3-PE-process_eviction|D3-PE: Process Eviction]]

## Related ATT&CK Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
- [[T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]
- [[T1003-os_credential_dumping#^t1003002-security-account-manager|T1003.002: Security Account Manager]]
- [[T1003-os_credential_dumping#^t1003004-lsa-secrets|T1003.004: LSA Secrets]]
- [[T1033-system_owner_user_discovery|T1033: System Owner/User Discovery]]
- [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]]
- [[T1053-scheduled_task_job#^t1053002-at|T1053.002: At]]
- [[T1053-scheduled_task_job#^t1053003-cron|T1053.003: Cron]]
- [[T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]
- [[T1053-scheduled_task_job#^t1053006-systemd-timers|T1053.006: Systemd Timers]]
- [[T1053-scheduled_task_job#^t1053007-container-orchestration-job|T1053.007: Container Orchestration Job]]
- [[T1212-exploitation_for_credential_access|T1212: Exploitation for Credential Access]]
- [[T1505-server_software_component|T1505: Server Software Component]]
- [[T1505-server_software_component#^t1505002-transport-agent|T1505.002: Transport Agent]]
- [[T1505-server_software_component#^t1505003-web-shell|T1505.003: Web Shell]]
- [[T1546-event_triggered_execution|T1546: Event Triggered Execution]]
- [[T1546-event_triggered_execution#^t1546007-netsh-helper-dll|T1546.007: Netsh Helper DLL]]
- [[T1550-use_alternate_authentication_material|T1550: Use Alternate Authentication Material]]
- [[T1550-use_alternate_authentication_material#^t1550001-application-access-token|T1550.001: Application Access Token]]
- [[T1550-use_alternate_authentication_material#^t1550002-pass-the-hash|T1550.002: Pass the Hash]]
- [[T1550-use_alternate_authentication_material#^t1550003-pass-the-ticket|T1550.003: Pass the Ticket]]
- [[T1550-use_alternate_authentication_material#^t1550004-web-session-cookie|T1550.004: Web Session Cookie]]
- [[T1556-modify_authentication_process|T1556: Modify Authentication Process]]
- [[T1556-modify_authentication_process#^t1556001-domain-controller-authentication|T1556.001: Domain Controller Authentication]]
- [[T1556-modify_authentication_process#^t1556002-password-filter-dll|T1556.002: Password Filter DLL]]
- [[T1556-modify_authentication_process#^t1556003-pluggable-authentication-modules|T1556.003: Pluggable Authentication Modules]]
- [[T1556-modify_authentication_process#^t1556004-network-device-authentication|T1556.004: Network Device Authentication]]
- [[T1556-modify_authentication_process#^t1556005-reversible-encryption|T1556.005: Reversible Encryption]]
- [[T1556-modify_authentication_process#^t1556006-multi-factor-authentication|T1556.006: Multi-Factor Authentication]]
- [[T1556-modify_authentication_process#^t1556007-hybrid-identity|T1556.007: Hybrid Identity]]
- [[T1556-modify_authentication_process#^t1556008-network-provider-dll|T1556.008: Network Provider DLL]]
- [[T1556-modify_authentication_process#^t1556009-conditional-access-policies|T1556.009: Conditional Access Policies]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
- [[T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]
- [[T1621-multi-factor_authentication_request_generation|T1621: Multi-Factor Authentication Request Generation]]

## Knowledge Base Article

## How it works

Processes are managed by the operating system kernel.  Different operating system kernels manage the creation and termination of processes in a different manner, and expose this functionality via the kernel API.

A running process might be terminated to mitigate its immediate effects if it is exhibiting anomalous, unauthorized, or malicious behavior; such as after detecting anomalous behavior via <a href="https://d3fend.mitre.org/technique/d3f:AdministrativeNetworkActivityAnalysis" rdf:about="https://d3fend.mitre.org/ontologies/d3fend.owl#AdministrativeNetworkActivityAnalysis">Administrative Network Activity Analysis</a>, after a failed check from <a href="https://d3fend.mitre.org/technique/d3f:StackFrameCanaryVerification" rdf:about="https://d3fend.mitre.org/ontologies/d3fend.owl#StackFrameCanaryValidation">Stack Frame Canary Validation</a>, or after <a href="https://d3fend.mitre.org/technique/d3f:SystemCallAnalysis" rdf:about="https://d3fend.mitre.org/ontologies/d3fend.owl#SystemCallAnalysis">System Call Analysis</a> finds an attempt to execute an unauthorized system call.

### Proprietary technology
Security software might use proprietary technology to terminate processes, instead of the system-provided functions.    Further research may provide specific detail on such methods used.

### System-provided functions

#### Windows tools
In Windows, `ExitProcess()` is used to send a signal to a process to request it to exit, and `TerminateProcess()` is used to force a process to exit.

The `taskkill` executable available in the cmd shell is used to kill a process, with the `/F` switch forcing termination as with `TerminateProcess()`.  In PowerShell, `Stop-Process` is used, which is aliased by default to `spps` and `kill`.  Processes started in the Windows Subsystem for Linux (WSL) environment may be terminated there with the `kill` command.

In some cases, existing drivers can also be leveraged to kill processes.

#### Unix/Linux tools
In Unix-like systems, all process termination requests are handled using signals.  The `kill` function takes the Process ID and signal to send, and is accessible with the `kill` command.  Some shells have a `kill` builtin function which is separate than the `kill` binary, which can also kill background jobs in the shell and additionally perform the function faster, and can run from an existing instance of the shell if the process table is full.  The signal SIGTERM specifies that the process to terminate may invoke a handler that it has defined instead of terminating, and the signal SIGKILL forces immediate termination.

The related command `xkill` terminates the connection of a program to the X window server, after which the user process may decide to terminate itself; however, termination is not guaranteed as the process, which could be on the same or different host, could then run in a terminal or reconnect to a different X server on any host.  Emacs is such a program that would not terminate itself after its connection to the X server is terminated.

## Considerations

### Persistence Mechanisms
Terminating a malicious process is not enough to stop an adversary that has already gained persistence in the host via any initial access mechanism, including through that process or another access mechanism.

### Terminating Multiple Processes
On most operating systems, process termination operations typically occur independently of each other, without functionality provided to atomically terminate multiple processes.  If there are multiple malicious processes which can make system calls to spawn other processes once one of them is closed, user session termination or system restart might be required.

### Process Access Permissions
Users must have permissions to kill the process.  On Unix-like systems, either root or the process user can kill the process.  On Windows systems, process permissions are managed separately via process security tokens.

### Process Resource Handles

#### Terminating Processes with Open Resource Handles

Processes may have open resource handles, which could leave those resources in an undesired state if the process is forced to terminate.  As such, most operating systems provide a means to send a signal to a process to inform it to gracefully terminate, and on most of these operating systems, it is the typical first step used to terminate a process.

#### Signal Traps
As the process may have open resource handles, commonly-used methods of process termination involve sending a signal to the process to terminate.
On Windows, the `ExitProcess()` function is used for this purpose.  Process instructions, as well as a third-party DLL can also cause the process to exit.
On Linux, the process is sent a signal on the occurrence of various events: when it loses the console, `SIGHUP`; when termination is requested, `SIGTERM`.  The processor then redirects execution to the function registered to handle the signal.

Therefore, sending a signal to the process to ask it to terminate may not always work.

##### Avoiding Signal Traps

On Unix-like systems, sending the `SIGKILL` signal for a process does not send a message to the process or invoke an implementation-defined handler; instead, it immediately does not allow the process to execute any further processor instructions.   On Windows `TerminateProcess()` instead of `ExitProcess()` performs the equivalent.

#### Hang on System Call Execution

Even still, as the operating system kernel manages the processes, kernel code may block process signals, including those which cannot be trapped, and does in certain circumstances.  Signals are blocked and queued for the duration of the system call when interrupting the system call would result in a kernel invariant being violated, such as when an action results in a malformed data structure; this blocking is common for filesystem requests.  Such system calls can hang when a filesystem has gone offline, leading to a long-term uninterruptible sleep, represented in POSIX command `ps` output as D state.
Any malicious system calls or system call handlers are issues of a much larger problem (a kernel-level rootkit) and the system should be redeployed entirely or restored from a backup known to be prior to compromise, and other systems accessible directly and indirectly from that one should also be examined.

A process that is truly hung in a system call may prevent the system from shutting down and leave it in an unresponsive state; a hard power off is required.

To speed up the action of terminating a process in uninterruptible sleep, the process resource accesses (handles) could be analyzed.

On Linux, [`sync` followed by `echo 3 > /proc/sys/vm/drop_caches`](https://www.kernel.org/doc/Documentation/sysctl/vm.txt) is a safe way to free up some inactive resource handles.


#### Kernel Processes and Threads
The kernel may not allow kernel processes, which are created via methods other than user-space processes, to be terminated.

#### Other Code using the Process

Terminating a shared library can lead to unexpected errors; such shared libraries have their own mechanisms for termination.

On Windows, a DLL is unloaded when the reference count of the library reaches 0.

#### Zombie process

After a process has been terminated, it may still take up an entry in the operating system process table until another event occurs.

##### Windows
In Windows, a process object is deleted when the last handle to the process is closed.

##### Linux
In Linux, a process is removed from the process table when it is reaped by its parent process.  If the parent terminates, historically the parent has been changed to pid 1; however, in the Linux kernel 3.4 and above, processes can set a different process as the subreaper using the `prctl()` system call.

Zombie processes and hung processes could be resolved with a restart of the system.

#### System restart
Finally a system restart might be required to kill a process.
Systems which are only accessible via a remote in-band connection may become inaccessible if a process termination operation that is necessary for reboot does not complete.

### Subsystems
Processes that are started in a subsystem might not be fully terminated if they are terminated using the command for that subsystem.  For example, in the Windows Subsystem for Linux (WSL), processes started and terminated via WSL calls such as with the `kill` command in Bash may still have an entry in the Windows process table.

## Ontology Relationships

- [[D3-PE-process_eviction|D3-PE: Process Eviction]]

