##  Commits in production - for 3 days, generated on: 2019-04-30 03:32:02 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=8484074f6e62)|No Bug, taskcluster/docker/funsize-update-generator pipfile-update. r=sfraser Differential Revision: https://phabricator.services.mozilla.com/D29170|sfraser@mozilla.com|sfraser|2019-04-29 14:11:16|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=28e4375e491e)|Backed out changeset 8218cc92ee8d for docker images builds failures CLOSED TREE|btara@mozilla.com||2019-04-28 03:34:16|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=4c994bf99569)|[Bug 1544986](https://bugzilla.mozilla.org/show_bug.cgi?id=1544986)  - Fall back more gracefully when TASKCLUSTER_WORKER_GROUP is not set. r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D27841|mh@glandium.org|tomprince|2019-04-28 02:35:20|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=ebe9a3ca4b17)|[Bug 1545344](https://bugzilla.mozilla.org/show_bug.cgi?id=1545344)  - Don't change current directory when executing a command via run-task. r=tomprince Currently, all things running via run-task don't really care that the current directory is set to /. However, on generic-worker, many things assume the current directory is the task directory, which varies by task, and wrapping them with run-task fails because it resets the current directory. Differential Revision: https://phabricator.services.mozilla.com/D28018|mh@glandium.org|tomprince|2019-04-28 02:35:20|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=a584e4e9473f)|[Bug 1545368](https://bugzilla.mozilla.org/show_bug.cgi?id=1545368)  - Support fetches in run-task on generic-worker. r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D28048|mh@glandium.org|tomprince|2019-04-28 02:35:20|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=8c3a37a0a53e)|[Bug 1546870](https://bugzilla.mozilla.org/show_bug.cgi?id=1546870)  - Package win*-rust toolchains as .tar.xz. r=froydnj This uniformizes the artifact name across platforms. We may want to do the same for other toolchains, but it bears the question whether xz is reliably available on users' Windows machines, while it doesn't matter for rust, since mach bootstrap pulls it with rustup rather than from automation, contrary to other toolchains. Differential Revision: https://phabricator.services.mozilla.com/D28780|mh@glandium.org|froydnj|2019-04-28 02:35:20|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=8484074f6e62)|No Bug, taskcluster/docker/funsize-update-generator pipfile-update. r=sfraser Differential Revision: https://phabricator.services.mozilla.com/D29170|csabou@mozilla.com|sfraser|2019-04-29 19:05:37|

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=8484074f6e62)|No Bug, taskcluster/docker/funsize-update-generator pipfile-update. r=sfraser Differential Revision: https://phabricator.services.mozilla.com/D29170|csabou@mozilla.com|sfraser|2019-04-29 18:59:55|

|	mozilla-beta	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)|FIC - BOT|Self Generated| - |

|	version-control-tools	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/version-control-tools.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/version-control-tools.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/hgcustom/version-control-tools/pushloghtml?changeset=ae489559efe1)|mozhg: use renamed keyword argument when running under Mercurial >= 5.0 [Bug 1546508](https://bugzilla.mozilla.org/show_bug.cgi?id=1546508)  r=glob Under Mercurial 5.0, the `copied` keyword argument passed to `context.memfilectx` has been renamed to `copysource`. This commit adds a conditional to use the correct argument name when running under the new version. Differential Revision: https://phabricator.services.mozilla.com/D29212|cosheehan@mozilla.com|glob|2019-04-29 18:44:11|
|[Link](https://hg.mozilla.org/hgcustom/version-control-tools/pushloghtml?changeset=db9bc20ab995)|push-to-try: mark as compatible with Mercurial 5.0 [Bug 1546508](https://bugzilla.mozilla.org/show_bug.cgi?id=1546508)  r=glob With `mozhg` now compatible with the 5.0 release candidate, `push-to-try` tests pass under the new version. Differential Revision: https://phabricator.services.mozilla.com/D29213|cosheehan@mozilla.com|glob|2019-04-29 18:44:11|
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
