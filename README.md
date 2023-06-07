# isi-solutions
Repo for ISI Solutions Form questions.

Sadly I got sick and wasn't able to complete the whole challenge, but I'll be happy to solve the rest on a pair-programming call if you'd like.
If it's ok with you guys, I'll solve the rest of the problems in a different branch just to make sure I'm able to.

## Q2
Just imagine that we have already prepared lists of articles that are similar.  You can see an example below: 
Retrieve an article in PubMed: https://pubmed.ncbi.nlm.nih.gov/ 
Click on the desired record to display the Abstract view. 
Examine links to Related Articles, including Reviews, on the right side of the page, or click "See all" to display all related records. 

https://pubmed.ncbi.nlm.nih.gov/?linkname=pubmed_pubmed&from_uid=33400058 
you can see that: 
PMID: 33400058 (Recent Developments on Therapeutic and Diagnostic Approaches for COVID-19) 
has the following similar articles: 
33400058: [32889088, 32935333, 33261606, 33781287, 33334802, 33070079, etc.] (623 results) 
https://pubmed.ncbi.nlm.nih.gov/?linkname=pubmed_pubmed&from_uid=33070079 
33070079: [34276652, 33371468, etc.] 
. . .  
The task is to find all 2‑tuple (ordered pair or couple) for the given lists. For simplification just let’s have the following: 
similar_ids = { 
    123: [458, 812, 765], 
    458: [123, 812, 765], 
    812: [123, 458], 
    765: [123, 458], 
    999: [100], 
    100: [999] 
}
The expected result will be: 
expected = { 
    (123, 458), (123, 812), (123, 765), (458, 812), (458, 765), (100, 999) 
}
The tuples are ordered and appear only once, so if you have (123, 458) the (458, 123) is not possible. 
Please write a program on Python. You can put a link to your code (https://pastebin.com/ for example or a link to GitHub, GitLab, etc.).
The scripts which are not working wouldn't be evaluated. Any comments are also welcome.
The extra points will be given if you write tests for different input and outputs and if you follow PEP8.

Solved in q2.py. Basic tests in test_q2.py.

## Q3

Create a program that collects articles from the https://www.bbc.com/news website. We are only interested in the sections "/business" (Business - without the "Features & Analysis", "Watch/Listen" and "Special reports" subsections) and "/technology" (Tech - without the Watch/Listen and Features & Analysis subsections).

A. The script should save every article to a separate JSON file, keeping only the article content (TITLE and BODY). All non-relevant content (external links, links to categories, CSS, scripts, multimedia content, etc.) should be removed.

B. Make sure to keep track of the downloaded content. If run again, the script should only collect articles we have not downloaded already.

C. (bonus) Containerize your Python application. Outputs should be outside the container.

The program should be written in Python and could use the Selenium framework.
In order to keep formatting, please encode your script in Base64 and paste it bellow or you can put a link to your code (https://pastebin.com/ for example or a link to GitHub, GitLab, etc.)
The scripts which are not working wouldn't be evaluated. Any comments are also welcome.
Writing a code following PEP 8 is highly recommended.

Solved in q3.py. To successfully run the script please install the Python libraries listed in requirements.txt.

## Q4

Create a command line Python program, which retrieves the information of a GitHub User and creates a new Contact or updates an existing contact in Freshdesk, using their respective APIs.
 - Use GitHub Rest API v3. Documentation is available at https://developer.github.com/v3/
 - Use Freshdesk API v2. Documentation is available at https://developers.freshdesk.com/api/
 - Your program should be able to get GitHub user login (username) and Freshdesk subdomain from the command line.
 - For authentication assume GitHub personal access token is given in GITHUB_TOKEN environmental variable and Freshdesk API key is given in FRESHDESK_TOKEN environmental variable.
 - Transfer all compatible fields from the GitHub User to the Freshdesk Contact by your judgment.
 - Please provide unit tests for the main program functionality. Create a separate module for the unit tests.
 - While you may create trial accounts in GitHub and Freshdesk, this is not a requirement. You can use the examples from the documentation as test data.
 - Please provide a README (README.md file) with instructions on how to run the Python program and the tests.
In order to keep formatting, please encode your script in Base64 and paste it bellow or you can put a link to your code (https://pastebin.com/ for example or a link to GitHub, GitLab, etc.)
The scripts which are not working wouldn't be evaluated. Any comments are also welcome.
Writing a code following PEP 8 is highly recommended.

In progress.

## Q5

Pick one of Java, Python or Docker Container type of an artifact that is a typical simple web application. You can pick any open-source project artifact or a simple hello world container.
Write a simple deployment automation script that deploys the given artifact on AWS.
Please prepare a presentation to discuss these points:
* What type of steps you would perform to verify the deployment is successful?
* Plan and a task break-down how you would implement monitoring of this deployed app.
* What kind of security policies and scans would you recommend putting into place?
* What other improvements would you make to the CI/CD process if you had more time?
* Are there any other good dev-ops tools and practices that you recommend?

In progress.