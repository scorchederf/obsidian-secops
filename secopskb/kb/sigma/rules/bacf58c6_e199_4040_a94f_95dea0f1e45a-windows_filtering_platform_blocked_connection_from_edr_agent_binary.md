---
sigma_id: "bacf58c6-e199-4040-a94f-95dea0f1e45a"
title: "Windows Filtering Platform Blocked Connection From EDR Agent Binary"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/object_access/win_security_wfp_endpoint_agent_blocked.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/object_access/win_security_wfp_endpoint_agent_blocked.yml"
build_date: "2026-04-26 17:03:24"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "bacf58c6-e199-4040-a94f-95dea0f1e45a"
  - "Windows Filtering Platform Blocked Connection From EDR Agent Binary"
attack_technique_ids:
  - "T1562"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows Filtering Platform Blocked Connection From EDR Agent Binary

Detects a Windows Filtering Platform (WFP) blocked connection event involving common Endpoint Detection and Response (EDR) agents.
Adversaries may use WFP filters to prevent Endpoint Detection and Response (EDR) agents from reporting security events.

## Metadata

- Rule ID: bacf58c6-e199-4040-a94f-95dea0f1e45a
- Status: test
- Level: high
- Author: @gott_cyber
- Date: 2024-01-08
- Source Path: rules/windows/builtin/security/object_access/win_security_wfp_endpoint_agent_blocked.yml

## Logsource

- definition: Requirements: Audit Filtering Platform Connection needs to be enabled
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562]]

## Detection

```yaml
selection:
  EventID: 5157
  Application|endswith:
  - \AmSvc.exe
  - \cb.exe
  - \CETASvc.exe
  - \CNTAoSMgr.exe
  - \CrAmTray.exe
  - \CrsSvc.exe
  - \CSFalconContainer.exe
  - \CSFalconService.exe
  - \CybereasonAV.exe
  - \CylanceSvc.exe
  - \cyserver.exe
  - \CyveraService.exe
  - \CyvrFsFlt.exe
  - \EIConnector.exe
  - \elastic-agent.exe
  - \elastic-endpoint.exe
  - \EndpointBasecamp.exe
  - \ExecutionPreventionSvc.exe
  - \filebeat.exe
  - \fortiedr.exe
  - \hmpalert.exe
  - \hurukai.exe
  - \LogProcessorService.exe
  - \mcsagent.exe
  - \mcsclient.exe
  - \MsMpEng.exe
  - \MsSense.exe
  - \Ntrtscan.exe
  - \PccNTMon.exe
  - \QualysAgent.exe
  - \RepMgr.exe
  - \RepUtils.exe
  - \RepUx.exe
  - \RepWAV.exe
  - \RepWSC.exe
  - \sedservice.exe
  - \SenseCncProxy.exe
  - \SenseIR.exe
  - \SenseNdr.exe
  - \SenseSampleUploader.exe
  - \SentinelAgent.exe
  - \SentinelAgentWorker.exe
  - \SentinelBrowserNativeHost.exe
  - \SentinelHelperService.exe
  - \SentinelServiceHost.exe
  - \SentinelStaticEngine.exe
  - \SentinelStaticEngineScanner.exe
  - \sfc.exe
  - \sophos ui.exe
  - \sophosfilescanner.exe
  - \sophosfs.exe
  - \sophoshealth.exe
  - \sophosips.exe
  - \sophosLivequeryservice.exe
  - \sophosnetfilter.exe
  - \sophosntpservice.exe
  - \sophososquery.exe
  - \sspservice.exe
  - \TaniumClient.exe
  - \TaniumCX.exe
  - \TaniumDetectEngine.exe
  - \TMBMSRV.exe
  - \TmCCSF.exe
  - \TmListen.exe
  - \TmWSCSvc.exe
  - \Traps.exe
  - \winlogbeat.exe
  - \WSCommunicator.exe
  - \xagt.exe
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/netero1010/EDRSilencer
- https://github.com/amjcyber/EDRNoiseMaker
- https://ghoulsec.medium.com/misc-series-4-forensics-on-edrsilencer-events-428b20b3f983

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/object_access/win_security_wfp_endpoint_agent_blocked.yml)
