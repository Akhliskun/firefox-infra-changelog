##  Commits in production - for 3 days, generated on: 2019-04-28 05:40:55 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=2ce05675c447)|[Bug 1545810](https://bugzilla.mozilla.org/show_bug.cgi?id=1545810)  - disable tests in testing/web-platform/meta/media-source/ on windows10-aarch64 that cause task to abort r=jmaher Changes: - disable wholesale the `media-source` subsuite within web-platform-test Attempts were made to isolate the tests that cause the test harness to lock up with a permission issue on `Ahem.ttf` however the attempts were unsuccessful in isolating the tests to a manageable set. It appears the solution is to simply stop running `media-source` tests on windows10-aarch64 as that seems to have solved the problem in a previous try run. Differential Revision: https://phabricator.services.mozilla.com/D28778|egao@mozilla.com|jmaher|2019-04-28 06:22:33|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=28e4375e491e)|Backed out changeset 8218cc92ee8d for docker images builds failures CLOSED TREE|btara@mozilla.com||2019-04-28 03:34:16|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=4c994bf99569)|[Bug 1544986](https://bugzilla.mozilla.org/show_bug.cgi?id=1544986)  - Fall back more gracefully when TASKCLUSTER_WORKER_GROUP is not set. r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D27841|mh@glandium.org|tomprince|2019-04-28 02:35:20|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=ebe9a3ca4b17)|[Bug 1545344](https://bugzilla.mozilla.org/show_bug.cgi?id=1545344)  - Don't change current directory when executing a command via run-task. r=tomprince Currently, all things running via run-task don't really care that the current directory is set to /. However, on generic-worker, many things assume the current directory is the task directory, which varies by task, and wrapping them with run-task fails because it resets the current directory. Differential Revision: https://phabricator.services.mozilla.com/D28018|mh@glandium.org|tomprince|2019-04-28 02:35:20|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=a584e4e9473f)|[Bug 1545368](https://bugzilla.mozilla.org/show_bug.cgi?id=1545368)  - Support fetches in run-task on generic-worker. r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D28048|mh@glandium.org|tomprince|2019-04-28 02:35:20|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=8c3a37a0a53e)|[Bug 1546870](https://bugzilla.mozilla.org/show_bug.cgi?id=1546870)  - Package win*-rust toolchains as .tar.xz. r=froydnj This uniformizes the artifact name across platforms. We may want to do the same for other toolchains, but it bears the question whether xz is reliably available on users' Windows machines, while it doesn't matter for rust, since mach bootstrap pulls it with rustup rather than from automation, contrary to other toolchains. Differential Revision: https://phabricator.services.mozilla.com/D28780|mh@glandium.org|froydnj|2019-04-28 02:35:20|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=c8d4031fcf80)|[Bug 1547272](https://bugzilla.mozilla.org/show_bug.cgi?id=1547272)  - ensure windows10-aarch64 is set to tier 2 for talos-bcv. r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D29003|sdonner@mozilla.com|jmaher|2019-04-26 19:31:21|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=9879ab660a34)|[Bug 1250737](https://bugzilla.mozilla.org/show_bug.cgi?id=1250737)  - Update android mozharness 'chunked' handling, for jittest; r=bc It turns out there are several places where the change to suite 'jittest-chunked' causes problem. I am abandoning that approach. Desktop uses this trick, and this returns android '-chunked' handling to a state similar to what it was before I started messing around! Differential Revision: https://phabricator.services.mozilla.com/D28897|gbrown@mozilla.com|bc|2019-04-26 02:01:34|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=716e89455efe)|[Bug 1547044](https://bugzilla.mozilla.org/show_bug.cgi?id=1547044)  Properly set windows10-aarch64 tests to tier 2. r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D28887|sdonner@mozilla.com|jmaher|2019-04-25 23:39:08|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=4243e8a01b2e)|[Bug 1546858](https://bugzilla.mozilla.org/show_bug.cgi?id=1546858)  - Force the wpt manifest job to rebuild the manifest, r=Aryx If we use the downloaded manifest then any bug that leads to an error in the manifest may be propogated forward. Instead force the manifest to be built from scratch in CI. Differential Revision: https://phabricator.services.mozilla.com/D28809|rgurzau@mozilla.com|Aryx|2019-04-25 19:31:07|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=8218cc92ee8d)|No bug: Handle unicode output from docker builds; r=dustin This is not strictly required in mozilla-central, as `mach` sets the encoding of the output to UTF-8. Differential Revision: https://phabricator.services.mozilla.com/D28861|mozilla@hocat.ca|dustin|2019-04-25 19:05:37|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=18ba664cbccf)|[Bug 1546452](https://bugzilla.mozilla.org/show_bug.cgi?id=1546452)  - Run fewer headless mochitests; r=jmaher - stop mochitest-headless on windows10 - stop mochitest-headless on linux64/debug - make mochitest-headless tier-2 - make mochitest-headless run on m-c/try Differential Revision: https://phabricator.services.mozilla.com/D28715|gbrown@mozilla.com|jmaher|2019-04-25 15:35:01|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=ce1c928fb0cd)|[Bug 1546100](https://bugzilla.mozilla.org/show_bug.cgi?id=1546100)  - [mochitest] Error out when running 'a11y' or 'chrome' with e10s, r=jmaher Previously we would silently change the value of "e10s" from False to True. This can cause confusion and lead people to falsely think mochitest-chrome/a11y work with e10s (they do not). Now we explicitly error out in this case. This might be slightly less convenient for the developer (e.g they might need to re-run the command), but the downside of needing to rerun a test command is less than the risk of misunderstanding what is being tested. Note: when running |mach test| or |mach mochitest| on a directory that contains both chrome/a11y and another suite, we'll still do the right thing and implicitly set "e10s=False". Differential Revision: https://phabricator.services.mozilla.com/D28538|nbeleuzu@mozilla.com|jmaher|2019-04-27 12:55:23|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=c8d4031fcf80)|[Bug 1547272](https://bugzilla.mozilla.org/show_bug.cgi?id=1547272)  - ensure windows10-aarch64 is set to tier 2 for talos-bcv. r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D29003|aiakab@mozilla.com|jmaher|2019-04-27 01:08:15|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=716e89455efe)|[Bug 1547044](https://bugzilla.mozilla.org/show_bug.cgi?id=1547044)  Properly set windows10-aarch64 tests to tier 2. r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D28887|rmaries@mozilla.com|jmaher|2019-04-26 12:59:41|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=f534de537db5)|[Bug 1546610](https://bugzilla.mozilla.org/show_bug.cgi?id=1546610)  - reduce marionette-headless to run on linux64/shippable as tier2 only. r=whimboo reduce marionette-headless to run on linux64/shippable as tier2 only Differential Revision: https://phabricator.services.mozilla.com/D28838|rmaries@mozilla.com|whimboo|2019-04-26 12:59:41|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=9879ab660a34)|[Bug 1250737](https://bugzilla.mozilla.org/show_bug.cgi?id=1250737)  - Update android mozharness 'chunked' handling, for jittest; r=bc It turns out there are several places where the change to suite 'jittest-chunked' causes problem. I am abandoning that approach. Desktop uses this trick, and this returns android '-chunked' handling to a state similar to what it was before I started messing around! Differential Revision: https://phabricator.services.mozilla.com/D28897|rmaries@mozilla.com|bc|2019-04-26 12:59:41|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=27527aa56004)|[Bug 1540082](https://bugzilla.mozilla.org/show_bug.cgi?id=1540082)  - add a `toolchain-arm64-build` docker image; r=nalexander We need this image for building clang on machines with arm64 sysroots. (Note that this image *is* a linux x86-64 image, just with some arm64 cross-compilation packages available.) Differential Revision: https://phabricator.services.mozilla.com/D28404|rmaries@mozilla.com|nalexander|2019-04-26 12:59:41|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=6cbad9f5b259)|[Bug 1540082](https://bugzilla.mozilla.org/show_bug.cgi?id=1540082)  - add an aarch64-cross clang build; r=nalexander Analogously to the existing `linux64-clang-8-android-cross` build, this build is a linux x86-64 build with runtime library support for aarch64. Depends on D28405 Differential Revision: https://phabricator.services.mozilla.com/D28406|rmaries@mozilla.com|nalexander|2019-04-26 12:59:41|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=7e4f89f8eafe)|[Bug 1546728](https://bugzilla.mozilla.org/show_bug.cgi?id=1546728)  - enable cppunittest for windows10-aarch64 r=gbrown Differential Revision: https://phabricator.services.mozilla.com/D28700|btara@mozilla.com|gbrown|2019-04-25 12:52:28|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=6f64c339a2a8)|[Bug 1506928](https://bugzilla.mozilla.org/show_bug.cgi?id=1506928)  - [mozharness] Handle KeyboardInterrupt in ScriptMixin. r=gbrown Differential Revision: https://phabricator.services.mozilla.com/D25749|btara@mozilla.com|gbrown|2019-04-25 12:52:28|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=8e4422d0040f)|[Bug 1546373](https://bugzilla.mozilla.org/show_bug.cgi?id=1546373)  - [ci] Update fenix try tasks to new index, r=rwood Differential Revision: https://phabricator.services.mozilla.com/D28716|btara@mozilla.com|rwood|2019-04-25 12:52:28|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=62218e6b1c11)|[Bug 1546113](https://bugzilla.mozilla.org/show_bug.cgi?id=1546113)  - Update public balrog api endpoint for stage r=Callek Differential Revision: https://phabricator.services.mozilla.com/D28711|btara@mozilla.com|Callek|2019-04-25 12:52:28|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=dc42ae4e7a3a)|[Bug 1546732](https://bugzilla.mozilla.org/show_bug.cgi?id=1546732)  - enable jittest for windows10-aarch64 r=gbrown Differential Revision: https://phabricator.services.mozilla.com/D28704|btara@mozilla.com|gbrown|2019-04-25 12:52:28|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=1fae6818d4e4)|[Bug 1492695](https://bugzilla.mozilla.org/show_bug.cgi?id=1492695)  - Fix android-hw jittest suite name to avoid timeouts; r=bc I still haven't managed to verify this on try, but it seems like the best explanation for the timeouts. Differential Revision: https://phabricator.services.mozilla.com/D28762|btara@mozilla.com|bc|2019-04-25 12:52:28|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=006af3739e10)|[Bug 1546845](https://bugzilla.mozilla.org/show_bug.cgi?id=1546845)  - Remove separate win64-aarch64 rust toolchain. r=nalexander It was necessary when it was a different version than win64-rust, but that's not the case anymore. Differential Revision: https://phabricator.services.mozilla.com/D28761|btara@mozilla.com|nalexander|2019-04-25 12:52:28|

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=ce1c928fb0cd)|[Bug 1546100](https://bugzilla.mozilla.org/show_bug.cgi?id=1546100)  - [mochitest] Error out when running 'a11y' or 'chrome' with e10s, r=jmaher Previously we would silently change the value of "e10s" from False to True. This can cause confusion and lead people to falsely think mochitest-chrome/a11y work with e10s (they do not). Now we explicitly error out in this case. This might be slightly less convenient for the developer (e.g they might need to re-run the command), but the downside of needing to rerun a test command is less than the risk of misunderstanding what is being tested. Note: when running |mach test| or |mach mochitest| on a directory that contains both chrome/a11y and another suite, we'll still do the right thing and implicitly set "e10s=False". Differential Revision: https://phabricator.services.mozilla.com/D28538|nbeleuzu@mozilla.com|jmaher|2019-04-27 12:45:52|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=c8d4031fcf80)|[Bug 1547272](https://bugzilla.mozilla.org/show_bug.cgi?id=1547272)  - ensure windows10-aarch64 is set to tier 2 for talos-bcv. r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D29003|aiakab@mozilla.com|jmaher|2019-04-27 01:02:33|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=716e89455efe)|[Bug 1547044](https://bugzilla.mozilla.org/show_bug.cgi?id=1547044)  Properly set windows10-aarch64 tests to tier 2. r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D28887|rmaries@mozilla.com|jmaher|2019-04-26 12:46:15|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=f534de537db5)|[Bug 1546610](https://bugzilla.mozilla.org/show_bug.cgi?id=1546610)  - reduce marionette-headless to run on linux64/shippable as tier2 only. r=whimboo reduce marionette-headless to run on linux64/shippable as tier2 only Differential Revision: https://phabricator.services.mozilla.com/D28838|rmaries@mozilla.com|whimboo|2019-04-26 12:46:15|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=9879ab660a34)|[Bug 1250737](https://bugzilla.mozilla.org/show_bug.cgi?id=1250737)  - Update android mozharness 'chunked' handling, for jittest; r=bc It turns out there are several places where the change to suite 'jittest-chunked' causes problem. I am abandoning that approach. Desktop uses this trick, and this returns android '-chunked' handling to a state similar to what it was before I started messing around! Differential Revision: https://phabricator.services.mozilla.com/D28897|rmaries@mozilla.com|bc|2019-04-26 12:46:15|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=27527aa56004)|[Bug 1540082](https://bugzilla.mozilla.org/show_bug.cgi?id=1540082)  - add a `toolchain-arm64-build` docker image; r=nalexander We need this image for building clang on machines with arm64 sysroots. (Note that this image *is* a linux x86-64 image, just with some arm64 cross-compilation packages available.) Differential Revision: https://phabricator.services.mozilla.com/D28404|rmaries@mozilla.com|nalexander|2019-04-26 12:46:15|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=6cbad9f5b259)|[Bug 1540082](https://bugzilla.mozilla.org/show_bug.cgi?id=1540082)  - add an aarch64-cross clang build; r=nalexander Analogously to the existing `linux64-clang-8-android-cross` build, this build is a linux x86-64 build with runtime library support for aarch64. Depends on D28405 Differential Revision: https://phabricator.services.mozilla.com/D28406|rmaries@mozilla.com|nalexander|2019-04-26 12:46:15|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=7e4f89f8eafe)|[Bug 1546728](https://bugzilla.mozilla.org/show_bug.cgi?id=1546728)  - enable cppunittest for windows10-aarch64 r=gbrown Differential Revision: https://phabricator.services.mozilla.com/D28700|btara@mozilla.com|gbrown|2019-04-25 12:46:25|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=6f64c339a2a8)|[Bug 1506928](https://bugzilla.mozilla.org/show_bug.cgi?id=1506928)  - [mozharness] Handle KeyboardInterrupt in ScriptMixin. r=gbrown Differential Revision: https://phabricator.services.mozilla.com/D25749|btara@mozilla.com|gbrown|2019-04-25 12:46:25|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=8e4422d0040f)|[Bug 1546373](https://bugzilla.mozilla.org/show_bug.cgi?id=1546373)  - [ci] Update fenix try tasks to new index, r=rwood Differential Revision: https://phabricator.services.mozilla.com/D28716|btara@mozilla.com|rwood|2019-04-25 12:46:25|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=62218e6b1c11)|[Bug 1546113](https://bugzilla.mozilla.org/show_bug.cgi?id=1546113)  - Update public balrog api endpoint for stage r=Callek Differential Revision: https://phabricator.services.mozilla.com/D28711|btara@mozilla.com|Callek|2019-04-25 12:46:25|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=dc42ae4e7a3a)|[Bug 1546732](https://bugzilla.mozilla.org/show_bug.cgi?id=1546732)  - enable jittest for windows10-aarch64 r=gbrown Differential Revision: https://phabricator.services.mozilla.com/D28704|btara@mozilla.com|gbrown|2019-04-25 12:46:25|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=1fae6818d4e4)|[Bug 1492695](https://bugzilla.mozilla.org/show_bug.cgi?id=1492695)  - Fix android-hw jittest suite name to avoid timeouts; r=bc I still haven't managed to verify this on try, but it seems like the best explanation for the timeouts. Differential Revision: https://phabricator.services.mozilla.com/D28762|btara@mozilla.com|bc|2019-04-25 12:46:25|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=006af3739e10)|[Bug 1546845](https://bugzilla.mozilla.org/show_bug.cgi?id=1546845)  - Remove separate win64-aarch64 rust toolchain. r=nalexander It was necessary when it was a different version than win64-rust, but that's not the case anymore. Differential Revision: https://phabricator.services.mozilla.com/D28761|btara@mozilla.com|nalexander|2019-04-25 12:46:25|

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
|[Link](https://github.com/mozilla-releng/build-puppet/commit/8df8e9b8abde8ccd815c1d97ffb0dab8a1dce917)|Merge pull request #460 from mozilla-releng/pyup-scheduled-update-2019-04-24  Scheduled weekly dependency update for week 16|mutterroland|N/A|2019-04-25 14:42:33|

|	taskcluster	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/taskcluster/taskcluster/commit/118fbb5f3cad5fb8924af27437d25fac9e17f328)|[UI] Improve favicons (#601)    add new accessible favicons      remove shadow      new logoRunning svg      redesign icons with mask      adjust cutoff point and green checkmark      adjust logoCompleted      new logo favicons      adjust T width in logos      replace non favicon logo.png|projectyang|N/A|2019-04-26 12:41:45|
|[Link](https://github.com/taskcluster/taskcluster/commit/453e8f8e48532778b8f45afa9d7c1dd3f513f7a8)|Merge pull request #638 from djmitche/bug1547000  Bug 1547000 - don't show diffs for generated files|djmitche|N/A|2019-04-26 12:35:33|
|[Link](https://github.com/taskcluster/taskcluster/commit/b4f7b84e80c43efc02fc79d5bc10889cadf2b07f)|Bug 1547000 - don't show diffs for generated files  Note that these files are still shown in a PR, just without the line-by-line diff -- much like `yarn.lock` is already.  Note, too, that this does not cover files which are  edited  by yarn generate, such as `package.json` or the READMEs.  Diffs in those files will appear in PRs as expected.|djmitche|N/A|2019-04-26 12:28:00|
|[Link](https://github.com/taskcluster/taskcluster/commit/74ffd9583ce7b4be2b1c83869380cba45d9fb2ae)|Merge pull request #634 from helfi92/docs-404-links  Fix: Links in documentation|helfi92|N/A|2019-04-25 17:52:03|
|[Link](https://github.com/taskcluster/taskcluster/commit/37428e673a2e9c2e6172dcd2e1fc840ac380495d)|Merge pull request #618 from OjaswinM/change-denylist-scope  [Bug 1542212] Change denylist scope and rename list()|djmitche|N/A|2019-04-25 15:30:55|
|[Link](https://github.com/taskcluster/taskcluster/commit/fb9116f05b49fb85aa6bc667b42eb2f88a57f189)|Add links to taskcluster worker implementation|helfi92|N/A|2019-04-25 13:34:28|
|[Link](https://github.com/taskcluster/taskcluster/commit/3a8cba73511dc8a57db5fae6f7336c26f074b879)|Fix: Links in documentation|helfi92|N/A|2019-04-25 13:07:42|

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
