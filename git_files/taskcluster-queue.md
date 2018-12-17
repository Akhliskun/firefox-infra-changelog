## TASKCLUSTER-QUEUE COMMIT MARKDOWN TABLE SINCE 2018-12-03 17:46:15.735277

| Commit Number | Commiter | Commit Message | Commit Url | Date | 
|:---:|:----:|:----------------------------------:|:------:|:----:| 
|1241|djmitche|Merge pull request #306 from djmitche/bug1502892  Bug 1502892 - refactor create/defineTask to check authorization before validation|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1e47a960a34cd36322900cad5bfc2834fcea7b8f)|2018-12-14 17:22:13
|1240|djmitche|Bug 1502892 - refactor create/defineTask to check authorization before validating|[URL](https://github.com/taskcluster/taskcluster-queue/commit/98f3728774245c48582184e4ba49dc7a00f84b9a)|2018-12-13 21:36:40
|1239|djmitche|Bug 1502892 - add some more tests around createTask and priorities|[URL](https://github.com/taskcluster/taskcluster-queue/commit/45bbf334a67982ff9cd6bd58b2ad0e502879cd89)|2018-12-13 21:20:09
|1238|djmitche|Merge pull request #305 from djmitche/bug1510377  Bug 1510377 - use tc-lib-references to validate references|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f16ab6658148efcac18434802525091f66359f42)|2018-12-07 15:23:43
|1237|djmitche|Bug 1510377 - use tc-lib-references to validate references|[URL](https://github.com/taskcluster/taskcluster-queue/commit/904a244e39a0d96488f7fe41f031355b0e01f018)|2018-12-06 00:01:53
|1236|djmitche|Merge pull request #304 from djmitche/bug1509189  Bug 1509189 - use unique table names to avoid conflicts|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c3a424aa0811c0b8bef42219a485d5a179a14ba2)|2018-11-30 02:12:03
|1235|djmitche|Bug 1509189 - use unique table names to avoid conflicts  Taskcluster-Github already does something like this.  The tables get cleaned out and should have no rows at test completion, so this doesn't use a lot of space.  There's no limit (aside from space) on the number of tables in an account.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/cb8f3946830b982b58d2f93b99202cab15f40719)|2018-11-29 01:12:10
|1234|djmitche|Bug 1509186 - remove references to taskcluster.net from the API description|[URL](https://github.com/taskcluster/taskcluster-queue/commit/eae5a8ff58e6edaac15fd95d273509c8045da3f6)|2018-11-26 18:08:58
|1233|djmitche|Merge pull request #303 from djmitche/bug1456909  Bug 1456909 - use monitor.oneShot()|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9595f61cd17ad72c315e52d7d950026527ded5c6)|2018-11-26 22:05:11
|1232|djmitche|Bug 1456909 - use monitor.oneShot()|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0e7810781f5e64b1ef06a01f97abf85830e024c9)|2018-11-26 19:30:30
|1231|djmitche|Bug 1508846 - upgrade tc-lib-api|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5f259488c4ea8bd43a15fa4c5f1b660c2ce887da)|2018-11-21 21:35:58
|1230|djmitche|Merge pull request #299 from djmitche/bug1508395  Bug 1508395 - upgrade tc-lib-validate|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ee3bef79dc9bb2726dd8cea644ad3290da60d3d4)|2018-11-21 21:34:10
|1229|djmitche|Merge branch 'master' into bug1508395|[URL](https://github.com/taskcluster/taskcluster-queue/commit/087cca55ada7a151518f018819b1a21f59df769d)|2018-11-21 21:34:04
|1228|djmitche|Merge pull request #300 from djmitche/bug1505405  Bug 1505405 - upgrade tc-lib-pulse|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6340fc2bafc194872799e59b55a37a7c54dd63b6)|2018-11-21 21:33:36
|1227|djmitche|Bug 1505405 - upgrade tc-lib-pulse|[URL](https://github.com/taskcluster/taskcluster-queue/commit/17bf8649dabb96c849f2b875c82ad02fdf0d14ff)|2018-11-20 20:24:55
|1226|djmitche|Merge pull request #301 from djmitche/bug1508849  Bug 1508849 - implement   -scope protection differently|[URL](https://github.com/taskcluster/taskcluster-queue/commit/bed26fb8855ee4c96174be3f9200cf4965f75a1d)|2018-11-21 21:32:11
|1225|djmitche|Bug 1508849 - implement   -scope protection differently  The old solution used a negative lookbehind, which per https://json-schema.org/understanding-json-schema/reference/regular_expressions.html#regular-expressions is not supported in json-schema. In fact, it's not supported in even fairly recent versions of Node. This causes problems when validating schemas using those old versions of node (or using json-schema validators that do not support this form).  So, the new solution is to explicitly forbid those forms where used in creating clients and roles. The result is much the same, as evidenced by the minimal changes to the tests.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/936be6b0b42002fbae57b69a6b4f7acabf82d8ac)|2018-11-21 00:55:08
|1224|djmitche|Bug 1508395 - upgrade tc-lib-validate  This should only affect writeDocs|[URL](https://github.com/taskcluster/taskcluster-queue/commit/54344d0e797e7338f88dadca4627846648200c36)|2018-11-20 20:22:31
|1223|djmitche|Merge pull request #295 from djmitche/bug1488796  Bug 1488796 - upgrade to tc-lib-pulse for sending pulse messages|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a321054a3b02cc88472580f43fbbbb0be486c570)|2018-10-24 20:49:38
|1222|djmitche|Bug 1488796 - upgrade to tc-lib-pulse for sending pulse messages|[URL](https://github.com/taskcluster/taskcluster-queue/commit/92157abfc0189acbcf5306ad7be7d649bd33eb94)|2018-10-19 18:07:44
|1221|djmitche|Merge pull request #294 from djmitche/bug1499701  Bug 1499701 - upgrade azure to behave better on SAS errors|[URL](https://github.com/taskcluster/taskcluster-queue/commit/42acaa6521a94f7675308376b0e4ed62aafdcc6f)|2018-10-24 17:40:07
|1220|djmitche|Bug 1501007 - terminate the queueservice so expirequeues exits|[URL](https://github.com/taskcluster/taskcluster-queue/commit/89d09cf5112053546ab3e237bd44bfff6d085946)|2018-10-22 21:31:52
|1219|djmitche|Bug 1499701 - upgrade azure to behave better on SAS errors|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5f7a9b0e7cf3685c5ff97f06a669ca4eb4368737)|2018-10-19 16:39:58
|1218|imbstack|Merge pull request #293 from taskcluster/bug1495918  Bug 1495918 - use `NO_TEST_SKIP: "true"` rather than `NO_TEST_SKIP: true` in yaml files|[URL](https://github.com/taskcluster/taskcluster-queue/commit/cece39035772aed4f6b044db72210bec5df37537)|2018-10-10 22:32:59
|1217|petemoore|Bug 1495918 - use `NO_TEST_SKIP: "true"` rather than `NO_TEST_SKIP: true` in yaml files|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c655a1819bb900aa8d40130db01ee34b4bc27929)|2018-10-09 09:18:21
|1216|imbstack|Merge pull request #291 from taskcluster/audit-log-ip  Update lib-api to report ip addrs for auth|[URL](https://github.com/taskcluster/taskcluster-queue/commit/bb380d3ebd811808999f5473b88c56cdbfae125e)|2018-09-28 19:50:31
|1215|imbstack|Update lib-testing|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f8d084e21261da31eca56e016e38a56a3021db49)|2018-09-28 17:06:44
|1214|imbstack|Remove instance of improperly cased tc|[URL](https://github.com/taskcluster/taskcluster-queue/commit/25fddd929e0250de9b1b8d3d9300362a29006625)|2018-09-27 20:33:34
|1213|imbstack|Remove travis to avoid racing tests|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a274f562bdf15a53b38ec86bce54ed3c99a6012a)|2018-09-27 20:28:46
|1212|imbstack|Update lib-api to send ip addr to auth|[URL](https://github.com/taskcluster/taskcluster-queue/commit/08d92089895727040a906b92b0f928d7ce420b1f)|2018-09-27 20:16:26
|1211|djmitche|Merge pull request #290 from djmitche/bug1478835  Bug 1478835 - fix support for useCloudMirror|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7c76631a1cdfd9811936cf6f58430d9da042f2df)|2018-09-18 12:20:14
|1210|djmitche|Bug 1478835 - fix support for useCloudMirror  This includes renaming the env var to USE_CLOUD_MIRROR for consistency with the JS name and removing the unused `usePublicArtifactBucketProxy` configuration property.  Thanks to @jhford for most of this patch :)|[URL](https://github.com/taskcluster/taskcluster-queue/commit/08b4faa44417d3f1149d3935c5a81e5925179055)|2018-09-17 23:29:46
|1209|djmitche|Merge pull request #289 from djmitche/bug1490780  Bug 1490780 - minor formatting fixes in queue error messages|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a4f77737abcbb9003e4a582ac8125778d20610bf)|2018-09-17 18:22:01
|1208|djmitche|Bug 1490780 - minor formatting fixes in queue error messages|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6d4aa09be8d5ef5c4e027f6a2acb8172df16e936)|2018-09-14 21:34:37
|1207|ccooper|Add documentation to bring taskcluster repos closer to the Github recommended community standards  Added licensing info (MPL2), contribution suggestions, and a link to the Mozilla Community Participation Guidelines.  Addresses https://bugzil.la/1408073 for this repo.  Carrying-over review from https://github.com/taskcluster/taskcluster-tools/pull/546|[URL](https://github.com/taskcluster/taskcluster-queue/commit/163f0aa95c51550967ed46619322c991f477e234)|2018-09-13 15:07:23
|1206|djmitche|Merge pull request #288 from djmitche/bug1440965  Bug 1440965 - enforce that scopes not end in   |[URL](https://github.com/taskcluster/taskcluster-queue/commit/3b2960adf20ccb960a474fd68a526b4c389868b4)|2018-08-24 16:32:13
|1205|djmitche|Bug 1440965 - enforce that scopes not end in   |[URL](https://github.com/taskcluster/taskcluster-queue/commit/fd8027f1231421e95f11399a45aac3e59ade8525)|2018-08-23 19:45:09
|1204|imbstack|Merge pull request #287 from taskcluster/bug-1481493  Allow logging azure timings|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ea0a61f5fe03359326ce2450ff88642b9c47b841)|2018-08-13 18:01:58
|1203|imbstack|Only run one task at a time|[URL](https://github.com/taskcluster/taskcluster-queue/commit/99d4d41355fc446c43f269be1cfa989783d3f918)|2018-08-13 16:18:42
|1202|imbstack|Allow logging azure timings|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9bedbe5313f881bb08ea621c3ff873590d8099f2)|2018-08-08 04:20:54
|1201|djmitche|Merge pull request #285 from djmitche/createtask-docs-update  Consolidate schemas with $ref|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f7e4fcf0ad0fa507e81d003b0362e290b0c7a760)|2018-07-25 14:25:05
|1200|arjunkrishnababu96|Bug 1453714 - Return http 424 instead of 403 for error artifacts. (#283)|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c420eeae58971ce25b1c3ef27350e0d2e52d780c)|2018-07-24 18:09:34
|1199|djmitche|Consolidate schemas with $ref  This helps to clean up some documentation as it appears in the docs service, and removes redundant, sometimes contradictory statements about similar fields.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f0225cc98f3b47f47e23ccdcb26b946996d798f3)|2018-07-20 20:40:35
|1198|djmitche|Build all pull requests|[URL](https://github.com/taskcluster/taskcluster-queue/commit/56fe21f0faaf061029c3d0b8c75f1bff0c9abeb2)|2018-07-19 19:18:56
|1197|djmitche|less DEBUG, more cowbell|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4daad23c1265b699e66fd9d9fd2b5a32711e330d)|2018-07-19 14:54:21
|1196|djmitche|Merge pull request #284 from djmitche/bug1476441  Bug 1476441 - fix relative docs links|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e53bd984331f658e153100fff162bad98b1b657a)|2018-07-19 14:53:23
|1195|djmitche|Bug 1476441 - fix relative docs links|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a307e102b111c62391c87aaf2191a76295805cf6)|2018-07-18 21:59:23
|1194|djmitche|clean up Procfile|[URL](https://github.com/taskcluster/taskcluster-queue/commit/af3862821d4541f8d07f0971ca19991f43d36312)|2018-07-12 22:46:39
|1193|djmitche|Merge pull request #280 from djmitche/poll-deprecated  Mark claimTask and pollTaskUrls as deprecated|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ee26ba9257aa05b11e29adae7e961e3d5b885005)|2018-07-02 19:51:57
|1192|djmitche|Mark claimTask and pollTaskUrls as deprecated  Both are deprecated, part of the same process where workers interact directly with Azure queues.  This also adds some docs for claimWork.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/cdab20dfb42de222dda15c6d77fb7efe0f092d7e)|2018-07-02 18:03:02
|1191|djmitche|Merge pull request #279 from djmitche/bug1462758  Bug 1462758 - upgrade queue to use newest libraries, rootUrl|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3c6626cfe32d54b9bef470398e3576c23e90fc25)|2018-07-02 17:34:33
|1190|djmitche|Bug 1453514 - remove intermittent comment from test/queueservice_test.js|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4c8d7d14ec14d2153bbf57875d424e860b1bea3b)|2018-06-29 16:20:21
|1189|djmitche|Bug 1462758 - make taskgroup_test more robust|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5ba3228ecbe0a125b382211de1fce8ef76ccae88)|2018-06-21 18:04:58
|1188|djmitche|Bug 1462758 - add .taskcluster.yml  Also fix up the handling of secrets fetched from the secrets service|[URL](https://github.com/taskcluster/taskcluster-queue/commit/89105d82e642b6d0aae410654747407791df3c69)|2018-06-20 21:54:28
|1187|djmitche|Bug 1462758 - always set something as a rootUrl|[URL](https://github.com/taskcluster/taskcluster-queue/commit/48791467eb4c0e26683f567c0f923e14be559b10)|2018-06-20 21:38:36
|1186|djmitche|Bug 1462758 - use consistent names for resolvers  I like "reaper" but "resolver" was used more often so I changed everything to that name.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5ced0ec5fbe06d9b6ceb70b3f624e8ff6447466f)|2018-06-20 20:55:57
|1185|djmitche|Bug 1462758 - update tests to new best practices  This includes introducing a mock QueueService.  Support for testing poll-tasks is removed, as it is no longer used and rather difficult to test.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/be7b47907ebf394a5fe6eb092463a2a0c0926ee1)|2018-06-16 23:56:18
|1184|djmitche|Bug 1462758 - remove hard-coded forceSSL|[URL](https://github.com/taskcluster/taskcluster-queue/commit/45067d454023cd9acf410b40f5d030b80b6598c5)|2018-06-15 22:20:40
|1183|djmitche|Bug 1462758 - don't hard code bucket regions|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e5a686523bebf26ebdeff227e2f868c8a0ae2de9)|2018-06-15 21:56:58
|1182|djmitche|Bug 1462758 - don't hard code bucket names|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4e57c3d15d93b8fd09e41f4bc4d15ba4a3cc7752)|2018-06-15 21:45:40
|1181|djmitche|Bug 1462758 - update all libraries (tests not passing yet)|[URL](https://github.com/taskcluster/taskcluster-queue/commit/63963da662f53ceedc2129d2c07f1c22c3e59ca4)|2018-06-15 21:06:41
|1180|djmitche|Merge pull request #278 from djmitche/worker-put-not-found  Handle a PUT to a worker that doesn't exist|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f8abdea320b81828ce89e3e03cc8706d02d649ee)|2018-05-24 13:07:23
|1179|djmitche|Handle a PUT to a worker that doesn't exist|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a6a024988acc8f73bff97cf24fc47fc597845025)|2018-05-23 20:37:39
|1178|djmitche|Merge pull request #277 from djmitche/bug1463473  Bug 1463473 - don't expire quarantined hosts|[URL](https://github.com/taskcluster/taskcluster-queue/commit/37e8f8b9fd5ccb21645bce42127f3a3b5004726c)|2018-05-22 17:14:34
|1177|djmitche|Bug 1463473 - don't expire quarantined hosts|[URL](https://github.com/taskcluster/taskcluster-queue/commit/502c81c2e574e4fbbf8e8de3726ddd671217ded5)|2018-05-22 15:55:48
|1176|petemoore|Merge pull request #274 from djmitche/rm-schema-1  remove spurious file|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1e4786b103eff3b79f21d4146842838f34d84a63)|2018-05-03 11:03:44
|1175|djmitche|Bug 1451390 - upgrade tc-lib-docs to start publishing again; a=bstack|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0197685cf1d9a8ecf7ec932e213f5f5ca9eb50a0)|2018-04-25 18:46:53
|1174|jhford|have encodable urls in tests|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0e2d225879633041843a0dbcad5b41c5bd14d026)|2018-04-17 15:13:35
|1173|jhford|Test signed URLs for S3 storage type (non-blob)|[URL](https://github.com/taskcluster/taskcluster-queue/commit/8c14e33ff0ea1ad1ef7b1407b5e309ec51ef4cd7)|2018-04-16 16:11:32
|1172|jhford|document special headers and download flow|[URL](https://github.com/taskcluster/taskcluster-queue/commit/44ee922128a5c0486ad59d0b59bc8e57135156b5)|2017-12-06 14:48:43
|1171|jhford|Clean up the logic about skipping and add a Skip-CDN option|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a98b86b95411554534980c65bdf0c2ce0c0623e6)|2017-11-22 16:02:20
|1170|jhford|Set some informational headers on artifact responses|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0505155bb9805664520ffd1053c63dab9b651918)|2017-11-22 14:23:01
|1169|jhford|Test signed urls with blob artifacts|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3828ecd962cf1a6c329e6c0858aca6756c510b1d)|2018-04-16 14:45:21
|1168|jonasfj|Merge pull request #276 from taskcluster/upgrade-azure-entities  Force upgrade of fast-azure-storage|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9f04a2cfe959dd4c562223ab76b4fcd6a34165b2)|2018-04-20 13:59:27
|1167|jonasfj|force upgrade of azure-entities, to get better error messages from fast-azure-storage|[URL](https://github.com/taskcluster/taskcluster-queue/commit/309a3cb8b2c4ab0fabb90c843943b554e961ddb6)|2018-04-20 13:11:50
|1166|djmitche|Bug 1453725 - fix .git-version filename|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e107c590dc984ed33e52058429393c93b271e24f)|2018-04-19 14:53:09
|1165|djmitche|Merge pull request #275 from djmitche/bug1452611-c  Bug 1452611 - make fingerprint a list, add one more signature|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9ca8b2720e9d42f9f43ac5909ce8a08da6906e10)|2018-04-18 20:11:58
|1164|djmitche|Bug 1452611 - make fingerprint a list, add one more signature|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4247716c7291511613e9ec31f85236057a62ed6f)|2018-04-18 20:11:16
|1163|djmitche|remove spurious file|[URL](https://github.com/taskcluster/taskcluster-queue/commit/28dada021a3ff7e866ef71cd46ac30a30a05c37f)|2018-04-18 20:09:12
|1162|djmitche|Merge pull request #269 from djmitche/bug1452611-b  Bug 1452611 - fingerprint SSL errors|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c71f8bc7362c033315f934763fdcbfb4eab28568)|2018-04-18 19:39:01
|1161|djmitche|Merge pull request #271 from djmitche/bug1434921  Bug 1434921 - use continuation token pattern in params|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0ba07673749a4fc73b9a8df90bb1ae441cef2258)|2018-04-18 18:06:23
|1160|petemoore|Merge pull request #273 from taskcluster/fix-tcqueueevent-schemas  Adjust schema titles for consistency|[URL](https://github.com/taskcluster/taskcluster-queue/commit/081663053eeead80720158204ac4e58bfb164929)|2018-04-18 16:27:31
|1159|petemoore|Adjust schema titles for consistency and to improve downstream golang tcqueueevents generated types|[URL](https://github.com/taskcluster/taskcluster-queue/commit/25e8db166003807767a90100ebedcc9aa5b2e68f)|2018-04-18 16:19:27
|1158|petemoore|Merge pull request #272 from taskcluster/task-definition-and-status  Moved task definition and status into task-definition-and-status.yml|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7a67020f67835f4386518c58e70b515a1631973e)|2018-04-18 10:57:44
|1157|petemoore|Moved task definition and status into task-definition-and-status.yml|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2bfa305c379750de8242d64d61554c04fb0d1227)|2018-04-18 06:47:54
|1156|petemoore|Merge pull request #270 from taskcluster/more-schema-cleanup  Hopefully last round of cleanup|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4cacffa0020725276069e74901bac0b1ebe548bf)|2018-04-18 06:04:29
|1155|djmitche|Bug 1434921 - use continuation token pattern in params|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3c103b89c2d5e9b1fb69faa9925a86fb88c59138)|2018-04-17 17:26:49
|1154|petemoore|Hopefully last round of cleanup|[URL](https://github.com/taskcluster/taskcluster-queue/commit/879f87fac512980293cdb686f203d7ed9365c1b8)|2018-04-17 17:06:09
|1153|petemoore|Merge pull request #268 from taskcluster/actions-schema-fix  Some extra changes missed in #262|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4c8e10c1bc0b6795fd9e18e9a702bd3eb1f66eba)|2018-04-17 15:01:12
|1152|djmitche|Bug 1452611 - fingerprint SSL errors|[URL](https://github.com/taskcluster/taskcluster-queue/commit/74e6282630a544d517318cc70b28fcad3a337db0)|2018-04-17 14:41:34
|1151|petemoore|Some extra changes missed in #262|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f5544ed7ce5e0cbc0f75ed10a1c707676f6bc15b)|2018-04-17 14:34:51
|1150|jonasfj|Merge pull request #266 from taskcluster/upgrade-fast-azure-storage  Upgrade fast-azure-storage|[URL](https://github.com/taskcluster/taskcluster-queue/commit/8473bfe53eb31f662f7609e9da1b3f5f86c0bda9)|2018-04-17 12:13:23
|1149|jonasfj|upgrade fast-azure-storage|[URL](https://github.com/taskcluster/taskcluster-queue/commit/59eb4316e61e193d5989c79786638ef919f31e92)|2018-04-17 12:12:31
|1148|djmitche|Merge pull request #267 from djmitche/bug1452000  Bug 1452000, 1453724, 1453725 - upgrade tc-lib-monitor for greater good|[URL](https://github.com/taskcluster/taskcluster-queue/commit/abcef54bea5398cd38af88117ece4ad7c7531337)|2018-04-16 21:27:23
|1147|djmitche|Bug 1452000, 1453724, 1453725 - upgrade tc-lib-monitor for greater good|[URL](https://github.com/taskcluster/taskcluster-queue/commit/79ea2eb733a3fd2ad320c913781dbdd007600dfb)|2018-04-16 21:22:55
|1146|jhford|Revert 5733666..f1ef234|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b40a1da8831b97a4646b39c28ff3e8d1a47d5cdf)|2018-04-16 14:28:57
|1145|jhford|document special headers and download flow|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f1ef2345a23d5f578939fa7cb6b1c6b6ac6c9893)|2017-12-06 14:48:43
|1144|jhford|bug 1419577 -- URL Encode the prefix portion of S3 urls  It turns out that regardless of what we put into the prefix, S3 will URL Encode some characters of the prefix (e.g. + will always be encoded to %2B).  This results in broken URLs.  This approach is the simple approach of just encoding the entire S3 Object Key.  I've verified that with a problem URL (e.g. has + in it) that this encoding results in valid URLS which get 200 from S3 instead of 403s.  I've also verified that Cloudfront also supports this encoding.  Another approach for prettier URLs would be to revert the %2F character back to a / character since S3 and CloudFront already deal with those characters quite well.  This would require prefix = encodeURIComponent(prefix).replace(/%2f/gi, "/");|[URL](https://github.com/taskcluster/taskcluster-queue/commit/be13f1899e2a5a8541ef9c08c685424bb4cf1707)|2017-11-22 16:02:48
|1143|jhford|Clean up the logic about skipping and add a Skip-CDN option|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a0ba7844a7b67133ebc8bcf220343c0ff37f72bc)|2017-11-22 16:02:20
|1142|jhford|Set some informational headers on artifact responses|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5733666ddeecb8d302dd7d1075676d0c98a44bda)|2017-11-22 14:23:01
|1141|petemoore|Merge pull request #262 from taskcluster/actions-schemas  Reduced duplication of actions in schemas, and updated titles and descriptions|[URL](https://github.com/taskcluster/taskcluster-queue/commit/01417abcd289ba538c2e74fb6bf87ce41f76fc6e)|2018-04-16 08:55:28
|1140|petemoore|Reduced duplication of actions in schemas, and updated titles and descriptions|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4b2625dc4040e778a35a04129b81c357f38c54fc)|2018-04-16 08:40:10
|1139|djmitche|Merge pull request #263 from djmitche/bug1453866  Bug 1453866 - bump s3 upload expiry to 45 minutes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/50c4640554fad9c68cd8c00a5e3d736c32431e42)|2018-04-13 18:17:50
|1138|djmitche|Bug 1453866 - bump s3 upload expiry to 45 minutes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/58ef65274516d0d5b3a72b07fa200aa979a01e2a)|2018-04-13 17:57:57
|1137|djmitche|Merge pull request #259 from djmitche/bug1434322-b  Bug 1434322 - return 404's when appropriate and always upsert upstream objects|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0e9562aa158634ffcdb99510e3545ece954107aa)|2018-04-12 16:43:07
|1136|djmitche|fix node version in travis|[URL](https://github.com/taskcluster/taskcluster-queue/commit/39f49dee3b2a9b17654f25618e32625c624fefb6)|2018-04-12 15:23:12
|1135|djmitche|Merge taskcluster/taskcluster-queue:try-node-8-10 (PR #261)|[URL](https://github.com/taskcluster/taskcluster-queue/commit/bb8f192f0edeb0e1d6f65fca0a04eb5559e88fc4)|2018-04-12 14:56:47
|1134|jonasfj|hack to try node 8.10.0 to see if this fixes SSL issues|[URL](https://github.com/taskcluster/taskcluster-queue/commit/773bde3bce3e950c2d717ea64e5f8d9dc7e867e9)|2018-04-12 14:53:33
|1133|jonasfj|Merge pull request #199 from taskcluster/count-claim-work  Count claimWork calls|[URL](https://github.com/taskcluster/taskcluster-queue/commit/30891e429b7c4701c29d9997c9501c265c560d48)|2018-04-12 14:42:51
|1132|jonasfj|Count claimWork calls  We can use this to create alerts in signalfx, if some workerType isn't claiming work anymore...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d226c5882fc5ff6379c26fd413b5f503eac18be4)|2017-09-12 21:42:14
|1131|jonasfj|Merge pull request #258 from djmitche/remove-unnecessary-errorCodes  Remove custom InputError definition, since lib-api supports it|[URL](https://github.com/taskcluster/taskcluster-queue/commit/cf16cc530dd57c1bba5747ea04919c156b494132)|2018-04-12 13:43:02
|1130|jonasfj|Merge pull request #260 from djmitche/bug1453514-disable  Bug 1453514 - disable intermittent test|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1221bef13e104ba7b43a1fb92c5d8338b27142bf)|2018-04-12 13:42:51
|1129|djmitche|Bug 1453514 - disable intermittent test|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3f78f8c5e6e1c349ad8da9f9c2c61e82249a09b1)|2018-04-11 23:17:29
|1128|djmitche|Bug 1434322 - factor out upserting|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7ed2624a0f0b5f82f513bdc603f166f5ab7e4972)|2018-04-11 23:03:15
|1127|djmitche|Bug 1434322 - Return 404's, and ensure parent objects exist  Declaring a worker should also declare workerType and provisioner; declaring a workerType should also delcare a provisioner.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/8321592dba60036450d494dfe311109931cce8fb)|2018-04-11 22:38:26
|1126|djmitche|Bug 1434322 - Refactor worker info tests  Use common object-creation helpers|[URL](https://github.com/taskcluster/taskcluster-queue/commit/50eafee62b1b454c47a9c267dccf98809251813e)|2018-04-11 22:07:08
|1125|djmitche|Bug 1434322 - Retry to claim all 30 tasks (fix flaky test)  Since claimTask uses a real Azure queue, sometimes the messages don't arrive in time, so call claimTasks a few times until we get all 30..|[URL](https://github.com/taskcluster/taskcluster-queue/commit/802421ef0883865349994af29af234f57929493f)|2018-04-11 21:38:54
|1124|djmitche|Remove custom InputError definition, since lib-api supports it|[URL](https://github.com/taskcluster/taskcluster-queue/commit/cac32f13a34bf1e34f170e4f16eb62cd128f4ebd)|2018-04-11 20:53:29
|1123|djmitche|Merge pull request #256 from djmitche/relative-svg-links  Use relative links for svgs in docs|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7a3b2af2c3241b46f5f6bc1cbd28dd865bbab313)|2018-04-04 22:06:39
|1122|djmitche|Use relative links for svgs in docs  The tools build process prefers this; otherwise, it doesn't really matter..|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f37b304e5a246ed6d0f6897c8966994b5bd671e4)|2018-04-04 21:40:27
|1121|djmitche|Merge pull request #255 from djmitche/bug1436212  Bug 1451390 - add write-docs proc, use PUBLISH_METADATA|[URL](https://github.com/taskcluster/taskcluster-queue/commit/11f437e23c2f81c7a6fe4a130edf95064faca157)|2018-04-04 19:44:05
|1120|djmitche|Bug 1451390 - add write-docs proc, use PUBLISH_METADATA|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1d617c78d15a579fb0893d010d6b581dd67c694c)|2018-04-04 18:58:32
|1119|djmitche|Upgrade tc-lib-api for bugfix|[URL](https://github.com/taskcluster/taskcluster-queue/commit/52e6e333a0b7759db5431638502c562fba4a4cab)|2018-04-03 18:48:27
|1118|djmitche|Merge pull request #254 from djmitche/escape-markdown  Bug 1449848 - Escape markdown (by upgrading tc-lib-api)|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5c1cc2136b420dbeb640b254096493768404c865)|2018-04-03 17:01:41
|1117|djmitche|Bug 1449848 - Escape markdown (by upgrading tc-lib-api)|[URL](https://github.com/taskcluster/taskcluster-queue/commit/249303fbd08eb1f14cf28ac9433a8eff30ee2044)|2018-04-03 14:49:26
|1116|djmitche|Merge pull request #246 from djmitche/Procfile-syntax  Add colons where they belong in Procfile|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d1fc88ce0cd50b35b354a883ed4b3720e0663aaf)|2018-03-30 15:32:58
|1115|djmitche|Add existing context items to the list|[URL](https://github.com/taskcluster/taskcluster-queue/commit/634c6e80d9ffe12b571d9fe0a02d47d12e710126)|2018-03-30 15:01:19
|1114|djmitche|Merge pull request #253 from kritisingh1/upgrade  upgrade taskcluster-lib-api to version 8.0.0|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f45f3cd71cf885f3b5b224f4f2b68ff1cb4eb8fc)|2018-03-30 14:45:26
|1113|kritisingh1|upgrade taskcluster-lib-api to version 8.0.0|[URL](https://github.com/taskcluster/taskcluster-queue/commit/35155ec2d795263f183d2f1b331568f6205f5ae4)|2018-03-22 07:01:18
|1112|djmitche|Merge pull request #252 from fiennyangeln/upgrade-lib-api  Upgrade taskcluster-lib-api version|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3185a5b4767574fe4cd90cbdfec183fa5c3ab2ba)|2018-03-12 14:54:27
|1111|fiennyangeln|Upgrade taskcluster-lib-api version  Upgrade taskcluster-lib-api version to the newest one. It is to enable Access-Control-Max-Age  Related to Bug 1442636|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1e9f7be66dc93138f83b7d3177d70398fdeca387)|2018-03-09 15:07:09
|1110|imbstack|Update to new lib-api|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2c8f8f5f07655356cf2d1dcad31730a19270402f)|2018-02-09 18:48:57
|1109|imbstack|Merge pull request #244 from taskcluster/update-to-scope-expressions  Update to new taskcluster-lib-api with scope expressions|[URL](https://github.com/taskcluster/taskcluster-queue/commit/365602426928be979755201043c0a88cf03e26a7)|2018-02-08 00:04:44
|1108|imbstack|Update to new taskcluster-lib-api with scope expressions|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1a696975993e6aa469da0dc23a0e0c770ee8d1c6)|2018-01-18 01:19:28
|1107|djmitche|Bug 1434322 - missed git-add|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ce102d8e19d9de3085e600114ef2bfa5c50a2bfa)|2018-01-30 20:16:02
|1106|djmitche|Bug 1434322 - create provisioners for other tests, too|[URL](https://github.com/taskcluster/taskcluster-queue/commit/edf512f8158cb965a988572f18fee0f6fab690ba)|2018-01-30 19:54:41
|1105|djmitche|Merge pull request #247 from djmitche/bug1434322  Bug 1434322 - handle worker types not found|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d0260a20e7d54945848dc24c4ad2226893279648)|2018-01-30 18:07:05
|1104|djmitche|Bug 1434322 - handle worker types not found|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9a7babd7199cf2ad45f128f624b06e8a7563bde7)|2018-01-30 17:05:14
|1103|djmitche|Add colons where they belong in Procfile  Apparently Heroku's parsing of Procfiles is pretty generous..|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ee352072b0111998fe0dc6445e85bf7b6cc3fcce)|2018-01-24 23:28:42
|1102|djmitche|restore aws-sdk-promise, too|[URL](https://github.com/taskcluster/taskcluster-queue/commit/04c3c40d80273ccfd7d14ead3a46cf798e0882ff)|2018-01-24 20:14:42
|1101|djmitche|Merge pull request #245 from djmitche/redeploy-spring-cleaning  Redeploy spring cleaning|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5898a27dc1145b318129bcfaef1084c5a6fa3064)|2018-01-24 19:49:59
|1100|djmitche|Bug 1432183 - pin version of AWS SDK at 2.1.22  Newer versions generate valid URLs that cause failures in cloud-mirror; cloud-mirror cannot be redeployed to fix this issue, so we will hold back aws-sdk in the queue until cloud-mirror is turned off.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d1bc912764f66f5a4489a90782428e98ee32bc50)|2018-01-24 18:46:05
|1099|djmitche|Re-land pull request #240 from taskcluster/spring-cleaning-fall-2017  This reverts commit e9726d143240d230626761e7a2eb7fa2f13fa25f.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a8908c3dbec6c8668bc8c2afce56c98b0d701d77)|2018-01-24 18:44:59
|1098|djmitche|Revert "Re-land pull request #240 from taskcluster/spring-cleaning-fall-2017"  This reverts commit b804b4e6fa9e44b85b97b141fcc7d68911406428.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e9726d143240d230626761e7a2eb7fa2f13fa25f)|2018-01-24 16:59:30
|1097|djmitche|Revert "Re-upgrade AWS-SDK"  This reverts commit 354fd0c54b7a21853383b474154b1b1e606c435f.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/97535c132336e9f5df7f9f5f805b6a60f4c19712)|2018-01-24 16:59:23
|1096|djmitche|Re-upgrade AWS-SDK|[URL](https://github.com/taskcluster/taskcluster-queue/commit/354fd0c54b7a21853383b474154b1b1e606c435f)|2018-01-24 15:46:56
|1095|djmitche|Re-land pull request #240 from taskcluster/spring-cleaning-fall-2017  This reverts commit 305db6763c96537d459b4f0f63a92924b8e24aae re-landing 01c3013c80decc31bc79bd1d128d271e77924dca.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b804b4e6fa9e44b85b97b141fcc7d68911406428)|2018-01-24 14:54:04
|1094|djmitche|Revert all of "Merge pull request #240 from taskcluster/spring-cleaning-fall-2017"  This reverts commit 01c3013c80decc31bc79bd1d128d271e77924dca, reversing changes made to a2007b195c0cd875b64ea29372731ccd5e760fc5.  Earlier partial reverts did not work.  This upgrade caused a URL change which led to the outage in https://github.com/taskcluster/taskcluster-retrospectives/blob/master/retrospectives/2018-01-18-spring-cleaning-url-change.md|[URL](https://github.com/taskcluster/taskcluster-queue/commit/305db6763c96537d459b4f0f63a92924b8e24aae)|2018-01-22 16:16:47
|1093|djmitche|include yarn.lock too|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4760993253b5d83712ceb3cc5298434b612856df)|2018-01-22 15:46:25
|1092|djmitche|Bug 1432183 - Go back to the old AWS-SDK version  This is a partial revert of a8c1f01734d7457af1fe23bb0e406a0b78043228. This upgrade caused a URL change which led to the outage in https://github.com/taskcluster/taskcluster-retrospectives/blob/master/retrospectives/2018-01-18-spring-cleaning-url-change.md|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0beb33f6680f2121685af292b420c2eb518b8d43)|2018-01-22 15:28:02
|1091|petemoore|Merge pull request #243 from taskcluster/bug1431750  Bug 1431750 - add additionalProperties to schemas where missing|[URL](https://github.com/taskcluster/taskcluster-queue/commit/fcd0931e4be512113949c3ec25da66cdf1174fda)|2018-01-22 14:58:52
|1090|petemoore|Bug 1431750 - add additionalProperties to schemas where missing|[URL](https://github.com/taskcluster/taskcluster-queue/commit/181bb23fe0a3890f989c1c88e208b8a971f61324)|2018-01-19 17:13:19
|1089|djmitche|Merge pull request #240 from taskcluster/spring-cleaning-fall-2017  Spring cleaning fall 2017|[URL](https://github.com/taskcluster/taskcluster-queue/commit/01c3013c80decc31bc79bd1d128d271e77924dca)|2018-01-18 14:48:30
|1088|djmitche|upgrade typed-env-config|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7d458f171a916e669337013b33a3db4cc2061720)|2017-12-22 01:10:03
|1087|djmitche|upgrade remotely-signed-s3|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a8bf5693199d474a79d00f0ae6a1fe48be3414ac)|2017-12-22 01:05:39
|1086|djmitche|upgrade taskcluster-client|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e7767495e250d1ebacca6c57e6037c1343f5d5b6)|2017-12-22 01:05:23
|1085|djmitche|upgrade tc-lib-app|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b54453dc549492bda96d5f26616fd16fb5b45c07)|2017-12-22 01:04:59
|1084|djmitche|upgrade tc-lib-loader, -app, -docs, and pulse-publisher|[URL](https://github.com/taskcluster/taskcluster-queue/commit/879be6137aebd1c54a0a7db5c5e589c61ee9cc63)|2017-12-22 00:55:52
|1083|djmitche|upgrade some simple stuff|[URL](https://github.com/taskcluster/taskcluster-queue/commit/95f55aeb0597aac1bcdf2ff07ef0e238c1ed7454)|2017-12-22 00:50:25
|1082|djmitche|upgrade mocha|[URL](https://github.com/taskcluster/taskcluster-queue/commit/27cf70cde0ebb23e4c14eaec2713bd10f5bf278e)|2017-12-22 00:29:14
|1081|djmitche|upgrade url-join, move to devDependencies|[URL](https://github.com/taskcluster/taskcluster-queue/commit/17aa45d374decd69932725abeaa43954ae315155)|2017-12-22 00:27:42
|1080|djmitche|upgrade azure libs  Changes are based on   https://github.com/Azure/azure-storage-node/blob/d789db2de5185b28486638d2513e4ef2b07ecf1f/BreakingChanges.md|[URL](https://github.com/taskcluster/taskcluster-queue/commit/335676f61c88e58cdb82990b0a6d812132e1db8b)|2017-12-22 00:26:15
|1079|djmitche|remove promise|[URL](https://github.com/taskcluster/taskcluster-queue/commit/84db4afb840db4e3976c591b711ee75cf16cb928)|2017-12-22 00:15:49
|1078|djmitche|upgrade thirty-two, xml2js, xmlbuilder, and move the latter two to devDependencies|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c73a1f585ed54cce74b8e1f336838e1f2ddf0ee4)|2017-12-22 00:09:53
|1077|djmitche|upgrade tc-lib-validate|[URL](https://github.com/taskcluster/taskcluster-queue/commit/bbdd47fa32ab3e774694ac2df1d8be89a6e5c184)|2017-12-22 00:06:31
|1076|djmitche|remove aws-sdk-promise and upgrade aws-sdk|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a8c1f01734d7457af1fe23bb0e406a0b78043228)|2017-12-22 00:04:44
|1075|djmitche|Upgrade superagent|[URL](https://github.com/taskcluster/taskcluster-queue/commit/05444e36e921d521665a06921e2fbbc70fb9d7b1)|2017-12-21 23:56:01
|1074|djmitche|stop compiling|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9b9b5ef3508b4e60c4e979868c277942571e7d89)|2017-12-21 23:26:02
|1073|djmitche|Fix up lint|[URL](https://github.com/taskcluster/taskcluster-queue/commit/19d827e904da5be61bf3522849ab2e92fbf981fd)|2017-12-21 23:17:33
|1072|petemoore|Merge pull request #239 from taskcluster/bug1249045  Bug 1249045 - issue named temporary credentials to tasks|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a2007b195c0cd875b64ea29372731ccd5e760fc5)|2018-01-08 16:00:26
|1071|petemoore|Relocate task credential creation into separate module|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9f42fa7f5fc50bc9e2753aeddd89797318110cbb)|2018-01-08 15:16:17
|1070|djmitche|Merge pull request #241 from djmitche/source-url  Bug 1427305 - limit source URLs to https?://|[URL](https://github.com/taskcluster/taskcluster-queue/commit/54967840fe8ee0834961ae326c0436967aee895d)|2018-01-04 16:10:40
|1069|djmitche|Bug 1427305 - limit source URLs to https?://|[URL](https://github.com/taskcluster/taskcluster-queue/commit/984929d1a7792344c51129e7d26a4104b65c86ac)|2018-01-03 22:52:32
|1068|petemoore|Bug 1249045 - issue named temporary credentials to tasks|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6ccfc3b3b4207078b0272ece37c6befdc21bec4b)|2017-12-21 12:58:29
|1067|djmitche|Merge pull request #237 from helfi92/action-docs  Docs: Recommend returning early for actions|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0ce0e1940dde8851e9a352452c1cc10e9d6202c0)|2017-12-05 20:52:24
|1066|helfi92|Docs: Recommend returning early for actions|[URL](https://github.com/taskcluster/taskcluster-queue/commit/42aeda17ebffaae8a763a8af6e3d326164a2c72b)|2017-12-05 19:55:07
|1065|helfi92|Handle server error (#236)  We want to be able to handle the error when the resource is not found.  The azure load method will throw an error if the row does not exist,  unless its second argument is `true`.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ccac868c7944e233cbf76f0d9bc7c52271cc9145)|2017-12-05 19:04:15
|1064|petemoore|Merge pull request #235 from taskcluster/more-null-fixing  Make quarantineUntil an optional field, rather than allowing null value|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f94279467fbaf81b48b4f87ffdeb6c61ca48af0e)|2017-11-28 14:07:49
|1063|petemoore|all type properties are now a single string rather than an array in json schemas|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6ec98e6489e424cf8fe7415ace350e16d6d9fcc3)|2017-11-28 13:51:47
|1062|petemoore|Revert "Revert "Merge pull request #232 from taskcluster/use-required-in-preference-to-null""  This reverts commit 8a9ebb307a6c88a4f0670c6ac1c29507a09d4ef1.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/48dd91b579eac93932aba98907cd1dbeb1074f94)|2017-11-28 07:36:57
|1061|djmitche|Revert "Merge pull request #232 from taskcluster/use-required-in-preference-to-null"  This reverts commit 77093220532779ca0ac9c593e8211d1313d1560b, reversing changes made to 1079d4690b12efbae44715f200ae78940e7d5ca3.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/8a9ebb307a6c88a4f0670c6ac1c29507a09d4ef1)|2017-11-27 17:06:23
|1060|djmitche|Merge pull request #232 from taskcluster/use-required-in-preference-to-null  Make property optional rather than returning null value|[URL](https://github.com/taskcluster/taskcluster-queue/commit/77093220532779ca0ac9c593e8211d1313d1560b)|2017-11-27 16:54:10
|1059|jhford|Don't mutate an entity when not persisting the change  We're not persisting the change, so let's not mutate the internal data structures.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ff5b43a7d8bd86fdc245bbb38d39cb71ab93fe6a)|2017-11-24 16:36:50
|1058|jhford|latestTask shouldn't be mandatory  in the code on master branch, non of the fields are actually required. This field clearly won't be there if there wasn't a latestTask.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/37886ab6e4c2caa4ef08819e99c9e206b811f4ca)|2017-11-24 16:36:02
|1057|jhford|Only include quarantineUntil when useful  Note that this is still failing with the following exception.  I'm not sure what the cause is.    base:api Error occurred handling: /provisioners/prov1/worker-types/gecko-b-2-linux/workers, err: Error: Output schema validation error: Schema Validation Failed! Rejecting Schema: http://schemas.taskcluster.net/queue/v1/list-workers-response.json# Errors:     data.workers[0] should have required property 'latestTask', as JSON: {"schema":"http://schemas.taskcluster.net/queue/v1/list-workers-response.json#","url":"/provisioners/prov1/worker-types/gecko-b-2-linux/workers","payload":{"workers":[{"workerGroup":"my-worker-group","workerId":"my-worker","firstClaim":"2017-11-24T16:14:15.093Z"}]}}, incidentId: b1e571d4-770e-454b-8e0e-8396366f9650 Error: Output schema validation error: Schema Validation Failed! Rejecting Schema: http://schemas.taskcluster.net/queue/v1/list-workers-response.json# Errors:     data.workers[0] should have required property 'latestTask'     at ServerResponse.res.reply (/home/jhford/taskcluster/taskcluster-queue/node_modules/taskcluster-lib-api/src/api.js:159:21)     at Object._callee29$ (/home/jhford/taskcluster/taskcluster-queue/src/api.js:2407:14)     at tryCatch (/home/jhford/taskcluster/taskcluster-queue/node_modules/regenerator-runtime/runtime.js:65:40)     at Generator.invoke [as _invoke] (/home/jhford/taskcluster/taskcluster-queue/node_modules/regenerator-runtime/runtime.js:303:22)     at Generator.prototype.(anonymous function) [as next] (/home/jhford/taskcluster/taskcluster-queue/node_modules/regenerator-runtime/runtime.js:117:21)     at step (/home/jhford/taskcluster/taskcluster-queue/node_modules/babel-runtime/helpers/asyncToGenerator.js:17:30)     at /home/jhford/taskcluster/taskcluster-queue/node_modules/babel-runtime/helpers/asyncToGenerator.js:28:13     at <anonymous>     at process._tickDomainCallback (internal/process/next_tick.js:228:7) +0ms|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ac6acc21e0c4182ee8e638d1f56a4e40b97d7478)|2017-11-24 16:16:08
|1056|petemoore|Make property optional rather than returning null value|[URL](https://github.com/taskcluster/taskcluster-queue/commit/8eacd843c3643ab4479986b41f5f0b4800510c3c)|2017-11-22 14:06:35
|1055|helfi92|Remove actions when listing workerTypes and workers (#231)|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1079d4690b12efbae44715f200ae78940e7d5ca3)|2017-11-21 18:59:26
|1054|helfi92|Bug 1414364 - Switch the disabled property of a worker to quarantineUntil (#222)    Bug 1414364 - Switch the disabled property of a worker to quarantineUntil      Omit quarantineUntil when lt; date. Fix clock skew. Clarify comment      listWorkers quarantineUntil property displayed only when quarantined      Return null when quarantineUntil is in the past      Make listWorkers to filter on quarantined instead of quarantineUntil|[URL](https://github.com/taskcluster/taskcluster-queue/commit/8ff1500485511d7723ecb3beac7925230de85c0b)|2017-11-19 21:09:10
|1053|djmitche|Merge pull request #230 from djmitche/more-actions-docs  Expand Queue Actions documentation|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5487efba5f5f21bf7c10acc29e7e941b6bd5f3a0)|2017-11-16 21:17:20
|1052|djmitche|Expand Queue Actions documentation  This    defines the provisioner / worker-type / worker hierarchy a little    better    distinguishes queue actions from task actions    removes specific reference to the tools UI views    gives more detail on how calls can occur from automation, including    use of the `name` property    sets an explicit order for queue docs  It presupposes some planned changes to the queue APIs; in particular, that actions be returned from the getXxx methods and not from the listXxx methods.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/65a60dcfe653bb8913c5c3cf1e74709aa4b45348)|2017-11-16 17:39:24
|1051|helfi92|Merge pull request #228 from taskcluster/fix-worker-response-schema  Fix worker response schema|[URL](https://github.com/taskcluster/taskcluster-queue/commit/647d87188d6741606412b089fc2751eced7ee277)|2017-11-13 13:38:50
|1050|petemoore|Define actions/items/method property in worker-response.yml|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a5255c1b48b57e9c85d874a9aca09049466b552a)|2017-11-13 10:35:27
|1049|petemoore|Add last line line endings in yml files|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c70fe4d77353fab14d7f682db375afdce25af77d)|2017-11-13 10:35:18
|1048|helfi92|Merge pull request #227 from helfi92/action-docs  Hotfix remove uri format from schema since we're using <parameter>|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1b841d188d11e0ebf0d5fd02dd0473a7fd45e307)|2017-11-09 20:27:27
|1047|helfi92|add method in schema|[URL](https://github.com/taskcluster/taskcluster-queue/commit/95755694e173adb9932b96dfd85110372c47da73)|2017-11-09 20:24:12
|1046|helfi92|Hotfix|[URL](https://github.com/taskcluster/taskcluster-queue/commit/820f01bc9009a6bc67830d129df9e9bd4cb7faf0)|2017-11-09 20:20:09
|1045|helfi92|Merge pull request #226 from helfi92/docs-action  Docs: escape greater than and lesser than symbols|[URL](https://github.com/taskcluster/taskcluster-queue/commit/01ee50305e49cd4cae1ac50db126d792f04f3298)|2017-11-09 19:52:49
|1044|helfi92|escape < and >|[URL](https://github.com/taskcluster/taskcluster-queue/commit/467d10b4e2ca4808d703aa5277df8dbdfc95dd3a)|2017-11-09 19:48:57
|1043|helfi92|Merge pull request #223 from helfi92/modify-action  Modify action explanations to reflect path parameters|[URL](https://github.com/taskcluster/taskcluster-queue/commit/967b51a3497063b4800e5d263fbe6fa330b9ea60)|2017-11-09 19:38:06
|1042|helfi92|Merge pull request #225 from helfi92/action-docs-nit  action docs nit (remove GET from action method)|[URL](https://github.com/taskcluster/taskcluster-queue/commit/85f1ff8a6283118dfc3ffb075cbeeecc61888036)|2017-11-09 19:22:00
|1041|helfi92|action docs nit (remove GET from action method)|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6dc6a1066a7d2e660557c21dd22b702f5a32b20c)|2017-11-09 19:18:25
|1040|helfi92|Remove get from method|[URL](https://github.com/taskcluster/taskcluster-queue/commit/90b5e6ad552829ed8befbe5bf6514c39952f75dd)|2017-11-09 19:16:49
|1039|helfi92|Add method property to action|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6cd3a704c261e296cd3217fd5b38e3ca9ea12de0)|2017-11-09 16:38:11
|1038|helfi92|Use <parameter> instead of :parameter|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e06e0137258868433710f19e5a4a9a85b5a01fe2)|2017-11-08 21:51:22
|1037|helfi92|Fix grammar|[URL](https://github.com/taskcluster/taskcluster-queue/commit/37f6bb82b3d66665f8db5567e052f85226f60be0)|2017-11-08 19:34:59
|1036|helfi92|Merge pull request #224 from helfi92/modify-actions-docs  Remove actions query parameters from docs|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d1f8ee9becb54aa70d1aa4496407bb34dc9b7940)|2017-11-09 18:46:41
|1035|helfi92|Modify action explanations to reflect path parameters|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3148a0281b4b87d9afeca3a695054e5d4ed66759)|2017-11-08 13:29:57
|1034|helfi92|Add method propety to action definition|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a11f61d631266615f459db049b8ec38c346168a7)|2017-11-09 15:16:55
|1033|helfi92|Use <parameter> instead of :parameter|[URL](https://github.com/taskcluster/taskcluster-queue/commit/833caa9ce8280e27642e125cff81b56b1d8d4c93)|2017-11-08 21:49:03
|1032|helfi92|Update action docs|[URL](https://github.com/taskcluster/taskcluster-queue/commit/59cc86a5ef77de50547d8a517e07dbf59b271e6d)|2017-11-08 19:49:55
|1031|jhford|Do not redirect blob artifacts to cloud-mirror|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6446a50d0edd2c87eed5a66a1a91e873190b134c)|2017-11-07 10:57:34
|1030|jhford|Correctly send all headers as strings|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e19d7c32fbac3eff6445eb236d0390def11550b6)|2017-11-01 21:47:59
|1029|jhford|Merge pull request #217 from taskcluster/fix-list-artifact-response  Add blob storageType to the list artifact response|[URL](https://github.com/taskcluster/taskcluster-queue/commit/21e2769375f61e762a386e192c6be1cc5b2135b3)|2017-11-01 17:57:02
|1028|jonasfj|Merge pull request #219 from taskcluster/fix-declareWorker-scope  Fix declareWorker scope|[URL](https://github.com/taskcluster/taskcluster-queue/commit/8d65a80b3f85143568e59a527d8e248cc1fb105c)|2017-10-31 18:42:30
|1027|jonasfj|Fix declareWorker scope|[URL](https://github.com/taskcluster/taskcluster-queue/commit/acf52f45c22e424caa6bf3b10e57c130cdb28ffb)|2017-10-31 18:23:48
|1026|djmitche|Merge pull request #218 from djmitche/bug1407037  Bug 1407037 - cast expires to a Date|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2363fae113eeb82cb84d5c1aa531ce3ef1b53aa1)|2017-10-31 15:54:55
|1025|djmitche|Bug 1407037 - cast expires to a Date|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f2f53d5e5fc80b820b63c3278fcc17656984cb91)|2017-10-31 15:40:59
|1024|jhford|Add blob storageType to the list artifact response|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e54b05bdd7fe7dbad36dc77afb5154ea1045fed2)|2017-10-20 14:22:51
|1023|helfi92|Merge pull request #216 from helfi92/actions-docs  Add docs to actions|[URL](https://github.com/taskcluster/taskcluster-queue/commit/099d4d2565db4d88abe08536e981195a3d8ac746)|2017-10-20 12:55:03
|1022|helfi92|Merge pull request #215 from helfi92/workertype-worker-actions  Add actions as top level property for worker-types and workers|[URL](https://github.com/taskcluster/taskcluster-queue/commit/aba5d5c4947b334066c8d69a0352cb25c3e5ba20)|2017-10-20 12:54:41
|1021|helfi92|Add 2 space indentation|[URL](https://github.com/taskcluster/taskcluster-queue/commit/bed018efd22d8a3055827023bf3153f64b91682f)|2017-10-19 22:55:22
|1020|helfi92|Put context in a table; Change words to the imperative voice|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2f94d459703a27fa6520d4089af8a00a614c2c57)|2017-10-19 22:18:58
|1019|helfi92|Add actions docs|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1d7d5cd85bfd3552d60a7ed00788888ae90a107b)|2017-10-19 18:55:10
|1018|jonasfj|Merge pull request #214 from taskcluster/fix-typo  Fix a typo in schema|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2ff95ffdc081b79b006e3e5712f79db0179bb191)|2017-10-19 16:44:25
|1017|helfi92|Add actions as top level property for worker-types and workers|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4aecf710bf28d7c802c3987aed83b0fb97e051f9)|2017-10-19 15:42:03
|1016|jhford|Fix a typo in schema|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2bf72ec1b5a16eaee476f9b08cc727e90551d003)|2017-10-19 13:30:14
|1015|helfi92|Merge pull request #212 from helfi92/provisioner-actions  Bug 1409186 - Implement actions on the Provisioner context|[URL](https://github.com/taskcluster/taskcluster-queue/commit/696902f66dfb4b0ff09202535d0754c662cd431e)|2017-10-19 12:52:07
|1014|helfi92|Remove some schema duplications; Change label to name|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c16dc0484b607c6bb92709ef7f8b338ed57b1e5b)|2017-10-18 20:46:10
|1013|helfi92|Improve schema descriptions|[URL](https://github.com/taskcluster/taskcluster-queue/commit/402a2b50496c1db2596bbcac26b4e1043849a2ce)|2017-10-17 19:23:50
|1012|helfi92|Change level to context; Remove `severity` property from action|[URL](https://github.com/taskcluster/taskcluster-queue/commit/cd305bc97a676341b1cff34e79d7a416cfa3f756)|2017-10-17 12:54:51
|1011|helfi92|Bug 1409186 - Implement actions on the Provisioner context|[URL](https://github.com/taskcluster/taskcluster-queue/commit/885faca573b03264b646d11dc1aa6d2a8831bbc9)|2017-10-16 21:29:35
|1010|helfi92|Merge pull request #211 from taskcluster/jonasfj-patch-1  Minor fixes...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d7e1f3c78812fcaccd5e31899ddd00029ae94c8c)|2017-10-16 18:41:16
|1009|jonasfj|Minor fixes...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b24b493b099b07f62563cd5bfb2d6d405b76e0f6)|2017-10-11 23:54:49
|1008|helfi92|Merge pull request #210 from helfi92/extend-worker-to-have-runid  Bug 1404010 - Extend the worker to have the runId of its most recentTask|[URL](https://github.com/taskcluster/taskcluster-queue/commit/01a517db767074f60b21fe6411ed46f1124f6b10)|2017-10-02 20:38:02
|1007|helfi92|Add optimistic concurrency|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ecfe3887deafef8e8b1c49fb73315807e3946c76)|2017-10-02 20:11:13
|1006|helfi92|Fix off-by-one error in the runIds|[URL](https://github.com/taskcluster/taskcluster-queue/commit/741b0c345cb86232437d6e6cc51b8bb1fa3bb7aa)|2017-10-02 13:32:46
|1005|helfi92|Use list of JSON instead of SlugIdArray|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6c09259d01017c74d2a34ad4efdee82f0ccbcce1)|2017-09-28 18:42:15
|1004|helfi92|Merge pull request #209 from helfi92/nit-add-newline  Add newline|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c1b816e17e82feaa14dbf331c43bc7c6f4b43604)|2017-09-26 23:11:45
|1003|helfi92|Add newline|[URL](https://github.com/taskcluster/taskcluster-queue/commit/25dafecf6c289ffe504d3ed03a17c5e5d6d1a422)|2017-09-26 23:09:21
|1002|helfi92|Merge pull request #208 from helfi92/lint-error  Fix linting issue (add a comma)|[URL](https://github.com/taskcluster/taskcluster-queue/commit/879cf32f73380439b9a80d12297c156170e20d98)|2017-09-26 22:52:19
|1001|helfi92|Fix linting issue|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4f614acd423773cca00d5fc7e83971fc0535be74)|2017-09-26 22:49:07
|1000|helfi92|Merge pull request #207 from taskcluster/document-complete-artifact  Document the complete artifact endpoint|[URL](https://github.com/taskcluster/taskcluster-queue/commit/79cf24cc65b41008885eff97a942e585a8de9139)|2017-09-26 22:39:40
|999|jhford|Document the complete artifact endpoint|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b36312264f3c04373977a90c6193e937f232f307)|2017-09-26 19:51:16
|998|jhford|Merge pull request #206 from taskcluster/blob-artifacts  Artifacts, now with more SHA256 and Content-Length verification.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6cba02804aeb05b6a5c44134dca1df1b018f1860)|2017-09-22 18:18:09
|997|jhford|Avoid a slight timing issue|[URL](https://github.com/taskcluster/taskcluster-queue/commit/620a4564a51b93f3a02cb71949ce654e48a61d17)|2017-09-21 19:51:06
|996|jhford|Return early|[URL](https://github.com/taskcluster/taskcluster-queue/commit/05a02604b80c3f64ff3d360cd2f4e63704e39638)|2017-09-19 10:35:05
|995|jhford|Publish on early return|[URL](https://github.com/taskcluster/taskcluster-queue/commit/573381417eb6355bc84af6b2db9a09fcfb78d296)|2017-09-19 10:34:11
|994|jhford|Ensure that the run is running to allow for completion of uploading|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4ded97f4f897b28983b2c78dd456fa8370b8873a)|2017-09-19 10:28:11
|993|jhford|Idempotent completeArtifact|[URL](https://github.com/taskcluster/taskcluster-queue/commit/8eac10e1f9127a5e0558fbf3bb82b81d8e390c69)|2017-09-11 11:32:44
|992|jhford|cleanup|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3011a234b22aebcfad582b242b645829f35abadb)|2017-09-11 10:06:25
|991|jhford|change how we generate partHash|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e55c4e6821172f71409c6614bb42b1d29d9837ba)|2017-09-11 09:52:37
|990|jhford|Make missing blobs a request conflict instead of input error|[URL](https://github.com/taskcluster/taskcluster-queue/commit/04c3aae2de0c63dcb8e757723f5809cab1db4c52)|2017-09-11 09:48:15
|989|jhford|Remove put-artifact-response schema|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3c00e127e9cf526028de643229f57b3a0e0adcfb)|2017-09-11 09:47:35
|988|jhford|Print out remote s3 debugging|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0f80502a95af22ec914794403e491c26cb04e06d)|2017-08-31 08:21:20
|987|jhford|Use correct version of node in travis|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3e6bff3fe6a862438ff2c6d730ff005f64f920f2)|2017-08-31 07:56:43
|986|jhford|Check that all blob artifacts are present before marking as resolved|[URL](https://github.com/taskcluster/taskcluster-queue/commit/27d34ffc1233d800a4a586f4a412869342ff8051)|2017-08-30 15:48:46
|985|jhford|Simplify the partshash calculation  Since we're not actually using this information anywhere, let's just use the most simple format possible.  Because \n is system dependant, we should just write everything concatenated.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/581b0456bd4dcc7ff7d696c027431b5edc3e0f82)|2017-08-30 14:55:25
|984|jhford|Why not?|[URL](https://github.com/taskcluster/taskcluster-queue/commit/79aaf8c1b0a0dfbab12e48dc7c3c89686b2c5243)|2017-08-30 14:54:03
|983|jhford|Remove stale comment|[URL](https://github.com/taskcluster/taskcluster-queue/commit/da387c53e7b22bd7c422b86dbb70075355a06878)|2017-08-30 14:51:42
|982|jhford|Fix a couple issues which didn't work because of unit tests|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a92943b5c0cc08474a0bc87044c6349a1e91724a)|2017-08-30 14:30:35
|981|jhford|Use integer instead of numbers|[URL](https://github.com/taskcluster/taskcluster-queue/commit/41fd7ee806424d366b55d3485b67b026d7283bb8)|2017-08-29 11:09:29
|980|jhford|Ensure that single-part uploads exist with the correct x-amz-meta-content-sha256 value|[URL](https://github.com/taskcluster/taskcluster-queue/commit/cfe27640926cb0be5cd0959434edd5eb6214f6ba)|2017-08-29 11:06:47
|979|jhford|Stop using json.stringify for hashing the parts|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6c04d699debfa5bec50bfd532569fbf6cc70eb10)|2017-08-11 15:47:00
|978|jhford|Inline encodeBlobKey|[URL](https://github.com/taskcluster/taskcluster-queue/commit/165d9be5f6014c88ea7eb8ae7903b589ef3d2b76)|2017-08-11 15:44:51
|977|jhford|More documentation about the details property|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4fc683db0ca51b9d3a52a8990e5fbf92be4f2a55)|2017-08-11 15:41:58
|976|jhford|Remove createBuckets component|[URL](https://github.com/taskcluster/taskcluster-queue/commit/078fcac2efa869d5a45f437973533b93f07c6127)|2017-08-11 15:32:15
|975|jhford|get the correct etag value|[URL](https://github.com/taskcluster/taskcluster-queue/commit/31aa596e17343947c26848e6d2c9f4aba2e42be3)|2017-08-10 13:45:52
|974|jhford|rename encoding to contentEncoding|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3b60cb53289f031e19b942b04953637e03e6e6fe)|2017-08-10 13:40:07
|973|jhford|Fix lint|[URL](https://github.com/taskcluster/taskcluster-queue/commit/37d9458c47a429158b02bc74531d736abc8ad97a)|2017-08-04 10:01:30
|972|jhford|Implement Artifact.remove() for blobs|[URL](https://github.com/taskcluster/taskcluster-queue/commit/df6990c1e04dbfd62b671f6b3ce092c0f5696fa9)|2017-08-03 14:13:07
|971|jhford|remove unit test limiting|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6c20a0a415774db7cee7ecef482082e23d7e84f5)|2017-08-03 13:30:45
|970|jhford|Rename things|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d1b475b44772fb388a5cc9443f8b3811aede8c89)|2017-08-03 13:29:14
|969|jhford|Only use regex for length validation|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ec8d30ae75553dfe7189ef6dee69aa421bd0b0df)|2017-08-03 10:27:48
|968|jhford|some test fixes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/55b0872bb58eca8c627e348a2254773c04e0dde4)|2017-08-03 10:20:38
|967|jhford|install remotely signed s3|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c852cf7e009b2c86cd02853c80007fe8e2c8522e)|2017-07-18 13:55:07
|966|jhford|fix a couple tests|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c1f90b6fbbae7f2aa9e4c1473a07ab8a0930591a)|2017-05-04 14:55:01
|965|jhford|use the Boolean entity property type|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2c2d1be46648685d76cbe11ecbe397141fc52122)|2017-05-03 12:07:14
|964|jhford|remove decodeBlobKey|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d46854b9bd7ba141381959722a49cbe56c2bf98f)|2017-05-03 12:02:50
|963|jhford|change title of a schema|[URL](https://github.com/taskcluster/taskcluster-queue/commit/763c1b2059b533cb5286d50dc86bd016d3a017db)|2017-04-28 14:00:45
|962|jhford|stop providing the byte offset in the parts list|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6203758055c0bb2f03d680726462ebac46483437)|2017-04-28 13:47:02
|961|jhford|anchor sha256 patterns|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f6f434429495c5cedfd3b74674387942869721dc)|2017-04-28 13:41:24
|960|jhford|remove randbytes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ae0739e52c61c9db02949b0c8f6651e1e892438d)|2017-04-28 13:40:02
|959|jhford|remove tmp library|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e24589713c93f92a08b77d9a5525363ae16f4920)|2017-04-28 13:32:41
|958|jhford|use existing garbage buckets for testing|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3183c304878a39ca6de8c5c553b2d78762a1788e)|2017-04-28 13:28:16
|957|jhford|note to self|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f5a75d102bad847ff19b2b8737771e8aca38e63a)|2017-03-23 16:18:25
|956|jhford|Verify downloads|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3ad433914ef518faeb391fb9b2492546a004b90d)|2017-03-23 15:16:13
|955|jhford|Ensure that idempotent operations generate new signatures with same upload id|[URL](https://github.com/taskcluster/taskcluster-queue/commit/67780b441862915151ee05e8e8c16328f5374f9d)|2017-03-23 13:28:06
|954|jhford|ensure that idempotent operations return the same uploadId|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ffdac118c8c9a984026922e882fa6a2da1038992)|2017-03-23 13:11:16
|953|jhford|Idempotency works for multipart uploads|[URL](https://github.com/taskcluster/taskcluster-queue/commit/80d0ce0cca24aca970dbd91f3eb83eeb957abbde)|2017-03-23 13:04:37
|952|jhford|Multipart upload is working!|[URL](https://github.com/taskcluster/taskcluster-queue/commit/047f43656f291cf01516860c512e6796f40fd22d)|2017-03-23 12:06:35
|951|jhford|a couple small changes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7f9d448fcc15e745c21a138e4062e448aa4c7efb)|2017-03-23 11:51:07
|950|jhford|Finish making things configurable|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a5de6007ab01022346a7f65d18091a10c6f61cfc)|2017-03-23 11:43:31
|949|jhford|Implement multipart test and schemas, as well as schemas for put requests and bucket creation|[URL](https://github.com/taskcluster/taskcluster-queue/commit/86dd2d549ace215ca07c84953a745af89f6969ff)|2017-03-23 11:37:44
|948|jhford|Tests for single part uploads started|[URL](https://github.com/taskcluster/taskcluster-queue/commit/431f9f71c64553b423979696bbc4804852c5d763)|2017-03-22 16:33:46
|947|jhford|fix a small bug and remove runtests.sh|[URL](https://github.com/taskcluster/taskcluster-queue/commit/44d8da39f183e3f126e4dd3ded1d444aa3748a29)|2017-03-22 14:43:39
|946|jhford|compile errors|[URL](https://github.com/taskcluster/taskcluster-queue/commit/32ded33211850588d8e3198dfa8175f99d9b0ce8)|2017-03-21 09:46:48
|945|jhford|set the present flag to 0 by default and 1 for new s3/azure/error/redirect artifacts|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e3e407920e74df12816f58fc0a804e037b2ea7b3)|2017-03-20 14:25:15
|944|jhford|Implement present status on Artifacts and finish implementing the completeArtifact endpoint|[URL](https://github.com/taskcluster/taskcluster-queue/commit/874e2c29d4bf01a9302f2880c9f7ec32ca271228)|2017-03-20 14:23:42
|943|jhford|Add a `present` property to the Artifact entity|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5158c1758ff0ed28c459ab0695e7a1d9f097f4c0)|2017-03-20 14:14:00
|942|jhford|API Changes to generate the uploadId when creating the Artifact entity  This should address the bulk of the feedback from the last review cycle|[URL](https://github.com/taskcluster/taskcluster-queue/commit/13d1e3eadafc4c0a3aeae2bdaa004b6bdf71dfdb)|2017-03-20 14:01:27
|941|jhford|basics of the createArtifact method, skeleton for the completeArtifact method|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f9d20fd8a414adc3b4db3046026e4d88f4d5f4a0)|2017-03-13 14:57:18
|940|jhford|stub out the completeArtifact method|[URL](https://github.com/taskcluster/taskcluster-queue/commit/cb3bde2544b04724f77e54bb1b4fbaafba249a96)|2017-03-13 13:03:07
|939|helfi92|Merge pull request #205 from helfi92/allow-filter  Bug 1401961 - Extend listWorkers endpoint to allow filtering by disabled workers|[URL](https://github.com/taskcluster/taskcluster-queue/commit/8157ebdd0dd9d01c3bd64200703435365e4b90bd)|2017-09-21 17:40:52
|938|helfi92|Add docs and change variable name|[URL](https://github.com/taskcluster/taskcluster-queue/commit/03735154a566d704643ff8c65f5450f5cb8c9a48)|2017-09-21 17:38:42
|937|helfi92|Bug 1401961 - Extend listWorkers endpoint to allow filtering by disabled workers|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b01b6c3d7fdb6dcf5aa34a8fded159f9604b4491)|2017-09-21 14:02:44
|936|helfi92|Merge pull request #204 from helfi92/recentTasks  Bug 1401360 - Modify taskSeen to use the new SlugIdArrray methods|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4f112ba12e6a368e80f8156bc26961af75d8afee)|2017-09-20 21:14:59
|935|helfi92|Remove try catch statement|[URL](https://github.com/taskcluster/taskcluster-queue/commit/37fad6ae8f8453a972a3d80f6f36dbfead68a580)|2017-09-20 21:12:57
|934|helfi92|Use push and shift now that realloc bug has been fixed|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b8d367b12874f95194c78d1fb8f4d203f35c0965)|2017-09-20 21:02:37
|933|helfi92|Merge pull request #202 from helfi92/add-extra-data-workers-list  Bug 1401206 - Extend the list of workers endpoint|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1361ffd44720e49bc53160bac125ea56fe036946)|2017-09-19 20:34:48
|932|helfi92|Bug 1401206 - Extend the list of workers endpoint|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4924cafe91919ec9c719b5d89bce189a34c5ff88)|2017-09-19 14:11:59
|931|helfi92|Merge pull request #203 from helfi92/update-azure-version  Update azure-entites repo version|[URL](https://github.com/taskcluster/taskcluster-queue/commit/50fdf3cffb8d5dcf661e30017979d6f840534af9)|2017-09-19 20:16:29
|930|helfi92|Update azure-entites repo version|[URL](https://github.com/taskcluster/taskcluster-queue/commit/bb5503eacec89178e2d2e6ecd093dcaa54759f3b)|2017-09-19 20:13:00
|929|helfi92|Merge pull request #200 from helfi92/tasks-length  Patch to fix sentry error|[URL](https://github.com/taskcluster/taskcluster-queue/commit/84d68c08d2f3add044a3ef05e74c65d81011e628)|2017-09-15 00:04:10
|928|helfi92|Remove ternary|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4a8295b7afd09e5fb316341c894437c2e12dcae8)|2017-09-14 23:59:39
|927|helfi92|Move call down|[URL](https://github.com/taskcluster/taskcluster-queue/commit/8bc02e9b0dda110e7c6e94dc28fb83a024eed9c5)|2017-09-14 23:43:12
|926|helfi92|Send empty array if result is string|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c810454593e00a0c28a87119b0e9de8d1998c78b)|2017-09-14 23:38:14
|925|helfi92|Patch to fix sentry error|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6b4a7d0c5a714a1e7929a8d8b2316998cf89fdee)|2017-09-14 23:19:34
|924|helfi92|Merge pull request #198 from helfi92/disable-enable-workers  Bug 1399123 - Enable/Disable workers|[URL](https://github.com/taskcluster/taskcluster-queue/commit/98e9b145a9077849ccbef648a431da9108c1e568)|2017-09-14 13:56:18
|923|helfi92|Check if worker disabled before claimWork and claimTask|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3c7d4e5b03a3415da1f38a0b8a20a85cf4c93722)|2017-09-13 19:53:37
|922|helfi92|Change ternary to if statement and add a try catch statement|[URL](https://github.com/taskcluster/taskcluster-queue/commit/36cfdceebb6a3eb89625b1aefc02ecb46c88b4c6)|2017-09-12 19:42:49
|921|helfi92|Bug 1399123 - Enable/Disable workers|[URL](https://github.com/taskcluster/taskcluster-queue/commit/38a6606dc8d11690ae3b692f5dd01b840324492d)|2017-09-12 14:00:04
|920|djmitche|Merge pull request #196 from djmitche/bug1397373  Bug 1397373 - describe superseding in queue reference|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9b36857aa8f8f27515382b48e638e9754ebf5993)|2017-09-08 12:52:13
|919|djmitche|Bug 1397373 - describe superseding in queue reference  This describes superseding as a convention, rather than a rule.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5a6dc0d33956da0d72caa15b0934e2882de5cfce)|2017-09-06 18:03:30
|918|djmitche|Merge pull request #195 from djmitche/remove-all-worker-tables  add remove-all-worker-tables target|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e433382aa036fb37cb9d3b3804845f8e4f0bef28)|2017-09-05 18:53:44
|917|djmitche|add remove-all-worker-tables target|[URL](https://github.com/taskcluster/taskcluster-queue/commit/8146e4349266096ca1e562179844f7907c03a5b5)|2017-09-05 18:24:07
|916|helfi92|Merge pull request #194 from helfi92/get-put-workerid  Bug 1390870 - Implement API endpoint for a worker|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f39b1e9d8dcb9334557b030d3a9456ccef6af112)|2017-09-05 18:23:29
|915|helfi92|Remove unused constant|[URL](https://github.com/taskcluster/taskcluster-queue/commit/83c666ed00d07a7979fbaca19b7614548015dd53)|2017-09-01 16:52:59
|914|helfi92|Implement API endpoint to GET and PUT a worker|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a3d35574e998d4e7f08f6bb70e5da57682f73470)|2017-08-29 19:07:17
|913|helfi92|Merge pull request #189 from taskcluster/get-put-prov  Bug 1390866 - Implement API endpoint to GET and PUT a provisioner|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b65848496947d7f486f7efd6e471859433c96424)|2017-08-31 16:50:38
|912|helfi92|Fix typo|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e96472aa2e522c47f9496583f73014fd8e94356e)|2017-08-31 15:01:43
|911|helfi92|Add deferAuth and fix grammar|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4ce4afcc9794fe0b43c39348195773ad2fdd69ed)|2017-08-31 14:05:03
|910|helfi92|Implement GET and PUT to a provisioner|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7a848bfbb49e9f95707cae21e6c292e3b33c7d27)|2017-08-24 20:52:08
|909|helfi92|Merge pull request #193 from taskcluster/get-put-wtype  Set migrate lastDateActive to January 1 2000 instead of null|[URL](https://github.com/taskcluster/taskcluster-queue/commit/88d94494857688c05506feb710949ff655d40cf5)|2017-08-30 18:56:51
|908|helfi92|Set migrate lastDateActive to January 1 2000 instead of null|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ed241c007ca67319d0b6d74133a1982676281048)|2017-08-30 18:41:14
|907|helfi92|Merge pull request #190 from taskcluster/get-put-wtype  Implement API endpoint to GET and PUT a worker-type|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b193fbe6d8d84fbb36e4b86b4874d86a112ee132)|2017-08-30 16:42:33
|906|helfi92|Add minor tweaks|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9c84938a7a1db386fad749bc405e6daa20994628)|2017-08-30 15:22:53
|905|helfi92|Replace instances of updateWorkerType with declareWorkerType|[URL](https://github.com/taskcluster/taskcluster-queue/commit/07cdad16f0f15649966310d11ce4c00c2d790633)|2017-08-29 14:26:27
|904|helfi92|Allow update of one or many properties of a worker-type|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ccd93218f468bb83c297f83d4634511cd158377b)|2017-08-27 15:02:24
|903|helfi92|Make PUT permissive; Make sure scope is satisfied in PUT|[URL](https://github.com/taskcluster/taskcluster-queue/commit/90c9ceb87a46f666852bb911e054b03d48227ac6)|2017-08-27 00:07:50
|902|helfi92|Implement API endpoint to GET and PUT a worker-type|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9a59d3bc5dccc665562b989d86430e49c0a5ab80)|2017-08-25 20:14:59
|901|helfi92|Merge pull request #186 from helfi92/provisioners-metadata  Bug 1390865 - Expand the /provisioners endpoint to return metadata|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7496392143d8f0dab0931532434c611006383b45)|2017-08-24 19:56:41
|900|helfi92|Merge pull request #187 from helfi92/expand-workertypes  Bug 1390867 - Expand the worker-types endpoint to return metadata|[URL](https://github.com/taskcluster/taskcluster-queue/commit/69e245968cbce879d2263d462fd6d8b77a4eabc4)|2017-08-24 19:56:18
|899|helfi92|Make description a markdown|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ec1a844c40124798857c215b5b7268412a4bf0ef)|2017-08-24 19:52:49
|898|helfi92|Make description markdown|[URL](https://github.com/taskcluster/taskcluster-queue/commit/173b8a772f997f7371b0fa4794cef3bb2b3c2b4f)|2017-08-24 19:51:20
|897|helfi92|Remove documentation, payloadSchema from entity|[URL](https://github.com/taskcluster/taskcluster-queue/commit/dcc05ab5e3c54d43800b346f3fa672e68f1c7818)|2017-08-24 19:41:38
|896|djmitche|Merge pull request #188 from djmitche/lowercase-urls  Use worker-types, not workerTypes, in url pattern|[URL](https://github.com/taskcluster/taskcluster-queue/commit/015c3d4e438f161939e9ef6ae2cf698ffe8a2bf9)|2017-08-24 19:28:22
|895|djmitche|Use worker-types, not workerTypes, in url pattern|[URL](https://github.com/taskcluster/taskcluster-queue/commit/bdf0b3b3c8ea195318598715fa94d4314087f666)|2017-08-24 18:38:55
|894|helfi92|Make documentation Text|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2e915b7597dd88454b1c0c1e40604219c856bdb3)|2017-08-24 18:29:57
|893|helfi92|Add Provisioner azure entity v2|[URL](https://github.com/taskcluster/taskcluster-queue/commit/05d88df7617c49c500ee8ed5d930869966dbc0ee)|2017-08-18 13:30:56
|892|helfi92|Add worker type azure entity v2; Make payloadSchema null|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4b16ccef74fab440451b7241727a1c2d7766658c)|2017-08-18 13:10:22
|891|helfi92|Expand worker-types response with extra metadata|[URL](https://github.com/taskcluster/taskcluster-queue/commit/51e86b313e8158d50d05c50c4e33e030ccc89dcc)|2017-08-17 03:39:50
|890|helfi92|Extend the provisioners endpoint to return metadata|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ba7a2337ad67d9af10a3cb377c4cb3531ceef555)|2017-08-16 20:52:51
|889|helfi92|Merge pull request #184 from helfi92/workergroup-workerid  Bug 1384949 - Implement API endpoint to list out a list of workerGroup/workerId|[URL](https://github.com/taskcluster/taskcluster-queue/commit/eda08ebdd707498fb64658ac5e6c158719bd808a)|2017-08-15 19:44:46
|888|helfi92|Reduce expiration to 1 day for workers; Fix expired; Rest is nit|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2551dcc5d7b78961c7a3743cdd7e95230318fc7c)|2017-08-14 13:37:19
|887|djmitche|Merge pull request #185 from djmitche/procfile-upd  add expireWorkerInfo to Procfile|[URL](https://github.com/taskcluster/taskcluster-queue/commit/dd24e916930d996951ef49f41e2a5cbfab67b8df)|2017-08-11 21:47:52
|886|djmitche|add expireWorkerInfo to Procfile|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3bf9616da6a50e6e11d759e1c8f347d2ac496e6c)|2017-08-10 13:32:12
|885|helfi92|Modify schema workerGroup and workerId descriptions|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d2d14ce94a8a0d3e4ff9b1abea0258a5d6b1e7c8)|2017-08-10 12:59:02
|884|helfi92|Bug 1384949 - Implement API endpoint to list out a list of workerGroup/workerId|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ce66823a96507bdf0fc7d533c44e4eb2456883ba)|2017-08-09 20:18:29
|883|helfi92|Merge pull request #183 from helfi92/list-workertypes  Bug 1384948 - API endpoint to list out worker types for a given provisioner|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2472832703f1dc3f4a3f8c40c4cbb43df5c7bd05)|2017-08-09 12:44:23
|882|helfi92|Nit|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7817ffd31d6bb42b5db1621ccba7ace4f2b1053e)|2017-08-08 22:17:38
|881|helfi92|Make workerTypes schema an object; Unify seen function; Nits|[URL](https://github.com/taskcluster/taskcluster-queue/commit/767c3a864459dbccfa001146505fda8d93d73c40)|2017-08-08 21:53:18
|880|helfi92|Remove usage of slugids in test/workerinfo.js|[URL](https://github.com/taskcluster/taskcluster-queue/commit/037733c1476c5b0f8f05ade187209a158fa98a72)|2017-08-08 14:38:09
|879|helfi92|Better worker-type testing name|[URL](https://github.com/taskcluster/taskcluster-queue/commit/fe2ee758cdcc260657ea3cd5177289a936dc7e43)|2017-08-07 17:35:24
|878|helfi92|Handle worker-type expiration|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9058cbfcd3663e43ff9d76adb702d1dd340b172c)|2017-08-07 05:07:01
|877|helfi92|Merge branch 'master' into list-workertypes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/939cd276298dab46b1e9b90093b515964b92ceb4)|2017-08-04 18:50:56
|876|helfi92|Bug 1384948 - Implement API endpoint to list out worker types for a given provisioner|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4c6b2e7e5f67474d53b344a41605963d9d19d131)|2017-08-04 16:51:45
|875|djmitche|Use a Provisioners table  ..instead of dumping provisioners into the TaskDependency table|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f2f7d79e3d4d7a770ae184537d00ddc09a116193)|2017-08-04 18:39:05
|874|helfi92|Merge pull request #182 from taskcluster/djmitche-bug1384947  Bug 1384947 - track and list provisioners|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7ba255117bb3c58714a41a27e81524fba12c755c)|2017-08-03 22:11:39
|873|helfi92|Add conditional update; Nits|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5249588e1c59fdd2c86bc66d380fa061adb39bdf)|2017-08-03 21:49:27
|872|djmitche|begin populating worker info tables|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7e1fe8524664e1a6d4b234c3b96c474f228ea548)|2017-07-28 22:54:47
|871|djmitche|add a listProvisioners endpoint and table to back it|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f0d8d6507c8daf8fe72af8b9e8317e87bb663540)|2017-07-28 22:11:17
|870|jonasfj|Merge pull request #179 from taskcluster/upgrade-node  Upgrade to node 8.2|[URL](https://github.com/taskcluster/taskcluster-queue/commit/770cbc0d9423b353c8d181e40520a12febc967b0)|2017-07-20 23:01:21
|869|jonasfj|Upgrade to node 8.2|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d678f83b4885fe415ae4f623707d980f0b6613d3)|2017-07-20 22:45:47
|868|jonasfj|Merge pull request #178 from djmitche/spelling  spell Taskcluster|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6fb03af62d9701aba691007c8dd017d2fede48ef)|2017-07-17 20:11:37
|867|djmitche|Merge pull request #177 from taskcluster/create-artifact-wording-fix  API error message fix for createArtifact|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2c2e1a679228f9c919384b667e463eb440839820)|2017-07-17 18:44:18
|866|djmitche|spell Taskcluster|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f9b15ac42388aaf4ecf9f0d244fd4bcd1709ca66)|2017-07-17 16:48:54
|865|petemoore|API error message fix for createArtifact|[URL](https://github.com/taskcluster/taskcluster-queue/commit/599ba6fee7fa5c8117d84e49dba3d23d6fcbc739)|2017-07-17 13:04:31
|864|jonasfj|Merge pull request #176 from taskcluster/upgrade-node  Upgrade to node 8|[URL](https://github.com/taskcluster/taskcluster-queue/commit/850359f099eeb1b784a1a5c540084b2594e3571b)|2017-07-13 22:03:08
|863|jonasfj|Upgrade to node 8|[URL](https://github.com/taskcluster/taskcluster-queue/commit/41709ad747176cf46c130af0972adaf3ce56371e)|2017-07-13 21:57:31
|862|jonasfj|Merge pull request #174 from taskcluster/revert-151-limit-routes  Revert "Limit task.routes to 10"|[URL](https://github.com/taskcluster/taskcluster-queue/commit/36932da9c000534cf5d36d995e694311634411ee)|2017-06-06 03:27:56
|861|jonasfj|Revert "Limit task.routes to 10"|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3fccaf46a79060fd7d23a48c84a32e0e557dc298)|2017-06-06 03:26:19
|860|jonasfj|Merge pull request #151 from taskcluster/limit-routes  Limit task.routes to 10|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f887c100fb0285d84ee1ad84b106eff426a49646)|2017-06-01 20:54:54
|859|djmitche|Merge pull request #172 from djmitche/dustin-is-dum  Bug 1364121: use backticks to get interpolation|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4d59d8025f390e57a9e06e7ac98ac2dbc332339d)|2017-05-30 17:22:40
|858|imbstack|Merge pull request #173 from taskcluster/fix-608950  Fix artifacts for runs that have been cancelled|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3b7eb7e59de1545d1eafbe5313ee3b6d23559c1f)|2017-05-25 23:40:57
|857|imbstack|Fix artifacts for runs that have been cancelled|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6519138f82701ec2e8589db29c4fbdf73d19518e)|2017-05-25 23:08:35
|856|djmitche|use backticks to get interpolation|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2f2c0b5e68fdd7605fa0a86ef5347b1845ed61eb)|2017-05-24 18:22:21
|855|jonasfj|Upgraded pulse-publisher again|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b92e94447c1d8445cbb0d11265ba5d057c8fd7d3)|2017-05-23 01:25:18
|854|jonasfj|Merge pull request #171 from taskcluster/upgrade-pulse-publisher  Updated npm packages, including pulse-publisher with reconnects|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3a2b83fb1db91cd7f6a77ea95982a37634b37479)|2017-05-23 00:31:15
|853|jonasfj|Updated npm packages, including pulse-publisher with reconnects|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2e26f89a73b8511e75995c807205379852963acf)|2017-05-23 00:24:37
|852|jonasfj|Merge pull request #170 from taskcluster/more-queue-metrics  More azure queue metrics|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f9a7348f621ec6f684ca3718a612f6cf69059b2f)|2017-05-21 23:48:17
|851|jonasfj|Another measurement|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ae0298b60573b8a6e95c4fc3f39b131172554b36)|2017-05-21 22:22:57
|850|jonasfj|More azure queue metrics|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ff44297f6343a67f2964b5653a0964d4379dc43e)|2017-05-21 22:19:29
|849|djmitche|add missing comma|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3d06bc3cf0727636185b5ca72fa73e96e3bc6f1a)|2017-05-17 13:28:14
|848|djmitche|Merge pull request #168 from djmitche/bug1364121  Set clientId for claimed-task temporary creds|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3f16d7f25c53564b5935561893c93deeef7e88e5)|2017-05-17 12:52:06
|847|jonasfj|Merge pull request #169 from taskcluster/fix-priority-scoping  Fix scope issues to require new scopes for priority usage|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c7a7e54db74b164e80d40d4077d7c53e7adacc53)|2017-05-16 15:24:18
|846|jonasfj|Fix scope issues to require new scopes for priority usage|[URL](https://github.com/taskcluster/taskcluster-queue/commit/dfd5a3bab2f29a36d8b940948260efbdd8c1f3c0)|2017-05-16 04:48:27
|845|imbstack|Merge pull request #166 from taskcluster/task-priority  Implemented new priority levels|[URL](https://github.com/taskcluster/taskcluster-queue/commit/8200bb3c85c1182bab5eda88b39dd4fec09462e9)|2017-05-15 20:54:53
|844|djmitche|Merge pull request #167 from djmitche/retry-reasons  mention the resolve reasons that might trigger a retry, vaguely|[URL](https://github.com/taskcluster/taskcluster-queue/commit/27c5d07fcf3357c6c306ff61bc899971db5a3250)|2017-05-15 13:53:00
|843|djmitche|Set clientId for claimed-task temporary creds|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3f19792ee1f5727b336a0976a7e1c344b5b9c8c8)|2017-05-12 23:16:57
|842|djmitche|mention the resolve reasons that might trigger a retry, vaguely|[URL](https://github.com/taskcluster/taskcluster-queue/commit/09c19d88a3396e6a3f5297a2761534586833c795)|2017-05-12 19:10:49
|841|jonasfj|Fixed language in docs|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ef31c266c662c7451e73e1d55fb52c916afa11fb)|2017-05-12 00:18:06
|840|jonasfj|Added extra scopes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/eed2b450b8187431a1386f2a1b3291e39dffc0e1)|2017-05-12 00:16:19
|839|jonasfj|Implemented new priority levels|[URL](https://github.com/taskcluster/taskcluster-queue/commit/30a456a6cc8c3660631d3780060a7e6040431cce)|2017-05-11 23:05:51
|838|djmitche|Merge pull request #165 from djmitche/task-schema-title  add a title for task-schema|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2880d3b656113314b9b270e37cbeb4f9bf850931)|2017-04-26 20:16:39
|837|djmitche|add a title for task-schema|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e69b06340049b9557b1a4bff121f1553c566a5d8)|2017-04-26 19:28:07
|836|jonasfj|Merge pull request #160 from grenade/patch-1  bug 1318648 - support instance instantiation in us-east-2|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6e121df48c0ce4a42c3fcd2b269302114e562c23)|2017-04-24 23:11:30
|835|imbstack|Merge pull request #164 from taskcluster/bump-lib-api  Bump lib-api to reduce auth load|[URL](https://github.com/taskcluster/taskcluster-queue/commit/047859f8f83900badf10b639ae24e98064d9dc02)|2017-04-17 17:00:16
|834|imbstack|Bump lib-api to reduce auth load|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2327979dcb5946963856297ad87f9a9f59f14de4)|2017-04-14 21:08:21
|833|imbstack|Merge pull request #161 from taskcluster/fix-readme-structure  Fix readme structure section|[URL](https://github.com/taskcluster/taskcluster-queue/commit/267ca7c68653658c7af19864309114724b95b380)|2017-04-12 00:33:12
|832|imbstack|Fix readme structure section|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e7ce4907051d5b14a0ca8dd3573f549b15fafba9)|2017-04-03 22:59:30
|831|imbstack|Merge pull request #163 from taskcluster/add-creds-to-data  Add credentials to azure-entities|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e39b8d2a6ef0bd75336a79f89a8a713495a45659)|2017-04-11 23:09:14
|830|imbstack|Add credentials to azure-entities|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6f14f7fafe51940acb63fbf1fe0de60cb2ee5ed3)|2017-04-11 18:23:28
|829|imbstack|Merge pull request #162 from taskcluster/fix-azure-testing-leaks  Change azure tables auth mechanism|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4d0d5434510444f4b9fa074215eb787f579d69fe)|2017-04-11 17:30:41
|828|imbstack|Change azure tables auth mechanism|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b2357dddb11547b116a62098f672d1f7996e35e4)|2017-04-05 00:39:13
|827|grenade|bug 1318648 - support instance instantiation in us-east-2  in anticipation of increased load for g2.2xlarge (gecko-t-win7-32-gpu, gecko-t-win10-64-gpu worker types) enable instance instantiation in us-east-2 to mitigate cost and availability issues|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3aff46e404efec3642723c1da7c8d7e430b2d2a8)|2017-04-03 12:45:01
|826|djmitche|rename to the project name in package.json|[URL](https://github.com/taskcluster/taskcluster-queue/commit/8716db894eb0bbcbe3e4c1508040dce2e20d4966)|2017-03-21 14:53:35
|825|jonasfj|Merge pull request #158 from taskcluster/reclaim-task-docs  Docs for reclaimTask|[URL](https://github.com/taskcluster/taskcluster-queue/commit/abaf40850793f0dc648970dd354f44fa0b8a7e59)|2017-03-16 23:52:21
|824|jonasfj|Docs for reclaimTask|[URL](https://github.com/taskcluster/taskcluster-queue/commit/802036b1438fe0ccdf2fb22da67e88d31bea1afd)|2017-03-16 21:14:46
|823|jonasfj|npm -> yarn, README.md|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9fcb9c70f82e5c0e12c02096803a73c362439e8e)|2017-03-13 19:04:51
|822|imbstack|Merge pull request #156 from taskcluster/jonasfj-patch-1  npm -> yarn|[URL](https://github.com/taskcluster/taskcluster-queue/commit/94947ee3e53bcb842c246900cd2affe69e641d10)|2017-03-13 18:53:51
|821|jonasfj|npm -> yarn|[URL](https://github.com/taskcluster/taskcluster-queue/commit/809c2834d12b07d5d0e82c994f2f2fb0981af95d)|2017-03-13 18:28:13
|820|jonasfj|Merge pull request #154 from taskcluster/use-new-babel-present  Use the same babel-preset that we're using elsewhere|[URL](https://github.com/taskcluster/taskcluster-queue/commit/83aa08088e64a143792203fcd1d9c3e29a2b306b)|2017-03-13 17:28:51
|819|jhford|Forgot to commit Yarn.lock changes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/df0db414c15b1ad9df113ce3c179cfe1b5a5d737)|2017-03-13 12:58:18
|818|jhford|update eslint and babel parser|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c0723f2929c421a89a288f030ce86ac4af87375b)|2017-03-13 12:57:35
|817|jhford|Use the same babel-preset that we're using elsewhere|[URL](https://github.com/taskcluster/taskcluster-queue/commit/abd4941dc58189911f9ad467f0919daefccddce0)|2017-03-13 11:55:00
|816|imbstack|Roll back node to 7.4.0|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a91ba4b8e329aeb7b86ed8858006b72b4175da0b)|2017-03-09 18:30:51
|815|imbstack|Merge pull request #153 from taskcluster/yarnification  Move to yarn|[URL](https://github.com/taskcluster/taskcluster-queue/commit/65a7e594213182ccf9adb0cf8a6b0a3e18552371)|2017-03-09 18:13:05
|814|jonasfj|Added LICENSE file|[URL](https://github.com/taskcluster/taskcluster-queue/commit/943eaa2ce4313e7a0fa4a7de28ac09708ffd5158)|2017-03-09 01:09:26
|813|imbstack|Move to yarn|[URL](https://github.com/taskcluster/taskcluster-queue/commit/16f6897f492b0cc84725305f947e8f373b073349)|2017-03-07 23:42:13
|812|jonasfj|Limit task.routes to 10  This is only on the create task request, not on the response since that would break what we currently have stored in the queue.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/97a764ffb15ec059b4160698a63f5cf7690f11bd)|2017-03-07 17:39:52
|811|djmitche|add service owner|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9051895694b5cc31ba99502369405a1e2a0ef200)|2017-03-07 16:56:51
|810|jonasfj|Merge pull request #149 from taskcluster/fixed-bug-removing-requests  Found a bug with timedout requests not being removed, not sure how mu…|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7ea66fac8b2a194b622a9558464eef6741882988)|2017-02-15 22:05:46
|809|jonasfj|.catch -> reject|[URL](https://github.com/taskcluster/taskcluster-queue/commit/78f0abb99d3a43eff5d9a14578a704ea7d95ceab)|2017-02-15 21:59:33
|808|jonasfj|Found a bug with timedout requests not being removed, not sure how much it explains.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/38c111f06e7c9c4ec9e560abc12e9e6fdfecc63c)|2017-02-15 21:49:45
|807|jonasfj|Merge pull request #148 from taskcluster/jonasfj-patch-1  Increasing polling interval|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a4ba77bacbf72fb3b7fb06e9416aebc3c7d8549e)|2017-02-15 00:19:36
|806|jonasfj|Increasing polling interval|[URL](https://github.com/taskcluster/taskcluster-queue/commit/98c0db272533f11d178ad57a950bca24217cc6cc)|2017-02-14 20:36:45
|805|jonasfj|Merge pull request #147 from djmitche/spellos  fix spelling errors|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5d0c9fff70101c4fc92408a5ddfcc8e6e350f358)|2017-02-14 18:19:37
|804|djmitche|fix spelling errors|[URL](https://github.com/taskcluster/taskcluster-queue/commit/615550869954278a9081fbb81c176b2edf7d7215)|2017-02-14 18:09:59
|803|jonasfj|Merge pull request #146 from taskcluster/extra-asserts  Extra asserts|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b5d5eaa2af73b8e1791aae823f866e3f50160bb4)|2017-02-09 23:15:52
|802|jonasfj|Upgrade libraries, fix tests, and reduce number of timers|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c834001d4cebacd61c8fc9b78a673e8f625e65f7)|2017-02-09 22:41:32
|801|jonasfj|Extra asserts for claimWork|[URL](https://github.com/taskcluster/taskcluster-queue/commit/eef49f3f8a92ca78c5dcd7178f8e569057435ea6)|2017-02-09 22:20:32
|800|djmitche|Merge pull request #145 from taskcluster/jonasfj-patch-1  Update api docs|[URL](https://github.com/taskcluster/taskcluster-queue/commit/88e1f0edc66350dcaf977d2934ef0486f555c2b0)|2017-02-07 22:51:44
|799|jonasfj|Update api docs|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9767c0429d36e5eec03c4232f9d79150a2575c13)|2017-02-07 22:49:31
|798|jonasfj|Fix missing count limit for azure queue polling|[URL](https://github.com/taskcluster/taskcluster-queue/commit/347adae5243187ffb7c956833ca501ed4b28762a)|2017-01-31 22:19:36
|797|imbstack|Merge pull request #143 from taskcluster/bump-pulse  Upgrade taskcluster-client + pulse-publisher|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4821e69dccc4d58b02a57794bb36c6aa5039aea5)|2017-01-25 00:24:40
|796|jonasfj|Merge pull request #142 from taskcluster/reportError  use res.reportError instead of res.status|[URL](https://github.com/taskcluster/taskcluster-queue/commit/20874363a9d376b97656c80bc9c533cb465e18b2)|2017-01-25 00:13:20
|795|jonasfj|Merged npm-shrinkwrap|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c299a62a06528ada9044b02a5fb88a7d5c023d09)|2017-01-24 23:47:49
|794|jonasfj|Merge branch 'master' of github.com:taskcluster/taskcluster-queue into bump-pulse|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6c2e1b76eb244ec5557dddfe7544384a11d371e3)|2017-01-24 23:10:50
|793|jonasfj|Upgrade taskcluster-client + pulse-publisher|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d90d7d52d7f2ff2b5429855bf18d1705a71f3f18)|2017-01-24 22:21:44
|792|djmitche|use res.reportError instead of res.status|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4fb53f99e0119d4aca4092f976c986f127892ef7)|2017-01-23 02:26:44
|791|jonasfj|Merge pull request #141 from taskcluster/jonasfj-patch-2  deduplicate headline|[URL](https://github.com/taskcluster/taskcluster-queue/commit/cf8761c380808748540f6103067bb5572944f2d8)|2017-01-21 02:11:58
|790|jonasfj|Merge pull request #140 from taskcluster/jonasfj-patch-1  Deduplicate headline|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1ad648889020bc2ac5b6ae64b4daa231318c04e4)|2017-01-21 02:05:04
|789|jonasfj|deduplicate headline|[URL](https://github.com/taskcluster/taskcluster-queue/commit/78c70bfd11f0ec6432c2811c2043246d5e64c854)|2017-01-21 01:58:45
|788|jonasfj|Deduplicate headline|[URL](https://github.com/taskcluster/taskcluster-queue/commit/41d6e3dc694ef6050ed097ad93fe82750e9d6792)|2017-01-21 01:58:22
|787|jonasfj|Merge pull request #139 from taskcluster/bump-pulse-publisher  Bump pulse-publisher|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c2928c65ea096e4f3e59716eabaee77a48d5a42b)|2017-01-19 01:30:44
|786|jonasfj|Bump pulse-publisher|[URL](https://github.com/taskcluster/taskcluster-queue/commit/862dd4173437c36d3a03a1f66d7e62e3231b2b9b)|2017-01-19 01:19:24
|785|jonasfj|Merge pull request #136 from taskcluster/more-docs  Added more docs on worker-queue interaction|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7a394b0d1c5447e4bd3dc5c5e918f77bd0ac9b45)|2017-01-04 15:48:07
|784|imbstack|Merge pull request #137 from taskcluster/add-task-schema-docs  add schema docs|[URL](https://github.com/taskcluster/taskcluster-queue/commit/fe5ea0ae6540219258962dd99413fd416934dea3)|2017-01-03 15:30:05
|783|djmitche|add schema docs|[URL](https://github.com/taskcluster/taskcluster-queue/commit/fde314c335decb65ae23ffa99ac7a7bb44510fbc)|2016-12-31 01:28:22
|782|jonasfj|Added more docs on worker-queue interaction|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3d304a720f4dc41d237dd87cfc9df7680b4bbd2a)|2016-12-19 18:08:51
|781|jonasfj|Merge pull request #135 from taskcluster/increase-route-limit  Increase route limit|[URL](https://github.com/taskcluster/taskcluster-queue/commit/25ed2068a131f3a3335eb5ac62711d5391aae211)|2016-12-15 21:59:20
|780|jonasfj|Increase route limit to 64|[URL](https://github.com/taskcluster/taskcluster-queue/commit/30225a6d294742ecd0e578b4f06266641e2460b6)|2016-12-15 20:50:49
|779|jonasfj|Set route limit to 64|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2c249a8a409191fb59834fb86126d2fbae4bb1ca)|2016-12-15 20:49:23
|778|jonasfj|Merge pull request #134 from taskcluster/more-docs  Task life-cycle documentation|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f0b2ce1bda8e0774084b009af8a2381582aa4a08)|2016-12-14 23:30:59
|777|jonasfj|Task life-cycle documentation|[URL](https://github.com/taskcluster/taskcluster-queue/commit/35b1c684156a839a8a369319ccaa81b0e6e2c6c1)|2016-12-14 20:57:50
|776|imbstack|Merge pull request #132 from taskcluster/add-lib-docs  Add tc-lib-docs|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ed35ce62fd2f250fe13b0e680e4fd684b12cc9c3)|2016-11-22 19:00:29
|775|imbstack|Fix docs tier|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5d856403ce2883f1ecf113412b39639f57251d01)|2016-11-18 00:46:41
|774|imbstack|Merge pull request #133 from taskcluster/add-lib-docs-pr  Removing indirection|[URL](https://github.com/taskcluster/taskcluster-queue/commit/283cd51ec3ea662d2d60ad4c32b012999d710408)|2016-11-16 20:06:18
|773|jonasfj|Removing indirection|[URL](https://github.com/taskcluster/taskcluster-queue/commit/47b5ab1630d8ed203df9f92b54f35ce873712165)|2016-11-16 20:03:12
|772|imbstack|Add tc-lib-docs|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f773baf77d3fd8a4609fec2937899ced058f0e7b)|2016-11-16 19:20:41
|771|jonasfj|Merge pull request #129 from taskcluster/skip-cache-header  Add support for x-taskcluster-skip-cache header|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d813ef2ea7452d1ec141a2f2395ae60d6d81774d)|2016-11-11 21:30:53
|770|jonasfj|Addressed review comments from jhford|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c85661f31f9958bb2634d292445709708e198eed)|2016-11-11 21:22:26
|769|jonasfj|Merge pull request #131 from owlishDeveloper/master  Eliminated tc-base from tests|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f60d8c261120b3b83743448bed082246ad1130b7)|2016-11-09 00:11:11
|768|owlishDeveloper|Eliminated tc-base from tests|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f772482101361413431477c3c48784a743aee234)|2016-11-09 00:07:14
|767|jonasfj|Merge pull request #130 from owlishDeveloper/noBase  Tc-base eliminated|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d24dcfaeaa38d1a5ae19baef1825b95ef0b2f4a9)|2016-11-08 23:01:30
|766|owlishDeveloper|Tc-base eliminated|[URL](https://github.com/taskcluster/taskcluster-queue/commit/76bd87d3f7f0092d7420419e0fe2719b5840fe7a)|2016-11-08 22:56:38
|765|jonasfj|Merge pull request #127 from owlishDeveloper/master  New ping API|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a7e15859da07669ac9ed8cb4ae53571061a455ec)|2016-11-08 21:08:32
|764|owlishDeveloper|New ping API; tc API directly; tc-base is back for everything else; new shrinkwrap; new package.json|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a40d8e672e489fcb850a1be35edb9bedf03922a5)|2016-10-21 21:15:39
|763|jonasfj|Add support for x-taskcluster-skip-cache header|[URL](https://github.com/taskcluster/taskcluster-queue/commit/87573741f99501b228113cea6e1f23b8e6ffe362)|2016-10-31 17:04:58
|762|djmitche|more lint|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7439ef735575b0474640b455d7bfde0879f733de)|2016-10-26 23:51:58
|761|djmitche|fix lint|[URL](https://github.com/taskcluster/taskcluster-queue/commit/11a0af5e4c57b47e8846ccf70ef871a72126e5b6)|2016-10-26 23:38:28
|760|djmitche|parallize s3 scanning|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d1f55da9215dc1bd9f45d1fefea1e1ca65072a30)|2016-10-26 23:15:33
|759|jonasfj|Merge pull request #126 from taskcluster/use-hint-id  Use hint|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b4fb052d385c2f8396f6417150bc5480274379da)|2016-10-25 18:42:33
|758|jonasfj|Merge pull request #124 from taskcluster/add-hint-id  Added hintId to all pending azure queue messages|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5d634809b5ffccbe3ff1f22dc75232cca8fb8e67)|2016-10-17 17:23:42
|757|jonasfj|Merge pull request #125 from taskcluster/more-let  change some: var -> let|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ba0ab77683ab4263d2681103a337397d6884c9a7)|2016-10-17 17:23:28
|756|jonasfj|Fixed bug where queue.claimWork can return two claims for the same task|[URL](https://github.com/taskcluster/taskcluster-queue/commit/86b1791759e9a6b7d096a3458ae5745b64d5a6b1)|2016-10-14 22:22:30
|755|jonasfj|Extract hintId and verify it is present in tests|[URL](https://github.com/taskcluster/taskcluster-queue/commit/68a4face9188729bca60ac75a271861ed0c28efd)|2016-10-14 18:40:45
|754|jonasfj|change some: var -> let|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3fc5335917de5ed36e4e9d1bdd6bdb8ff12c4ac9)|2016-10-14 18:08:58
|753|jonasfj|Added hintId to all pending azure queue messages|[URL](https://github.com/taskcluster/taskcluster-queue/commit/8c0140fc4ffe6026d42c044f6a624e75ee2f3c5a)|2016-10-14 18:07:11
|752|petemoore|Merge pull request #123 from taskcluster/deadline-exceeded-is-exception-not-failure  Fixed wording of deadline description|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d45c29675461ceff3a38c6881edfe700855f4517)|2016-10-04 18:42:09
|751|petemoore|Fixed wording of deadline description to advise that deadline exceeded is an exception not a failure|[URL](https://github.com/taskcluster/taskcluster-queue/commit/239748882deb7786ae14b486a2968bb87d68eb4c)|2016-10-04 15:27:26
|750|jonasfj|Merge pull request #121 from taskcluster/bug-1306040  Always resolve canonical region|[URL](https://github.com/taskcluster/taskcluster-queue/commit/710c72d9daaa9cc0100b7574a9041020f26fa489)|2016-09-28 21:16:11
|749|jonasfj|Added debug statement for CDN redirects|[URL](https://github.com/taskcluster/taskcluster-queue/commit/daf5faff8e632fc9bebd27ee81e4d24fdbca3ec5)|2016-09-28 21:14:11
|748|jonasfj|Always resolve canonical region  Should be a partial fix for https://bugzilla.mozilla.org/show_bug.cgi?id=1306040|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9a3f94a14a6c958486446f671aa42b40bd3affef)|2016-09-28 18:53:16
|747|jonasfj|Fixed linter issues|[URL](https://github.com/taskcluster/taskcluster-queue/commit/8e9a186726233904457dbac429074a5954a6fbd3)|2016-09-28 18:39:07
|746|jonasfj|Merge pull request #119 from djmitche/scanning  Add a skeleton of task/s3 scanning support|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ced3b7bd824b445fd33ce0deb5de87a65f02b8b3)|2016-09-23 18:41:11
|745|djmitche|Add a skeleton of task/s3 scanning support|[URL](https://github.com/taskcluster/taskcluster-queue/commit/64144f15d3b9d8dfcc0b1ada4d38b0a48b8a2555)|2016-09-22 13:57:24
|744|jonasfj|Merge pull request #118 from taskcluster/intermittent-task  Added intermittent-task reason for resolveException|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2b9008eae2312ef848ff49c7c0555cc8a402fe37)|2016-09-19 20:48:23
|743|jonasfj|Fix typo, credits @imbstack|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4882e5343ac7a278080d413b0eb3be9ad3a87311)|2016-09-19 20:47:55
|742|jonasfj|Added intermittent-task reason for resolveException|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1796f68f726005d71790fc670d9f25b48e134274)|2016-09-19 18:48:45
|741|jonasfj|Merge pull request #117 from taskcluster/fix-sentry-issue  non-printable ascii in artifact names -> 400|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3fce9ef39f9ffaf1de7d0390d3ec941ee6266aae)|2016-09-12 18:35:51
|740|jonasfj|non-printable ascii in artifact names -> 400  See: https://sentry.io/taskcluster/taskcluster-queue/issues/158299920/|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4f882205d0b8bf846e3c945a0b2b2c1ab9f972a5)|2016-09-12 17:58:18
|739|jonasfj|Merge pull request #88 from taskcluster/claim-work  [DONE] claimWork (ready to merge)|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a4b7ca4c32655f98330ff73b0581b29a67f4f7b1)|2016-09-09 17:26:03
|738|jonasfj|Upgraded node version in travis.yml|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2ef6b58465c0d935de5f26d63b8d15258a51b924)|2016-09-09 17:13:47
|737|jonasfj|Fixed reviewed comments by @imbstack and @jhford|[URL](https://github.com/taskcluster/taskcluster-queue/commit/17b8d33b800a1d67bcc7b8b09dedcb12834c78fe)|2016-09-09 17:12:16
|736|jonasfj|load-test createTask/claimWork/reportCompleted|[URL](https://github.com/taskcluster/taskcluster-queue/commit/094f2b9f18f50d102a1f93411de1fca9cc87e8f2)|2016-09-08 02:26:33
|735|jonasfj|load-test createTask/claimTask/reportCompleted|[URL](https://github.com/taskcluster/taskcluster-queue/commit/bb6ddf9d2ed3f88f15a88bc10f53835c8fea944a)|2016-09-08 01:35:08
|734|jonasfj|Revert "load-test with azure sas"  This reverts commit d055e5671fd8617c2084ace278c9cf3f716cc4e0.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1f1d65b967488f4211d3843b251b3a46e8d3424b)|2016-09-08 01:27:51
|733|jonasfj|load-test with azure sas|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d055e5671fd8617c2084ace278c9cf3f716cc4e0)|2016-09-07 23:58:20
|732|jonasfj|update load-test logic to test for 3mins|[URL](https://github.com/taskcluster/taskcluster-queue/commit/89ca231bdadf92ef8917ff26a896cd69e913359e)|2016-09-01 23:58:46
|731|jonasfj|Use real credentials for load-test|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7ee7f2b9274485f2de92087bca8d929a9bfd1ad9)|2016-09-01 23:49:47
|730|imbstack|Add expire-task-group-sizes to Procfile|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a5f51256b5657fda31ca888bf54dfcd40f540fda)|2016-09-01 23:35:31
|729|jonasfj|Mock monitor in all non-production configurations|[URL](https://github.com/taskcluster/taskcluster-queue/commit/120a39692bca01b14d069949d0464fbb2a4d9efa)|2016-09-01 23:41:31
|728|jonasfj|Upgrade to node 6|[URL](https://github.com/taskcluster/taskcluster-queue/commit/8a4394d461b6b03ad35bc17b583cd124f9740fdc)|2016-09-01 23:38:12
|727|jonasfj|Reduce load-test queue prefix|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ebc1b38d5fd3b00fea163ffdc0bbe42cecea3946)|2016-09-01 23:36:40
|726|jonasfj|Improved load-testing|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2467fec5d1f3fe4719b651f6a834c6dc223fe0bf)|2016-09-01 23:22:35
|725|jonasfj|Merge branch 'master' of github.com:taskcluster/taskcluster-queue into claim-work|[URL](https://github.com/taskcluster/taskcluster-queue/commit/025b88991296b4b3503253ef1b54af79930c8b25)|2016-09-01 22:39:07
|724|imbstack|Merge pull request #116 from taskcluster/add-inverse-test-for-task-group-resolved  Add inverse test for task group resolved|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b71eb6f574937b35b4b538f41cabf1067dfc7ef7)|2016-09-01 22:24:08
|723|jonasfj|Update taskgroup_test.js|[URL](https://github.com/taskcluster/taskcluster-queue/commit/94adc6e0aa63ee534294c0fd74e44b25ed8954d8)|2016-09-01 22:11:57
|722|jonasfj|Merge pull request #115 from taskcluster/bug1204898  Fix bug 1204898|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5ada924b5a674ed4669aed77ec9600d139b5e4a2)|2016-09-01 22:06:48
|721|imbstack|Make schedulerId mandatory in task-group-resolved messages|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d6c0a3323b21f615eccf23e583d9bed0027b7a8b)|2016-09-01 22:00:37
|720|imbstack|Add test that we're not resolving task groups too soon|[URL](https://github.com/taskcluster/taskcluster-queue/commit/73616295dbd022f6e47d3f1a16e1ef033714d674)|2016-09-01 21:49:09
|719|jonasfj|Fix bug 1204898|[URL](https://github.com/taskcluster/taskcluster-queue/commit/15823ada2e01ec8d542243a0323bcf20081056f9)|2016-09-01 21:35:02
|718|jonasfj|Added shrinkwrap|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2cb0f962916a139ee4d2285f0224bcd09fed97d1)|2016-08-27 03:27:51
|717|jonasfj|Fixed linter issues|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0366ef8d8cf293770622b039d19d8e97fd3b1463)|2016-08-25 20:49:15
|716|jonasfj|Fixed tests, claimWork works... load-tests needed|[URL](https://github.com/taskcluster/taskcluster-queue/commit/940b756235cf93b6722ed2603bfe48dd1d113918)|2016-08-25 20:42:06
|715|jonasfj|test case for QueueService|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d623f20e00375650cdaf4ce67719b4dca5c30346)|2016-08-24 01:01:36
|714|jonasfj|Fixed linter issues|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a5756bf2a891201eae2ebc09f3ad2e477a7025a0)|2016-08-23 22:28:41
|713|jonasfj|Merge branch 'master' of github.com:taskcluster/taskcluster-queue into claim-work|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e75a34d9032faeaf51022c4a3504ac678dfe2d9b)|2016-08-23 17:36:47
|712|jonasfj|More work on workclaimer, tests needed, code pretty much finished|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b8a08ea000d0d2558b716e5d99b74a5cbb34765b)|2016-08-23 17:36:18
|711|jonasfj|Patched queue service with polling logic|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1546979a188ed807adc4e8a95fabdfa59bdc98f0)|2016-08-23 17:35:53
|710|jonasfj|Merge pull request #114 from SingingTree/expiration_desc_missing_word  Description of task expiraiton has a missing word.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1237170704627ac683b2d4e49275582dd6b51ff7)|2016-08-23 17:21:10
|709|SingingTree|Description of task expiraiton has a missing word.  The description of task expiration looks like it's missing 'task' in the sentence: "Notice that all artifacts for the must have an expiration that is no later than this."|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a53f77655f1244ad98425565acab26c2bfeb9bd3)|2016-08-23 02:38:54
|708|jonasfj|Updated npm-shrinkwrap|[URL](https://github.com/taskcluster/taskcluster-queue/commit/41c8e15573abf819b6f29149fb75b3cef2794915)|2016-08-19 20:12:01
|707|jonasfj|Merge branch 'master' into claim-work|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f0c2e1393481311fdbe2c625faf0fa260b0049b5)|2016-08-18 21:47:18
|706|jonasfj|Merge pull request #113 from taskcluster/update-monitor  Update monitor to not loop on failures|[URL](https://github.com/taskcluster/taskcluster-queue/commit/bd9e89e926c094193e3739cefa5ef56e24411f30)|2016-08-15 16:57:14
|705|imbstack|Update monitor to not loop on failures|[URL](https://github.com/taskcluster/taskcluster-queue/commit/845fbbc0c2dac8ff21db516a7c59472e574813db)|2016-08-12 20:03:04
|704|jonasfj|Update shrinkwrap|[URL](https://github.com/taskcluster/taskcluster-queue/commit/31af5f78ddeb368420d4b392a1fc515b111396f9)|2016-08-10 16:59:55
|703|jonasfj|Merge pull request #112 from taskcluster/typos  Simplified text for taskGroupResolved exchange description|[URL](https://github.com/taskcluster/taskcluster-queue/commit/10c96e0b10544a8c9e45230c894181ec52dfbdec)|2016-08-03 16:49:16
|702|petemoore|Adjusted wording to account for scheduled/unscheduled|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d76c07f2ab171783d0a2b5fab1ac63dfe04b3d10)|2016-08-03 16:40:26
|701|petemoore|Aligned title of task-group-resolved exchange with other exchange titles|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a58035142af41fd38accbf14f9b7e44c80026547)|2016-08-03 09:12:00
|700|petemoore|Simplified text for taskGroupResolved exchange description|[URL](https://github.com/taskcluster/taskcluster-queue/commit/046c75027261d29a38550e0d1e765beafe5cd22c)|2016-08-03 08:51:02
|699|imbstack|Merge pull request #110 from taskcluster/add-sid-to-pulse  Start writing schedulerId in task-group-resolved|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b79e73d6e70ba74965eb369374c3379aa23d1a99)|2016-08-01 20:35:27
|698|imbstack|Start writing schedulerId in task-group-resolved|[URL](https://github.com/taskcluster/taskcluster-queue/commit/846e0fb2060a937111f252e68fa53f3d7cb8d6c7)|2016-07-29 22:36:34
|697|imbstack|Merge pull request #109 from taskcluster/add-sid-to-queues  Add schedulerId to some azure message queues|[URL](https://github.com/taskcluster/taskcluster-queue/commit/53c1a34a75211063f4c44f5b9acf3f2f21ec4682)|2016-07-29 21:19:05
|696|imbstack|Use better schedulerId in testing|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a7f88499db43ad76d95f4a5e49b562357ea6ec14)|2016-07-29 21:07:09
|695|imbstack|Update dependencies|[URL](https://github.com/taskcluster/taskcluster-queue/commit/20bbcfe318880c006fd7088f6819dcbef53cd865)|2016-07-29 21:05:40
|694|imbstack|Add schedulerId to some azure message queues|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5bbc7a09fc6a5c584d2f9ac7e140a1daeeb40e90)|2016-07-29 20:41:53
|693|imbstack|Merge pull request #103 from taskcluster/t-g-drained  Add pulse message for Task Group Resolved|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6410e1c9a24970bd1a5be299f071c2cc0c8b5b9f)|2016-07-28 21:45:32
|692|jonasfj|Updated package.json and npm-shrinkwrap.json|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a18fe47933717ea23147967718fff6e67f826deb)|2016-07-28 21:19:51
|691|imbstack|Update taskGroupActiveSet at deadline as well.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/beed4eb66e70eeaec35d890cb5aab91cb3c4dda2)|2016-07-28 00:58:49
|690|imbstack|Refactor a bit|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b0812c7a3307232ea85b106880e50de75e42897b)|2016-07-27 22:22:41
|689|jonasfj|More error info|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5fb775c99396b4fac27ba7e40ee6b4aeef451520)|2016-07-27 00:29:24
|688|imbstack|Add a check for idempotency of task group active sets|[URL](https://github.com/taskcluster/taskcluster-queue/commit/22c5c4cf64b7146090c7360cec51ada252b7c2de)|2016-07-26 21:19:26
|687|imbstack|Make task group completion route better|[URL](https://github.com/taskcluster/taskcluster-queue/commit/8fb0a3fbb48a35138590a27f743afc363967fbc3)|2016-07-25 18:10:46
|686|imbstack|WIP|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7370a7ca5f87d4cd22e536ebb43853263e2d95cf)|2016-07-21 23:24:37
|685|imbstack|Add a test for the task-group-resolved message|[URL](https://github.com/taskcluster/taskcluster-queue/commit/77eca5d341556768a70b6010eb1ce400bf690d86)|2016-07-20 00:05:19
|684|imbstack|Add a pulse message for when a task group is done|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7cf0820443bacc5bbbe4f3745f3db2923e1be6d5)|2016-07-19 22:49:50
|683|jonasfj|Merge pull request #108 from taskcluster/add-tg-to-deadline  Add task-group to deadline message as well|[URL](https://github.com/taskcluster/taskcluster-queue/commit/94167705b5ddf836f184c407291d923762e87ab5)|2016-07-27 23:26:11
|682|imbstack|Add task-group to deadline message as well|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a9f0689c54126bc586234d3877cdeca3852791fe)|2016-07-27 23:24:27
|681|jonasfj|Merge pull request #106 from taskcluster/enable-eu-central-1  bug 1285506 -- let queue rewrite urls for eu-central-1|[URL](https://github.com/taskcluster/taskcluster-queue/commit/98b90ddfdedb6c96cd8b6d197149cf7576ffdef0)|2016-07-26 18:36:45
|680|jonasfj|Fixed linter issues|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5497dd941a3815e351c00a779f551bbedc1533c5)|2016-07-26 18:36:03
|679|jhford|bug 1285506 -- let queue rewrite urls for eu-central-1|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7f3205db23f5f37b3718b2ca03a806f84808bb1d)|2016-07-26 12:47:53
|678|jonasfj|Merge pull request #105 from taskcluster/monitor-queue-emptiness  Count when work queues reach zero|[URL](https://github.com/taskcluster/taskcluster-queue/commit/fca8965305a8de87ddfc605efcf6761f05befd5c)|2016-07-23 00:26:46
|677|jonasfj|Count when work queues reach zero|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d198200d844351853e6121849f113dc6d3b7dd3e)|2016-07-23 00:20:58
|676|jonasfj|Merge pull request #104 from taskcluster/add-task-group  Add taskGroupId to taskResolved message queue messages|[URL](https://github.com/taskcluster/taskcluster-queue/commit/63cb130b91e8f87cbbfec48a00833ac8e782b874)|2016-07-21 23:47:44
|675|imbstack|Add taskGroupId to taskResolved message queue messages|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d7b93728e83e8c90b11f797851e1eb662bc185d9)|2016-07-21 23:41:05
|674|imbstack|Update shrinkwrap|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d851821cae2b999a26c387260ae4bc71499e409b)|2016-07-21 23:35:16
|673|jonasfj|Merge pull request #102 from taskcluster/explain-scheduleTask-ignores-dependencies  Updated scheduleTask docs to say it ignores dependencies|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f957b93869311983c4c97ba66623bf48968b3e07)|2016-07-12 14:58:29
|672|petemoore|Updated scheduleTask docs to say it ignores dependencies|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a119d25bc891ab7de6d4f32aececd9d4a7e16fcb)|2016-07-12 14:39:11
|671|jonasfj|Merge pull request #101 from taskcluster/bug1283450  Bug1283450|[URL](https://github.com/taskcluster/taskcluster-queue/commit/28e9fd91426c69d62d13405f7d0cbc975413d50c)|2016-07-05 16:41:59
|670|jonasfj|Fixed bug 1283450|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7f7b7f28ac476c03a63f888f516f9ad05d06858e)|2016-07-05 16:34:47
|669|jonasfj|Added test case proving we have a bug|[URL](https://github.com/taskcluster/taskcluster-queue/commit/16f2dc1e3870ed3ad7be02b76d322ca9f1192724)|2016-07-05 16:30:44
|668|jonasfj|Merge pull request #100 from taskcluster/fix-linter  Fix linter|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4319a4bf805bc36404d433f88353f22572263642)|2016-07-05 16:09:51
|667|jonasfj|Merge pull request #98 from taskcluster/more-monitor  More monitor|[URL](https://github.com/taskcluster/taskcluster-queue/commit/15ac6de93e1411c1da7685c6796389c1e97eeae5)|2016-06-30 18:03:13
|666|jonasfj|activate lint tests|[URL](https://github.com/taskcluster/taskcluster-queue/commit/47dfdbfd79a82a8fdac2085e9f68d578a34b5e79)|2016-06-29 14:53:56
|665|jonasfj|Fixed the last linter test|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f5fb5df2174c2f4e9f1819896f9136734ccad260)|2016-06-29 14:49:01
|664|jonasfj|Lots of minor linter fixes just by search/replace|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1455cc0a220467f7934253ed0ca24630111428bf)|2016-06-28 22:14:10
|663|jonasfj|Fixed half the linter issues|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5e05c89e57925086ec991ffb2deb654229420753)|2016-06-28 21:42:13
|662|jonasfj|Fixed exchanges|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ed6ae559d5cab0e44238aa0f1072c26d5364d147)|2016-06-28 21:35:16
|661|jonasfj|more linter fixes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/91a4d416fbac8807c9cc335b50567235a41769a4)|2016-06-28 21:29:06
|660|jonasfj|9 files passing YAY|[URL](https://github.com/taskcluster/taskcluster-queue/commit/bc933681efdbedf1f99390c87731d25e60327039)|2016-06-28 21:24:06
|659|jonasfj|fix linter in data.js|[URL](https://github.com/taskcluster/taskcluster-queue/commit/925ba0c480c32fefb541eca1d02d0a6cba228b37)|2016-06-28 21:20:13
|658|jonasfj|More linter fixes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/538e57a11a883df898354f848010352ea77b5428)|2016-06-28 21:13:52
|657|jonasfj|Fixed linter issuers in artifacts.js|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e1e1eee055fa2d859a3ff6527248240a7edb15f9)|2016-06-28 21:04:55
|656|jonasfj|Fixed a lot of linter issues|[URL](https://github.com/taskcluster/taskcluster-queue/commit/caba5ae0441facf5edd2f24da14970b23ba26ca7)|2016-06-28 17:26:40
|655|jonasfj|remove the last alert-operator|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7c14f95a7f574af7068701e7c8b4e9c13d319400)|2016-06-28 16:28:02
|654|jonasfj|Added monitoring for resolvers|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3b462c8f71f2d83e6ca8d249d40c718067a65629)|2016-06-28 15:41:14
|653|jonasfj|remove some more alert-operator|[URL](https://github.com/taskcluster/taskcluster-queue/commit/39a3180988d498171f188d8e73121169456ed626)|2016-06-28 14:45:28
|652|jonasfj|Fixed tests, and make sure dependencyresolver will crash|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4f45ea9f32507a6788a98be96949cfe0d2729915)|2016-06-28 00:39:32
|651|jonasfj|Merge branch 'master' into more-monitor  Conflicts: 	src/api.js|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f5fa8db4c16ad1a409d5759f487b702e042ee5b2)|2016-06-09 19:54:06
|650|jonasfj|Some more debug information|[URL](https://github.com/taskcluster/taskcluster-queue/commit/92ec6fedbb266e44e30a1fa08e1f14dcdd0b4502)|2016-06-05 22:54:20
|649|jonasfj|Merge pull request #97 from taskcluster/poll-loop-counter  Count poll-loop cycles|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9e4e050394c455ef9ebab482ce91a4c76bbd4ea4)|2016-05-27 15:43:47
|648|jonasfj|Count poll-loop cycles  Now we can make an alert in signalfx...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/76c2c39d6a3d66e51dff7fa7d31d5364be50d432)|2016-05-27 15:18:20
|647|jonasfj|Merge pull request #95 from djmitche/create-in-postorder  Must create tasks after their dependencies|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9a6f11b72d14b7d00ec9d212165354e24a6a0ebe)|2016-05-26 18:23:05
|646|jonasfj|Merge pull request #96 from taskcluster/fix-idempotency  bug 1275326 fix createTask idempotency|[URL](https://github.com/taskcluster/taskcluster-queue/commit/8cb909aa8bdf610e179f93b16913aee439bbd189)|2016-05-26 17:35:53
|645|jonasfj|We don't need at-least one run anymore as createTask with task.dependencies as a self-loop is the same as defineTask, so no distinction|[URL](https://github.com/taskcluster/taskcluster-queue/commit/791a8b826d95a6602993ac63811081c1f205b5ac)|2016-05-26 17:16:55
|644|jonasfj|Enabled linting too...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/08491d4cfd2d8026d2e84182ebe5c2ef2498e606)|2016-05-26 17:12:41
|643|djmitche|Must create tasks after their dependencies|[URL](https://github.com/taskcluster/taskcluster-queue/commit/bb2ae483dda8da94e0feb2fe9b4b13c47e7810b5)|2016-05-26 13:23:07
|642|jonasfj|Merge pull request #94 from taskcluster/list-dependents  List dependents|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e532c5170b0dcfe686d576bf6b97baa9e5dedbcc)|2016-05-24 01:37:37
|641|jonasfj|Merge pull request #93 from taskcluster/fix-loop-breaks  Similar improements for other resolvers|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5bbf1935679931170da28836b2aab4676be13e20)|2016-05-24 00:15:37
|640|jonasfj|Added tests that uses limit and continuationToken|[URL](https://github.com/taskcluster/taskcluster-queue/commit/26747529a52c73879f8bb32a1888a8814034e2b4)|2016-05-23 22:49:22
|639|jonasfj|Merge branch 'master' of github.com:taskcluster/taskcluster-queue into list-dependents|[URL](https://github.com/taskcluster/taskcluster-queue/commit/bef242dfce70682a371cc7da55f48a67d20b8b26)|2016-05-23 22:41:03
|638|jonasfj|Similar improements for other resolvers|[URL](https://github.com/taskcluster/taskcluster-queue/commit/79865d0a7ebe562051850768351c47e4b8136ac6)|2016-05-23 22:38:40
|637|jonasfj|Merge pull request #92 from taskcluster/fix-loop-breaks  emit('error' when loops crash|[URL](https://github.com/taskcluster/taskcluster-queue/commit/105f598338e409b3304ec8c9e7cd3f658f9ee81f)|2016-05-23 22:13:25
|636|jonasfj|reportError -> monitor.reportError, credits @gregarndt|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a723c279f253af33dcdb7b05ade3417b5f245bd4)|2016-05-23 21:56:03
|635|jonasfj|emit('error' when loops crash|[URL](https://github.com/taskcluster/taskcluster-queue/commit/91511e3f93cbbeffb7e77915fd324778a1ae5164)|2016-05-23 21:43:05
|634|jonasfj|More tests|[URL](https://github.com/taskcluster/taskcluster-queue/commit/602a411840f3dfdb7da62a8b573d7eb852eb2e3d)|2016-05-23 21:31:06
|633|jonasfj|Added list dependent tasks|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c25877bb9d0b53a22895a36fc2568ffd4c205687)|2016-05-23 21:08:15
|632|jhford|Use cloud-mirror instead of s3-copy-proxy, take 2  This reverts commit e009de0c852c9426fde24bd4515af222cea37ad7.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4ad55c11ff0db15567649f9ee25583c9b0891bd7)|2016-05-19 13:44:19
|631|imbstack|Merge pull request #91 from taskcluster/tabel  Fix tabel typo|[URL](https://github.com/taskcluster/taskcluster-queue/commit/518ace728abad18302eabfd77a1361b5aec6658b)|2016-05-18 22:03:13
|630|imbstack|Fix tabel typo|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5e7c0e316681258d7b124bda36682a4656144afd)|2016-05-18 21:52:14
|629|imbstack|Merge pull request #90 from taskcluster/new-monitoring  Use new monitoring library instead of tc-lib-stats|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1a5948ca08253c7c2c5addd831dca6ae0a6a3f7a)|2016-05-18 21:22:07
|628|imbstack|Gracefully exit scheduled jobs|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e8f442de3260599efc63f84529c25f7fe6b8ea0a)|2016-05-18 19:20:55
|627|imbstack|Use more descriptive monitoring names|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7ee6e40acb47bd35d67836b46bfea76d2261d64d)|2016-05-16 20:46:31
|626|imbstack|Don't use checked-in encrypted configs anymore|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7454ca3dbc049278681b450a21463b3273c0b7f9)|2016-05-16 18:40:53
|625|imbstack|Use new monitoring library instead of tc-lib-stats|[URL](https://github.com/taskcluster/taskcluster-queue/commit/8979b27f90d934865721b3f278763535c6d54dcb)|2016-05-16 17:42:39
|624|jhford|Revert "Use cloud-mirror instead of s3-copy-proxy"  This reverts commit e3241219559a1a22e8abc500d9af94288509c2d3.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e009de0c852c9426fde24bd4515af222cea37ad7)|2016-04-21 13:48:26
|623|jhford|Use cloud-mirror instead of s3-copy-proxy|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e3241219559a1a22e8abc500d9af94288509c2d3)|2016-04-20 13:05:12
|622|jonasfj|Added an comment to help explain|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1c1c0b942a3aff322801b273a78851e0f4263345)|2016-04-04 21:46:40
|621|jonasfj|Initial work on claimWork|[URL](https://github.com/taskcluster/taskcluster-queue/commit/985e0a1680685124241589b6230bed7db310a938)|2016-04-04 21:40:30
|620|jonasfj|Move src/main -> lib/main|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d410ff4d2303c6c3f8cf3c253016649c57c0a041)|2016-03-24 21:08:11
|619|jonasfj|Moved procfile from babel-node -> node|[URL](https://github.com/taskcluster/taskcluster-queue/commit/fad027d7e465553a8589c96f1c54e85ff623c07a)|2016-03-24 21:05:20
|618|jonasfj|Merge pull request #87 from taskcluster/babel-compile  Babel compile and new validator|[URL](https://github.com/taskcluster/taskcluster-queue/commit/994c7c1f3a481a4a885ac179da3da2927d74347b)|2016-03-24 20:50:37
|617|jonasfj|fixed all tests after bumping version|[URL](https://github.com/taskcluster/taskcluster-queue/commit/fda09119eab4c964203c397eefc2f4f1bd550c54)|2016-03-24 20:28:27
|616|jonasfj|Upgrade and lock dependencies|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1b4219982f8aeb412b0b8c1d9becd7f454cefea2)|2016-03-24 18:55:04
|615|jonasfj|Fixes thing we forgot... tests are passing|[URL](https://github.com/taskcluster/taskcluster-queue/commit/27c2b1d75ccef2d2fbf49cba58687e382845ebfc)|2016-03-23 23:31:32
|614|jonasfj|Modifed debug and require lines|[URL](https://github.com/taskcluster/taskcluster-queue/commit/905a92dc8045e7e0cb7d35db54719d0775d47750)|2016-03-23 23:21:52
|613|jonasfj|Moved tests|[URL](https://github.com/taskcluster/taskcluster-queue/commit/548331a65adaa47873b0321e5886199130b66958)|2016-03-23 23:10:09
|612|jonasfj|Merge pull request #86 from taskcluster/rm-config  Remove config/ folder|[URL](https://github.com/taskcluster/taskcluster-queue/commit/26bc92c4dd163ea476021a3c42100121adcca9c7)|2016-03-23 22:50:42
|611|jonasfj|Moved things around|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b188dc55bb904c4c5bc6e435b442973cd33c7895)|2016-03-23 22:42:09
|610|jonasfj|Remove config/ folder|[URL](https://github.com/taskcluster/taskcluster-queue/commit/685920e3b0f4b280aa332d877669acb328853aa1)|2016-03-23 22:06:53
|609|jonasfj|Merge pull request #85 from taskcluster/npm-shrinkwrap  Add npm-shrinkwrap|[URL](https://github.com/taskcluster/taskcluster-queue/commit/eaaf79d0b911ca8199f5c94b07a7ce66fc35e594)|2016-03-23 21:45:44
|608|jonasfj|Add cache on travis|[URL](https://github.com/taskcluster/taskcluster-queue/commit/bd2e4e1d8c78c7fcdfe0cd88501548dfdd033aac)|2016-03-23 19:10:20
|607|jonasfj|Add npm-shrinkwrap|[URL](https://github.com/taskcluster/taskcluster-queue/commit/306e96ad56d74fd9c255a04828644989d8dc8f81)|2016-03-23 19:06:17
|606|jonasfj|Merge pull request #84 from taskcluster/list-artifacts-w-continuation  Employ continuationToken for listArtifact|[URL](https://github.com/taskcluster/taskcluster-queue/commit/cc2e187e747563101106d80b238152d5e39c72a8)|2016-03-23 19:01:15
|605|jonasfj|Merge branch 'master' of github.com:taskcluster/taskcluster-queue into list-artifacts-w-continuation  Conflicts: 	schemas/list-task-group-response.yml|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5deb9cf92c9a72daf752ab45ff41ff4336215f9b)|2016-03-23 19:00:16
|604|jonasfj|Merge pull request #83 from taskcluster/break-list-group  More data in listTaskGroup, also breaks api...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a96efac0c721f4793f87379bc87fc90cf855c8c7)|2016-03-23 18:58:27
|603|jonasfj|more tests|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d9b0c632e6e98f5444760bc358d0f33d1db31e3f)|2016-03-23 18:30:43
|602|jonasfj|Return 404 for missing task or run|[URL](https://github.com/taskcluster/taskcluster-queue/commit/65bb42f71e27806fd7ad48127b78fa03c35bdeb2)|2016-03-23 18:23:57
|601|jonasfj|Minor spell check|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e1509e16df37d0e3946d5aa9d518b82b0a6064a8)|2016-03-23 17:16:49
|600|jonasfj|Employ continuationToken for listArtifact|[URL](https://github.com/taskcluster/taskcluster-queue/commit/83f0a37ced3c0ef3f1d698d2ab749cff1074f51b)|2016-03-23 01:13:26
|599|jonasfj|Merge branch 'gregarndt-patch-1' of github.com:taskcluster/taskcluster-queue|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e305d8620f701830acb3f1a43063e4dd80598076)|2016-03-22 23:58:51
|598|jonasfj|More data in listTaskGroup, also breaks api...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7570835878fe76204cf381c5b9e29b4b1fbafdfb)|2016-03-22 23:57:20
|597|jonasfj|Merge branch 'master' of github.com:taskcluster/taskcluster-queue into task-deps|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d48ff32331fe67084a34e9a7e2d1e13f61dcb7c9)|2016-03-22 20:33:54
|596|jonasfj|bug 1251435|[URL](https://github.com/taskcluster/taskcluster-queue/commit/98845f1b69f173abb391a385cffc17169f067608)|2016-03-17 23:32:12
|595|jonasfj|Merge branch 'master' of github.com:taskcluster/taskcluster-queue into task-deps  Conflicts: 	config.yml|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f0c1a0001fc1a8d6c56a608cc81927550180f48b)|2016-03-17 18:56:53
|594|jonasfj|Better error code formatting..|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d9279beb32d6d770b1cebd920073a669e10cec1f)|2016-03-17 02:25:54
|593|jonasfj|Tests for expiration|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4db779e78181b6f5e9f0879c671116518f09cf40)|2016-03-17 02:22:28
|592|jonasfj|Added expiration|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b52525eb1f4dfa8c97dea67fda504859383dcd8e)|2016-03-17 00:31:38
|591|jonasfj|Done with all tests... need only expiration...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a54bee14d864208d014cbeb42918b76387ee2d7b)|2016-03-17 00:15:01
|590|jhford|fix exception|[URL](https://github.com/taskcluster/taskcluster-queue/commit/489ef6581e3509e3d9f8252ab03a53c5606df601)|2016-03-17 00:12:50
|589|jonasfj|Moved dependency resolution to background worker|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b81a0bad0496012b86acbba8a5600b0245118124)|2016-03-16 20:51:25
|588|jonasfj|task.dependencyRelation -> task.requires|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e60201256796f91321f3103050ecea5bbe62067d)|2016-03-16 18:45:25
|587|jhford|because travis|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c1dbedcbe6b5aca6f02b06a93cbe8af1deefa3d4)|2016-03-16 18:08:26
|586|jhford|fix cloud-mirror opt-in|[URL](https://github.com/taskcluster/taskcluster-queue/commit/65393a90cffaec23baf73414f7dc4dfab727c22d)|2016-03-16 17:27:24
|585|jhford|more logging for useCloudMirror path|[URL](https://github.com/taskcluster/taskcluster-queue/commit/557edb18ae4c8929053bb686e5749e947fe40fd0)|2016-03-16 16:45:46
|584|jhford|rename testing tables|[URL](https://github.com/taskcluster/taskcluster-queue/commit/69e446470cf72a8c2ee306f85150abd1302e3b50)|2016-03-16 16:03:23
|583|jhford|Merge branch 'use-cloud-mirror'|[URL](https://github.com/taskcluster/taskcluster-queue/commit/695b7e109dc7363a3e4711d13e4bc58356123b5c)|2016-03-15 18:16:58
|582|djmitche|add doc about routing key scopes, since I missed it|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ac5daa109c917b3e9a996208e9d49a70ff74dd8c)|2016-03-03 14:30:36
|581|jonasfj|All tests are passing :)|[URL](https://github.com/taskcluster/taskcluster-queue/commit/31f545eabb54adc12ca323fa2963c25795a58df3)|2016-03-02 00:45:23
|580|jonasfj|Fixed a lot of small issues|[URL](https://github.com/taskcluster/taskcluster-queue/commit/8fad0c303f7ee2a11adb4ab5ccd40dbef21bd8cd)|2016-03-01 23:44:25
|579|jonasfj|Fixed a few bugs..|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e0b5a655ac17ab968f9dafc6c7c69e398a0756de)|2016-03-01 21:19:07
|578|jonasfj|Finished task.dependencies, no tests - not sure I dare run this, he he|[URL](https://github.com/taskcluster/taskcluster-queue/commit/88aa0f78e7dac7721855dc9451435eab3467d488)|2016-03-01 19:11:58
|577|jhford|opt in to using cloud-mirror|[URL](https://github.com/taskcluster/taskcluster-queue/commit/84fcdeb972a8af7cc6ae40f103e370c95a9d65ab)|2016-02-26 16:39:38
|576|gregarndt|Fix error message when reclaiming past deadline|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1e8a959b18cc99b28fa2d45fc37737f6eab87d4f)|2016-02-23 21:36:56
|575|jhford|Initial work for transitioning to cloud-mirror|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6a5a6acd46a815cac3d19ee1cf92ab6fb713c197)|2016-02-15 17:41:26
|574|imbstack|Merge pull request #78 from taskcluster/replace-more-old-errors  Update to all new-style errors in v1.js|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2ab0317576d9b7c6ca9b011a76ff36aaf7eaff3e)|2016-02-12 18:24:35
|573|imbstack|Use correct errors|[URL](https://github.com/taskcluster/taskcluster-queue/commit/bdd3b89c55fadcd83c2272c0097cc1402e94902a)|2016-02-11 20:15:44
|572|imbstack|Update to all new-style errors in v1.js|[URL](https://github.com/taskcluster/taskcluster-queue/commit/99620119b45208f046d20c13a22a5589a428d215)|2016-02-10 21:54:30
|571|imbstack|Merge pull request #77 from imbstack/sentry-and-newstyle  Sentry and newstyle|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ae8e278822e100a9569bcc4664b0c5d85104e3e0)|2016-02-10 18:02:30
|570|imbstack|Improve error message for conflict when creating task|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a1a866c40e663eaed332bd859f6db90841b6130f)|2016-02-10 00:58:38
|569|imbstack|Add note about sentry DSN|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0d70a1c14f58efbd76376d30d05e24a0a1d643e9)|2016-02-10 00:41:00
|568|imbstack|Add sentry/raven as an option|[URL](https://github.com/taskcluster/taskcluster-queue/commit/cd1806b696909f012891c6bd1079f0f1aa995e59)|2016-02-10 00:37:23
|567|imbstack|Add some more new-style error reporting|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5ae69ac12e050afad9c125a6e57abb892185b560)|2016-02-10 00:37:11
|566|imbstack|Bump tc-base to get new tc-lib-api for raven/sentry|[URL](https://github.com/taskcluster/taskcluster-queue/commit/cdfe2fc0c8d76cc348dd29ef83c975e871a1a9c5)|2016-02-09 21:23:58
|565|imbstack|Merge pull request #76 from taskcluster/update_to_new_errors  Update to new errors.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4467305abea7cd0e003d654a0b3b008506e3d7e3)|2016-02-08 19:29:17
|564|imbstack|Respond to code review comments.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/bd446ba775adecf2f2d3b8e938e63466658d9fe9)|2016-02-08 19:23:11
|563|imbstack|Use details and message field properly|[URL](https://github.com/taskcluster/taskcluster-queue/commit/80fe3463f2e9f1ba06a2bdbb6f687d20425c26d5)|2016-02-08 18:48:41
|562|imbstack|Add first new reportError call|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0b72a1f14cc24d1a58388c99f28ca0f3a83633bb)|2016-02-08 05:54:01
|561|petemoore|Added IRC notifications to irc.mozilla.org#taskcluster-bots|[URL](https://github.com/taskcluster/taskcluster-queue/commit/979055f24c1c370b871e56f87cb609e681cb6c36)|2016-01-26 18:13:53
|560|jonasfj|Merge pull request #74 from taskcluster/remove-pending-tasks-scope  Remove pending tasks scope|[URL](https://github.com/taskcluster/taskcluster-queue/commit/78fd4267dfd894dd5d4802f87126581a9a8a8fe7)|2016-01-26 16:10:02
|559|jonasfj|Added some documentation|[URL](https://github.com/taskcluster/taskcluster-queue/commit/099c695d639d05c1a01f5e71a7de2777eeb7f869)|2016-01-22 17:19:03
|558|jonasfj|Initial commit removing pendingTasks scope|[URL](https://github.com/taskcluster/taskcluster-queue/commit/15278259038f29c2caf92867674558cde0bd76c7)|2016-01-22 17:07:50
|557|jonasfj|Merge branch 'master' of github.com:taskcluster/taskcluster-queue into api-stability-levels|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a47a60732692b2d19b022b93f865d9918f8ea97a)|2016-01-19 21:31:27
|556|jonasfj|Version bump, + minor fix|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4ad4448d0fc3f89d16c416e5f9e653e6fd859c9a)|2016-01-19 21:30:50
|555|jonasfj|Merge pull request #73 from taskcluster/api-stability-levels  bug 1237308|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1c6b02844bbb45ccad73133ec32f3eb16602bd85)|2016-01-15 22:12:32
|554|jonasfj|Fix bug 1237308|[URL](https://github.com/taskcluster/taskcluster-queue/commit/31c0fdeb4bd40a06b417227eb73e76414fc989c3)|2016-01-15 22:11:42
|553|jonasfj|bug 1237308|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1a6227938a27e872e8195e6afaaf358dd1f90929)|2016-01-15 19:54:48
|552|jonasfj|Merge pull request #72 from taskcluster/list-by-task-group  List by task group|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3865e356f44cf3fe82d62cd8991fa86b46580077)|2016-01-15 19:04:21
|551|jonasfj|Address review comments|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6c03cc90697e97ccbe74cd3f4fdb61c518973fe1)|2016-01-15 18:57:32
|550|jonasfj|Expiration and more tests...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/337dd349f9ba559cb659d6baac43ea360c0f1284)|2016-01-15 00:39:52
|549|jonasfj|Bug 1137914|[URL](https://github.com/taskcluster/taskcluster-queue/commit/80b994b0f78b3a84eb2b9023ab8f5981cc99ce68)|2016-01-14 23:46:34
|548|jonasfj|Got listing to work with continationToken|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1cb7da214abfbf734519522b8c4fb855086a3846)|2016-01-14 23:35:04
|547|jonasfj|Added test for single schedulerId per taskGroupId|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f82586f1215a3d968b3254a59a4009cd3723fe7d)|2016-01-12 20:45:20
|546|jonasfj|Merge branch 'master' into list-by-task-group|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7388be32ee79f0b61473948b58c77f18d5c6c2e0)|2016-01-12 20:28:22
|545|jonasfj|Merge pull request #71 from taskcluster/lock-scheduler-id  Lock scheduler|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4247c9b041b52a0e39c4ad4b1e7cdf6e890a42ec)|2016-01-12 20:27:23
|544|jonasfj|Merge branch 'master' into list-by-task-group|[URL](https://github.com/taskcluster/taskcluster-queue/commit/718041005841aca544fce1b8999d33af7fc243cf)|2016-01-12 20:15:31
|543|jonasfj|Test cleanup, as we removed some scopes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/267555a66cac88bf7298896cf0b07c7740474cba)|2016-01-12 20:12:47
|542|jonasfj|Minor clean up|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2999bcdc9c190c63a461f7a50892ba0a4dc1a812)|2016-01-12 20:05:40
|541|jonasfj|Merge branch 'master' into lock-scheduler-id  Conflicts: 	routes/v1.js|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1ca00a737f9d12a2bd92fe6ef53ffac1e40bfe04)|2016-01-12 20:02:30
|540|jonasfj|Merge pull request #69 from djmitche/bug1230344  Bug 1230344: add 'superseded' as an exception reason|[URL](https://github.com/taskcluster/taskcluster-queue/commit/da0119e5019042c65d5ad5af35871324e59fccbb)|2015-12-04 20:58:22
|539|djmitche|Bug 1230344: add 'superseded' as an exception reason|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b3fa6e10f8a1ac5fc39e86db0280e04fa440e69c)|2015-12-04 19:52:01
|538|jonasfj|Merge pull request #68 from taskcluster/scope-workerid  Added queue:worker-id:..|[URL](https://github.com/taskcluster/taskcluster-queue/commit/42b160ca2421595a0dc2855454946aff8d774a3d)|2015-12-01 20:04:29
|537|petemoore|markup fix in schema|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9da437f0b3d680ad7173336157ad30facc418e1e)|2015-11-26 14:42:50
|536|petemoore|Fixed backtick typo that wreaked havoc upon http://docs.taskcluster.net/queue/api-docs/#reportException|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0cba9147e1ce20ab1f51e7ccd773ccee1daaecef)|2015-11-26 14:33:53
|535|jonasfj|Added queue:worker-id:..|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e03410b5f278f16d9d0080a58cb5bc05fdab7147)|2015-11-25 22:06:23
|534|jonasfj|Merge pull request #67 from taskcluster/remove-assume  Bug 1228012: Deprecate all assume: scopes in API endpoints|[URL](https://github.com/taskcluster/taskcluster-queue/commit/de85475458273fb79736b7d313692307378abcec)|2015-11-25 21:46:46
|533|jonasfj|Refactored and clean up all the new scopes as discussed this morning|[URL](https://github.com/taskcluster/taskcluster-queue/commit/847ef2319982e64ab2fcb28b64608b49a74a3657)|2015-11-24 21:43:29
|532|jonasfj|another hack along the way|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e28ac8d353d5472cb21dce17c14cb859c08b3bfc)|2015-11-24 19:37:01
|531|jonasfj|Save so we have secondary index|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ca6b1c0ea41aa528800546304af9912f2dfbeb78)|2015-11-20 23:34:22
|530|jonasfj|Deprecate all assume: scopes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/8a1cef1b70aa6d9f239c897a1bb2edabc6b35279)|2015-11-20 21:51:35
|529|jonasfj|Minor code clean up|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5bd2668766bc08dfecbdd7c3de209a88fb949563)|2015-11-18 23:43:52
|528|jonasfj|Force scope for sceduler-id|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2c8ff1647bdee2965a2f147850b81736b7933e27)|2015-11-18 22:48:02
|527|jonasfj|Added USE_PUBLIC_ARTIFACT_BUCKET_PROXY|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c82c5d0ba580e6389a97c748ed4b088e572f6117)|2015-11-18 00:55:16
|526|jonasfj|Merge pull request #66 from taskcluster/upgrade-tc-base  Upgrade tc base|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d18661770d455787a7a8557249031cfadbfd3c7b)|2015-11-17 19:29:48
|525|jonasfj|Upgrade to node 4|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d2d1443895868e4b26d9cb75d2780dccfba479e6)|2015-11-13 21:04:29
|524|jonasfj|Added user-config.yml.enc|[URL](https://github.com/taskcluster/taskcluster-queue/commit/bfea23b967c89b8477fc37bc4a14891aba21fe31)|2015-11-13 21:00:16
|523|jonasfj|Nice travis, and bug fix|[URL](https://github.com/taskcluster/taskcluster-queue/commit/28a42dbe37ce66f6a9691f73f01a30a8afdc8d01)|2015-11-13 20:43:20
|522|jonasfj|Minor fixes and travis working I hope|[URL](https://github.com/taskcluster/taskcluster-queue/commit/8f1f198ffd9defb61b0dbd5e394fe6e15adda57c)|2015-11-13 20:41:26
|521|jonasfj|Moved away from legacy config|[URL](https://github.com/taskcluster/taskcluster-queue/commit/cb26815de7bda61e96279b5a1e67c545f251f327)|2015-11-13 19:49:46
|520|jonasfj|Remove old binaries|[URL](https://github.com/taskcluster/taskcluster-queue/commit/208c6f509c6c94aad3f5c7769675b7401233347d)|2015-11-13 19:23:35
|519|jonasfj|Added src/|[URL](https://github.com/taskcluster/taskcluster-queue/commit/abeae65ba4431fe658c1b8a566326306a08c9273)|2015-11-13 19:22:49
|518|jonasfj|config and test works using loader|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f38ef74b2735d1ed6d80c8b0100bb851c4bb7a69)|2015-11-13 01:16:37
|517|jonasfj|Upgraded tc-base|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c58dad2c574b9f9c81d55f1bccf2d924f59cbc99)|2015-11-11 21:40:50
|516|petemoore|Merge pull request #64 from taskcluster/bug1221132  Bug 1221132 - improve wording|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3af44218e9e64fcc1ddf3867c0269b0083c61c5f)|2015-11-09 12:15:31
|515|petemoore|trivial text correction in README.md to trigger a new build after disabling push builds in travis (so push builds and PR builds don't run in parallel)|[URL](https://github.com/taskcluster/taskcluster-queue/commit/09ac67eb9fc89e125c248dc4bf29814edf34c984)|2015-11-09 12:00:15
|514|petemoore|Resolved merge conflict|[URL](https://github.com/taskcluster/taskcluster-queue/commit/883f37b55e3cb8d77751681f418ab24718c35ef5)|2015-11-09 11:43:33
|513|petemoore|Undid post -> put for defineTask based on feedback from jonasfj in PR #64|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f24b16f3df0daae9fb89b68daec5ef359ab3da56)|2015-11-09 11:37:47
|512|jonasfj|Merge pull request #65 from taskcluster/add_post-artifact-response_type  Added missing type|[URL](https://github.com/taskcluster/taskcluster-queue/commit/73074e1a9f03f09f1aed443b470971c2e0a5b9c9)|2015-11-05 21:01:25
|511|petemoore|Added missing type|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e2253cce4e8bf37bfe71194ed02c6799b9781253)|2015-11-05 08:04:54
|510|jonasfj|Merge pull request #63 from taskcluster/bug1221045  Bug 1221045 - fix to schemas and routes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a89522266f7e54355e7bd007f99c66836c3cab0d)|2015-11-03 18:58:45
|509|petemoore|Alternative fixes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/372496d17db919ddb5de6a489d009970928d2661)|2015-11-03 18:15:53
|508|petemoore|Alternative fixes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2d5488eca759af074de81415cd24a763377313d0)|2015-11-03 18:14:28
|507|petemoore|syntax fix|[URL](https://github.com/taskcluster/taskcluster-queue/commit/8786bb159e50b83a639925c506c82f2ef3f0ba52)|2015-11-03 15:35:23
|506|petemoore|Bug 1221132 - improve wording|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e0564683ded19732c1a25b0eb663aafd00b0552d)|2015-11-03 15:05:02
|505|petemoore|Bug 1221045 - fix to schemas and routes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/afc13e57622747923a1276e0f510308e3ad30489)|2015-11-03 10:32:52
|504|jonasfj|Merge pull request #61 from taskcluster/issue-temp-creds  Issue temp creds|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3aac5faa841b1b8efefb48442122ce9e7094e52b)|2015-11-02 22:01:13
|503|jonasfj|Fix comments by @garndt|[URL](https://github.com/taskcluster/taskcluster-queue/commit/863c95e4cbb634eb76d06196809b4bf9516ba070)|2015-11-02 21:51:42
|502|jonasfj|Fixed schema bug|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6f3ddb49263a5f0d78043b8a834c36e5ca0e1796)|2015-10-28 19:31:18
|501|jonasfj|Test for creating artifacts with temp task creds|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d99b540e1ee21a39243eaaedb1f8bb4903b30a1d)|2015-10-28 18:52:15
|500|jonasfj|Added extra tests to resolve task tests|[URL](https://github.com/taskcluster/taskcluster-queue/commit/fdac00ab616580fec10a26d3fe8c6646c69d8317)|2015-10-28 18:44:16
|499|jonasfj|Tests for claim/reclaimTask|[URL](https://github.com/taskcluster/taskcluster-queue/commit/8bbcb36da30a4b661dc6d012549ac1a2e6702093)|2015-10-28 18:39:09
|498|jonasfj|Changed scopes to something nice..|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5548f44f6f206649477766e993b164a957f77c0b)|2015-10-28 18:27:28
|497|jonasfj|Added temp creds and task def to claim/reclaim|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d8345ab7f5e8aee18ee502c8d4a5c121c28b12ed)|2015-10-28 18:17:26
|496|jonasfj|Merge pull request #60 from petemoore/bug1218913  Bug 1218913 - added missing type entries to schemas|[URL](https://github.com/taskcluster/taskcluster-queue/commit/faa3defcadb4e0bf00662dda1b3b350c101fa02d)|2015-10-28 17:06:18
|495|petemoore|Bug 1218913 - incorporated review feedback from @jonasfj in PR #60|[URL](https://github.com/taskcluster/taskcluster-queue/commit/523483fab85dd98e56c1d39c8384d3115d0bef92)|2015-10-28 07:19:30
|494|jonasfj|Fix issue in task.yml which doesn't like comma|[URL](https://github.com/taskcluster/taskcluster-queue/commit/25f258ae657b13b507177a76eaf387f348c9bb6b)|2015-10-28 01:02:54
|493|petemoore|Bug 1218913 - added missing type entries to schemas|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f3fd365505358499f7d9a386af3d9504a1f330ff)|2015-10-27 19:45:28
|492|jonasfj|Merge pull request #59 from djmitche/bug1193607-$  add trailing `$` to scope pattern|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7b478d76f37c01b50bb17e6dcc773598e19d5cd3)|2015-10-26 17:14:00
|491|djmitche|add trailing `$` to scope pattern|[URL](https://github.com/taskcluster/taskcluster-queue/commit/017f7d8340bdef3fe008a1e9753711e1468402a1)|2015-10-26 14:26:15
|490|jonasfj|Merge pull request #58 from djmitche/bug1193607  Bug 1193607: update schema for limite scope charset|[URL](https://github.com/taskcluster/taskcluster-queue/commit/110d3d8b6c6460dbd43fe95572dce39f9b2eefc4)|2015-10-20 17:02:49
|489|djmitche|Bug 1193607: update schema for limite scope charset|[URL](https://github.com/taskcluster/taskcluster-queue/commit/cfe96a529ff56c3d4e1c340f194413cac16c5599)|2015-10-19 16:50:50
|488|jonasfj|Merge pull request #57 from taskcluster/public-bucket-cdn  Support for public bucket cdn|[URL](https://github.com/taskcluster/taskcluster-queue/commit/05e1362d89b787cbb100981be1c950e10dd98682)|2015-10-14 20:38:07
|487|jonasfj|Support for public bucket cdn|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1df11566f821eb0f91997ae657bb7849f5bacc48)|2015-10-14 20:19:05
|486|jonasfj|Merge pull request #54 from taskcluster/remote-signature-validation  Remote signature validation|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d6307d70c1ad9231fe4a170f456b27a4bef38dd0)|2015-09-10 20:16:27
|485|jonasfj|Merge pull request #56 from petemoore/no-travis-heroku-auto-deploy  Disabled travis auto-deploy to heroku - no longer used and was broken|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7938a78833c6af78f5cec9cd1d9038a63577eb40)|2015-09-10 19:32:56
|484|petemoore|Disabled travis auto-deploy to heroku - no longer used and was broken|[URL](https://github.com/taskcluster/taskcluster-queue/commit/575d140bbb70df0f6310434a8060447936ff31cd)|2015-09-10 10:57:01
|483|jonasfj|Merge pull request #55 from petemoore/bug1202573  Updated slugid pattern to enforce uuid v4 compliance|[URL](https://github.com/taskcluster/taskcluster-queue/commit/bc6ed5acfb28622596308784d2aae632b6af4c3d)|2015-09-08 17:56:49
|482|petemoore|Updated slugid pattern to ^[A-Za-z0-9_-]{8}[Q-T][A-Za-z0-9_-][CGKOSWaeimquy26-][A-Za-z0-9_-]{10}[AQgw]$|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6b19b69e13ac2dbcc731ebad713adb5b44f4eb98)|2015-09-08 14:27:08
|481|jonasfj|Updated tc-base|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9da7f6945f2b08d869f8c89672f33343541407ad)|2015-09-04 18:27:50
|480|jonasfj|Clean up and final fixes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/daa07b6385b1c4f11dc78a8844741aff11c19c98)|2015-09-03 01:47:43
|479|jonasfj|load-test changes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2580e4e3f41fd1297b6864f711260874040118bb)|2015-08-18 20:13:18
|478|jonasfj|load-test changes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/52452d2f711d5715787857cfc027f2d0455632e9)|2015-08-18 17:15:15
|477|jonasfj|load-test changes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3c9bc6435f8acdba793ea32fc1553cc3f127d0ab)|2015-08-18 01:15:36
|476|jonasfj|load-test changes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/144aaaf0661e5063ae8fdb36bbb5ede4eb779d07)|2015-08-17 23:26:14
|475|jonasfj|load-test without remote signatures|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9f7cefa23b5af9ae59ec39dfa1fadb6d9adff6be)|2015-08-17 22:20:39
|474|jonasfj|Added remote-signature support, ready for load-test|[URL](https://github.com/taskcluster/taskcluster-queue/commit/042f5668b95cf0119c65f555d63239efdaf51776)|2015-08-17 21:01:34
|473|jonasfj|Merge pull request #47 from taskcluster/internal-error  Internal error (bug 1180055)|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c2d56afffa87e0a8256e1b2ed7c86361becedcf5)|2015-08-31 23:52:13
|472|jonasfj|Minor fix from garndt|[URL](https://github.com/taskcluster/taskcluster-queue/commit/254db2a86c3c92c1e027c047f68cfaa38efe6c37)|2015-08-31 23:51:57
|471|jonasfj|Merge branch 'master' into internal-error|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0ef50be8768bc1e30b73eefba16a0a4819755c74)|2015-08-31 23:49:13
|470|jonasfj|Merge branch 'internal-error' of github.com:taskcluster/taskcluster-queue into internal-error|[URL](https://github.com/taskcluster/taskcluster-queue/commit/cd4526bc115072f71a600761d0f4ee406d84c068)|2015-08-31 23:48:14
|469|jonasfj|Merge pull request #52 from petemoore/bug1199634  Bug 1199634 - delete Vagrantfile|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d9bfcb7d06df932e81ca83a46fefe20db19ff899)|2015-08-31 20:12:31
|468|petemoore|grammatical correction: it's own -> its own|[URL](https://github.com/taskcluster/taskcluster-queue/commit/dfd462e470843c5a6faecfcd2bcaedfc5747d679)|2015-08-31 10:13:18
|467|petemoore|Removed vagrant references from project  Also updated README.md with more explicit details about how to get tests running locally.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/971067a684b53f3dbf8b92b9349897eb6595e944)|2015-08-31 10:08:43
|466|petemoore|Wrapped excessively long lines in README.md|[URL](https://github.com/taskcluster/taskcluster-queue/commit/123b38f8c24ea092f87c25273d599e42c7de01af)|2015-08-31 09:52:16
|465|petemoore|Bug 1199634 - updated /etc/apt/sources.list and /etc/apt/sources.list.d/docker.list and pull down key for docker apt repo|[URL](https://github.com/taskcluster/taskcluster-queue/commit/74c59b3647efcce93682696e9360cfc5d9c1c1be)|2015-08-28 12:49:20
|464|jonasfj|Added test for no creds needed for queue.task()|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b2d6a39ec273a7d6a8bfda32fa169cb53116e94b)|2015-08-28 02:47:55
|463|jonasfj|Fixed for [[]] not working I fear|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b7952119fa5ef1093f84b82f8e46766e7c1076a9)|2015-08-28 02:39:56
|462|jonasfj|Merge pull request #51 from taskcluster/extra-exception-messages  Fix extra exception messages after deadline|[URL](https://github.com/taskcluster/taskcluster-queue/commit/60f607c4f4f143dbfb5251123ce51f2dd166e34e)|2015-08-24 21:17:06
|461|jonasfj|Fix extra exception messages after deadline  Avoid duplicate messages for exceptions after deadline... We should only report the messages if `deadline-exceeded` is the reason.    If it was cancelled, or something else... we should publish another message about that.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0a6e3af369a4daf981b242949a381d9a88a4856b)|2015-08-24 20:00:35
|460|petemoore|Merge pull request #49 from taskcluster/priority-intermittent-error  Fixed intermiettent test error|[URL](https://github.com/taskcluster/taskcluster-queue/commit/feaf2c7d319d65b16a423893a47954591dc56df5)|2015-08-04 14:16:39
|459|jonasfj|Fixed intermiettent test error|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6f678536356c394e4ea382832c44e2795081ea8b)|2015-07-31 00:01:35
|458|jonasfj|Added internal-error and resource-unavailable|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b45df6a9454515ad7354dc73b0379b8906b78370)|2015-07-29 23:49:42
|457|jonasfj|Removed unnecessary statements from @gargarndt tests|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e50c988b8a6f884afcfc8f55f3133eee62c0751c)|2015-07-30 19:26:43
|456|jonasfj|Merge pull request #48 from gregarndt/error_message_create_artifact  Error response should include artifact details|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9cac714ab4bd328bb57a6aaf106f3d0eab2e616b)|2015-07-30 18:52:43
|455|null|Throw original error rather than rely on assume().fail|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e7a6246104c5b0f613cbda303f5fce767583afa0)|2015-07-30 18:50:30
|454|jonasfj|Merge pull request #46 from taskcluster/update-tc-base  Update tc base|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9a8c58575fc9e16efa9cb2b67d8911117728adac)|2015-07-30 17:33:37
|453|null|Error response should include artifact details  When a request is made to update an artifact, details about the original as well as the new artifact should be included in the error response when the artifact can not be updated.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5262ee6751f39ec59dc6e25e50abaad661a59bcb)|2015-07-30 16:15:00
|452|jonasfj|Added internal-error and resource-unavailable|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e9a0dc373649033287c91424235f6418d9a3fb74)|2015-07-29 23:49:42
|451|jonasfj|Refactored to use schemaPrefix in API and exchanges|[URL](https://github.com/taskcluster/taskcluster-queue/commit/66054514b5ebd240486045ddafe0fb1dd3bed916)|2015-07-29 20:29:43
|450|jonasfj|Use the params: {...} on API for parameter validation|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ff7aa2f1e5c710d3b3c2441ef6bb18f8efcd44fc)|2015-07-29 20:20:47
|449|jonasfj|Removed ids from all schemas - rely on generated ones|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c8c827b63fe4f88dba258f1dba9f3199f3746e0d)|2015-07-29 20:20:28
|448|jonasfj|Ported schemas to yaml|[URL](https://github.com/taskcluster/taskcluster-queue/commit/94b1eed033bcbc39e8c64de09b5b369bf4df2451)|2015-07-29 19:59:41
|447|jonasfj|Removed unused schemas|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d36b87d9e36a7eb61f9c8a18142da53390bd1ddd)|2015-07-29 19:37:41
|446|jonasfj|Fixed up scopes and schemas ids|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d96306c57ec2a21c8c62a9966deb08c95a02e86d)|2015-07-29 18:56:57
|445|jonasfj|Fixed intermittent test issues|[URL](https://github.com/taskcluster/taskcluster-queue/commit/14d283328851b360f55fc44169ec9eda13ccc76e)|2015-07-29 18:29:45
|444|jonasfj|Merge pull request #45 from taskcluster/fixed-scopes  Fixed scopes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c720df6dd025327d41b4b35607dd1f726fca7a26)|2015-07-28 16:07:50
|443|jonasfj|Fixed scopes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/beaa7e037a7e9e0a740591c94237a8a407c95fa7)|2015-07-28 01:58:07
|442|jonasfj|Merge pull request #44 from djmitche/bug1184272  Bug 1184272: specify all API scopes as [[str]]|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4fa6d7903cfc45d36bf59d94e60690d537cb14b4)|2015-07-24 18:39:22
|441|djmitche|Bug 1184272: specify all API scopes as [[str]]|[URL](https://github.com/taskcluster/taskcluster-queue/commit/06e128ae0f1dcf116f22be565837cba1b75da845)|2015-07-24 18:24:46
|440|jonasfj|Merge pull request #43 from taskcluster/task-priority  Task priority|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d42b48fe8b980c2eaebf24538fa87f60e32767e6)|2015-07-23 20:37:15
|439|jonasfj|Fixed spelling issues|[URL](https://github.com/taskcluster/taskcluster-queue/commit/417b3b2370bc2b512e992abd726f308b39250351)|2015-07-23 20:36:50
|438|jonasfj|Ensured correct order and add tests for priority|[URL](https://github.com/taskcluster/taskcluster-queue/commit/95fa8c049bd99f16366910a73d5a993df3ea9f2d)|2015-07-21 21:29:21
|437|jonasfj|Merge branch 'master' into task-priority|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0f8eba07d2bf4c768e0c8d24decf11ecd671853c)|2015-07-21 20:25:24
|436|jonasfj|Add job for expireQueues|[URL](https://github.com/taskcluster/taskcluster-queue/commit/425f8e77377c689998ec97500943d7e8147989d3)|2015-07-21 19:56:47
|435|jonasfj|Initial support for task.priority|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1fd98d2225d3b1acecf70bd98e7830ed16b742df)|2015-07-21 19:40:20
|434|jonasfj|Merge pull request #42 from taskcluster/remove-legacy-queues  Removed legacy queue creation|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b9e62a6a0eaf2fe2a844f8d5e4c9a45fc5d331cd)|2015-07-21 18:54:08
|433|jonasfj|Removed legacy queue creation|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3b75c93f922b652c6c5fa399da59e14652e72c58)|2015-07-20 23:07:00
|432|jonasfj|Adressed comments|[URL](https://github.com/taskcluster/taskcluster-queue/commit/50dab93f468d18235033f0e94dfffb4b7feef80d)|2015-06-09 21:34:49
|431|jonasfj|Added tests and binary for expiring queues|[URL](https://github.com/taskcluster/taskcluster-queue/commit/443044d7e4544a0c8de4f945c1f177ad033a0a5b)|2015-06-06 01:42:29
|430|jonasfj|Testing GC'ing and legacy queues|[URL](https://github.com/taskcluster/taskcluster-queue/commit/dee1c76cb7a8ae7128635de58fdd792473692aad)|2015-06-06 01:24:24
|429|jonasfj|Fixed existing tests|[URL](https://github.com/taskcluster/taskcluster-queue/commit/153373186eacdcd7482044bf8db9744acd8f2cde)|2015-06-06 00:56:24
|428|jonasfj|Merge branch 'master' into fix-queue-collisions|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6bf8abccc21b95f1fb2c3f65af1ea5767d7bfdce)|2015-06-05 22:25:19
|427|jonasfj|Merge pull request #40 from taskcluster/refactor-tests-to-use-assume  Refactor test to use assume|[URL](https://github.com/taskcluster/taskcluster-queue/commit/55b67b950e1af29bfac18a5a141c91ca36ad7da1)|2015-06-05 22:24:45
|426|jonasfj|Timeout of queues|[URL](https://github.com/taskcluster/taskcluster-queue/commit/bf6cbbd292ce2f1b0c43776499b369c35b2322bc)|2015-06-05 22:21:32
|425|jonasfj|New queue naming and meta-data|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e5763ffb4ce435e0da936beb1e2136b84240fe60)|2015-06-04 16:37:25
|424|jonasfj|Refactor test to use assuem|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1eeb877e98d4434d9460439c8a4117d69ba31076)|2015-05-28 21:18:32
|423|jonasfj|Merge pull request #39 from taskcluster/bug-1148860  Allow artifact creation past resolution as exception|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a51f68aae994d7d13b7e55b524b99b3fc17cf645)|2015-05-27 16:34:04
|422|jonasfj|Better error message|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a453d1033c7ce6f3f042bf6de060387be1a43097)|2015-05-27 16:33:46
|421|jonasfj|Allow artifact creation past resolution as exception|[URL](https://github.com/taskcluster/taskcluster-queue/commit/359fe83c666bdd130412361e4e0fcbd2f726fe1a)|2015-05-26 23:42:25
|420|jonasfj|Merge pull request #37 from taskcluster/fast-azure-storage  Fast azure storage|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e4eec406982dfcbef93157087ab588187448d2a2)|2015-05-19 23:01:53
|419|petemoore|Merge pull request #38 from taskcluster/reason-created-exception|[URL](https://github.com/taskcluster/taskcluster-queue/commit/30c52cb88fa7fb8743a4ec42057503f285f08d4e)|2015-05-19 18:12:17
|418|jonasfj|Use  for exception run|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2d2f83ed82b01bd080ae10d89e7dbc0009d8422b)|2015-05-17 20:21:16
|417|jonasfj|Remove node 0.10|[URL](https://github.com/taskcluster/taskcluster-queue/commit/31833440ab43ab3ddf348dfb543c035a994c7669)|2015-05-15 17:02:23
|416|jonasfj|Updated reference to taskcluster-base|[URL](https://github.com/taskcluster/taskcluster-queue/commit/bf7a8bce1bb00261e7e4d35e5ebf91922dea6cf6)|2015-05-14 21:14:46
|415|jonasfj|Cleanup queue service|[URL](https://github.com/taskcluster/taskcluster-queue/commit/52e71c733cd0b617194cb255185b104f61179edb)|2015-05-14 20:55:12
|414|jonasfj|Ported queueserivce.js to fast-azure-storage|[URL](https://github.com/taskcluster/taskcluster-queue/commit/50d4be04ebb415820cc820448909905ca4c3bf43)|2015-05-13 22:42:26
|413|jonasfj|Try out fast-azure-storage backed base.Entity|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e13dab4262861eae6e5f1282674ea2b76c670ed4)|2015-05-13 22:00:41
|412|jonasfj|Ignore MessageNotFound|[URL](https://github.com/taskcluster/taskcluster-queue/commit/480186d7bec8d8a7975065418fc2cdeb7712b324)|2015-05-11 20:03:08
|411|lightsofapollo|Revert "Disable proxy in us-east-1 for artifact download failures"  This reverts commit 07529fcef486d728c98df9c329cff038164b3b01.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/75c4670b64f6b68f1b0eb633ae66a703370c9217)|2015-05-06 22:10:42
|410|lightsofapollo|Disable proxy in us-east-1 for artifact download failures|[URL](https://github.com/taskcluster/taskcluster-queue/commit/07529fcef486d728c98df9c329cff038164b3b01)|2015-05-06 16:50:38
|409|lightsofapollo|configure new s3-copy-proxies|[URL](https://github.com/taskcluster/taskcluster-queue/commit/8a3a3f21eb88a430bdac85cdf303b3a72c3087d6)|2015-05-04 05:48:35
|408|lightsofapollo|Merge pull request #36 from taskcluster/proxy-through-nginx  Add support for proxing for EC2 regions, and prod config|[URL](https://github.com/taskcluster/taskcluster-queue/commit/af4b90c47ee1bd6de21ee39e37fac6292672cb9c)|2015-05-04 05:38:33
|407|jonasfj|Added option to disable proxy redirect thing|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3505e372611532249a866b9779b1579752fc6617)|2015-05-01 04:30:56
|406|jonasfj|Add support for proxing for EC2 regions, and prod config|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d3bc66d6e998d45490746ede10f1500c47b4fedd)|2015-05-01 03:40:28
|405|petemoore|Resolved merge conflict|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4587825ebdcd99dcbe2b9f470bcaeb2294825065)|2015-04-23 12:26:48
|404|jonasfj|Minor optimizations reusing status object|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6afb28c7b5fbbcdac198eb041187c9ee89f6a785)|2015-04-10 20:14:27
|403|jonasfj|Merge pull request #35 from taskcluster/fix-node-0.12  Fix node 0.12|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4d24c25055fe30f26a93f6e3ad2a5c9a6e179ea1)|2015-04-10 17:58:10
|402|jonasfj|Minor improvments, and new taskcluster-base|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1165ed15fa2024c3cac83666f651c460f3864be3)|2015-04-10 17:51:43
|401|jonasfj|Comment and test fix|[URL](https://github.com/taskcluster/taskcluster-queue/commit/abe62a34668e8fc7eee52893c56aa573f40f4c31)|2015-04-10 16:37:57
|400|jonasfj|Cleanup from hacks|[URL](https://github.com/taskcluster/taskcluster-queue/commit/828abc22c72c21c79c8579389655af6addce5a5b)|2015-04-10 05:21:32
|399|jonasfj|More load-test hacks|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7ce0f0aeb936268ba46c24e42876b8f51a4b0cac)|2015-04-07 20:28:14
|398|jonasfj|More load-test hacks|[URL](https://github.com/taskcluster/taskcluster-queue/commit/53474e14cb4304f55ff88de18c960e3c42c2fd89)|2015-04-07 19:17:47
|397|jonasfj|Fix load-testing utility|[URL](https://github.com/taskcluster/taskcluster-queue/commit/108ccd4b888e7e24d409b150fa158ab750e9213d)|2015-04-07 05:17:50
|396|jonasfj|Added load-testing utility|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5e803665a34f154269e75a73f98db6c11a806ab4)|2015-04-07 05:14:54
|395|jonasfj|Config for load-testing|[URL](https://github.com/taskcluster/taskcluster-queue/commit/341f6f3ec1d71409a8916f9eac618da7055dd6df)|2015-04-07 04:37:05
|394|jonasfj|Finished upgrade to 0.12, + lots of packages upgraded|[URL](https://github.com/taskcluster/taskcluster-queue/commit/16584f4e0b92134978b4976e5ffd2e03ddd744e5)|2015-04-07 04:08:38
|393|jonasfj|Queue service hacks...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0454b966851ddc3e6e6417e3fa82e41b90b07f61)|2015-04-03 22:00:37
|392|jonasfj|Ignore message not found errors|[URL](https://github.com/taskcluster/taskcluster-queue/commit/43a7a6b8db04343c79bcd05529078feabbd21a19)|2015-03-25 17:22:30
|391|jonasfj|Update dependencies and make tests work under node 0.12, after http.Agent with keep-alive|[URL](https://github.com/taskcluster/taskcluster-queue/commit/aae28c413675b70b301f88d83ba3774f8a56d964)|2015-03-24 20:03:12
|390|jonasfj|Upgraded taskcluster-base which now disables nagle for azure table storage|[URL](https://github.com/taskcluster/taskcluster-queue/commit/fe2868a2eb78a762e8a7a70d6ed04831d24457ac)|2015-03-21 22:32:43
|389|jonasfj|Ensure dates use javascript toJSON date-format before comparing for idempotent operations|[URL](https://github.com/taskcluster/taskcluster-queue/commit/04fc1f0c15f548e2cbe45cb3c77a6cf410cc7dcb)|2015-03-21 18:36:50
|388|jonasfj|Fix issue when claim-expires before deadline-exceeded message is handled -- strictly minor internal issue|[URL](https://github.com/taskcluster/taskcluster-queue/commit/80cc815edbef0595a377dba7daee9a0d01cffb93)|2015-03-21 17:50:51
|387|jonasfj|Upgrade base|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d471640043b196d8149a03c0578e7e35c404a000)|2015-03-21 00:33:07
|386|jonasfj|Updated to report stats about base.Entity use|[URL](https://github.com/taskcluster/taskcluster-queue/commit/000aa891667f207f28b513cede8ecc0e2ee0dadc)|2015-03-20 22:35:18
|385|jonasfj|Reporting stats from azure table operations|[URL](https://github.com/taskcluster/taskcluster-queue/commit/cfb070606e545b8d5e3411450ad6058b30811b06)|2015-03-20 22:24:52
|384|jonasfj|Removed bad entries from claim-request and updated base|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4ce57e06e8986aaa95f9432ccd67088d7888c24b)|2015-03-20 21:27:22
|383|jonasfj|Fewer connections|[URL](https://github.com/taskcluster/taskcluster-queue/commit/783ba270bbcd431c66cb987d84c7daed1174898a)|2015-03-20 19:04:35
|382|jonasfj|Wrong runId for azure queue in claimresolver|[URL](https://github.com/taskcluster/taskcluster-queue/commit/57c59128d571aad888e37259cbd10064ad3ac9a9)|2015-03-19 19:34:21
|381|jonasfj|Debug some more|[URL](https://github.com/taskcluster/taskcluster-queue/commit/be0da56f12cd9c3465dd0807c556a04e23721245)|2015-03-19 07:11:36
|380|jonasfj|Fix issue with worker-shutdown|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4f744e94d1cb8a6c474e8f1479ac6d6475ec8faf)|2015-03-19 06:37:31
|379|jonasfj|Downgraded node|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2d942036cec1bafe32c85abf59f90c531ef23eba)|2015-03-19 05:59:59
|378|jonasfj|Updated procfile|[URL](https://github.com/taskcluster/taskcluster-queue/commit/55e16f5b49facd3b63b35d335f43943b0d81bc89)|2015-03-19 05:16:37
|377|jonasfj|Reducing parallelism for reapers|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d3b50c960ca3bf6a75c4f20556cf9b01327511c1)|2015-03-19 05:01:33
|376|jonasfj|Shrinkwrap updated|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d7da00dde506fbfadb218305f1ac95b4ec48192f)|2015-03-19 04:31:13
|375|jonasfj|Fixed wrong config|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d9e79fc41ee93b101faae5f0a002504d6478a4f3)|2015-03-19 04:25:28
|374|jonasfj|Uploaded to wrong bucket|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3f4bf8658494b8c2019ba729e0c6fba2ba14de70)|2015-03-19 04:23:29
|373|jonasfj|Fixed GET cors issues when no cors present|[URL](https://github.com/taskcluster/taskcluster-queue/commit/365981a7787d14a77a9cd636acee0da9969c59e3)|2015-03-19 04:03:39
|372|jonasfj|Labeled azure artifact experimental, for now at least -- we use S3 everywhere anyways...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/74b5e59c750938a7f1357d71b45ce2eb6a505466)|2015-03-19 03:33:42
|371|jonasfj|new taskcluster-base and more robust test - yes I just upped the time delay|[URL](https://github.com/taskcluster/taskcluster-queue/commit/fbe86e08079d6a68a9d0042a2bfe59fbf630abb0)|2015-03-18 17:59:04
|370|jonasfj|Minor clean up more docs|[URL](https://github.com/taskcluster/taskcluster-queue/commit/18aff3d439158018e772f3d1595afc8f131950ae)|2015-03-18 17:33:49
|369|jonasfj|Removed signature secret|[URL](https://github.com/taskcluster/taskcluster-queue/commit/39630fad65348194b38d040a6dcd0baae122fb7b)|2015-03-18 17:21:41
|368|jonasfj|Added shrinkwrap back|[URL](https://github.com/taskcluster/taskcluster-queue/commit/18bfe8b561b000b884482693a897c01bd4aae6ad)|2015-03-18 17:11:44
|367|jonasfj|Fixed taskcluster.utils.fromNow|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4aeeae52feda6021b088c7975651ecdbda7886d5)|2015-03-18 17:09:13
|366|jonasfj|Updated to babel and new taskcluster-client|[URL](https://github.com/taskcluster/taskcluster-queue/commit/17134d7041e9475ef5678ba9cd6765f21e2e06c3)|2015-03-18 16:56:19
|365|jonasfj|Addressed review comments|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6a2254aac56e83296f6f8201794e4927130269ca)|2015-03-18 16:51:40
|364|jonasfj|Updated localhost to make it not interfere with test queues|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2a67606e1564c64818638e4aba313a89ae540dc8)|2015-02-26 21:03:57
|363|jonasfj|Comments clearifying some of garndt comments|[URL](https://github.com/taskcluster/taskcluster-queue/commit/25ab042e16aaef9d23f729016d6bb2409764424f)|2015-02-25 17:05:53
|362|jonasfj|Removed xmljs from dependencies, to only be a dev dependency|[URL](https://github.com/taskcluster/taskcluster-queue/commit/650e6c3d3b179e83877b1bfa1299a370fa9a8a87)|2015-02-20 07:31:04
|361|jonasfj|Use different tablename in testing, so old entries with old base.Entity doesn't break us|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0d54f6742a15e599b5f3a4c8e5d2bbee65e343a9)|2015-02-20 01:48:42
|360|jonasfj|More test for querytasks|[URL](https://github.com/taskcluster/taskcluster-queue/commit/dc5c881728b9a8a1a954a0db6ce328f34c14b2f6)|2015-02-20 01:27:05
|359|jonasfj|Ensured that all schema references ends with #|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4a9f08c910a57c04d61e48301860a615d1743e1d)|2015-02-20 01:20:10
|358|jonasfj|Fix claimtask test, compare timestamps in a robust manner|[URL](https://github.com/taskcluster/taskcluster-queue/commit/cdbe0b8323e2c134036585419aa2163adb514d61)|2015-02-13 07:42:30
|357|jonasfj|Start processes from npm, to ensure that we launch with 6to5-node|[URL](https://github.com/taskcluster/taskcluster-queue/commit/02c882f6c090a566c725acf14865872aa7eb415b)|2015-02-13 07:34:05
|356|jonasfj|Fixed tests on travis - I hope|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c873b70a45c801a6446f5e5d2d39830e2d051650)|2015-02-13 06:43:11
|355|jonasfj|Updated .travis to remove 6to5 from DEBUG and test with node 0.12|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4c00251ac766e7e5cdf8e85e031493196a16b5da)|2015-02-13 02:11:58
|354|jonasfj|Added expire-tasks and abused global state to restart server less often, leading to faster tests|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d1b0bab2868b3fc5e93944479d23f806c6bcc9ff)|2015-02-13 02:08:03
|353|jonasfj|Implement deadline test and improved error handling a bit|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f4bb1abdf7107093f9ad6a1c80e01498d609ae5d)|2015-02-12 21:52:24
|352|jonasfj|claim-reaper, deadline-reaper done, retry_tests for claim-reaper|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c11d4d7e72e61c2548dea6395c3adda1bc533b82)|2015-02-12 01:10:44
|351|jonasfj|claim and deadline resolver... still need the bin/ files... but the code is there|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a5560ac90f024cd02c4ae5496abbec420a0d8b1f)|2015-02-11 07:13:52
|350|jonasfj|Artifact and reportCompleted tests done|[URL](https://github.com/taskcluster/taskcluster-queue/commit/113cee26c86322094afbd7df455f4e8a3321944b)|2015-02-10 21:48:35
|349|jonasfj|Fixed a lot of tests... still quite a few to go..|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3ed7074cbcfd8e9c48b94102aaa251563a8ac283)|2015-02-10 02:07:00
|348|jonasfj|Finished up most of the artifact API end-points, needs testing still|[URL](https://github.com/taskcluster/taskcluster-queue/commit/41783c192bc40a3f0989721f6e0baf725d31b272)|2015-02-09 19:27:13
|347|jonasfj|Fixed issue so we only retry on reportException with reason = worker-shutdown|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9d29e5c61a560ff4709073461e972608e3c760db)|2015-02-07 21:48:17
|346|jonasfj|Ensure that we can't have more than 50 runs...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7ce51a56e543062ef6b093c973671dbbe2298aee)|2015-02-06 23:58:40
|345|jonasfj|Only missing reapers and artifact API...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f9d99ee656df7adbdddab0a6a92c93a972f5034a)|2015-02-06 23:47:09
|344|jonasfj|cancelTask added, and the get poll urls... next up claimTask|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7857d22df7c986823754d5c46acb2db93b041a42)|2015-02-06 07:22:03
|343|jonasfj|Fixed queue service how it needs to be for implementation strategy B, well I think it's right this time|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a939f2e03c418f571e0221aa7d21c318ef288a87)|2015-02-06 06:40:00
|342|jonasfj|More work on invariants necessary for consistency|[URL](https://github.com/taskcluster/taskcluster-queue/commit/63ad313a1ae34b73934a4ed2f112f4d36f35ea7a)|2015-02-04 19:12:52
|341|jonasfj|queueservice_test now passes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c6dd71cba6ecc85874cf4b80f6d2ca897ff94032)|2015-02-03 20:58:34
|340|petemoore|Added # to schema names|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5ff59b67fe01cf466faba2409f5133450e0bae91)|2015-02-03 16:21:58
|339|petemoore|Corrected schema name and added "type" declaration for an object definition|[URL](https://github.com/taskcluster/taskcluster-queue/commit/afb497cd6486c2e4c8bae0b8f0a2550f363b50f1)|2015-02-03 16:14:05
|338|jonasfj|Got server running again...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e21435a2725cf5bb2b616b1884e8c82d055f4002)|2015-01-31 20:27:57
|337|jonasfj|Lots of progress... nothings works, but abstractions are really good now|[URL](https://github.com/taskcluster/taskcluster-queue/commit/29215106e5a3aad941c4d1272a963e077c1d0b53)|2015-01-31 02:29:44
|336|jonasfj|Got tests running with 6to5, I   LOVE   await :)|[URL](https://github.com/taskcluster/taskcluster-queue/commit/01e5ae5c244d775c03484c970dd879e6a455e847)|2015-01-30 20:46:52
|335|jonasfj|Simple ping test runs...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3f4f91b0e5bb98745fcc65c342ff5263fb51a7f2)|2015-01-30 19:36:42
|334|jonasfj|Reasonably happy with artifact design...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5b551622182adf65893ae8d59e4a80f2ad94f3c9)|2015-01-30 17:41:43
|333|jonasfj|Upgraded aws-sdk|[URL](https://github.com/taskcluster/taskcluster-queue/commit/982d6566f18147fbb3e45bf9ecbedbc1666a0e74)|2015-01-29 19:16:29
|332|jonasfj|Removed files and config that must die... updated dependencies, expects nothing to work...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/539da233deaa977e2ab0d06719ce43c92041ac47)|2015-01-29 19:04:59
|331|jonasfj|Added config loaders for azure credentials to reaper|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0d46f4490e2b50a65fd4262edf2e7088ad975394)|2015-01-28 20:27:36
|330|lightsofapollo|hotfix update shrinkwrap|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6e36497ee70658526893c434923ef18b8548a80d)|2015-01-28 16:26:51
|329|lightsofapollo|fix missing package|[URL](https://github.com/taskcluster/taskcluster-queue/commit/bc706597781702ea8c6ab45762f4873389141e7a)|2015-01-28 16:24:47
|328|jonasfj|Don't load xml2js in production|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ca7483c1611157dd1da4d559fbc23d5c05d4654c)|2015-01-28 01:57:12
|327|jonasfj|clean up for diff for the PR, just a bit|[URL](https://github.com/taskcluster/taskcluster-queue/commit/adbc13ed88d50042f64fd71684b4116d0ab98866)|2015-01-23 23:17:55
|326|jonasfj|Fixed tests and got it running again...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1b591a0d03cab96c8b1c9a6ece353e37d44563d9)|2015-01-23 23:07:03
|325|jonasfj|updated npm shrinkwrap|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0962c156b9e91e74c671690e60060b0f6f3e5bd6)|2015-01-23 20:10:36
|324|jonasfj|Refactored to match draft from docs site...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/eaf0387a52cd0c6585da61e2997b137d0bb66fde)|2015-01-23 03:05:57
|323|jonasfj|Rework to my new polling model...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/87f40c23a4b7667530045e4d9d75038c99e0c348)|2015-01-20 23:24:44
|322|jonasfj|Access task test works|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9beb77a5dafa047675e452b5041cb903b92d2b30)|2015-01-20 19:34:48
|321|jonasfj|Added option to use azure queue storage for getting pending tasks to workers|[URL](https://github.com/taskcluster/taskcluster-queue/commit/888f9df790b1f58897242ebde06f4dac5ce41abd)|2015-01-17 21:03:36
|320|jonasfj|Added schema for access-tasks API end-point|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9ebe3bf60e180ba4df101ee0e67026903814e1f1)|2015-01-17 02:27:59
|319|jonasfj|Added API end-points and started putting messages into azure queue storage queues|[URL](https://github.com/taskcluster/taskcluster-queue/commit/161d4cf86a7eea12919ef7cfb9d994d2ee279540)|2015-01-17 02:07:42
|318|jonasfj|Use absolute Date for ttl, this makes deadline easier to implement...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2058fee38af6369e7e699fa23f99b38cf7e20cb7)|2015-01-17 00:17:30
|317|jonasfj|Got SAS test with azure queue storage working|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ce7112c2ccde7dff8018c2097ba5cc43ea696c88)|2015-01-17 00:07:37
|316|jonasfj|Started work on a azure queue storage wrapper|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c00a3c1197d936cd0b918aebbfca63de3689b593)|2015-01-16 00:59:18
|315|jonasfj|Upgraded package versions|[URL](https://github.com/taskcluster/taskcluster-queue/commit/faacb3dd392a78c01cfaf3fbb8ed6df8d8c6452e)|2015-01-15 23:37:44
|314|jonasfj|Merge pull request #28 from taskcluster/pending-task-count  Added end-point to get summary of pending task, for various workerTypes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/23c32841d493c3ada0f646778a34637c9b238757)|2015-01-15 01:10:27
|313|jonasfj|Updated config|[URL](https://github.com/taskcluster/taskcluster-queue/commit/fa4c1070b86ce3f23edf60460fd4476c9e287fc3)|2015-01-14 23:44:45
|312|jonasfj|new config file|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d80ca68b41a83785cc9efe651c2fd836f847f062)|2015-01-14 23:29:10
|311|jonasfj|Added end-point to get summary of pending task, for various workerTypes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/883f27f132269d0c6aa6e39e2485fec011fc88d0)|2015-01-14 01:57:49
|310|jonasfj|Modified npm shrinkwrap|[URL](https://github.com/taskcluster/taskcluster-queue/commit/769d07ffdd7028d74654d770ad2bb52c7d40f48b)|2014-12-11 23:19:21
|309|jonasfj|Added config file for localhost|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c1efa0b37b75f964e50961e6039ce2e3490f432c)|2014-12-11 02:55:05
|308|jonasfj|Fixed doc string error|[URL](https://github.com/taskcluster/taskcluster-queue/commit/144628e91b0e49e7459b7ad066bb3d379db3aaa1)|2014-12-10 02:24:08
|307|jonasfj|Split task-completed into task-completed|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e7f4a39eb1b6919fc174a4bdf367a65065f47a55)|2014-12-09 23:53:47
|306|lightsofapollo|Merge pull request #25 from lightsofapollo/tc-base  tc base v0.6.1|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a13dad177a45dd63219823877bdcbc271b4e7b48)|2014-11-25 03:18:32
|305|lightsofapollo|tc base v0.6.1|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e17a66eb81d786a7356d997c46ecef08bde1f586)|2014-11-25 03:05:26
|304|jonasfj|Fix for issue where we return 500 instead of 409 for defineTask when taskId is already in use...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/cf3119a296db9e54f9ddceb0f1512b5cecde3ba0)|2014-10-27 23:02:03
|303|jonasfj|ported to pulse|[URL](https://github.com/taskcluster/taskcluster-queue/commit/bf66feeed2b95b6c4e98e980341c15e24d6e36da)|2014-10-17 21:34:53
|302|jonasfj|Updated dev dependency, with tc-client with retries to see if it fixes tests|[URL](https://github.com/taskcluster/taskcluster-queue/commit/bbfac91c24b4ef8dd09af1bba10e575e3524ac29)|2014-10-10 04:56:39
|301|jonasfj|More error logging and longer timeouts|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4ac5dc9aed6fe166e9e2e6fcd0e291218fe01ad2)|2014-10-09 20:28:56
|300|jonasfj|Apply exponential retry filter to azure blob storage client|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5f03fa64f71a06eb975999f961551c944d7334b2)|2014-10-09 20:11:10
|299|jonasfj|Additional error messages|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d1a3bd121f64e58eaa8eb85b765fa9e513f627e6)|2014-10-09 19:53:38
|298|jonasfj|Fixed race condition in listenFor|[URL](https://github.com/taskcluster/taskcluster-queue/commit/cefeddcb179455b73f5407bb4ab60733c9239434)|2014-10-09 19:22:14
|297|jonasfj|Removed superagent dependency and proper travis deployment strategy|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e1016ada57c51776274b26c322013d02619f5299)|2014-10-09 18:53:34
|296|jonasfj|Upgraded taskcluster-base and client|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e78e2873e48ca872f3f0a36e56f897b32c0f22a6)|2014-10-09 00:06:19
|295|jonasfj|Upgraded knex|[URL](https://github.com/taskcluster/taskcluster-queue/commit/29cbd9d6e453f910a2a972842771fba5fd0ccace)|2014-10-03 01:11:18
|294|jonasfj|Added note to when we handle insertion errors for artifact creation|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7f7fb0069737c279a63fab58eaed2ff8eed46494)|2014-10-03 00:44:57
|293|jonasfj|Added npm-shrinkwrap|[URL](https://github.com/taskcluster/taskcluster-queue/commit/efd5fae549b2b73f26e5474335f1c75bb1e847ee)|2014-09-29 22:08:51
|292|jonasfj|Removed node_modules|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e059d34a0f99d58e24e7e7b6ce19b9674c8af57b)|2014-09-29 22:07:45
|291|jonasfj|Updated config for travis with new influxdb|[URL](https://github.com/taskcluster/taskcluster-queue/commit/599358c9d98bee4a2e85a12c381b794a50ef1389)|2014-09-26 19:05:10
|290|jonasfj|Adopted code the new Promise and added influxdb reporting exchanges|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9dc7f3d37f930df481c48882068f4bd63436358d)|2014-09-16 01:08:59
|289|jonasfj|Updated node_modules|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ae0afc55a8afe67cb161f61b9b1713eb4d3b3539)|2014-09-16 00:54:19
|288|jonasfj|Updated node_modules|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b3de19be659951d9486f29c4bc930e5291d6af9b)|2014-09-16 00:30:51
|287|jonasfj|Refactor config to let DATABASE_URL override database_url|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a1658b7c0a4a44a93598043e12cfd95d865a2bcf)|2014-09-11 19:35:42
|286|jonasfj|Removing task.priority and improved reaper tests|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0407246ff691453ef9ab29136cba90b75d21472b)|2014-09-11 18:49:24
|285|jonasfj|Added CORS setup for S3, fixing bug 1063337|[URL](https://github.com/taskcluster/taskcluster-queue/commit/28bf28b3140605a1288d0a9245b995997665f295)|2014-09-11 00:51:57
|284|jonasfj|documentation for getArtifact|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f90243d5ee2f4f6eb6ed00d12ed906f2a5c590b6)|2014-09-11 00:41:24
|283|lightsofapollo|terrible bandaid|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ae0973c90ae6608e2ef155b947f2cb1023715869)|2014-09-05 23:20:20
|282|jonasfj|Give tests more time|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f0f7328401ad9a5872c17d71cf28c0ba88ed4074)|2014-09-04 23:22:45
|281|jonasfj|Added all required encrypted config in encrypted file|[URL](https://github.com/taskcluster/taskcluster-queue/commit/db5557745e0322271f98c4e0dfdebdb4c4cfaf59)|2014-09-04 23:11:27
|280|jonasfj|Upgraded taskcluster-base|[URL](https://github.com/taskcluster/taskcluster-queue/commit/53e0101a03021fb96efe0536e292dc4b6c8ef91f)|2014-09-04 00:44:17
|279|jonasfj|Added process monitoring|[URL](https://github.com/taskcluster/taskcluster-queue/commit/fcec5b0f1c417c8fc0ec7fd179564af381470140)|2014-09-04 00:27:33
|278|jonasfj|Merge pull request #23 from taskcluster/add-extra-data  Added 'extra' field for extra data|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ae77890e08ec91a916fe787365c142d302f465a7)|2014-09-03 18:31:25
|277|jonasfj|Added 'extra' field for extra data|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7f31beb18f7572c05de20da912114381c5593220)|2014-09-03 07:25:27
|276|jonasfj|fix bug 1055847|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2323038b4679d9e8bc1208df7089388fec157009)|2014-09-01 18:36:48
|275|jonasfj|Added statistics|[URL](https://github.com/taskcluster/taskcluster-queue/commit/bd4abbd0513d54becd288d948f808cc5992ea094)|2014-08-24 06:21:26
|274|jonasfj|Update dependencies again|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d97191ac5cc8d4f1a977eb25034fceb959729671)|2014-08-24 06:00:35
|273|jonasfj|Updated dependencies|[URL](https://github.com/taskcluster/taskcluster-queue/commit/13f75b464d5e70b0663ddabcc827401b1f3c7902)|2014-08-24 05:59:39
|272|jonasfj|Minor documentation fix for exchanges|[URL](https://github.com/taskcluster/taskcluster-queue/commit/becf10fda5d63176c5486e6d6c6af3d51fd88f7e)|2014-08-20 19:12:54
|271|jonasfj|More docs, schemas and artifact-created exchange|[URL](https://github.com/taskcluster/taskcluster-queue/commit/fa9f765f198b90fc7ad3cc7c7edfd3d8903acb27)|2014-08-20 18:47:05
|270|jonasfj|Added documentation for createArtifact method|[URL](https://github.com/taskcluster/taskcluster-queue/commit/015ee19d1f5bba5b2a712b8c935543344610e591)|2014-08-19 23:49:49
|269|jonasfj|Updated taskcluster-base|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5726d5a827adb0c6e2c94a30a56da4da1b6d9e3e)|2014-08-19 21:11:06
|268|jonasfj|Upgraded taskcluster-base to fix CORS issue|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b3161e998090a331b2ab909b1af264a9724f942c)|2014-08-19 21:03:51
|267|jonasfj|Updated taskcluster-base with caching|[URL](https://github.com/taskcluster/taskcluster-queue/commit/596a15e170f2420a538bd9748fbcc07d4c244304)|2014-08-19 00:49:09
|266|jonasfj|New taskcluster-base and client... with some smart defaults|[URL](https://github.com/taskcluster/taskcluster-queue/commit/62ac59cec7a58899b36f5168ac8d6327050e1b52)|2014-08-19 00:48:17
|265|jonasfj|Updated taskcluster-base|[URL](https://github.com/taskcluster/taskcluster-queue/commit/41123dbcf5678f491be913d2e4931f65d3a82557)|2014-08-16 02:49:39
|264|jonasfj|Fixed deadline expiration of task that are pending.. and added tests|[URL](https://github.com/taskcluster/taskcluster-queue/commit/174c5419e554102a462c0c723af46e804b1fe3fe)|2014-08-15 19:03:49
|263|jonasfj|Minor docs fixes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ebbb6e3d25dc556d6cf72070a9fda4aa0a2af812)|2014-08-14 23:29:42
|262|jonasfj|Fixed last bugs in rethink of routes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e2674388ba432732e948e4fdb0cda270cf000755)|2014-08-14 21:15:27
|261|jonasfj|Updated node modules|[URL](https://github.com/taskcluster/taskcluster-queue/commit/62bb33723c6e4aaaec6d8836a054e0557725d8bf)|2014-08-14 21:15:11
|260|jonasfj|Porting most things to new taskcluster-base, just need to test and fix bugs|[URL](https://github.com/taskcluster/taskcluster-queue/commit/cedca03c620a16cb218a35f8ed165c1270e01c93)|2014-08-14 17:17:37
|259|jonasfj|Fixed task-completed messages to report run as completed and not running... added test to catch this|[URL](https://github.com/taskcluster/taskcluster-queue/commit/fb04ea3b5146eb4a84060e80fb86692b8353372e)|2014-08-13 04:08:41
|258|jonasfj|Renamed a few methods|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6ba42000e8f14a261ad237bbfee1d41042c7cccf)|2014-08-12 21:25:02
|257|jonasfj|Update node_modules|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2a219021d2378d37ca4fe85537f101c58ce321ea)|2014-08-12 20:36:14
|256|jonasfj|Fixed sas|[URL](https://github.com/taskcluster/taskcluster-queue/commit/08a8d9caa7e06dd2c81f0c29ce0852b92584f486)|2014-08-11 22:29:49
|255|jonasfj|Got CORS definition working|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d54f83b79c6129847188e830b407bd652aaeb87b)|2014-08-11 21:48:05
|254|jonasfj|Ported code|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f34da923452220e63bab28b3fe576e62b091fcdb)|2014-08-11 21:41:46
|253|jonasfj|Moved from azure to azure-storage, newer lib with cors support|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c931e2bb5c321f72a372c45c4db819282535e43c)|2014-08-11 21:41:22
|252|jonasfj|Added CORS for azure blobstorage|[URL](https://github.com/taskcluster/taskcluster-queue/commit/48c2f38478ee0d138d2c99ea13b12fa4f223bf00)|2014-08-11 21:39:01
|251|jonasfj|Fixed provisioner interface|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0da78d0b26730cd585a4fb4a5d31827d97e9846f)|2014-08-10 18:57:41
|250|jonasfj|Ups ping returns 409|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4904e41d56c2605b34cdbd1f03a25e8f788d1e91)|2014-08-09 23:08:01
|249|jonasfj|fixed deprecation warnings|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7f2ac186bc24a6b961a7554b75457a3c960cb5e4)|2014-08-07 23:57:04
|248|jonasfj|Updated taskcluster-base|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d71be7fb47b76cec2a7cba8c668e4c9f1a581c73)|2014-08-07 23:21:34
|247|jonasfj|new node_modules|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e980b8836c487ea38a68a2a62e133a99f4b024e3)|2014-08-06 21:47:34
|246|jonasfj|new taskcluster-base version|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ba4d231d7d1a2b404778bfe196fb04e391a4ef94)|2014-08-06 21:47:10
|245|jonasfj|Added end-point for pinging the server|[URL](https://github.com/taskcluster/taskcluster-queue/commit/560ff13e308dbe52a5dd1a7ee1f7dfccd5ea6f2a)|2014-08-04 21:36:35
|244|jonasfj|Merge pull request #22 from taskcluster/rename-artifact-kind  Changed artifact kind to storageType|[URL](https://github.com/taskcluster/taskcluster-queue/commit/27df35f8278771b3eff2e58d6443e5cca19ecadd)|2014-08-04 21:27:39
|243|jonasfj|Fixed isNaN assertion|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2e8cf419b16c8aaf3c37d458ac0b1013445c4cd5)|2014-08-04 21:26:00
|242|jonasfj|Fixed missing assert|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f1f893b0117fbd23ba69c4338da1e4f0d3c6ce14)|2014-08-04 21:21:25
|241|jonasfj|Changed artifact kind to storageType|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2c5eb2dedcf91aabeac6d1b9ffa0ff9e20a09b79)|2014-08-04 21:11:52
|240|jonasfj|Updated expire artifacts to allow for me to delete all artifacts as needed in upgrade|[URL](https://github.com/taskcluster/taskcluster-queue/commit/23054e528672763dd487f88c5349e2b7acea2434)|2014-08-04 21:12:39
|239|jonasfj|Merge pull request #21 from taskcluster/task-defined-exchange  Task defined exchange|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5aa206dafe5601fdaad7edfd6abc75890f8bf18f)|2014-08-04 17:10:36
|238|jonasfj|Updated taskcluster-base|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c59c0ae9ded8daf3eaf7b4f3d61b092bfe99a3a1)|2014-08-03 03:57:27
|237|jonasfj|Add taskDefined exchange and used safer port numbers|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4ffd25310d03d8b0871c14962308cfea1f8c9ef8)|2014-08-03 01:46:00
|236|jonasfj|Added schedulerId|[URL](https://github.com/taskcluster/taskcluster-queue/commit/26adb70dfcf7f79fddb9f2ea62f2a6c4bdd463b8)|2014-08-03 00:43:21
|235|jonasfj|Upgraded taskclsuter-base|[URL](https://github.com/taskcluster/taskcluster-queue/commit/160fe03ddf051a1ae99776dba8a6d6398af20cc4)|2014-08-02 03:32:03
|234|jonasfj|Updated to latest taskcluster-client|[URL](https://github.com/taskcluster/taskcluster-queue/commit/fb3e84caf0afa892117f03c33c5287562dbdbf8f)|2014-08-02 00:47:05
|233|jonasfj|Updated taskcluster-base|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e273a9a3250c678dd4580b3132fa4e981f33cc28)|2014-08-02 00:31:42
|232|jonasfj|Updated taskcluster-base|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4c1aa3637d42085aff1a8f1c610ce9e4b58270d2)|2014-08-01 23:18:04
|231|jonasfj|Added another check to a test case|[URL](https://github.com/taskcluster/taskcluster-queue/commit/23592a092e4d1bc5c8309ffe44098935437a65c0)|2014-07-30 21:38:28
|230|jonasfj|Validate URL parameters for sanity and remove old getTask end-point|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ece952e2f62be783e94a1727243eac35d6515213)|2014-07-30 21:16:51
|229|jonasfj|Merge pull request #19 from lightsofapollo/normalize-sas-to-url  Normalize sas object to url|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c62e623a98e126453e6fd4374273471558d7551c)|2014-07-31 06:34:04
|228|lightsofapollo|Update negative tests for sas signing|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0562a2a87af662ffdcee204abf629ddf6f26d4ad)|2014-07-31 04:21:47
|227|lightsofapollo|Change azure artifacts to return putUrl (a write signed sas url)|[URL](https://github.com/taskcluster/taskcluster-queue/commit/bcf1bd1d3479fc26d7b73aa0a4258d5439c5f2d4)|2014-07-31 04:11:04
|226|jonasfj|More tests and a fix for poor scope parameterization|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6343a7652c0f6fd02b8e41747074ebeafa640ad3)|2014-07-30 20:07:45
|225|jonasfj|Upgraded taskcluster-client and moved it to development only|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2edc68f4f91d45ab3cdc50f23aa2348bd29fc1ae)|2014-07-30 18:26:38
|224|jonasfj|Fixed another scope parameterization issue|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5e8e6a6c2ccd586914180199bc6807a709bef6c5)|2014-07-30 02:55:34
|223|jonasfj|Upgraded node_modules|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5f7c7ece121d92518736fdb5b72ef9383673f623)|2014-07-30 02:39:59
|222|jonasfj|Upgraded packages|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5ab47ae12528d3689968f2c1334be124c00e1937)|2014-07-30 02:18:13
|221|jonasfj|Fixing another scope parameterization issue|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1abedbee708090d8435526c1fc188b04a12bd172)|2014-07-30 00:49:17
|220|jonasfj|Fixed issue with bad scope parameterization|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5413d710738402f5d25f3466f69fd164987f0ee7)|2014-07-30 00:47:32
|219|jonasfj|Quick fix for https authentication|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5bf79a49f95dc3c0fe13c478e2457643dd4cf214)|2014-07-29 22:05:56
|218|jonasfj|Removed version number from task exchange format, it's in /v1/task url anyways|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f3f6fca1998cb8e4fb0e1f56c5856a16dcd57765)|2014-07-29 17:40:52
|217|jonasfj|Merge pull request #18 from taskcluster/refactor-status-structure  Refactor status structure (okay, well the API too)|[URL](https://github.com/taskcluster/taskcluster-queue/commit/da73ae0072e01aeff80a832abdf3c44bfa750b57)|2014-07-24 23:16:25
|216|jonasfj|Updated readme and credentials for travis|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5b46e85721abd3730a76c7a207fb4eeb5e8965ca)|2014-07-24 23:08:43
|215|jonasfj|Added node_modules|[URL](https://github.com/taskcluster/taskcluster-queue/commit/18209b016cc1479e59791067a3449843b8db2fee)|2014-07-24 21:24:28
|214|jonasfj|Merged|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3d01502e2a29e5bcc468f4b7c156e38c3e9bc85c)|2014-07-24 21:24:11
|213|jonasfj|Updated README|[URL](https://github.com/taskcluster/taskcluster-queue/commit/62c879100c892f94bc03d219e255bbc3a029789b)|2014-07-24 21:20:04
|212|jonasfj|Renaming procs|[URL](https://github.com/taskcluster/taskcluster-queue/commit/53ca0df5cd28cc32ee50a273f787880bd125aa9d)|2014-07-24 21:07:22
|211|jonasfj|Renaming procs|[URL](https://github.com/taskcluster/taskcluster-queue/commit/de1cdf47433fa1140f63422d0df8b7277bbf2c64)|2014-07-24 21:06:18
|210|jonasfj|Removing dropdb from list of commands, it's too dangerous|[URL](https://github.com/taskcluster/taskcluster-queue/commit/24ef7f3afccb8ff6a287f82a881ac64c142aed4a)|2014-07-24 21:03:18
|209|jonasfj|Renamed worker process to reaper for consistency|[URL](https://github.com/taskcluster/taskcluster-queue/commit/992d97d3d6a9e34c7ed21e80ebc8cd867ec0024b)|2014-07-24 20:55:31
|208|jonasfj|Add utility to drop database|[URL](https://github.com/taskcluster/taskcluster-queue/commit/650c036326e0055371aa72196022d79978315c4a)|2014-07-24 20:50:52
|207|jonasfj|Added more envs for configure|[URL](https://github.com/taskcluster/taskcluster-queue/commit/df5daf69a1e9b6641c8f7762b149fc0305c75d5e)|2014-07-24 20:48:18
|206|jonasfj|Modified configs|[URL](https://github.com/taskcluster/taskcluster-queue/commit/603e3bd2e05c560827d163789f91358a74dcc995)|2014-07-24 20:41:12
|205|jonasfj|Install npm_modules|[URL](https://github.com/taskcluster/taskcluster-queue/commit/17172913da1ea0847055b3d8e2d1e553690ec941)|2014-07-24 20:25:33
|204|jonasfj|Removed unused dependency|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3d9a62f3366684321ed19c47baef0254cc888a09)|2014-07-24 18:25:36
|203|jonasfj|Adding getTask() how could I forget that, lol..|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3eca6d97930d33e81477ca1e6406ee76459c1041)|2014-07-24 00:39:11
|202|jonasfj|Removed files not needed and added auth to defineTask|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0e8545ec5f531c4219bfa8ae55c560aee4f9f0d1)|2014-07-23 22:59:24
|201|jonasfj|Adding old node modules to reduce diff|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7db75ec7aa4f68a97074702bf5f909becb5eebbd)|2014-07-23 22:05:34
|200|jonasfj|Use envs in tests (for travis support)|[URL](https://github.com/taskcluster/taskcluster-queue/commit/fb64baa841833ef5d109858e4705b72c4f9527a6)|2014-07-23 22:05:01
|199|jonasfj|Extended timeouts, hide a few uncessary thins from debug|[URL](https://github.com/taskcluster/taskcluster-queue/commit/bebe9d94536c27fa52773af39236358a9e461816)|2014-07-23 21:58:01
|198|jonasfj|Extended timeout for artifact tests, they do a lot|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e43f88366597f67f3aa95aa80f3369b44a5898ea)|2014-07-23 21:45:57
|197|jonasfj|Added secrets for travis|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0dc5d79843786aa645aeb6def91c3e2fa3d20f86)|2014-07-23 21:26:23
|196|jonasfj|Got all tests running|[URL](https://github.com/taskcluster/taskcluster-queue/commit/58ea030dd70e4bbb3d3b57c14bb7482a241a6d48)|2014-07-23 20:28:15
|195|jonasfj|Fixed and tests for expire artifacts|[URL](https://github.com/taskcluster/taskcluster-queue/commit/02a095fafd21c786881b210912fb24fd358a6d8b)|2014-07-23 19:35:06
|194|jonasfj|Added expire-artifacts.js|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6e693eebdd29e00f527c16281f1c5172b20b0de6)|2014-07-23 17:26:11
|193|jonasfj|Method to delete expired artifacts|[URL](https://github.com/taskcluster/taskcluster-queue/commit/05d067e6874ac6f4ecd120eb0bcc3279ed7b9609)|2014-07-23 17:07:25
|192|jonasfj|Added utility to retire old tasks|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b8dae5cf554fc764c84d52ddceeaa3c408d55d7b)|2014-07-23 00:10:25
|191|jonasfj|database query and test for query to move old tasks from database|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f30c4148c36eebef176ac4797b271279bd0e1f4b)|2014-07-22 23:57:05
|190|jonasfj|Added tests for reaper and got it running again...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1e895d1d93da7e75e48a0b1cdc9c395e8ce8a0d0)|2014-07-22 23:22:56
|189|jonasfj|Added queries for expiring tasks|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d963f43513f5efd5e7b0b49bbe3cad9fdeb3a4a3)|2014-07-22 21:35:14
|188|jonasfj|API end-points are working, now porting reaper|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0265a2409dbeaeb3dddcf59561c96059bb89a245)|2014-07-22 18:27:22
|187|jonasfj|Initial work, not done yet|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d27430699891c6cb2e4ef0472a567a41034a1640)|2014-07-17 20:29:15
|186|lightsofapollo|Always run all api tests|[URL](https://github.com/taskcluster/taskcluster-queue/commit/59d9770fc100f0a91b29bb59d36aa9d0ce6e5389)|2014-07-09 07:45:22
|185|lightsofapollo|Merge pull request #17 from taskcluster/get-task-endpoint  Get task endpoint|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f3b19b67886caa67fea2bbdc35c2a7c55436dd26)|2014-07-09 07:34:55
|184|lightsofapollo|get task endpoint|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a031d372758d634a2a0a9a1bdc0caa2e04bfb690)|2014-07-09 07:28:55
|183|lightsofapollo|correct port range for test|[URL](https://github.com/taskcluster/taskcluster-queue/commit/80dd03c87034a8e6b09162370a47b13f4b6f0cc1)|2014-07-09 07:27:14
|182|lightsofapollo|update node_modules|[URL](https://github.com/taskcluster/taskcluster-queue/commit/01b6fefcdbc1bcb6979db98d1e6a796807d27395)|2014-07-09 07:26:53
|181|jonasfj|Removed all node_modules|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b5f024fb64687bd467f8f1a3e699865168793e01)|2014-06-30 18:21:49
|180|jonasfj|Updated node_modules|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5ca670d9c975eb0c084cb5b8f45803d372599ec2)|2014-06-30 18:21:25
|179|jonasfj|Updated tests and change format for defineTasks to something more array based|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c3248a7b5ccfe56712e7f6aac0a50fa7366b4724)|2014-06-18 21:44:09
|178|jonasfj|Merge pull request #15 from lightsofapollo/only-pending  Only return pending items in pending-tasks|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6f58315db85fc9544d0a3e0a06258f85ebcccf5f)|2014-06-12 17:22:03
|177|lightsofapollo|Only return pending items in pending-tasks|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b6a28ba43fbf19d522166d3823f3aca25994129f)|2014-06-12 16:59:35
|176|jonasfj|Updated taskcluster-base to fixed version|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a63a83c7d465d416a293876b8f5ab19a8f2b2f2e)|2014-06-10 17:35:19
|175|jonasfj|Update taskcluster-base|[URL](https://github.com/taskcluster/taskcluster-queue/commit/eae7357114a0adab48b8a72efbc5c549ec0be43a)|2014-06-09 19:30:59
|174|jonasfj|Wrong config in server.js|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e13483ff10734060c3e1b70c3303c6e1c8c28dad)|2014-06-09 18:49:17
|173|jonasfj|Added pg.js for knex|[URL](https://github.com/taskcluster/taskcluster-queue/commit/aa0e7fc4e3f856f7ed57875bd6dcbad90144c554)|2014-06-09 18:45:04
|172|jonasfj|Update node_modules/|[URL](https://github.com/taskcluster/taskcluster-queue/commit/deb7180bd3b5243c1127ad7fa625d0f4618308a3)|2014-06-09 18:39:57
|171|jonasfj|Fix me not being able to write JSON|[URL](https://github.com/taskcluster/taskcluster-queue/commit/010e65d4cd152744a24d674057c601a93030de75)|2014-06-09 18:37:36
|170|jonasfj|Added new node_modules/|[URL](https://github.com/taskcluster/taskcluster-queue/commit/dc0af7090b38605217e82cdc2f9b26fefaaffb79)|2014-06-07 00:24:28
|169|jonasfj|Checked out node_modules from master, so as not to show changes in PR|[URL](https://github.com/taskcluster/taskcluster-queue/commit/bd43a3d9edbd44286b7e06741bec47b611ccd22a)|2014-06-05 23:22:39
|168|jonasfj|Create Task table before creating Runs table|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f64846cf921c6e769909681fdac8396ffe9c94a2)|2014-06-05 23:17:01
|167|jonasfj|Various tests fixed|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ac021c52f7c9c6ff3cc57b59207d9b59a1707029)|2014-06-05 22:47:42
|166|jonasfj|Fixed task storage tests|[URL](https://github.com/taskcluster/taskcluster-queue/commit/aab644d83159bd268882ca0e1772e1dfc8aee50c)|2014-06-05 02:42:25
|165|jonasfj|Removed localqueue as it's nolonger used, move to taskcluster-base|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3df213d4115d6e3785b27bab2f77d00d54bb1669)|2014-06-05 01:58:08
|164|jonasfj|Removed events testing, the publisher is now tested in taskcluster-base|[URL](https://github.com/taskcluster/taskcluster-queue/commit/96f8e05a09ab3e91b3727569c5de502d0fe6fb00)|2014-06-05 01:57:50
|163|jonasfj|All api tests are now ported|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e2d26b8de48d4274340adb04f4c3ad0dd7e22f74)|2014-06-05 01:55:09
|162|jonasfj|Got claim_timeouts working|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ccbb64ab6830690399733e4642716135ed306bc0)|2014-06-05 01:49:45
|161|jonasfj|Updated taskcluster-base|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c925eec3229922255088842a74c982fea0ca6e7c)|2014-06-05 01:49:34
|160|jonasfj|Update taskcluster-base|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ff2e8e292c811b188e86f4e9f3d73b2b0e544640)|2014-06-04 23:18:07
|159|jonasfj|Fixes of tests keeping db clean|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9786c62618a0c5115302f06faf91f3dbf923a0b9)|2014-06-04 23:17:39
|158|jonasfj|Final fixes for artifacts|[URL](https://github.com/taskcluster/taskcluster-queue/commit/cdfb3a1697adf5e62d4d71a5e09ee3beaf924edf)|2014-06-04 22:41:16
|157|jonasfj|Updated taskcluster-base|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f27897b938b3ee817017107b8f4cf488d73998f2)|2014-06-04 22:25:54
|156|jonasfj|Moved artifacts url post task tests|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c0fc8b22531d4b40c76f6fd84e9fcc8165436564)|2014-06-04 22:25:34
|155|jonasfj|New version of taskcluster base|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f854dba3d05fb26b2a2b1c00caf1b577e4221ad8)|2014-06-04 21:53:09
|154|jonasfj|Work to fix queue|[URL](https://github.com/taskcluster/taskcluster-queue/commit/af318feace247f2e6a992fba225e3105fbd6c77c)|2014-06-04 21:51:47
|153|jonasfj|fixed bin/reaper.js|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2e0849fa49a46f85931be7391ea5b30fb6484731)|2014-06-03 22:52:01
|152|jonasfj|Updated taskcluster-base with minor fixes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d723e084babf04e6019ab51772a9c14871debbc3)|2014-06-03 22:51:31
|151|jonasfj|Fixed dropdb took a while to track down how to kill knex connections|[URL](https://github.com/taskcluster/taskcluster-queue/commit/252f79a9f39ff263b1326d353e38ddc9edc64dc3)|2014-06-03 22:40:36
|150|jonasfj|Renamed schema tests|[URL](https://github.com/taskcluster/taskcluster-queue/commit/86d40a6821b7628e01ddec0558e336ac70c42472)|2014-06-03 22:11:48
|149|jonasfj|Added node-modules|[URL](https://github.com/taskcluster/taskcluster-queue/commit/da92c4b630e8140a325a4f44fde1686af37ce28d)|2014-06-03 22:09:35
|148|jonasfj|Added dropdb.js|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a9e4561a1568b3b8c6b52337431d932dde5f907f)|2014-06-03 22:04:07
|147|jonasfj|Moved schema testing to use test utility|[URL](https://github.com/taskcluster/taskcluster-queue/commit/617a847596fb461313ae49c561d16eefef32a8f5)|2014-06-03 21:36:27
|146|jonasfj|Refactored config files|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e1fa090596a9b346c86f3de87703cee3fcb86417)|2014-06-03 00:47:18
|145|jonasfj|Ported, tests and a few configs still missing...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/95157b2d342f0f427996c456c24f738ecd7ccc0c)|2014-05-30 23:12:23
|144|jonasfj|Ported exchanges and v1.js|[URL](https://github.com/taskcluster/taskcluster-queue/commit/fb5f6dfb5645b42e56269e0876d7559aee53a0d3)|2014-05-30 19:06:07
|143|jonasfj|Removed utils they are in taskcluster-base now|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f93b90ddbd26434ab9a22afeaedce74f13c914bb)|2014-05-29 22:40:46
|142|jonasfj|Moved schemas for niceness|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7e1239c4e76ef32ead070b685358f0f7c94c0e35)|2014-05-29 22:40:24
|141|lightsofapollo|Remove replaced or unused things|[URL](https://github.com/taskcluster/taskcluster-queue/commit/8601184fa6285aa08caaa9285be60b4e77d0be20)|2014-05-01 20:49:03
|140|lightsofapollo|New internals for the queue|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a6a0253f497a97532696a2223e60171ba3a03324)|2014-05-01 20:47:37
|139|jonasfj|Moved TODOs to bugs - there was only one relevant left...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/54bd79acce1711d00be322c550954d07bbe96317)|2014-04-25 18:02:08
|138|jonasfj|Documented aws policy in README.md|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1dd9aff841fe597da774945c6fd7ba2b341bb42c)|2014-04-25 17:54:51
|137|jonasfj|Added name to API end-points for auto-genenrating client|[URL](https://github.com/taskcluster/taskcluster-queue/commit/de6b36bb194417d9f858e148810819b0ac29a004)|2014-04-18 22:44:31
|136|jonasfj|Test routingkey length and fix database string sizes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/05d6022a1220abd97b3559209cddb5d5aa713465)|2014-04-17 22:03:45
|135|jonasfj|Upped routingKey limit from 64 to 128 bytes|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5003638aac2c767305567208968554294ecaf7e9)|2014-04-17 19:29:33
|134|jonasfj|Allow for optional taskGraphId in task metadata|[URL](https://github.com/taskcluster/taskcluster-queue/commit/fe2e847f924c427001a9cc0d967a5837d1cc7fbf)|2014-04-08 00:24:25
|133|jonasfj|Adding success to resolution.json|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e728fbfa613edea00a42d14ae8b1ea977cccfa81)|2014-04-07 23:14:08
|132|jonasfj|Add success to result.json, task completion request and completion messages|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9a942b7af9688850be53678461b6347aa49b58dd)|2014-04-07 23:01:29
|131|lightsofapollo|Merge pull request #11 from taskcluster/bug-985394  Fix bug 985394|[URL](https://github.com/taskcluster/taskcluster-queue/commit/50731a0eb8186f3d1b0665c6293410440a07ec4d)|2014-03-26 20:28:14
|130|jonasfj|Fix bug 985394|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e7f454064953cc32917f2525b43d71aab6e57033)|2014-03-21 01:05:49
|129|lightsofapollo|Merge pull request #12 from taskcluster/aws-sdk-upgrade  Aws sdk upgrade|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4299d98d00a54a29c823435e4fb6014118254f37)|2014-03-24 21:11:34
|128|jonasfj|Move to using aws-sdk-promise|[URL](https://github.com/taskcluster/taskcluster-queue/commit/05e34b0ba1706b4b7d7b9d2cccb44c6b12ecb17e)|2014-03-21 19:31:50
|127|jonasfj|Added aws-sdk-promise|[URL](https://github.com/taskcluster/taskcluster-queue/commit/90ae39e16539274c368f4de8813bc0ad2b0ddeda)|2014-03-21 19:27:41
|126|jonasfj|Upgrade of aws-sdk|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b7bbcde49844a583212722bf6d4de87df91df86d)|2014-03-21 19:17:36
|125|jonasfj|Adding incident ID to errors|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1e0b05388af549fe4a674bc629890eec52e8bfeb)|2014-03-21 18:59:33
|124|jonasfj|Merge pull request #7 from taskcluster/post-task-url-signing  Post task url signing|[URL](https://github.com/taskcluster/taskcluster-queue/commit/22860a5e2a2937f83d571eb6b0ba3a7272195be9)|2014-03-11 01:12:28
|123|jonasfj|Ported to LocalQueue|[URL](https://github.com/taskcluster/taskcluster-queue/commit/30802ed94e0c6753fee8f76fe7119c511b48cd14)|2014-03-11 00:48:17
|122|jonasfj|Merge branch 'master' of github.com:taskcluster/taskcluster-queue into post-task-url-signing  Conflicts: 	test.sh|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a05f22abd55c539e0aae0240d1542d43b5bcf801)|2014-03-10 21:46:42
|121|lightsofapollo|hotfix - unbreak claim + some initial incomplete tests for it|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0cb76a069fe55356616d58bf31c90c95ae810d51)|2014-03-10 08:20:38
|120|jonasfj|Don't ignore errors|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2fd758ff231fc3b5c088fe818a0aeca0e7d62ecf)|2014-03-08 23:21:47
|119|jonasfj|Let's just set DEBUG=  for travis... it's useful..|[URL](https://github.com/taskcluster/taskcluster-queue/commit/cd82752d145437e61a3ab5f1cb04ede738254482)|2014-03-08 23:06:43
|118|jonasfj|Moved to fetch with S3.getObject, we can now use secret buckets... not sure this is a good idea. Other components will definitely break...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/040e76536e8df220a8d6f855cdd28f1e429df387)|2014-03-08 22:57:12
|117|jonasfj|Changed taskBucketIsCNAME to a string|[URL](https://github.com/taskcluster/taskcluster-queue/commit/db4185b54808bdae971d83b9c43a90bc638e3e18)|2014-03-08 22:33:17
|116|jonasfj|Testing travis CNAME setup problem|[URL](https://github.com/taskcluster/taskcluster-queue/commit/210aff3e46f48aefa368efd553cfe01f53cdd494)|2014-03-08 22:27:57
|115|jonasfj|Testing travis CNAME setup problem|[URL](https://github.com/taskcluster/taskcluster-queue/commit/50d336c0eb7129bc11d955f193c34292f659ca87)|2014-03-08 22:26:09
|114|jonasfj|Okay, need to ask not test...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/585e5e6621eb54cff0728707db9be173fad136fe)|2014-03-08 22:14:11
|113|jonasfj|Testing what is on travis|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f7e63d7a4abc5b591eea27d24dd6ed401cfe409d)|2014-03-08 22:09:18
|112|jonasfj|Testing what is on travis|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0590f61c4ac609d84b6598ad6a7694ae0b21c615)|2014-03-08 22:07:48
|111|jonasfj|fixing up travis configuration|[URL](https://github.com/taskcluster/taskcluster-queue/commit/96ba8b2b791e996cdee8ce3774e9650bcb958427)|2014-03-08 21:54:23
|110|jonasfj|Added DEBUG=  tests|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e682ce2f7e89211fead95e6bc87b3ab168ff7adf)|2014-03-08 21:46:26
|109|jonasfj|disabled data_test.js it doesn't shutdown reliably|[URL](https://github.com/taskcluster/taskcluster-queue/commit/86d1d2a90a20cf3a9a780e075bf15f2fda3b91df)|2014-03-08 11:00:01
|108|jonasfj|Fixed timeout in schedule api end-point... and added extensive tests|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ac3917c78f3a5a75c4a86fbccf75a147aaab472e)|2014-03-08 01:26:07
|107|jonasfj|Upgraded superagent-promise|[URL](https://github.com/taskcluster/taskcluster-queue/commit/375fdced2953d2b720014880b9292516401fab02)|2014-03-08 00:09:00
|106|jonasfj|Added LocalQueue and used process.send() to notifiy parent process that we're now ready|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5b579040fcccfc6607742fcf7d8a519168d0b359)|2014-03-07 23:54:30
|105|jonasfj|Refactored test/ folder layout and fixed bugs from previous merged|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7ab10c01908f319382c1cd360059cfaadfca6b2e)|2014-03-07 23:15:02
|104|jonasfj|Merge branch 'master' of github.com:taskcluster/taskcluster-queue into post-task-url-signing  Conflicts: 	node_modules/promise/node_modules/asap/package.json 	node_modules/promise/package.json 	node_modules/superagent/package.json 	package.json 	test/api/index.js|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ca132fd088832c83ac665dc92b76a79320481a36)|2014-03-07 22:46:47
|103|lightsofapollo|Merge pull request #10 from lightsofapollo/test-fix  test fixup|[URL](https://github.com/taskcluster/taskcluster-queue/commit/336f465e4f87f5356d67b28167279af84a08e80f)|2014-03-07 21:23:47
|102|lightsofapollo|test fixup|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7c2915d6b792d79ce56a6cbd2964499a19d94b91)|2014-03-07 21:23:06
|101|lightsofapollo|Merge pull request #8 from lightsofapollo/configurable-timeout  Configurable timeout|[URL](https://github.com/taskcluster/taskcluster-queue/commit/76716205b232f53a09f6d75dd7fa36cc678a08bc)|2014-03-07 21:13:14
|100|lightsofapollo|Merge pull request #9 from lightsofapollo/use-post  use post instead of get for claim-work (more breaking changes)|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b07f1f0abb7166942111703d759154bbacacd50c)|2014-03-07 21:12:46
|99|lightsofapollo|timeout is mandated|[URL](https://github.com/taskcluster/taskcluster-queue/commit/22926eec0c767924f9bdab8f5076b529903875b3)|2014-03-07 21:11:30
|98|lightsofapollo|update checks in test.sh|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6f4c0acc65a175421027aaae2230de352dedd856)|2014-03-07 20:54:40
|97|lightsofapollo|use post instead of get for claim-work (more breaking changes)|[URL](https://github.com/taskcluster/taskcluster-queue/commit/122ad381daf3d568d849dbdf9c82c9770e52c974)|2014-03-07 20:22:22
|96|lightsofapollo|tweaks for test.sh on CI|[URL](https://github.com/taskcluster/taskcluster-queue/commit/74c55dec9576d3e30c37a9467bc34e7aa5226ff2)|2014-03-07 10:38:11
|95|lightsofapollo|dont drop tables|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1e6bb6e26ee42e94a88fc3d8c870ea6d2a311de2)|2014-03-07 10:21:16
|94|lightsofapollo|Implement configurable timeout / fix bugs in retries|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e6e85385b2d16bf4ea5f604181718bf15c351d6a)|2014-03-07 10:13:30
|93|lightsofapollo|move tests -> test (mostly for mocha)|[URL](https://github.com/taskcluster/taskcluster-queue/commit/aad55fc280d93f11d1677b4f568953bb51158dbe)|2014-03-06 23:22:05
|92|lightsofapollo|update package dependencies|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a1c25957d4c30310435552a8673dc96450d9c5f9)|2014-03-07 09:56:40
|91|jonasfj|Bugfixes for rerun and schedule along with more debug()|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5eaf24c570a547ad781b789cc1a72d2b2d0690a0)|2014-03-07 03:51:45
|90|jonasfj|Added rerun task API end-point|[URL](https://github.com/taskcluster/taskcluster-queue/commit/7c5fcc6a335a465f916fa84d4b9eff04496e6514)|2014-03-06 18:54:26
|89|jonasfj|Added v1/task/:taskId/schedule|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1c9a3c0d81d27ac6d53cab119b5acfc9f5596bc4)|2014-03-06 05:15:30
|88|jonasfj|Bumped to new version of promise and added superagent, maybe we can remove request from tests later..|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4940ce72568ca506b3ede4685454d6c9fd229bbd)|2014-03-06 05:14:30
|87|lightsofapollo|Add procfile so autodeploy works correctly|[URL](https://github.com/taskcluster/taskcluster-queue/commit/14fb5e2ed5ea88a4505e0a57d1be25ddc90df511)|2014-03-06 01:58:28
|86|jonasfj|Added define-tasks API end-point|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e370c988f6d3f4be087c48b8e1b0add767b2ca59)|2014-03-06 01:30:44
|85|lightsofapollo|Merge pull request #6 from taskcluster/schema-renaming  Schema renaming|[URL](https://github.com/taskcluster/taskcluster-queue/commit/49f216a51255b3f48c98eeaa924460b4addaf750)|2014-03-06 01:12:53
|84|jonasfj|Found one that I missed|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4050e2814062d38f011ba81fd5e658aa8620bd2a)|2014-03-05 23:02:44
|83|jonasfj|Load schemas at startup instead of lazy loading them... this increases predictability|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ddea99f299030f603612777e85f67f280043fc98)|2014-03-05 22:56:50
|82|jonasfj|Upgraded jayschema to v2.5|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c66e791da8c0d3c3fafc1d4d496e9f79b78f52fc)|2014-03-05 22:43:39
|81|jonasfj|Renamed all schemas|[URL](https://github.com/taskcluster/taskcluster-queue/commit/685081247ab1dd8cc6c0440194822acfb5e812bf)|2014-03-05 22:42:21
|80|lightsofapollo|schema debugging|[URL](https://github.com/taskcluster/taskcluster-queue/commit/86221fc7f8400e581e8cc027f9995dfba34e4e77)|2014-03-05 21:21:24
|79|lightsofapollo|Merge pull request #4 from lightsofapollo/debug  more schema debugging|[URL](https://github.com/taskcluster/taskcluster-queue/commit/331a7311702ad68f8421161b86e796328aad4c6f)|2014-03-05 21:15:20
|78|lightsofapollo|more schema debugging|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1e27f5d49fe7aed6275ab2709f3f5def327ae8d9)|2014-03-05 21:14:39
|77|lightsofapollo|Merge pull request #3 from taskcluster/slugid  uuid -> slugid, then fixed tests and stabelized events test|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0ac486d8640658f3a15c1b486da6e5c66b62ccd3)|2014-03-05 20:38:47
|76|jonasfj|Okay, I forget to fix the data.js test|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a89aeddbef3f1be5225d9bb1bd805f9606110f81)|2014-03-05 20:32:36
|75|jonasfj|Merge branch 'master' of github.com:taskcluster/taskcluster-queue|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ecd639c3c27d8fdfc4d146d8932516668537cc9a)|2014-03-05 20:27:13
|74|jonasfj|uuid -> slugid, then fixed tests and stabelized events test|[URL](https://github.com/taskcluster/taskcluster-queue/commit/baf12e60f5acb8bab92d9fc560ad8e342d7be41b)|2014-03-05 20:07:47
|73|lightsofapollo|debug|[URL](https://github.com/taskcluster/taskcluster-queue/commit/99e923f484f53eb03ca66ef44159c753ef1b2754)|2014-03-02 23:38:28
|72|lightsofapollo|Add debug to schema|[URL](https://github.com/taskcluster/taskcluster-queue/commit/45b5877bb462fcdf1e9d52afc3f5d9500844aefd)|2014-03-02 23:25:29
|71|lightsofapollo|Update deployment note|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5a02fb56b0777fdc5a1887dffcd6dd4ed1544111)|2014-03-01 01:14:10
|70|jonasfj|Merge pull request #2 from lightsofapollo/fullstack-testing  Kill makefile simple bash script is easier for ci stuff|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b8e545dc0d774e183e9fd6671c705792e99be8ce)|2014-03-01 01:10:19
|69|lightsofapollo|Kill makefile simple bash script is easier for ci stuff|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d7806dd373325210ff593e3be167d1af2ce433ff)|2014-03-01 00:56:35
|68|jonasfj|Merge pull request #1 from lightsofapollo/autodeploy  Turn on heroku autodeploy & travis ci|[URL](https://github.com/taskcluster/taskcluster-queue/commit/fd1909cfa191f0b7788cf209195d068399bba2c3)|2014-03-01 00:08:47
|67|lightsofapollo|fix service name|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1fb4b973fd6a2cbdbf481e4369a220704e4a3ecd)|2014-02-28 23:15:04
|66|lightsofapollo|Turn on heroku autodeploy & travis ci|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1873361f14921eb1f99dc0a24a8c05028a2aa45d)|2014-02-28 23:13:11
|65|jonasfj|Fixing bug just introduced...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f4f80882e27f75fb0cb8ef76a8aa8699bc4270fd)|2014-02-27 19:57:48
|64|jonasfj|Update artifact put-url response to include result URL, this is useful|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f45a451b335e8204692f2724fb60c4e8d4c9c6cd)|2014-02-27 19:32:26
|63|jonasfj|Allow Content-Type for CORS request, it's basically required :)|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3dc6e2015a7e0659595cac5efda19b598986e611)|2014-02-26 02:27:44
|62|jonasfj|Added specification to task.json tags|[URL](https://github.com/taskcluster/taskcluster-queue/commit/bb8a1a7a1d2bb9cddb1db7b8123713f623e1e388)|2014-02-26 00:58:55
|61|jonasfj|Title and description for task payload|[URL](https://github.com/taskcluster/taskcluster-queue/commit/dcf3d5ba8c5d538ec1072ece3e330aa79f1fa52a)|2014-02-26 00:23:10
|60|jonasfj|Added title to task definition schema|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2ab736de1e2f80bd2121ee895bb6de5e11bdb125)|2014-02-26 00:08:44
|59|jonasfj|Adding http:// for generated urls|[URL](https://github.com/taskcluster/taskcluster-queue/commit/cd7e38d6be8d672f29ab2355d8fa2d899d52ced9)|2014-02-25 01:04:11
|58|jonasfj|Fixed minor bugs with URLs for results.json and logs.json|[URL](https://github.com/taskcluster/taskcluster-queue/commit/048146d15c82d0c99da3e4a1df5386133d95ec22)|2014-02-22 03:16:04
|57|jonasfj|Fixed schema description bugs|[URL](https://github.com/taskcluster/taskcluster-queue/commit/200f8d6f5bc0d236e426570c946270f5256679cc)|2014-02-19 19:19:47
|56|jonasfj|Ups, middleware bug|[URL](https://github.com/taskcluster/taskcluster-queue/commit/a2245c0d9d53f01771eeb61e03579f8e08067b46)|2014-02-19 18:36:53
|55|jonasfj|Allow CORS request against the API|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6931ad6de74cfe2f45c898b8e9ba9b0bac74825a)|2014-02-19 18:21:44
|54|jonasfj|Build schema publication into server startup... disabled by default, activated by config|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f79985525701b23cd3132ab93d555e8b30db79ee)|2014-02-19 18:16:17
|53|jonasfj|Added API end-point for fetching AMQP connection string|[URL](https://github.com/taskcluster/taskcluster-queue/commit/8acd859dd76c511512622a5235a7cecd60bfaa99)|2014-02-19 05:26:04
|52|jonasfj|Forced to obscure my configs further by heroku... tsk tsk...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/89ef3c96872dd8df608715f5c499e32de4ba42f9)|2014-02-19 02:38:57
|51|jonasfj|Updated package.json for heroku|[URL](https://github.com/taskcluster/taskcluster-queue/commit/eb2ebe1ca561eafd965ad566d14524855081bb52)|2014-02-19 02:33:57
|50|jonasfj|Refactored config to loadedable from environment varialbes...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5c3fba549c5d21c63728b54f3aa0127e9c5283b7)|2014-02-19 02:18:39
|49|jonasfj|Formalized schemas for files stored in S3, we might not validate against them right now.. but having them formally defined is important|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f6c9a1013f7bf8ad29e9b174f7e811001386db92)|2014-02-18 20:35:46
|48|jonasfj|Fixed bug in artifact response schema|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b5f1d9a0f8d66092801f1ca6bb7c3a5840c27c64)|2014-02-18 20:14:00
|47|jonasfj|Added more logging, fixed minor potential bug, and added a schema for ealier error detection|[URL](https://github.com/taskcluster/taskcluster-queue/commit/20ee9f5fc67d7c9c47c622c0babb473c6fef3db3)|2014-02-15 05:53:48
|46|jonasfj|Fixed pending task querying for provisioner|[URL](https://github.com/taskcluster/taskcluster-queue/commit/45b8baf0431bc87f0ee8d3baa48f8f4a18bb057e)|2014-02-12 23:24:29
|45|jonasfj|Fixed bugs|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d783b46c6197abf21281bd679acb44aac7072f3c)|2014-02-12 06:14:31
|44|jonasfj|Schemas for most request and responses|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6c3509dce237f97092360fd76b455847a4fa27b3)|2014-02-12 06:04:58
|43|jonasfj|Let claims and deadlines expire|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e4ba5fc9522179e32f35b103bce7cd9a588666ef)|2014-02-12 01:47:43
|42|jonasfj|Additional tests and improved schemas|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9eb0e8fa30b0152024a8437f8d22a99f1444b9bf)|2014-02-12 01:47:21
|41|jonasfj|Spelling error - I knew alignment was too good to be true...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0dd2b45b860836a2ef6c651c5499c9abfb5670ad)|2014-02-11 20:06:06
|40|jonasfj|Think I enabled CORS|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e34806bef310c5cbd07b9fd5c65f4e5fd64be965)|2014-02-11 19:44:57
|39|jonasfj|Fixed /v1/reference end-point|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0eac74d8787c7fd85294986be231d2a855e7bcb4)|2014-02-11 19:35:11
|38|jonasfj|Offer API documentation as JSON|[URL](https://github.com/taskcluster/taskcluster-queue/commit/978e9d89079a2986f4e68839dc221b93f8c20e91)|2014-02-11 19:24:33
|37|jonasfj|Extended schemas for messages|[URL](https://github.com/taskcluster/taskcluster-queue/commit/11e48ed3ec155337e47f79970ae7b91dc7a8ebe6)|2014-02-11 07:58:37
|36|jonasfj|Added little documentation...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/028a74babd42f8e549774eec09ccfd0610082c99)|2014-02-11 05:57:31
|35|jonasfj|Add a little logging|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f1b9527a42a6d764b0cbe1107d38ed0da7f9bf2a)|2014-02-11 05:54:27
|34|jonasfj|Refactored schemas, to support a simple constants that can be substituted for better maintainability|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2d0909a5661d2d752b01cf2f5351e8481777c962)|2014-02-11 05:48:16
|33|jonasfj|Added mkdirp|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f68d3425680c8770899a959ce049b535d138a446)|2014-02-11 05:12:39
|32|jonasfj|Refactored schemas for docson usage|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0504d9cbca2b596599de231ed7c84984f0cc81fe)|2014-02-11 02:58:01
|31|jonasfj|Updated readme|[URL](https://github.com/taskcluster/taskcluster-queue/commit/8344904a456b2b98b0e25b21ea34835f07638ebc)|2014-02-10 22:48:05
|30|jonasfj|Fixed title|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0157180450c7389a123d7fb4b06e261b3a267f26)|2014-02-10 21:46:21
|29|jonasfj|Tesing deploy again|[URL](https://github.com/taskcluster/taskcluster-queue/commit/4bacd3eaa768396823aab4d0372ddd2d13c83fa0)|2014-02-10 21:44:10
|28|jonasfj|Forgot to add github hook, it's great that my templates are fairly outdated, so I keep updating :)|[URL](https://github.com/taskcluster/taskcluster-queue/commit/690648847d590eafb71242dde5f3908acb257c9e)|2014-02-10 19:05:53
|27|jonasfj|Updated template to test auto-deploy|[URL](https://github.com/taskcluster/taskcluster-queue/commit/45f8f4076fb02337eca82c56aa3641061c2639ae)|2014-02-10 19:03:11
|26|jonasfj|Fixed postgres case insensitivty issues|[URL](https://github.com/taskcluster/taskcluster-queue/commit/cab830a3c3b5879ff5e97fe3301afafe448ab8b0)|2014-02-10 00:18:48
|25|jonasfj|Fixed test to refactored naming|[URL](https://github.com/taskcluster/taskcluster-queue/commit/68b687f372cfca3f77689ab7a4864300cacaadd7)|2014-02-09 23:37:40
|24|jonasfj|Fixed schema source references|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b63c0e34a71c353fe669c05d521e1c09d794141b)|2014-02-09 23:25:31
|23|jonasfj|Refactored schema structure|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9a27406289418252d01dfa67e86622f76d8717d9)|2014-02-08 23:06:38
|22|jonasfj|Renamed from xxxx_id to xxxxId|[URL](https://github.com/taskcluster/taskcluster-queue/commit/19e67b9af218c43694965f3d2169a2b983b2fd03)|2014-02-08 20:32:47
|21|jonasfj|Minor chanages removing a stupid hack|[URL](https://github.com/taskcluster/taskcluster-queue/commit/2ce566eb94bdc7ce928c4a1ff9e9bca8e7d4f59f)|2014-02-07 23:39:19
|20|jonasfj|Lots of small bugfixes all around|[URL](https://github.com/taskcluster/taskcluster-queue/commit/e194adbc39aeaff69ee7e4cb875bdba427fb4be2)|2014-02-07 06:55:44
|19|jonasfj|Updated name in package.json|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d317fce362a1b097ffab6001ebb481efe41b9e12)|2014-02-05 23:25:54
|18|jonasfj|More API implementation, only need testing|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f6ec8603f9a45b576b0fdd2a2d8cdd795a83e7c5)|2014-02-05 04:16:07
|17|jonasfj|Documented todos and project structure|[URL](https://github.com/taskcluster/taskcluster-queue/commit/f75312b94b63966352145e4093f5295a71c271f6)|2014-02-05 04:01:18
|16|jonasfj|Added a few dummy schemas|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9090fcd7a431e1c55e110a7359dc7f62be6e49b8)|2014-02-05 00:01:53
|15|jonasfj|Claim route and more tests... and data layer stuff|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ee6da21f4483ec5e4fcd4bd7dae85a7ce14352c7)|2014-02-04 23:58:41
|14|jonasfj|Connect to postgres and create tables...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/3c7f0b4f68732d137308b60f4b59a669e551f382)|2014-02-04 00:24:05
|13|jonasfj|Updated nodeunit|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b67b0f4c8719a70a12ea58446e5b4249fdde4673)|2014-02-03 22:20:19
|12|jonasfj|Tests for API end-points|[URL](https://github.com/taskcluster/taskcluster-queue/commit/eade628e785f0eb4899bd84d7bf507e224be01a9)|2014-02-03 22:19:32
|11|jonasfj|Added lots of tests, events.js now works :)|[URL](https://github.com/taskcluster/taskcluster-queue/commit/91b75d4cf62f00b2a6930d52dea6a0c15e34d3b1)|2014-02-02 08:20:34
|10|jonasfj|JSON Schema setup... and AMQP setup|[URL](https://github.com/taskcluster/taskcluster-queue/commit/fd9a57f3246b4c1606b48e965a1140746df7cad9)|2014-02-01 06:33:55
|9|jonasfj|Committing ugly node_module/ files again|[URL](https://github.com/taskcluster/taskcluster-queue/commit/10ec6e68edddc7ffae56c89545657c6186651818)|2014-02-01 01:24:43
|8|jonasfj|Depend on jayschema|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9398216cd8ead116bcf7bbd3f9b5f4a1561a2df5)|2014-02-01 01:23:58
|7|jonasfj|Adding node_moduels again, feeling so sad...|[URL](https://github.com/taskcluster/taskcluster-queue/commit/1f20bcf72e67cfd348250a2fe279232046cdf1cb)|2014-02-01 00:23:19
|6|jonasfj|Depend on node-amqp|[URL](https://github.com/taskcluster/taskcluster-queue/commit/fb90321c196aaa86c0c6d9b2ed48184357ff786d)|2014-02-01 00:22:52
|5|jonasfj|Adding config for AMQP|[URL](https://github.com/taskcluster/taskcluster-queue/commit/c6b1da7c681e08a18e50e28244de7f861590700c)|2014-02-01 00:22:39
|4|jonasfj|Add aws configuration back|[URL](https://github.com/taskcluster/taskcluster-queue/commit/b4ab6a210593892f6f70f75fb37423f6c9a81959)|2014-01-31 23:31:46
|3|jonasfj|Add gitignore... for .vagrant/|[URL](https://github.com/taskcluster/taskcluster-queue/commit/77e8030d4b893c4915247f98181c2cf84c090eb2)|2014-01-31 23:27:29
|2|jonasfj|Added pg.js installed files|[URL](https://github.com/taskcluster/taskcluster-queue/commit/cc12928bd4a50a6e9a3c547095bc5a4d5325c12a)|2014-01-31 23:27:00
|1|jonasfj|Add pg dependency|[URL](https://github.com/taskcluster/taskcluster-queue/commit/d511ea51621b55d2e9be02925400fdab3b032ad4)|2014-01-31 23:24:18


