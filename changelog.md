##  Commits in production - for 3 days, generated on: 2019-04-16 20:51:00 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=9066ae618a1e)|[Bug 1544858](https://bugzilla.mozilla.org/show_bug.cgi?id=1544858)  - [ci] Add '-e10s' back to task labels to satisfy SETA, r=jmaher CLOSED TREE Differential Revision: https://phabricator.services.mozilla.com/D27791|dluca@mozilla.com|jmaher|2019-04-16 23:10:54|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=8c63b67c8273)|[Bug 1544865](https://bugzilla.mozilla.org/show_bug.cgi?id=1544865)  - Build `dist-server` in the sccache toolchain job where available. r=nalexander Differential Revision: https://phabricator.services.mozilla.com/D27749|cmanchester@mozilla.com|nalexander|2019-04-16 20:11:25|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=11ec88883d98)|[Bug 1544521](https://bugzilla.mozilla.org/show_bug.cgi?id=1544521)  - Update the sccache revision used in our automation to the current master. r=nalexander Differential Revision: https://phabricator.services.mozilla.com/D27568|cmanchester@mozilla.com|nalexander|2019-04-16 19:53:09|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=638822e29d0d)|[Bug 1541436](https://bugzilla.mozilla.org/show_bug.cgi?id=1541436)  - remove unused file r=kats Differential Revision: https://phabricator.services.mozilla.com/D27697|dmitchell@mozilla.com|kats|2019-04-16 17:20:45|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=2b3d5e8d716d)|[Bug 1544473](https://bugzilla.mozilla.org/show_bug.cgi?id=1544473)  - remove screen resolution check from osx perf configs. r=rwood remove screen resolution check from os perf configs Differential Revision: https://phabricator.services.mozilla.com/D27687|jmaher@mozilla.com|rwood|2019-04-16 17:03:14|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=c6c39f570b1f)|[Bug 1541527](https://bugzilla.mozilla.org/show_bug.cgi?id=1541527)  - [ci] Remove unused raptor chrome group symbols, r=rwood Differential Revision: https://phabricator.services.mozilla.com/D27504|ahalberstadt@mozilla.com|rwood|2019-04-15 21:42:07|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=99e40003ff9a)|[Bug 1541527](https://bugzilla.mozilla.org/show_bug.cgi?id=1541527)  - Remove "-e10s" from treeherder group symbols and task labels, r=jmaher,gbrown Since e10s is the default configuration, we shouldn't explicitly mark things with the "-e10s" suffix. Instead we should mark things that *don't* run with 'e10s. This patch removes '-e10s' from all treeherder group symbols and task labels, adds the "-1proc" suffix to tasks that are non-e10s. Differential Revision: https://phabricator.services.mozilla.com/D25958|ahalberstadt@mozilla.com|jmaher,gbrown|2019-04-15 21:42:07|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=b8f49a14c458)|[Bug 1474897](https://bugzilla.mozilla.org/show_bug.cgi?id=1474897)  switch bitbar workers to g-w r=bc,tomprince Much of this was already reviewed in D21473 (my test change where I developed the payload modifications and that pointed tests at my test queue). This change keeps the payload changes from D21473, but points at the new 'real' queues we'll be using. Differential Revision: https://phabricator.services.mozilla.com/D25009|bclary@mozilla.com|bc,tomprince|2019-04-15 21:37:05|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=69d1e80c405d)|No Bug, taskcluster/docker/funsize-update-generator pipfile-update. r=sfraser Differential Revision: https://phabricator.services.mozilla.com/D27483|sfraser@mozilla.com|sfraser|2019-04-15 14:25:24|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=98df9bc51da2)|Backed out changeset f0ee3a81b179 [Bug 1538278](https://bugzilla.mozilla.org/show_bug.cgi?id=1538278)  for gecko decision task bustage CLOSED TREE|btara@mozilla.com||2019-04-15 13:35:35|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=f0ee3a81b179)|[Bug 1538278](https://bugzilla.mozilla.org/show_bug.cgi?id=1538278)  - Adds route for accessing geckoview releases r=tomprince,jlorenzo Adds route for accessing geckoview releases Differential Revision: https://phabricator.services.mozilla.com/D23928|mhentges@mozilla.com|tomprince,jlorenzo|2019-04-15 13:10:29|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=3d299e7104cd)|Backed out changeset 58593f23158c in order to trigger SETA (hit multiple of 5 last time)|ahalberstadt@mozilla.com||2019-04-16 22:55:25|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=549d05befaa0)|[Bug 1544858](https://bugzilla.mozilla.org/show_bug.cgi?id=1544858)  - [ci] Add '-e10s' back to task labels to satisfy SETA, r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D27791|ahalberstadt@mozilla.com|jmaher|2019-04-16 22:55:25|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=de85946fe255)|Backed out changeset 415d4eb9182a in order to trigger SETA|ahalberstadt@mozilla.com||2019-04-16 22:36:23|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=58593f23158c)|[Bug 1544858](https://bugzilla.mozilla.org/show_bug.cgi?id=1544858)  - [ci] Add '-e10s' back to task labels to satisfy SETA, r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D27791|ahalberstadt@mozilla.com|jmaher|2019-04-16 22:36:23|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=415d4eb9182a)|[Bug 1544858](https://bugzilla.mozilla.org/show_bug.cgi?id=1544858)  - [ci] Add '-e10s' back to task labels to satisfy SETA, r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D27791|ahalberstadt@mozilla.com|jmaher|2019-04-16 22:10:47|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=9463e541aa94)|[Bug 1538278](https://bugzilla.mozilla.org/show_bug.cgi?id=1538278)  - Adds route for accessing geckoview releases r=tomprince,jlorenzo Differential Revision: https://phabricator.services.mozilla.com/D23928|apavel@mozilla.com|tomprince,jlorenzo|2019-04-16 18:49:42|

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=9463e541aa94)|[Bug 1538278](https://bugzilla.mozilla.org/show_bug.cgi?id=1538278)  - Adds route for accessing geckoview releases r=tomprince,jlorenzo Differential Revision: https://phabricator.services.mozilla.com/D23928|apavel@mozilla.com|tomprince,jlorenzo|2019-04-16 18:43:40|

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
|[Link](https://github.com/taskcluster/taskcluster/commit/8b35f93a931ad5e673ad5374700173b22e48930d)|[UI] Adjust fetchPolicy for list of secrets (#588)|helfi92|N/A|2019-04-16 20:08:15|
|[Link](https://github.com/taskcluster/taskcluster/commit/ed10f541af2e38ce6df00b9cda3f7c4d87d51197)|[UI] Add spacing under spinner (#586)|helfi92|N/A|2019-04-16 18:58:49|
|[Link](https://github.com/taskcluster/taskcluster/commit/0d516ce098cb5376ebd193fd40023ae47e3fdf92)|[UI] Hide secret initially (#583)|helfi92|N/A|2019-04-16 18:55:49|
|[Link](https://github.com/taskcluster/taskcluster/commit/12f0f41ed486d55d2c9deb48443323b43f4295e5)|Merge pull request #585 from djmitche/bug1544601  Bug 1544601 - use correct table name for hooks|djmitche|N/A|2019-04-16 17:10:59|
|[Link](https://github.com/taskcluster/taskcluster/commit/5bee2f02782378d985890f4134a171df95ca4ca8)|Bug 1544601 - use correct table name for hooks|djmitche|N/A|2019-04-16 15:57:32|
|[Link](https://github.com/taskcluster/taskcluster/commit/23546f1b0c297f988d6f12b1bd1aba6722e804d7)|(hotfix) add whitespace|djmitche|N/A|2019-04-15 20:41:52|
|[Link](https://github.com/taskcluster/taskcluster/commit/d1c10072b5751bb995a040c3a64fe5944b7dbec1)|Merge pull request #572 from iFlameing/policy-docs  Add docs for collaborators_quiet policy|djmitche|N/A|2019-04-15 20:41:22|
|[Link](https://github.com/taskcluster/taskcluster/commit/c5dd4925ce575c5bba40bef3c60a1133d9834de8)|Merge pull request #569 from djmitche/stop-require-promise  Stop using the promise dependency|djmitche|N/A|2019-04-15 19:47:46|
|[Link](https://github.com/taskcluster/taskcluster/commit/0fb17720a305bc5d4fe1e0463088a310f36645fb)|latest build|djmitche|N/A|2019-04-15 19:43:50|
|[Link](https://github.com/taskcluster/taskcluster/commit/baccd899a12b581c3f7fd96594a234f59e0b38af)|Add docs for collaborators_quiet policy|iFlameing|N/A|2019-04-14 09:47:17|
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
|[Link](https://github.com/mozilla/release-services/commit/5d438f48891ad19ae5da4ecf833484227beeccce)|treestatus/api: adding statuspage sync (#2041)|garbas|N/A|2019-04-15 19:04:20|

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
|[Link](https://hg.mozilla.org/ci/ci-admin/pushloghtml?changeset=4a5c6ff8d56b)|[Bug 1544600](https://bugzilla.mozilla.org/show_bug.cgi?id=1544600)  - add modifier to remove hook bindings r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D27628|dmitchell@mozilla.com|tomprince|2019-04-16 19:11:20|
|[Link](https://hg.mozilla.org/ci/ci-admin/pushloghtml?changeset=172c211075a3)|[Bug 1544581](https://bugzilla.mozilla.org/show_bug.cgi?id=1544581)  - upgrade taskcluster client r=tomprince This also handles the case where a hookGroup does not exist. Differential Revision: https://phabricator.services.mozilla.com/D27620|dmitchell@mozilla.com|tomprince|2019-04-16 19:09:46|
|[Link](https://hg.mozilla.org/ci/ci-admin/pushloghtml?changeset=b211a777790e)|[Bug 1544581](https://bugzilla.mozilla.org/show_bug.cgi?id=1544581)  - fix failing tests from [Bug 1526979](https://bugzilla.mozilla.org/show_bug.cgi?id=1526979)  r=tomprince Depends on D27620 Differential Revision: https://phabricator.services.mozilla.com/D27621|dmitchell@mozilla.com|tomprince|2019-04-16 19:09:46|
