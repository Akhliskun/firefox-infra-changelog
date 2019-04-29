##  Commits in production - for 3 days, generated on: 2019-04-29 05:50:54 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=dfadeda46370)|[Bug 1545500](https://bugzilla.mozilla.org/show_bug.cgi?id=1545500)  - Add Win32 SM(p) jobs back for 32-bit jit-test coverage. r=sfink,jmaher Differential Revision: https://phabricator.services.mozilla.com/D28830|jdemooij@mozilla.com|sfink,jmaher|2019-04-28 21:16:49|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=28e4375e491e)|Backed out changeset 8218cc92ee8d for docker images builds failures CLOSED TREE|btara@mozilla.com||2019-04-28 03:34:16|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=4c994bf99569)|[Bug 1544986](https://bugzilla.mozilla.org/show_bug.cgi?id=1544986)  - Fall back more gracefully when TASKCLUSTER_WORKER_GROUP is not set. r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D27841|mh@glandium.org|tomprince|2019-04-28 02:35:20|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=ebe9a3ca4b17)|[Bug 1545344](https://bugzilla.mozilla.org/show_bug.cgi?id=1545344)  - Don't change current directory when executing a command via run-task. r=tomprince Currently, all things running via run-task don't really care that the current directory is set to /. However, on generic-worker, many things assume the current directory is the task directory, which varies by task, and wrapping them with run-task fails because it resets the current directory. Differential Revision: https://phabricator.services.mozilla.com/D28018|mh@glandium.org|tomprince|2019-04-28 02:35:20|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=a584e4e9473f)|[Bug 1545368](https://bugzilla.mozilla.org/show_bug.cgi?id=1545368)  - Support fetches in run-task on generic-worker. r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D28048|mh@glandium.org|tomprince|2019-04-28 02:35:20|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=8c3a37a0a53e)|[Bug 1546870](https://bugzilla.mozilla.org/show_bug.cgi?id=1546870)  - Package win*-rust toolchains as .tar.xz. r=froydnj This uniformizes the artifact name across platforms. We may want to do the same for other toolchains, but it bears the question whether xz is reliably available on users' Windows machines, while it doesn't matter for rust, since mach bootstrap pulls it with rustup rather than from automation, contrary to other toolchains. Differential Revision: https://phabricator.services.mozilla.com/D28780|mh@glandium.org|froydnj|2019-04-28 02:35:20|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=c8d4031fcf80)|[Bug 1547272](https://bugzilla.mozilla.org/show_bug.cgi?id=1547272)  - ensure windows10-aarch64 is set to tier 2 for talos-bcv. r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D29003|sdonner@mozilla.com|jmaher|2019-04-26 19:31:21|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=dfadeda46370)|[Bug 1545500](https://bugzilla.mozilla.org/show_bug.cgi?id=1545500)  - Add Win32 SM(p) jobs back for 32-bit jit-test coverage. r=sfink,jmaher Differential Revision: https://phabricator.services.mozilla.com/D28830|rgurzau@mozilla.com|sfink,jmaher|2019-04-29 01:00:01|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=c8d4031fcf80)|[Bug 1547272](https://bugzilla.mozilla.org/show_bug.cgi?id=1547272)  - ensure windows10-aarch64 is set to tier 2 for talos-bcv. r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D29003|aiakab@mozilla.com|jmaher|2019-04-27 01:08:15|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=716e89455efe)|[Bug 1547044](https://bugzilla.mozilla.org/show_bug.cgi?id=1547044)  Properly set windows10-aarch64 tests to tier 2. r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D28887|rmaries@mozilla.com|jmaher|2019-04-26 12:59:41|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=f534de537db5)|[Bug 1546610](https://bugzilla.mozilla.org/show_bug.cgi?id=1546610)  - reduce marionette-headless to run on linux64/shippable as tier2 only. r=whimboo reduce marionette-headless to run on linux64/shippable as tier2 only Differential Revision: https://phabricator.services.mozilla.com/D28838|rmaries@mozilla.com|whimboo|2019-04-26 12:59:41|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=9879ab660a34)|[Bug 1250737](https://bugzilla.mozilla.org/show_bug.cgi?id=1250737)  - Update android mozharness 'chunked' handling, for jittest; r=bc It turns out there are several places where the change to suite 'jittest-chunked' causes problem. I am abandoning that approach. Desktop uses this trick, and this returns android '-chunked' handling to a state similar to what it was before I started messing around! Differential Revision: https://phabricator.services.mozilla.com/D28897|rmaries@mozilla.com|bc|2019-04-26 12:59:41|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=27527aa56004)|[Bug 1540082](https://bugzilla.mozilla.org/show_bug.cgi?id=1540082)  - add a `toolchain-arm64-build` docker image; r=nalexander We need this image for building clang on machines with arm64 sysroots. (Note that this image *is* a linux x86-64 image, just with some arm64 cross-compilation packages available.) Differential Revision: https://phabricator.services.mozilla.com/D28404|rmaries@mozilla.com|nalexander|2019-04-26 12:59:41|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=6cbad9f5b259)|[Bug 1540082](https://bugzilla.mozilla.org/show_bug.cgi?id=1540082)  - add an aarch64-cross clang build; r=nalexander Analogously to the existing `linux64-clang-8-android-cross` build, this build is a linux x86-64 build with runtime library support for aarch64. Depends on D28405 Differential Revision: https://phabricator.services.mozilla.com/D28406|rmaries@mozilla.com|nalexander|2019-04-26 12:59:41|

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=dfadeda46370)|[Bug 1545500](https://bugzilla.mozilla.org/show_bug.cgi?id=1545500)  - Add Win32 SM(p) jobs back for 32-bit jit-test coverage. r=sfink,jmaher Differential Revision: https://phabricator.services.mozilla.com/D28830|rgurzau@mozilla.com|sfink,jmaher|2019-04-29 00:55:07|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=c8d4031fcf80)|[Bug 1547272](https://bugzilla.mozilla.org/show_bug.cgi?id=1547272)  - ensure windows10-aarch64 is set to tier 2 for talos-bcv. r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D29003|aiakab@mozilla.com|jmaher|2019-04-27 01:02:33|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=716e89455efe)|[Bug 1547044](https://bugzilla.mozilla.org/show_bug.cgi?id=1547044)  Properly set windows10-aarch64 tests to tier 2. r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D28887|rmaries@mozilla.com|jmaher|2019-04-26 12:46:15|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=f534de537db5)|[Bug 1546610](https://bugzilla.mozilla.org/show_bug.cgi?id=1546610)  - reduce marionette-headless to run on linux64/shippable as tier2 only. r=whimboo reduce marionette-headless to run on linux64/shippable as tier2 only Differential Revision: https://phabricator.services.mozilla.com/D28838|rmaries@mozilla.com|whimboo|2019-04-26 12:46:15|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=9879ab660a34)|[Bug 1250737](https://bugzilla.mozilla.org/show_bug.cgi?id=1250737)  - Update android mozharness 'chunked' handling, for jittest; r=bc It turns out there are several places where the change to suite 'jittest-chunked' causes problem. I am abandoning that approach. Desktop uses this trick, and this returns android '-chunked' handling to a state similar to what it was before I started messing around! Differential Revision: https://phabricator.services.mozilla.com/D28897|rmaries@mozilla.com|bc|2019-04-26 12:46:15|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=27527aa56004)|[Bug 1540082](https://bugzilla.mozilla.org/show_bug.cgi?id=1540082)  - add a `toolchain-arm64-build` docker image; r=nalexander We need this image for building clang on machines with arm64 sysroots. (Note that this image *is* a linux x86-64 image, just with some arm64 cross-compilation packages available.) Differential Revision: https://phabricator.services.mozilla.com/D28404|rmaries@mozilla.com|nalexander|2019-04-26 12:46:15|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=6cbad9f5b259)|[Bug 1540082](https://bugzilla.mozilla.org/show_bug.cgi?id=1540082)  - add an aarch64-cross clang build; r=nalexander Analogously to the existing `linux64-clang-8-android-cross` build, this build is a linux x86-64 build with runtime library support for aarch64. Depends on D28405 Differential Revision: https://phabricator.services.mozilla.com/D28406|rmaries@mozilla.com|nalexander|2019-04-26 12:46:15|

|	mozilla-beta	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)|FIC - BOT|Self Generated| - |

|	version-control-tools	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/version-control-tools.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/version-control-tools.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/hgcustom/version-control-tools/pushloghtml?changeset=0ec322c77f23)|hgserver: add `sparserevlog` capability to `test-obsolescence-server.t` [Bug 1547276](https://bugzilla.mozilla.org/show_bug.cgi?id=1547276) |cosheehan@mozilla.com||2019-04-26 18:21:03|
|[Link](https://hg.mozilla.org/hgcustom/version-control-tools/pushloghtml?changeset=58286127f121)|hgserver: add `sparserevlog` bundle requirement to `test-clonebundles.t` [Bug 1547276](https://bugzilla.mozilla.org/show_bug.cgi?id=1547276)  New bundles under 4.9.1 include the `sparserevlog` requirement. Since none of the repos on hgmo are in the `sparserevlog` format yet, this is just extra test output we need to add. It doesn't affect behaviour in any way.|cosheehan@mozilla.com||2019-04-26 18:21:03|
|[Link](https://hg.mozilla.org/hgcustom/version-control-tools/pushloghtml?changeset=e8a3e082d629)|hgserver: add `reposetup` timing output to `test-push-basic.t` blackbox logs [Bug 1547276](https://bugzilla.mozilla.org/show_bug.cgi?id=1547276)  Mercurial 4.9.1 now includes repo setup timing information in blackbox logs, which we have yet to add to the tests.|cosheehan@mozilla.com||2019-04-26 18:21:03|

|	relops-image-builder	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/relops-image-builder.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/relops-image-builder.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/relops-image-builder.md)|FIC - BOT|Self Generated| - |

|	OpenCloudConfig	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)|FIC - BOT|Self Generated| - |

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
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.md)|FIC - BOT|Self Generated| - |

|	taskcluster	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/taskcluster/taskcluster/commit/18434828e8ea28b34d29f2af19d0236fa2d7b386)|Merge pull request #641 from djmitche/bug1542405  Bug 1542405 - update tc-github handler tests to use new fake pulse support|djmitche|N/A|2019-04-28 18:19:37|
|[Link](https://github.com/taskcluster/taskcluster/commit/118fbb5f3cad5fb8924af27437d25fac9e17f328)|[UI] Improve favicons (#601)    add new accessible favicons      remove shadow      new logoRunning svg      redesign icons with mask      adjust cutoff point and green checkmark      adjust logoCompleted      new logo favicons      adjust T width in logos      replace non favicon logo.png|projectyang|N/A|2019-04-26 12:41:45|
|[Link](https://github.com/taskcluster/taskcluster/commit/453e8f8e48532778b8f45afa9d7c1dd3f513f7a8)|Merge pull request #638 from djmitche/bug1547000  Bug 1547000 - don't show diffs for generated files|djmitche|N/A|2019-04-26 12:35:33|
|[Link](https://github.com/taskcluster/taskcluster/commit/b4f7b84e80c43efc02fc79d5bc10889cadf2b07f)|Bug 1547000 - don't show diffs for generated files  Note that these files are still shown in a PR, just without the line-by-line diff -- much like `yarn.lock` is already.  Note, too, that this does not cover files which are  edited  by yarn generate, such as `package.json` or the READMEs.  Diffs in those files will appear in PRs as expected.|djmitche|N/A|2019-04-26 12:28:00|

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
|[Link](https://github.com/mozilla-releng/pushapkscript/commit/87f2148a487bbc8df53a970006faeb437bbb815d)|1.0.2|mitchhentges|N/A|2019-04-26 14:57:52|
|[Link](https://github.com/mozilla-releng/pushapkscript/commit/87f2148a487bbc8df53a970006faeb437bbb815d)|1.0.2|mitchhentges|N/A|2019-04-26 14:57:52|
|[Link](https://github.com/mozilla-releng/pushapkscript/commit/87f2148a487bbc8df53a970006faeb437bbb815d)|1.0.2|mitchhentges|N/A|2019-04-26 14:57:52|
|[Link](https://github.com/mozilla-releng/pushapkscript/commit/87f2148a487bbc8df53a970006faeb437bbb815d)|1.0.2|mitchhentges|N/A|2019-04-26 14:57:52|
|[Link](https://github.com/mozilla-releng/pushapkscript/commit/87f2148a487bbc8df53a970006faeb437bbb815d)|1.0.2|mitchhentges|N/A|2019-04-26 14:57:52|
|[Link](https://github.com/mozilla-releng/pushapkscript/commit/87f2148a487bbc8df53a970006faeb437bbb815d)|1.0.2|mitchhentges|N/A|2019-04-26 14:57:52|

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
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.md)|FIC - BOT|Self Generated| - |
