---
title: "The one where a picture of your dog broke your CD pipeline"
date: 2023-12-31
draft: true
---
It starts out innocent enough, on a frozen New Year's Eve afternoon. You are doing some final documentation cleanup - because it is New Year's Eve and not the best time for the team to be rolling out fresh feature code, and because updating the repo docs is usually a worthwhile endeavor in moments like this as part of good code hygiene. Being the clever and hilarious documentation author that you are, you hyperlink a picture of your dog Bash to a bash code block (pure pun magnificence, I might add).  Happy with your updates, you wait for CI to pass testing, linting, scanning etc. and solicit a pull request rubber stamp from the team. 

![Bash is so destructive](/images/bash.png)

You are just about ready to close down your laptop when an alert pops up from AWS _CodeDeploy_: your deployment has failed. You assume it is a fluke - probably a failed resource allocation or something similar, all you did was add one line to a markdown file :man_shrugging:. So you retry. A few minutes pass, and then again the pipeline fails. 
Upon closer inspection the error indicates that your `appspec.yaml` file has a syntax error, and the deploy was not able to complete. You look in GitHub and the `appspec.yaml` has not changed for a month. 
An earlier pipeline with the same `appspec.yaml` built just fine three hours ago. Only one line of markdown has changed. What fresh hell is this? 
I'll skip to the end (you can fill in several hours of searching and tweaking and pointless pull requests trying to find the suddenly offending character if you want the full experience): part of the _CodeDeploy_ configuration is to specify artifacts to be used during the ECS blue/green deployment flow - and you can specify `source` and `build` artifacts. As you would expect, `source` artifacts are a copy of your repository code checked out in the _source_ stage of your _CodePipeline_, while `build` artifacts are assets you created (and specified) during your _CodeBuild_ stage. Since the `appspec.yaml` was not altered during the build, I had naively chosen to use the file directly from the repo those many months ago. However, the `source` artifacts have a hard size limit of 3MB; once your repository grows to larger than this, the artifact fails to import and silently returns nothing. 

Luckily, this "silent killer" is prominently documented in the [_CodePipeline_ docs](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome-introducing-artifacts.html) ... just kidding, there's no mention of it anywhere outside the troubleshooting guide. I appreciate the very Pythonic nature of that documentation styl
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0OTMxMjk1NzIsMTA4MDM0NjgzMV19
-->