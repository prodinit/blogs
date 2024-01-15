# How to download/view code running in your lambda functions?

CloudWatch? Check. UI console? Check. Specific line I need? Nope. Debugging Lambdas is like playing hide-and-seek with your code.

<figure><img src="https://i.ibb.co/Kxr12nd/Screenshot-2024-01-15-at-11-56-50-PM.png" alt=""><figcaption></figcaption></figure>

While direct code modification in the console and immediate deployment to production should always be avoided, having visibility into the running code can be valuable, especially when working with branches containing extensive feature merges.

if you have lots of dependencies, it is easy to reach the 3M limit and having the console just showing the following warning:

> The deployment package of your Lambda function "xyz" is too large to enable inline code editing. However, you can still invoke your function.

### How can you check that code then?

Well, just use aws lambda get-function

```
aws lambda get-function --function-name YOUR_FUNCTION_NAME --query 'Code.Location' | xargs curl -o YOUR_FUNCTION_NAME.zip
```

Then it´s just a matter of unzip YOUR_FUNCTION_NAME.zip and you have the folder with all the content of the deployed package!

Happy debugging.

#### Written by - [Dishant Sethi](https://linkedin.com/in/dishantsethi)

#### Tags

<a>
<img alt="AWS" src="https://img.shields.io/badge/AWS-8A2BE2" />
<a>
<img alt="Devops" src="https://img.shields.io/badge/Devops-8A2BE2" />
</a>

### Enjoyed the blog? If so, you'll appreciate collaborating with the minds behind it as well.