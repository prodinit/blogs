# Enable Cloudwatch Alarm and SNS Topic for AWS Billing Alert

Hello viewers. If you are someone who owns a root account of AWS or has a free-tier AWS account then billing must be something that makes you feel very terrified until you are extremely rich😜

So, in this blog, we will be configuring a cloud watch alarm that triggers and sends an email to the root account when the billing amount exceeds a threshold value. Easy Peasy.

FYI, If you have signed up for a free tier account. You already have 10 free cloud watch alarms and 1000 free email notifications each month…

Let’s Begin

#### Go to the Billing Dashboard -> Billing Preferences

<figure><img src="https://dishantsethi.files.wordpress.com/2022/01/screenshot-2022-01-26-at-10.37.16-pm.png" alt=""><figcaption></figcaption></figure>

Check **Receive Free Tier Usage Alerts** -> Add **Email Address** -> Check **Receive Billing Alerts** -> Click **Save Preferences**

Post this, Click on **Manage Billing Alerts.** It will redirect you to Cloud watch page. We will now create a Billing cloud watch alarm.

<figure><img src="https://dishantsethi.files.wordpress.com/2022/01/screenshot-2022-01-26-at-10.42.28-pm.png" alt=""><figcaption></figcaption></figure>

Let’s now create an alarm.

* Click Create Alarm
* Update currency to your preferred currency
* Define the threshold value

&#x20;

<figure><img src="https://dishantsethi.files.wordpress.com/2022/01/screenshot-2022-01-26-at-10.47.59-pm.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://dishantsethi.files.wordpress.com/2022/01/screenshot-2022-01-26-at-10.47.35-pm.png" alt=""><figcaption></figcaption></figure>

* Click Next
* Create New SNS Topic

<figure><img src="https://dishantsethi.files.wordpress.com/2022/01/screenshot-2022-01-26-at-10.49.23-pm.png" alt=""><figcaption></figcaption></figure>

* Click Create Topic

By this time you’ll have received AWS Notification for Subscription Confirmation. Subscribe to the SNS topic. Save topic, Save alarm.

Tada…

It is always good to create this billing alert. You never know what is going to cost you. It is better to be on the safer side. Alright, Now comes the important step of reaching me out and following me on twitter and linkedin.

#### Written by - [Dishant Sethi](https://linkedin.com/in/dishantsethi)

#### Tags

<a>
<img alt="AWS" src="https://img.shields.io/badge/AWS-8A2BE2" />
</a>

### Enjoyed the blog? If so, you'll appreciate collaborating with the minds behind it as well.
