---
id: S0581
name: IronNetInjector
created: 2021-02-24 21:28:44.175000+00:00
modified: 2024-04-11 02:14:36.791000+00:00
type: tool
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

# IronNetInjector

[IronNetInjector](https://attack.mitre.org/software/S0581) is a [Turla](https://attack.mitre.org/groups/G0010) toolchain that utilizes scripts from the open-source IronPython implementation of Python with a .NET injector to drop one or more payloads including [ComRAT](https://attack.mitre.org/software/S0126).(Citation: Unit 42 IronNetInjector February 2021 )

## Properties

- id: S0581
- name: IronNetInjector
- created: 2021-02-24 21:28:44.175000+00:00
- modified: 2024-04-11 02:14:36.791000+00:00
- type: tool
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Uses Techniques

- [[T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]]
    - [[T1027-obfuscated_files_or_information#^t1027013-encrypted-encoded-file|T1027.013: Encrypted/Encoded File]]
- [[T1036-masquerading|T1036: Masquerading]]
    - [[T1036-masquerading#^t1036004-masquerade-task-or-service|T1036.004: Masquerade Task or Service]]
- [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]]
    - [[T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]
- [[T1055-process_injection|T1055: Process Injection]]
    - [[T1055-process_injection#^t1055001-dynamic-link-library-injection|T1055.001: Dynamic-link Library Injection]]
- [[T1057-process_discovery|T1057: Process Discovery]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
    - [[T1059-command_and_scripting_interpreter#^t1059006-python|T1059.006: Python]]
- [[T1140-deobfuscate_decode_files_or_information|T1140: Deobfuscate/Decode Files or Information]]

