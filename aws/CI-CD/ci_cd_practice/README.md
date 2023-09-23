# Introduction to CI/CD on AWS
In this project, you will learn how to configure a CI/CD pipeline on AWS using CloudFormation. The pipeline setup will be accomplished using CloudFormation, allowing you to enhance your CloudFormation skills while grasping the concept of creating a deployment pipeline. We will utilize both GitHub and CodeCommit as our code sources.

The repository you have cloned contains the following files:
- template.yml
- buildspec.yml
- README.md 
- index.html

Each of these files will play a role in this project.
### Follow the steps below carefully to set up your first pipeline on aws:
#### STEP 1: Repository Setup (GitHub as Source)
1. Navigate to your GitHub repository and create a new repository.
2. Leave the repository empty.
3. Refer to the steps outlined in this [video](https://www.youtube.com/watch?v=toFrROIhUHM) to generate a personal access token.
4. Make a note of the personal access token, your repository name, and your GitHub username, as you will require them in the upcoming steps.
#### STEP 2: Deploy Pipeline with CloudFormation
1. Log in to your AWS account and search for "CloudFormation" using the search bar.
2. Create a new stack on Cloudformation.
3. Choose the option to upload a template file and upload the **template.yml** file from this folder.
4. Input the necessary parameters **refer to STEP 1** and initiate the stack creation.
#### STEP 3: Push to the pipeline
1. Access the new repository you created in **STEP 1**
2. Add the **index.html** and **buildspec.yml** files from the current folder to the repository.
3. Commit the changes to the main branch.
4. Search for "CodePipeline" in the AWS console search bar to observe how the deployed code progresses through the pipeline stages.
#### STEP 4: Review Changes
1. Locate and click on the S3 bucket that ends with **-website-bucket**.
2. Access the bucket properties and find the **static website hosting** option.
3. Click on the provided URL to view the content of the **index.html** page that was pushed to the pipeline.
#### STEP 5: Push a New Update.
1. Modify the content of the **index.html** file as desired and push the update to the main branch.
2. Navigate to the AWS CodePipeline dashboard to observe how the new push to the main branch triggers the pipeline.
3. Once the pipeline successfully runs, return to S3, and click the static website URL to view the new update.
#### STEP 6: Repository Setup (CodeCommit as Source)
1. In the **Resources** section of **template.yml**, uncomment both the "Repository" and "SNSRepoTrigger" resources.
2. Scroll down to the CodePipeline Resource in the **template.yml** file and comment out the "GithubSource," then uncomment the "CodeCommit" source.
3. Save the changes.
#### STEP 7: Update the Cloudformation stack
1. Navigate to the CloudFormation dashboard in the AWS console and select the stack created in **Step 2**.
2. Update the stack with the modified **template.yml** file.
3. After the update completes, go to the CodePipeline dashboard to confirm that the pipeline source stage now uses CodeCommit.
#### STEP 8: Add Files to Codecommit Repository
1. Access the AWS CodeCommit dashboard on the console and locate the newly created repository.
2. Click on the repository and add the index.html and buildspec.yml files.
3. Commit the changes to the main branch.
4. Go to the pipeline to observe the impact of the CodeCommit push we performed.
#### STEP 9: Review Changes
1. Navigate to the S3 console and find the bucket used to deploy our application.
2. Locate the static website URL of the bucket in the bucket's properties section.
3. Click the URL to view the simple website once again.

Feel free to repeat **Step 5** to experience how changes in CodeCommit trigger updates to the website.
