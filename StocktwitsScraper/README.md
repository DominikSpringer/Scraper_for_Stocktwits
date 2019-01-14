# Installation 
1.  To run this program you need Scrapy (http://scrapy.org/). 
    Install it for example by running the following code in your command-line
    $ pip install scrapy
2.  Now download the python code for the scraper:
    $ git clone https://github.com/springa36/a_scraper.git
    $ cd StocktwitsScraper/
    $ pip install -r requirements.txt 

# Usage #

1.  Change the `USER_AGENT` in `StocktwitsScraper/settings.py`. Please identify 
    yourself properly and be respectful and align with the following guidelines:
    https://en.wikipedia.org/wiki/Web_crawler#Politeness_policy.
	
2.  Specify the path where the output of the scraper should be stored via modifying
    the 'SAVE_TWEET_PATH' variable in the 'StocktwitstScraper/settings.py' file
    
    
3.  Make the root folder of the project to your current folder (via 'cd' command)

4.  Run the following code:
    $ scrapy crawl twitscraper -a query="examplestock"


# Acknowledgement #
Inspired by jonbakerfish/TweetScraper as found via: https://github.com/jonbakerfish/TweetScraper
Brought to you by Dominik Springer

# LICENSE
The springa36/Stocktwitsscraper is licensed under the GNU General Public License v2.0
