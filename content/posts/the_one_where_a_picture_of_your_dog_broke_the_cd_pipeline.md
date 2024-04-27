---
title: "The one where a picture of your dog broke your CD pipeline"
tags: ['ai','ml','ops']
date: 2023-12-31
draft: false
---
It starts out innocent enough, on a frozen New Year's Eve afternoon. You are doing some final documentation cleanup - because it is New Year's Eve and not the best time for the team to be rolling out fresh feature code, and because updating the repo docs is usually a worthwhile endeavor in moments like this as part of good code hygiene. Being the clever and hilarious documentation author that you are, you hyperlink a picture of your dog Bash to a bash code block (pure pun magnificence, I might add).  Happy with your updates, you wait for CI to pass testing, linting, scanning etc. and solicit a pull request rubber stamp from the team.

![Bash is so destructive](/images/bash.png)

You are just about ready to close down your laptop when an alert pops up from AWS _CodeDeploy_: your deployment has failed. You assume it is a fluke - probably a failed resource allocation or something similar, all you did was add one line to a markdown file :man_shrugging:. So you retry. A few minutes pass, and then again the pipeline fails.
Upon closer inspection the error indicates that your `appspec.yaml` file has a syntax error, and the deploy was not able to complete. You look in GitHub and the `appspec.yaml` has not changed for a month.
An earlier pipeline with the same `appspec.yaml` built just fine three hours ago. Only one line of markdown has changed. What fresh hell is this?
I'll skip to the end (you can fill in several hours of searching and tweaking and pointless pull requests trying to find the suddenly offending character if you want the full experience): part of the _CodeDeploy_ configuration is to specify artifacts to be used during the ECS blue/green deployment flow - and you can specify `source` and `build` artifacts. As you would expect, `source` artifacts are a copy of your repository code checked out in the _source_ stage of your _CodePipeline_, while `build` artifacts are assets you created (and specified) during your _CodeBuild_ stage. Since the `appspec.yaml` was not altered during the build, I had naively chosen to use the file directly from the repo those many months ago. However, the `source` artifacts have a hard size limit of 3MB; once your repository grows to larger than this, the artifact fails to import and silently returns nothing.

Luckily, this "silent killer" is prominently documented in the [_CodePipeline_ docs](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome-introducing-artifacts.html) ... just kidding, there's no mention of it anywhere outside the troubleshooting guide. I appreciate the very Pythonic nature of that documentation style (don't document the constraints, just explain them in the errors page). Of course there's also no mention of the limit in the error - just that it cannot read the file. Happy New Year :tada:!
The fix is relatively easy - include the file in the build artifacts, switch to `build`, call it a day. The frustration is that CodeDeploy (like so many AWS services) feels less and less like a managed service product and more and more like piggybacking on found code. As if someone built the `source` artifact to handle a very specific use case, and it worked, and so that was the end of the development cycle for that feature. There are only about 6 fields in the _ECS Blue/Green_ deployment, and one of them can lead to your pipeline randomly failing when your codebase reaches a modest size. It is reflective of the AWS mentality of late - a complete fixation on shipping new services while barely supporting continuity for the old ones, with meaningful updates only for flagship products.
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzIxODkyMTA0LDI2NDQxNzY1OSwtMzE2OT
gwMzk0LDEwODAzNDY4MzFdfQ==
-->