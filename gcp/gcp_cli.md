# GCP CLI

## Introduction to the GCP CLI
- [The gcloud CLI cheat sheet](https://cloud.google.com/sdk/docs/cheatsheet)
- [gcloud CLI overview](https://cloud.google.com/sdk/gcloud)
- [Google Cloud Command Line Interface (gcloud CLI)](https://cloud.google.com/cli?utm_source=youtube&utm_medium=unpaidsoc&utm_campaign=CDR_ret_businessapps_fbu_tf7uzqy_GoogleCloudCLI_031422&utm_content=description)


## Installation
- [Install Google Cloud SDK & CLI for Mac Linux & Windows](https://www.youtube.com/watch?v=k-8qFh8EfFA)
- [Google Cloud CLI & SDK Setup](https://www.codingforentrepreneurs.com/blog/google-cloud-cli-and-sdk-setup/)
- [gcloud | How to setup and configure gcloud command line tool and basic commands | gcloud tutorial](https://www.youtube.com/watch?v=q8jed3aU_FY)

Download Google Cloud CLI Package (gcloud) | Linux

```sh
wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-432.0.0-linux-x86_64.tar.gz
```

Open up Terminal or Command Line

```sh
mv google-cloud-cli-432.0.0-linux-x86_64.tar.gz ~/
cd ~/
```

Unpack the `tar` file

```sh
tar xopf google-cloud-cli-432.0.0-linux-x86_64.tar.gz
rm google-cloud-cli-432.0.0-linux-x86_64.tar.gz
```

Install `gcloud` on your `PATH`

```sh
cd google-cloud-sdk
./install.sh
```

Start a new `shell/terminal` for the changes to take effect

### Update glcoud

On your command line (`Terminal` or `PowerShell`), you should be able to run `gcloud` now:

```sh
gcloud --version
```

Let's update `gcloud`:

```sh
gcloud components update
```

## Scripting and Automation
- [Scripting with gcloud: a beginner’s guide to automating GCP tasks](https://cloud.google.com/blog/products/management-tools/scripting-with-gcloud-a-beginners-guide-to-automating-gcp-tasks)
- [gcloud init | Cloud SDK Documentation - the workflow that start after the installation](https://cloud.google.com/sdk/gcloud/reference/init)
- [gcloud auth login | Cloud SDK Documentation - the command to authenticate a user](https://cloud.google.com/sdk/gcloud/reference/auth/login)
- [gcloud auth activate-service-account | Cloud SDK Documentation - authenticate service account](https://cloud.google.com/sdk/gcloud/reference/auth/activate-service-account)


## Tutorials
- [Google Cloud Shell Tutorial for Beginners](https://www.youtube.com/watch?v=RdDyF3jVbbE)
- [Google Cloud Command Line for Beginners, or "How to gcloud" | 9.13.18 | Linux Academy](https://www.youtube.com/watch?v=j274vq9a2Rs)