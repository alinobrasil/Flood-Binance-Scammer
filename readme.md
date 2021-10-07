##About
This python script just floods a scammer's site with garbage info, so if they ever succeed in extracting someone's secret info, it'll be hidden among a bunch of garbage data. Or the script will prevent them from receiving any new data due to API call limits.

##Running the script
If you want to use this, you'll just need to change the code where you identify the text fields on the webpage, since every site is different.

After than, just run "python browser.py"


###Background info:
If you ever ask any question in a crypto related telegram group, you'll get tons of messages from scammers.

##How most of these scams work:
They message you with some BS excuse for you to click on a link
The site will be a pathetic attempt at looking like a legit crypto site. 
The site asks you to login but ends up asking for your wallet's seed phrase, which legit sites never do. Or it'll try to just steal your login credentials.

##Video demo: 
https://www.youtube.com/watch?v=8a_3B42AGzU
The scammer that tried to get me to login with my binance credentials sent me to a site that tried to look like WalletConnect. Their site was using a 3rd party API to send the info they collect via email. This script eventually reached their API call limit so they couldn't receive any more new data. 
