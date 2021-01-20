# Arkhn DevOps exercise

## Introduction

If you're there it means you've succesfully passed the first interview, congratulations :)

**It is now time to demonstrate your amazing skills!**

Don't worry if you don't already know all the tools we will be using through this exercise: reading documentation and learning is a part of it!
Depending on your knowledge of the several tools, this exercise may take about 1-4 hours.

There will be 4 steps, and the two last ones are optional: we don't expect you to finish all steps if you're completely unfamiliar with some concepts.
You will have to create a git repository (on github.com or somewhere else) with your work and a small documentation (a README.md like this one is enough) to explain how to use it.

## STEP 1: A small python program

First, you'll have to implement a basic algorithm that solves the following problem:

Given a string composed of the characters `(`, `)`, `[`, `]`, `{`, `}`, you need to tell if this string is balanced or not. What we call a balanced string is one where all the brackets are closed in the right order.

For instance, `([]){}` is balanced, whereas `([)]{}` or `(()` are not.

The input will whether come from the user launching the script or, if none is provided, your code should query a `generator` service which is provided in this repo.

### Generator server

You can launch the generator server with the following command:

```shell
python generator-server/src/server.py
```

It's a very basic flask application with a single http route: `/input`. With a `GET` query on this route, you'll be returned a response with an input string as text.
You can test the server with `curl http://localhost:5000/input` or directly in your browser.

### Solution behavior

Here is how your script should behave:

```shell
$> python your-solution.py ([]){}
INPUT: ([]){} -- RESULT: OK!
$> python your-solution.py ([)]{}
INPUT: (((] -- RESULT: BAD INPUT :(
$> python your-solution.py # Here, the input will be provided by the generator
INPUT: <generated input> -- RESULT: <...>
```

**NB**: If you really don't want to use Python, feel free to choose your favorite language.

## STEP 2: Dockerizing the program

**NB**: You need to install Docker for this step.

The goal of this step is to write a Dockerfile in order to containerize the python applications. The result is a docker image which can be used using `docker run <your_image>`.

The python program must behave the same way than when running it locally.

Example:

```shell
$> docker build -t solver .
$> docker run solver [({})]
INPUT: [({})] -- RESULT: OK!
$> docker run solver (((]
INPUT: (((] -- RESULT: BAD INPUT :(
$> docker run solver # ask the generator server when there are no input to the program
INPUT: {{()}} -- RESULT: BAD INPUT :(
```

**BONUS**: Write a `docker-compose.yml` file which runs both the generator server and the solver program when running `docker-compose up`.

## STEP 3: Using a CI to build a publish your docker image

**NB**: you need to have a DockerHub account for this step (it's free: [signup here](https://hub.docker.com/signup))

Now that you have a way to build a docker image for your service, we want to publish it to the docker registry. This can be done manually using `docker push <your_image>:<tag>`.

However, we want to automate the build process using a Continuous Integration (CI) pipeline. If you are familiar with a specific CI tool (jenkins, travis, GitlabCI...), feel free to use it. Otherwise, we encourage you to use Github's tool: [Github Actions](https://docs.github.com/en/actions/quickstart). You can get started in just a few minutes.

The goal of this exercise is to add a workflow for your repository that will build and push the docker image to the docker hub. And because I'm nice: [here are some instructions on how to do it](https://github.com/marketplace/actions/build-and-push-docker-images)

The CI workflow should be triggered by a commit on any branch. The examiner (me) should be able to `docker pull` your published docker image (it will be the case if the docker repository is public, which is the default).

## STEP 4: Ansible automation

**NB**: You need to install:

- [Vagrant](https://www.vagrantup.com/docs/installation) >= 2.2
- vagrant-disksize: `vagrant plugin install vagrant-disksize`

In this exercise, we want to deploy our dockerized services to a remote machine. Since it would be complex to provision a machine on the cloud, you will simply use a VM on your machine.
We provide a `Vagrantfile` in order to setup a VM on your machine. Here is the command you have to use to start the VM:

```shell
$> vagrant up ubuntu
```
