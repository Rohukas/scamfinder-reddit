**Before you start**\
Because some people had trouble getting the script to work initially I have made a web application for it.\
https://rohukas.github.io/scamfinder/
This requires no setup and you can simply start finding numbers withing seconds.

**Scamfinder**\
Scamfinder is a tool used for finding scammers numbers from reddit.
It uses the reddit search function to search the query you entered(i.e 'tech support') and attempt to parse a phone numbers from the results.

**Example Output**\
[X min old]\
Title: SBCglobal MaiL TecH SuPPoRt 1.234.(567).8901 Jrkpvas\
Parsed Number: 1234567890\
Link: _Link to reddit post_

**How does it work?**\
It works by using the reddit search mechanism and parsing the titles of every given result.\
Example title: _HP Printer Tech support PHoNe {1/=855/=4O9/=1555} NuMbER _{@#\$}_ atit_\
The script parses the number from the title by cleaning and doing some more tricks.

**How do I use it?**\
In order to use it you must first create a Reddit App and get the client_secret and client_id values.
You can create an app and get the client_id and client_secret using this guide:
https://redditclient.readthedocs.io/en/latest/oauth/
Paste the client_id and client_secret into the code

**Dependencies**\
The script uses PRAW - [https://praw.readthedocs.io/en/latest/](https://praw.readthedocs.io/en/latest/)
You can install praw using pip.

     pip install praw

or

    python -m pip install praw

**How to run?**

    python scamfinder.py
