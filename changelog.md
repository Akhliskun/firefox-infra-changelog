##  Commits in production - for 3 days, generated on: 2019-04-23 19:13:28 UTC.
|	OpenCloudConfig	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)|FIC - BOT|Self Generated| - |

|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=2b9ff41f9e37)|[Bug 1546113](https://bugzilla.mozilla.org/show_bug.cgi?id=1546113)  - switch to GCP balrog instance for staging releases r=rail Differential Revision: https://phabricator.services.mozilla.com/D28370|bhearsum@mozilla.com|rail|2019-04-23 21:47:16|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=6356a349f12f)|[Bug 1531876](https://bugzilla.mozilla.org/show_bug.cgi?id=1531876)  Only run talos-perf-reftest-singletons via try, on windows10-aarch64. r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D28500|sdonner@mozilla.com|jmaher|2019-04-23 18:49:59|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=176055665c32)|[Bug 1544360](https://bugzilla.mozilla.org/show_bug.cgi?id=1544360)  run talos-damp only on try, due to crashes. r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D28437|sdonner@mozilla.com|jmaher|2019-04-23 17:48:02|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=c9e17214f445)|[Bug 1501558](https://bugzilla.mozilla.org/show_bug.cgi?id=1501558)  - Move Android cppunit tests to 7.0 x86_64; r=jmaher Run cppunit on Android 7.0 instead of Android 4.3. Differential Revision: https://phabricator.services.mozilla.com/D28297|gbrown@mozilla.com|jmaher|2019-04-23 16:59:45|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=00c2b2449639)|[Bug 1523303](https://bugzilla.mozilla.org/show_bug.cgi?id=1523303)  - [taskgraph] Define suite "categories" rather than flavours task configs, r=gbrown Currently we have the concept of a "suite" and a "flavour" in our task configuration. Typically, the "suite" refers to the high-level test harness like "mochitest" or "reftest", whereas the flavour is more specific, e.g "browser-chrome-instrumentation" or "crashtest". However the line between suite and flavour is not applied with any semblance of consistency which results in inconsistent naming throughout the tree. This patch gets rid of the concept of "flavours" entirely (at least when it comes to task configuration). A suite is a type of test run, for example: - mochitest-plain - mochitest-devtools-chrome - mochitest-browser-chrome-instrumentation - jsreftest - reftest - firefox-ui-functional-remote etc There is no confusion here between suites and flavours because flavours don't exist. However, there are a couple of places where we *do* need to know what "test harness" is used to run a suite. These cases are: 1. For SCHEDULES moz.build rules 2. For the desktop_unittest.py mozharness script which takes arguments like --mochitest-suite=browser (this is not a compelling use of this information and should be refactored to work more like the android_emulator_unittest.py script) So to get this information, this patch introduces a new concept of a "category" which is the overall "test harness" that runs the suite. For many suites, the "category" is identical to the suite name. Unlike flavours, "categories" have no bearing on how we call or refer to the suite. Differential Revision: https://phabricator.services.mozilla.com/D27554|ahalberstadt@mozilla.com|gbrown|2019-04-23 16:49:04|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=60c512bab3e9)|[Bug 1523303](https://bugzilla.mozilla.org/show_bug.cgi?id=1523303)  - Align mozharness suite names with the ones in 'moztest.resolve', r=gbrown This officially makes 'moztest.resolve' the source of truth when it comes to suite names. It aligns that file with the names used in both the desktop_unittest and android_emulator_unittest scripts. Differential Revision: https://phabricator.services.mozilla.com/D27555|ahalberstadt@mozilla.com|gbrown|2019-04-23 16:49:04|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=80a5deca7438)|[Bug 1427849](https://bugzilla.mozilla.org/show_bug.cgi?id=1427849)  - Digitally sign geckodriver binaries on Windows and Linux r=aki Digitally sign geckodriver binaries on Windows and Linux Differential Revision: https://phabricator.services.mozilla.com/D28185|jlorenzo@mozilla.com|aki|2019-04-23 12:08:25|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=8d1a81e59d2c)|No Bug, taskcluster/docker/funsize-update-generator pipfile-update. r=bhearsum Differential Revision: https://phabricator.services.mozilla.com/D28323|bhearsum@mozilla.com|bhearsum|2019-04-22 15:48:40|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=02cacfd48078)|[Bug 1544761](https://bugzilla.mozilla.org/show_bug.cgi?id=1544761)  Move tp6 tests to Tier 1 r=rwood Differential Revision: https://phabricator.services.mozilla.com/D28053|fstrugariu@mozilla.com|rwood|2019-04-22 14:23:23|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=70ebde4e0b6d)|[Bug 1545722](https://bugzilla.mozilla.org/show_bug.cgi?id=1545722)  remove raptor-tp6-8-404 jobs r=AlexandruIonescu Differential Revision: https://phabricator.services.mozilla.com/D28180|fstrugariu@mozilla.com|AlexandruIonescu|2019-04-22 14:21:56|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=3c1b4fc52fe2)|Backed out 4 changesets [Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562)  for wpt failures at allowed-to-play.html and event_play_noautoplay.html. Backed out changeset 64c05e3826cd [Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562)  Backed out changeset 00f60c8cf8fb [Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562)  Backed out changeset fddb75448c79 [Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562)  Backed out changeset a033f955b188 [Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562) |cbrindusan@mozilla.com||2019-04-22 14:13:30|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=a033f955b188)|[Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562)  - Run wpt against geckoview r=jgraham This patch leaves wpt running against fennec on androidx86 as tier2, adds wpt to run against geckoview testactivity on android x86_64 as tier3, and adds enough metadata to run_info_extras to help differentiate the two in expectation files. Fennec is "os == android and not e10s", while geckoview is "os == android and e10s". Differential Revision: https://phabricator.services.mozilla.com/D27182|james@hoppipolla.co.uk|jgraham|2019-04-22 12:17:37|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=993dca7c302e)|[Bug 1538290](https://bugzilla.mozilla.org/show_bug.cgi?id=1538290)  [wpt PR 15946] - Use the checks API with taskcluster jobs, a=testonly Automatic update from web-platform-tests Use the checks API with taskcluster jobs -- wpt-commits: 6a2b8ebad7aeec36e693a03e60d6ce239eb74956 wpt-pr: 15946|james@hoppipolla.co.uk|testonly|2019-04-23 17:15:53|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=c68ee1d9e921)|[Bug 1534281](https://bugzilla.mozilla.org/show_bug.cgi?id=1534281)  [wpt PR 15724] - Move more Travis jobs to TaskCluster, a=testonly Automatic update from web-platform-tests Move more Travis jobs to TaskCluster -- Move all setup after clone to tools/ci/tc_run.py -- wpt-commits: 53e263d0d8297a02390d56c3d8f75ee82544780d, cc9980226202699835703082cdd4ccf62be91f8a wpt-pr: 15724|james@hoppipolla.co.uk|testonly|2019-04-23 17:15:53|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=84c9ed88a5e5)|[Bug 1504514](https://bugzilla.mozilla.org/show_bug.cgi?id=1504514)  [wpt PR 13902] - An incoming offer can generate simulcast, a=testonly Automatic update from web-platform-tests Avoid referring to self._data and self._path_hash everywhere This is hot code, and removing the slight indirection here is significant. -- fixup! Avoid referring to self._data and self._path_hash everywhere -- Put TaskCluster environment variables into the yml file This avoids escaping issues when the data contains unescaped shell special characters, notably ' but possibly also ` " $ ! and similar. -- wpt-commits: cc0904d7d6f067528786cedf7f581f2fc6a2bb53, 3c8e586dc068bf82429414a6610fe47729a464cf, e9e3f11de7472be4bd71d45d96f434872fd3f974 wpt-pr: 13902|james@hoppipolla.co.uk|testonly|2019-04-23 17:15:53|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=9e702bdd566c)|[Bug 1541460](https://bugzilla.mozilla.org/show_bug.cgi?id=1541460)  [wpt PR 16027] - Revert "Use the checks API with taskcluster jobs", a=testonly Automatic update from web-platform-tests Revert "Use the checks API with taskcluster jobs" This reverts commit 6a2b8ebad7aeec36e693a03e60d6ce239eb74956. -- wpt-commits: 967e4dd2487bf4c9d0db425f8eaf6d6e969be258 wpt-pr: 16027|james@hoppipolla.co.uk|testonly|2019-04-23 17:15:53|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=fea9dea2676f)|[Bug 1541481](https://bugzilla.mozilla.org/show_bug.cgi?id=1541481)  [wpt PR 16030] - Fix running full testsuites on master, a=testonly Automatic update from web-platform-tests Fix running full testsuites on master -- wpt-commits: 48070156dd14700631d4b713f8715e1477c31e95 wpt-pr: 16030|james@hoppipolla.co.uk|testonly|2019-04-23 17:15:53|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=9980646b6dd4)|[Bug 1539660](https://bugzilla.mozilla.org/show_bug.cgi?id=1539660)  [wpt PR 16066] - Don't use HEAD or FETCH_HEAD to checkout specific revisions., a=testonly Automatic update from web-platform-tests Don't use HEAD or FETCH_HEAD to checkout specific revisions. (#16066) FETCH_HEAD is unreliable because it's a global variable that can be accidentially clobbered by adding an additional fetch anywhere in the pipeline. As a result running tests in CI has been broken since we chose the wrong revisions. HEAD is more reliable but doesn't exist until we first check something out. Instead, do the following: * Fetch the initial commits into a branch called task_head and check this out unconditionally. * For PRs, create branches called base_head and pr_head pointing to the two parents of the merge commit that we test on PRs. * Express all the other revisions in terms of task_head, pr_head and base_head, since they are both correct and more descriptive than using complex revision specifiers. * Move as much logic as possible out of the script baked in to the docker image since that's hardest to update. -- wpt-commits: 856a95f08c3674cf34edbd15cf51d4fbffe84a5c wpt-pr: 16066|james@hoppipolla.co.uk|testonly|2019-04-23 17:15:53|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=478796294020)|[Bug 1540048](https://bugzilla.mozilla.org/show_bug.cgi?id=1540048)  [wpt PR 16101] - Revert "Don't use HEAD or FETCH_HEAD to checkout specific revisions.", a=testonly Automatic update from web-platform-tests Revert "Don't use HEAD or FETCH_HEAD to checkout specific revisions. (#16066)" (#16101) This reverts commit 856a95f08c3674cf34edbd15cf51d4fbffe84a5c. -- wpt-commits: fbd91b73ea03f23fffe4717556c088ae344c9501 wpt-pr: 16101|james@hoppipolla.co.uk|testonly|2019-04-23 17:15:53|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=ba8d6e98b620)|[Bug 1540306](https://bugzilla.mozilla.org/show_bug.cgi?id=1540306)  [wpt PR 16110] - Don't use HEAD or FETCH_HEAD to checkout specific revisions. (#16066), a=testonly Automatic update from web-platform-tests Don't use HEAD or FETCH_HEAD to checkout specific revisions. (#16066) FETCH_HEAD is unreliable because it's a global variable that can be accidentially clobbered by adding an additional fetch anywhere in the pipeline. As a result running tests in CI has been broken since we chose the wrong revisions. HEAD is more reliable but doesn't exist until we first check something out. Instead, do the following: * Fetch the initial commits into a branch called task_head and check this out unconditionally. * For PRs, create branches called base_head and pr_head pointing to the two parents of the merge commit that we test on PRs. * Express all the other revisions in terms of task_head, pr_head and base_head, since they are both correct and more descriptive than using complex revision specifiers. * Move as much logic as possible out of the script baked in to the docker image since that's hardest to update. -- wpt-commits: e5044ace1ad217e683fb239ce6f88806f05139e3 wpt-pr: 16110|james@hoppipolla.co.uk|testonly|2019-04-23 17:15:53|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=a033f955b188)|[Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562)  - Run wpt against geckoview r=jgraham This patch leaves wpt running against fennec on androidx86 as tier2, adds wpt to run against geckoview testactivity on android x86_64 as tier3, and adds enough metadata to run_info_extras to help differentiate the two in expectation files. Fennec is "os == android and not e10s", while geckoview is "os == android and e10s". Differential Revision: https://phabricator.services.mozilla.com/D27182|shindli@mozilla.com|jgraham|2019-04-22 18:52:44|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=3c1b4fc52fe2)|Backed out 4 changesets [Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562)  for wpt failures at allowed-to-play.html and event_play_noautoplay.html. Backed out changeset 64c05e3826cd [Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562)  Backed out changeset 00f60c8cf8fb [Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562)  Backed out changeset fddb75448c79 [Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562)  Backed out changeset a033f955b188 [Bug 1501562](https://bugzilla.mozilla.org/show_bug.cgi?id=1501562) |shindli@mozilla.com||2019-04-22 18:52:44|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=70ebde4e0b6d)|[Bug 1545722](https://bugzilla.mozilla.org/show_bug.cgi?id=1545722)  remove raptor-tp6-8-404 jobs r=AlexandruIonescu Differential Revision: https://phabricator.services.mozilla.com/D28180|shindli@mozilla.com|AlexandruIonescu|2019-04-22 18:52:44|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=02cacfd48078)|[Bug 1544761](https://bugzilla.mozilla.org/show_bug.cgi?id=1544761)  Move tp6 tests to Tier 1 r=rwood Differential Revision: https://phabricator.services.mozilla.com/D28053|shindli@mozilla.com|rwood|2019-04-22 18:52:44|

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=643d7793369e)|[Bug 1546100](https://bugzilla.mozilla.org/show_bug.cgi?id=1546100)  - [tryselect] Fix tools/tryselect/test/test_fuzzy.py, r=jmaher This was regressed by [Bug 1544816](https://bugzilla.mozilla.org/show_bug.cgi?id=1544816)  but the test never ran on the push that regressed. This patch also updates the 'files-changed' for the tryselect task. Differential Revision: https://phabricator.services.mozilla.com/D28386|dvarga@mozilla.com|jmaher|2019-04-23 12:53:27|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=8cef878e7aa6)|[Bug 1546100](https://bugzilla.mozilla.org/show_bug.cgi?id=1546100)  - Turn off e10s for mochitest-a11y/chrome in task configuration (Backs out effa55bd84bb and 2f12958d4e8c), r=jmaher Turns out these suites were hardcoded to be non-e10s in the mochitest harness. So while it looked like they were working with e10s in treeherder, they were actually still running with it disabled. Turning e10s on causes both suites to permafail due to timeouts. Depends on D28386 Differential Revision: https://phabricator.services.mozilla.com/D28387|dvarga@mozilla.com|jmaher|2019-04-23 12:53:27|
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
|[Link](https://github.com/taskcluster/taskcluster/commit/a6344990b57912a1da8bc2c4c65f15deda356bac)|update docker image|djmitche|N/A|2019-04-23 18:09:04|
|[Link](https://github.com/taskcluster/taskcluster/commit/e420e0b648b4ce81e5a9ef3e88d37ce59f09fa8d)|Merge pull request #625 from helfi92/workers-not-displaying  Bug 1545857 - Workers not displaying|helfi92|N/A|2019-04-23 17:29:21|
|[Link](https://github.com/taskcluster/taskcluster/commit/9350f9d8ff7d69920bf50f3fcf4f092d07593b13)|Merge pull request #617 from djmitche/bug1526705  Bug 1526705 - await workerinfo updates|djmitche|N/A|2019-04-23 17:18:16|
|[Link](https://github.com/taskcluster/taskcluster/commit/eca9d6b6c5f60c3042d915c362b90811570260d5)|Add fetchPolicy network-only to task view (#628)|helfi92|N/A|2019-04-23 15:29:53|
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
|[Link](https://github.com/mozilla-releng/build-cloud-tools/commit/e08a2a542121bf3ffda8aa2b1a552a673f4f34a1)|terraform: Fix releng stuff (#382)    Revert "Revert "terraform: move static pages to cloudops managed S3 buckets" (#380)"    This reverts commit b73e56f18956ce705d70741a20181eec552ba211.      already exists|garbas|N/A|2019-04-23 17:13:45|
|[Link](https://github.com/mozilla-releng/build-cloud-tools/commit/55518a745b7076ea407cc96d860594363777dbbe)|Add root . to moztools hosted zone name (#381)|dividehex|N/A|2019-04-23 15:40:34|
|[Link](https://github.com/mozilla-releng/build-cloud-tools/commit/b73e56f18956ce705d70741a20181eec552ba211)|Revert "terraform: move static pages to cloudops managed S3 buckets" (#380)|rail|N/A|2019-04-23 15:08:25|
|[Link](https://github.com/mozilla-releng/build-cloud-tools/commit/88d853fd79dd41b11f957d8ba571ba39eee6149a)|Merge pull request #379 from garbas/releng-frontend-cloudops  terraform: move static pages to cloudops managed S3 buckets|garbas|N/A|2019-04-23 11:16:50|
|[Link](https://github.com/mozilla-releng/build-cloud-tools/commit/a65be299b354707fdc2f0253b178c152d4a2e200)|terraform: point to cloudfront instances under cloudops account|garbas|N/A|2019-04-23 11:10:28|

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
|[Link](https://github.com/mozilla-releng/mozapkpublisher/commit/49254cd61a4536206651424179a39e846d61d8b1)|2.0.2|mitchhentges|N/A|2019-04-22 14:36:01|
|[Link](https://github.com/mozilla-releng/mozapkpublisher/commit/49254cd61a4536206651424179a39e846d61d8b1)|2.0.2|mitchhentges|N/A|2019-04-22 14:36:01|
|[Link](https://github.com/mozilla-releng/mozapkpublisher/commit/49254cd61a4536206651424179a39e846d61d8b1)|2.0.2|mitchhentges|N/A|2019-04-22 14:36:01|
