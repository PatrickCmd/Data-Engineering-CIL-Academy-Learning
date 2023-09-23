# PRACTICAL INTRODUCTION TO CI/CD ON AWS

## Resources / References
- [**Redhat - What is CI/CD?**](https://www.redhat.com/en/topics/devops/what-is-ci-cd)

## What is CI/CD?
CI/CD is a method to frequently deliver **apps** to customers by introducing **automation** into the stages of **app development**. The main concepts attributed to CI/CD are **continuous integration**, **continuous delivery**, and **continuous deployment**. CI/CD is a solution to the problems integrating new code can cause for development and operations teams (AKA "integration hell").

### What's the difference between CI and CD (and the other CD)?
The acronym CI/CD has a few different meanings. The "CI" in CI/CD always refers to continuous integration, which is an automation process for developers. Successful CI means new code changes to an app are regularly built, tested, and merged to a shared repository. It’s a solution to the problem of having too many branches of an app in development at once that might conflict with each other.

The "CD" in CI/CD refers to continuous delivery and/or continuous deployment, which are related concepts that sometimes get used interchangeably. Both are about automating further stages of the pipeline, but they’re sometimes used separately to illustrate just how much automation is happening.

Continuous delivery usually means a developer’s changes to an application are automatically bug tested and uploaded to a repository (like GitHub or a container registry), where they can then be deployed to a live production environment by the operations team. It’s an answer to the problem of poor visibility and communication between dev and business teams. To that end, the purpose of continuous delivery is to ensure that it takes minimal effort to deploy new code.

Continuous deployment (the other possible "CD") can refer to automatically releasing a developer’s changes from the repository to production, where it is usable by customers. It addresses the problem of overloading operations teams with manual processes that slow down app delivery. It builds on the benefits of continuous delivery by automating the next stage in the pipeline.

![CI-CD Flow](images/ci-cd-flow-desktop.png)

### Continuous integration
In modern application development, the goal is to have multiple developers working simultaneously on different features of the same app. However, if an organization is set up to merge all branching source code together on one day (known as “merge day”), the resulting work can be tedious, manual, and time-intensive. That’s because when a developer working in isolation makes a change to an application, there’s a chance it will conflict with different changes being simultaneously made by other developers. This problem can be further compounded if each developer has customized their own local integrated development environment (IDE), rather than the team agreeing on one cloud-based IDE.

Continuous integration (CI) helps developers merge their code changes back to a shared branch, or “trunk,” more frequently—sometimes even daily. Once a developer’s changes to an application are merged, those changes are validated by automatically building the application and running different levels of automated testing, typically unit and integration tests, to ensure the changes haven’t broken the app. This means testing everything from classes and function to the different modules that comprise the entire app. If automated testing discovers a conflict between new and existing code, CI makes it easier to fix those bugs quickly and often.

### Continuous delivery
Following the automation of builds and unit and integration testing in CI, continuous delivery automates the release of that validated code to a repository. So, in order to have an effective continuous delivery process, it’s important that CI is already built into your development pipeline. The goal of continuous delivery is to have a codebase that is always ready for deployment to a production environment.

In continuous delivery, every stage—from the merger of code changes to the delivery of production-ready builds—involves test automation and code release automation. At the end of that process, the operations team is able to deploy an app to production quickly and easily.

### Continuous deployment
The final stage of a mature CI/CD pipeline is continuous deployment. As an extension of continuous delivery, which automates the release of a production-ready build to a code repository, continuous deployment automates releasing an app to production. Because there is no manual gate at the stage of the pipeline before production, continuous deployment relies heavily on well-designed test automation.

In practice, continuous deployment means that a developer’s change to a cloud application could go live within minutes of writing it (assuming it passes automated testing). This makes it much easier to continuously receive and incorporate user feedback. Taken together, all of these connected CI/CD practices make deployment of an application less risky, whereby it’s easier to release changes to apps in small pieces, rather than all at once. There’s also a lot of upfront investment, though, since automated tests will need to be written to accommodate a variety of testing and release stages in the CI/CD pipeline.

### What are some common CI/CD tools?
CI/CD tools can help a team automate their development, deployment, and testing. Some tools specifically handle the integration (CI) side, some manage development and deployment (CD), while others specialize in continuous testing or related functions.

One of the best known open source tools for CI/CD is the automation server [**Jenkins**](https://www.jenkins.io/). Jenkins is designed to handle anything from a simple CI server to a complete CD hub. See [**documentation**](https://www.jenkins.io/doc/)

[**Tekton Pipelines**](https://tekton.dev/) is a CI/CD framework for Kubernetes platforms that provides a standard cloud-native CI/CD experience with containers.

Beyond Jenkins and Tekton Pipelines, other open source CI/CD tools you may wish to investigate include:

- [**Spinnaker**](https://spinnaker.io/), a CD platform built for [multicloud](https://www.redhat.com/en/topics/cloud-computing/what-is-multicloud?cicd=32h281b) environments.

- [**GoCD**](https://www.gocd.org/), a CI/CD server with an emphasis on modeling and visualization.

- [**Concourse**](https://concourse-ci.org/), "an open-source continuous thing-doer."

- [**Screwdriver**](https://screwdriver.cd/), a build platform designed for CD.

Teams may also want to consider managed CI/CD tools, which are available from a variety of vendors. The major public cloud providers all offer CI/CD solutions, along with [GitLab](https://about.gitlab.com/), [CircleCI](https://circleci.com/), [Travis CI](https://www.travis-ci.com/), [Atlassian Bamboo](https://www.atlassian.com/software/bamboo), and many others.

Additionally, any tool that’s foundational to DevOps is likely to be part of a CI/CD process. Tools for configuration automation (such as [Ansible](https://www.redhat.com/en/technologies/management/ansible?cicd=32h281b), [Chef](https://www.chef.io/), and [Puppet](https://puppet.com/)), container runtimes (such as Docker, rkt, and cri-o), and container orchestration (Kubernetes) aren’t strictly CI/CD tools, but they’ll show up in many CI/CD workflows.

