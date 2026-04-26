---
mitre_id: "T1053"
mitre_name: "Scheduled Task/Job"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--35dd844a-b219-4e2b-a6bb-efa9a75995a9"
mitre_created: "2017-05-31T21:30:46.977Z"
mitre_modified: "2025-10-24T17:48:38.539Z"
mitre_version: "2.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1053/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
  - "Linux"
  - "macOS"
  - "Containers"
  - "ESXi"
mitre_tactic_ids:
  - "TA0002"
  - "TA0003"
  - "TA0004"
d3fend_ids:
  - "D3-ABPI"
  - "D3-CF"
  - "D3-CM"
  - "D3-CQ"
  - "D3-DF"
  - "D3-EAL"
  - "D3-EDL"
  - "D3-FA"
  - "D3-FE"
  - "D3-FEV"
  - "D3-FIM"
  - "D3-HBPI"
  - "D3-HR"
  - "D3-HS"
  - "D3-KBPI"
  - "D3-LFP"
  - "D3-PLA"
  - "D3-PS"
  - "D3-PSA"
  - "D3-PSMD"
  - "D3-PT"
  - "D3-RF"
  - "D3-RFAM"
  - "D3-SCA"
  - "D3-SCF"
  - "D3-SDM"
  - "D3-SJA"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may abuse task scheduling functionality to facilitate initial or recurring execution of malicious code. Utilities exist within all major operating systems to schedule programs or scripts to be executed at a specified date and time. A task can also be scheduled on a remote system, provided the proper authentication is met (ex: RPC and file and printer sharing in Windows environments). Scheduling a task on a remote system typically may require being a member of an admin or otherwise privileged group on the remote system.(Citation: TechNet Task Scheduler Security)

Adversaries may use task scheduling to execute programs at system startup or on a scheduled basis for persistence. These mechanisms can also be abused to run a process under the context of a specified account (such as one with elevated permissions/privileges). Similar to [[T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]], adversaries have also abused task scheduling to potentially mask one-time execution under a trusted system process.(Citation: ProofPoint Serpent)

## Workspace

- [[workspaces/attack/techniques/T1053-scheduled_task_job-note|Open workspace note]]

![[workspaces/attack/techniques/T1053-scheduled_task_job-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### CAR Analytics

- [[kb/car/analytics/CAR-2013-01-002-autorun_differences|CAR-2013-01-002: Autorun Differences]]
- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2013-05-004-execution_with_at|CAR-2013-05-004: Execution with AT]]
- [[kb/car/analytics/CAR-2013-08-001-execution_with_schtasks|CAR-2013-08-001: Execution with schtasks]]
- [[kb/car/analytics/CAR-2015-04-001-remotely_scheduled_tasks_via_at|CAR-2015-04-001: Remotely Scheduled Tasks via AT]]
- [[kb/car/analytics/CAR-2015-04-002-remotely_scheduled_tasks_via_schtasks|CAR-2015-04-002: Remotely Scheduled Tasks via Schtasks]]
- [[kb/car/analytics/CAR-2020-09-001-scheduled_task_fileaccess|CAR-2020-09-001: Scheduled Task - FileAccess]]
- [[kb/car/analytics/CAR-2021-12-001-scheduled_task_creation_or_modification_containing_suspicious_scripts_extensions_or_user_writable_paths|CAR-2021-12-001: Scheduled Task Creation or Modification Containing Suspicious Scripts, Extensions or User Writable Paths]]

### Sigma Rules

- [[kb/sigma/rules/058f4380_962d_40a5_afce_50207d36d7e2-hacktool_crackmapexec_execution_patterns|HackTool - CrackMapExec Execution Patterns (high; windows / process_creation)]]
- [[kb/sigma/rules/0fcd1c79_4eeb_4746_aba9_1b458f7a79cb-remote_schedule_task_lateral_movement_via_atsvc|Remote Schedule Task Lateral Movement via ATSvc (high; rpc_firewall / application)]]
- [[kb/sigma/rules/1a2ea919_d11d_4d1e_8535_06cda13be20f-triple_cross_ebpf_rootkit_default_persistence|Triple Cross eBPF Rootkit Default Persistence (high; linux / file_event)]]
- [[kb/sigma/rules/1c0e41cd_21bb_4433_9acc_4a2cd6367b9b-suspicious_modification_of_scheduled_tasks|Suspicious Modification Of Scheduled Tasks (high; windows / process_creation)]]
- [[kb/sigma/rules/24c8392b_aa3c_46b7_a545_43f71657fe98-suspicious_schtasks_schedule_types|Suspicious Schtasks Schedule Types (high; windows / process_creation)]]
- [[kb/sigma/rules/26488ad0_f9fd_4536_876f_52fea846a2e4-hacktool_sharpersist_execution|HackTool - SharPersist Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/2daa93a0_a5fb_41c5_8cd8_3c11294bfd1f-potential_ssh_tunnel_persistence_install_using_a_scheduled_task|Potential SSH Tunnel Persistence Install Using A Scheduled Task (high; windows / process_creation)]]
- [[kb/sigma/rules/39019a4e_317f_4ce3_ae63_309a8c6b53c5-suspicious_scheduled_task_creation_involving_temp_folder|Suspicious Scheduled Task Creation Involving Temp Folder (high; windows / process_creation)]]
- [[kb/sigma/rules/3a734d25_df5c_4b99_8034_af1ddb5883a4-suspicious_scheduled_task_creation|Suspicious Scheduled Task Creation (high; windows / security)]]
- [[kb/sigma/rules/42a993dd_bb3e_48c8_b372_4d6684c4106c-hacktool_crackmapexec_execution|HackTool - CrackMapExec Execution (high; windows / process_creation)]]
- 19 more in the generated source index

### Atomic Tests

- [[kb/atomic/tests/02124c37_767e_4b76_9383_c9fc366d9d4c-scheduled_task_persistence_via_eventviewer_msc|Scheduled Task Persistence via Eventviewer.msc (command_prompt; windows)]]
- [[kb/atomic/tests/078e69eb_d9fb_450e_b9d0_2e118217c846-cron_add_script_to_etc_cron_d_folder|Cron - Add script to /etc/cron.d folder (sh; linux)]]
- [[kb/atomic/tests/2d943c18_e74a_44bf_936f_25ade6cccab4-cron_add_script_to_var_spool_cron_crontabs_folder|Cron - Add script to /var/spool/cron/crontabs/ folder (bash; linux)]]
- [[kb/atomic/tests/2e5eac3e_327b_4a88_a0c0_c4057039a8dd-scheduled_task_remote|Scheduled task Remote (command_prompt; windows)]]
- [[kb/atomic/tests/3de33f5b_62e5_4e63_a2a0_6fd8808c80ec-create_a_user_level_transient_systemd_service_and_timer|Create a user level transient systemd service and timer (sh; linux)]]
- [[kb/atomic/tests/42f53695_ad4a_4546_abb6_7d837f644a71-scheduled_task_local|Scheduled task Local (command_prompt; windows)]]
- [[kb/atomic/tests/435057fb_74b1_410e_9403_d81baf194f75-cron_replace_crontab_with_referenced_file|Cron - Replace crontab with referenced file (sh; linux, macos)]]
- [[kb/atomic/tests/4a6c0dc4_0f2a_4203_9298_a5a9bdc21ed8-at_exe_scheduled_task|At.exe Scheduled task (command_prompt; windows)]]
- [[kb/atomic/tests/704333ca_cc12_4bcf_9916_101844881f54-scheduled_task_ghost_task_via_registry_key_manipulation|Scheduled Task ("Ghost Task") via Registry Key Manipulation (command_prompt; windows)]]
- [[kb/atomic/tests/7266d898_ac82_4ec0_97c7_436075d0d08e-at_schedule_a_job|At - Schedule a job (sh; linux)]]
- 14 more in the generated source index

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0002-execution|TA0002: Execution]]
- [[TA0003-persistence|TA0003: Persistence]]
- [[TA0004-privilege_escalation|TA0004: Privilege Escalation]]

## D3FEND

- [[D3-ABPI-application-based_process_isolation|D3-ABPI: Application-based Process Isolation]]
- [[D3-CF-content_filtering|D3-CF: Content Filtering]]
- [[D3-CM-content_modification|D3-CM: Content Modification]]
- [[D3-CQ-content_quarantine|D3-CQ: Content Quarantine]]
- [[D3-DF-decoy_file|D3-DF: Decoy File]]
- [[D3-EAL-executable_allowlisting|D3-EAL: Executable Allowlisting]]
- [[D3-EDL-executable_denylisting|D3-EDL: Executable Denylisting]]
- [[D3-FA-file_analysis|D3-FA: File Analysis]]
- [[D3-FE-file_encryption|D3-FE: File Encryption]]
- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]
- [[D3-FIM-file_integrity_monitoring|D3-FIM: File Integrity Monitoring]]
- [[D3-HBPI-hardware-based_process_isolation|D3-HBPI: Hardware-based Process Isolation]]
- [[D3-HR-host_reboot|D3-HR: Host Reboot]]
- [[D3-HS-host_shutdown|D3-HS: Host Shutdown]]
- [[D3-KBPI-kernel-based_process_isolation|D3-KBPI: Kernel-based Process Isolation]]
- [[D3-LFP-local_file_permissions|D3-LFP: Local File Permissions]]
- [[D3-PLA-process_lineage_analysis|D3-PLA: Process Lineage Analysis]]
- [[D3-PS-process_suspension|D3-PS: Process Suspension]]
- [[D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]
- [[D3-PSMD-process_self-modification_detection|D3-PSMD: Process Self-Modification Detection]]
- [[D3-PT-process_termination|D3-PT: Process Termination]]
- [[D3-RF-restore_file|D3-RF: Restore File]]
- [[D3-RFAM-remote_file_access_mediation|D3-RFAM: Remote File Access Mediation]]
- [[D3-SCA-system_call_analysis|D3-SCA: System Call Analysis]]
- [[D3-SCF-system_call_filtering|D3-SCF: System Call Filtering]]
- [[D3-SDM-system_daemon_monitoring|D3-SDM: System Daemon Monitoring]]
- [[D3-SJA-scheduled_job_analysis|D3-SJA: Scheduled Job Analysis]]

## Subtechniques

### T1053.002: At

^t1053002-at

Adversaries may abuse the [[at|at (S0110)]] utility to perform task scheduling for initial or recurring execution of malicious code. The [[at|at (S0110)]] utility exists as an executable within Windows, Linux, and macOS for scheduling tasks at a specified time and date. Although deprecated in favor of [[T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]'s [[schtasks|schtasks (S0111)]] in Windows environments, using [[at|at (S0110)]] requires that the Task Scheduler service be running, and the user to be logged on as a member of the local Administrators group. In addition to explicitly running the `at` command, adversaries may also schedule a task with [[at|at (S0110)]] by directly leveraging the [[T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]] `Win32_ScheduledJob` WMI class.(Citation: Malicious Life by Cybereason)

On Linux and macOS, [[at|at (S0110)]] may be invoked by the superuser as well as any users added to the `at.allow` file. If the `at.allow` file does not exist, the `at.deny` file is checked. Every username not listed in `at.deny` is allowed to invoke [[at|at (S0110)]]. If the `at.deny` exists and is empty, global use of [[at|at (S0110)]] is permitted. If neither file exists (which is often the baseline) only the superuser is allowed to use [[at|at (S0110)]].(Citation: Linux at)

Adversaries may use [[at|at (S0110)]] to execute programs at system startup or on a scheduled basis for [[TA0003-persistence|TA0003: Persistence]]. [[at|at (S0110)]] can also be abused to conduct remote [[TA0002-execution|TA0002: Execution]] as part of [[TA0008-lateral_movement|TA0008: Lateral Movement]] and/or to run a process under the context of a specified account (such as SYSTEM).

In Linux environments, adversaries may also abuse [[at|at (S0110)]] to break out of restricted environments by using a task to spawn an interactive system shell or to run system commands. Similarly, [[at|at (S0110)]] may also be used for [[TA0004-privilege_escalation|TA0004: Privilege Escalation]] if the binary is allowed to run as superuser via `sudo`.(Citation: GTFObins at)

### T1053.003: Cron

^t1053003-cron

Adversaries may abuse the `cron` utility to perform task scheduling for initial or recurring execution of malicious code.(Citation: 20 macOS Common Tools and Techniques) The `cron` utility is a time-based job scheduler for Unix-like operating systems.  The `crontab` file contains the schedule of cron entries to be run and the specified times for execution. Any `crontab` files are stored in operating system-specific file paths.

An adversary may use `cron` in Linux or Unix environments to execute programs at system startup or on a scheduled basis for [[TA0003-persistence|TA0003: Persistence]]. In ESXi environments, cron jobs must be created directly via the crontab file (e.g., `/var/spool/cron/crontabs/root`).(Citation: CloudSEK ESXiArgs 2023)

### T1053.005: Scheduled Task

^t1053005-scheduled-task

Adversaries may abuse the Windows Task Scheduler to perform task scheduling for initial or recurring execution of malicious code. There are multiple ways to access the Task Scheduler in Windows. The [[schtasks|schtasks (S0111)]] utility can be run directly on the command line, or the Task Scheduler can be opened through the GUI within the Administrator Tools section of the Control Panel.(Citation: Stack Overflow) In some cases, adversaries have used a .NET wrapper for the Windows Task Scheduler, and alternatively, adversaries have used the Windows netapi32 library and [[T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]] (WMI) to create a scheduled task. Adversaries may also utilize the Powershell Cmdlet `Invoke-CimMethod`, which leverages WMI class `PS_ScheduledTask` to create a scheduled task via an XML path.(Citation: Red Canary - Atomic Red Team)

An adversary may use Windows Task Scheduler to execute programs at system startup or on a scheduled basis for persistence. The Windows Task Scheduler can also be abused to conduct remote Execution as part of Lateral Movement and/or to run a process under the context of a specified account (such as SYSTEM). Similar to [[T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]], adversaries have also abused the Windows Task Scheduler to potentially mask one-time execution under signed/trusted system processes.(Citation: ProofPoint Serpent)

Adversaries may also create "hidden" scheduled tasks (i.e. [[T1564-hide_artifacts|T1564: Hide Artifacts]]) that may not be visible to defender tools and manual queries used to enumerate tasks. Specifically, an adversary may hide a task from `schtasks /query` and the Task Scheduler by deleting the associated Security Descriptor (SD) registry value (where deletion of this value must be completed using SYSTEM permissions).(Citation: SigmaHQ)(Citation: Tarrask scheduled task) Adversaries may also employ alternate methods to hide tasks, such as altering the metadata (e.g., `Index` value) within associated registry keys.(Citation: Defending Against Scheduled Task Attacks in Windows Environments) 

### T1053.006: Systemd Timers

^t1053006-systemd-timers

Adversaries may abuse systemd timers to perform task scheduling for initial or recurring execution of malicious code. Systemd timers are unit files with file extension `.timer` that control services. Timers can be set to run on a calendar event or after a time span relative to a starting point. They can be used as an alternative to [[T1053-scheduled_task_job#^t1053003-cron|T1053.003: Cron]] in Linux environments.(Citation: archlinux Systemd Timers Aug 2020) Systemd timers may be activated remotely via the `systemctl` command line utility, which operates over [[T1021-remote_services#^t1021004-ssh|T1021.004: SSH]].(Citation: Systemd Remote Control)

Each `.timer` file must have a corresponding `.service` file with the same name, e.g., `example.timer` and `example.service`. `.service` files are [[T1543-create_or_modify_system_process#^t1543002-systemd-service|T1543.002: Systemd Service]] unit files that are managed by the systemd system and service manager.(Citation: Linux man-pages: systemd January 2014) Privileged timers are written to `/etc/systemd/system/` and `/usr/lib/systemd/system` while user level are written to `~/.config/systemd/user/`.

An adversary may use systemd timers to execute malicious code at system startup or on a scheduled basis for persistence.(Citation: Arch Linux Package Systemd Compromise BleepingComputer 10JUL2018)(Citation: gist Arch package compromise 10JUL2018)(Citation: acroread package compromised Arch Linux Mail 8JUL2018) Timers installed using privileged paths may be used to maintain root level persistence. Adversaries may also install user level timers to achieve user level persistence.(Citation: Falcon Sandbox smp: 28553b3a9d)

### T1053.007: Container Orchestration Job

^t1053007-container-orchestration-job

Adversaries may abuse task scheduling functionality provided by container orchestration tools such as Kubernetes to schedule deployment of containers configured to execute malicious code. Container orchestration jobs run these automated tasks at a specific date and time, similar to cron jobs on a Linux system. Deployments of this type can also be configured to maintain a quantity of containers over time, automating the process of maintaining persistence within a cluster.

In Kubernetes, a CronJob may be used to schedule a Job that runs one or more containers to perform specific tasks.(Citation: Kubernetes Jobs)(Citation: Kubernetes CronJob) An adversary therefore may utilize a CronJob to schedule deployment of a Job that executes malicious code in various nodes within a cluster.(Citation: Threat Matrix for Kubernetes)

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1022-restrict_file_and_directory_permissions|M1022: Restrict File and Directory Permissions]]
- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1028-operating_system_configuration|M1028: Operating System Configuration]]
- [[M1047-audit|M1047: Audit]]

## Platforms

- Windows
- Linux
- macOS
- Containers
- ESXi

