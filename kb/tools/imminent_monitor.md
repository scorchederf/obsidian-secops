---
id: S0434
name: Imminent Monitor
created: 2020-05-05 18:45:36.358000+00:00
modified: 2023-10-03 19:35:03.646000+00:00
type: tool
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

# Imminent Monitor

[Imminent Monitor](https://attack.mitre.org/software/S0434) was a commodity remote access tool (RAT) offered for sale from 2012 until 2019, when an operation was conducted to take down the Imminent Monitor infrastructure. Various cracked versions and variations of this RAT are still in circulation.(Citation: Imminent Unit42 Dec2019)

## Properties

- id: S0434
- name: Imminent Monitor
- created: 2020-05-05 18:45:36.358000+00:00
- modified: 2023-10-03 19:35:03.646000+00:00
- type: tool
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Uses Techniques

- [[T1021-remote_services|T1021: Remote Services]]
    - [[T1021-remote_services#^t1021001-remote-desktop-protocol|T1021.001: Remote Desktop Protocol]]
- [[T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]]
- [[T1041-exfiltration_over_c2_channel|T1041: Exfiltration Over C2 Channel]]
- [[T1056-input_capture|T1056: Input Capture]]
    - [[T1056-input_capture#^t1056001-keylogging|T1056.001: Keylogging]]
- [[T1057-process_discovery|T1057: Process Discovery]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
- [[T1070-indicator_removal|T1070: Indicator Removal]]
    - [[T1070-indicator_removal#^t1070004-file-deletion|T1070.004: File Deletion]]
- [[T1083-file_and_directory_discovery|T1083: File and Directory Discovery]]
- [[T1106-native_api|T1106: Native API]]
- [[T1123-audio_capture|T1123: Audio Capture]]
- [[T1125-video_capture|T1125: Video Capture]]
- [[T1140-deobfuscate_decode_files_or_information|T1140: Deobfuscate/Decode Files or Information]]
- [[T1496-resource_hijacking|T1496: Resource Hijacking]]
    - [[T1496-resource_hijacking#^t1496001-compute-hijacking|T1496.001: Compute Hijacking]]
- [[T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]
    - [[T1555-credentials_from_password_stores#^t1555003-credentials-from-web-browsers|T1555.003: Credentials from Web Browsers]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
    - [[T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]
    - [[T1564-hide_artifacts#^t1564001-hidden-files-and-directories|T1564.001: Hidden Files and Directories]]

