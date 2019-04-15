##  Commits in production - for 3 days, generated on: 2019-04-15 03:02:47 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=f4c8925d83ed)|[Bug 1543044](https://bugzilla.mozilla.org/show_bug.cgi?id=1543044)  - ensure high_value_tasks has a default value when we fail to get data from treeherder/seta. r=Callek ensure high_value_tasks has a default value when we fail to get data from treeherder/seta. Differential Revision: https://phabricator.services.mozilla.com/D27445|jmaher@mozilla.com|Callek|2019-04-14 20:51:36|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=cbd247c21a3e)|[Bug 1543915](https://bugzilla.mozilla.org/show_bug.cgi?id=1543915)  - Move installer_url and test_packages_url to EXTRA_MOZHARNESS_CONFIG. r=tomprince This allows to stop using task-reference for mozharness_test commands. Differential Revision: https://phabricator.services.mozilla.com/D27236|mh@glandium.org|tomprince|2019-04-13 00:13:27|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=ce6ffba148da)|[Bug 1544062](https://bugzilla.mozilla.org/show_bug.cgi?id=1544062)  - Run windows/aarch64 xpcshell in 3 chunks; r=egao Reduce chunks from 8 to 3. Each test task has at least a couple of minutes of overhead, so fewer chunks improves overall efficiency. At 3 chunks, each one still completes reasonably quickly (less than 20 minutes). Differential Revision: https://phabricator.services.mozilla.com/D27339|gbrown@mozilla.com|egao|2019-04-12 21:20:27|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=5d2e9236aa79)|[Bug 1543993](https://bugzilla.mozilla.org/show_bug.cgi?id=1543993)  - Run remaining Talos ccov tasks only on try; r=jmaher Stop running Tss(tp6) and T(bcv) on ccov builds on central -- the remaining 2 cases missed in the previous bug. Differential Revision: https://phabricator.services.mozilla.com/D27313|gbrown@mozilla.com|jmaher|2019-04-12 19:28:02|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=483960ad2be2)|[Bug 1318091](https://bugzilla.mozilla.org/show_bug.cgi?id=1318091)  - Add Android 7.0 gtest tasks; r=bc Add Android 7.0 gtests, opt and debug, running against the geckoview TestRunnerActivity. Differential Revision: https://phabricator.services.mozilla.com/D27016|gbrown@mozilla.com|bc|2019-04-12 18:16:32|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=60a4738fdc31)|[Bug 1520261](https://bugzilla.mozilla.org/show_bug.cgi?id=1520261)  - Let ARM64 Fennec ride the trains to Beta r=mhentges Let ARM64 Fennec ride the trains to Beta Differential Revision: https://phabricator.services.mozilla.com/D26736|jlorenzo@mozilla.com|mhentges|2019-04-12 16:57:30|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=6800e99ad32a)|[Bug 1539437](https://bugzilla.mozilla.org/show_bug.cgi?id=1539437)  - Replace Chrome with Chromium mentionings where needed r=sparky,davehunt Differential Revision: https://phabricator.services.mozilla.com/D25094|igoldan@mozilla.com|sparky,davehunt|2019-04-12 16:43:02|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=7a209bab1bfe)|[Bug 1543662](https://bugzilla.mozilla.org/show_bug.cgi?id=1543662)  Introduce channel verification to partials r=catlee Differential Revision: https://phabricator.services.mozilla.com/D27115|sfraser@mozilla.com|catlee|2019-04-12 15:19:41|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=a632dfa60af6)|[Bug 1543895](https://bugzilla.mozilla.org/show_bug.cgi?id=1543895)  - Move test-platform keying of fetches in tests to individual fetch types. r=tomprince So, instead of fetches['by-test-platform']['fetch'], we have fetches['fetch']['by-test-platform']. Differential Revision: https://phabricator.services.mozilla.com/D27227|mh@glandium.org|tomprince|2019-04-12 09:19:00|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=0d76e1701610)|[Bug 1541823](https://bugzilla.mozilla.org/show_bug.cgi?id=1541823)  - Derive the fetch docker image from debian9-raw rather than debian9-base. r=dustin This will make the image smaller, and will make it happen earlier in cases its dependencies need to be rebuilt. Differential Revision: https://phabricator.services.mozilla.com/D26082|csabou@mozilla.com|dustin|2019-04-12 06:48:25|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=940684cd1065)|[Bug 1543826](https://bugzilla.mozilla.org/show_bug.cgi?id=1543826)  - Remove duplication of key "linux64-ccov/.*" in mapping to fix yaml failure.|csabou@mozilla.com||2019-04-12 03:04:51|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=f4c8925d83ed)|[Bug 1543044](https://bugzilla.mozilla.org/show_bug.cgi?id=1543044)  - ensure high_value_tasks has a default value when we fail to get data from treeherder/seta. r=Callek ensure high_value_tasks has a default value when we fail to get data from treeherder/seta. Differential Revision: https://phabricator.services.mozilla.com/D27445|nbeleuzu@mozilla.com|Callek|2019-04-15 00:52:28|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=7a209bab1bfe)|[Bug 1543662](https://bugzilla.mozilla.org/show_bug.cgi?id=1543662)  Introduce channel verification to partials r=catlee Differential Revision: https://phabricator.services.mozilla.com/D27115|shindli@mozilla.com|catlee|2019-04-12 19:20:17|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=a632dfa60af6)|[Bug 1543895](https://bugzilla.mozilla.org/show_bug.cgi?id=1543895)  - Move test-platform keying of fetches in tests to individual fetch types. r=tomprince So, instead of fetches['by-test-platform']['fetch'], we have fetches['fetch']['by-test-platform']. Differential Revision: https://phabricator.services.mozilla.com/D27227|shindli@mozilla.com|tomprince|2019-04-12 12:36:35|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=c91bf0806ef7)|[Bug 1543033](https://bugzilla.mozilla.org/show_bug.cgi?id=1543033)  Fix pathing for win64_aarch64_info.txt r=mtabara I've refactored the artifact map generation slightly to make the list of platforms more flexible, and also to let us have the previous name for win64_aarch64_info.txt. Differential Revision: https://phabricator.services.mozilla.com/D27049|csabou@mozilla.com|mtabara|2019-04-12 06:51:12|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=82d83ff9faca)|[Bug 1543558](https://bugzilla.mozilla.org/show_bug.cgi?id=1543558)  - Increase max-run-time for linux shippable builds; r=jmaher Avoid intermittent timeouts: increase max-run-time to 2.5 hours to account for normal variability in run time. Differential Revision: https://phabricator.services.mozilla.com/D27017|csabou@mozilla.com|jmaher|2019-04-12 06:51:12|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=1ce8b8034950)|[Bug 1536804](https://bugzilla.mozilla.org/show_bug.cgi?id=1536804)  - Add a task for summarising wpt metadata, r=ahal This task runs on wpt metadata changes and uploads an artifact containing the summarised metadata. Depends on D24178 Depends on D24178 Differential Revision: https://phabricator.services.mozilla.com/D24179|csabou@mozilla.com|ahal|2019-04-12 06:51:12|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=a498ba7a0992)|[Bug 1534463](https://bugzilla.mozilla.org/show_bug.cgi?id=1534463)  give tasks access to `hgmointernal` Taskcluster secret r=tomprince Now that we have added the necessary scopes to `ci-configuration`, we can add the in-tree scopes to give tasks access to the `hgmointernal` config Taskcluster secret. Differential Revision: https://phabricator.services.mozilla.com/D25001|csabou@mozilla.com|tomprince|2019-04-12 06:51:12|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=3595f2b4875f)|[Bug 1534463](https://bugzilla.mozilla.org/show_bug.cgi?id=1534463)  patch `run-task` to clone from private hgweb mirrors r=tomprince With tasks able to access the hgmointernal config from a Taskcluster secret, we can now add functionality to `run-task` to support checking out from the private hg service. Here we add add a `resolve_checkout_url` function which takes the base/head repository URLs and determines whether we should clone from the public or private service, returning the resolved URL. The function pulls down the secret and checks that the region the task is executing in is in the set of supported regions. Then we generate a random number and default to the public service if the number is lower than our "rate". If all the above conditions are met, we replace `hg.mozilla.org` with the resolved domain name for the given region. We add a call to this function to `collect_vcs_options`, and skip resolving the private URL if we aren't performing a checkout from within `run-task`. Differential Revision: https://phabricator.services.mozilla.com/D25002|csabou@mozilla.com|tomprince|2019-04-12 06:51:12|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=ef120e802c6f)|[Bug 1543747](https://bugzilla.mozilla.org/show_bug.cgi?id=1543747)  Don't display exceptions from bouncer when the checks fail; r=sfraser Differential Revision: https://phabricator.services.mozilla.com/D27135|csabou@mozilla.com|sfraser|2019-04-12 06:51:12|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=d709880ef6dd)|[Bug 1543595](https://bugzilla.mozilla.org/show_bug.cgi?id=1543595)  - Add missing aarch64 target to the rust 1.33 toolchain. r=froydnj I must have written the rust 1.33 patch before I landed the linux64-aarch64 patches, so when that landed, it lacked the aarch64 target. (it's still there on the rust 1.32 toolchain) Differential Revision: https://phabricator.services.mozilla.com/D27035|csabou@mozilla.com|froydnj|2019-04-12 06:51:12|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=76d16b72c985)|[Bug 1543595](https://bugzilla.mozilla.org/show_bug.cgi?id=1543595)  - Enable linux64-aarch64 builds. r=froydnj While we don't have an actual need for those builds at the moment, there is work in progress to get fuzzing builds for aarch64, and as the previous change showed, the build were busted by other changes since they were put in place. So we might as well enable them, so as to be aware of bustage when it happens rather than while working on getting the fuzzing builds up. Depends on D27035 Differential Revision: https://phabricator.services.mozilla.com/D27036|csabou@mozilla.com|froydnj|2019-04-12 06:51:12|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=47660e04a4f9)|[Bug 1543469](https://bugzilla.mozilla.org/show_bug.cgi?id=1543469)  - Update builders to rustc 1.34. r=glandium Differential Revision: https://phabricator.services.mozilla.com/D27184|csabou@mozilla.com|glandium|2019-04-12 06:51:12|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=53309e75d9a0)|[Bug 1543826](https://bugzilla.mozilla.org/show_bug.cgi?id=1543826)  - Run Talos ccov tests only on try; r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D27175|csabou@mozilla.com|jmaher|2019-04-12 06:51:12|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=940684cd1065)|[Bug 1543826](https://bugzilla.mozilla.org/show_bug.cgi?id=1543826)  - Remove duplication of key "linux64-ccov/.*" in mapping to fix yaml failure.|csabou@mozilla.com||2019-04-12 06:51:12|

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=f4c8925d83ed)|[Bug 1543044](https://bugzilla.mozilla.org/show_bug.cgi?id=1543044)  - ensure high_value_tasks has a default value when we fail to get data from treeherder/seta. r=Callek ensure high_value_tasks has a default value when we fail to get data from treeherder/seta. Differential Revision: https://phabricator.services.mozilla.com/D27445|nbeleuzu@mozilla.com|Callek|2019-04-15 00:47:46|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=7a209bab1bfe)|[Bug 1543662](https://bugzilla.mozilla.org/show_bug.cgi?id=1543662)  Introduce channel verification to partials r=catlee Differential Revision: https://phabricator.services.mozilla.com/D27115|shindli@mozilla.com|catlee|2019-04-12 18:46:45|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=a632dfa60af6)|[Bug 1543895](https://bugzilla.mozilla.org/show_bug.cgi?id=1543895)  - Move test-platform keying of fetches in tests to individual fetch types. r=tomprince So, instead of fetches['by-test-platform']['fetch'], we have fetches['fetch']['by-test-platform']. Differential Revision: https://phabricator.services.mozilla.com/D27227|shindli@mozilla.com|tomprince|2019-04-12 12:34:00|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=0d76e1701610)|[Bug 1541823](https://bugzilla.mozilla.org/show_bug.cgi?id=1541823)  - Derive the fetch docker image from debian9-raw rather than debian9-base. r=dustin This will make the image smaller, and will make it happen earlier in cases its dependencies need to be rebuilt. Differential Revision: https://phabricator.services.mozilla.com/D26082|csabou@mozilla.com|dustin|2019-04-12 06:46:07|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=c91bf0806ef7)|[Bug 1543033](https://bugzilla.mozilla.org/show_bug.cgi?id=1543033)  Fix pathing for win64_aarch64_info.txt r=mtabara I've refactored the artifact map generation slightly to make the list of platforms more flexible, and also to let us have the previous name for win64_aarch64_info.txt. Differential Revision: https://phabricator.services.mozilla.com/D27049|csabou@mozilla.com|mtabara|2019-04-12 06:19:48|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=82d83ff9faca)|[Bug 1543558](https://bugzilla.mozilla.org/show_bug.cgi?id=1543558)  - Increase max-run-time for linux shippable builds; r=jmaher Avoid intermittent timeouts: increase max-run-time to 2.5 hours to account for normal variability in run time. Differential Revision: https://phabricator.services.mozilla.com/D27017|csabou@mozilla.com|jmaher|2019-04-12 06:19:48|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=1ce8b8034950)|[Bug 1536804](https://bugzilla.mozilla.org/show_bug.cgi?id=1536804)  - Add a task for summarising wpt metadata, r=ahal This task runs on wpt metadata changes and uploads an artifact containing the summarised metadata. Depends on D24178 Depends on D24178 Differential Revision: https://phabricator.services.mozilla.com/D24179|csabou@mozilla.com|ahal|2019-04-12 06:19:48|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=a498ba7a0992)|[Bug 1534463](https://bugzilla.mozilla.org/show_bug.cgi?id=1534463)  give tasks access to `hgmointernal` Taskcluster secret r=tomprince Now that we have added the necessary scopes to `ci-configuration`, we can add the in-tree scopes to give tasks access to the `hgmointernal` config Taskcluster secret. Differential Revision: https://phabricator.services.mozilla.com/D25001|csabou@mozilla.com|tomprince|2019-04-12 06:19:48|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=3595f2b4875f)|[Bug 1534463](https://bugzilla.mozilla.org/show_bug.cgi?id=1534463)  patch `run-task` to clone from private hgweb mirrors r=tomprince With tasks able to access the hgmointernal config from a Taskcluster secret, we can now add functionality to `run-task` to support checking out from the private hg service. Here we add add a `resolve_checkout_url` function which takes the base/head repository URLs and determines whether we should clone from the public or private service, returning the resolved URL. The function pulls down the secret and checks that the region the task is executing in is in the set of supported regions. Then we generate a random number and default to the public service if the number is lower than our "rate". If all the above conditions are met, we replace `hg.mozilla.org` with the resolved domain name for the given region. We add a call to this function to `collect_vcs_options`, and skip resolving the private URL if we aren't performing a checkout from within `run-task`. Differential Revision: https://phabricator.services.mozilla.com/D25002|csabou@mozilla.com|tomprince|2019-04-12 06:19:48|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=ef120e802c6f)|[Bug 1543747](https://bugzilla.mozilla.org/show_bug.cgi?id=1543747)  Don't display exceptions from bouncer when the checks fail; r=sfraser Differential Revision: https://phabricator.services.mozilla.com/D27135|csabou@mozilla.com|sfraser|2019-04-12 06:19:48|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=d709880ef6dd)|[Bug 1543595](https://bugzilla.mozilla.org/show_bug.cgi?id=1543595)  - Add missing aarch64 target to the rust 1.33 toolchain. r=froydnj I must have written the rust 1.33 patch before I landed the linux64-aarch64 patches, so when that landed, it lacked the aarch64 target. (it's still there on the rust 1.32 toolchain) Differential Revision: https://phabricator.services.mozilla.com/D27035|csabou@mozilla.com|froydnj|2019-04-12 06:19:48|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=76d16b72c985)|[Bug 1543595](https://bugzilla.mozilla.org/show_bug.cgi?id=1543595)  - Enable linux64-aarch64 builds. r=froydnj While we don't have an actual need for those builds at the moment, there is work in progress to get fuzzing builds for aarch64, and as the previous change showed, the build were busted by other changes since they were put in place. So we might as well enable them, so as to be aware of bustage when it happens rather than while working on getting the fuzzing builds up. Depends on D27035 Differential Revision: https://phabricator.services.mozilla.com/D27036|csabou@mozilla.com|froydnj|2019-04-12 06:19:48|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=47660e04a4f9)|[Bug 1543469](https://bugzilla.mozilla.org/show_bug.cgi?id=1543469)  - Update builders to rustc 1.34. r=glandium Differential Revision: https://phabricator.services.mozilla.com/D27184|csabou@mozilla.com|glandium|2019-04-12 06:19:48|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=53309e75d9a0)|[Bug 1543826](https://bugzilla.mozilla.org/show_bug.cgi?id=1543826)  - Run Talos ccov tests only on try; r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D27175|csabou@mozilla.com|jmaher|2019-04-12 06:19:48|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=940684cd1065)|[Bug 1543826](https://bugzilla.mozilla.org/show_bug.cgi?id=1543826)  - Remove duplication of key "linux64-ccov/.*" in mapping to fix yaml failure.|csabou@mozilla.com||2019-04-12 06:19:48|

|	mozilla-beta	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=5d7fb687b031)|[Bug 1543033](https://bugzilla.mozilla.org/show_bug.cgi?id=1543033)  Fix pathing for win64_aarch64_info.txt r=mtabara a=release I've refactored the artifact map generation slightly to make the list of platforms more flexible, and also to let us have the previous name for win64_aarch64_info.txt. Differential Revision: https://phabricator.services.mozilla.com/D27049|sfraser@mozilla.com|mtabara|2019-04-12 11:46:38|

|	mozilla-release	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)|FIC - BOT|Self Generated| - |

|	build-puppet	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla-releng/build-puppet/commit/093a779afb8c7f6abf60b04d54afc9851f7faf9b)|Scheduled weekly dependency update for week 14 (#448)    Update jinja2 from 2.10 to 2.10.1      Update jinja2 from 2.10 to 2.10.1      Update jinja2 from 2.10 to 2.10.1      Update boto3 from 1.9.127 to 1.9.130      Update botocore from 1.12.127 to 1.12.130      Update twisted from 18.9.0 to 19.2.0      Update hyperlink from 18.0.0 to 19.0.0      Update parso from 0.3.4 to 0.4.0      Update pexpect from 4.6.0 to 4.7.0      Update pexpect from 4.6.0 to 4.7.0      Update pexpect from 4.6.0 to 4.7.0      Update pyparsing from 2.3.1 to 2.4.0      Update pytz from 2018.9 to 2019.1      Update setuptools from 40.8.0 to 41.0.0|pyup-bot|N/A|2019-04-12 15:56:57|

|	OpenCloudConfig	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla-releng/OpenCloudConfig/commit/b32c096ea39c709a09a99358fc28a713e35060db)|Testing generic-worker 14.1.0 / taskcluster-proxy 5.1.0 on  STAGING   This change does _not_ affect any production workers. Commit made with:      ./gecko-try.sh 14.1.0 5.1.0  See https://github.com/taskcluster/generic-worker/blob/081b7c0200fb915ccc08d0cace49712ebc6e23c3/mozilla-try-scripts/gecko-try.sh  deploy: gecko-1-b-win2012-beta gecko-t-win10-64-beta gecko-t-win10-64-cu gecko-t-win10-64-gpu-b gecko-t-win10-64-hw-b gecko-t-win10-64-ux-b gecko-t-win10-a64-beta gecko-t-win7-32-beta gecko-t-win7-32-cu gecko-t-win7-32-gpu-b|petemoore|N/A|2019-04-12 18:05:46|

|	taskcluster	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/taskcluster/taskcluster/commit/d91ced93f8b6bfb5d62fad41b4d762b6d5132895)|Merge pull request #573 from taskcluster/renovate/cron-parser-2.x  Update dependency cron-parser to v2.11.0|djmitche|N/A|2019-04-15 02:11:47|
|[Link](https://github.com/taskcluster/taskcluster/commit/776b12749e94bce891082e7813b384e6fd09d67e)|Update dependency cron-parser to v2.11.0|renovate-bot|N/A|2019-04-15 00:41:17|
|[Link](https://github.com/taskcluster/taskcluster/commit/13104aabcc4be20d38f9defdb5e8c65434a9c57b)|Merge pull request #327 from iFlameing/yml  Bug[1446768] Adding new policy in .taskcluster.yml|djmitche|N/A|2019-04-12 18:19:27|
|[Link](https://github.com/taskcluster/taskcluster/commit/e37dcec7aaa0d53ab14f34ba1b9f3639f19bf8a9)|Merge pull request #563 from djmitche/bug1534713-b  Bug 1534713 - ignore errors draining a broken channel|djmitche|N/A|2019-04-12 17:01:02|

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
