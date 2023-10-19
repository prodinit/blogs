# Host your static website with s3, CloudFront, Route53, and domain from godaddy in 4 easy steps

Before getting our hands dirty, I would want you to sign-up for a free-tier account of AWS because it provides you with:

<figure><img src="https://dishantsethi.files.wordpress.com/2022/01/screenshot-2022-01-20-at-2.09.58-pm.png?w=352" alt=""><figcaption></figcaption></figure>

Even though AWS CloudFront and S3 charge very little but still…

We will be using 4 AWS services to host our static website.

* S3
* Route 53
* Certificate Manager
* CloudFront

## STEP 1

Create 2 S3 buckets.
- `www.yourdomain.com`
- `yourdomain.com`

Go with the default configurations while creating the buckets

We need to consider one of the buckets as our main bucket. So, let us consider `www.yourdomain.com` as our main bucket for the tutorial.

Upload all the static files, assets, and index.html in the main s3 bucket (`www.yourdomain.com`)

Then go to **Properties** -> **Static Website hosting**. Select the “Use this bucket to host a website” option and write index.html in the Index document field. Do not forget to click the save button.😜

At this point, our website is hosted inside the S3 bucket but nobody can access it because the bucket is only privately accessible. To make the bucket public, we need to add a **bucket policy**, but before this, we need to enable our bucket to accept new bucket policies.

Go to **Permission** of your main bucket (`www.yourdomain.com`) -> Edit **Block public access** -> Uncheck **Block all public** access -> Save

This would allow us to add new **Bucket Policies** for our S3 bucket. The only bucket policy we need is to make our bucket available to the world.

**Permission** -> **Edit Bucket Policy** -> Add this:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AddPerm",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::www.yourdomain.com/*"
        }
    ]
}
```

This will allow any user to “read access” to any objects in the bucket. To test this, Go to **Properties** -> **Static Website hosting**. You should be able to find this endpoint where your static website is hosted.

Now let us redirect non-www. to www.

Go to **Bucket 2** (`yourdomain.com`) -> **Properties** -> **Static website hosting** -> Redirect Requests -> type your target bucket (`www.yourdomain.com`) and specify http protocol for now.

## STEP 2

Let us take a break from s3 and create hosted zone for our DNS. I am assuming that you bought your domain from godaddy.com (because I bought it from there😜)

Go to **Route53** -> **Hosted Zone (under DNS Management)** -> **Create Hosted Zone** -> Enter **domain name** -> **Save** with all default settings

Now, copy the NS(nameservers) provided by AWS and update them in the nameservers of `yourdomain.com` on GoDaddy’s website.

<figure><img src="https://dishantsethi.files.wordpress.com/2022/01/screenshot-2022-01-22-at-4.16.10-pm-1.png"><figcaption>Copy these nameservers from AWS route53</figcaption></figure>

<figure><img src="https://dishantsethi.files.wordpress.com/2022/01/screenshot-2022-01-22-at-4.22.46-pm.png"><figcaption>Paste here</figcaption></figure>

Now we have to create 2 new A-records.

Go to **Hosted Zone** -> **yourdomain.com** -> **Create Record** -> Record name = **www** -> Switch to Alias in Values field and select **S3 AWS resource, S3 bucket region and S3 bucket endpoint**

We need to create a non-www record as well.

Go to **Hosted Zone** -> **yourdomain.com** -> **Create Record** -> (leave the record name blank) Switch to Alias in Values field and select S3 AWS resource, S3 bucket region, and **S3 bucket endpoint**

## STEP 3

AWS -> **Certificate Manager service** -> **Switch region** to the region of your S3 bucket (us-east-1 in my case) -> **Hit the Request Certificate** -> Request Public certificate -> **Add domain names** (`www.yourdomain.com` and `yourdomain.com`) -> **Select DNS Valdiation** -> **Request**

Create CNAME Records in Route53 for the certificates you just created. Just click **Create record in Route53** and let AWS do the task for you.

Wait for a couple of minutes until the certificates are issued.

## STEP 4

Now only the CloudFront part is left. Navigate to AWS CloudFront and start creating a CloudFront distribution.

We’ll be creating 2 CloudFront distributions. One for `www.yourdomain.com` and other for `yourdomain.com`.

Create Distributions:

* Add Origin Domain name (Copy and paste the main S3 bucket endpoint URL, AWS suggests incorrect origin domain name)
* viewers protcol (choose Redirect http to https)
* alternative domain name: `http://www.yourdomain.com`
* SSL Certificate: choose the certificate you created

Repeat the process for non-www domain as well.

## POST DEPLOYMENT STEPS

* Change bucket redirects protocol to https for non-www. S3 bucket.
* Since our Route53 A-records are pointing to S3 (remember we chose Alias AWS S3 resource), Change alias to point to cloudfront for both www. and non-www. records.

This is how the flow looks like:

<figure><img src="https://dishantsethi.files.wordpress.com/2022/01/screenshot-2022-01-22-at-8.04.46-pm.png"></figure>

#### Written by - [Dishant Sethi](https://linkedin.com/in/dishantsethi)

#### Tags

<a>
<img alt="Frontend Engineering" src="https://img.shields.io/badge/Frontend_Engineering-8A2BE2" />
<a>
<img alt="AWS" src="https://img.shields.io/badge/AWS-8A2BE2" />
</a>

### Enjoyed the blog? If so, you'll appreciate collaborating with the minds behind it as well.