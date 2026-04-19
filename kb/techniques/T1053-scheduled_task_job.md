---
id: T1053
name: Scheduled Task/Job
created: 2017-05-31 21:30:46.977000+00:00
modified: 2025-10-24 17:48:38.539000+00:00
type: attack-pattern
x_mitre_version: 2.4
x_mitre_domains: enterprise-attack
---

## Tactic

- [[privilege_escalation|Privilege Escalation]]

Adversaries may abuse task scheduling functionality to facilitate initial or recurring execution of malicious code. Utilities exist within all major operating systems to schedule programs or scripts to be executed at a specified date and time. A task can also be scheduled on a remote system, provided the proper authentication is met (ex: RPC and file and printer sharing in Windows environments). Scheduling a task on a remote system typically may require being a member of an admin or otherwise privileged group on the remote system.(Citation: TechNet Task Scheduler Security)

Adversaries may use task scheduling to execute programs at system startup or on a scheduled basis for persistence. These mechanisms can also be abused to run a process under the context of a specified account (such as one with elevated permissions/privileges). Similar to [System Binary Proxy Execution](https://attack.mitre.org/techniques/T1218), adversaries have also abused task scheduling to potentially mask one-time execution under a trusted system process.(Citation: ProofPoint Serpent)

## Properties

- id: T1053
- name: Scheduled Task/Job
- created: 2017-05-31 21:30:46.977000+00:00
- modified: 2025-10-24 17:48:38.539000+00:00
- type: attack-pattern
- x_mitre_version: 2.4
- x_mitre_domains: enterprise-attack

## Subtechniques

### T1053.002: At

^t1053002-at

**Parent Technique**
- [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]]

**Tactic**
- [[privilege_escalation|Privilege Escalation]]

Adversaries may abuse the [at](https://attack.mitre.org/software/S0110) utility to perform task scheduling for initial or recurring execution of malicious code. The [at](https://attack.mitre.org/software/S0110) utility exists as an executable within Windows, Linux, and macOS for scheduling tasks at a specified time and date. Although deprecated in favor of [Scheduled Task](https://attack.mitre.org/techniques/T1053/005)'s [schtasks](https://attack.mitre.org/software/S0111) in Windows environments, using [at](https://attack.mitre.org/software/S0110) requires that the Task Scheduler service be running, and the user to be logged on as a member of the local Administrators group. In addition to explicitly running the `at` command, adversaries may also schedule a task with [at](https://attack.mitre.org/software/S0110) by directly leveraging the [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) `Win32_ScheduledJob` WMI class.(Citation: Malicious Life by Cybereason)

On Linux and macOS, [at](https://attack.mitre.org/software/S0110) may be invoked by the superuser as well as any users added to the <code>at.allow</code> file. If the <code>at.allow</code> file does not exist, the <code>at.deny</code> file is checked. Every username not listed in <code>at.deny</code> is allowed to invoke [at](https://attack.mitre.org/software/S0110). If the <code>at.deny</code> exists and is empty, global use of [at](https://attack.mitre.org/software/S0110) is permitted. If neither file exists (which is often the baseline) only the superuser is allowed to use [at](https://attack.mitre.org/software/S0110).(Citation: Linux at)

Adversaries may use [at](https://attack.mitre.org/software/S0110) to execute programs at system startup or on a scheduled basis for [Persistence](https://attack.mitre.org/tactics/TA0003). [at](https://attack.mitre.org/software/S0110) can also be abused to conduct remote [Execution](https://attack.mitre.org/tactics/TA0002) as part of [Lateral Movement](https://attack.mitre.org/tactics/TA0008) and/or to run a process under the context of a specified account (such as SYSTEM).

In Linux environments, adversaries may also abuse [at](https://attack.mitre.org/software/S0110) to break out of restricted environments by using a task to spawn an interactive system shell or to run system commands. Similarly, [at](https://attack.mitre.org/software/S0110) may also be used for [Privilege Escalation](https://attack.mitre.org/tactics/TA0004) if the binary is allowed to run as superuser via <code>sudo</code>.(Citation: GTFObins at)

#### Properties

- id: T1053.002
- name: At
- created: 2019-11-27 13:52:45.853000+00:00
- modified: 2025-10-24 17:49:36.495000+00:00
- type: attack-pattern
- x_mitre_version: 2.4
- x_mitre_domains: enterprise-attack

### T1053.003: Cron

^t1053003-cron

**Parent Technique**
- [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]]

**Tactic**
- [[privilege_escalation|Privilege Escalation]]

Adversaries may abuse the <code>cron</code> utility to perform task scheduling for initial or recurring execution of malicious code.(Citation: 20 macOS Common Tools and Techniques) The <code>cron</code> utility is a time-based job scheduler for Unix-like operating systems.  The <code> crontab</code> file contains the schedule of cron entries to be run and the specified times for execution. Any <code>crontab</code> files are stored in operating system-specific file paths.

An adversary may use <code>cron</code> in Linux or Unix environments to execute programs at system startup or on a scheduled basis for [Persistence](https://attack.mitre.org/tactics/TA0003). In ESXi environments, cron jobs must be created directly via the crontab file (e.g., `/var/spool/cron/crontabs/root`).(Citation: CloudSEK ESXiArgs 2023)

#### Properties

- id: T1053.003
- name: Cron
- created: 2019-12-03 14:25:00.538000+00:00
- modified: 2025-10-24 17:48:33.856000+00:00
- type: attack-pattern
- x_mitre_version: 1.3
- x_mitre_domains: enterprise-attack

### T1053.005: Scheduled Task

^t1053005-scheduled-task

**Parent Technique**
- [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]]

**Tactic**
- [[privilege_escalation|Privilege Escalation]]

Adversaries may abuse the Windows Task Scheduler to perform task scheduling for initial or recurring execution of malicious code. There are multiple ways to access the Task Scheduler in Windows. The [schtasks](https://attack.mitre.org/software/S0111) utility can be run directly on the command line, or the Task Scheduler can be opened through the GUI within the Administrator Tools section of the Control Panel.(Citation: Stack Overflow) In some cases, adversaries have used a .NET wrapper for the Windows Task Scheduler, and alternatively, adversaries have used the Windows netapi32 library and [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) (WMI) to create a scheduled task. Adversaries may also utilize the Powershell Cmdlet `Invoke-CimMethod`, which leverages WMI class `PS_ScheduledTask` to create a scheduled task via an XML path.(Citation: Red Canary - Atomic Red Team)

An adversary may use Windows Task Scheduler to execute programs at system startup or on a scheduled basis for persistence. The Windows Task Scheduler can also be abused to conduct remote Execution as part of Lateral Movement and/or to run a process under the context of a specified account (such as SYSTEM). Similar to [System Binary Proxy Execution](https://attack.mitre.org/techniques/T1218), adversaries have also abused the Windows Task Scheduler to potentially mask one-time execution under signed/trusted system processes.(Citation: ProofPoint Serpent)

Adversaries may also create "hidden" scheduled tasks (i.e. [Hide Artifacts](https://attack.mitre.org/techniques/T1564)) that may not be visible to defender tools and manual queries used to enumerate tasks. Specifically, an adversary may hide a task from `schtasks /query` and the Task Scheduler by deleting the associated Security Descriptor (SD) registry value (where deletion of this value must be completed using SYSTEM permissions).(Citation: SigmaHQ)(Citation: Tarrask scheduled task) Adversaries may also employ alternate methods to hide tasks, such as altering the metadata (e.g., `Index` value) within associated registry keys.(Citation: Defending Against Scheduled Task Attacks in Windows Environments) 

#### Properties

- id: T1053.005
- name: Scheduled Task
- created: 2019-11-27 14:58:00.429000+00:00
- modified: 2025-10-24 17:48:19.176000+00:00
- type: attack-pattern
- x_mitre_version: 1.8
- x_mitre_domains: enterprise-attack

### T1053.006: Systemd Timers

^t1053006-systemd-timers

**Parent Technique**
- [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]]

**Tactic**
- [[privilege_escalation|Privilege Escalation]]

Adversaries may abuse systemd timers to perform task scheduling for initial or recurring execution of malicious code. Systemd timers are unit files with file extension <code>.timer</code> that control services. Timers can be set to run on a calendar event or after a time span relative to a starting point. They can be used as an alternative to [Cron](https://attack.mitre.org/techniques/T1053/003) in Linux environments.(Citation: archlinux Systemd Timers Aug 2020) Systemd timers may be activated remotely via the <code>systemctl</code> command line utility, which operates over [SSH](https://attack.mitre.org/techniques/T1021/004).(Citation: Systemd Remote Control)

Each <code>.timer</code> file must have a corresponding <code>.service</code> file with the same name, e.g., <code>example.timer</code> and <code>example.service</code>. <code>.service</code> files are [Systemd Service](https://attack.mitre.org/techniques/T1543/002) unit files that are managed by the systemd system and service manager.(Citation: Linux man-pages: systemd January 2014) Privileged timers are written to <code>/etc/systemd/system/</code> and <code>/usr/lib/systemd/system</code> while user level are written to <code>~/.config/systemd/user/</code>.

An adversary may use systemd timers to execute malicious code at system startup or on a scheduled basis for persistence.(Citation: Arch Linux Package Systemd Compromise BleepingComputer 10JUL2018)(Citation: gist Arch package compromise 10JUL2018)(Citation: acroread package compromised Arch Linux Mail 8JUL2018) Timers installed using privileged paths may be used to maintain root level persistence. Adversaries may also install user level timers to achieve user level persistence.(Citation: Falcon Sandbox smp: 28553b3a9d)

#### Properties

- id: T1053.006
- name: Systemd Timers
- created: 2020-10-12 17:50:31.584000+00:00
- modified: 2025-10-24 17:49:11.261000+00:00
- type: attack-pattern
- x_mitre_version: 1.3
- x_mitre_domains: enterprise-attack

### T1053.007: Container Orchestration Job

^t1053007-container-orchestration-job

**Parent Technique**
- [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]]

**Tactic**
- [[privilege_escalation|Privilege Escalation]]

Adversaries may abuse task scheduling functionality provided by container orchestration tools such as Kubernetes to schedule deployment of containers configured to execute malicious code. Container orchestration jobs run these automated tasks at a specific date and time, similar to cron jobs on a Linux system. Deployments of this type can also be configured to maintain a quantity of containers over time, automating the process of maintaining persistence within a cluster.

In Kubernetes, a CronJob may be used to schedule a Job that runs one or more containers to perform specific tasks.(Citation: Kubernetes Jobs)(Citation: Kubernetes CronJob) An adversary therefore may utilize a CronJob to schedule deployment of a Job that executes malicious code in various nodes within a cluster.(Citation: Threat Matrix for Kubernetes)

#### Properties

- id: T1053.007
- name: Container Orchestration Job
- created: 2021-03-29 17:06:22.247000+00:00
- modified: 2025-10-24 17:48:25.363000+00:00
- type: attack-pattern
- x_mitre_version: 1.4
- x_mitre_domains: enterprise-attack

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

## Tools


