# The Rise of Software Supply Chain Attacks: How to Consolidate Your Code Security

Building an application is like running a marathon. 

Just as athletes prepare for months to participate in the marathon.    

Similarly, for developing an application, countless hours are spent discussing what features to add, fueled by countless cups of coffee. Once the brainstorming is done, then the team of developers has to write the required code for it, followed by testing and resolving all the bugs in it. This is a very labor-intensive task. 

All of this is being done with one aim: To provide customers with the best possible experience when using the application. 

But what if, instead of providing a good experience to the users, the application ends up leaking all of their data on the dark web? Or continuously sends OTPs to annoy the heck out of them. They may even lock the application, preventing anyone from using it.   

This is akin to an athlete getting grievously injured on the eve of the marathon. Experiences like these can be demotivating as all the hard work has gone down the drain. 

Unfortunately, such incidents are a reality: 

- [A malware attack took place on an engineer’s laptop ](https://circleci.com/blog/jan-4-2023-incident-report/#:~:text=To%20date%2C%20we%20have%20learned,compromised%20on%20December%2016%2C%202022.)who was working for CircleCI. It exposed many of the company’s confidential data.
 
- [A supply chain attack took place on Codecov](https://www.cpomagazine.com/cyber-security/codecov-supply-chain-attack-remained-undetected-for-months-and-potentially-affected-major-companies-including-google-ibm-hp-and-others/#:~:text=2%20min%20read-,Codecov%20Supply%20Chain%20Attack%20Remained%20Undetected%20For%20Months%20and%20Potentially,%2C%20IBM%2C%20HP%2C%20and%20Others&text=Hundreds%20of%20clients%20were%20compromised,on%20the%20condition%20of%20anonymity.) which remained undetected for months and affected nearly all major technological companies. 

- [Ubiquitous “COA” NPM library got hijacked ](https://www.bleepingcomputer.com/news/security/popular-coa-npm-library-hijacked-to-steal-user-passwords/)which contained developer passwords

- [Adversaries targeted SolarWinds](https://www.techtarget.com/whatis/feature/SolarWinds-hack-explained-Everything-you-need-to-know#:~:text=Hackers%20targeted%20SolarWinds%20by%20deploying,enterprises%20and%20government%20agencies%20worldwide.&text=2020%20was%20a%20roller%20coaster%20of%20major%2C%20world%2Dshaking%20events.) by injecting malware code into its IT monitoring and management software, which is used by many enterprises and government agencies globally   

Attacks like these will make the customers lose trust in the company, regulators will hammer them with a hefty fine, and the organization will take a significant hit in its revenue and reputation.

One of the reasons why attacks like these are happening frequently is because adversaries are increasingly targeting applications in their development stages, which is why code security has become more important than ever now. You don’t want your organization to be in the news for getting all its data stolen, right? Well, that might one day become a reality if you don’t secure your code. 

How can you do it? Please continue reading the blog to find it out. 


## From Fake Repositories to Code Vulnerabilities: The Rapid Increase in Open-Source Software Supply Chain Attacks

Modern applications rely heavily on open-source libraries and frameworks. 

Now, what if these libraries and frameworks are infected with malware? That’s precisely what is happening with Github. 

Recently, [it was discovered that over 100,000 repositories in Github have been infected with malware](https://www.darkreading.com/application-security/millions-of-malicious-repositories-flood-github). Through a repo confusion campaign, adversaries created fake repositories with names similar to those of trusted ones. This tricked the developers into downloading malicious code for building their applications.  

Furthermore, organizations are increasingly adopting cloud-native applications that have given adversaries more opportunity to breach into an organization.
 
For example, they can target developers who are building applications on the cloud, allowing them to exploit the vulnerabilities that are present there to attack the entire organization. Just recently it was revealed that there are [approximately 200 critical cloud issues that could cause a breach if exploited](https://softwareanalyst.substack.com/p/a-deep-dive-into-the-cloud-and-application?r=414hy&utm_campaign=post&utm_medium=web&triedRedirect=true). 

That’s not all! Cloud misconfiguration is one of the top 10 most dangerous software weaknesses.               

The rise in software supply chain attacks is also due to developers using too many dependencies when writing code which not only creates bloating but also adds more vulnerabilities to the application.  

(Note: Software dependency is the relationship between different components of software where one relies on the other to work properly) Another reason is that adversaries are increasingly attacking pipelines which is the most vulnerable part of the application journey, as it is getting built in these CI/CD pipelines and then pushed into the cloud. This entire journey needs to be as secure as the code itself.   

Problems like these gave birth to code security, which involves finding, fixing, and preventing security vulnerabilities at the development stage. It became part of the software development process. 

Unfortunately, code security came with its own set of problems. 

## The Problem with Code Security 

To explain code security in brief, organizations scan the source code continuously and try to ensure that the application during its build and deployment stages is secure. This is done through the following tools: 

- Source Code Review: It involves identifying and mitigating issues that could be exploited by attackers. This includes SQL injection, cross-site scripting, and code level vulnerabilities.
  
- Software Supply Chain Security: It involves Securing the components, activities, and practices involved in the creation and deployment of an application. This includes third-party and proprietary code, 
  deployment methods and infrastructure, interfaces and protocols, and developer practices and development tools. 
  
- SCA: Software composition analysis, which is an automated process to identify open source software in codebase. This analysis is done to evaluate security of the code, license compliances (if any), and quality 
  of the code.
  
- Secrets Management: Securely storing sensitive information that, if leaked, could give unauthorized parties access to application infrastructure.
 
- SBOM: It is a list of all the open source and third-party components present in a codebase. The list also contains licenses that govern those components, the versions of the components used in the codebase, and their patch status, which allows security teams to detect any security or license risks.

### Application Security Tools   

- SAST: Static application security testing to analyze source code and find vulnerabilities that can make the application susceptible to any attacks.

- DAST: Dynamic application security testing in which testers examine the application while it's running. With the help of a testing tool, they perform a series of simulated attacks to check how vulnerable the 
        application is to an actual malicious attack.

- IAST:  Interactive application security testing through which code is analyzed for vulnerabilities while the application is running. This process is either done through automated testing or handled by a human 
         tester. Vulnerabilities are reported in real-time to avoid adding any extra time in the CI/CD pipeline. 

The problem we see with the use of all these tools is that it creates silos in an organization’s security apparatus since all individual solutions are provided by different vendors. This fosters a negative culture where individual vendors don’t interact and communicate with each other due to their work being separate from one another. 

You cannot secure an application if it is siloed.

Another problem with code security is that it makes developers eye roll since it creates too much noise. All it does is focusing on finding newest problems in application development, which annoys them in general. It makes sense as their plates are already full, so further filling it with 1400 CWES, 2000 vulnerabilities, or 200 misconfigurations in the cloud will only frustrate them more. 

Right now, code security tools only cause alert fatigues for developers by giving too many false positives. This is one reason why all its findings don’t really matter to them.
 
Here is an explanation of what alert fatigues are:
 
Alert fatigue happens when the brain stops paying attention to signals it has classified as irrelevant. They get filtered out before reaching the conscious processing level. If the developers feel that false positives from code security tools are unreliable, they will simply stop paying attention to them. 

Developers can tolerate false positives depending on the risk, the frequency at which false positives occur, and how much work they have on their plate. Although, alert fatigue can happen even with 10% false positives. 
 
Once the developers start to dismiss alarms, it is hard to get them to take it seriously again. Moreover, once they dismiss one type of security warning as false, similar-looking ones will also be dismissed. 
Security warnings nowadays have far too high a false positive rate and thus get dismissed. 

For example, SSL certificate warnings have a false-positive rate of 50% or even more. So, it is not surprising that developers ignore them, especially if there are no other secure alternatives for completing their tasks at hand.  

While the findings from these tools are important, it’s also equally essential to prioritize which one of them truly poses a risk. That should be the main goal of code security. It should be able to find a needle from the haystack. 

Speaking of developers, we have observed in many conversations in the cybersecurity subreddit that the most common complaint is that developers don’t cooperate when it comes to following security policies and mechanisms.
 
It is essential to bridge the gap between development and cybersecurity teams. The next section will help you with that.  

## The Human Factor in Code Security: Why Enforcement Isn’t Enough

People who are working in code security need to understand that most developers ignore security aspects because they are working under a tight schedule to deliver the application. This naturally takes more priority since that’s how their performance will be judged by the higher-ups. So, anything that disrupts their workflow will get ignored. 

Calling them lazy or careless won’t help in this situation. 

![human-factor](https://github.com/Infopercept/devsecops/assets/171223067/7dba9587-f760-48a8-a93a-4010557162bf)

                              (Source: The Cybersecurity Body of Knowledge) 

If you want to enforce security policies and mechanisms in the organization, then keep in mind these three things: 

- The process needs to be psychologically acceptable to developers as they are the ones who have to follow it. 

- The process shouldn’t take too much time. It needs to be easy to follow and shouldn't feel stressful to the developers. 

- The process should be extremely hard for adversaries to breach into, to the point where it's much more costly than the reward gained. 

The success of any security mechanism depends on whether people are willing to use it, and if yes, then how easy it is for them to implement it. Take, for example, email encryption tools, which have been there for 20 years, yet only 0.1% of emails sent are end-to-end encrypted. Furthermore, employees routinely bypass password policies and mechanisms as mandated by cybersecurity officials. 

Both these examples show that human behavior cannot be controlled or molded through security policies and mechanisms. 

So, whatever process you come up with to secure your application code, ensure that it does not affect the productivity and workflow of people working in your organization. 

One way you can do this is through Invinsense.   

## Consolidate Your Code Security With Invinsense Cyber Security Platform

Invinsense DevSecOps addresses all the pain points that we have discussed above.

### 1) A Platform that consolidates All Code Security Tools in One Place and also Provides Remediation

Firstly, Invinsense consolidated all security tools into one single platform, which streamlined the code security process, meaning organizations will no longer need different vendors to perform various code security processes (SAST, SCA, DAST, IAST, Source Code Review, Software Supply Chain Security, Secrets Management, and SBOM) as everything is now being done from one single platform. 

This prevents siloing, due to which the application has much better security. 

Secondly, many DevSecOps vendors only focus on finding issues but don’t do anything to rectify them. Invinsense DevSecOps goes one step ahead by not only focusing on finding different types of vulnerabilities but also patching them out. 

![dev-ops](https://github.com/Infopercept/devsecops/assets/171223067/3eda5d11-0cdc-40e9-acb0-4b980910e4c8)

This ensures that the workflow and productivity of developers don't get disturbed because of security tools as they don’t have to do anything since Invinsense is taking care of everything. 

Developers can focus on their tasks while we handle all the security aspects of their application. 

### 2) Invinsense Vulnerability Management (VM) Provides Consolidated View of All the Vulnerabilities Reported

![dev-sec-ops 1](https://github.com/Infopercept/devsecops/assets/171223067/4927a21d-368a-4cc9-b58a-8d994570a574)

Furthermore, Invinsense Vulnerability Management will bring all the vulnerabilities reported by the code security tools under one umbrella, meaning you will get a consolidated single view of all the issues present in the development stage of the application. 

This will reduce the complexity of vulnerabilities being reported by various tools, allowing you to easily determine which vulnerabilities have been fixed and which ones are still pending.  

If you want to learn more about Invinsense, then schedule a demo by [filling this form](https://www.infopercept.com/contact/) and our team will reach out to you shortly.

@AmitK-ICPL

