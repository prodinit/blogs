# Ways to delete AWS ECR images

Since you are here, I'm sure that you are figuring out ways to clean the old and not required ECR images. But, before that lets talk about the basics. 

ECR is AWS managed elatic container registery is what everybody already aware of. It hosts images in a highly scalable and available architecture just like dockerhub/gitlab registery. 

It’s important to delete untagged and old images to maintain hygiene, sainity and to release the used storage space.

The pricing of AWS ECR is “$0.10 per GB / month for data stored in private or public repositories” and you would not unnecessarily want to pay for the storage spaces. **This price might look small to you, but as they say, drops make up the ocean. All these images, if put in store for a longer period, will add higher bills to your AWS invoices.**

Now that you have understood that you should clear these old and untagged images out of your ECR repositories because simply you do not need them, let's start discussing different ways to delete them.

## Delete them manually (eww 🤮)

As an engineer, this should never come to your mind as an ideal solution. This can/should only be used when you are the initial stages of your development and devops process. When you are doing a lot of hit and trial and creating images that doesn't meet the requirements.

The manual way is, you go to the AWS ECR console, select the images you dont need and delete them. Simple!

## Delete them using CLI (okay.. but..)

Similar to manual effort, deleting images from CLI is not going to be a periodic job, and, you everytime have to come and decide what needs to be deleted manually.

Configure AWS CLI and you can use the following command to delete an untagged ECR image.

```
aws ecr batch-delete-image --repository-name test-ecr-repo --image-ids imageTag=test-web-img
```

Here we are deleting the image tagged as `test-web-img` residing in the repository `test-ecr-repo`

## Running a periodic script in lambda

You are smart enough to configure a cloudwatch event to periodically trigger a lambda, which will run a script with a custom logic to delete unused/untagged/old images from ECR. 

<figure><img src="https://i.ibb.co/fQ4mF5L/get-ecr-images.png"><figcaption>Returns untagged images older than 15 days</figcaption></figure>

<figure><img src="https://i.ibb.co/bsvjZrH/describe-ecr-images.png" alt="describe-ecr-images"/><figcaption>A pagination function to return images based on nextToken value</figcaption></figure>

Now that you have the image ids in the required list of dict format. Simply pass the list of dict generated from the above function to the following code

```
ecr_client.batch_delete_image(
    repositoryName="test-ecr-repo",
    imageIds=get_imageids_to_delete()
)
```

Tada 🎉 ...

## ECR Lifecycle policy (Recommended in production)

So, ECR images comes with a lifecycle policy and you can customise the rules of policy according to your requirement. If you are comfortable with terrform, just a few lines of code can give a ECR lifecycle policy rule. Below is a sample ECR lifecycle rule which removes untagged images older than 15 days.

```
resource "aws_ecr_repository" "ecr_repo" {
 ...
}

resource "aws_ecr_lifecycle_policy" "ecr_lifecycle" {
  repository = aws_ecr_repository.ecr_repo.name

  policy = <<EOF
{
  "rules": [
    {
      "rulePriority": 1,
      "description": "Remove untagged images and images pushed before 15 days.",
      "selection": {
        "tagStatus": "untagged",
        "countType": "sinceImagePushed",
        "countUnit": "days",
        "countNumber": 15
      },
      "action": {
        "type": "expire"
      }
    }
  ]
}
EOF
}
```

Creating an ECR lifecycle policy and removing older images based on specific parameters is a straightforward process. AWS offers comprehensive documentation and sample lifecycle policies.

Additionally, you can explore different policies for tagged images, like criteria matching based on the upload date of the image.

#### Written by - [Dishant Sethi](https://linkedin.com/in/dishantsethi)

#### Tags

<a>
<img alt="AWS" src="https://img.shields.io/badge/AWS-8A2BE2" />
<a>
<img alt="Backend Engineering" src="https://img.shields.io/badge/Backend_Engineering-8A2BE2" />
<a>
<img alt="Devops" src="https://img.shields.io/badge/Devops-8A2BE2" />
</a>

### Enjoyed the blog? If so, you'll appreciate collaborating with the minds behind it as well.
