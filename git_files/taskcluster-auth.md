## TASKCLUSTER-AUTH COMMIT MARKDOWN TABLE SINCE 2018-12-03 17:46:15.735277

| Commit Number | Commiter | Commit Message | Commit Url | Date | 
|:---:|:----:|:----------------------------------:|:------:|:----:| 
|668|djmitche|Merge pull request #188 from djmitche/bug1510377  Bug 1510377 - use tc-lib-references to validate references|[URL](https://github.com/taskcluster/taskcluster-auth/commit/5077077f2e4094d22eef527dc9883cb8dffa387e)|2018-12-10 18:27:23
|667|djmitche|Bug 1510377 - use tc-lib-references to validate references|[URL](https://github.com/taskcluster/taskcluster-auth/commit/325de3bc38bed1b8800668f0eed6e0d2ec8b73e7)|2018-12-06 00:00:09
|666|djmitche|(hotfix) upgrade tc-lib-api for previous change|[URL](https://github.com/taskcluster/taskcluster-auth/commit/d6424744e5f48b20255bac0083889508d3ab95a2)|2018-12-05 23:45:07
|665|djmitche|Merge pull request #187 from arshadkazmi42/bug-1400999  204 response changed to use res.reply|[URL](https://github.com/taskcluster/taskcluster-auth/commit/4c1447920ffafd15bdbc32cc5a243cd97c62684c)|2018-12-05 23:38:19
|664|arshadkazmi42|204 response changed to use res.reply|[URL](https://github.com/taskcluster/taskcluster-auth/commit/2a6d46d36e0b7e2fb4b6fc4ee59914033238506f)|2018-12-02 18:34:01
|663|djmitche|Merge pull request #185 from djmitche/bug1509089  Bug 1509089 - remove LOCK_ROLES support|[URL](https://github.com/taskcluster/taskcluster-auth/commit/dbbcef916c53765e535d7cd9580367089cec3a17)|2018-11-30 02:24:43
|662|djmitche|Merge pull request #186 from djmitche/bug1509154  Bug 1509154 - await row removals|[URL](https://github.com/taskcluster/taskcluster-auth/commit/9babc5e6d48fc27013e58e8e67eb085bfaa6561e)|2018-11-30 02:24:34
|661|djmitche|Bug 1509154 - await row removals|[URL](https://github.com/taskcluster/taskcluster-auth/commit/6375db436a015e587979ded3e94fe36cd90ec7c6)|2018-11-29 01:23:01
|660|djmitche|Bug 1509089 - remove LOCK_ROLES support  This was a big old hack meant to block changes to roles during the transition to storing roles in a blob.  It's not needed anymore.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/b8c3dfe5dc51e448e3c4773b7bd386e8db37ffe9)|2018-11-28 22:01:44
|659|djmitche|Merge pull request #184 from djmitche/bug1456909  Bug 1456909 - use monitor.oneShot|[URL](https://github.com/taskcluster/taskcluster-auth/commit/68bd2858a24e54fb079e76b8997b1ef19bfb5f88)|2018-11-26 22:08:53
|658|djmitche|Merge pull request #183 from djmitche/bug1509186  Bug 1509186 - remove references to taskcluster.net from API description|[URL](https://github.com/taskcluster/taskcluster-auth/commit/e414f8fd6a2aae1a8dd5ec378bfac8771eac4063)|2018-11-26 21:22:45
|657|djmitche|Bug 1456909 - use monitor.oneShot|[URL](https://github.com/taskcluster/taskcluster-auth/commit/85c8a9e8ca9847fdaf85b61391d52046deca152f)|2018-11-26 19:12:05
|656|djmitche|Bug 1509186 - remove references to taskcluster.net from API description|[URL](https://github.com/taskcluster/taskcluster-auth/commit/c0f7725ddbe0816b5189aca59077831ae795f73d)|2018-11-26 18:10:46
|655|djmitche|Bug 1508846 - upgrade tc-lib-api|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ee8964bac335b073f41210c3968e7f12a5ec5341)|2018-11-21 20:12:20
|654|djmitche|Merge pull request #181 from djmitche/bug1505405  Bug 1505405 - upgrade tc-lib-pulse|[URL](https://github.com/taskcluster/taskcluster-auth/commit/d0bc2154649c75406ff56757d126127289ee4e01)|2018-11-21 20:32:22
|653|djmitche|Bug 1505405 - upgrade tc-lib-pulse  This only affects the output references format (for RFC 128)|[URL](https://github.com/taskcluster/taskcluster-auth/commit/33052858d025cf67f128dff7fd55231c323c95b1)|2018-11-20 19:13:43
|652|djmitche|Merge pull request #180 from djmitche/bug1508395  Bug 1508395 - upgrade tc-lib-validate|[URL](https://github.com/taskcluster/taskcluster-auth/commit/9ed089f62916fa2a54967379cfb5bc35156b8cea)|2018-11-21 19:48:44
|651|djmitche|Merge pull request #182 from djmitche/bug1508849  Bug 1508849 - implement   -scope protection differently|[URL](https://github.com/taskcluster/taskcluster-auth/commit/052d624ea730559489f6984b8fb47b819e2ffe94)|2018-11-21 19:48:33
|650|djmitche|Bug 1508849 - implement   -scope protection differently  The old solution used a negative lookbehind, which per https://json-schema.org/understanding-json-schema/reference/regular_expressions.html#regular-expressions is not supported in json-schema.  In fact, it's not supported in even fairly recent versions of Node.  This causes problems when validating schemas using those old versions of node (or using json-schema validators that do not support this form).  So, the new solution is to explicitly forbid those forms where used in creating clients and roles.  The result is much the same, as evidenced by the minimal changes to the tests.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/b19103d6d2ac47d16e2086a283e04320651ff383)|2018-11-21 00:46:14
|649|djmitche|Bug 1508395 - upgrade tc-lib-validate  The change ony affects the output of writeDocs.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/e52d89a68dc312b5ca045558ff7d4011663312db)|2018-11-20 19:10:53
|648|djmitche|Merge pull request #179 from djmitche/update-lib-validate  Update taskcluster-lib-validate for better errors|[URL](https://github.com/taskcluster/taskcluster-auth/commit/41298abbcf415a877d96c6e28cf721e85ac324c5)|2018-10-31 19:33:19
|647|djmitche|Merge pull request #177 from djmitche/staticallyconfigured  add whitespace|[URL](https://github.com/taskcluster/taskcluster-auth/commit/0fa04e11f2fdcc902eed9c083a8c56d732f3d744)|2018-10-31 17:51:34
|646|djmitche|Merge pull request #178 from djmitche/node-0-8-10  upgrade node|[URL](https://github.com/taskcluster/taskcluster-auth/commit/5ca9fb130b20caea3a37e48572c4158355633f89)|2018-10-31 17:38:06
|645|djmitche|Update taskcluster-lib-validate for better errors|[URL](https://github.com/taskcluster/taskcluster-auth/commit/e29fadd5db61078fc0eef117d0bf212cef56960e)|2018-10-31 17:37:53
|644|helfi92|Fix user-config-example.yml (#176)|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ff3a9391f1cb64b1c9fc2c56d091c0022d0a197b)|2018-10-30 23:05:52
|643|djmitche|upgrade node|[URL](https://github.com/taskcluster/taskcluster-auth/commit/417fc7f78090de1bc27c659e314b62259beac5d5)|2018-10-30 22:03:07
|642|djmitche|add whitespace|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ee2f930a844588b29d913d954a862e0f215220cf)|2018-10-30 02:44:28
|641|djmitche|Merge pull request #175 from djmitche/bug1499701  Bug 1499701 - upgrade fast-azure-storage|[URL](https://github.com/taskcluster/taskcluster-auth/commit/d4dee5dd32fb602cc86a0f1f6a3454912d4f6fe3)|2018-10-19 18:02:19
|640|djmitche|Bug 1499701 - upgrade azure to behave better on SAS errors|[URL](https://github.com/taskcluster/taskcluster-auth/commit/7371458b6c493180b6d75ed054de6c9b6e366500)|2018-10-18 23:51:42
|639|djmitche|set the pr policy to collaborators|[URL](https://github.com/taskcluster/taskcluster-auth/commit/40deb9ea17b4ac7ecbcf24728c4987f8ff95b0e2)|2018-10-19 17:01:29
|638|djmitche|Merge pull request #173 from djmitche/bug1488789  Bug 1488789 - use tc-lib-pulse|[URL](https://github.com/taskcluster/taskcluster-auth/commit/91168809cf79ba3f9409b19045b1b0cda75348a1)|2018-10-19 16:06:26
|637|djmitche|Bug 1488789 - use tc-lib-pulse  For real this time!     Use configured pulse credentials, so no dependency on another service    Use ephemeral consumers for the "notification" pulse messages|[URL](https://github.com/taskcluster/taskcluster-auth/commit/651b2f813a43b9037f8072b8e1d722fc6c47dd0c)|2018-10-16 20:53:38
|636|djmitche|Revert "Merge pull request #171 from djmitche/bug1488789"  This reverts commit c5f1b3d46754b278acf91380b1b5b9b76cc42311, reversing changes made to 37b71bface82b73f293edced091bb63f3013db06.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/bcd02063f724c810d87b2270d68a9c302d305499)|2018-10-18 18:11:01
|635|djmitche|Merge pull request #171 from djmitche/bug1488789  Bug 1488789 - use taskcluster-lib-pulse to interface with Pulse|[URL](https://github.com/taskcluster/taskcluster-auth/commit/c5f1b3d46754b278acf91380b1b5b9b76cc42311)|2018-10-18 17:18:22
|634|djmitche|Merge branch 'master' into bug1488789|[URL](https://github.com/taskcluster/taskcluster-auth/commit/779f9649e71c09016ebb953fd1336329559e1e0c)|2018-10-18 17:18:12
|633|imbstack|Merge pull request #172 from taskcluster/update-lib-monitor-with-fix  Add fix to audit log monitoring|[URL](https://github.com/taskcluster/taskcluster-auth/commit/37b71bface82b73f293edced091bb63f3013db06)|2018-10-17 21:53:13
|632|imbstack|Add fix to audit log monitoring|[URL](https://github.com/taskcluster/taskcluster-auth/commit/07b276e9ac96e8cfb6234155f6c09ee028005183)|2018-10-17 21:28:34
|631|djmitche|Bug 1488789 - use taskcluster-lib-pulse to interface with Pulse|[URL](https://github.com/taskcluster/taskcluster-auth/commit/834a3a300067a740a79db493f259bcaab8fa5b2d)|2018-10-16 20:53:38
|630|djmitche|Revert "Merge pull request #170 from djmitche/bug1488789"  This reverts commit 40e44eacf15ed2b40e309f16ec909a08b08b33c0, reversing changes made to 9d93656b73593331a9e01bfe76e757a75114fafc.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/7ddbd25f01872d28f1cdaf7c9ae7a3ae7ad51f31)|2018-10-17 19:42:44
|629|djmitche|Revert "Bug 1488789 - provide taskcluster credentials for use with tc-pulse"  This reverts commit 66f7ffd1d4d04a22b7394bfb249f1d947d00b971.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/f8269df84dbfe5c80ec7262a660be99285c787c8)|2018-10-17 19:42:35
|628|djmitche|Bug 1488789 - provide taskcluster credentials for use with tc-pulse|[URL](https://github.com/taskcluster/taskcluster-auth/commit/66f7ffd1d4d04a22b7394bfb249f1d947d00b971)|2018-10-17 19:20:55
|627|djmitche|Merge pull request #170 from djmitche/bug1488789  Bug 1488789 - use taskcluster-pulse to get pulse creds|[URL](https://github.com/taskcluster/taskcluster-auth/commit/40e44eacf15ed2b40e309f16ec909a08b08b33c0)|2018-10-17 19:07:14
|626|djmitche|Bug 1488789 - use taskcluster-pulse to get pulse creds|[URL](https://github.com/taskcluster/taskcluster-auth/commit/c750ed2c970fb73422f5673986dd96f92ddddc56)|2018-10-16 20:53:38
|625|djmitche|Take the AWS region from AWS_REGION|[URL](https://github.com/taskcluster/taskcluster-auth/commit/9d93656b73593331a9e01bfe76e757a75114fafc)|2018-10-16 19:08:41
|624|djmitche|Don't hard-code auditLog for production|[URL](https://github.com/taskcluster/taskcluster-auth/commit/e0b08698cfe334d602c33dc16969ee6d52268e24)|2018-10-16 17:59:37
|623|djmitche|upgrade pulse-publisher to fix bug|[URL](https://github.com/taskcluster/taskcluster-auth/commit/33b38bd5150ef9dc258b0c9bfb6586a7287ae6fc)|2018-10-16 17:29:08
|622|djmitche|Merge pull request #169 from djmitche/bug1498700  Bug 1498700 - pass a namespace in case different from username|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ee48c7b7c5b9c64e2fe567c632a8d456287fa364)|2018-10-15 23:41:35
|621|djmitche|Bug 1498700 - pass a namespace in case different from username|[URL](https://github.com/taskcluster/taskcluster-auth/commit/b3d764f9a5f79e97aa771b477f2adc2c6b473e12)|2018-10-15 20:50:56
|620|petemoore|Merge pull request #168 from taskcluster/bug1495918  Bug 1495918 - use `NO_TEST_SKIP: "true"` rather than `NO_TEST_SKIP: true` in yaml files|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ca609c36397ee5914be9c231c9e601cc2ae1433d)|2018-10-10 14:04:11
|619|petemoore|Bug 1495918 - use `NO_TEST_SKIP: "true"` rather than `NO_TEST_SKIP: true` in yaml files|[URL](https://github.com/taskcluster/taskcluster-auth/commit/8baecb668bf32f17aa0da2f0ee477a9988602127)|2018-10-09 09:17:23
|618|imbstack|Temporarily hardcode audit log path for rollout.  Revert after this lands and is working in production|[URL](https://github.com/taskcluster/taskcluster-auth/commit/4301f80d38ea2a336fb2446fcb9b4098ed142c47)|2018-10-03 20:25:20
|617|imbstack|Merge pull request #167 from taskcluster/putrecords-audit-logs  Update lib-monitor for new audit logs process|[URL](https://github.com/taskcluster/taskcluster-auth/commit/0d70c783b084168c6a5a3ce7978083a78686bf68)|2018-10-03 20:21:42
|616|imbstack|Update lib-monitor for new audit logs process|[URL](https://github.com/taskcluster/taskcluster-auth/commit/06d6d47f14f9385786ac164c84edac68d202be89)|2018-10-03 18:35:01
|615|imbstack|Merge pull request #166 from taskcluster/fix-azure-tests  Fix azure table listing|[URL](https://github.com/taskcluster/taskcluster-auth/commit/c79a00ac64f27f80d648d9d6108715e29aa30856)|2018-09-27 19:45:04
|614|imbstack|Fix azure table listing|[URL](https://github.com/taskcluster/taskcluster-auth/commit/2f2232ee6521fd252760818a254f191c55f93093)|2018-09-27 18:19:54
|613|imbstack|Merge pull request #165 from taskcluster/update-lib-api  Update lib-api for audit log ip addresses|[URL](https://github.com/taskcluster/taskcluster-auth/commit/95fc8d6a34ec75c60d1b447f2bbcb38138c4dbb2)|2018-09-26 20:04:54
|612|imbstack|Allow ipv6 source addressses|[URL](https://github.com/taskcluster/taskcluster-auth/commit/f16a5807fab6429a2ed34ab4cc5aaf9c8f046851)|2018-09-26 19:43:26
|611|imbstack|Update lib-api for audit log ip addresses|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ef4897bc0b2ea94cffe6a7d5ffe3dc71e4ae0326)|2018-09-25 21:23:52
|610|ccooper|Add documentation to bring taskcluster repos closer to the Github recommended community standards  Added licensing info (MPL2), contribution suggestions, and a link to the Mozilla Community Participation Guidelines.  Addresses https://bugzil.la/1408073 for this repo.  Carrying-over review from https://github.com/taskcluster/taskcluster-tools/pull/546|[URL](https://github.com/taskcluster/taskcluster-auth/commit/cdfc489c7fcb463d021ce6907786e58a450cbe78)|2018-09-13 15:03:47
|609|imbstack|Merge pull request #163 from ajvb/ajvb/add-sourceip  Add sourceIp to auditlog log line|[URL](https://github.com/taskcluster/taskcluster-auth/commit/6468f75e2e3fe9c72023221c90f9ee51fa77e604)|2018-09-12 17:39:34
|608|djmitche|Merge pull request #164 from djmitche/bug1481944  Bug 1481944 - upgrade hawk|[URL](https://github.com/taskcluster/taskcluster-auth/commit/18dadcfb9b12e6379a0480b379a735896cbdd3d8)|2018-09-07 12:27:43
|607|djmitche|Bug 1481944 - upgrade lib-testing to use newer hawk, too, just because|[URL](https://github.com/taskcluster/taskcluster-auth/commit/c2dc9d678ec54eaf0d29a486f1202d10c4c6ff66)|2018-09-06 18:55:49
|606|djmitche|Bug 1481944 - remove unused superagent-hawk|[URL](https://github.com/taskcluster/taskcluster-auth/commit/6e17209cb70c2f87bb59c7e73d2b5fa02ff10f58)|2018-09-06 18:48:36
|605|djmitche|Bug 1481944 - update to Hawk-4.1.2  Hawk does not follow semver, and does not have a changelog. The only thing described as "breaking" is hueniverse/hawk@f11626d1a651f505700d26af7bb14fabe7fdf65d. This is a change to the nonceFunc API; auth does not use nonceFunc, but had some unused support for it which is now removed. Attempts to use that support will fail with an assertion error.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/650e01df728e0ff9d3f80cf4630bf39a90018b82)|2018-09-06 17:37:04
|604|djmitche|Bug 1481944 - explicitly exclude creds in test  Without this, the client will use $TASKCLUSTER_  if they are set, which is not what we want!|[URL](https://github.com/taskcluster/taskcluster-auth/commit/a64bee77d28ea3c493494e736a8f04ea44d139cd)|2018-09-06 18:29:17
|603|ajvb|Add sourceIp to schema and schema test data|[URL](https://github.com/taskcluster/taskcluster-auth/commit/d2e70d0093fdd1fb15a8f86f82979d4277edff01)|2018-09-05 22:09:18
|602|ajvb|add \|\| 0.0.0.0 to sourceIp logging line|[URL](https://github.com/taskcluster/taskcluster-auth/commit/3d5bad0f01999e05f0c06bfca8181b1a462e696a)|2018-09-05 22:08:40
|601|ajvb|Add sourceIp to auditlog log line|[URL](https://github.com/taskcluster/taskcluster-auth/commit/da1c3e0093b10a663e14ab583ae116219e39720d)|2018-09-04 21:45:53
|600|imbstack|Merge pull request #162 from taskcluster/timestamps-for-logs  Add timestamps for more accurate logging. Also this will work with Athena|[URL](https://github.com/taskcluster/taskcluster-auth/commit/cffd2c1a302c281648c286b87c9796027d940ddf)|2018-08-30 21:30:42
|599|imbstack|Add timestamps for more accurate logging. Also this will work with Athena|[URL](https://github.com/taskcluster/taskcluster-auth/commit/345da415dec37b6d9930d45f8dd0000b77bd14a0)|2018-08-27 17:51:24
|598|djmitche|Merge pull request #161 from djmitche/bug1440965  Bug 1440965 - enforce scopes don't end in   |[URL](https://github.com/taskcluster/taskcluster-auth/commit/034af1ac9e0bead86e8443589138f2625fdb3cd5)|2018-08-24 16:32:10
|597|djmitche|Bug 1440965 - document double-stars issue|[URL](https://github.com/taskcluster/taskcluster-auth/commit/740f01f1fcf24bb2019068bb8b8000449cce7a89)|2018-08-23 19:34:48
|596|djmitche|Bug 1440965 - enforce no scopes ending with    in clients or roles|[URL](https://github.com/taskcluster/taskcluster-auth/commit/e69c185e2c0dc0b55312e020d24f4f4e1f15e13d)|2018-08-23 19:24:59
|595|djmitche|Merge pull request #160 from owlishDeveloper/bug1476856  Use v1 taskcluster.yml|[URL](https://github.com/taskcluster/taskcluster-auth/commit/7a8edf6057a831bcf426281fabe6d86709aed9e4)|2018-07-20 19:47:26
|594|owlishDeveloper|Use v1 taskcluster.yml|[URL](https://github.com/taskcluster/taskcluster-auth/commit/4b2cbe7b33b5c66cb2cc75c824b9afaf5ff21e29)|2018-07-20 02:34:35
|593|djmitche|Bug 1476441 - update absolute link in README (#159)|[URL](https://github.com/taskcluster/taskcluster-auth/commit/4ecdb8d574c87c6ba24624a96d205c11ec2f29fc)|2018-07-18 22:25:05
|592|imbstack|Merge pull request #158 from taskcluster/update-libs  Get some bugfixes in libs|[URL](https://github.com/taskcluster/taskcluster-auth/commit/b1eeb50c52b8dea224f7b8bde2cf4d4297dc1c23)|2018-07-09 15:52:00
|591|imbstack|Get some bugfixes in libs|[URL](https://github.com/taskcluster/taskcluster-auth/commit/e48cb0cc80fc087973b0001bbe7da9971c7e668d)|2018-07-09 15:18:11
|590|imbstack|Update for r14y (#157)  This both upgrades all libraries to their 10.x versions and makes static-clients actually usable.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/0185b8b44f8ee3128b5b5fb6e972ddfdbb59183d)|2018-07-06 15:18:31
|589|jonasfj|Merge pull request #138 from taskcluster/complete-trie  Complete trie|[URL](https://github.com/taskcluster/taskcluster-auth/commit/cd56d5b60082433f993152fab94adf209b8af93e)|2018-06-28 11:25:49
|588|jonasfj|updated test cases after fixing all cycles in roles|[URL](https://github.com/taskcluster/taskcluster-auth/commit/7d9b6483ecf1a438b1a22584370a87abf1f7a6b1)|2018-06-28 11:01:06
|587|jonasfj|fixed tests and update yarn.lock|[URL](https://github.com/taskcluster/taskcluster-auth/commit/af206952041aab4a1e18bf460b35ad63dddc9460)|2018-06-21 12:15:36
|586|jonasfj|Merge branch 'master' of github.com:taskcluster/taskcluster-auth into complete-trie|[URL](https://github.com/taskcluster/taskcluster-auth/commit/997d97a6118c47928526b74d439eca8861a93a0f)|2018-06-21 09:45:54
|585|imbstack|Merge pull request #156 from taskcluster/longer-project-names  Increase length of project names to allow for standardizing on projectName|[URL](https://github.com/taskcluster/taskcluster-auth/commit/bed325a8efd931fa7559c7521ed0a1e6eecc0790)|2018-05-17 20:53:26
|584|imbstack|Increase length of project names to allow for standardizing on projectName|[URL](https://github.com/taskcluster/taskcluster-auth/commit/a7c7289399b4950e4ce1e646aa93662a464efa97)|2018-05-10 22:15:52
|583|imbstack|Merge pull request #155 from taskcluster/fix-sentry-stuff  Port sentry to auth tokens|[URL](https://github.com/taskcluster/taskcluster-auth/commit/1dda4bc67b1cdaee68cb0063af49298652981996)|2018-04-30 22:59:34
|582|imbstack|Port sentry to auth tokens|[URL](https://github.com/taskcluster/taskcluster-auth/commit/0ea95a41c4685cd25a7c4b58881f4711e21f8aaf)|2018-04-30 21:53:50
|581|imbstack|Merge pull request #153 from taskcluster/ingress-healthcheck  Allow auth to work in gke ingress|[URL](https://github.com/taskcluster/taskcluster-auth/commit/9732903e290eb2fa05f63461ed1fa093075cd384)|2018-04-27 21:05:30
|580|imbstack|ingress healthcheck|[URL](https://github.com/taskcluster/taskcluster-auth/commit/d0b16310e123271ac73126dc086b6fc97be2425b)|2018-04-24 17:20:05
|579|imbstack|Merge pull request #152 from taskcluster/update-hoek  Update hoek for CVE-2018-3728|[URL](https://github.com/taskcluster/taskcluster-auth/commit/c00acfab571492a7271d7a781c985816be2acd75)|2018-04-27 20:25:47
|578|imbstack|Update hoek for CVE-2018-3728|[URL](https://github.com/taskcluster/taskcluster-auth/commit/2779a3e631149f44dbd45c6cfd1a991f77cf0dbd)|2018-04-26 18:45:40
|577|djmitche|Bug 1451390 - upgrade tc-lib-docs to start publishing again; a=bstack|[URL](https://github.com/taskcluster/taskcluster-auth/commit/d0418fabc0bb1b21f8c803f2b49459f5a6b96d7b)|2018-04-25 18:22:53
|576|djmitche|Bug 1453725 - fix .git-version filename|[URL](https://github.com/taskcluster/taskcluster-auth/commit/3953c510033d507998b0657154a6f107a493915b)|2018-04-19 14:49:26
|575|tuhina2020|added paginateListClients API and tests (#148)    added paginateListClients API and tests      retry Client scan if no clients are fetched      Update list-clients response schema      Refactor retry Client scan      Tests for limit and continuationToken      update listClients tests      Remove the loop-until-results-found    @jonasfj pointed out this could lead to timeouts while searching for a  matching client.    This commit also adds some docs of the continuation functionality.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/825e845bf019049a4647755b57c5736c72851fea)|2018-04-18 21:43:38
|574|fiennyangeln|make tests run without pulse credentials (#143)    WIP to make test run without pulse credentials    It is done by creating fake helper attributes    Related to Bug 1436799      Make fake publisher    Make fake publisher by observing main.js    Related to bug 1436799       move everything outside else block      put fake:true in pulse-publisher and helper.events      Add connection loader in main      make client test work      remove hasPulseCredentials from all test    It is done by modifying the code, and done on all test that initially  needs pulse credentials, except for azure_test    Bug 1436799      fixups from rebase|[URL](https://github.com/taskcluster/taskcluster-auth/commit/bb84161847b934aec006d98aec6bd669b73a6e20)|2018-04-18 21:17:11
|573|petemoore|Merge pull request #151 from taskcluster/schema-cleanup  Cleaned up schemas to improve generated go types in taskcluster-client-go|[URL](https://github.com/taskcluster/taskcluster-auth/commit/10c20a04e99e65f9ecea0f42e8cc5244792bf27a)|2018-04-17 12:51:59
|572|djmitche|Bug 1453725 - add heroku prebuild step|[URL](https://github.com/taskcluster/taskcluster-auth/commit/b7e5e49ddb93650bf6e4005f379e9eeca8a43cc3)|2018-04-16 21:08:51
|571|djmitche|Merge pull request #150 from djmitche/bug1452000  Bug 1452000 - update to new lib-monitoring and supply project, enable�|[URL](https://github.com/taskcluster/taskcluster-auth/commit/322acf06c4d2fd1911a085cc294b2f42aa6b113e)|2018-04-16 21:00:11
|570|djmitche|Bug 1452000 - update to new lib-monitor and supply project, enable from config|[URL](https://github.com/taskcluster/taskcluster-auth/commit/a6f35e19737eed7cf4a2a7788b59ee83c95ca11a)|2018-04-13 21:59:00
|569|petemoore|Cleaned up schemas to improve generated go types in taskcluster-client-go|[URL](https://github.com/taskcluster/taskcluster-auth/commit/57a92d9eb2e6a2bc4dc92651be5d3b6f079f9044)|2018-04-16 18:15:53
|568|jonasfj|Merge pull request #146 from taskcluster/static-clients  added support for static clients|[URL](https://github.com/taskcluster/taskcluster-auth/commit/770cb1574bb85bcc1c782f9bcf845e3470c4adc5)|2018-04-12 10:14:22
|567|jonasfj|Fix comments and docs...|[URL](https://github.com/taskcluster/taskcluster-auth/commit/480d51f4dde8388cd2d84adc46a5e209adbce3de)|2018-04-11 21:02:45
|566|jonasfj|Fixed linting|[URL](https://github.com/taskcluster/taskcluster-auth/commit/83ce64b7a19adbd7e49f1f555480635fa9b35a51)|2018-04-11 17:09:57
|565|jonasfj|Added tests that we can create/remove static clients|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ee3a7b8bef24723312453e36113990a8da14cc7f)|2018-04-11 14:58:50
|564|djmitche|Merge pull request #149 from djmitche/bug1451390  Bug 1451390: write docs|[URL](https://github.com/taskcluster/taskcluster-auth/commit/5737647c8f08abee1de432a3d31b2b5e62ddf20e)|2018-04-04 18:53:13
|563|djmitche|Bug 1451390: write docs|[URL](https://github.com/taskcluster/taskcluster-auth/commit/8cfddfe7547f6f05742bec5bbd29928fa655dbdb)|2018-04-04 16:45:38
|562|djmitche|fix docs|[URL](https://github.com/taskcluster/taskcluster-auth/commit/3b8779a85f6bd9de26c8edf7dded4a61c83070f2)|2018-03-30 20:07:35
|561|jonasfj|added support for static clients|[URL](https://github.com/taskcluster/taskcluster-auth/commit/28176b01f44f922ae4685ca8d794ca3740077317)|2018-03-27 14:53:30
|560|djmitche|Merge pull request #144 from kritisingh1/upgrade  upgrade to version 8.0.0 of taskcluster-lib-api|[URL](https://github.com/taskcluster/taskcluster-auth/commit/193dd5c9641ee2450b8400071fbd5e2d5a585942)|2018-03-27 13:24:22
|559|djmitche|add a comment documenting the webhooktunnel context property|[URL](https://github.com/taskcluster/taskcluster-auth/commit/59d553084133f7814932f6a9dcc978c6f8b015cf)|2018-03-26 16:25:46
|558|djmitche|Merge pull request #145 from taskcluster/bug1441176  Bug 1441176 - add development instructions to README|[URL](https://github.com/taskcluster/taskcluster-auth/commit/27934a58b24e95cc5e49dc0ca052c47f30aeb7cc)|2018-03-26 15:55:04
|557|kritisingh1|fix tests|[URL](https://github.com/taskcluster/taskcluster-auth/commit/4ad35d1c505addf1fb4287436e9e3465c08b7ba9)|2018-03-21 16:19:33
|556|kritisingh1|upgrade to version 8.0.0 of taskcluster-lib-api|[URL](https://github.com/taskcluster/taskcluster-auth/commit/e2c8295266788ae91f736bd3574ac28178567aa8)|2018-03-21 11:20:44
|555|djmitche|Bug 1441176 - add development instructions to README|[URL](https://github.com/taskcluster/taskcluster-auth/commit/46186b6b524d9c3b34f8aa9e9ef28af86b6bb18a)|2018-03-19 00:22:26
|554|jonasfj|Updated roles used in tests|[URL](https://github.com/taskcluster/taskcluster-auth/commit/d1fc284005cae9a207c8ca6dd2d80c494e2f89b3)|2018-03-13 17:26:19
|553|djmitche|Merge pull request #142 from fiennyangeln/upgrade-lib-api  Upgrade taskcluster-lib-api|[URL](https://github.com/taskcluster/taskcluster-auth/commit/3b087a6790fc22e169475843096ea8700247f18b)|2018-03-12 18:13:19
|552|fiennyangeln|Upgrade taskcluster-lib-api  Upgrade taskcluster-lib-api to carry Access-Control-Max-Age  Related to Bug 1442636|[URL](https://github.com/taskcluster/taskcluster-auth/commit/18599c1ea57a2f5b617f60da4e2d52981ff938d2)|2018-03-09 15:27:33
|551|djmitche|fix listClients prefix regexp|[URL](https://github.com/taskcluster/taskcluster-auth/commit/04f61e6f1bfa055f2bedc0de1127ffe9555c7b10)|2018-03-08 19:27:24
|550|djmitche|Merge pull request #141 from djmitche/update-parameter-clientid-pattern  Update clientId parameter regexp|[URL](https://github.com/taskcluster/taskcluster-auth/commit/f720729f730f4f5df174949829e38bbd2a4808b1)|2018-03-08 17:01:41
|549|djmitche|Update clientId parameter regexp|[URL](https://github.com/taskcluster/taskcluster-auth/commit/cc02eb9748f82e66022ed6f1f77fdc4c1f84a13c)|2018-03-08 16:57:37
|548|jonasfj|Update documentation for roles|[URL](https://github.com/taskcluster/taskcluster-auth/commit/00955248299ca31ffc0c108825b0b82164d4b921)|2018-03-06 20:27:45
|547|djmitche|Merge pull request #139 from fiennyangeln/make-test-independent  make test skip if insufficient credentials|[URL](https://github.com/taskcluster/taskcluster-auth/commit/51a284206e86a373f797191d48051a9af749f94c)|2018-03-06 14:28:48
|546|fiennyangeln|make test skip if insufficient credentials  make test skip if the test needs pulse credentials and it is not provided. use the suite setup to skip test  Bug 1436799|[URL](https://github.com/taskcluster/taskcluster-auth/commit/f8c8cb03a5c2f90370ae0fe226a608f20d2773fe)|2018-03-03 08:49:45
|545|jonasfj|Addressed review comments with more doc strings|[URL](https://github.com/taskcluster/taskcluster-auth/commit/17ebcaf77b31c5cc4b71d8ce4f456090469c6354)|2018-03-03 02:37:01
|544|jonasfj|Removed collections package left-over|[URL](https://github.com/taskcluster/taskcluster-auth/commit/8b15c76a7c06f24145a4de4d10db82a662005626)|2018-03-03 02:27:39
|543|helfi92|Add bang symbol to the client ID schema (#137)|[URL](https://github.com/taskcluster/taskcluster-auth/commit/f46d7b8b76d7eaabd1a2a4e198a49e1686b5e2e8)|2018-03-02 14:56:48
|542|jonasfj|Re-ordered methods and fixed comments|[URL](https://github.com/taskcluster/taskcluster-auth/commit/08b155f058ee4e69043a597237592b2b334a6392)|2018-03-02 01:30:43
|541|jonasfj|Derive ScopeSetBuilder nodes from a single BaseNode|[URL](https://github.com/taskcluster/taskcluster-auth/commit/2f2acef08502eb31d3b5cf3a53a4760f23040a25)|2018-03-02 00:50:52
|540|jonasfj|remove 0x from devDeps|[URL](https://github.com/taskcluster/taskcluster-auth/commit/932a31ca9889337eae46c9efc76548d4edd5bd9f)|2018-03-02 00:44:51
|539|jonasfj|Merge branch 'master' of github.com:taskcluster/taskcluster-auth into complete-trie|[URL](https://github.com/taskcluster/taskcluster-auth/commit/6753f05d52c88ab11224bcfc7d8a5279bd644ce7)|2018-02-28 19:56:58
|538|jonasfj|Use trie to resolve all roles in one pass|[URL](https://github.com/taskcluster/taskcluster-auth/commit/faf6c27448535cf151452681a8b6ec568ce9637e)|2018-02-28 19:56:43
|537|djmitche|Merge pull request #134 from djmitche/more-parameter-cleanup  remove leftovers from the parameterized-roles transition|[URL](https://github.com/taskcluster/taskcluster-auth/commit/04ea1fa6e27c8230b555970ff8a8a298970e9e95)|2018-02-27 21:25:23
|536|imbstack|Update lib-api|[URL](https://github.com/taskcluster/taskcluster-auth/commit/44dc61eafc3454c145ec45b5b3201a76b4d2589f)|2018-02-09 18:47:58
|535|imbstack|Merge pull request #136 from taskcluster/fix-tests-with-rejecting-promises  Fix tests that use azure blob store fake|[URL](https://github.com/taskcluster/taskcluster-auth/commit/f50a16e1f44010f8dcaeef1f33edfd8efb45950d)|2018-02-08 21:33:35
|534|imbstack|Fix tests that use azure blob store fake|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ccec2cad04f8b179f659eba05044856bb404e697)|2018-02-08 21:01:24
|533|djmitche|Merge pull request #135 from djmitche/rename-to-container  Bug 1436112 - Rename blob to container|[URL](https://github.com/taskcluster/taskcluster-auth/commit/cff01d250b052b1455b50ebb1c78d05ea2c74285)|2018-02-07 16:23:18
|532|djmitche|Bug 1436112 - Fix scope for azureContainers  This method is new and only used by as-yet un-landed tc-backup code, so no migration is required.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/7b2d5ae172bebd486c40ad01c76799867465434a)|2018-02-06 21:28:35
|531|djmitche|Bug 1436112 - Rename azureBlobSAS to azureContainerSAS  Note that the HTTP path doesn't change, but the scope required does.  I have also updated all roles and clients with `auth:azure-blob:..` to have `auth:azure-container:.` too.  That's really just tc-backups.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/1ea8329c971a9ad2254901085635ea236da86d9b)|2018-02-06 21:08:17
|530|jonasfj|Fixed conflict that somehow got merged|[URL](https://github.com/taskcluster/taskcluster-auth/commit/091df91de452619afc06b5d617cf916aa5c16ce4)|2018-02-06 23:17:57
|529|jonasfj|Merge pull request #133 from taskcluster/upgrade-lib-api  Upgrade lib api|[URL](https://github.com/taskcluster/taskcluster-auth/commit/3bad0dfc2abc996097a84db0de112f9c35871090)|2018-02-06 22:14:34
|528|jonasfj|Merge branch 'master' of github.com:taskcluster/taskcluster-auth into upgrade-lib-api|[URL](https://github.com/taskcluster/taskcluster-auth/commit/1c3f3eda268a6820adb604307d04175b44cfbb02)|2018-02-06 22:14:01
|527|jonasfj|Refactored scope expressions to be prettier|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ee0efd297b499bd3bbd85a9f5058fcf2dfe012e5)|2018-02-06 22:11:21
|526|jonasfj|Moved to new tc-lib-api with scope expressions|[URL](https://github.com/taskcluster/taskcluster-auth/commit/38fe7cac6bb1fc76167b729e93f11905c707bcee)|2018-02-06 18:55:19
|525|imbstack|Merge pull request #132 from taskcluster/compile-on-osx-again  Switch lru package to fix osx compilation|[URL](https://github.com/taskcluster/taskcluster-auth/commit/2481326c0a7fd47d39defbcde1731244fcb1ba9e)|2018-02-06 17:56:35
|524|imbstack|Update audit logging|[URL](https://github.com/taskcluster/taskcluster-auth/commit/80de0de93b6477418ab0a7f4d6a6e4cab1424087)|2018-02-01 20:13:37
|523|djmitche|Merge pull request #130 from djmitche/bug1434369  Bug 1434369 - don't try to create tables / containers every time|[URL](https://github.com/taskcluster/taskcluster-auth/commit/e438fc490d2b187e40f7673be9b5c59dac53a998)|2018-02-05 17:36:20
|522|djmitche|remove broken image link|[URL](https://github.com/taskcluster/taskcluster-auth/commit/a5b0f35e843feb85eeba8e08166f65d16ca77c7e)|2018-02-05 15:48:52
|521|djmitche|Merge pull request #131 from djmitche/bug1433963  Bug 1433963 - add azureContainers|[URL](https://github.com/taskcluster/taskcluster-auth/commit/b2b2210834b4fc06983998500a824cb03eb21fe8)|2018-02-05 15:39:37
|520|imbstack|Switch lru package to fix osx compilation|[URL](https://github.com/taskcluster/taskcluster-auth/commit/06b766f19c9a65d5b9f9e67469ee47aa2ec9e75f)|2018-02-01 20:10:35
|519|djmitche|Bug 1433963 - add azureContainers|[URL](https://github.com/taskcluster/taskcluster-auth/commit/db688614e59d8f93db9cfef7b87e6f39c85fce0c)|2018-01-31 13:15:37
|518|djmitche|Bug 1434369 - don't try to create tables / containers every time  This operation occasionally times out, so let's try to do it less often.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/db83723f26a49103103679b87b0f6b552d36a300)|2018-01-30 20:28:13
|517|djmitche|Merge pull request #129 from djmitche/delete-204  Reply with a 204 when deleting roles and clients|[URL](https://github.com/taskcluster/taskcluster-auth/commit/a41f55e30ac58183cf87f78fcb2f1a7d3835e1a2)|2018-01-30 01:32:57
|516|djmitche|Merge pull request #128 from djmitche/post-expand-scopes  Use POST for expandScopes|[URL](https://github.com/taskcluster/taskcluster-auth/commit/89865c51110543bd9a0dff246d2fea20e61e83e9)|2018-01-30 01:31:17
|515|djmitche|remove leftovers from the parameterized-roles transition|[URL](https://github.com/taskcluster/taskcluster-auth/commit/6471dc1ad8ff5b4039ccebb03e41af0dda90685b)|2018-01-30 01:17:15
|514|djmitche|Reply with a 204 when deleting roles and clients|[URL](https://github.com/taskcluster/taskcluster-auth/commit/53af7c8e361d7285c21b0b7e6989a92f1e3b56ef)|2018-01-30 01:15:33
|513|djmitche|Use POST for expandScopes  Docker-worker calls the existing (GET-based) expandScopes, so that remains in place as expandScopesGet, but marked deprecated.  When docker-worker is upgraded to not use the old method, or is itself deprecated, we can remove expandScopesOld.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/b9c41cae67a7fac6756f6884350bb60af02aa3b8)|2018-01-28 17:51:57
|512|jonasfj|Merge pull request #127 from djmitche/end-periodic-tasks  Stop monitoring so that periodic tasks actually complete|[URL](https://github.com/taskcluster/taskcluster-auth/commit/4ecc3d470eb12bb69b3f73023e0118312efb676b)|2018-01-25 20:22:04
|511|djmitche|Stop monitoring so that periodic tasks actually complete  Without this in place, the timers for resource monitoring keep the Node event loop full, so it never exits.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/050454436285cdc8b3e8bbc49c10e4b464a91e4d)|2018-01-25 17:11:44
|510|jonasfj|Upgrade dependencies|[URL](https://github.com/taskcluster/taskcluster-auth/commit/e8d53031b3e8fd2882e21d7235b0bd34b0505049)|2018-01-24 21:32:36
|509|jonasfj|Upgraded to node ^8.9.0|[URL](https://github.com/taskcluster/taskcluster-auth/commit/1dd693e2d696b56952aceb1a068a2ff88455746b)|2018-01-24 21:29:52
|508|jonasfj|Merge pull request #126 from taskcluster/more-perf-tests  updated roles/clients and testing perf of resolving clients|[URL](https://github.com/taskcluster/taskcluster-auth/commit/849b0c20ab9dee41d0f62312c119b75725a98ad7)|2018-01-24 19:54:21
|507|jonasfj|New performance tests for real clients|[URL](https://github.com/taskcluster/taskcluster-auth/commit/24942137fbc7a9b3eef962bf11100ff0266e747f)|2018-01-24 19:39:41
|506|jonasfj|Lazily generate client scopes|[URL](https://github.com/taskcluster/taskcluster-auth/commit/c184533a2a50849c98087cd163e6e1fc381c878b)|2018-01-24 19:38:56
|505|jonasfj|Allow disable cache for performance tests|[URL](https://github.com/taskcluster/taskcluster-auth/commit/d3bf3209fb885f12568001338ddb94c67b3ca687)|2018-01-24 19:38:06
|504|djmitche|Merge pull request #125 from djmitche/monitor-generation  monitor trie generation and cycle checking|[URL](https://github.com/taskcluster/taskcluster-auth/commit/32eaac831f4af4a5dfbba810bcffa51d7bde0259)|2018-01-23 23:59:04
|503|djmitche|monitor trie generation and cycle checking|[URL](https://github.com/taskcluster/taskcluster-auth/commit/cf0cce9702820b4ae87730265e907b4cb3168719)|2018-01-23 23:50:47
|502|jonasfj|Merge pull request #124 from taskcluster/caching-resolver  Added LRU cache to ScopeResolver, and instrumentation|[URL](https://github.com/taskcluster/taskcluster-auth/commit/4f08d9a873220a6ae4074901a6ea0df563b41a0e)|2018-01-23 23:37:50
|501|jonasfj|Added LRU cache to ScopeResolver, and instrumentation|[URL](https://github.com/taskcluster/taskcluster-auth/commit/70158214cb15054b751d7991a6a31f24cab5051f)|2018-01-23 23:20:50
|500|petemoore|Merge pull request #123 from taskcluster/bug1431750  Bug 1431750 - add additionalProperties to schemas where missing|[URL](https://github.com/taskcluster/taskcluster-auth/commit/d402bb8d6be2041c4ddd7c14c3606b2ef3631a98)|2018-01-22 14:57:55
|499|petemoore|Bug 1431750 - add additionalProperties to schemas where missing|[URL](https://github.com/taskcluster/taskcluster-auth/commit/df068b1f6ec4ff67c95263666f295f12c528a079)|2018-01-19 16:05:51
|498|djmitche|remove lingering 'Role'|[URL](https://github.com/taskcluster/taskcluster-auth/commit/5737db03997b807a820a32ca95e6e48bd7f02791)|2018-01-19 14:11:52
|497|djmitche|Merge pull request #118 from djmitche/parameterized-roles-cleanup  remove support for Roles table|[URL](https://github.com/taskcluster/taskcluster-auth/commit/9b6bfa0f8dbe07a4ef5d3af39659060f5be6f845)|2018-01-19 13:46:36
|496|jonasfj|Merge pull request #122 from taskcluster/faster-resolver  Faster resolver|[URL](https://github.com/taskcluster/taskcluster-auth/commit/8c747a8fa508fa6c23d4a52f77247ac8d474e1a0)|2018-01-11 20:02:52
|495|jonasfj|yarn lint --fix|[URL](https://github.com/taskcluster/taskcluster-auth/commit/fad710712b58185512640a462b405ac193336fc7)|2018-01-11 19:49:50
|494|jonasfj|Tweak executeTrie to use a callback rather than building a large result array|[URL](https://github.com/taskcluster/taskcluster-auth/commit/aafb038f8cc3d9c2c3b387fbdaa475fa54b94af2)|2018-01-11 19:42:09
|493|jonasfj|Tweak timing logic in test  Notably we try to run fn() for as many iterations as it takes to fill out 3s. That way we don't run short functions quickly, and long functions still get run a few times...|[URL](https://github.com/taskcluster/taskcluster-auth/commit/102db6f11b8ea1b31ba44cebf61bacf43b6a2e51)|2018-01-11 19:37:37
|492|djmitche|log to morgan before invoking api|[URL](https://github.com/taskcluster/taskcluster-auth/commit/37d7525d595adabd86d653b1e4f2a637e298ae9c)|2018-01-09 19:37:17
|491|djmitche|Merge pull request #120 from djmitche/use-morgan  Use morgan|[URL](https://github.com/taskcluster/taskcluster-auth/commit/8bfd8296227906f4b19fcd044df7193599a51f54)|2018-01-09 19:29:40
|490|djmitche|Use morgan-debug to log requests|[URL](https://github.com/taskcluster/taskcluster-auth/commit/de7edeccc1e9f50d5cfc1ad0e076a091271ae8d8)|2018-01-09 19:21:50
|489|djmitche|remove unnecessary and incorrect `this`|[URL](https://github.com/taskcluster/taskcluster-auth/commit/4b02544c84a7fb8d040635da072f9082566ef8a6)|2018-01-08 18:24:59
|488|djmitche|Merge pull request #119 from djmitche/upstream-abs  use the upstream azure-blob-storage|[URL](https://github.com/taskcluster/taskcluster-auth/commit/a23602f96286ae68627c41865b1ecc702f3a3fb8)|2018-01-04 14:43:45
|487|djmitche|use the upstream azure-blob-storage|[URL](https://github.com/taskcluster/taskcluster-auth/commit/95cc8315cdab623fee19ff1c2052407a2e1711f9)|2018-01-03 20:06:34
|486|djmitche|remove support for Roles table|[URL](https://github.com/taskcluster/taskcluster-auth/commit/6e1ea73e6510fee180e3db09fe32fe5ba7e0de0b)|2017-12-06 20:19:30
|485|djmitche|Bug 1424743: upgrade tc-lib-scopes|[URL](https://github.com/taskcluster/taskcluster-auth/commit/1d0db61c740fcdb43b2093b0a404ea1f7102dd4e)|2017-12-20 18:36:14
|484|petemoore|Merge pull request #117 from taskcluster/clock-skew  Allow clock skew in temp creds|[URL](https://github.com/taskcluster/taskcluster-auth/commit/55fddc59d7746fe3c1d9b1f50267148688980294)|2017-12-20 15:07:49
|483|jonasfj|Allow clock skew in temp creds|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ed09e5de4307bdd870cb8c450511a9d410d1d241)|2017-12-20 12:51:17
|482|djmitche|Merge branch 'rfc48'|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ac1c904f840c4703a27f43a189725b4a7e986b04)|2017-12-07 13:47:14
|481|djmitche|Fix role loading at startup  Pass a Promise instead of a function that returns a Promise (which Promise.all will not do anything with).  Also remove redundant import of Promise.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/0fdccc131ff65750a4ea81d73425b4e63aa8b1bb)|2017-12-07 00:17:08
|480|djmitche|more logging for rolesToBlob|[URL](https://github.com/taskcluster/taskcluster-auth/commit/6bca5f2e1c3ecb8497a1d8d7b40b0f7d9b409830)|2017-12-06 21:16:14
|479|djmitche|Merge branch 'rfc48-pre'|[URL](https://github.com/taskcluster/taskcluster-auth/commit/7489b5ed159718e673f622b28e004e6cdec7683e)|2017-12-06 20:59:45
|478|djmitche|Use blob storage for roles|[URL](https://github.com/taskcluster/taskcluster-auth/commit/3c916ad24b6b18fde1323f9379641c7b64b823b6)|2017-11-22 21:36:35
|477|djmitche|temporary utilities for converting roles to blobs|[URL](https://github.com/taskcluster/taskcluster-auth/commit/f0360f3a5016dde28caf458b225e9ab36bffd272)|2017-12-06 20:58:25
|476|djmitche|Introduce blob storage for roles, but do not use it yet.  The blob stores all roles in one row, meaning that we can be sure of atomic updates to the entire set of roles.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/eb6efaea90518288fee00e25e4d28614cbdd03c0)|2017-11-22 21:36:35
|475|djmitche|vendor azure-blob-storage at ae74db9b75568519e669b3bc6d8d092b11fe8075|[URL](https://github.com/taskcluster/taskcluster-auth/commit/384f6ee9c0642be5bacf88c5af0031b39ba16a30)|2017-12-04 19:25:48
|474|djmitche|Prohibit parameterized roles with cycles  Cycles with parameterized roles can potentially cause infinite expansion; for example    a  -> assume:bc%   b  -> assume:a%d  here ax -> bcx -> acxd -> bccxd -> ...  We therefore prohibit compilation of such sets of roles and also check in REST API calls.  Note, however, that at this stage it is still possible to use the API to write such roles in a race condition, resulting in a failure of the auth service.  This will be addressed in the next commit.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/291971bdaf0e17369b8eb45bc019ce58e02950e6)|2017-11-17 00:08:54
|473|djmitche|Optimize resolver's seen tracking  Modify the resolver to keep a normalized `seen` scopeset and use the work queue to flatten recursion only for scopes that are not already satisfied by `seen`. This has a big impact on massive expansions that end up reducing to ` ` or `assume: `: once the star scope is seen, nothing else goes on the queue, so recursion peters out quickly.  The final result is the seen queue.  Times in my testing are down to <10ms for all of the "real roles" performance tests. It's 500-1000x slower for some of the pathological examples, which is about where the old solution was.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/38e5753c8b882cc4fea1a2f5089e46f4a267695e)|2017-11-28 19:24:41
|472|djmitche|Support parameterized roles (finally!)  This adds support for `<..>` in role expansions.  On execution, the portion of the input matching a final ` ` in a roleid -- or the empty string if the roleId does not end in ` ` -- substituted for `<..>`. There is a special case that if the input ends with ` ` then it consumes the rest of the scope.  Examples, given role `assume:ab  -> de<..>f, gh<..>`:     `assume:abc -> decf ghc`    `assume:abcd  -> decd , ghcd `    `assume:ab  -> de , gh `    `assume:a  -> de , gh `|[URL](https://github.com/taskcluster/taskcluster-auth/commit/cc00bda452d142f1f2570db127fdfe5f5ea651c5)|2017-11-20 20:08:47
|471|djmitche|[refactor] update resolver generation and execution  The core of resolution was not and is not a DFA -- it's just a Trie. That is now cleaned up and shipped off to its own module.  It's also simplified, in that it no longer represents recursive expansion.  Very soon (parameterized roles) such a thing will be impossible.  Resolver execution is also substantially refactored: instead of searching for a fixed point, which soon will not exist, excution involves a recursive expansion of roles.  The recursion is flattened into a queue, with the scopes added to the queue becoming the result. This is a different interface than before, so there is some compatibility in place that will be removed later with a refactor of scoperesolver.js.  That will also entail a move of the remainder of dfa.js into scoperesolver.js.  This new approach changes performance drastically: initial generation of a resolver is quite a bit faster, but execution is 10-100x slower.  The worst cases are those that involve recursing over just about every role, only to normalize to a very short list of scopes.  The trie execution return value is a little unusual, but the purpose will become clear soon enough.  This also consolidates the various tests for scoperesolver.js.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/aed51d57fe2b6acc4e52b51d522106dfad07efd2)|2017-11-14 22:42:52
|470|djmitche|[refactor] drop unused grantsRole functionality|[URL](https://github.com/taskcluster/taskcluster-auth/commit/9a51753a74304959b223efaa5c7b4f772367b504)|2017-11-22 17:53:39
|469|djmitche|[refactor] use functions from tc-lib-scopes|[URL](https://github.com/taskcluster/taskcluster-auth/commit/667f96bfef698b5b7237ca4867514ab8ce4b0291)|2017-11-22 14:56:02
|468|djmitche|Fix typo in error code|[URL](https://github.com/taskcluster/taskcluster-auth/commit/18ab3ddc7a68ba8cf415918d0420c5a60844fbe8)|2017-12-06 19:49:11
|467|djmitche|Merge pull request #115 from djmitche/lock-roles  Temporarily allow "locking" roles|[URL](https://github.com/taskcluster/taskcluster-auth/commit/0803a98b9744a73d3999b0099644253beff725ee)|2017-12-06 20:19:54
|466|djmitche|Temporarily allow "locking" roles  This will be used to allow duplicating roles between Azure tables and blob storage without concern that we will miss an update.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/5d3a1089c5c45451dd6f15b219953ebcbb9a69bb)|2017-12-06 19:25:30
|465|imbstack|Merge pull request #112 from taskcluster/spring-cleaning  Spring cleaning|[URL](https://github.com/taskcluster/taskcluster-auth/commit/46032812b75e0ca9317d344f473c4a4d57a7eeb2)|2017-11-27 20:56:48
|464|djmitche|Merge pull request #113 from djmitche/cleanup  General Cleanup|[URL](https://github.com/taskcluster/taskcluster-auth/commit/e7f9bb59a5899643ab6254fe459d963b594b2943)|2017-11-22 19:12:37
|463|djmitche|[tests] remove unused imports in rolelogic_test|[URL](https://github.com/taskcluster/taskcluster-auth/commit/642aa2020d156d9d0d9f4474a4f49f82bbf0083b)|2017-11-22 14:58:06
|462|djmitche|[tests] Add a test to demonstrate that sorting is specific to  terminal  stars  Specifically, 'foo ' sorts before 'foo', but 'foo abc' does not.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/941df2f91186a007ea17cd14b591669086ff5e06)|2017-11-14 17:40:21
|461|djmitche|[tests] Add code to measure performance of DFA/resolver  When MEASURE_PERFORMANCE is set, this will measure the performance of some interesting cases and record the results in a JSON file. The intent is that these results can be compared across changes to the resolver.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/2d8e9341fa3ca5990f783fbac537010b3238bb3b)|2017-11-16 00:35:48
|460|djmitche|[tests] Make client_test tests independent of one another  With this change, the tests in this file do not depend on one another, making them easier to debug and run individually.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/226c6a0cfdce3b4354da11a5bfe86cc21cbf5586)|2017-11-21 23:14:25
|459|djmitche|[tests] Add suites to dfa_test.js  This helps navigate the output, and also allows testing one suite at a time with `.skip`.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/05b31dbc7d50116941dfbd140fa7abab40ff4afe)|2017-11-10 21:26:59
|458|djmitche|[docs] Add docs of existing clients, scopes, roles  This is largely copied from   https://docs.taskcluster.net/manual/design/apis/hawk and that section of the documentation will need to be edited to point here.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/f4c037dc46a993aadc95a6b177225c40a50fed99)|2017-11-22 14:39:17
|457|imbstack|Update travis for node 8|[URL](https://github.com/taskcluster/taskcluster-auth/commit/d2da824dda1c6e2d660ae66c67fb8dbe0825d4ba)|2017-11-15 01:38:30
|456|imbstack|Update mocha and add --exit to mocha opts  The --exit is needed for now because taskcluster-lib-loader does not provide a way for us to reach in and call close() on pulse-publisher we provide to taskcluster-lib-api. It would be possible to do with overwrites, but would result in a lot of extra fuss for little gain.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/d374a5b987bec8e39f5ef3fd3c210f6474286354)|2017-11-15 01:35:37
|455|imbstack|Update dependencies|[URL](https://github.com/taskcluster/taskcluster-auth/commit/71a2e20c7bd8fc068b67ecf8a7a0628b897898f7)|2017-11-15 00:34:48
|454|imbstack|Remove cryptiles|[URL](https://github.com/taskcluster/taskcluster-auth/commit/4ece45d1ab4f5e3e340bb7340e377d84ff16f210)|2017-11-15 00:04:25
|453|imbstack|Remove aws-sdk-promise|[URL](https://github.com/taskcluster/taskcluster-auth/commit/806497bc1591fc7222853803210114fd36f16312)|2017-11-14 23:36:24
|452|imbstack|Remove superagent-promise|[URL](https://github.com/taskcluster/taskcluster-auth/commit/31130671f3e72ee972df7421f005b3f968c45154)|2017-11-14 22:57:08
|451|imbstack|Remove compilation|[URL](https://github.com/taskcluster/taskcluster-auth/commit/bc1551f3847abb0c06e90142fafbbfb47b75b54a)|2017-11-14 21:15:51
|450|imbstack|Add linting|[URL](https://github.com/taskcluster/taskcluster-auth/commit/d37c252a8832664cf85b42127383103faacaa151)|2017-11-14 21:09:01
|449|djmitche|Merge pull request #109 from djmitche/bug1382716  Bug 1382716 - allow + and \| in clientId|[URL](https://github.com/taskcluster/taskcluster-auth/commit/e7517fddeb0615ab80472be75919adf4c0f1b68a)|2017-08-29 14:34:36
|448|djmitche|Bug 1382716 - allow + and \| in clientId|[URL](https://github.com/taskcluster/taskcluster-auth/commit/57e7da04fe0a49cba8347fd44e4927f36ac4c05f)|2017-08-28 13:24:37
|447|djmitche|Merge pull request #108 from djmitche/spelling  Spell Taskcluster|[URL](https://github.com/taskcluster/taskcluster-auth/commit/c3d24f57e2972ccae8f02931e4f5f284ca4174ce)|2017-07-17 21:07:56
|446|djmitche|Spell Taskcluster|[URL](https://github.com/taskcluster/taskcluster-auth/commit/f3975c2b4e3f4d89ddea448f9abdc2b005d75eec)|2017-07-17 16:51:37
|445|imbstack|Update yarn and node|[URL](https://github.com/taskcluster/taskcluster-auth/commit/73b5b8c1ae85a9d79dc7caadfab1a226a519614f)|2017-07-13 23:47:28
|444|jonasfj|Merge pull request #107 from ckousik/whtunnel  Added webhooktunnel endpoint|[URL](https://github.com/taskcluster/taskcluster-auth/commit/6518986319d594f75c8d7df4f80b7145a976af1e)|2017-07-06 17:49:51
|443|ckousik|removed trailing whitespace main.js:51|[URL](https://github.com/taskcluster/taskcluster-auth/commit/508ba362502ce0a2207a69413484748c510a81b8)|2017-07-05 22:56:03
|442|ckousik|yarn lock|[URL](https://github.com/taskcluster/taskcluster-auth/commit/587424bf80a01ff36fc82491b9da5e42179ffb74)|2017-06-30 21:07:45
|441|ckousik|made requested changes|[URL](https://github.com/taskcluster/taskcluster-auth/commit/3d1836ad55b662da1dd0336f115316222c2fe59e)|2017-06-30 20:54:21
|440|ckousik|Added webhooktunnel endpoint|[URL](https://github.com/taskcluster/taskcluster-auth/commit/bf87ab9cfe50b868481b46471421e83f5f72d6fa)|2017-06-30 17:05:22
|439|imbstack|Merge pull request #106 from taskcluster/bug-1361169  Move sentry to mozilla hosted instance|[URL](https://github.com/taskcluster/taskcluster-auth/commit/2ba831f62ec88b0216b8624024c55cdf605dd5ed)|2017-05-16 19:47:45
|438|imbstack|Move sentry to mozilla hosted instance|[URL](https://github.com/taskcluster/taskcluster-auth/commit/32cc80000f364e22a0200dc372b85ab57d43f6eb)|2017-05-16 17:56:48
|437|imbstack|Merge pull request #105 from taskcluster/add-version-to-logs  Add version to audit logs|[URL](https://github.com/taskcluster/taskcluster-auth/commit/a1d8a6b197371841a0e073ec9418f2656a2f1b74)|2017-04-25 20:46:27
|436|imbstack|Add version to audit logs|[URL](https://github.com/taskcluster/taskcluster-auth/commit/bf15f480f935af580435c5beb620c7af013d57ea)|2017-04-25 20:33:28
|435|imbstack|Merge pull request #102 from taskcluster/logs-to-s3  Add audit log|[URL](https://github.com/taskcluster/taskcluster-auth/commit/7805950475ae4a60293fee2893cde03106c4663b)|2017-04-25 20:18:43
|434|imbstack|Add audit log for authenticateHawk|[URL](https://github.com/taskcluster/taskcluster-auth/commit/d299e27d6ec5c252c9716275db854ff26a84802f)|2017-03-28 00:08:52
|433|imbstack|Merge pull request #104 from taskcluster/bump-lib-api  Bump lib-api to reduce auth load|[URL](https://github.com/taskcluster/taskcluster-auth/commit/4fe83bd8bbb7342dd179cfecbc7afa145da264e6)|2017-04-17 17:12:17
|432|imbstack|Bump lib-api to reduce auth load|[URL](https://github.com/taskcluster/taskcluster-auth/commit/3002d960116e92f27a287e4e45f732a3b4d96f2f)|2017-04-14 21:07:27
|431|imbstack|Merge pull request #103 from taskcluster/update-azure-entities-to-2  Use azure-entities 2.0.0|[URL](https://github.com/taskcluster/taskcluster-auth/commit/fdec1c19075759c1a6c175a84c88d6d855f1773f)|2017-04-12 16:23:56
|430|imbstack|Use azure-entities 2.0.0|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ba54ef77efe2d8d3953cbe72f2d3abbcc221cb0e)|2017-04-12 00:01:34
|429|djmitche|doc that we do not do user authentication|[URL](https://github.com/taskcluster/taskcluster-auth/commit/d345d899f9e4046e67fa10b7164fbbe3da244c05)|2017-04-07 17:33:18
|428|djmitche|Merge pull request #101 from djmitche/level-docs  describe 'level' each time it is referenced|[URL](https://github.com/taskcluster/taskcluster-auth/commit/d5fca8266da7b7ba7a738f887be0d7d465b4a2bf)|2017-03-30 19:33:44
|427|djmitche|describe 'level' each time it is referenced  This also removes some languge about not specifying a level, that seems to refer to an endpoint that doesn't exist.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/a086a4d8b76fbb116f6b9e456f51dad56c116ed7)|2017-03-30 18:14:41
|426|djmitche|use the project name from package.json|[URL](https://github.com/taskcluster/taskcluster-auth/commit/972e09424a9e04385d8c888fd5fe232a917f7b7a)|2017-03-21 15:01:21
|425|djmitche|ws change to force rebuild of buildpack|[URL](https://github.com/taskcluster/taskcluster-auth/commit/87ee53010a737c81d21c48277de5f9b6a5155dc0)|2017-03-16 18:31:21
|424|djmitche|Merge pull request #100 from djmitche/use-reportError  use res.reportError instead of res.status|[URL](https://github.com/taskcluster/taskcluster-auth/commit/255f6646a34f805eaede2e6f733b530488bf1164)|2017-03-16 15:50:20
|423|djmitche|use res.reportError instead of res.status|[URL](https://github.com/taskcluster/taskcluster-auth/commit/a0e725131f4b1abc67418b0f179520a1f63bd0eb)|2017-03-16 15:48:32
|422|imbstack|Merge pull request #99 from taskcluster/yarnification  Move to yarn|[URL](https://github.com/taskcluster/taskcluster-auth/commit/75dfe79b877e1d5da0b43e0c4477630f1befee30)|2017-03-09 22:45:25
|421|imbstack|Merge pull request #98 from taskcluster/bucket-overrides  Allow overriding buckets for redeploying|[URL](https://github.com/taskcluster/taskcluster-auth/commit/8e11df2ca87420c9e8029a77de0db023260dc22d)|2017-03-09 22:39:03
|420|imbstack|Move to yarn|[URL](https://github.com/taskcluster/taskcluster-auth/commit/c625a86c4638a875b97820b93c9ae546084e06f5)|2017-03-07 23:41:20
|419|djmitche|add service owner|[URL](https://github.com/taskcluster/taskcluster-auth/commit/e599ba7daff91926500cc26834d2b660ed3fee27)|2017-03-07 16:56:04
|418|imbstack|Allow overriding buckets for redeploying|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ca070f1718747d482bfc8d6c873f3102760dee6c)|2017-03-06 08:14:06
|417|jonasfj|Fix tests not running|[URL](https://github.com/taskcluster/taskcluster-auth/commit/82bc99e2bf723ddcac402dac1b99d98ad7a84d4d)|2017-02-28 18:01:33
|416|jonasfj|Updated npm-shrinkwrap.json|[URL](https://github.com/taskcluster/taskcluster-auth/commit/aecca20e9aea91e16de359b9fbd3b942c9e1e9cb)|2017-02-28 17:34:28
|415|jonasfj|Merge pull request #94 from elenasolomon/azure-blob-access  Azure blob access|[URL](https://github.com/taskcluster/taskcluster-auth/commit/e4d5660f4f5346597ff21dd57fcae31aef1c85e9)|2017-02-28 16:21:26
|414|elenasolomon|creates a helper method to set authorized scopes|[URL](https://github.com/taskcluster/taskcluster-auth/commit/e647e301e3e1b8cd92673503b8e297eaa7a0a25a)|2017-02-27 20:03:00
|413|elenasolomon|- changed the error from InvalidRequestArguments in ResourceNotFound - corrects some unit tests|[URL](https://github.com/taskcluster/taskcluster-auth/commit/91811dce210aa342388a27b6fce653658cfe5f5b)|2017-02-27 10:00:44
|412|elenasolomon|res.reportError insteadof res.status|[URL](https://github.com/taskcluster/taskcluster-auth/commit/9a598b1ed62752fee762460d08eb78423b11eadb)|2017-02-24 16:16:57
|411|elenasolomon|fixes the container regex pattern|[URL](https://github.com/taskcluster/taskcluster-auth/commit/3c836152cab479fa467c1adbecb593119ebfa5f6)|2017-02-24 16:06:53
|410|elenasolomon|integrate changes requested in code review|[URL](https://github.com/taskcluster/taskcluster-auth/commit/356eb99fb88012afb5a263015a204f2c99c118b1)|2017-02-24 13:12:47
|409|elenasolomon|changed the version of the fast-azure-storage library|[URL](https://github.com/taskcluster/taskcluster-auth/commit/b52858d5b858541ddaf266f8a4470683cdae7d6d)|2017-02-22 14:34:39
|408|elenasolomon|removes .only from azure tests|[URL](https://github.com/taskcluster/taskcluster-auth/commit/93921d254234b18e3d49b2bb0c3323deb851c369)|2017-02-21 08:41:34
|407|elenasolomon|Integrate the changes requested in the code review|[URL](https://github.com/taskcluster/taskcluster-auth/commit/5a2a074ac7a2f9fabc77ed9b0f5ffd540f146307)|2017-02-21 08:39:49
|406|elenasolomon|changes the scope to:  auth:azure-blob:<level>:<account>/<container>|[URL](https://github.com/taskcluster/taskcluster-auth/commit/931d0a50eeee70dc01474be9a7f4a490bdb71f7e)|2017-02-20 15:45:29
|405|elenasolomon|removes '.only' from azure test suite|[URL](https://github.com/taskcluster/taskcluster-auth/commit/10c4478b5f3789f864b1784e5dd6792484843798)|2017-02-10 08:59:22
|404|elenasolomon|small correction to a schema description|[URL](https://github.com/taskcluster/taskcluster-auth/commit/619a8c1805119edd6b54906dfd32ec12da98bb10)|2017-02-09 12:40:22
|403|elenasolomon|Add an API endpoint for getting a SAS string for use with a specific Azure Blob Storage container|[URL](https://github.com/taskcluster/taskcluster-auth/commit/bee99cc9034c9a5cb9a8d8773f44968253f4a71f)|2017-02-09 12:28:41
|402|imbstack|Merge pull request #97 from taskcluster/allow-rw-to-grant-ro  Allow azure read-write access to grant read-only as well|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ce1f509c11179875674a7c548ca07fd0e8db20ac)|2017-02-23 16:33:45
|401|imbstack|Allow azure read-write access to grant read-only as well|[URL](https://github.com/taskcluster/taskcluster-auth/commit/b8ea5b65a1dcba08fd332568b20ba3b9ac20db7f)|2017-02-22 23:01:16
|400|imbstack|Merge pull request #92 from taskcluster/list-azure-stuff  Add table listing abilities to azure manager|[URL](https://github.com/taskcluster/taskcluster-auth/commit/46aa7176bf53d34bc2b7601e2c4f9ee36ae5515e)|2017-02-22 19:24:38
|399|imbstack|Add ability to list managed accounts and tables|[URL](https://github.com/taskcluster/taskcluster-auth/commit/6814be040946675ff0b332f1cc147e9a709b99e4)|2017-02-22 00:15:45
|398|imbstack|Merge pull request #96 from taskcluster/fix-rw-azure  Fixes from PR I forgot to push before merging PR|[URL](https://github.com/taskcluster/taskcluster-auth/commit/9b7031eaecad71d065f8bddd71b1905eb7887eca)|2017-02-21 23:51:06
|397|imbstack|Fixes from PR I forgot to push before merging PR|[URL](https://github.com/taskcluster/taskcluster-auth/commit/b21dccfb2a47cc6f327097767f926e473e7b34de)|2017-02-21 23:13:59
|396|imbstack|Merge pull request #91 from taskcluster/read-write-azure  Add level to azure sas creds|[URL](https://github.com/taskcluster/taskcluster-auth/commit/b0abd3c065dd6833d15c05aa7f60e6ae9eca626b)|2017-02-21 23:11:40
|395|jonasfj|Merge pull request #95 from djmitche/spellos  fix spelling errors|[URL](https://github.com/taskcluster/taskcluster-auth/commit/7465d9bcc3fadad32ef51106045513c50fce2410)|2017-02-14 18:20:46
|394|djmitche|fix spelling errors|[URL](https://github.com/taskcluster/taskcluster-auth/commit/323fc35a22446c3e65a84db1a4883608a5819016)|2017-02-14 18:10:08
|393|imbstack|Add level to azure sas creds|[URL](https://github.com/taskcluster/taskcluster-auth/commit/211e297472125f08bef7761f3b32f513a1c109fc)|2017-02-03 19:54:23
|392|djmitche|Merge pull request #93 from taskcluster/simplify-config  Removed unused config variables|[URL](https://github.com/taskcluster/taskcluster-auth/commit/13a32d6635b585fc8a6b4ea060baf7235bd8a956)|2017-02-09 22:09:58
|391|jonasfj|Removed unused config variables|[URL](https://github.com/taskcluster/taskcluster-auth/commit/f4114f2b6b72e299a6e485cf2ccae0ec1c111b51)|2017-02-09 01:28:32
|390|djmitche|Merge pull request #89 from taskcluster/optional-autoexpire  Add support for optional client autoexpire|[URL](https://github.com/taskcluster/taskcluster-auth/commit/442145d92ff92802206d6d93b94b199c05f3274e)|2017-02-01 19:22:18
|389|jonasfj|lastDataUsed -> lastDateUsed  Caught in testing by `Entity.types.Schema`, so we know it works :)|[URL](https://github.com/taskcluster/taskcluster-auth/commit/8da31f06de260a7a77645d700b72d602857c13a6)|2017-02-01 18:59:40
|388|jonasfj|Updated npm shrinkwrap|[URL](https://github.com/taskcluster/taskcluster-auth/commit/d919305527d97d21ef34da00ad159b4801a072f4)|2017-02-01 18:39:54
|387|jonasfj|Bumped azure-entities  We'll also have to updated npm-shrinkwrap.json|[URL](https://github.com/taskcluster/taskcluster-auth/commit/51a6f0ea4e81a4d8836ef7008f64ba9fdd06d21b)|2017-02-01 18:34:14
|386|jonasfj|Use Entity.types.Schema to enforce details|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ad91016d5dbc2944cd4e7f0a6d1cc27bb1f33175)|2017-02-01 18:33:02
|385|djmitche|Add a deleteOnExpiration property to clients and purge|[URL](https://github.com/taskcluster/taskcluster-auth/commit/13489725b6cb3a487128db0559ef5dc176e084c6)|2017-01-22 20:53:46
|384|djmitche|remove unused schema file|[URL](https://github.com/taskcluster/taskcluster-auth/commit/501235f82c055d81b71d7d1f5262c7cffc275c24)|2017-01-22 20:54:23
|383|imbstack|Merge pull request #88 from taskcluster/bump-pulse  Upgrade taskcluster-client + pulse-publisher|[URL](https://github.com/taskcluster/taskcluster-auth/commit/3abead371644082252f8c0181f07bb04053ebffb)|2017-01-25 00:24:12
|382|jonasfj|Upgrade taskcluster-client + pulse-publisher|[URL](https://github.com/taskcluster/taskcluster-auth/commit/d1d08d9cec5fbbdf6b8d2dfda96f7e10431ee9e8)|2017-01-24 22:21:31
|381|djmitche|Merge pull request #87 from djmitche/bug1242473  Bug 1242473: better handling of scopes when updating roles|[URL](https://github.com/taskcluster/taskcluster-auth/commit/dcf5dffb8ce9a4de42ddc05e0bff7619794844a8)|2017-01-20 20:06:56
|380|jonasfj|Merge pull request #86 from taskcluster/bump-pulse-publisher  Bump pulse-publisher|[URL](https://github.com/taskcluster/taskcluster-auth/commit/b991a32185ebcdca6f6fcefbd5229df4e9d974e3)|2017-01-19 21:10:29
|379|jonasfj|oneOf -> anyOf, also added type: string|[URL](https://github.com/taskcluster/taskcluster-auth/commit/7a09cd613b933f7608c70be5c7a147cc3e1f3beb)|2017-01-19 20:45:48
|378|djmitche|handle scopes better for updating roles|[URL](https://github.com/taskcluster/taskcluster-auth/commit/bdaafb831cddf611eaa4a0c2842c4e8d1473eb8f)|2017-01-19 16:29:26
|377|djmitche|Add tests for scope checks when updating roles|[URL](https://github.com/taskcluster/taskcluster-auth/commit/e2ea7212a5e872d52a584b0902d606aa941fb09d)|2017-01-19 01:05:01
|376|jonasfj|Bump pulse-publisher|[URL](https://github.com/taskcluster/taskcluster-auth/commit/1b71d45b03968364ef477d10373ec47f3f135dc5)|2017-01-19 01:21:20
|375|djmitche|Merge taskcluster/taskcluster-auth:add-lib-docs (PR #85)|[URL](https://github.com/taskcluster/taskcluster-auth/commit/dc5672b95b56b9385731acaf960538b65b6bfda9)|2016-11-18 13:06:31
|374|imbstack|Add lib-docs|[URL](https://github.com/taskcluster/taskcluster-auth/commit/f8a8d9924f4670a2457e746a828971d7ab2e6754)|2016-11-17 00:42:57
|373|jonasfj|Merge pull request #84 from taskcluster/bug-1316698  Bug 1316698 - EC2 metadata compat|[URL](https://github.com/taskcluster/taskcluster-auth/commit/a613065de514f21c67efe7dc326f1f0665432f61)|2016-11-11 21:55:05
|372|imbstack|Merge pull request #83 from taskcluster/travis-node-6  use node 6 on travis|[URL](https://github.com/taskcluster/taskcluster-auth/commit/be0b9a221e76d53f91159c950aa1019887ba3ea5)|2016-11-11 21:10:03
|371|jonasfj|Bug 1316698 - EC2 metadata compat|[URL](https://github.com/taskcluster/taskcluster-auth/commit/6f8a84373fc33870cd144ca96865488a00650f6f)|2016-11-11 00:25:05
|370|jonasfj|Merge pull request #60 from taskcluster/improving-readability  Improve readability|[URL](https://github.com/taskcluster/taskcluster-auth/commit/00aad5ff118b6ccf4b2dea698943fa3226ff4e72)|2016-11-08 23:33:35
|369|jonasfj|use node 6 on travis|[URL](https://github.com/taskcluster/taskcluster-auth/commit/d543cfe0a52610a87498594c25f9b8dc9273223e)|2016-11-08 23:31:45
|368|djmitche|Merge taskcluster/taskcluster-auth:bug-1242753 (PR #81)|[URL](https://github.com/taskcluster/taskcluster-auth/commit/e3f6ebaca27ecae79af76ca1076e35d7c90a1a6d)|2016-10-25 18:00:29
|367|djmitche|Merge taskcluster/taskcluster-auth:newPing (PR #82)|[URL](https://github.com/taskcluster/taskcluster-auth/commit/2e15e5e772b8fb18e21fb155a592d579177103ee)|2016-10-24 13:50:11
|366|owlishDeveloper|lib-api v.3.0.0|[URL](https://github.com/taskcluster/taskcluster-auth/commit/50e4c733809f3cd1b39791b361cd7f88ae78cfab)|2016-10-21 20:43:16
|365|owlishDeveloper|Corrected typo in v1|[URL](https://github.com/taskcluster/taskcluster-auth/commit/2769c7afeb234661620ef9004d8b50ab46471981)|2016-10-21 20:16:01
|364|owlishDeveloper|Removed commas|[URL](https://github.com/taskcluster/taskcluster-auth/commit/c0a33340e13616e79d8b1f3f6ad5ad7ba6cc7f13)|2016-10-21 18:45:26
|363|owlishDeveloper|Synced with master|[URL](https://github.com/taskcluster/taskcluster-auth/commit/df70ce83910a4e8ca1b3befacff540933a761348)|2016-10-21 18:08:05
|362|owlishDeveloper|Check reference object 3|[URL](https://github.com/taskcluster/taskcluster-auth/commit/6a4533cc5fb9729f2844bb34853d5cd80c1a6989)|2016-10-21 04:29:44
|361|owlishDeveloper|Check reference object 2|[URL](https://github.com/taskcluster/taskcluster-auth/commit/1708cf8a91ea4ab4cd2f8ab72d8c78023a9283a9)|2016-10-21 04:26:33
|360|owlishDeveloper|Check reference object|[URL](https://github.com/taskcluster/taskcluster-auth/commit/431c4a6357c48334189af649fb754ff366312a99)|2016-10-21 04:23:27
|359|owlishDeveloper|Try to see if ping is in the reference|[URL](https://github.com/taskcluster/taskcluster-auth/commit/827639a817b15d6916b667514de2ef9b894b9a87)|2016-10-21 04:11:15
|358|owlishDeveloper|Removed old ping|[URL](https://github.com/taskcluster/taskcluster-auth/commit/84f419f0326be3ac1e8865e54834656404441e23)|2016-10-20 23:43:03
|357|owlishDeveloper|Revert millichange in data.js|[URL](https://github.com/taskcluster/taskcluster-auth/commit/4675b2d54ebfacad1106f26a5c06c9e70ebe3b0a)|2016-10-20 19:59:51
|356|djmitche|Merge pull request #80 from djmitche/put-object-acl  add note to the docs about PutObjectAcl|[URL](https://github.com/taskcluster/taskcluster-auth/commit/e3e390d6ef948ccdbbca139aa9b0e282aa4898f2)|2016-10-20 19:53:32
|355|djmitche|Merge pull request #1 from djmitche/put-object-acl-2  Minor formatting proposal|[URL](https://github.com/taskcluster/taskcluster-auth/commit/0e6b90f52e5bb72920577738dd9dac223161867d)|2016-10-20 19:53:07
|354|owlishDeveloper|Millichange in data.js|[URL](https://github.com/taskcluster/taskcluster-auth/commit/30b19813e02477a4895c218d723111d8e1f94c86)|2016-10-20 19:51:22
|353|owlishDeveloper|.expandedScopes() is back|[URL](https://github.com/taskcluster/taskcluster-auth/commit/f61e9ac457cc3079bb5977e299212a60984fa9cf)|2016-10-20 18:55:33
|352|owlishDeveloper|Accidental reset restored|[URL](https://github.com/taskcluster/taskcluster-auth/commit/d58a72e133b5474fe559983c3d1e91611e5d8581)|2016-10-20 18:13:27
|351|owlishDeveloper|Merge branch 'bug-1242753' of github.com:taskcluster/taskcluster-auth into bug-1242753  Merging after accidental reseting|[URL](https://github.com/taskcluster/taskcluster-auth/commit/8cb7e98e76ca806e90d03b855cbeba6ae7997f94)|2016-10-20 18:01:48
|350|owlishDeveloper|Changed main.js|[URL](https://github.com/taskcluster/taskcluster-auth/commit/eec45e86517fd3e538fa1f01a0893b05c086d96b)|2016-10-20 18:01:39
|349|jonasfj|Minor formatting proposal|[URL](https://github.com/taskcluster/taskcluster-auth/commit/c6d0e63d281f1cd83fbb99cd21ad4b1aed01cfec)|2016-10-20 17:53:08
|348|djmitche|add note to the docs about PutObjectAcl  ..since this trips me up EVERY TIME|[URL](https://github.com/taskcluster/taskcluster-auth/commit/5052757db8c3bf452a520ba37c42546e2e8eeb51)|2016-10-20 01:12:40
|347|owlishDeveloper|Solution v.0.3|[URL](https://github.com/taskcluster/taskcluster-auth/commit/0bad7d0c2efa2cb699e8b0a5d52cd72f4bce286f)|2016-10-20 00:18:28
|346|owlishDeveloper|Solution v.0.2|[URL](https://github.com/taskcluster/taskcluster-auth/commit/1389e3057f07818262201d5ee0afc9eaa9a526d7)|2016-10-19 22:14:37
|345|owlishDeveloper|solution v.0.1|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ab5f1a7fc5616f101fdfc527558a0e6c783fbb37)|2016-10-19 03:49:06
|344|djmitche|Merge pull request #77 from owlishDeveloper/bug-1262612  Changed ping() description|[URL](https://github.com/taskcluster/taskcluster-auth/commit/23170cad5ac45712dd9d92e17cd92a55c4a185cc)|2016-10-14 13:39:57
|343|owlishDeveloper|Changed stability level to Stable|[URL](https://github.com/taskcluster/taskcluster-auth/commit/5b4d9f1d877cce7e1c670ed3392b389f190ab2a9)|2016-10-13 23:37:15
|342|owlishDeveloper|Changed ping() description|[URL](https://github.com/taskcluster/taskcluster-auth/commit/c8ac62868c85192a850d164cd847ec32dd13fa5f)|2016-10-12 23:53:39
|341|djmitche|Merge pull request #76 from taskcluster/execute-dfa  Added executeDFA hopefully solving memory issues|[URL](https://github.com/taskcluster/taskcluster-auth/commit/bad9f5588d87cfdc445fbfb9047543cf45467fb8)|2016-10-05 19:03:33
|340|jonasfj|Moved compileDFA to separate file|[URL](https://github.com/taskcluster/taskcluster-auth/commit/2907be88d936f0b1d8f288a726ed68799314048b)|2016-10-05 19:01:55
|339|jonasfj|More comments at request of @imbstack|[URL](https://github.com/taskcluster/taskcluster-auth/commit/1bf75413aff05f4d5c7eaf896a6601f64a07a023)|2016-10-05 18:19:04
|338|jonasfj|Added executeDFA hopefully solving memory issues|[URL](https://github.com/taskcluster/taskcluster-auth/commit/5b4aa08c9c990fe01e15ad370db49219c0e2700d)|2016-10-04 17:56:04
|337|djmitche|Merge djmitche/taskcluster-auth:bug1302753 (PR #75)|[URL](https://github.com/taskcluster/taskcluster-auth/commit/f664edae61ab4c370d099b57865679a57d96ffcb)|2016-10-04 17:18:38
|336|djmitche|Bug 1302753: log all successful authentications; r?jonasfj  This logs messages like ``` Authenticated mozilla-user/dmitchell@mozilla.com for PUT access to https://localhost:60551/v1/clients/nobody%2Fsds%3Aad_asd%2Fdf-sAdSfchsdfsdfs%2Fbb%2F1 ```|[URL](https://github.com/taskcluster/taskcluster-auth/commit/8417ab0280457c00714e30556cc153925445f609)|2016-10-03 22:10:42
|335|jonasfj|Merge pull request #74 from taskcluster/fix-scope-implication  S3: read-write implies read-only|[URL](https://github.com/taskcluster/taskcluster-auth/commit/c6cce15bc13b9ec36134c6a69c74cc8d41b12540)|2016-10-03 17:43:05
|334|jonasfj|S3: read-write implies read-only|[URL](https://github.com/taskcluster/taskcluster-auth/commit/0f1ecb519a725a3a7472e8cd04b333fea885168b)|2016-10-03 17:33:24
|333|imbstack|Merge pull request #73 from taskcluster/update-monitor  Updated tc-lib-monitor|[URL](https://github.com/taskcluster/taskcluster-auth/commit/7be41bad7a37c405d36f63549dbee9224a2c823f)|2016-09-29 21:46:03
|332|jonasfj|Updated tc-lib-monitor|[URL](https://github.com/taskcluster/taskcluster-auth/commit/f4c85544288d0fc051548130150d38c21260ea2f)|2016-09-29 21:22:06
|331|imbstack|Merge pull request #72 from taskcluster/upgrade-libs  Upgraded libraries (api)|[URL](https://github.com/taskcluster/taskcluster-auth/commit/767758eaa917d444b370cf40b489fc00bbc83848)|2016-09-28 21:57:28
|330|jonasfj|Upgraded libraries (api)|[URL](https://github.com/taskcluster/taskcluster-auth/commit/210b12a3c3940c50d307a37e22aa9a5e4d027552)|2016-09-28 21:55:39
|329|imbstack|Merge pull request #70 from taskcluster/dns-typo  DNS -> DSN typo, credits @imbstack|[URL](https://github.com/taskcluster/taskcluster-auth/commit/319a1cd8b837b5db71f9c20aff085558149bab3a)|2016-09-27 19:12:16
|328|imbstack|Merge pull request #71 from taskcluster/imbstack-patch-1  Reverse monitor setup functions|[URL](https://github.com/taskcluster/taskcluster-auth/commit/8064c2fbf9d538c398c39ab05fb1f8c044d532fc)|2016-09-27 18:57:29
|327|imbstack|Reverse monitor setup functions|[URL](https://github.com/taskcluster/taskcluster-auth/commit/e5c4fb17b956f1ffa5e7b0b3e9543c329af99604)|2016-09-27 18:54:44
|326|jonasfj|DNS -> DSN typo, credits @imbstack|[URL](https://github.com/taskcluster/taskcluster-auth/commit/762ba3c985e693ae2fc620f158eed01643f191df)|2016-09-27 18:51:45
|325|djmitche|Merge pull request #69 from taskcluster/monitor-things  Pass monitor to api, etc|[URL](https://github.com/taskcluster/taskcluster-auth/commit/f20437e691b77d1f869f9803dd9e5b932046993b)|2016-09-27 18:35:55
|324|jonasfj|Pass monitor to api, etc|[URL](https://github.com/taskcluster/taskcluster-auth/commit/900ace11642a297e0741d2dc90e219df1522b22c)|2016-09-27 18:16:14
|323|jonasfj|Merge pull request #67 from taskcluster/update-libs  Update libs|[URL](https://github.com/taskcluster/taskcluster-auth/commit/1b58e5841c465bf5eaa8d5318e399967e4b71a45)|2016-08-26 19:18:04
|322|jonasfj|Merge pull request #68 from taskcluster/add-lib-monitor  Added lib-monitor, had to bootstrap|[URL](https://github.com/taskcluster/taskcluster-auth/commit/1c75ef735429fac5763e738a571afa24483e411d)|2016-08-26 19:17:53
|321|jonasfj|Added lib-monitor, had to bootstrap|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ddb93c7ee738fd08231bd874d1876763ed776df6)|2016-08-25 23:04:21
|320|jonasfj|Fixed all tests again, removing tc-base|[URL](https://github.com/taskcluster/taskcluster-auth/commit/42f40e53a7e23246cd88afb04f17945344172432)|2016-08-24 00:27:32
|319|jonasfj|Update npm-shrinkwrap|[URL](https://github.com/taskcluster/taskcluster-auth/commit/139646bc934a82b3603e40f590054c4940d34154)|2016-08-23 22:29:45
|318|jonasfj|Removed tc-base|[URL](https://github.com/taskcluster/taskcluster-auth/commit/97cfb351e2ec2400d624f14f18554fbbbcc3284b)|2016-08-23 22:29:32
|317|jonasfj|Addeding shrinkwrap|[URL](https://github.com/taskcluster/taskcluster-auth/commit/eda84aaffa9f68a4a5779f6c274cf49aa778071e)|2016-08-22 19:11:00
|316|jonasfj|Using base.Exchanges again|[URL](https://github.com/taskcluster/taskcluster-auth/commit/32082a506afb2b08a132568a73306b3b640a3231)|2016-08-22 19:10:12
|315|jonasfj|updated libraries|[URL](https://github.com/taskcluster/taskcluster-auth/commit/886401a27b3c571551cdb90c708d3d78fcb7f44a)|2016-08-20 00:14:14
|314|djmitche|Merge djmitche/taskcluster-auth:bug1274321 (PR #66)|[URL](https://github.com/taskcluster/taskcluster-auth/commit/5daa2a8a671e2156a91fe7b86cb57ddfba90958e)|2016-08-12 13:42:51
|313|djmitche|Bug 1274321: return expires from authenticateHawk; r?jonasfj|[URL](https://github.com/taskcluster/taskcluster-auth/commit/60354d6beab622d2dfc2c16c1fe8c3b3532c91d3)|2016-08-11 19:30:56
|312|djmitche|delete test clients before creating|[URL](https://github.com/taskcluster/taskcluster-auth/commit/7f6d0f428caceabf1144fad8ffd2c991558aea7e)|2016-05-16 15:20:13
|311|djmitche|Merge djmitche/taskcluster-auth:bug1264100 (PR #63)|[URL](https://github.com/taskcluster/taskcluster-auth/commit/6ff72bc4742dce418ba72d90fbe64ccbf5974b18)|2016-05-16 14:41:37
|310|djmitche|Bug 1264100: include information on delegating bucket access|[URL](https://github.com/taskcluster/taskcluster-auth/commit/b4630a10b112762e4f500355cb6e9d3de92e8ad3)|2016-05-12 18:54:39
|309|djmitche|Merge djmitche/taskcluster-auth:no-dots-in-buckets (PR #61)|[URL](https://github.com/taskcluster/taskcluster-auth/commit/04989c253614b591de3749fb68c9a07bed89d2df)|2016-05-04 17:47:39
|308|djmitche|No dots allowed in buckets|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ed7b70f38f3a1bc37bc7cfa8a102879593cb7383)|2016-05-04 17:21:29
|307|djmitche|Revert "Bug 1091780: use https://schemas.t.n"  This reverts commit 0d0f83f6b2d9f98dffb91480f8a95da86fc2519f.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/90f83b9550dc96d811039ebab637b0a6ca7a91b0)|2016-05-03 18:51:28
|306|djmitche|Bug 1091780: use https://schemas.t.n|[URL](https://github.com/taskcluster/taskcluster-auth/commit/0d0f83f6b2d9f98dffb91480f8a95da86fc2519f)|2016-05-03 18:21:12
|305|jonasfj|Improve readability|[URL](https://github.com/taskcluster/taskcluster-auth/commit/5d7a6b19755355a15c4057c9c7ecb783c0e34bd0)|2016-04-21 17:30:35
|304|imbstack|Merge pull request #58 from taskcluster/modern-art  node 5 & npm shrinkwrap & compiled babel|[URL](https://github.com/taskcluster/taskcluster-auth/commit/bc2218e5c05f6843ab9e160c16279c4e3b0a030d)|2016-04-08 19:26:59
|303|imbstack|Upgrade to node 5 and shrinkwrap dependencies|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ec083ff47aca63aa285dcf2277bb31b989d3c2a4)|2016-04-07 21:31:09
|302|imbstack|Move to compiled babel rather than runtime|[URL](https://github.com/taskcluster/taskcluster-auth/commit/e9ece3363e68de7f74b191d16db8f65dc613a55f)|2016-04-07 21:18:39
|301|imbstack|Merge pull request #57 from taskcluster/pick-at-boundary  Better place to filter for dsn|[URL](https://github.com/taskcluster/taskcluster-auth/commit/3ca2f127f2aa777e6cbe3ad7daa3c103a8c96c50)|2016-04-06 23:08:10
|300|imbstack|Better place to filter for dsn|[URL](https://github.com/taskcluster/taskcluster-auth/commit/c806226fab8b9f25bf34f3091863ea4910118dea)|2016-04-06 22:57:55
|299|imbstack|Merge pull request #56 from taskcluster/sentry-fixes  Fixes for generic sentry issues.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/277e52ddebd33f8b588a59d0c0efc24e22e24459)|2016-04-06 20:47:14
|298|imbstack|Fixes for generic sentry issues. There is a csp field in the dsn returned from the api.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/5e2c1af1863bca0c69a1251cc10d19798d30b3f0)|2016-04-06 19:22:20
|297|djmitche|Merge anarute/taskcluster-auth:master (PR #54)|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ae0ab62d4d51bd841474a86e62e3441f54d326c7)|2016-04-04 19:08:29
|296|imbstack|Merge pull request #53 from taskcluster/statsum-token  Added method to grant a statsum token|[URL](https://github.com/taskcluster/taskcluster-auth/commit/5deb10dac3a7138c220947372236f8dacdc53f0a)|2016-04-04 18:57:57
|295|imbstack|Merge pull request #55 from taskcluster/shorter-sentry-scope  Make smaller scope for sentry|[URL](https://github.com/taskcluster/taskcluster-auth/commit/fb6e322391fccb37c1bc7f0ae17153f7b6c79717)|2016-04-04 18:57:28
|294|imbstack|Make smaller scope for sentry   This is a shorter and more straightforward scope.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/a85c304f25e009e38e059548c084058d841d34cd)|2016-03-30 20:47:24
|293|imbstack|Make smaller scope for statsum  This is a shorter and more straightforward scope.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/4c32a59617aec41838d19ae7690d3e1cd863b552)|2016-03-30 20:44:34
|292|anarute|Bug 1237311: add 'stable' level for auth methods|[URL](https://github.com/taskcluster/taskcluster-auth/commit/657450c0631433361c75085cf57aad674eee106d)|2016-03-29 14:37:16
|291|jonasfj|Added expiration to statsum token response|[URL](https://github.com/taskcluster/taskcluster-auth/commit/81d7c09bca0171e55f48037c7ffdcae80cbaa6e4)|2016-03-29 05:33:44
|290|jonasfj|Space|[URL](https://github.com/taskcluster/taskcluster-auth/commit/a42677bcf1f1e03305633afc2284e084d0012ebd)|2016-03-28 23:57:40
|289|jonasfj|Added method to grant a statsum token|[URL](https://github.com/taskcluster/taskcluster-auth/commit/68d66ea5beecbfe76d63b0ac79ed3b13c0a862d4)|2016-03-28 23:57:08
|288|jonasfj|Merge pull request #52 from taskcluster/sentry-access  Fixing spelling issues in schemas|[URL](https://github.com/taskcluster/taskcluster-auth/commit/790974932c1f8cc8949c0a8a340a83dcc0ad0f01)|2016-03-28 23:02:08
|287|jonasfj|Fixing spelling issues in schemas|[URL](https://github.com/taskcluster/taskcluster-auth/commit/99cf88cae3e1ffd205e78be7d751d39434931b06)|2016-03-28 22:59:17
|286|jonasfj|Merge pull request #51 from taskcluster/sentry-access  Added sentry manager|[URL](https://github.com/taskcluster/taskcluster-auth/commit/865111679bef8255aabe06a3fddb716776e1f3d5)|2016-03-28 22:34:41
|285|jonasfj|Added sentry manager|[URL](https://github.com/taskcluster/taskcluster-auth/commit/50d79ebe24a588978a5c7c2d3d1165546c548bc2)|2016-03-28 18:44:16
|284|djmitche|Merge djmitche/taskcluster-auth:bug1254733 (PR #50)|[URL](https://github.com/taskcluster/taskcluster-auth/commit/377039b3f70d2ccd62a79f5599c86353bb351d96)|2016-03-28 13:02:43
|283|djmitche|Bug 1254733: include cert scopes in error message  When handling temporary credentials where cert.scopes are not satisfied by the issuer's scopes, include the cert scopes in the error message to help debugging.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/7936b766270abdba9a6712c88c295336b87bf83b)|2016-03-25 22:25:18
|282|imbstack|Merge pull request #49 from taskcluster/new-validate  Use new schema validation library|[URL](https://github.com/taskcluster/taskcluster-auth/commit/b7fca6804e15a18f5b03877abe716dcee6464a53)|2016-03-24 21:48:47
|281|imbstack|Use a nicer name for new validator|[URL](https://github.com/taskcluster/taskcluster-auth/commit/710e5e8c7d008c4d394c79872fb8a5dfa5ddf25c)|2016-03-24 19:07:22
|280|djmitche|Merge djmitche/taskcluster-auth:bug1256743 (PR #48)|[URL](https://github.com/taskcluster/taskcluster-auth/commit/aaf167cc8cc173be7a6e4adb4f248339fb44bba3)|2016-03-24 14:21:21
|279|imbstack|Use new schema validation library|[URL](https://github.com/taskcluster/taskcluster-auth/commit/e53bfcabb33f1aa34cf039fdb53552fa97f452b5)|2016-03-24 00:17:40
|278|djmitche|Bug 1256743: Remove 'assume:client-id:..' special-casing|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ab2debca7bd55367180091c254a7482f38bb6f91)|2016-03-23 22:04:49
|277|djmitche|it's 'npm run'|[URL](https://github.com/taskcluster/taskcluster-auth/commit/56c90cf1442feaf50fa7818970d73b04b6aee078)|2016-03-11 20:34:57
|276|djmitche|Bug 1247425: add checkStagingSetup to set up creds for checkStaging|[URL](https://github.com/taskcluster/taskcluster-auth/commit/31a770029872c0edb74c91237e11aa8e4efe01a2)|2016-03-11 20:33:56
|275|djmitche|Merge djmitche/taskcluster-auth:test-authentication-get (PR #47)|[URL](https://github.com/taskcluster/taskcluster-auth/commit/9e7a5f59ad3a7fb9c50453d0eb3cbf0773d55ed3)|2016-02-16 15:24:27
|274|imbstack|Merge pull request #46 from taskcluster/add-sentry  Add sentry integration|[URL](https://github.com/taskcluster/taskcluster-auth/commit/8abc15d124ce66d13bfd6ac29f9f79d8a05e9aa5)|2016-02-12 23:08:37
|273|djmitche|Add testAuthenticationGet|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ef5be2659b31f54a9b8d8193e177725566c20025)|2016-02-12 21:15:49
|272|imbstack|Add sentry integration|[URL](https://github.com/taskcluster/taskcluster-auth/commit/a92bc689e3ff64b86f592cbd27960d96b6583b29)|2016-02-12 20:30:01
|271|jonasfj|Merge pull request #45 from taskcluster/fix-auth-code-in-tests  Fix auth code in tests|[URL](https://github.com/taskcluster/taskcluster-auth/commit/6a415ade5ecbfaa9a6ba9f0446bd0331972c787a)|2016-02-12 21:14:04
|270|jonasfj|Merge branch 'master' of github.com:taskcluster/taskcluster-auth into fix-auth-code-in-tests|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ec32437e73f672858b1fdb26aae7016b21a5ee87)|2016-02-12 20:20:41
|269|jonasfj|Fixed testcases where I wrote code worng|[URL](https://github.com/taskcluster/taskcluster-auth/commit/2c2aa92af8f1c54ebbd8e32c0e3703f2ac8f8d27)|2016-02-12 20:20:14
|268|djmitche|Merge taskcluster/taskcluster-auth:test-end-point (PR #40)|[URL](https://github.com/taskcluster/taskcluster-auth/commit/84e3153ebb14ce8bd9a671c3aa0f91fdbf179d79)|2016-02-12 17:53:09
|267|jonasfj|Better description credits to @djmitche|[URL](https://github.com/taskcluster/taskcluster-auth/commit/354d22139fdb3eab4142078e5a6a26fa7e1c0e3d)|2016-02-11 20:49:29
|266|jonasfj|Newline at end of file|[URL](https://github.com/taskcluster/taskcluster-auth/commit/5211bb70da2805125c86fce7376734ae0ffd80b5)|2016-02-11 20:41:11
|265|jonasfj|Merge branch 'master' of github.com:taskcluster/taskcluster-auth into test-end-point|[URL](https://github.com/taskcluster/taskcluster-auth/commit/5aad3e9d8946b29d9133d0f2bee2135f7f5f92f2)|2016-02-11 20:40:28
|264|walac|Merge pull request #44 from walac/master  Better explanatory message when authorized scopes are not satisfied.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/5cd2d2ae3f04f7d0bb774b029fbadcacbfa10aed)|2016-02-11 16:31:01
|263|walac|Better explanatory message when authorized scopes are not satisfied.  When the clientId doesn't satisfies the authorized scopes, report the client scopes and the authorized scopes in the error messsage.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/8b8468c208bd996a78290f8eb7a7630a175e5a9d)|2016-02-11 14:19:25
|262|djmitche|Merge djmitche/taskcluster-auth:checkStaging (PR #42)|[URL](https://github.com/taskcluster/taskcluster-auth/commit/6048b688a3745bd4a0aa92d3ab44754150c6a5a8)|2016-02-10 21:53:31
|261|djmitche|Revert "create a staging env with different table names"  This reverts commit 96be6c95b13f39766d38daf232c61681977f8556.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/592ac0404d3c0542186411bce1f5e17edae0e021)|2016-02-10 21:48:31
|260|djmitche|create a staging env with different table names|[URL](https://github.com/taskcluster/taskcluster-auth/commit/96be6c95b13f39766d38daf232c61681977f8556)|2016-02-10 21:38:51
|259|djmitche|Merge djmitche/taskcluster-auth:hash-test (PR #43)|[URL](https://github.com/taskcluster/taskcluster-auth/commit/7b2f31fb5f4366216a1571f2e1bf8e2c7bf40783)|2016-02-10 21:16:08
|258|djmitche|add test for signaturevalidator to return a hash|[URL](https://github.com/taskcluster/taskcluster-auth/commit/be4efa77c249438f41747265ea97d641c1dcaf5b)|2016-02-10 19:47:57
|257|djmitche|add a test for hashes|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ca67bc5a53dff939624ae40d3938e94a1bea6035)|2016-02-10 19:44:11
|256|djmitche|Revert "remove unsupported field"  This reverts commit a64fba5b34928e9e07b639d803bfcf6c79397e1d.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/8330d3cdabcdec55f7203aca7f9275efa96a0f8b)|2016-02-10 19:30:09
|255|jonasfj|Some test cases too|[URL](https://github.com/taskcluster/taskcluster-auth/commit/02f1592723273f20770b878e44a3087f93084136)|2016-02-10 19:16:47
|254|djmitche|add check-staging script|[URL](https://github.com/taskcluster/taskcluster-auth/commit/a3595f62a934f023c1d2a71c099fc58eb3ea681c)|2016-02-10 17:27:21
|253|jonasfj|Merge branch 'master' of github.com:taskcluster/taskcluster-auth into test-end-point|[URL](https://github.com/taskcluster/taskcluster-auth/commit/b92bd544a2a341623a8eba2eb6194c57d0c57a57)|2016-02-10 17:52:57
|252|jonasfj|Progress towards test end-point|[URL](https://github.com/taskcluster/taskcluster-auth/commit/d459e70182ec59726cf417a76fa97f8bb56e06f8)|2016-02-10 17:52:50
|251|djmitche|Merge djmitche/taskcluster-auth:named-temp-creds (PR #41)|[URL](https://github.com/taskcluster/taskcluster-auth/commit/32b7af1f92e5e357f782058ad2ef538f1558f6e5)|2016-02-10 17:32:41
|250|jonasfj|Merge branch 'master' of github.com:taskcluster/taskcluster-auth into test-end-point|[URL](https://github.com/taskcluster/taskcluster-auth/commit/7b10f37003883562a4ea196ec3a5e129229b130f)|2016-02-10 17:12:08
|249|djmitche|don't include clientId in certificate|[URL](https://github.com/taskcluster/taskcluster-auth/commit/50c365af6ec06cf1e211e30df81505b80a0025ba)|2016-02-10 00:06:32
|248|djmitche|restore info about hash|[URL](https://github.com/taskcluster/taskcluster-auth/commit/233c6fda19754c2f72ff6fccd34a18f75d9c60d0)|2016-02-09 19:26:40
|247|djmitche|rename cert.name to cert.clientId|[URL](https://github.com/taskcluster/taskcluster-auth/commit/662c7b2680505c601cf8e3e734d749fecaf22079)|2016-02-08 23:57:08
|246|djmitche|alter authenticateHawk scheme to include clientId|[URL](https://github.com/taskcluster/taskcluster-auth/commit/01fb3a967d3069ad74b7d1a171a7483d752e9815)|2016-02-08 23:48:07
|245|djmitche|remove unsupported field|[URL](https://github.com/taskcluster/taskcluster-auth/commit/a64fba5b34928e9e07b639d803bfcf6c79397e1d)|2016-02-08 23:44:21
|244|djmitche|Support named temporary credentials  Credentials are {id, key, cert}.  A "simple" temporary credential has the issing client as its `id`, scopes and expiry in the cert, all signed to generate a new key.  "Named" temporary credentials further include a name and an issuer in the certificate; the issuer is the clientId that created the credential (and the corresponding accessToken is used in the signature), while the name is the clientId that should be supplied as `id`.  The result is that temporary credentials can have a meaningful id that is useful for logging and for identifying the credentials.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/2917332803b4f9054941c3b108763af54c780a88)|2016-02-08 19:55:00
|243|djmitche|generate temporary credentials when running tests|[URL](https://github.com/taskcluster/taskcluster-auth/commit/79c5d47ef7682eb3c9fa033a8e6c8e507b4c5fdc)|2016-02-08 18:59:16
|242|djmitche|fix DEBUG|[URL](https://github.com/taskcluster/taskcluster-auth/commit/9cef1c7606a1d466b99701d751298858d4859cbf)|2016-02-08 18:33:25
|241|djmitche|add debugging for travis-only failure|[URL](https://github.com/taskcluster/taskcluster-auth/commit/70ebedd9f477b195347dcf565bdf33d872a2ae3a)|2016-02-08 18:07:03
|240|djmitche|require superagent for non-dev|[URL](https://github.com/taskcluster/taskcluster-auth/commit/bff03789f0c97c8d23ed419f67e1f48339bb4b16)|2016-02-08 18:06:54
|239|djmitche|run (and fix) all tests|[URL](https://github.com/taskcluster/taskcluster-auth/commit/73fe1bac5a2ad489262eb8f195f44a3c9c17f712)|2016-02-08 17:04:03
|238|djmitche|Merge djmitche/taskcluster-auth:sig-validator-move (PR #39)|[URL](https://github.com/taskcluster/taskcluster-auth/commit/b81c7d9d4e375ef2f963e243da365df3671cf746)|2016-02-08 16:53:58
|237|djmitche|Thorough tests for signature validator|[URL](https://github.com/taskcluster/taskcluster-auth/commit/5b33efbd235c5abc933493887da4c8903a320d21)|2016-02-04 15:17:28
|236|jonasfj|Added req/res schemas|[URL](https://github.com/taskcluster/taskcluster-auth/commit/180682781bf85ff9e373a7e513bfb533b091b278)|2016-02-04 18:33:58
|235|jonasfj|Not really tested yet... nor working, still need export|[URL](https://github.com/taskcluster/taskcluster-auth/commit/fd8b2c4d2c9703c6b82bcab2155fa6c9632486f1)|2016-02-04 18:24:49
|234|djmitche|WIP|[URL](https://github.com/taskcluster/taskcluster-auth/commit/0298aa1a7d6cff0a5a6c44f77f7c01cec0720cc5)|2016-02-04 15:17:28
|233|djmitche|move local signature validator from tc-lib-api|[URL](https://github.com/taskcluster/taskcluster-auth/commit/f643ca48398c44d6c8542f9973b83bc88589346f)|2016-02-03 18:15:07
|232|djmitche|Merge djmitche/taskcluster-auth:util-methods (PR #38)|[URL](https://github.com/taskcluster/taskcluster-auth/commit/03eacb0c3fe6e6c164030bf91c9a1da89d9ea960)|2016-02-01 14:48:07
|231|djmitche|support prefix filtering in listClients|[URL](https://github.com/taskcluster/taskcluster-auth/commit/2e86c5c576827be9a028b256eb85cb83e2ed691e)|2016-01-29 20:32:55
|230|djmitche|add currentScopes|[URL](https://github.com/taskcluster/taskcluster-auth/commit/c8a4eb574346a5ff9b80c1009bac3ed5c180b418)|2016-01-29 20:06:39
|229|djmitche|normalize input to resolve()|[URL](https://github.com/taskcluster/taskcluster-auth/commit/06aaaf8aedd21a974abbda70c91c7e39db2c39c9)|2016-01-29 19:52:22
|228|djmitche|add expandScopes|[URL](https://github.com/taskcluster/taskcluster-auth/commit/dc8aeb6a2d32845cc1a16cc665c4f8234fe64a24)|2016-01-29 19:33:58
|227|jonasfj|Merge pull request #37 from djmitche/handle-missing-config  handle missing config a little better|[URL](https://github.com/taskcluster/taskcluster-auth/commit/3c3b0c9f9a98baa23839ee0d8b0accff878f462f)|2016-01-29 20:33:40
|226|djmitche|handle missing config a little better|[URL](https://github.com/taskcluster/taskcluster-auth/commit/1743386c91d036f615cc015d7baa267073f19eeb)|2016-01-29 19:10:47
|225|jonasfj|Minor config cleanup|[URL](https://github.com/taskcluster/taskcluster-auth/commit/c10cde2a99d91df149c9de388f4c8023d1c1d8f7)|2016-01-29 18:12:10
|224|jonasfj|Fix exploit of idempotent operation|[URL](https://github.com/taskcluster/taskcluster-auth/commit/53f09cf531e1d5ac8fafb1bd410dcd66826feb59)|2016-01-29 00:17:29
|223|jonasfj|Okay this time travis better work|[URL](https://github.com/taskcluster/taskcluster-auth/commit/f9aadda752744d2332fe448204044af52aa6e5eb)|2016-01-29 00:03:12
|222|jonasfj|Reduce DEBUG noise|[URL](https://github.com/taskcluster/taskcluster-auth/commit/c50d12a8ed3efb35e52faca3d9564f7f3d8c8a54)|2016-01-28 21:55:19
|221|jonasfj|Revert travis hack|[URL](https://github.com/taskcluster/taskcluster-auth/commit/6b5a2e176c586791fc1f4982d6b132a9a33570ac)|2016-01-28 21:47:22
|220|jonasfj|test travis env var support|[URL](https://github.com/taskcluster/taskcluster-auth/commit/2236bd9052fb923f82ab939bb031d30637cf21a5)|2016-01-28 21:42:23
|219|jonasfj|Using a clean tablename helps perf of tests|[URL](https://github.com/taskcluster/taskcluster-auth/commit/a5d8f4a172fed28ac3fc1eca5e46479b0f7d2ff3)|2016-01-28 20:20:27
|218|jonasfj|More work on travis fixing...|[URL](https://github.com/taskcluster/taskcluster-auth/commit/eb1e3f707f7bfef1d16790938c5b923cd426130a)|2016-01-28 19:03:34
|217|jonasfj|Some fixes for travis|[URL](https://github.com/taskcluster/taskcluster-auth/commit/29f43b5e42ca28db1daf42a42624952500444cec)|2016-01-27 20:14:35
|216|jonasfj|Fixed _scopes|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ffc56b5aa6d3c0223c32e0c4c98d2b2805cdeac0)|2016-01-27 20:08:56
|215|jonasfj|Remove old config and upgrade travis config|[URL](https://github.com/taskcluster/taskcluster-auth/commit/b138343fe57c5b14c31498eddf428b7f353421aa)|2016-01-27 20:00:54
|214|jonasfj|forgot the fix|[URL](https://github.com/taskcluster/taskcluster-auth/commit/15f82441a1f1f38cd86bf2539917afdfe5590432)|2016-01-27 19:53:32
|213|jonasfj|Fix bug 1234929 - upgrade node, make faster, upgrade libs|[URL](https://github.com/taskcluster/taskcluster-auth/commit/f6d3b00ef5dbf4f25931e7c12cfb888dc2421211)|2016-01-27 19:48:34
|212|jonasfj|Merge branch 'new-config-system' into upgrade-node4  Conflicts: 	package.json|[URL](https://github.com/taskcluster/taskcluster-auth/commit/191f348d3cd23eb463647631091d9898073c89aa)|2016-01-27 18:25:34
|211|jonasfj|Upgrade tc-base|[URL](https://github.com/taskcluster/taskcluster-auth/commit/2c13e053c1bddc200f320c23db94d14be7c13a9e)|2016-01-27 18:24:48
|210|djmitche|increase test server timeout|[URL](https://github.com/taskcluster/taskcluster-auth/commit/fc36bcafd3843bd1f15bf64a8dd6eef5b41930f0)|2016-01-27 17:15:08
|209|djmitche|use correct type when migrating disabled property|[URL](https://github.com/taskcluster/taskcluster-auth/commit/d97798be9992f2a20f4dbf7e8e5de542bb7b6a50)|2016-01-27 17:03:07
|208|djmitche|use the more reliable docker-based travis infra|[URL](https://github.com/taskcluster/taskcluster-auth/commit/85424b8555f9401243bac16b786f9e516ad6ee2d)|2016-01-26 20:05:36
|207|djmitche|Merge branch 'master' of github.com:taskcluster/taskcluster-auth|[URL](https://github.com/taskcluster/taskcluster-auth/commit/2d56b0cacda455b5b765a69c66fedd0ee12babce)|2016-01-26 18:56:50
|206|petemoore|Added IRC notifications to irc.mozilla.org#taskcluster-bots|[URL](https://github.com/taskcluster/taskcluster-auth/commit/d7efdcb128374c8dd06967331dd155db674980e9)|2016-01-26 18:13:27
|205|djmitche|Merge djmitche/taskcluster-auth:new-client-properties (PR #34)|[URL](https://github.com/taskcluster/taskcluster-auth/commit/a3206adfe05d0e0622c5cdfb59d06de48e9368d5)|2016-01-26 17:28:10
|204|djmitche|fix api copy-pasta|[URL](https://github.com/taskcluster/taskcluster-auth/commit/1a0a97988e09684cce981830195d25b375a248f2)|2016-01-26 15:20:34
|203|djmitche|remove import support|[URL](https://github.com/taskcluster/taskcluster-auth/commit/9baa1580d24e019ff73571590e01752b2b94aea8)|2016-01-26 14:55:09
|202|djmitche|Revert "Fix bug 1234929"  This reverts commit 0baa798c2d3fdd4dfe9265e57fda14fb5814817c.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/bd16d2aa771d686cf1df192ff734e40d8c1387ec)|2016-01-26 14:44:49
|201|djmitche|use client.scopes for root client|[URL](https://github.com/taskcluster/taskcluster-auth/commit/3e6ad246f8b40905fd8cc69e899894b5183e7da6)|2016-01-25 21:31:32
|200|djmitche|test disabling|[URL](https://github.com/taskcluster/taskcluster-auth/commit/a508b4996ec6ef088035ed53c73ff6f3673ec618)|2016-01-25 20:44:19
|199|djmitche|Give a better error message when clients are disabled|[URL](https://github.com/taskcluster/taskcluster-auth/commit/e20c863eb23268140d516bdaa5660a801b114591)|2016-01-25 20:44:07
|198|djmitche|add enable/disable to the API|[URL](https://github.com/taskcluster/taskcluster-auth/commit/b829205ceb5020cbea01f64321ad5a0721d5d2bd)|2016-01-25 20:24:54
|197|djmitche|test a user story|[URL](https://github.com/taskcluster/taskcluster-auth/commit/04064af5b5df7f72a991bbdf997dfb466fdb9761)|2016-01-25 18:24:53
|196|djmitche|add a Clients v2|[URL](https://github.com/taskcluster/taskcluster-auth/commit/aa8ae0db2db3ae515f3ee90148bb07c83ed16a9b)|2016-01-25 14:12:21
|195|djmitche|Bug 1240452: increase timeout for slow tests|[URL](https://github.com/taskcluster/taskcluster-auth/commit/20ec3379cce9bb9eb75ca372e9612b1793c50638)|2016-01-26 14:22:43
|194|djmitche|Merge taskcluster/taskcluster-auth:bug-1234929 (PR #33)|[URL](https://github.com/taskcluster/taskcluster-auth/commit/c33ee5d6cb6fd0fb64e49bd3b661a467031e52e3)|2016-01-26 00:10:33
|193|djmitche|don't make a client that expires immediately|[URL](https://github.com/taskcluster/taskcluster-auth/commit/f1f78f13ff3f58b78a3b28ea83d9b0f1121d3923)|2016-01-26 00:08:30
|192|djmitche|Merge djmitche/taskcluster-auth:bug1242714 (PR #32)|[URL](https://github.com/taskcluster/taskcluster-auth/commit/3c7ecad89b6ba0d3cddc70403e9f1b9c1afdc593)|2016-01-26 00:02:00
|191|jonasfj|Fix bug 1234929  Also reduces amount of code...|[URL](https://github.com/taskcluster/taskcluster-auth/commit/0baa798c2d3fdd4dfe9265e57fda14fb5814817c)|2016-01-25 23:01:50
|190|jonasfj|Merge pull request #31 from djmitche/testing-fixes  Testing fixes|[URL](https://github.com/taskcluster/taskcluster-auth/commit/32633e8eedd5080293e2e7e5acf0315238983d8d)|2016-01-25 22:06:48
|189|djmitche|Bug 1242714: reject expired clients|[URL](https://github.com/taskcluster/taskcluster-auth/commit/acaf960e08866041888792dd5d66d9ca6cfa0f67)|2016-01-25 21:20:03
|188|djmitche|Merge https://github.com/taskcluster/taskcluster-auth/pull/9|[URL](https://github.com/taskcluster/taskcluster-auth/commit/9e76bf4ec101e55ffa5e088768965210db8101dc)|2016-01-25 21:17:53
|187|djmitche|don't require azure or influx credentials to run tests|[URL](https://github.com/taskcluster/taskcluster-auth/commit/8e389a6e4be2c675bafba48b0acc4aa74b3e7123)|2016-01-22 21:57:59
|186|djmitche|use newer azure-entities|[URL](https://github.com/taskcluster/taskcluster-auth/commit/dbd3109be15db69674a2dabc6b95ebc68d365b4f)|2016-01-22 21:37:55
|185|djmitche|use newer taskcluster-lib-app for better logging|[URL](https://github.com/taskcluster/taskcluster-auth/commit/25532d58509d205de7b8a41301db661150bae06f)|2016-01-22 21:25:41
|184|djmitche|refactor server to use taskcluster-lib-loader|[URL](https://github.com/taskcluster/taskcluster-auth/commit/3864a198ad95592e0b8463c3a8309c976f77f9ba)|2016-01-22 21:16:41
|183|djmitche|remove debug output|[URL](https://github.com/taskcluster/taskcluster-auth/commit/f9af332026a3dec08593dbe580f72def6dae07ec)|2016-01-22 20:21:52
|182|djmitche|Revert "use an internally-generated root access token for tests"  This reverts commit d65f36135479f1ef10c4b20119962296466d12f0.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/eb0d0b93c8b210cf0580b77b8772344488b69172)|2016-01-22 20:18:31
|181|djmitche|add example of auth file|[URL](https://github.com/taskcluster/taskcluster-auth/commit/89b37ec6c6341f8cfbb2240ba9a86bf01ae4cd60)|2016-01-22 20:17:04
|180|djmitche|use an internally-generated root access token for tests|[URL](https://github.com/taskcluster/taskcluster-auth/commit/d65f36135479f1ef10c4b20119962296466d12f0)|2016-01-22 20:10:57
|179|jonasfj|Merge pull request #29 from taskcluster/fix-tests-again  Added pulse credentials to encrypted test config file to get tests running|[URL](https://github.com/taskcluster/taskcluster-auth/commit/7c83bd3e8108b00289429a0a2daf3730b3aee647)|2015-12-01 19:22:34
|178|petemoore|Added some pulse credentials to encrypted test config file to get them working on travis again|[URL](https://github.com/taskcluster/taskcluster-auth/commit/6577aa5da0c5fe768cf6a02d27fb899b44c5375c)|2015-12-01 14:39:52
|177|jonasfj|Merge pull request #28 from taskcluster/bug1220295  bug 1220295|[URL](https://github.com/taskcluster/taskcluster-auth/commit/d821125d3900b15f6ebf34da9c15a81ef0dbbcbd)|2015-11-26 00:46:03
|176|jonasfj|bug 1220295|[URL](https://github.com/taskcluster/taskcluster-auth/commit/34f94bbe1efcbfe942b74070f0d2bc81734b3b83)|2015-11-25 22:17:07
|175|jonasfj|Merge pull request #27 from taskcluster/use-login  Use login|[URL](https://github.com/taskcluster/taskcluster-auth/commit/2b3d781e82c3f5964e975a78b3f5a696430c6ad4)|2015-11-18 21:01:16
|174|jonasfj|Remove all UI, redirect login requests to login.taskcluster.net|[URL](https://github.com/taskcluster/taskcluster-auth/commit/8dd14848b9f16d9c9d6fbf738d54854d3d348dce)|2015-11-16 23:04:43
|173|jonasfj|Remove persona...|[URL](https://github.com/taskcluster/taskcluster-auth/commit/78841157ccf104396725e5bd4980ab0d84898966)|2015-11-16 22:57:52
|172|jonasfj|Use login.tc.net for login, removing all UI...|[URL](https://github.com/taskcluster/taskcluster-auth/commit/9af2fa37c7424908eda5edb85eb0bac56ca95ca5)|2015-11-16 22:51:21
|171|jonasfj|Initial work on moving config|[URL](https://github.com/taskcluster/taskcluster-auth/commit/e11b701ea6d3bfa640eade8b7608ae0715aa19f4)|2015-11-11 21:25:35
|170|jonasfj|Fixed tests|[URL](https://github.com/taskcluster/taskcluster-auth/commit/872c6c054a070e580a92e8fb35f5d7b38e28831c)|2015-11-05 01:48:53
|169|jonasfj|Merge pull request #24 from djmitche/bug1221121  Bug 1221121: check input scopes on createRole|[URL](https://github.com/taskcluster/taskcluster-auth/commit/adcd6d9e328f2c454886c3cee3c08628c65605e5)|2015-11-05 01:37:22
|168|jonasfj|Fixed role_test|[URL](https://github.com/taskcluster/taskcluster-auth/commit/2fa8f341488962d1c2932e7291ea91da1fb81e12)|2015-11-05 01:33:22
|167|jonasfj|Merge branch 'master' into allow-all-printable-clientids|[URL](https://github.com/taskcluster/taskcluster-auth/commit/237aea36cd105e626e86406d8dabf8df93296bb5)|2015-11-05 01:19:32
|166|jonasfj|Fixed temp creds expiry|[URL](https://github.com/taskcluster/taskcluster-auth/commit/4d8abb20c27a45604cfebae90af204d51ace377b)|2015-11-04 22:26:34
|165|jonasfj|Merge pull request #25 from djmitche/bug1137740  Bug 1137740: limit temporary credentials, use client role|[URL](https://github.com/taskcluster/taskcluster-auth/commit/184d2df85950bde20d6ea939dbfff644dd4c912c)|2015-11-04 17:11:58
|164|jonasfj|Support for more clientIds..|[URL](https://github.com/taskcluster/taskcluster-auth/commit/eb57e606a1576497d1de1e732f26f633595bd9c7)|2015-11-04 00:50:54
|163|jonasfj|Refactored test|[URL](https://github.com/taskcluster/taskcluster-auth/commit/780779709ffc85e9cefb197fb55951f9235db9be)|2015-11-04 00:14:59
|162|djmitche|Bug 1221121: check input scopes on createRole|[URL](https://github.com/taskcluster/taskcluster-auth/commit/d615c440b9a4ba6f91c4ae84139e14a18c731d14)|2015-11-03 15:01:18
|161|djmitche|Bug 1137740: limit temporary credentials, use client role  This limits the creds' lifetime to 3 days, and uses the `client-id:..` role explicitly so that as the clientId's scopes change, so do the temporary credentials.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/79b407cd98d2911c77042d4f1263a33b76e3b372)|2015-11-03 15:27:06
|160|jonasfj|Merge pull request #23 from taskcluster/test-for-lastused  Test for lastused and fix...|[URL](https://github.com/taskcluster/taskcluster-auth/commit/16ce249b645935e1f33da461883d30ce7163de6b)|2015-11-02 18:54:56
|159|jonasfj|Fixed lastDateUsed and made it somewhat testable...|[URL](https://github.com/taskcluster/taskcluster-auth/commit/75bf5c11b41fd087af011835682bdd7c2a239786)|2015-10-30 23:31:26
|158|jonasfj|Added test that created client can be used...|[URL](https://github.com/taskcluster/taskcluster-auth/commit/54237a75d7f8d860f2675355c271f5dfe173847b)|2015-10-30 22:53:34
|157|jonasfj|Refactored testserver into a reusable form|[URL](https://github.com/taskcluster/taskcluster-auth/commit/43a47839c12d3808875b960a427f6779b93ff728)|2015-10-30 22:47:25
|156|jonasfj|Remove old tests|[URL](https://github.com/taskcluster/taskcluster-auth/commit/23fd0aa7650dc112b61670071c044fd602571cf2)|2015-10-30 22:16:44
|155|jonasfj|test for lastModified for role...|[URL](https://github.com/taskcluster/taskcluster-auth/commit/1351650464edd551f323f43c8ef1cef13b605293)|2015-10-30 21:48:33
|154|jonasfj|Merge pull request #21 from taskcluster/more-scope-tests  More scope tests|[URL](https://github.com/taskcluster/taskcluster-auth/commit/fc269ad4b531d8c1f8288137301ad419c13d60f8)|2015-10-28 17:34:58
|153|jonasfj|Merge pull request #16 from taskcluster/optimizations-for-fixed-point  Optimizations for fixed point|[URL](https://github.com/taskcluster/taskcluster-auth/commit/107f26749dd26a2b0b78eb3db1e24af1f585c155)|2015-10-28 17:34:49
|152|jonasfj|Merge pull request #22 from petemoore/bug1218913  Bug 1218913 - added missing type entries to schemas|[URL](https://github.com/taskcluster/taskcluster-auth/commit/aaaa40c6e137c285a34c8ce88ff62ce5f228308c)|2015-10-27 22:09:21
|151|petemoore|Bug 1218913 - added missing type entries to schemas|[URL](https://github.com/taskcluster/taskcluster-auth/commit/50b57c9e83440cd2baa0e0aae97d193ecb551ff8)|2015-10-27 18:51:10
|150|jonasfj|More scope schema tests|[URL](https://github.com/taskcluster/taskcluster-auth/commit/92ab9c7b876257b133e0e41ab7235b5b0ed08ac8)|2015-10-26 22:29:44
|149|jonasfj|Merge branch 'master' of github.com:taskcluster/taskcluster-auth into optimizations-for-fixed-point|[URL](https://github.com/taskcluster/taskcluster-auth/commit/75b3e7872fd5c38b876d51e9d32ae16414959402)|2015-10-26 22:20:12
|148|jonasfj|dfa should work now...|[URL](https://github.com/taskcluster/taskcluster-auth/commit/fda510b5a5e15251dabd07021bf588f8b85baac9)|2015-10-26 22:16:50
|147|jonasfj|Merge pull request #20 from djmitche/bug1193607-$  add trailing `$` to scope pattern|[URL](https://github.com/taskcluster/taskcluster-auth/commit/16642d5d67fe1c0f898224345e8cd370cf4561b5)|2015-10-26 17:11:13
|146|jonasfj|Merge pull request #19 from djmitche/add-validate-test  add a validation test covering a schema with a scope|[URL](https://github.com/taskcluster/taskcluster-auth/commit/fa81f04935533a426d403c14106fd38e3e2ce5b3)|2015-10-26 17:03:29
|145|djmitche|add trailing `$` to scope pattern|[URL](https://github.com/taskcluster/taskcluster-auth/commit/1cf402adbf420d8b6068a313c78f5e14ab16c462)|2015-10-26 14:24:26
|144|djmitche|add a validation test covering a schema with a scope|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ad09d51cf65606c49d212e1d748c7ade273b4abf)|2015-10-23 15:40:54
|143|jonasfj|Added test case|[URL](https://github.com/taskcluster/taskcluster-auth/commit/a63889b265dbcfd19c418732e2d507f5e68815c6)|2015-10-22 20:38:24
|142|jonasfj|Merge pull request #18 from djmitche/bug1193607-2  Bug 1193607: update schema for limited scope charset|[URL](https://github.com/taskcluster/taskcluster-auth/commit/cd884e800b4963fef38f6d7c7e6f155be71ad19c)|2015-10-22 20:27:15
|141|jonasfj|Got the build resolver things working and passing a crazy amount of tests...|[URL](https://github.com/taskcluster/taskcluster-auth/commit/38c0dc661769eb472d7c9ab1d266a546eb6a6fc3)|2015-10-22 03:25:06
|140|jonasfj|buildResolver works now...|[URL](https://github.com/taskcluster/taskcluster-auth/commit/272c71f3ac4ce75ab088114a54adee9ed52a9e18)|2015-10-22 02:53:42
|139|jonasfj|work making this simpler|[URL](https://github.com/taskcluster/taskcluster-auth/commit/e206a8335ff7c677cd32ca1e28d0f5f0f6d6c34b)|2015-10-21 23:38:49
|138|djmitche|Bug 1193607: update schema for limited scope charset|[URL](https://github.com/taskcluster/taskcluster-auth/commit/a3306862ea69625de3b0c136c2b1a6aabe3b6705)|2015-10-21 21:17:35
|137|jonasfj|Merge branch 'master' into optimizations-for-fixed-point|[URL](https://github.com/taskcluster/taskcluster-auth/commit/5cb7079489a7873d8480947cf4d78d615bdd0450)|2015-10-18 22:46:20
|136|jonasfj|Add publishMetaData support|[URL](https://github.com/taskcluster/taskcluster-auth/commit/77c047d9c573baf2d0499d6ded79248922fd0e84)|2015-10-14 00:27:14
|135|jonasfj|don't publish by default|[URL](https://github.com/taskcluster/taskcluster-auth/commit/091703ab69f0446526745626973801124c4b23bf)|2015-10-13 20:56:19
|134|jonasfj|Minor fix|[URL](https://github.com/taskcluster/taskcluster-auth/commit/2085c91e635a1be8400d2f7a09136df14fd80e6d)|2015-10-13 20:14:32
|133|jonasfj|Fixed login page|[URL](https://github.com/taskcluster/taskcluster-auth/commit/323d3866307e13e97e47817e888f5beb63ad1e2f)|2015-10-13 20:04:48
|132|jonasfj|Merge pull request #17 from djmitche/optimizations-for-fixed-point  comment cleanup|[URL](https://github.com/taskcluster/taskcluster-auth/commit/50b3fb71daadac2580338becfd9234e95b67bcc0)|2015-10-13 16:19:37
|131|djmitche|comment cleanup|[URL](https://github.com/taskcluster/taskcluster-auth/commit/a6d32859de8161591e39d92451c731cf663bdf2d)|2015-10-13 15:49:52
|130|jonasfj|More tests and adding iterations to existing tests, shuffling the input...|[URL](https://github.com/taskcluster/taskcluster-auth/commit/9e977020b029bff887843f4ce1507c8c845a6f15)|2015-10-13 01:44:55
|129|jonasfj|Commented some test back in|[URL](https://github.com/taskcluster/taskcluster-auth/commit/972a005b255b80612da0c6ad7de02cd4c565df0f)|2015-10-09 22:37:53
|128|jonasfj|dfa generation should work now...|[URL](https://github.com/taskcluster/taskcluster-auth/commit/980c6ffd97d09b23b3f52cbfb366954ad5e7adf9)|2015-10-09 22:33:19
|127|jonasfj|Fixed point computation using local algorithm, is a lot faster...|[URL](https://github.com/taskcluster/taskcluster-auth/commit/8185ffe4632146088ffc0f5973e1834d761517fc)|2015-10-09 00:26:11
|126|jonasfj|load-test changes|[URL](https://github.com/taskcluster/taskcluster-auth/commit/61973caa2c7511b530b0ef62107123ad118a9f8b)|2015-10-08 17:46:22
|125|jonasfj|Merge branch 'support-roles'|[URL](https://github.com/taskcluster/taskcluster-auth/commit/a5198359c95dd8f8310fe766ecf995c90071c354)|2015-10-08 17:35:41
|124|jonasfj|Added test for normalizeScopes|[URL](https://github.com/taskcluster/taskcluster-auth/commit/b294c314ac4742002f57a898d7838a3630f6fcca)|2015-10-08 17:35:09
|123|jonasfj|Merge pull request #14 from taskcluster/support-roles  Support roles|[URL](https://github.com/taskcluster/taskcluster-auth/commit/3aedeeda6354eac89b9094246460f09b522fa2b8)|2015-10-07 19:00:07
|122|jonasfj|Fixed spell error|[URL](https://github.com/taskcluster/taskcluster-auth/commit/8a9da5d799ab22208ba89d2eab3fc60065aa228c)|2015-10-07 18:57:16
|121|jonasfj|Docs...|[URL](https://github.com/taskcluster/taskcluster-auth/commit/6f76cb06fd67e8f59497de1ba6ad083d64ac078d)|2015-10-05 17:59:59
|120|jonasfj|Load-test fixes|[URL](https://github.com/taskcluster/taskcluster-auth/commit/6b1b0cb9f4183424f461babeb14f186f32b6852a)|2015-10-03 01:10:46
|119|jonasfj|Load-test fixes|[URL](https://github.com/taskcluster/taskcluster-auth/commit/fa1ea131c0e593992291ffe8737f6b76634baeea)|2015-10-02 19:42:07
|118|jonasfj|Load-test fixes|[URL](https://github.com/taskcluster/taskcluster-auth/commit/7c8c2dbd3a6dec87d2beacce8ba9bd727649bd90)|2015-10-02 19:33:44
|117|jonasfj|Load-test fixes|[URL](https://github.com/taskcluster/taskcluster-auth/commit/48ce65fb9732dff0f18418e2beec4a7cb84e633d)|2015-10-02 19:25:12
|116|jonasfj|Load-test fixes|[URL](https://github.com/taskcluster/taskcluster-auth/commit/1538a9fc05bad4e27939b33a2e9fbf9aa6d97859)|2015-10-02 18:36:44
|115|jonasfj|Load-test fixes|[URL](https://github.com/taskcluster/taskcluster-auth/commit/0aafcfc7db82a0cee492d76fdb084274c46fee04)|2015-10-02 18:29:00
|114|jonasfj|Load-test config|[URL](https://github.com/taskcluster/taskcluster-auth/commit/19158848fea884d0b8c7b2a07caaea06a67a5993)|2015-10-02 18:16:51
|113|jonasfj|More tests|[URL](https://github.com/taskcluster/taskcluster-auth/commit/56507956c056ac6ec0a7460e72eb6e54af992b46)|2015-10-01 23:59:22
|112|jonasfj|Lots of minor fixes|[URL](https://github.com/taskcluster/taskcluster-auth/commit/47ee43aeeb7ab3daf4b70a807494d7526508d338)|2015-10-01 17:51:15
|111|jonasfj|Merge branch 'master' into support-roles  Conflicts: 	schemas/constants.js|[URL](https://github.com/taskcluster/taskcluster-auth/commit/5ab4d97c3e1b4cb1c662a11a46cea5c1fd1451f3)|2015-09-30 15:46:35
|110|jonasfj|New auth w. roles implemented|[URL](https://github.com/taskcluster/taskcluster-auth/commit/47fe608163e4a15f50a6303af37a6f802aa0a02b)|2015-09-30 15:37:12
|109|jonasfj|Improved handling of cache expiration|[URL](https://github.com/taskcluster/taskcluster-auth/commit/30121ad643de76e556d19f8880494ae5c66b1668)|2015-09-12 00:56:48
|108|jonasfj|First tests are now running|[URL](https://github.com/taskcluster/taskcluster-auth/commit/a48f807a342d53b49502d9761b2fd78a403726cd)|2015-09-11 23:45:38
|107|jonasfj|Gluing things together...|[URL](https://github.com/taskcluster/taskcluster-auth/commit/f17ba8535101cd1cfb59feef42d8448188912879)|2015-09-10 23:55:47
|106|jonasfj|Merge branch 'master' of github.com:taskcluster/taskcluster-auth|[URL](https://github.com/taskcluster/taskcluster-auth/commit/0f14146d6a56d5234d17ff8a6e6a6ada950d70ec)|2015-09-10 23:09:36
|105|petemoore|Revert "Fix bug" - see https://github.com/taskcluster/taskcluster-auth/commit/9f53e007789a71b76ce3efe51871af259e0a2784#commitcomment-13150232  This reverts commit eda0a6ab48042e15130aa9ac9c3cbd501e1b373a.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/b38ea26a7dbd061301fa92d1996b3023e18d6a74)|2015-09-10 09:54:16
|104|jonasfj|Used regexp again|[URL](https://github.com/taskcluster/taskcluster-auth/commit/e54635bdc7a8446eb8dc3535ef30e5b7fb8021ab)|2015-09-10 02:18:38
|103|jonasfj|Fix bug|[URL](https://github.com/taskcluster/taskcluster-auth/commit/eda0a6ab48042e15130aa9ac9c3cbd501e1b373a)|2015-09-10 02:11:54
|102|jonasfj|Added another test|[URL](https://github.com/taskcluster/taskcluster-auth/commit/0eb1c76e33016ddf833118f57e0290794d3ee893)|2015-09-10 00:23:25
|101|jonasfj|Added schemas for all API calls...|[URL](https://github.com/taskcluster/taskcluster-auth/commit/aa833835be080d67171516e189d354a764f1c6a6)|2015-09-10 00:23:12
|100|jonasfj|Lots of work...|[URL](https://github.com/taskcluster/taskcluster-auth/commit/c5a9910bb93e28e79aa52712cdd2b4f8d4b5ee7f)|2015-09-10 00:00:16
|99|petemoore|Merge pull request #10 from taskcluster/fix-tests  Fix tests, add License, add README badges|[URL](https://github.com/taskcluster/taskcluster-auth/commit/64cd104753eaf2e96ec72c0d561c3409dd004772)|2015-09-09 07:18:25
|98|jonasfj|Merge pull request #11 from petemoore/bug1202573  Updated slugid pattern to enforce uuid v4 compliance|[URL](https://github.com/taskcluster/taskcluster-auth/commit/168b8393ec9fb37c4e1c43cd7e00558b4deb77db)|2015-09-08 17:57:50
|97|petemoore|Merge pull request #12 from taskcluster/fix-tests-test  Try with 1500|[URL](https://github.com/taskcluster/taskcluster-auth/commit/fc7185026b697ced5b0fd601a506f59127c2dc85)|2015-09-08 17:26:57
|96|jonasfj|Try with 1500|[URL](https://github.com/taskcluster/taskcluster-auth/commit/171ceb62470bfe4fe101784e93f19f3c03e687be)|2015-09-08 17:22:25
|95|petemoore|Updated slugid pattern to ^[A-Za-z0-9_-]{8}[Q-T][A-Za-z0-9_-][CGKOSWaeimquy26-][A-Za-z0-9_-]{10}[AQgw]$|[URL](https://github.com/taskcluster/taskcluster-auth/commit/9f53e007789a71b76ce3efe51871af259e0a2784)|2015-09-08 15:31:34
|94|jonasfj|some work|[URL](https://github.com/taskcluster/taskcluster-auth/commit/75eeecc7053e8b94a365d1b254bcceed7f721369)|2015-09-07 21:06:21
|93|petemoore|Added LICENSE file|[URL](https://github.com/taskcluster/taskcluster-auth/commit/e67ae52748b478fc3ca7fdfcbc04ddbcf48dc600)|2015-09-07 12:53:47
|92|petemoore|Add badges to README.md|[URL](https://github.com/taskcluster/taskcluster-auth/commit/4907893e6d1d1d197a83c4d1e537e27f78b48a55)|2015-09-07 12:53:06
|91|petemoore|Fix travis tests by increasing timeout of web server|[URL](https://github.com/taskcluster/taskcluster-auth/commit/4f8ac6ceb50ef81bfc4baf60ea941a7440e0d90d)|2015-09-07 12:51:38
|90|jonasfj|renaming as requested by :mrrrgn|[URL](https://github.com/taskcluster/taskcluster-auth/commit/7b2a9f551489955279a8659236de97617e93728b)|2015-09-02 23:15:37
|89|jonasfj|Merge pull request #8 from taskcluster/remote-signature-validation  Remote signature validation|[URL](https://github.com/taskcluster/taskcluster-auth/commit/f90e5126d8e4af49416cc4f75abb411a05d1c772)|2015-09-02 20:44:52
|88|jonasfj|Fixed issues|[URL](https://github.com/taskcluster/taskcluster-auth/commit/0ac22f3d90939774fefaff1bf99cea715c4d6726)|2015-08-26 21:48:54
|87|jonasfj|Fixed issues|[URL](https://github.com/taskcluster/taskcluster-auth/commit/c58fd1c2da63485a74eb632f04d6156f06a29c71)|2015-08-26 21:46:51
|86|jonasfj|Updated to support payload validation|[URL](https://github.com/taskcluster/taskcluster-auth/commit/abfd034a838dcbdb94f1efe7c94d6f5b25a0c6c5)|2015-08-24 23:55:24
|85|jonasfj|fix load-test back to something sane|[URL](https://github.com/taskcluster/taskcluster-auth/commit/6b9b92e57fa9f09976396a6caee06b683c843940)|2015-08-19 17:58:17
|84|jonasfj|Test for an hour|[URL](https://github.com/taskcluster/taskcluster-auth/commit/167f645e310447f6f3a1bacb58696bfb57e0b018)|2015-08-15 05:32:37
|83|jonasfj|Test for an hour|[URL](https://github.com/taskcluster/taskcluster-auth/commit/9f77041d83288bde13bcfb91b7a92bba41145fdd)|2015-08-15 04:00:04
|82|jonasfj|fix load-test|[URL](https://github.com/taskcluster/taskcluster-auth/commit/1a91b21846e355a2552d87c1fa1f29862536950a)|2015-08-15 00:00:28
|81|jonasfj|fix load-test|[URL](https://github.com/taskcluster/taskcluster-auth/commit/5016fb45ef520740b5f0e82c4979ac5f1f4dca82)|2015-08-14 22:48:03
|80|jonasfj|fix load-test|[URL](https://github.com/taskcluster/taskcluster-auth/commit/f081911fc9d720933d858508e83a5c4cd89cc51c)|2015-08-14 22:05:16
|79|jonasfj|big load-test|[URL](https://github.com/taskcluster/taskcluster-auth/commit/accb2f43cf4e75ed0e8b201046eac2b484e857af)|2015-08-14 22:02:57
|78|jonasfj|fix load-test|[URL](https://github.com/taskcluster/taskcluster-auth/commit/b16ebfa1dde1045f26e7879ac8cf0c8e46062ac4)|2015-08-14 21:55:09
|77|jonasfj|try to specify node and npm version differently|[URL](https://github.com/taskcluster/taskcluster-auth/commit/7b28b6cada2fdccf2cce4262de2a3239324577d7)|2015-08-14 21:48:07
|76|jonasfj|Forgot to auth|[URL](https://github.com/taskcluster/taskcluster-auth/commit/811091a8c9ed543f584318fed031184d6d9c64d8)|2015-08-14 21:47:04
|75|jonasfj|Forgot tc clinet|[URL](https://github.com/taskcluster/taskcluster-auth/commit/caa9fd9c7c93f2b3a7cb0cd00a274a966ced8544)|2015-08-14 21:45:51
|74|jonasfj|Adding load-test binary|[URL](https://github.com/taskcluster/taskcluster-auth/commit/e858964c98a13d6299a8c9e8328d2951fb83e6bb)|2015-08-14 21:42:58
|73|jonasfj|Updated procfile|[URL](https://github.com/taskcluster/taskcluster-auth/commit/94c2a2ed33295238a5aee9047e4e65f3f40bf9b6)|2015-08-14 21:13:59
|72|jonasfj|Add fix load-test|[URL](https://github.com/taskcluster/taskcluster-auth/commit/de9dde094bd3ef4b5603d78793a302b6b4ac52b3)|2015-08-14 00:35:26
|71|jonasfj|config for load-testing|[URL](https://github.com/taskcluster/taskcluster-auth/commit/3dc8de522f87ac2e55e13e91d0203efc63ad9ba9)|2015-08-14 00:28:36
|70|jonasfj|API end-point + test for remote signature validation|[URL](https://github.com/taskcluster/taskcluster-auth/commit/0b3f524f369f3b5fd7165c59fbaf02ce8dc4bb37)|2015-08-13 02:35:04
|69|jonasfj|Converted to use remote-signature-interface|[URL](https://github.com/taskcluster/taskcluster-auth/commit/cb6a587aef0b14c3950a9f59b3817aff677519ca)|2015-08-12 22:32:51
|68|jonasfj|Ported to base.testing.schemas|[URL](https://github.com/taskcluster/taskcluster-auth/commit/c2227d38242ce689f6579a05e9b95af072097d43)|2015-08-12 21:48:28
|67|petemoore|trivial grammatical correction|[URL](https://github.com/taskcluster/taskcluster-auth/commit/111910c7b8b7889523809b3dd25225bd23f4694d)|2015-08-06 12:18:33
|66|jonasfj|Merge pull request #6 from djmitche/bug1184272  Bug 1184272: specify all API scopes as [[str]]|[URL](https://github.com/taskcluster/taskcluster-auth/commit/9c862be30443a27ba4c3e51516b4fb2a449e311e)|2015-07-24 18:41:11
|65|djmitche|Bug 1184272: specify all API scopes as [[str]]|[URL](https://github.com/taskcluster/taskcluster-auth/commit/2b0438b1e4ebc29dfb326173953d3066026af28e)|2015-07-24 18:16:16
|64|jonasfj|Merge pull request #5 from djmitche/docstring-edit  Miscellaneous docstring edits|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ee6646e279608af504fb0da01298d47b390739ec)|2015-07-07 22:27:51
|63|djmitche|Miscellaneous docstring edits|[URL](https://github.com/taskcluster/taskcluster-auth/commit/35be5eb20d5f3db5928ada02a4e8f76323be0dda)|2015-07-06 21:40:48
|62|jonasfj|Upgrade tc-base|[URL](https://github.com/taskcluster/taskcluster-auth/commit/a6e31174a1b37c3029ec2bad97dcb959d739ae1c)|2015-06-09 23:02:46
|61|jonasfj|Update Procfile to use babel-node|[URL](https://github.com/taskcluster/taskcluster-auth/commit/f86ce0de8c0605fa9f65b52d903dfe834b7543ad)|2015-06-09 22:48:54
|60|jonasfj|Merge pull request #4 from taskcluster/import-export  Added import/export - ported a lot to babeljs|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ea177be4cb3ea78196e9458bda9e5ff7691239a9)|2015-06-03 20:30:44
|59|jonasfj|Added import/export - ported a lot to babeljs|[URL](https://github.com/taskcluster/taskcluster-auth/commit/7db91318d97dc7dd3bfe066954eb3471a7c877f6)|2015-05-28 18:36:46
|58|jonasfj|Added access for mgsei.com contractors|[URL](https://github.com/taskcluster/taskcluster-auth/commit/bf4f6f3579582af4ee53b3a2b1772920f3861761)|2015-05-15 17:16:09
|57|jonasfj|Granting access for @qanalydocs.com email addresses|[URL](https://github.com/taskcluster/taskcluster-auth/commit/10ec52ce53513a33da79aa9f1a568024a5ab59ee)|2015-05-01 17:18:27
|56|jonasfj|Changed "auth:client-clients" ->  "auth:list-clients"|[URL](https://github.com/taskcluster/taskcluster-auth/commit/6dca48f2e3fb6f290642308d426f027c36e47d27)|2015-04-29 23:52:21
|55|jonasfj|Merge pull request #3 from taskcluster/config-temp-client  Configured ClientId used for temp creds|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ac36a2d65d9909efe49cec258a939e47320279e5)|2015-04-20 18:07:36
|54|jonasfj|Fixed bugs...|[URL](https://github.com/taskcluster/taskcluster-auth/commit/d649f9531a8d623606df2427bb2eb95707232f39)|2015-04-17 00:50:31
|53|jonasfj|Update travis file|[URL](https://github.com/taskcluster/taskcluster-auth/commit/96e57122afa5ccabf0a3c4767123c3b7f46f3679)|2015-04-17 00:43:29
|52|jonasfj|Configured ClientId used for temp creds|[URL](https://github.com/taskcluster/taskcluster-auth/commit/9c0f28fee51e87ad582b105ff820a9e9e9bece97)|2015-04-16 23:51:13
|51|jonasfj|API key changed... we don't want to deploy with travis anyways. so removing it|[URL](https://github.com/taskcluster/taskcluster-auth/commit/17cff9af50f019a30e60beb0d1f81a2a9126880c)|2015-03-11 00:29:03
|50|jonasfj|Updated test config|[URL](https://github.com/taskcluster/taskcluster-auth/commit/d77687ea2d8b9d97bc5212b3600e2368a9ed5f61)|2015-03-11 00:23:59
|49|jonasfj|Require prefix for S3 delegration to not start with a slash|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ec1b160b88c0f8c36c08d5f4db6717ba4436e82c)|2015-03-11 00:16:57
|48|jonasfj|Finished up adding S3 delegation support|[URL](https://github.com/taskcluster/taskcluster-auth/commit/77441ff3cb88a862f46c6e02a6eb31a54794e290)|2015-02-23 02:08:38
|47|jonasfj|Initial work for issuing STS credentials for S3...|[URL](https://github.com/taskcluster/taskcluster-auth/commit/7d81181159bc402d9353bd0bf42723c93f94a2cb)|2015-02-09 02:45:02
|46|jonasfj|Added test for bug 1123681|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ce0629817d80861dc2046523ca7b7f8a6f70ee86)|2015-01-20 17:37:11
|45|jonasfj|Merge pull request #1 from taskcluster/fix-missing-lodash  Import the lodash library to be able to use it|[URL](https://github.com/taskcluster/taskcluster-auth/commit/13ded9adfb244a60821b6d0d1762984d4e666186)|2015-01-20 17:36:32
|44|jhford|Import the lodash library to be able to use it|[URL](https://github.com/taskcluster/taskcluster-auth/commit/8b7f5553c0f946b51893a71c3006e693e5893d2f)|2015-01-20 14:52:15
|43|jonasfj|Ensure azure table before handing out SAS credentials|[URL](https://github.com/taskcluster/taskcluster-auth/commit/c88fafaef3910db6abc349baefb675173fcdb3de)|2015-01-09 21:43:17
|42|jonasfj|Changed how we configure azureAccounts|[URL](https://github.com/taskcluster/taskcluster-auth/commit/e362f9ecc34444cc1f5a549cc97adba30083e233)|2015-01-06 23:02:30
|41|jonasfj|Test config|[URL](https://github.com/taskcluster/taskcluster-auth/commit/605867168275d9fd79caa9d118631a79720b9ac4)|2015-01-06 22:57:38
|40|jonasfj|Test config|[URL](https://github.com/taskcluster/taskcluster-auth/commit/00eee2385a6def568e984350f21d469d0a527462)|2015-01-06 22:48:33
|39|jonasfj|Test config|[URL](https://github.com/taskcluster/taskcluster-auth/commit/790ec4509de1993067a8fe0c8a0c382a1bdc9dd3)|2015-01-06 22:44:04
|38|jonasfj|Test config|[URL](https://github.com/taskcluster/taskcluster-auth/commit/4353310b9ec1f3a246d0f3df75a6276efb24aa61)|2015-01-06 22:40:58
|37|jonasfj|Test config|[URL](https://github.com/taskcluster/taskcluster-auth/commit/bdaa2a7a2ca2d3dc523090c59deadf551636c077)|2015-01-06 22:38:35
|36|jonasfj|Added azureTableSAS for delegating access using SAS|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ace76655f3202835b67fd61a2a7552e940bf49dc)|2015-01-06 21:48:28
|35|jonasfj|Merged|[URL](https://github.com/taskcluster/taskcluster-auth/commit/e070efac1fdeb5d2df81646b5c398edf7740674f)|2014-10-29 00:45:19
|34|jonasfj|Add schemas for all API calles, converted existing schemas to yaml|[URL](https://github.com/taskcluster/taskcluster-auth/commit/45d16439be10072e185529851b923c054465511f)|2014-10-29 00:43:40
|33|jonasfj|Minor cleanup removed lots of old files|[URL](https://github.com/taskcluster/taskcluster-auth/commit/92842a7e3863376c85008527ecab3f2a4a635e51)|2014-10-28 22:29:57
|32|jonasfj|Removed old UI, API only access and UI for delegation|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ecf32b7c0a572b5534e710d1ae7b442740d70437)|2014-10-16 18:50:29
|31|lightsofapollo|fix promies resolve|[URL](https://github.com/taskcluster/taskcluster-auth/commit/008dd2bb4a034857de4af6cedff9a7aae8d982ed)|2014-10-16 16:47:30
|30|jonasfj|Configured travis for deployment and tests|[URL](https://github.com/taskcluster/taskcluster-auth/commit/51b0103cf3d7710174cc75cd944accc20d68d296)|2014-10-13 17:39:26
|29|jonasfj|More API methods|[URL](https://github.com/taskcluster/taskcluster-auth/commit/863141f3a40add61466030107a23c223085633de)|2014-10-11 23:34:14
|28|jonasfj|Removed node_modules|[URL](https://github.com/taskcluster/taskcluster-auth/commit/4b7247f48713316f47c3400ac6d5e8b7f8b9d00e)|2014-10-10 20:04:31
|27|jonasfj|Updated to latest taskcluster-base|[URL](https://github.com/taskcluster/taskcluster-auth/commit/292653ff575b3438be9708bd91a23984ddfe1fa0)|2014-08-12 21:18:21
|26|jonasfj|Upgraded taskcluster-base to a version and will trust proxy|[URL](https://github.com/taskcluster/taskcluster-auth/commit/a2c6798ae126185a0e7a5de2df5ba88e49ec344b)|2014-08-02 00:10:13
|25|jonasfj|Added configuration necessary for deployment|[URL](https://github.com/taskcluster/taskcluster-auth/commit/242d1867c1dfc69ff60b0254f4ac9e6501bb550b)|2014-08-02 00:04:53
|24|jonasfj|Upgraded taskcluster-base|[URL](https://github.com/taskcluster/taskcluster-auth/commit/105a832ac5ad4aa533115f8cb3a9eaaf2a21ca18)|2014-08-02 00:00:31
|23|jonasfj|Upgraded taskcluster-base to fix nonceManager|[URL](https://github.com/taskcluster/taskcluster-auth/commit/105e1dccfab57e3eee6479129230a93715c5ba1a)|2014-07-30 02:14:24
|22|jonasfj|Updating production config to use HTTPS from defaults|[URL](https://github.com/taskcluster/taskcluster-auth/commit/8de17baf24b6b5d37d2fa90c362f81b442648250)|2014-07-29 23:11:48
|21|jonasfj|Try new taskclustre-base with X-Forwarded-Port|[URL](https://github.com/taskcluster/taskcluster-auth/commit/335cca9f81213b9eba0293d4c7841fb0542001ec)|2014-07-29 22:00:53
|20|jonasfj|Upgraded packages|[URL](https://github.com/taskcluster/taskcluster-auth/commit/933c9f4d101c60a02ba3904f182108e86a3e7a51)|2014-07-25 00:03:06
|19|jonasfj|New taskcluster-base release|[URL](https://github.com/taskcluster/taskcluster-auth/commit/c5236c769111db7824f19e48c2947f4a31a57152)|2014-06-04 21:50:02
|18|jonasfj|Fixed API|[URL](https://github.com/taskcluster/taskcluster-auth/commit/23bd19b7e870055029e4561675f9cab4f4d12d84)|2014-06-04 20:26:46
|17|jonasfj|Update taskcluster-base|[URL](https://github.com/taskcluster/taskcluster-auth/commit/c455f25cd2052c0ef8ccdcb818f25b0e566f57b1)|2014-06-04 19:20:53
|16|jonasfj|Fixed spelling error|[URL](https://github.com/taskcluster/taskcluster-auth/commit/1d27d2153a285b18b2e49613fcded3f99c6a5739)|2014-05-29 02:41:53
|15|jonasfj|Fix spelling error|[URL](https://github.com/taskcluster/taskcluster-auth/commit/6b599627a4d37a66382ac2596b04cd9789419ef3)|2014-05-22 17:24:00
|14|jonasfj|Fixing spelling error|[URL](https://github.com/taskcluster/taskcluster-auth/commit/304b09b83a0b439692393cf17e37305d01ac91c4)|2014-05-21 23:56:59
|13|jonasfj|Ups added _|[URL](https://github.com/taskcluster/taskcluster-auth/commit/11cbd31e584af757a8fbf729fbdb39c238e11a8e)|2014-05-21 21:27:22
|12|jonasfj|Forgot promis|[URL](https://github.com/taskcluster/taskcluster-auth/commit/0d3d5977351aeb174f0f1528df8b5eb48b893672)|2014-05-21 21:17:53
|11|jonasfj|CreateTable in server.js|[URL](https://github.com/taskcluster/taskcluster-auth/commit/c7fd865860c571e4d6519afc924af270193aec23)|2014-05-21 21:16:33
|10|jonasfj|Adding production config|[URL](https://github.com/taskcluster/taskcluster-auth/commit/7827f6769fc20296ba928202474e2378bad2c657)|2014-05-21 20:57:19
|9|jonasfj|Updated README and now trying it works on travis|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ab2093dc234c1e5ec16296fe9aa64f1c6ff52414)|2014-05-21 00:01:57
|8|jonasfj|npm install mocha|[URL](https://github.com/taskcluster/taskcluster-auth/commit/919d8004b0b1d6e150029cc03f68c67ef0d6e2cc)|2014-05-20 23:58:22
|7|jonasfj|Add schemas and tests for schemas|[URL](https://github.com/taskcluster/taskcluster-auth/commit/0b20fe16143cb97e1a55e973e34b5d5c2583d00f)|2014-05-20 23:57:43
|6|jonasfj|Reduced number of dependencies as we use them through taskcluster-base|[URL](https://github.com/taskcluster/taskcluster-auth/commit/eb83433d322320c0cc7ccf1d3c67f59764038091)|2014-05-20 23:04:44
|5|jonasfj|Utils are not in taskcluster-base|[URL](https://github.com/taskcluster/taskcluster-auth/commit/998fd1a1cee020b8b701a80a54fef9d1df10f8ea)|2014-05-20 23:02:11
|4|jonasfj|Updating Procfile|[URL](https://github.com/taskcluster/taskcluster-auth/commit/835b6a80b408732b6306bf56948acca7209f6fb7)|2014-05-20 23:01:02
|3|jonasfj|Remove hack.js|[URL](https://github.com/taskcluster/taskcluster-auth/commit/475aa813767d846cc4b6c6bdb0d9666895df28b6)|2014-05-20 22:59:49
|2|jonasfj|Port to taskcluster-base|[URL](https://github.com/taskcluster/taskcluster-auth/commit/5b10bc5700f4361d47ccbd7e209b2e9424001c73)|2014-05-20 22:56:24
|1|jonasfj|Port to taskcluster-base|[URL](https://github.com/taskcluster/taskcluster-auth/commit/061629bc991798440052e4416f009874b3d48a25)|2014-05-20 22:55:57



