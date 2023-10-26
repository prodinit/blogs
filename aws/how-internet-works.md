# How Internet Works?

If I ask you to imagine your life without the internet, rather than thinking about that, you would ask me to shut up and focus on what I want to say via the blog 🤣

Jokes apart, How many of you have actually thought what is internet and how it works?

Hopefully, I can provide some knowledge that gets you to the way there.

## The Internet

Most people do not have the idea where the internet came from but it doesn’t matter, they don’t need to. This is one of the things we use every day, we don’t even think about the fact that one day somebody invented them. Earlier, communication was a major issue. So to overcome this hurdle, great scientists come with the idea of interconnectivity of computers. Now, this INTERconnected NETwork of computers is referred to as the INTERNET.

Now you might be thinking that if the internet is only interconnectivity of computers then why do we pay for this and who is getting paid for this? So, there are 3 types of ISP(Internet Service Providers):

- Tier 1 ISP
- Tier 2 ISP
- Tier 3 ISP

**Tier 1 ISPs** are those who spread optic fibre(aka submarine cables) cables all over the world under the sea. Without a Tier 1 ISP, Internet traffic could not be exchanged between continents and countries. This is how submarine cables are spread all over the world

<figure><img src="https://dishantsethi.files.wordpress.com/2019/02/screenshot-from-2019-02-04-22-36-57-e1549300278741.png" alt=""><figcaption>https://www.submarinecablemap.com/#</figcaption></figure>

**Tier 2 ISPs** are those who connect Tier 1 ISPs to Tier 3 ISPs and vice-versa. Tier 2 providers purchase links(cables) from Tier 3 providers. The goal to tier 2 providers is to have as many networks as possible.

**Tier 3 ISPs** are the end user internet providers. They are responsible for the last mile connectivity. They connect a normal user to a network via their links to a tier 2 provider. A tier 3 ISP can also have direct links with tier 1 ISPs.

--- 

INTERNET is totally free of cost, you are just paying for the maintenance of the optic fibre cables being used by the service providers. Even the highest quality optic fibre cables used by tier 1 have a life of around 25 years. In India, there are five junctions where tier 2 providers can connect tier 3 with tier 2 providers(refer to submarine cable map).

> For instance, when someone visits google.com in India, the request travel from tier 3 provider’s network to tier 2 provider’s network. Then from tier 2, it will travel to Mumbai. From Mumbai, the request goes to California(where Google’s data centres are located) via the submarine cables. Now form California the response travels is the same way and reaches to the computer system of the one who has requested the service.

Now consider the situation when a company’s website whose server is in India, is being searched by an Indian. In this case, the data will not travel to other countries/continents thus submarine cables will not be involved. This will improve the privacy and security of the data. Considering the example of the Aadhar card, one would not want other countries to know what data(traffic) of the Aadhar card is coming from India. Thus, having an Indian server will not involve Tier 1 companies in this case, making the data more secure.

If you wanted to know the stats of data going out of India every day from the tier 1 junctions, you can refer this

<figure><img src="https://dishantsethi.files.wordpress.com/2019/02/screenshot-from-2019-02-07-00-15-17-e1549478781902.png" alt=""><figcaption>http://www.nixi.in/en/mrtg-statistics</figcaption></figure>

You can see from above stats, data going out from 2am – 6am is least.

## The IP Address and How we communicate?

Before going in detail with the IP addresses, I just wanted you to understand how we communicate with the servers and computers out there in the world.

<figure><img src="https://dishantsethi.files.wordpress.com/2019/02/img_20190209_162315-e1549710343938.jpg?w=2046" alt=""><figcaption></figcaption></figure>

Internet protocols(IP) are the set of rules which a request must follow to reach the owner. For a host to host communication, we need an IP address which is a Logical address. If you wanna know the IP address of your computer, just google ‘my IP address’. Considering the above image, it might happen that HOST2 is not the owner of the page you requested, then the request will travel to HOST3 which might have the source code of your request and can finally send you a particular response. For example, Google has different servers(machine) in different states/countries/continents. Now when you type ‘google.com’ you send a letter(request) that says you wanted to see Google’s website. Your letter(request) goes to the server nearest to you. Then it again goes to a server nearer to your addressee and another until it’s delivered at its destination. It is possible that you reach Google’s website with different IPs because there are many servers owned by them. When you send a request, there are certain features to be delivered correctly like different addresses. These set of rules are managed by Internet Protocols(https/http). You can verify the path followed by your request using the **traceroute** command(google it).

Now, you might be thinking that there are numerous processes running on a computer, how the server identifies the process number corresponding to a particular request. This is where the PORT number comes into play. Every process is defined with the different port number, which when matched with the port number on HOST2, sends back the response.

> You don't need to learn this. This is only for people who are curious to know what happens under the hood.

I’ll try to come up with more information on servers, protocols and different terms you want to be familiar with, hopefully soon.

#### Written by - [Dishant Sethi](https://linkedin.com/in/dishantsethi)

#### Tags

<a>
<img alt="AWS" src="https://img.shields.io/badge/AWS-8A2BE2" />
<a>
<img alt="Devops" src="https://img.shields.io/badge/Devops-8A2BE2" />
</a>

### Enjoyed the blog? If so, you'll appreciate collaborating with the minds behind it as well.