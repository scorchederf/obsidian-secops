---
sigma_id: "ce72ef99-22f1-43d4-8695-419dcb5d9330"
title: "Suspicious Windows Service Tampering"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_service_tamper.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_service_tamper.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "ce72ef99-22f1-43d4-8695-419dcb5d9330"
  - "Suspicious Windows Service Tampering"
attack_technique_ids:
  - "T1489"
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Windows Service Tampering

Detects the usage of binaries such as 'net', 'sc' or 'powershell' in order to stop, pause, disable or delete critical or important Windows services such as AV, Backup, etc. As seen being used in some ransomware scripts

## Metadata

- Rule ID: ce72ef99-22f1-43d4-8695-419dcb5d9330
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems), frack113 , X__Junior (Nextron Systems)
- Date: 2022-09-01
- Modified: 2025-08-27
- Source Path: rules/windows/process_creation/proc_creation_win_susp_service_tamper.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1489-service_stop|T1489]]
- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection_tools_img:
- OriginalFileName:
  - net.exe
  - net1.exe
  - PowerShell_ISE.EXE
  - PowerShell.EXE
  - psservice.exe
  - pwsh.dll
  - sc.exe
  - wmic.exe
- Image|endswith:
  - \net.exe
  - \net1.exe
  - \PowerShell_ISE.EXE
  - \powershell.exe
  - \PsService.exe
  - \PsService64.exe
  - \pwsh.exe
  - \sc.exe
  - \wmic.exe
selection_tools_cli:
- CommandLine|contains:
  - ' delete '
  - .delete()
  - ' pause '
  - ' stop '
  - 'Stop-Service '
  - 'Remove-Service '
- CommandLine|contains|all:
  - config
  - start=disabled
selection_services:
  CommandLine|contains:
  - 143Svc
  - Acronis VSS Provider
  - AcronisAgent
  - AcrSch2Svc
  - AdobeARMservice
  - AHS Service
  - Antivirus
  - Apache4
  - ARSM
  - aswBcc
  - AteraAgent
  - Avast Business Console Client Antivirus Service
  - avast! Antivirus
  - AVG Antivirus
  - avgAdminClient
  - AvgAdminServer
  - AVP1
  - BackupExec
  - bedbg
  - BITS
  - BrokerInfrastructure
  - CASLicenceServer
  - CASWebServer
  - Client Agent 7.60
  - Core Browsing Protection
  - Core Mail Protection
  - Core Scanning Server
  - DCAgent
  - dwmrcs
  - EhttpSr
  - ekrn
  - Enterprise Client Service
  - epag
  - EPIntegrationService
  - EPProtectedService
  - EPRedline
  - EPSecurityService
  - EPUpdateService
  - EraserSvc11710
  - EsgShKernel
  - ESHASRV
  - FA_Scheduler
  - FirebirdGuardianDefaultInstance
  - FirebirdServerDefaultInstance
  - FontCache3.0.0.0
  - HealthTLService
  - hmpalertsvc
  - HMS
  - HostControllerService
  - hvdsvc
  - IAStorDataMgrSvc
  - IBMHPS
  - ibmspsvc
  - IISAdmin
  - IMANSVC
  - IMAP4Svc
  - instance2
  - KAVFS
  - KAVFSGT
  - kavfsslp
  - KeyIso
  - klbackupdisk
  - klbackupflt
  - klflt
  - klhk
  - KLIF
  - klim6
  - klkbdflt
  - klmouflt
  - klnagent
  - klpd
  - kltap
  - KSDE1.0.0
  - LogProcessorService
  - M8EndpointAgent
  - macmnsvc
  - masvc
  - MBAMService
  - MBCloudEA
  - MBEndpointAgent
  - McAfeeDLPAgentService
  - McAfeeEngineService
  - MCAFEEEVENTPARSERSRV
  - McAfeeFramework
  - MCAFEETOMCATSRV530
  - McShield
  - McTaskManager
  - mfefire
  - mfemms
  - mfevto
  - mfevtp
  - mfewc
  - MMS
  - mozyprobackup
  - mpssvc
  - MSComplianceAudit
  - MSDTC
  - MsDtsServer
  - MSExchange
  - msftesq1SPROO
  - msftesql$PROD
  - msftesql$SQLEXPRESS
  - MSOLAP$SQL_2008
  - MSOLAP$SYSTEM_BGC
  - MSOLAP$TPS
  - MSOLAP$TPSAMA
  - MSOLAPSTPS
  - MSOLAPSTPSAMA
  - mssecflt
  - MSSQ!I.SPROFXENGAGEMEHT
  - MSSQ0SHAREPOINT
  - MSSQ0SOPHOS
  - MSSQL
  - MSSQLFDLauncher$
  - MySQL
  - NanoServiceMain
  - NetMsmqActivator
  - NetPipeActivator
  - netprofm
  - NetTcpActivator
  - NetTcpPortSharing
  - ntrtscan
  - nvspwmi
  - ofcservice
  - Online Protection System
  - OracleClientCache80
  - OracleDBConsole
  - OracleMTSRecoveryService
  - OracleOraDb11g_home1
  - OracleService
  - OracleVssWriter
  - osppsvc
  - PandaAetherAgent
  - PccNTUpd
  - PDVFSService
  - POP3Svc
  - postgresql-x64-9.4
  - POVFSService
  - PSUAService
  - Quick Update Service
  - RepairService
  - ReportServer
  - ReportServer$
  - RESvc
  - RpcEptMapper
  - sacsvr
  - SamSs
  - SAVAdminService
  - SAVService
  - ScSecSvc
  - SDRSVC
  - SearchExchangeTracing
  - sense
  - SentinelAgent
  - SentinelHelperService
  - SepMasterService
  - ShMonitor
  - Smcinst
  - SmcService
  - SMTPSvc
  - SNAC
  - SntpService
  - Sophos
  - SQ1SafeOLRService
  - SQL Backups
  - SQL Server
  - SQLAgent
  - SQLANYs_Sage_FAS_Fixed_Assets
  - SQLBrowser
  - SQLsafe
  - SQLSERVERAGENT
  - SQLTELEMETRY
  - SQLWriter
  - SSISTELEMETRY130
  - SstpSvc
  - storflt
  - svcGenericHost
  - swc_service
  - swi_filter
  - swi_service
  - swi_update
  - Symantec
  - sysmon
  - TeamViewer
  - Telemetryserver
  - ThreatLockerService
  - TMBMServer
  - TmCCSF
  - TmFilter
  - TMiCRCScanService
  - tmlisten
  - TMLWCSService
  - TmPfw
  - TmPreFilter
  - TmProxy
  - TMSmartRelayService
  - tmusa
  - Tomcat
  - Trend Micro Deep Security Manager
  - TrueKey
  - UFNet
  - UI0Detect
  - UniFi
  - UTODetect
  - vds
  - Veeam
  - VeeamDeploySvc
  - Veritas System Recovery
  - vmic
  - VMTools
  - vmvss
  - VSApiNt
  - VSS
  - W3Svc
  - wbengine
  - WdNisSvc
  - WeanClOudSve
  - Weems JY
  - WinDefend
  - wmms
  - wozyprobackup
  - WPFFontCache_v0400
  - WRSVC
  - wsbexchange
  - WSearch
  - wscsvc
  - Zoolz 2 Service
condition: all of selection_*
```

## False Positives

- Administrators or tools shutting down the services due to upgrade or removal purposes. If you experience some false positive, please consider adding filters to the parent process launching this command and not removing the entry

## References

- https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/h/ransomware-actor-abuses-genshin-impact-anti-cheat-driver-to-kill-antivirus/Genshin%20Impact%20Figure%2010.jpg
- https://www.trellix.com/en-sg/about/newsroom/stories/threat-labs/lockergoga-ransomware-family-used-in-targeted-attacks.html
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.001/T1562.001.md
- https://research.nccgroup.com/2022/08/19/back-in-black-unlocking-a-lockbit-3-0-ransomware-attack/
- https://www.virustotal.com/gui/file/38283b775552da8981452941ea74191aa0d203edd3f61fb2dee7b0aea3514955
- https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/delete-method-in-class-win32-service

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_service_tamper.yml)
