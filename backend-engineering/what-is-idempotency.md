# What is idempotency?

You might ignore idempotency but not when you are a **fintech**.
Dealing with payments and not building idempotent APIs could be a nightmare.

But, What are idempotent APIs?
An idempotent API endpoint is one that can be called any number of times while guaranteeing that the operation will occur only once.

How to design an idempotent payment API?
1. Generate an idempotent key at the server side.
2. Send it along with the payment request.
3. Validate it before starting the payment process.
4. Refer to the flow diagram below.

<figure><img src="https://media.licdn.com/dms/image/D4D22AQHPuiQxtQautQ/feedshare-shrink_800/0/1695895451968?e=1700697600&v=beta&t=uqU0K5rUGWVR6r-1xz76bXxBV2Nu05RO51teVkjdEn8"></figure>

#### Written by - [Dishant Sethi](https://linkedin.com/in/dishantsethi)

#### Tags

<a>
<img alt="Backend Engineering" src="https://img.shields.io/badge/Backend_Engineering-8A2BE2" />
<a>
<img alt="Fintech" src="https://img.shields.io/badge/Fintech-8A2BE2" />
</a>

### Enjoyed the blog? If so, you'll appreciate collaborating with the minds behind it as well.
