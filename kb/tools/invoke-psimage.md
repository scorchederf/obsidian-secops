---
id: S0231
name: Invoke-PSImage
created: 2018-04-18 17:59:24.739000+00:00
modified: 2025-04-16 20:38:55.222000+00:00
type: tool
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

# Invoke-PSImage

[Invoke-PSImage](https://attack.mitre.org/software/S0231) takes a PowerShell script and embeds the bytes of the script into the pixels of a PNG image. It generates a one liner for executing either from a file of from the web. Example of usage is embedding the PowerShell code from the Invoke-Mimikatz module and embed it into an image file. By calling the image file from a macro for example, the macro will download the picture and execute the PowerShell code, which in this case will dump the passwords. (Citation: GitHub Invoke-PSImage)

## Uses Techniques

- [[T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]]
    - [[T1027-obfuscated_files_or_information#^t1027003-steganography|T1027.003: Steganography]]
    - [[T1027-obfuscated_files_or_information#^t1027009-embedded-payloads|T1027.009: Embedded Payloads]]

