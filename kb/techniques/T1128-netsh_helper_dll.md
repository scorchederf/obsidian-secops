---
id: T1128
name: Netsh Helper DLL
created: 2017-05-31 21:31:40.168000+00:00
modified: 2025-10-24 17:49:17.716000+00:00
type: attack-pattern
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[persistence|Persistence]]

Netsh.exe (also referred to as Netshell) is a command-line scripting utility used to interact with the network configuration of a system. It contains functionality to add helper DLLs for extending functionality of the utility. (Citation: TechNet Netsh) The paths to registered netsh.exe helper DLLs are entered into the Windows Registry at <code>HKLM\SOFTWARE\Microsoft\Netsh</code>.

Adversaries can use netsh.exe with helper DLLs to proxy execution of arbitrary code in a persistent manner when netsh.exe is executed automatically with another Persistence technique or if other persistent software is present on the system that executes netsh.exe as part of its normal functionality. Examples include some VPN software that invoke netsh.exe. (Citation: Demaske Netsh Persistence)

Proof of concept code exists to load Cobalt Strike's payload using netsh.exe helper DLLs. (Citation: Github Netsh Helper CS Beacon)

## Platforms

- Windows

