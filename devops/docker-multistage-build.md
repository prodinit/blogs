# A comparision between multistage build and singlestage build in Docker

Image size is one of the essential considerations while build a production grade docker image. Container images often include development tools, libraries and other necessary application dependencies. These tools and dependencies can drastically increase the image size.

In this blog, we will see a size comparision between a single stage docker image and a multi stage docker image of a simple hello-world golang application.

Before build the image, Lets build a simple golang application. 

<figure><img src="https://i.ibb.co/jgg5PTH/Screenshot-2023-11-08-at-11-53-50-PM.png"><figcaption></figcaption></figure>

## Single stage dockerfile

```
FROM golang:alpine

ENV GO111MODULE=off
ENV CGO_ENABLED=0

WORKDIR /app
COPY ../app/ /app/
RUN go build -o .
EXPOSE 8080
CMD ./app
```

### Command to build the image
```
docker build -t singlestage:latest -f Dockerfile.singlestage .
```

Using the above dockerfile code, we can create a docker image of the golang application with only a single stage.
Lets check the size of the image.

<figure><img src="https://i.ibb.co/JCQkc5P/Screenshot-2023-11-09-at-12-05-01-AM.png"><figcaption></figcaption></figure>

Did you notice 247MB? That too for just a hello world application. Isn't it way too heavy. Multistage builds are here to rescue us.

## Multi stage docker build

```
############# Stage 1 #####################
FROM golang:alpine AS BUILD

ENV GO111MODULE=off
ENV CGO_ENABLED=0
WORKDIR /app
COPY ../app/ /app/
RUN go build -o .

############# Stage 2 #####################
FROM scratch
COPY --from=BUILD /app/app /app/app
ENTRYPOINT [ "/app/app" ]
```

### Command to build the image
```
docker build -t multistage:latest -f Dockerfile.multistage .
```

Using the above dockerfile code, we can create a docker image of the golang application with multi stage builds.

<figure><img src="https://i.ibb.co/2Zpm6fX/Screenshot-2023-11-09-at-12-17-17-AM.png"><figcaption></figcaption></figure>

###1.85MB docker image of the same hello world application.

74.89% lighter images.

We're constructing the image through a two-stage process. Initially, we employ a Golang base image, embed our code within it, and compile our executable file, App. Moving on to the next stage, we utilize a fresh Alpine base image, transferring the binary created in the previous step to this new stage.

This is just a small example. Imagine this for a large production grade application. Multistage builds are magical, if you haven’t explored it already – go ahead and do it.

#### Written by - [Dishant Sethi](https://linkedin.com/in/dishantsethi)

#### Tags

<a>
<img alt="Devops" src="https://img.shields.io/badge/Devops-8A2BE2" />
<a>
<img alt="Golang" src="https://img.shields.io/badge/Golang-8A2BE2" />
</a>

### Enjoyed the blog? If so, you'll appreciate collaborating with the minds behind it as well.