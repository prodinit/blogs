# How we develop a custom autoscaling metrics based on number of tasks in the queues?

This blog will illustrate a use case which was solved by developing a custom autoscaling metrics. We will hunt into a critical problem statement: **dynamically scaling an asynchronous distributed web application to handle variable loads**.

The solution we're about to explore was successfully implemented in a Django Celery Redis based asynchronous application, deployed on AWS ECS (Elastic Container Service). While the solution is demonstrated within this tech stack, the underlying concept can be replicated in other programming languages when deployed in a similar fashion.

## Basics of sistributed systems

<figure><img src="https://media.geeksforgeeks.org/wp-content/uploads/20221210223508/Screenshot-from-2022-12-10-22-34-49.png" alt=""><figcaption></figcaption></figure>

Let's explore the functioning of distributed systems. In essence, distributed systems comprise of independent computers systems linked through a central system, often represented by a message broker. Most problems that need scaling these days will need to scale beyond a single computer, maybe for a short period of time but it is required.

In our scenario, the Django application, serving as our primary program, distributes tasks into independent sets, pushing them into a Redis queue. These queues are then linked to Celery workers, that retrieve tasks from the queue, execute them, and store the results back in Redis or another designated database.

## What was the problem?

With the prerequisites in place, let's deep dive into the specific challenge we encountered and how we addressed it. Our primary issue revolved around the management of numerous asynchronous tasks requiring processing. We had designated queues for different task types, each aligned with a specific Celery worker. However, the workload on these workers proved unpredictable. At times, a queue could be flooded with thousands and thousands of concurrent tasks demanding swift processing, while at other times, it might be completely empty. Simultaneously, other Celery workers could remain idle because their associated queues were empty.

Traditional autoscaling solutions based on CPU and memory proved inadequate due to the unpredictable nature of the workload.

## Possible Solutions

Consideration of possible solutions brings us to the concept of running a fixed number of Celery workers aligned with our workload. However, this approach poses a challenge during periods of less number of  task, leaving resources idle and adding unnecessary cloud costs.

As for the AWS autoscaling group, the asynchronous tasks are not necessarily CPU heavy or memory heavy tasks. It could happen that even if we have a high number of tasks, the CPU/memory didn’t shoot up.

We require a solution that can dynamically adapt to the flow of asynchronous tasks without relying on CPU or memory metrics.

## Key points for a optimal solutions

An optimal solution should encompass several key features to effectively address the outlined challenges:


- The solution should continuously monitor the number of tasks in the Redis queue, allowing for real-time assessment of the workload.

- The system should employ a robust algorithm to calculate the optimal number of Celery workers required to process the tasks within a specified timeframe.

- The solution must offer configurable parameters to control the maximum and minimum number of Celery workers or ECS services, preventing excessive scaling that could lead to increased costs.

- It should be designed to avoid unnecessary scaling down when workers are actively processing tasks, ensuring efficient handling of ongoing workload.

- Consideration should be given to optimizing costs by dynamically adjusting the worker count based on the immediate celery worker demand.

## Solution

We created a solution which had the following components.

### Monitoring Logic
- We had a monitoring service which takes care of the number of tasks present in N number of queues.
- Our monitoring logic keeps track of active and reserved tasks in a particular queue. And also keeps track if the number of tasks in a queue are above threshold or not. If they are above, it sends a message to our scaling server to autoscale up after calculating how many extra celery workers are required to handle the variable load. Along with the active and reserved tasks, we track the failed and the retry tasks to get the actual count to tasks. Also, time taken to launch a new celery worker in AWS ECS should also be considered in our scaling up and monitoring logic.

### Configuration Model
- We had a configuration model, which includes configurations such as max task count threshold to scale up, min task count threshold to scale down. Min celery workers, max celery workers.

### Scaling Service
- We had a scaling service as well. for example if the max task count threshold to scale up is 1000 tasks. When our monitoring service encounters a queue with more than 1000 tasks, it sends a message to our scaling service, and our scaling service scales up the celery worker. 

1 celery worker = 2 tasks in 1 min

X celery workers = 1000 tasks in 1 min => 500 workers

X celery workers = 1000 tasks in 100 mins => 5 workers


## Few points we considered while implementing the solution:

- Frequency of Task Monitoring:: The consideration of how frequently to check the number of tasks in queues is crucial for striking a balance between real-time responsiveness and minimizing unnecessary overhead. This decision impacts the system's ability to adapt swiftly to changing workloads while avoiding unnecessary resource consumption.

- Calculation of Celery Workers: How to calculate the number of celery workers required to complete X number of tasks in Y time.

- Downscaling without task loss: The concern about downsizing without affecting ongoing tasks is pivotal for maintaining a smooth and uninterrupted workflow. This consideration likely involves mechanisms to gracefully handle the transition, allowing in-progress tasks to complete without disruption before scaling down.

## Results
#### We developed a custom auto scaling solution which scales our architecture based on variable load, which helped us save time and money.

## Open Source

Open-sourcing the solution is a fantastic idea, especially when you believe it can benefit other teams facing similar challenges. It aligns well with the collaborative nature of the open-source community and fosters knowledge sharing.

Here is the github link to repository. [https://github.com/prodinit/django-celery-autoscale](https://github.com/prodinit/django-celery-autoscale)
- Reach us out if you need help in integrations.
- Fork, clone and customize it according to your needs
- Open new issues if you want to grow this project and add more customisations and support.

#### Written by - [Dishant Sethi](https://linkedin.com/in/dishantsethi)

#### Tags

<a>
<img alt="AWS" src="https://img.shields.io/badge/AWS-8A2BE2" />
<a>
<img alt="Backend Engineering" src="https://img.shields.io/badge/Backend_Engineering-8A2BE2" />
<a>
<img alt="Devops" src="https://img.shields.io/badge/Devops-8A2BE2" />
<a>
<img alt="Python" src="https://img.shields.io/badge/Python-8A2BE2" />
</a>

### Enjoyed the blog? If so, you'll appreciate collaborating with the minds behind it as well.