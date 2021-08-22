This bot automates the process of saving jobs and applying for jobs on LinkedIn, using Selenium webdriver for Chrome.

The bot first opens the login page and logs you in using your username and password.    
It then navigates to the jobs tab in the top menu.      
It uses the JOB_SEARCH_KEYWORD and JOB_SEARCH_LOCATION to search the jobs you want to apply for.    
Once the search results are loaded, the bot goes through each job posting on the page and saves it and applies for it.      

Only those jobs that can be directly applied from LinkedIn (Easy Apply) and those that have only one-step application ('Submit Application' present in the first dialog box pop-up) are considered. The rest are skipped.   
