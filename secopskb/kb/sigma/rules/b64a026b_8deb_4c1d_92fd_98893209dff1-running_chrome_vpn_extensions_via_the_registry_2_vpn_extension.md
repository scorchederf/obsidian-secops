---
sigma_id: "b64a026b-8deb-4c1d-92fd-98893209dff1"
title: "Running Chrome VPN Extensions via the Registry 2 VPN Extension"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_chrome_extension.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_chrome_extension.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "b64a026b-8deb-4c1d-92fd-98893209dff1"
  - "Running Chrome VPN Extensions via the Registry 2 VPN Extension"
attack_technique_ids:
  - "T1133"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Running Chrome VPN Extensions via the Registry 2 VPN Extension

Running Chrome VPN Extensions via the Registry install 2 vpn extension

## Metadata

- Rule ID: b64a026b-8deb-4c1d-92fd-98893209dff1
- Status: test
- Level: high
- Author: frack113
- Date: 2021-12-28
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_chrome_extension.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1133-external_remote_services|T1133]]

## Detection

```yaml
chrome_ext:
  TargetObject|contains: Software\Wow6432Node\Google\Chrome\Extensions
  TargetObject|endswith: update_url
chrome_vpn:
  TargetObject|contains:
  - fdcgdnkidjaadafnichfpabhfomcebme
  - fcfhplploccackoneaefokcmbjfbkenj
  - bihmplhobchoageeokmgbdihknkjbknd
  - gkojfkhlekighikafcpjkiklfbnlmeio
  - jajilbjjinjmgcibalaakngmkilboobh
  - gjknjjomckknofjidppipffbpoekiipm
  - nabbmpekekjknlbkgpodfndbodhijjem
  - kpiecbcckbofpmkkkdibbllpinceiihk
  - nlbejmccbhkncgokjcmghpfloaajcffj
  - omghfjlpggmjjaagoclmmobgdodcjboh
  - bibjcjfmgapbfoljiojpipaooddpkpai
  - mpcaainmfjjigeicjnlkdfajbioopjko
  - jljopmgdobloagejpohpldgkiellmfnc
  - lochiccbgeohimldjooaakjllnafhaid
  - nhnfcgpcbfclhfafjlooihdfghaeinfc
  - ookhnhpkphagefgdiemllfajmkdkcaim
  - namfblliamklmeodpcelkokjbffgmeoo
  - nbcojefnccbanplpoffopkoepjmhgdgh
  - majdfhpaihoncoakbjgbdhglocklcgno
  - lnfdmdhmfbimhhpaeocncdlhiodoblbd
  - eppiocemhmnlbhjplcgkofciiegomcon
  - cocfojppfigjeefejbpfmedgjbpchcng
  - foiopecknacmiihiocgdjgbjokkpkohc
  - hhdobjgopfphlmjbmnpglhfcgppchgje
  - jgbaghohigdbgbolncodkdlpenhcmcge
  - inligpkjkhbpifecbdjhmdpcfhnlelja
  - higioemojdadgdbhbbbkfbebbdlfjbip
  - hipncndjamdcmphkgngojegjblibadbe
  - iolonopooapdagdemdoaihahlfkncfgg
  - nhfjkakglbnnpkpldhjmpmmfefifedcj
  - jpgljfpmoofbmlieejglhonfofmahini
  - fgddmllnllkalaagkghckoinaemmogpe
  - ejkaocphofnobjdedneohbbiilggdlbi
  - keodbianoliadkoelloecbhllnpiocoi
  - hoapmlpnmpaehilehggglehfdlnoegck
  - poeojclicodamonabcabmapamjkkmnnk
  - dfkdflfgjdajbhocmfjolpjbebdkcjog
  - kcdahmgmaagjhocpipbodaokikjkampi
  - klnkiajpmpkkkgpgbogmcgfjhdoljacg
  - lneaocagcijjdpkcabeanfpdbmapcjjg
  - pgfpignfckbloagkfnamnolkeaecfgfh
  - jplnlifepflhkbkgonidnobkakhmpnmh
  - jliodmnojccaloajphkingdnpljdhdok
  - hnmpcagpplmpfojmgmnngilcnanddlhb
  - ffbkglfijbcbgblgflchnbphjdllaogb
  - kcndmbbelllkmioekdagahekgimemejo
  - jdgilggpfmjpbodmhndmhojklgfdlhob
  - bihhflimonbpcfagfadcnbbdngpopnjb
  - ppajinakbfocjfnijggfndbdmjggcmde
  - oofgbpoabipfcfjapgnbbjjaenockbdp
  - bhnhkdgoefpmekcgnccpnhjfdgicfebm
  - knmmpciebaoojcpjjoeonlcjacjopcpf
  - dhadilbmmjiooceioladdphemaliiobo
  - jedieiamjmoflcknjdjhpieklepfglin
  - mhngpdlhojliikfknhfaglpnddniijfh
  - omdakjcmkglenbhjadbccaookpfjihpa
  - npgimkapccfidfkfoklhpkgmhgfejhbj
  - akeehkgglkmpapdnanoochpfmeghfdln
  - gbmdmipapolaohpinhblmcnpmmlgfgje
  - aigmfoeogfnljhnofglledbhhfegannp
  - cgojmfochfikphincbhokimmmjenhhgk
  - ficajfeojakddincjafebjmfiefcmanc
  - ifnaibldjfdmaipaddffmgcmekjhiloa
  - jbnmpdkcfkochpanomnkhnafobppmccn
  - apcfdffemoinopelidncddjbhkiblecc
  - mjolnodfokkkaichkcjipfgblbfgojpa
  - oifjbnnafapeiknapihcmpeodaeblbkn
  - plpmggfglncceinmilojdkiijhmajkjh
  - mjnbclmflcpookeapghfhapeffmpodij
  - bblcccknbdbplgmdjnnikffefhdlobhp
  - aojlhgbkmkahabcmcpifbolnoichfeep
  - lcmammnjlbmlbcaniggmlejfjpjagiia
  - knajdeaocbpmfghhmijicidfcmdgbdpm
  - bdlcnpceagnkjnjlbbbcepohejbheilk
  - edknjdjielmpdlnllkdmaghlbpnmjmgb
  - eidnihaadmmancegllknfbliaijfmkgo
  - ckiahbcmlmkpfiijecbpflfahoimklke
  - macdlemfnignjhclfcfichcdhiomgjjb
  - chioafkonnhbpajpengbalkececleldf
  - amnoibeflfphhplmckdbiajkjaoomgnj
  - llbhddikeonkpbhpncnhialfbpnilcnc
  - pcienlhnoficegnepejpfiklggkioccm
  - iocnglnmfkgfedpcemdflhkchokkfeii
  - igahhbkcppaollcjeaaoapkijbnphfhb
  - njpmifchgidinihmijhcfpbdmglecdlb
  - ggackgngljinccllcmbgnpgpllcjepgc
  - kchocjcihdgkoplngjemhpplmmloanja
  - bnijmipndnicefcdbhgcjoognndbgkep
  - lklekjodgannjcccdlbicoamibgbdnmi
  - dbdbnchagbkhknegmhgikkleoogjcfge
  - egblhcjfjmbjajhjhpmnlekffgaemgfh
  - ehbhfpfdkmhcpaehaooegfdflljcnfec
  - bkkgdjpomdnfemhhkalfkogckjdkcjkg
  - almalgbpmcfpdaopimbdchdliminoign
  - akkbkhnikoeojlhiiomohpdnkhbkhieh
  - gbfgfbopcfokdpkdigfmoeaajfmpkbnh
  - bniikohfmajhdcffljgfeiklcbgffppl
  - lejgfmmlngaigdmmikblappdafcmkndb
  - ffhhkmlgedgcliajaedapkdfigdobcif
  - gcknhkkoolaabfmlnjonogaaifnjlfnp
  - pooljnboifbodgifngpppfklhifechoe
  - fjoaledfpmneenckfbpdfhkmimnjocfa
  - aakchaleigkohafkfjfjbblobjifikek
  - dpplabbmogkhghncfbfdeeokoefdjegm
  - padekgcemlokbadohgkifijomclgjgif
  - bfidboloedlamgdmenmlbipfnccokknp
condition: all of chrome_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1133/T1133.md#atomic-test-1---running-chrome-vpn-extensions-via-the-registry-2-vpn-extension

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_chrome_extension.yml)
