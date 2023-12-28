---
title: "A Complete Containerized CD Pipeline With AWS and Cloudflare for 2024"
date: 2023-12-27
draft: false
---
Recently I went about standing up a fresh Continuous Delivery pipeline for a new project. The project is a relatively standard containerized stack with nothing exceptional to speak of, and as our exploratory work was already in AWS I decided to launch this CD in AWS CodePipeline. Furthermore, we wanted to dogfood our long-term infra management (this project is infra abstraction/automation software) and so opted _not_ to use TerraForm or CloudFormation templates - that way we could have a fully "Clickops'd" infrastructure for our tools to reclaim and manage. Besides, Clickops is easy right?

To my surprise, nothing worked. Deploying CD for a very standard stack (details to follow) via GUI clicks is a bizarre dance filled with broken states and never-resolvable circular dependencies, magic file/variable names that are either not documented or documented incorrectly (like the variety of spellings for `appspec.yaml / AppSpec.yml / appsec.yml` across AWS CodeDeploy docs), cryptic error codes, and incompatible default settings. Some of this is nothing new - all the clouds have quirks. But I was taken off guard by just how bad, how completely _non-functional_ I was suddenly finding these services which I had used happily for years. 

Maybe I have gotten too comfortable with infra as code, or maybe ECS and CodePipeline have gotten significantly more brittle in the last year. Maybe this is the multiverse where AWS services are much, much worse and I am a lost traveler. Whatever the reason, I decided that once this project was successfully deployed I would codify the process, in detail, as a guide for others (and my future self). This is that guide.

## How To Guide: 
We are setting up a blue/green deployment of a containerized application. The application uses docker-compose locally with one application container, one db container, a sidecar container (in our case logging, but can be anything) and an nginx container to serve web content. In AWS our stack will be:

- CodePipeline to manage our blue/green deployment via CodeBuild and CodeDeploy
- A single ECS service running on Fargate
- A single Elastic Load Balencer
- ECR for storing our container images
- SecretsManager for managing our environment variables
- Github as our source code provider
- CloudFlare for our DNS and proxy provider

There are numerous security groups, IAM roles etc needed in combination to make this all work, along with support elements like ACM to store the CloudFlare origin cert that I won't directly call out here, but will be noted in the process.

This deploy will blue/green the whole of your container stack - this means if your sidecar(s) or nginx need to roll back they can also do so. The downside is that they are all built with every deploy. If you want to add more complex checking logic later to only build changed containers, go for it.
  
{{< box warning >}} 
**Do not skim this guide!** If you are like me, you normally skim over these things, copy the code examples, and refer back when you hit errors. **Don't do that.** The ClickOps process here is like a ritual dance, missing one tiny step will anger the AWS gods and _you will have to start over from the beginning._ Suck it up and read the whole thing, and follow exactly step by step, or pain will follow.
{{< /box >}}

### Legend
To minimize repetition I am going to use some shorthands:
- The :monocle_face: icon means **Copy exactly.** I know, AWS docs or a tutorial might claim you can change the filename or specify the path somewhere; my experience has been that not all the configs are respected, and often only the default paths/names actually work. If you choose to deviate, best of luck to you.
- The aws account number for the examples will be `123456789012`. You can find-replace with your account. 
- The project name will be `bash-dog`.  You can find-replace with your project name.
- The AWS region will be `us-east-2`. You can find-replace with your default region. 

### Steps
1. #### Start your magic files.
Our pipeline needs 3 files placed in the root directory of your project. 
- :monocle_face: The `taskdef.json` behaves similar to a docker-compose.yml in ECS 
- :monocle_face: The `appspec.yaml` file which pulls together the CodeDeploy deployment (_Note_: `appspec.yaml` is the correct, and AFAIK only working naming convention for this file). 
- :monocle_face: The `buildspec.yml`file which is similar to any CI actions file you may have used, it is basically a list of bash commands run in a "builder" context.
also note that `buildspec.yml` and `appspec.yaml` have different filetype suffixes. Yay. 

Here are the files you should start with. 

{{< gist norton120 61e9a94f035da8202ab74e41e1705087 >}}

I strongly suggest cloning them as-is and updating only the elements as you follow along. To quick copy them to your project root (where they must live): 
```
cd bash-dog/ # your project root
curl https://gist.githubusercontent.com/norton120/61e9a94f035da8202ab74e41e1705087/raw/9b253c5ba06b05cbe1f6038d65b8690ffe088bd5/appspec.yaml > appspec.yaml
curl https://gist.githubusercontent.com/norton120/61e9a94f035da8202ab74e41e1705087/raw/9b253c5ba06b05cbe1f6038d65b8690ffe088bd5/taskdef.json > taskdef.json
curl https://gist.githubusercontent.com/norton120/61e9a94f035da8202ab74e41e1705087/raw/7ee3330bbbc33f3376cdc996a186cd0e90152e9a/buildspec.yml > buildspec.yml
```
Commit these files to your codebase. 

2. #### Making your project deploy-able
This is a whole other topic in itself, so I'll stick to the assumptions made with this current set of files and let you sort out what changes you may want to make:

- One dockerfile, named `Dockerfile`, contains all the image definitions for your deployment. 
- Each image to be deployed is targeted with the same name as the service you are deploying, i.e. the `api` image definition in your `Dockerfile` is defined as `FROM some-image:tag as api`. If this is foreign to you check out [Naming your Builds](https://docs.docker.com/build/building/multi-stage/#name-your-build-stages).
- Your code builds environment-agnostic, that is, the same build runs locally as in production. Things like requirements files and entrypoints are managed via an environment variable and not a different set of build steps. 
- Each service (i.e. container) runs on a different port. The `awsvpc` network addresses each of your containers via localhost (not the assigned container name!) so your containers cannot have port collisions.
- Only nginx will be exposed to the load balancer. Your nginx image needs to have an `nginx.conf` that routes traffic to all the other containers in your stack.
- Kinda goes without saying, but your nginx container should get port 80. We will be encrypting traffic from the load balancer to CloudFlare via origin cert (CloudFlare will handle client encryption), and restricting direct access to the container. 
Commit whatever changes you've made. For the duration of this deploy process it may save your sanity to turn off branch protection and deploy directly to main :scream:. Otherwise you will need to PR each tiny file tweak, and the PR process is basically valueless rubber-stamping in this case. 

3. #### ECR Images
This whole build process centers around container images stored in Elastic Container Registry (ECR). Navigate to ECR in the AWS GUI and click "Get Started" under "Create a Repository." 
![get started](/create_repository.png)
Name the repository with your project and service, i.e.`bash-dog-api` 
![name your repo](/repo_name.png)
:monocle_face: leave the defaults as they are. You need mutability to retag `latest`. Repeat for each of your services.
{{< box info >}} 
You _shouldn't_ need to worry about docker hub rate limits, because our `buildspec.yml` preloads your existing image as part of the pre-build, so CodeBuild will only pull from docker hub the first time you build. If this does become an issue for some reason (you start getting failed builds because of dockerhub limits for images like `niginx` and `python`) then you will want to add ECR repos for these base images as well and point your Dockerfile towards them. That requires local login to ECR and complicates things, so we will avoid it for now. Just keep in mind that if you run into this issue, you'll add these base images to everything we do here.
{{< /box >}}
Time to prime the pump: locally, log into your ECR registry with 
```
docker login --username AWS --password \
$(docker run \
-e AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} \
-e AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} \
-e AWS_SESSION_TOKEN=${AWS_SESSION_TOKEN} \
-e AWS_DEFAULT_REGION=${AWS_DEFAULT_REGION} \
--rm amazon/aws-cli ecr get-login-password) \
123456789012.dkr.ecr.us-east-2.amazonaws.com/bash-dog-api
```
_note_: this is using identity manager temporary creds. Use whatever strategy you prefer for authenticating the aws-cli container. 
Now build and tag your image:
```
docker build -f Dockerfile \
-t  123456789012.dkr.ecr.us-east-2.amazonaws.com/bash-dog-api \
--target api .
```
note the `--target` needs to match the target we are building. Once the build is successful, push it up
```
docker push 123456789012.dkr.ecr.us-east-2.amazonaws.com/bash-dog-api:latest
```
Rinse and repeat for each of the services you are deploying. Remember that `bash-dog-nginx` is our image of nginx with a custom `nginx.conf` mounted that will serve the sibling containers.

4. #### Secrets
We are going to keep all the envars in AWS SecretsManager. This removes secrets from our pipeline and repo code, and makes it less painful to update envars down the line. 
- Start by navigating to SecretsManager and clicking "Store a new Secret"
- select `other type of secret`
- set the key/value pairs. This should be in the format of `ENVAR_NAME` `value`. For example, if I want an envar `BASH_DOG_ENVIRONMENT` with a value of `production` it would look like this:
![secrets manager](/secretsmanager.png)
- name the secret something logical like `bash-dog/ecs-envars` and create it.
- Once created, refresh the index page and click into the new secret so you can get the _whole_ new arn (complete with the random suffix). 
- Head back to your `taskdef.json` file. See the `secrets` section in the api and sidecar containers? Update as follows:
	- for each envar you defined (and want for the given container), set a `name` key to match that envar (case sensitive). 
	- Update the arn with the whole new arn you just copied, paying special attention to the suffix on the arn. It must match the envar name you just set, and you need the 2 extra colons at the end. 
so setting our `BASH_DOG_ENVIRONMENT` envar in the api container would look like this:
```
...
"name": "bash-dog-api",
"secrets": [
	{
     "name":"BASH_DOG_ENVIRONMENT",
     "valueFrom":"arn:aws:secretsmanager:us-east-2:123456789012:secret:bash-dog/ecs-envars-PlIIOb:BASH_DOG_URL::"
    },
...
```
remember that this arn will be the one you just created, not the example arn above! 
- Be sure to delete any example envars you _aren't_ using, they will cause the pipeline to error if the secret or key does not exist.  
- If you have envars that conflict between containers (for example, if each container needs a different `HOSTNAME` envar) you will need to set up individual secrets for each container. Then reference them with the same pattern, just using the container-specific secret arns for each set of secrets. 
- Make sure references across containers use `localhost` and not the container names; this is one place I've found ECS `awsvpc` networking functions differently than a bridge docker network. so 
```
# bad
API_HOST=http://api-container-name:8080
# good
API_HOST=http://localhost:8080 
``` 
5. #### Artifact S3 Bucket
Your CodePipeline will manage state via _artifacts_; created by CodeBuild, consumed by CodeDeploy. You need a bucket for this. 
- Go to S3, create a logically named bucket, like `bash-dog-cd-artifacts`. Leave all the defaults.

6. #### Code Pipeline
I find it is much easier not to get twisted into a dependency pretzel if we start our pipeline at the very end, with the CodePipeline itself. 
- Navigate to _CodePipeline -> CreatePipeline_. 
- Name your new pipeline something sensible like `bash-dog-pipeline`.  
- Create a new service role, name it something sensible like `bash-dog-pipeline-role`.   :monocle_face: Leave "_Allow AWS CodePipeline to create a service role so it can be used with this new pipeline_" checked. (don't try to re-use an existing service role, or hand-roll your own... role. You will hate yourself if you do either of these things, and it just won't work). 
- Leave all the other defaults alone and click _Next_.
- In the next screen select `Github (Version 2)`. Follow the prompts to create a new Github Connection, and select your repository.
- :monocle_face: For _Branch name_ use your main branch `main` or equivalent. 
- Leave all the other defaults alone and click _Next_.
- Next, Create a build project inline by selecting AWS CodeBuild as the provider and then clicking _Create Project_. In the new window:
	-  name your build project something sensible like `bash-dog-build-project`.
	- :monocle_face: under _Additional configuration_ check 'restrict number of concurrent builds this project can start' and set the limit to 1.
	- For Environment select `Managed Image`, `EC2` `Amazon Linux` Operating system, `Standard` Runtime, and the :monocle_face:  `amazonlinux2-x86_64-standard:4.0` image (not the default!)
	- :monocle_face: Check '_Enable this flag..._' under _Privileged_. 
	- Leave the default _New service role_ and unless the provided role name is awful, leave it.
	- Optionally, reduce the timeouts. Generally my builds are running < 3 min, so if they are not done in 10 they are probably never going to be done. 
	- Leave _Use a buildspec file_ and :monocle_face: do not specify a file name. My experience has been that builds with a non-standard buildspec path fail periodically with issues finding the file.
	- Set up logging using logical names like `bash-dog` and `codebuild`.
- Skip the deploy stage for now, that needs to be backed-in from a running ECS Service.
- Save and create your new pipeline.
_Note:_ The pipeline will immediately build and fail. That's OK, we're far from done.

7. #### Update Build Role Access
Now we need to update the build service role, allowing it to:
	- login, pull and push our ECR images
	- write to our s3 artifact bucket
- Find that role you just created by searching IAM roles for `bash-dog` (well, your equivalent). It should look like `codebuild-bash-dog-pipeline-service-role` unless you changed it. It should also have a policy named something like `CodeBuildBasePolicy-bash-dog-pipeline-us-east-2`. Click into that.
-  Edit the policy and add these statements, updating the image and s3 bucket arns to match the images and s3 bucket you created earlier.
{{< gist norton120 d622626cb4ce4cace838ce1ec35f96ef >}}

8. #### Run a successful build
Push all the changes made so far to `main` in your application repo. If your main is already up to date, you will need to trigger it manually via the CodePipeline with the _Release Change_ button. Let it build, check the logs tab for errors, and with fate on your side you should see this:
![build success](/build_success.png)

Now for the fun part - navigate to the s3 bucket and find the path `bash-dog-pipeline/buildArtf/`. Look for an artifact with the newest timestamp. Download it. Now check out the `taskdef.json` file within the artifact. You'll see the images have been updated to reflect the image sha for the release you just built! 
You can also check ECR and see that the same image tag was created. 

9. Launching ECS
Now we can set up our runtime.   

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQwNDIzMTg5NywtMTgxOTUwNDkzNSwtND
YwNDM5OTcxLC0zMDg2Mjk4MjgsLTE2Mjc1ODE2Niw2MTU4ODk2
NzAsLTM2NTM4NTgyNywtMTY1Mjc5NjY4NywtOTA5MDE0MjYzLC
05MTY0ODYwNzEsMTcwNDQzNzIyNywyODAwMzc5NTUsLTEzNzE2
MTc1NTQsLTE1NTU3NTMwOTIsLTExNDU2NzY4MywxNTk3Mjg3Nz
gzLDIwMDc2MDg4NDMsLTg1MDE5MTAxOV19
-->