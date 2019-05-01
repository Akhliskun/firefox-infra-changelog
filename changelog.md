##  Commits in production - for 3 days, generated on: 2019-05-01 07:47:24 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=3c032a4347fa)|[Bug 1539227](https://bugzilla.mozilla.org/show_bug.cgi?id=1539227)  - land NSS 56826bedabba UPGRADE_NSS_RELEASE, r=KevinJacobs NSS uplift, 30 April 2019. Commit log: https://hg.mozilla.org/projects/nss/log?rev=e5e10a46b9ad..56826bedabba Differential Revision: https://phabricator.services.mozilla.com/D29382|jjones@mozilla.com|KevinJacobs|2019-05-01 02:14:35|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=96a1f7afe8ae)|[Bug 1532783](https://bugzilla.mozilla.org/show_bug.cgi?id=1532783)  [taskgraph] Fix lint error. Differential Revision: https://phabricator.services.mozilla.com/D29438|mozilla@hocat.ca||2019-05-01 02:09:30|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=cef374e9b298)|[Bug 1532783](https://bugzilla.mozilla.org/show_bug.cgi?id=1532783)  [taskgraph] Switch to using worker aliases for docker-worker and generic-worker; r=dustin Differential Revision: https://phabricator.services.mozilla.com/D24238|mozilla@hocat.ca|dustin|2019-05-01 02:03:44|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=49006e43876f)|[Bug 1532783](https://bugzilla.mozilla.org/show_bug.cgi?id=1532783)  [taskgraph] Remove entries from WORKER_TYPES that correspond to workers with aliases; r=dustin Differential Revision: https://phabricator.services.mozilla.com/D24239|mozilla@hocat.ca|dustin|2019-05-01 02:03:44|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=9aaca7d58bfa)|[Bug 1541313](https://bugzilla.mozilla.org/show_bug.cgi?id=1541313)  - Upgrade nightly rust to the last one that was versioned 1.34. r=dmajor Differential Revision: https://phabricator.services.mozilla.com/D29307|mh@glandium.org|dmajor|2019-05-01 01:17:12|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=67a90171e265)|[Bug 1536543](https://bugzilla.mozilla.org/show_bug.cgi?id=1536543)  - Require rust 1.34. r=froydnj Differential Revision: https://phabricator.services.mozilla.com/D25896|mh@glandium.org|froydnj|2019-05-01 01:17:12|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=486f55e81c57)|[Bug 1546320](https://bugzilla.mozilla.org/show_bug.cgi?id=1546320)  - Create mozconfigs for Fennec beta builds r=RyanVM Create mozconfigs for Fennec beta builds. This also prevents mergeday scripts from modifying nightly mozconfigs on beta Differential Revision: https://phabricator.services.mozilla.com/D29350|jlorenzo@mozilla.com|RyanVM|2019-04-30 16:59:17|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=626ad97710e3)|[Bug 1533330](https://bugzilla.mozilla.org/show_bug.cgi?id=1533330)  - Update tooltool.py with optional support of taskcluster auth tokens r=rail With this change tooltool.py also supports taskcluster credentials to be passed (in json format) to --authentication-file option. RelengAPI tokens are still working with this patch, just additional authentication is added. Differential Revision: https://phabricator.services.mozilla.com/D27881|rgarbas@mozilla.com|rail|2019-04-30 09:57:50|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=b7aa4980e921)|[Bug 1547395](https://bugzilla.mozilla.org/show_bug.cgi?id=1547395)  - Allow specific tasks in the use-pgo field; r=tomprince Some groups of tasks need to share the same profile data. For example, Android PGO builds and Android Nightly builds both use the generate-profile-android-api-16/pgo task for profile data. Previously this was done with a text substitution, but this is a bit hacky and doesn't easily scale with different build types. Allowing use_pgo to be a string means we can just directly point to the generate-profile task that contains the profile data to be used in a PGO build. Differential Revision: https://phabricator.services.mozilla.com/D29247|ccoroiu@mozilla.com|tomprince|2019-05-01 07:27:55|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=2de8fcb8a341)|[Bug 1547395](https://bugzilla.mozilla.org/show_bug.cgi?id=1547395)  - Use 3-tier PGO for linux64-devedition builds; r=chmanchester Depends on D29247 Differential Revision: https://phabricator.services.mozilla.com/D29248|ccoroiu@mozilla.com|chmanchester|2019-05-01 07:27:55|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=9aaca7d58bfa)|[Bug 1541313](https://bugzilla.mozilla.org/show_bug.cgi?id=1541313)  - Upgrade nightly rust to the last one that was versioned 1.34. r=dmajor Differential Revision: https://phabricator.services.mozilla.com/D29307|ccoroiu@mozilla.com|dmajor|2019-05-01 07:27:55|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=67a90171e265)|[Bug 1536543](https://bugzilla.mozilla.org/show_bug.cgi?id=1536543)  - Require rust 1.34. r=froydnj Differential Revision: https://phabricator.services.mozilla.com/D25896|ccoroiu@mozilla.com|froydnj|2019-05-01 07:27:55|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=cef374e9b298)|[Bug 1532783](https://bugzilla.mozilla.org/show_bug.cgi?id=1532783)  [taskgraph] Switch to using worker aliases for docker-worker and generic-worker; r=dustin Differential Revision: https://phabricator.services.mozilla.com/D24238|ccoroiu@mozilla.com|dustin|2019-05-01 07:27:55|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=49006e43876f)|[Bug 1532783](https://bugzilla.mozilla.org/show_bug.cgi?id=1532783)  [taskgraph] Remove entries from WORKER_TYPES that correspond to workers with aliases; r=dustin Differential Revision: https://phabricator.services.mozilla.com/D24239|ccoroiu@mozilla.com|dustin|2019-05-01 07:27:55|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=96a1f7afe8ae)|[Bug 1532783](https://bugzilla.mozilla.org/show_bug.cgi?id=1532783)  [taskgraph] Fix lint error. Differential Revision: https://phabricator.services.mozilla.com/D29438|ccoroiu@mozilla.com||2019-05-01 07:27:55|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=3c032a4347fa)|[Bug 1539227](https://bugzilla.mozilla.org/show_bug.cgi?id=1539227)  - land NSS 56826bedabba UPGRADE_NSS_RELEASE, r=KevinJacobs NSS uplift, 30 April 2019. Commit log: https://hg.mozilla.org/projects/nss/log?rev=e5e10a46b9ad..56826bedabba Differential Revision: https://phabricator.services.mozilla.com/D29382|ccoroiu@mozilla.com|KevinJacobs|2019-05-01 07:27:55|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=486f55e81c57)|[Bug 1546320](https://bugzilla.mozilla.org/show_bug.cgi?id=1546320)  - Create mozconfigs for Fennec beta builds r=RyanVM Create mozconfigs for Fennec beta builds. This also prevents mergeday scripts from modifying nightly mozconfigs on beta Differential Revision: https://phabricator.services.mozilla.com/D29350|ccoroiu@mozilla.com|RyanVM|2019-05-01 00:59:18|

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=b7aa4980e921)|[Bug 1547395](https://bugzilla.mozilla.org/show_bug.cgi?id=1547395)  - Allow specific tasks in the use-pgo field; r=tomprince Some groups of tasks need to share the same profile data. For example, Android PGO builds and Android Nightly builds both use the generate-profile-android-api-16/pgo task for profile data. Previously this was done with a text substitution, but this is a bit hacky and doesn't easily scale with different build types. Allowing use_pgo to be a string means we can just directly point to the generate-profile task that contains the profile data to be used in a PGO build. Differential Revision: https://phabricator.services.mozilla.com/D29247|ccoroiu@mozilla.com|tomprince|2019-05-01 07:21:12|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=2de8fcb8a341)|[Bug 1547395](https://bugzilla.mozilla.org/show_bug.cgi?id=1547395)  - Use 3-tier PGO for linux64-devedition builds; r=chmanchester Depends on D29247 Differential Revision: https://phabricator.services.mozilla.com/D29248|ccoroiu@mozilla.com|chmanchester|2019-05-01 07:21:12|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=9aaca7d58bfa)|[Bug 1541313](https://bugzilla.mozilla.org/show_bug.cgi?id=1541313)  - Upgrade nightly rust to the last one that was versioned 1.34. r=dmajor Differential Revision: https://phabricator.services.mozilla.com/D29307|ccoroiu@mozilla.com|dmajor|2019-05-01 07:21:12|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=67a90171e265)|[Bug 1536543](https://bugzilla.mozilla.org/show_bug.cgi?id=1536543)  - Require rust 1.34. r=froydnj Differential Revision: https://phabricator.services.mozilla.com/D25896|ccoroiu@mozilla.com|froydnj|2019-05-01 07:21:12|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=cef374e9b298)|[Bug 1532783](https://bugzilla.mozilla.org/show_bug.cgi?id=1532783)  [taskgraph] Switch to using worker aliases for docker-worker and generic-worker; r=dustin Differential Revision: https://phabricator.services.mozilla.com/D24238|ccoroiu@mozilla.com|dustin|2019-05-01 07:21:12|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=49006e43876f)|[Bug 1532783](https://bugzilla.mozilla.org/show_bug.cgi?id=1532783)  [taskgraph] Remove entries from WORKER_TYPES that correspond to workers with aliases; r=dustin Differential Revision: https://phabricator.services.mozilla.com/D24239|ccoroiu@mozilla.com|dustin|2019-05-01 07:21:12|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=96a1f7afe8ae)|[Bug 1532783](https://bugzilla.mozilla.org/show_bug.cgi?id=1532783)  [taskgraph] Fix lint error. Differential Revision: https://phabricator.services.mozilla.com/D29438|ccoroiu@mozilla.com||2019-05-01 07:21:12|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=3c032a4347fa)|[Bug 1539227](https://bugzilla.mozilla.org/show_bug.cgi?id=1539227)  - land NSS 56826bedabba UPGRADE_NSS_RELEASE, r=KevinJacobs NSS uplift, 30 April 2019. Commit log: https://hg.mozilla.org/projects/nss/log?rev=e5e10a46b9ad..56826bedabba Differential Revision: https://phabricator.services.mozilla.com/D29382|ccoroiu@mozilla.com|KevinJacobs|2019-05-01 07:21:12|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=486f55e81c57)|[Bug 1546320](https://bugzilla.mozilla.org/show_bug.cgi?id=1546320)  - Create mozconfigs for Fennec beta builds r=RyanVM Create mozconfigs for Fennec beta builds. This also prevents mergeday scripts from modifying nightly mozconfigs on beta Differential Revision: https://phabricator.services.mozilla.com/D29350|ccoroiu@mozilla.com|RyanVM|2019-05-01 00:53:37|

|	mozilla-beta	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)|FIC - BOT|Self Generated| - |

|	version-control-tools	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/version-control-tools.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/version-control-tools.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/hgcustom/version-control-tools/pushloghtml?changeset=d9911e62f3a4)|pushlog: fix tests regressed by 40-character node patch [Bug 1548054](https://bugzilla.mozilla.org/show_bug.cgi?id=1548054)  r=lars A few tests were overlooked when changing `gitweb_mozilla` to display 40-character SHAs. This commit fixes those tests. Differential Revision: https://phabricator.services.mozilla.com/D29397|cosheehan@mozilla.com|lars|2019-04-30 23:55:39|
|[Link](https://hg.mozilla.org/hgcustom/version-control-tools/pushloghtml?changeset=f13310e10021)|ansible/monitoring-agent: remove quotes around boolean variable [Bug 1543989](https://bugzilla.mozilla.org/show_bug.cgi?id=1543989)  This causes the variable to be a string instead of a bool.|cosheehan@mozilla.com||2019-04-30 19:25:39|
|[Link](https://hg.mozilla.org/hgcustom/version-control-tools/pushloghtml?changeset=d7b0532a4e6a)|ansible/monitoring-agent: fix production InfluxDB credentials [Bug 1543989](https://bugzilla.mozilla.org/show_bug.cgi?id=1543989)  The production URL for Mozilla's InfluxDB instance was incorrect, as well as the database name being enclosed by too many quotes. The `influxdb_skip_database_creation` variable is also added as `True` (valid in Python) instead of `true` (valid JSON/TOML), so we add a `to_json` filter to that variable.|cosheehan@mozilla.com||2019-04-30 19:09:51|
|[Link](https://hg.mozilla.org/hgcustom/version-control-tools/pushloghtml?changeset=88247fb4308a)|robustcheckout: remove arguments passed to `matchmod.always` in modern Mercurial [Bug 1546507](https://bugzilla.mozilla.org/show_bug.cgi?id=1546507)  r=glob The arguments passed to `matchmod.always` are unused under the hood, so they've been removed in Mercurial 5.0 and onward. Differential Revision: https://phabricator.services.mozilla.com/D29271|cosheehan@mozilla.com|glob|2019-04-30 18:53:54|
|[Link](https://hg.mozilla.org/hgcustom/version-control-tools/pushloghtml?changeset=baa4bb1271e8)|ansible/monitoring-agent: add encrypted InfluxDB credentials [Bug 1543989](https://bugzilla.mozilla.org/show_bug.cgi?id=1543989)  r=lars This commit adds a set of default Ansible variables in the `monitoring-agent` role, for sending data to Mozilla's production InfluxDB instance. Since `sops` doesn't yet know how to parse TOML, we store the secrets as YAML Ansible defaults. Differential Revision: https://phabricator.services.mozilla.com/D28363|cosheehan@mozilla.com|lars|2019-04-30 18:03:56|
|[Link](https://hg.mozilla.org/hgcustom/version-control-tools/pushloghtml?changeset=32df72677efb)|ansible/monitoring-agent: send monitoring data to production InfluxDB instance [Bug 1543989](https://bugzilla.mozilla.org/show_bug.cgi?id=1543989)  r=lars This commit tells Telegraf to send data to the production InfluxDB instance. At the moment we will send data to both the test instance and the production instance, to verify all the data is correctly sent. Differential Revision: https://phabricator.services.mozilla.com/D28364|cosheehan@mozilla.com|lars|2019-04-30 18:03:56|
|[Link](https://hg.mozilla.org/hgcustom/version-control-tools/pushloghtml?changeset=41e63de62c96)|hgtemplates: pass `node` through `short` template filter for `data-node` HTML tag [Bug 1547870](https://bugzilla.mozilla.org/show_bug.cgi?id=1547870)  r=glob Not passing the node through `short` causes a `querySelector` call in `mercurial.js` to return nothing. This call is responsible for applying left padding to the element, to allow the graph to display without the changeset information on top. Differential Revision: https://phabricator.services.mozilla.com/D29362|cosheehan@mozilla.com|glob|2019-04-30 18:00:40|
|[Link](https://hg.mozilla.org/hgcustom/version-control-tools/pushloghtml?changeset=51905dc214c4)|hgtemplates: do not pass `node` through `short` template filter anywhere [Bug 1539324](https://bugzilla.mozilla.org/show_bug.cgi?id=1539324)  r=glob Treeherder has removed support for using 12 character revision SHAs, due to the performance hit taken by being unable to fully index a 12 character SHA (since the 40 character SHA is the canonical version). This commit performs a global replace of `{node|short}` with `{node}` for the `gitweb_mozilla` theme. The existing form takes the `node` template keyword and passes it through the `short` template filter, producing the 12-character SHA. Removing the `short` filter will cause the full 40-char SHA to be displayed instead. Like all other templating changes, we add a patchfile to `hgtemplates/.patches` that encompasses all the changes made by this commit. Running `hgserver/tests/test-template-sync.t` verified that the changes are successfully tracked under version control. Differential Revision: https://phabricator.services.mozilla.com/D29033|cosheehan@mozilla.com|glob|2019-04-29 16:50:05|

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
|[Link](https://github.com/mozilla-platform-ops/ronin_puppet/commit/b07a9c709a702db512d9e99f64bb0e0606ac638f)|Merge pull request #23 from davehouse/bug1546448_notarization  Bug 1546448 notarization base|davehouse|N/A|2019-04-30 20:28:11|
|[Link](https://github.com/mozilla-platform-ops/ronin_puppet/commit/a395466ca7863f4d630ce030f2358ba6fd0b68a9)|bitbar: fixes (#24)|aerickson|N/A|2019-04-30 20:11:10|
|[Link](https://github.com/mozilla-platform-ops/ronin_puppet/commit/715fb0fc675aebe79556b20af6293ff1ccc124b4)|add bitbar_devicepool module (#22)|aerickson|N/A|2019-04-29 22:31:09|

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
|[Link](https://github.com/mozilla-releng/build-puppet/commit/c59b2740aab3d497c17fcc63eefdc01658b3ab9f)|Merge pull request #463 from mitchhentges/fenix-beta-signing  Adds configuration to signing/pushapk for Fenix beta|mitchhentges|N/A|2019-04-29 12:43:13|

|	taskcluster	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/taskcluster/taskcluster/commit/d2d5d6418fedbe42b00d6842bbb5ccf86db930fa)|Revert "Do not run strategy if config is undefined (#664)" (#666)  This reverts commit 31618225c2c7a4d1bf77f8f5b213a4c0176b0ab4.|helfi92|N/A|2019-04-30 19:50:19|
|[Link](https://github.com/taskcluster/taskcluster/commit/31618225c2c7a4d1bf77f8f5b213a4c0176b0ab4)|Do not run strategy if config is undefined (#664)|helfi92|N/A|2019-04-30 19:15:17|
|[Link](https://github.com/taskcluster/taskcluster/commit/4564286e712448533fd93c501e10ba6ca402952d)|Bump client versions|imbstack|N/A|2019-04-30 18:49:15|
|[Link](https://github.com/taskcluster/taskcluster/commit/50958a85588ee0f0f8b65887489f5d41855d6a6a)|Merge pull request #547 from helfi92/login-auth0  Add login via mozilla auth0|helfi92|N/A|2019-04-30 18:11:03|
|[Link](https://github.com/taskcluster/taskcluster/commit/406583d316a34dcc86f90bf8bc196e82a6a6f923)|Merge pull request #656 from taskcluster/fix-notify-irc  Fix notify irc|imbstack|N/A|2019-04-30 16:34:32|
|[Link](https://github.com/taskcluster/taskcluster/commit/8234b74b6c114a0a2b355312c006795e88ef4c51)|Merge pull request #655 from helfi92/resetting-store-issues  [UI] Rely on key and fetchPolicy instead of resetStore|helfi92|N/A|2019-04-30 15:32:01|
|[Link](https://github.com/taskcluster/taskcluster/commit/ece6b75a7051e28e936aa8454d54137861e27ac1)|Merge pull request #632 from owlishDeveloper/bug1546789  Add `list worker types` endpoint to worker manager|owlishDeveloper|N/A|2019-04-30 15:29:57|
|[Link](https://github.com/taskcluster/taskcluster/commit/22c7f5e038de9613beac113a91de5397d868520c)|Add note re:fetchPolicy|helfi92|N/A|2019-04-30 14:51:34|
|[Link](https://github.com/taskcluster/taskcluster/commit/72c579887f756edab92c73062bb3e6cb7b733a6b)|Merge pull request #295 from taskcluster/renovate/neutrino-monorepo  Update neutrino monorepo to v9.0.0-rc.0|helfi92|N/A|2019-04-30 15:09:21|
|[Link](https://github.com/taskcluster/taskcluster/commit/5f391e8fa40860737f58b83004dbb7a6b8c78ffc)|Rely on `key` and `fetchPolicy` instead of `resetStore`  `resetStore` causes the store to be cleared and all active queries to be refetched. The only problem is that for many of our views, we depend on `fetchMore` to fetch the full list. Refetching active queries will only fetch the first query.  To fix this issue, we should rely on the key prop and the networkPolicy property to refetch active queries. Changing the key prop of a component in React will re-render that component. This will have a similar effect as resetStore.|helfi92|N/A|2019-04-29 23:21:19|
|[Link](https://github.com/taskcluster/taskcluster/commit/7b7fd0629376fabf45e47501b17d03385e9d27b5)|Merge pull request #653 from djmitche/best-practices-monorepo  Add document describing development practices|djmitche|N/A|2019-04-29 23:11:00|
|[Link](https://github.com/taskcluster/taskcluster/commit/1a404938a43a7682898486d9ab49e2dc9f77b0b2)|Add document describing development practices|djmitche|N/A|2019-04-29 22:51:19|
|[Link](https://github.com/taskcluster/taskcluster/commit/04ecaf98b0ad5006a7cb7fcb08a86e7e2a57d82d)|Merge pull request #650 from djmitche/bug1547589  Bug 1547589 - denylisting fixes|imbstack|N/A|2019-04-29 21:33:51|
|[Link](https://github.com/taskcluster/taskcluster/commit/1213f33bcddc9933dbf604afaf39a57cc8ca04f0)|Merge pull request #652 from djmitche/dep-list-punct  Omit needless punctuation in error message|djmitche|N/A|2019-04-29 21:33:06|
|[Link](https://github.com/taskcluster/taskcluster/commit/efd48784232ce34728558e7733305a1099af7fa4)|Omit needless punctuation in error message  This had me briefly wondering if something had stuck a `,` into a taskId (which wouldn't be too hard with Python's treatment of `foo,` as a tuple)|djmitche|N/A|2019-04-29 20:49:02|
|[Link](https://github.com/taskcluster/taskcluster/commit/326e072427779e6f2e10af9747e5718a0488b560)|Merge pull request #649 from djmitche/bug1547733  Bug 1547733 - actually set 'trust proxy'|djmitche|N/A|2019-04-29 18:18:41|
|[Link](https://github.com/taskcluster/taskcluster/commit/13c8fcb4eb2f34e909e57a38a6a1c53bf12cd2bf)|Bug 1547589 - also deny notifications at the Notifier level  Note that here we just drop the notification (with a log message) since often it will be a result of a pulse message, etc.  Thus we get nice errors from the API methods, and quietly filter out other notification strategies.|djmitche|N/A|2019-04-29 17:02:05|
|[Link](https://github.com/taskcluster/taskcluster/commit/3862b8a7c5da11c876fbfc0362f6b2897ac6b261)|Bug 1547589 - add Denier to filter denied addresses  This also fixes up the test_api.js tests so that they can fail..|djmitche|N/A|2019-04-29 16:49:30|
|[Link](https://github.com/taskcluster/taskcluster/commit/d001032248a9e78dae921f06ec0eb3786b2a47a2)|[Bug 1519730] Replace sqs with pulse (#619)   [Bug 1519730] Replace sqs with pulse|imbstack|N/A|2019-04-29 18:11:25|
|[Link](https://github.com/taskcluster/taskcluster/commit/eaf924bb2d7a27bd5f6fbc6c928a1ebd11e6a922)|[UI] Remove unused dependencies (#648)|helfi92|N/A|2019-04-29 13:42:15|
|[Link](https://github.com/taskcluster/taskcluster/commit/a22bfed96fd93770f4b020d5141cbe22efde17ba)|Merge pull request #642 from djmitche/bug1544942  Bug 1544942 - replace signatureValidated logs with apiMethod|djmitche|N/A|2019-04-29 13:35:26|
|[Link](https://github.com/taskcluster/taskcluster/commit/a8089746ec276acfcf8bda5eac15192e95c47191)|[UI] Fix ambiguity in headers in lasstfire table (#644)|Biboswan|N/A|2019-04-29 13:14:19|
|[Link](https://github.com/taskcluster/taskcluster/commit/2354f0f5dc0e5f0e9f25e58c8edc3e4a4904e262)|Update dependency babel-merge to v3 (#646)|renovate[bot]|N/A|2019-04-29 13:05:39|
|[Link](https://github.com/taskcluster/taskcluster/commit/18434828e8ea28b34d29f2af19d0236fa2d7b386)|Merge pull request #641 from djmitche/bug1542405  Bug 1542405 - update tc-github handler tests to use new fake pulse support|djmitche|N/A|2019-04-28 18:19:37|

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
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=cefa9839aaad)|[Bug 1542550](https://bugzilla.mozilla.org/show_bug.cgi?id=1542550)  - Grant thunderbird scopes for signing shippable builds on push. r=tomprince Shippable builds cause release builds to be built on push. Since singing is done at that time, pushes need to be able access the production signing scriptworkers. Differential Revision: https://phabricator.services.mozilla.com/D28589|mozilla@hocat.ca|tomprince|2019-04-30 20:52:45|
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=f4167b7e7639)|[Bug 1526017](https://bugzilla.mozilla.org/show_bug.cgi?id=1526017)  - cleanup the docker-worker:cache scopes. r=jlorenzo More scopes cleanup Differential Revision: https://phabricator.services.mozilla.com/D29338|mtabara@mozilla.com|jlorenzo|2019-04-30 15:16:52|
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=ddd1bfed9ee4)|[Bug 1519493](https://bugzilla.mozilla.org/show_bug.cgi?id=1519493)  - create cron roles for hooks to use instead. r=jlorenzo Create cron prod/staging roles for hooks to use instead. Differential Revision: https://phabricator.services.mozilla.com/D29208|mtabara@mozilla.com|jlorenzo|2019-04-30 11:14:42|

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
