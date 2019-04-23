##  Commits in production - for 3 days, generated on: 2019-04-23 04:16:46 UTC.
|	OpenCloudConfig	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)|FIC - BOT|Self Generated| - |

|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=643d7793369e)|[Bug 1546100](https://bugzilla.mozilla.org/show_bug.cgi?id=1546100)  - [tryselect] Fix tools/tryselect/test/test_fuzzy.py, r=jmaher This was regressed by [Bug 1544816](https://bugzilla.mozilla.org/show_bug.cgi?id=1544816)  but the test never ran on the push that regressed. This patch also updates the 'files-changed' for the tryselect task. Differential Revision: https://phabricator.services.mozilla.com/D28386|ahalberstadt@mozilla.com|jmaher|2019-04-22 23:00:54|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=8cef878e7aa6)|[Bug 1546100](https://bugzilla.mozilla.org/show_bug.cgi?id=1546100)  - Turn off e10s for mochitest-a11y/chrome in task configuration (Backs out effa55bd84bb and 2f12958d4e8c), r=jmaher Turns out these suites were hardcoded to be non-e10s in the mochitest harness. So while it looked like they were working with e10s in treeherder, they were actually still running with it disabled. Turning e10s on causes both suites to permafail due to timeouts. Depends on D28386 Differential Revision: https://phabricator.services.mozilla.com/D28387|ahalberstadt@mozilla.com|jmaher|2019-04-22 23:00:54|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=8d1a81e59d2c)|No Bug, taskcluster/docker/funsize-update-generator pipfile-update. r=bhearsum Differential Revision: https://phabricator.services.mozilla.com/D28323|bhearsum@mozilla.com|bhearsum|2019-04-22 15:48:40|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=02cacfd48078)|[Bug 1544761](https://bugzilla.mozilla.org/show_bug.cgi?id=1544761)  Move tp6 tests to Tier 1 r=rwood Differential Revision: https://phabricator.services.mozilla.com/D28053|fstrugariu@mozilla.com|rwood|2019-04-22 14:23:23|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=70ebde4e0b6d)|[Bug 1545722](https://bugzilla.mozilla.org/show_bug.cgi?id=1545722)  remove raptor-tp6-8-404 jobs r=AlexandruIonescu Differential Revision: https://phabricator.services.mozilla.com/D28180|fstrugariu@mozilla.com|AlexandruIonescu|2019-04-22 14:21:56|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=3c1b4fc52fe2)|Backed out 4 changesets [Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562)  for wpt failures at allowed-to-play.html and event_play_noautoplay.html. Backed out changeset 64c05e3826cd [Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562)  Backed out changeset 00f60c8cf8fb [Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562)  Backed out changeset fddb75448c79 [Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562)  Backed out changeset a033f955b188 [Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562) |cbrindusan@mozilla.com||2019-04-22 14:13:30|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=a033f955b188)|[Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562)  - Run wpt against geckoview r=jgraham This patch leaves wpt running against fennec on androidx86 as tier2, adds wpt to run against geckoview testactivity on android x86_64 as tier3, and adds enough metadata to run_info_extras to help differentiate the two in expectation files. Fennec is "os == android and not e10s", while geckoview is "os == android and e10s". Differential Revision: https://phabricator.services.mozilla.com/D27182|james@hoppipolla.co.uk|jgraham|2019-04-22 12:17:37|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=8d1a81e59d2c)|No Bug, taskcluster/docker/funsize-update-generator pipfile-update. r=bhearsum Differential Revision: https://phabricator.services.mozilla.com/D28323|opoprus@mozilla.com|bhearsum|2019-04-23 01:19:22|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=a033f955b188)|[Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562)  - Run wpt against geckoview r=jgraham This patch leaves wpt running against fennec on androidx86 as tier2, adds wpt to run against geckoview testactivity on android x86_64 as tier3, and adds enough metadata to run_info_extras to help differentiate the two in expectation files. Fennec is "os == android and not e10s", while geckoview is "os == android and e10s". Differential Revision: https://phabricator.services.mozilla.com/D27182|shindli@mozilla.com|jgraham|2019-04-22 18:52:44|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=3c1b4fc52fe2)|Backed out 4 changesets [Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562)  for wpt failures at allowed-to-play.html and event_play_noautoplay.html. Backed out changeset 64c05e3826cd [Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562)  Backed out changeset 00f60c8cf8fb [Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562)  Backed out changeset fddb75448c79 [Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562)  Backed out changeset a033f955b188 [Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562) |shindli@mozilla.com||2019-04-22 18:52:44|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=70ebde4e0b6d)|[Bug 1545722](https://bugzilla.mozilla.org/show_bug.cgi?id=1545722)  remove raptor-tp6-8-404 jobs r=AlexandruIonescu Differential Revision: https://phabricator.services.mozilla.com/D28180|shindli@mozilla.com|AlexandruIonescu|2019-04-22 18:52:44|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=02cacfd48078)|[Bug 1544761](https://bugzilla.mozilla.org/show_bug.cgi?id=1544761)  Move tp6 tests to Tier 1 r=rwood Differential Revision: https://phabricator.services.mozilla.com/D28053|shindli@mozilla.com|rwood|2019-04-22 18:52:44|

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=8d1a81e59d2c)|No Bug, taskcluster/docker/funsize-update-generator pipfile-update. r=bhearsum Differential Revision: https://phabricator.services.mozilla.com/D28323|opoprus@mozilla.com|bhearsum|2019-04-23 00:46:44|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=a033f955b188)|[Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562)  - Run wpt against geckoview r=jgraham This patch leaves wpt running against fennec on androidx86 as tier2, adds wpt to run against geckoview testactivity on android x86_64 as tier3, and adds enough metadata to run_info_extras to help differentiate the two in expectation files. Fennec is "os == android and not e10s", while geckoview is "os == android and e10s". Differential Revision: https://phabricator.services.mozilla.com/D27182|shindli@mozilla.com|jgraham|2019-04-22 18:47:10|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=3c1b4fc52fe2)|Backed out 4 changesets [Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562)  for wpt failures at allowed-to-play.html and event_play_noautoplay.html. Backed out changeset 64c05e3826cd [Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562)  Backed out changeset 00f60c8cf8fb [Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562)  Backed out changeset fddb75448c79 [Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562)  Backed out changeset a033f955b188 [Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562) |shindli@mozilla.com||2019-04-22 18:47:10|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=70ebde4e0b6d)|[Bug 1545722](https://bugzilla.mozilla.org/show_bug.cgi?id=1545722)  remove raptor-tp6-8-404 jobs r=AlexandruIonescu Differential Revision: https://phabricator.services.mozilla.com/D28180|shindli@mozilla.com|AlexandruIonescu|2019-04-22 18:47:10|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=02cacfd48078)|[Bug 1544761](https://bugzilla.mozilla.org/show_bug.cgi?id=1544761)  Move tp6 tests to Tier 1 r=rwood Differential Revision: https://phabricator.services.mozilla.com/D28053|shindli@mozilla.com|rwood|2019-04-22 18:47:10|

|	mozilla-beta	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)|FIC - BOT|Self Generated| - |

|	version-control-tools	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/version-control-tools.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/version-control-tools.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/version-control-tools.md)|FIC - BOT|Self Generated| - |

|	relops-image-builder	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/relops-image-builder.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/relops-image-builder.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/relops-image-builder.md)|FIC - BOT|Self Generated| - |

|	relops-hardware-controller	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/relops-hardware-controller.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/relops-hardware-controller.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/relops-hardware-controller.md)|FIC - BOT|Self Generated| - |

|	ronin_puppet	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/ronin_puppet.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/ronin_puppet.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/ronin_puppet.md)|FIC - BOT|Self Generated| - |

|	mozilla-release	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)|FIC - BOT|Self Generated| - |

|	balrogscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/balrogscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/balrogscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/balrogscript.md)|FIC - BOT|Self Generated| - |

|	build-puppet	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla-releng/build-puppet/commit/5d412b5e4bd50973ae15ee4fb135ff7a72967eb2)|Merge pull request #456 from mitchhentges/focus-publish-nightly-fix  Updates mozapkpublisher to 2.0.2|mitchhentges|N/A|2019-04-22 15:16:24|
|[Link](https://github.com/mozilla-releng/build-puppet/commit/b5fd83b0e375d0f23bd1192d4293f9b45ed8c31c)|Updates mozapkpublisher to 2.0.2|mitchhentges|N/A|2019-04-22 14:56:37|

|	taskcluster	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/taskcluster/taskcluster/commit/fceee803b90809036399139f98a720e851d0e71d)|Worker Manager (#580)  Worker Manager|imbstack|N/A|2019-04-22 22:37:17|
|[Link](https://github.com/taskcluster/taskcluster/commit/38b385d9de55e9520e1e11e283eb32ddd23ad6f2)|Fix remaining review comments|imbstack|N/A|2019-04-22 20:53:37|
|[Link](https://github.com/taskcluster/taskcluster/commit/0fab3068782d651f60e632fb5652283a1af3cdb5)|Finish up most outstanding TODOs that won't be followed up in the next PR|imbstack|N/A|2019-04-22 20:20:40|
|[Link](https://github.com/taskcluster/taskcluster/commit/6bdb9f4bb99ce86c025316562bc41c6cb12197ca)|Nit: Sorting (#626)|helfi92|N/A|2019-04-22 15:43:58|
|[Link](https://github.com/taskcluster/taskcluster/commit/4fdd2516ea863b78778f00e02f3176852c6070d6)|Merge pull request #624 from helfi92/unused-dep  [UI] Remove unused dependency|helfi92|N/A|2019-04-22 12:51:17|
|[Link](https://github.com/taskcluster/taskcluster/commit/2c6ce455c180215850929de4ae1e9f77768a1aea)|Rename variant title to h6|helfi92|N/A|2019-04-22 12:35:34|
|[Link](https://github.com/taskcluster/taskcluster/commit/544e21d605d782804679e03528b55e81fe618a37)|Remove unused dependency|helfi92|N/A|2019-04-22 12:35:20|
|[Link](https://github.com/taskcluster/taskcluster/commit/47e624812b715d30fdee85f046df1b440ef05992)|docs: add arshadkazmi42 as a contributor (#623)    docs: update README.md      docs: update .all-contributorsrc|allcontributors[bot]|N/A|2019-04-22 12:22:01|
|[Link](https://github.com/taskcluster/taskcluster/commit/e1455538c5662c8f5a836e39f330b1c9cc1c3fbe)|[UI] Add top margin to headers in documentation (#613)|arshadkazmi42|N/A|2019-04-22 11:56:09|
|[Link](https://github.com/taskcluster/taskcluster/commit/298acb9efa4acfcf2654c43c5afdcd8c246df642)|[UI] Remove toggle effect from title on sidebar (#620)    [UI] Remove toggle effect from title on sidebar      Add requested changes|helfi92|N/A|2019-04-21 19:41:07|
|[Link](https://github.com/taskcluster/taskcluster/commit/fee4711e3933c5a89dde64e484729683a4412707)|Merge pull request #616 from djmitche/no-production-assume  Stop requiring assume() in production code|djmitche|N/A|2019-04-20 14:24:35|
|[Link](https://github.com/taskcluster/taskcluster/commit/5e4580068da24e36892fb958af722f7b3eafa7b3)|Merge pull request #615 from djmitche/bug1545265  Bug 1545265 - remove mention of pulse from purge-cache documentation|djmitche|N/A|2019-04-20 13:59:50|

|	beetmoverscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/beetmoverscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/beetmoverscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/beetmoverscript.md)|FIC - BOT|Self Generated| - |

|	addonscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/addonscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/addonscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/addonscript.md)|FIC - BOT|Self Generated| - |

|	pushsnapscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushsnapscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushsnapscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushsnapscript.md)|FIC - BOT|Self Generated| - |

|	pushapkscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushapkscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushapkscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushapkscript.md)|FIC - BOT|Self Generated| - |

|	shipitscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/shipitscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/shipitscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/shipitscript.md)|FIC - BOT|Self Generated| - |

|	bouncerscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/bouncerscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/bouncerscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/bouncerscript.md)|FIC - BOT|Self Generated| - |

|	scriptworker	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/scriptworker.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/scriptworker.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/scriptworker.md)|FIC - BOT|Self Generated| - |

|	treescript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)|FIC - BOT|Self Generated| - |

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

|	mozapkpublisher	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla-releng/mozapkpublisher/commit/49254cd61a4536206651424179a39e846d61d8b1)|2.0.2|mitchhentges|N/A|2019-04-22 14:36:01|
