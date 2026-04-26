---
mitre_id: "S0231"
mitre_name: "Invoke-PSImage"
mitre_type: "tool"
mitre_stix_id: "tool--b52d6583-14a2-4ddc-8527-87fd2142558f"
mitre_created: "2018-04-18T17:59:24.739Z"
mitre_modified: "2025-04-16T20:38:55.222Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0231/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "tool"
tags:
  - "attack"
  - "tool"
  - "offense"
mitre_aliases:
  - "Invoke-PSImage"
aliases:
  - "S0231"
  - "Invoke-PSImage"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

[Invoke-PSImage](https://attack.mitre.org/software/S0231) takes a PowerShell script and embeds the bytes of the script into the pixels of a PNG image. It generates a one liner for executing either from a file of from the web. Example of usage is embedding the PowerShell code from the Invoke-Mimikatz module and embed it into an image file. By calling the image file from a macro for example, the macro will download the picture and execute the PowerShell code, which in this case will dump the passwords. (Citation: GitHub Invoke-PSImage)

## Workspace

- [[workspaces/tools/S0231-invoke-psimage-note|Open workspace note]]

![[workspaces/tools/S0231-invoke-psimage-note]]

## Uses Techniques

- [[T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]]
    - [[T1027-obfuscated_files_or_information#^t1027003-steganography|T1027.003: Steganography]]
    - [[T1027-obfuscated_files_or_information#^t1027009-embedded-payloads|T1027.009: Embedded Payloads]]

