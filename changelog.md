##  Commits in production - for 3 days, generated on: 2019-04-15 18:10:36 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=fdbd2c02f391)|[Bug 1516114](https://bugzilla.mozilla.org/show_bug.cgi?id=1516114)  - Enable 3-tier PGO for Linux; r=firefox-build-system-reviewers,Callek,chmanchester Now that 3-tier PGO uses a debian9 image to generate the profile data [Bug 1519424](https://bugzilla.mozilla.org/show_bug.cgi?id=1519424)  we no longer see the XDG_RUNTIME_DIR failures in the run task. The frequency of those errors was the primary blocker for enabling 3-tier PGO in the first place. Since we still see those errors occasionally in 1-tier PGO, we should switch to the 3-tier model for Linux. Differential Revision: https://phabricator.services.mozilla.com/D27326|mshal@mozilla.com|firefox-build-system-reviewers,Callek,chmanchester|2019-04-15 20:20:06|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=69d1e80c405d)|No Bug, taskcluster/docker/funsize-update-generator pipfile-update. r=sfraser Differential Revision: https://phabricator.services.mozilla.com/D27483|sfraser@mozilla.com|sfraser|2019-04-15 14:25:24|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=98df9bc51da2)|Backed out changeset f0ee3a81b179 [Bug 1538278](https://bugzilla.mozilla.org/show_bug.cgi?id=1538278)  for gecko decision task bustage CLOSED TREE|btara@mozilla.com||2019-04-15 13:35:35|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=f0ee3a81b179)|[Bug 1538278](https://bugzilla.mozilla.org/show_bug.cgi?id=1538278)  - Adds route for accessing geckoview releases r=tomprince,jlorenzo Adds route for accessing geckoview releases Differential Revision: https://phabricator.services.mozilla.com/D23928|mhentges@mozilla.com|tomprince,jlorenzo|2019-04-15 13:10:29|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=cbd247c21a3e)|[Bug 1543915](https://bugzilla.mozilla.org/show_bug.cgi?id=1543915)  - Move installer_url and test_packages_url to EXTRA_MOZHARNESS_CONFIG. r=tomprince This allows to stop using task-reference for mozharness_test commands. Differential Revision: https://phabricator.services.mozilla.com/D27236|mh@glandium.org|tomprince|2019-04-13 00:13:27|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=ce6ffba148da)|[Bug 1544062](https://bugzilla.mozilla.org/show_bug.cgi?id=1544062)  - Run windows/aarch64 xpcshell in 3 chunks; r=egao Reduce chunks from 8 to 3. Each test task has at least a couple of minutes of overhead, so fewer chunks improves overall efficiency. At 3 chunks, each one still completes reasonably quickly (less than 20 minutes). Differential Revision: https://phabricator.services.mozilla.com/D27339|gbrown@mozilla.com|egao|2019-04-12 21:20:27|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=5d2e9236aa79)|[Bug 1543993](https://bugzilla.mozilla.org/show_bug.cgi?id=1543993)  - Run remaining Talos ccov tasks only on try; r=jmaher Stop running Tss(tp6) and T(bcv) on ccov builds on central -- the remaining 2 cases missed in the previous bug. Differential Revision: https://phabricator.services.mozilla.com/D27313|gbrown@mozilla.com|jmaher|2019-04-12 19:28:02|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=483960ad2be2)|[Bug 1318091](https://bugzilla.mozilla.org/show_bug.cgi?id=1318091)  - Add Android 7.0 gtest tasks; r=bc Add Android 7.0 gtests, opt and debug, running against the geckoview TestRunnerActivity. Differential Revision: https://phabricator.services.mozilla.com/D27016|gbrown@mozilla.com|bc|2019-04-12 18:16:32|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=f0ee3a81b179)|[Bug 1538278](https://bugzilla.mozilla.org/show_bug.cgi?id=1538278)  - Adds route for accessing geckoview releases r=tomprince,jlorenzo Adds route for accessing geckoview releases Differential Revision: https://phabricator.services.mozilla.com/D23928|ncsoregi@mozilla.com|tomprince,jlorenzo|2019-04-15 18:29:43|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=98df9bc51da2)|Backed out changeset f0ee3a81b179 [Bug 1538278](https://bugzilla.mozilla.org/show_bug.cgi?id=1538278)  for gecko decision task bustage CLOSED TREE|ncsoregi@mozilla.com||2019-04-15 18:29:43|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=7a209bab1bfe)|[Bug 1543662](https://bugzilla.mozilla.org/show_bug.cgi?id=1543662)  Introduce channel verification to partials r=catlee Differential Revision: https://phabricator.services.mozilla.com/D27115|shindli@mozilla.com|catlee|2019-04-12 19:20:17|

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=f0ee3a81b179)|[Bug 1538278](https://bugzilla.mozilla.org/show_bug.cgi?id=1538278)  - Adds route for accessing geckoview releases r=tomprince,jlorenzo Adds route for accessing geckoview releases Differential Revision: https://phabricator.services.mozilla.com/D23928|ncsoregi@mozilla.com|tomprince,jlorenzo|2019-04-15 18:24:06|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=98df9bc51da2)|Backed out changeset f0ee3a81b179 [Bug 1538278](https://bugzilla.mozilla.org/show_bug.cgi?id=1538278)  for gecko decision task bustage CLOSED TREE|ncsoregi@mozilla.com||2019-04-15 18:24:06|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=7a209bab1bfe)|[Bug 1543662](https://bugzilla.mozilla.org/show_bug.cgi?id=1543662)  Introduce channel verification to partials r=catlee Differential Revision: https://phabricator.services.mozilla.com/D27115|shindli@mozilla.com|catlee|2019-04-12 18:46:45|

|	mozilla-beta	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=2eec72aa8607)|[Bug 1520261](https://bugzilla.mozilla.org/show_bug.cgi?id=1520261)  - Let ARM64 Fennec ride the trains to Beta r=mhentges a=release Let ARM64 Fennec ride the trains to Beta Differential Revision: https://phabricator.services.mozilla.com/D26736|jlorenzo@mozilla.com|mhentges|2019-04-15 11:29:13|

|	mozilla-release	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)|FIC - BOT|Self Generated| - |

|	build-puppet	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla-releng/build-puppet/commit/fa8adf4b90272790e46c34faf891b00a81876c91)|Bump {mozapkpublisher,pushapkscript} to {2.0.1,1.0.1} (#451)|JohanLorenzo|N/A|2019-04-15 08:30:17|

|	OpenCloudConfig	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)|FIC - BOT|Self Generated| - |

|	taskcluster	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/taskcluster/taskcluster/commit/19cae6c62318b9edd2dc6917fdb3039a86996dd0)|Merge pull request #579 from helfi92/hotfix-taskid  [UI] Fix task ID undefined|helfi92|N/A|2019-04-15 15:12:51|
|[Link](https://github.com/taskcluster/taskcluster/commit/357589a7eac78221507ad613b8fdb15101f12308)|Hot fix: fix task ID undefined|helfi92|N/A|2019-04-15 15:11:07|
|[Link](https://github.com/taskcluster/taskcluster/commit/45711a4d273c94fa2a341e973c21cf6a338f1eca)|Merge pull request #570 from helfi92/task-run-reordering  Task Group UX (breadcrumbs, hide metadata)|helfi92|N/A|2019-04-15 14:45:24|
|[Link](https://github.com/taskcluster/taskcluster/commit/d1e2b33d347d408850d1b4947424014c67bc01fd)|Add TaskGroup suggestions|helfi92|N/A|2019-04-15 14:40:38|
|[Link](https://github.com/taskcluster/taskcluster/commit/177748ff79c1b7c0daf60c075cc9b458e3791b4c)|Fix hashing issue in docs when viewing an entry log (#571)|helfi92|N/A|2019-04-15 14:34:18|
|[Link](https://github.com/taskcluster/taskcluster/commit/fd837dfde1cce4e813c054c41091f9c1d57bc519)|Merge pull request #477 from helfi92/task-group-subscription  [UI] Task Group - use a subscription model instead of polling|helfi92|N/A|2019-04-15 14:30:51|
|[Link](https://github.com/taskcluster/taskcluster/commit/65b4545681af2857b50a79561e12789088fe8eaf)|Merge pull request #576 from taskcluster/renovate/xmlbuilder-12.x  Update dependency xmlbuilder to v12|djmitche|N/A|2019-04-15 14:29:38|
|[Link](https://github.com/taskcluster/taskcluster/commit/e8184926176eed12f9011571c021be1e74784c30)|[UI] Fix calendar icon positioning on date picker (#568)|helfi92|N/A|2019-04-15 14:14:31|
|[Link](https://github.com/taskcluster/taskcluster/commit/9ca9d115b9e2bfed16c63849944c9d185d34fad5)|Update dependency graphql-type-json to ^0.3.0 (#574)|renovate[bot]|N/A|2019-04-15 13:56:45|
|[Link](https://github.com/taskcluster/taskcluster/commit/d91ced93f8b6bfb5d62fad41b4d762b6d5132895)|Merge pull request #573 from taskcluster/renovate/cron-parser-2.x  Update dependency cron-parser to v2.11.0|djmitche|N/A|2019-04-15 02:11:47|
|[Link](https://github.com/taskcluster/taskcluster/commit/776b12749e94bce891082e7813b384e6fd09d67e)|Update dependency cron-parser to v2.11.0|renovate-bot|N/A|2019-04-15 00:41:17|
|[Link](https://github.com/taskcluster/taskcluster/commit/13104aabcc4be20d38f9defdb5e8c65434a9c57b)|Merge pull request #327 from iFlameing/yml  Bug[1446768] Adding new policy in .taskcluster.yml|djmitche|N/A|2019-04-12 18:19:27|

|	addonscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/addonscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/addonscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/addonscript.md)|FIC - BOT|Self Generated| - |

|	balrogscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/balrogscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/balrogscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/balrogscript.md)|FIC - BOT|Self Generated| - |

|	beetmoverscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/beetmoverscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/beetmoverscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/beetmoverscript.md)|FIC - BOT|Self Generated| - |

|	bouncerscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/bouncerscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/bouncerscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/bouncerscript.md)|FIC - BOT|Self Generated| - |

|	pushapkscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushapkscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushapkscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushapkscript.md)|FIC - BOT|Self Generated| - |

|	pushsnapscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushsnapscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushsnapscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushsnapscript.md)|FIC - BOT|Self Generated| - |

|	scriptworker	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/scriptworker.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/scriptworker.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/scriptworker.md)|FIC - BOT|Self Generated| - |

|	shipitscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/shipitscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/shipitscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/shipitscript.md)|FIC - BOT|Self Generated| - |

|	signingscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signingscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signingscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signingscript.md)|FIC - BOT|Self Generated| - |

|	signtool	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signtool.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signtool.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signtool.md)|FIC - BOT|Self Generated| - |

|	treescript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)|FIC - BOT|Self Generated| - |

|	mozapkpublisher	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.md)|FIC - BOT|Self Generated| - |

|	services	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/services.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/services.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/services.md)|FIC - BOT|Self Generated| - |

|	build-cloud-tools	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-cloud-tools.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-cloud-tools.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-cloud-tools.md)|FIC - BOT|Self Generated| - |

|	ci-configuration	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.md)|FIC - BOT|Self Generated| - |

|	ci-admin	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)|FIC - BOT|Self Generated| - |
