##  Commits in production - for 3 days, generated on: 2019-04-22 03:56:31 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=4a10eafaa8ad)|[Bug 1544044](https://bugzilla.mozilla.org/show_bug.cgi?id=1544044)  - turn off duplicated raptor jobs on android, r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D28166|bclary@mozilla.com|jmaher|2019-04-19 15:44:11|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=0b1de782bd32)|Backed out changeset 2cc5bbbfe082 [Bug 1544758](https://bugzilla.mozilla.org/show_bug.cgi?id=1544758)  for Android 1proc failures|nerli@mozilla.com||2019-04-19 13:55:26|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=2cc5bbbfe082)|[Bug 1544758](https://bugzilla.mozilla.org/show_bug.cgi?id=1544758)  Perma tier 2 [taskcluster:error] exit status 1 r=Bebe,jmaher Differential Revision: https://phabricator.services.mozilla.com/D28184|fstrugariu@mozilla.com|Bebe,jmaher|2019-04-19 12:38:09|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=d23c0160234d)|[Bug 1544113](https://bugzilla.mozilla.org/show_bug.cgi?id=1544113)  - Adjust the treeherder 'tier' of some tier 3 tasks; r=jmaher Promote T(f) to tier 1. Promote MnM to tier 2. Differential Revision: https://phabricator.services.mozilla.com/D28141|gbrown@mozilla.com|jmaher|2019-04-19 07:07:28|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=4a10eafaa8ad)|[Bug 1544044](https://bugzilla.mozilla.org/show_bug.cgi?id=1544044)  - turn off duplicated raptor jobs on android, r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D28166|dluca@mozilla.com|jmaher|2019-04-20 00:51:54|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=9f70dad286ff)|[Bug 1545451](https://bugzilla.mozilla.org/show_bug.cgi?id=1545451)  - Disable sy-tp6 on code coverage builds, r=jmaher. Differential Revision: https://phabricator.services.mozilla.com/D28076|aiakab@mozilla.com|jmaher.|2019-04-19 12:50:22|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=1acac8b55cf7)|[Bug 1532747](https://bugzilla.mozilla.org/show_bug.cgi?id=1532747)  - Create try-only raptor tp6m-1 fenix task, r=rwood Differential Revision: https://phabricator.services.mozilla.com/D27948|aiakab@mozilla.com|rwood|2019-04-19 12:50:22|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=614d913a1657)|[Bug 1539932](https://bugzilla.mozilla.org/show_bug.cgi?id=1539932)  - [ci] Handle serviceworker/socketprocess test variants more generically, r=jmaher We are starting to spin off more and more "variants" of test suites. These are usually just duplicates of our pre-existing tasks, except with an additional pref set. Currently there are two variants (serviceworker-e10s and socketprocess-e10s), but a third will be added soon (fission). This change ensures we handle these types of requests in a consistent and well defined manner. It also splits tasks in a loop, so we don't accidentally risk combinatorial explosion. Variants should typically be reserved for very large changes that will impact the entire codebase (think e10s). Differential Revision: https://phabricator.services.mozilla.com/D28061|aiakab@mozilla.com|jmaher|2019-04-19 12:50:22|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=050964a5e03e)|[Bug 1545175](https://bugzilla.mozilla.org/show_bug.cgi?id=1545175)  - Raptor test definitions and taskcluster configs for cold page-load tests on Fenix; r=Bebe,jmaher Differential Revision: https://phabricator.services.mozilla.com/D27964|aiakab@mozilla.com|Bebe,jmaher|2019-04-19 12:50:22|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=d23c0160234d)|[Bug 1544113](https://bugzilla.mozilla.org/show_bug.cgi?id=1544113)  - Adjust the treeherder 'tier' of some tier 3 tasks; r=jmaher Promote T(f) to tier 1. Promote MnM to tier 2. Differential Revision: https://phabricator.services.mozilla.com/D28141|aiakab@mozilla.com|jmaher|2019-04-19 12:50:22|

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=4a10eafaa8ad)|[Bug 1544044](https://bugzilla.mozilla.org/show_bug.cgi?id=1544044)  - turn off duplicated raptor jobs on android, r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D28166|dluca@mozilla.com|jmaher|2019-04-20 00:44:39|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=9f70dad286ff)|[Bug 1545451](https://bugzilla.mozilla.org/show_bug.cgi?id=1545451)  - Disable sy-tp6 on code coverage builds, r=jmaher. Differential Revision: https://phabricator.services.mozilla.com/D28076|aiakab@mozilla.com|jmaher.|2019-04-19 12:47:45|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=1acac8b55cf7)|[Bug 1532747](https://bugzilla.mozilla.org/show_bug.cgi?id=1532747)  - Create try-only raptor tp6m-1 fenix task, r=rwood Differential Revision: https://phabricator.services.mozilla.com/D27948|aiakab@mozilla.com|rwood|2019-04-19 12:47:45|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=614d913a1657)|[Bug 1539932](https://bugzilla.mozilla.org/show_bug.cgi?id=1539932)  - [ci] Handle serviceworker/socketprocess test variants more generically, r=jmaher We are starting to spin off more and more "variants" of test suites. These are usually just duplicates of our pre-existing tasks, except with an additional pref set. Currently there are two variants (serviceworker-e10s and socketprocess-e10s), but a third will be added soon (fission). This change ensures we handle these types of requests in a consistent and well defined manner. It also splits tasks in a loop, so we don't accidentally risk combinatorial explosion. Variants should typically be reserved for very large changes that will impact the entire codebase (think e10s). Differential Revision: https://phabricator.services.mozilla.com/D28061|aiakab@mozilla.com|jmaher|2019-04-19 12:47:45|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=050964a5e03e)|[Bug 1545175](https://bugzilla.mozilla.org/show_bug.cgi?id=1545175)  - Raptor test definitions and taskcluster configs for cold page-load tests on Fenix; r=Bebe,jmaher Differential Revision: https://phabricator.services.mozilla.com/D27964|aiakab@mozilla.com|Bebe,jmaher|2019-04-19 12:47:45|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=d23c0160234d)|[Bug 1544113](https://bugzilla.mozilla.org/show_bug.cgi?id=1544113)  - Adjust the treeherder 'tier' of some tier 3 tasks; r=jmaher Promote T(f) to tier 1. Promote MnM to tier 2. Differential Revision: https://phabricator.services.mozilla.com/D28141|aiakab@mozilla.com|jmaher|2019-04-19 12:47:45|

|	mozilla-beta	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=9772de93a464)|[Bug 1436457](https://bugzilla.mozilla.org/show_bug.cgi?id=1436457)  - Add a group policy file to disable app updates, as those are handled by snapd. r=jlorenzo,mkaply a=release Differential Revision: https://phabricator.services.mozilla.com/D26281|jlorenzo@mozilla.com|jlorenzo,mkaply|2019-04-19 13:06:02|

|	mozilla-release	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)|FIC - BOT|Self Generated| - |

|	build-puppet	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla-releng/build-puppet/commit/e659387382dadd23de6c01c7e033ec2e3e639516)|Merge pull request #455 from MihaiTabara/appservices  Add appservices support. Bump scriptworker 23.0.2|MihaiTabara|N/A|2019-04-19 11:01:33|

|	OpenCloudConfig	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)|FIC - BOT|Self Generated| - |

|	taskcluster	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/taskcluster/taskcluster/commit/298acb9efa4acfcf2654c43c5afdcd8c246df642)|[UI] Remove toggle effect from title on sidebar (#620)    [UI] Remove toggle effect from title on sidebar      Add requested changes|helfi92|N/A|2019-04-21 19:41:07|
|[Link](https://github.com/taskcluster/taskcluster/commit/fee4711e3933c5a89dde64e484729683a4412707)|Merge pull request #616 from djmitche/no-production-assume  Stop requiring assume() in production code|djmitche|N/A|2019-04-20 14:24:35|
|[Link](https://github.com/taskcluster/taskcluster/commit/5e4580068da24e36892fb958af722f7b3eafa7b3)|Merge pull request #615 from djmitche/bug1545265  Bug 1545265 - remove mention of pulse from purge-cache documentation|djmitche|N/A|2019-04-20 13:59:50|
|[Link](https://github.com/taskcluster/taskcluster/commit/07bd0c82a1092a9cbdaed218da08cd7e3e7a00c5)|Merge pull request #597 from djmitche/bug1541741-b  Bug 1541741 - handle API methods that are sometimes public|djmitche|N/A|2019-04-19 19:59:25|
|[Link](https://github.com/taskcluster/taskcluster/commit/b47846d24da725244b8196c3fe3c19a7c911b032)|Merge pull request #614 from djmitche/bug1544608-b  Bug 1544608 - really, don't kill connection on channel errors|djmitche|N/A|2019-04-19 19:16:58|
|[Link](https://github.com/taskcluster/taskcluster/commit/ca334e50e438d8944ad9daa5d278fb8cb7a71033)|Merge pull request #612 from arshadkazmi42/payload-signature-api  Add payload in Signature in API Docs|djmitche|N/A|2019-04-19 17:53:53|
|[Link](https://github.com/taskcluster/taskcluster/commit/2e60f161431344f8a823c01c935878b9dfbaf2de)|Change to copy object as value|arshadkazmi42|N/A|2019-04-19 17:30:02|
|[Link](https://github.com/taskcluster/taskcluster/commit/13318aedf0c28743aae9e5a4c1acc6a373438b2e)|Check payload in parameters before pushing|arshadkazmi42|N/A|2019-04-19 17:22:18|
|[Link](https://github.com/taskcluster/taskcluster/commit/eb700c3b613c5c33663ab38b421e9651245f487d)|Merge pull request #611 from djmitche/bug1544608  Bug 1544608 - better handling for errors binding queues|djmitche|N/A|2019-04-19 16:18:36|
|[Link](https://github.com/taskcluster/taskcluster/commit/df22ff9e3e4e25203a3c8a853ec0a8a6151c3c8f)|adds payload in signature api docs|arshadkazmi42|N/A|2019-04-19 10:17:30|

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
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=0c84b2dde013)|[Bug 1545730](https://bugzilla.mozilla.org/show_bug.cgi?id=1545730)  - Allow Fenix to dep-sign APKs on master-push and PRs r=mtabara Allow Fenix to dep-sign APKs on master-push and PRs Differential Revision: https://phabricator.services.mozilla.com/D28181|jlorenzo@mozilla.com|mtabara|2019-04-19 12:07:37|

|	ci-admin	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)|FIC - BOT|Self Generated| - |
