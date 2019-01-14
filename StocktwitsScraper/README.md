# Installation 
1.  To run this program you need Scrapy (http://scrapy.org/). 
    Install it for example by running the following code in your command-line 
    $ pip install scrapy 
2.  Now download the python code for the scraper:
    $ cd /directory_to_install_scraper_to
    $ git clone https://github.com/DominikSpringer/Scraper_for_Stocktwits.git
    $ pip install -r requirements.txt 

# Usage #

1.  Change the `USER_AGENT` in `Scraper_for_Stocktwits/StocktwitsScraper/settings.py`. Please identify 
    yourself properly and be respectful and align with the following guidelines:
    https://en.wikipedia.org/wiki/Web_crawler#Politeness_policy.
	
2.  Specify the path where the output of the scraper should be stored via modifying
    the 'SAVE_TWEET_PATH' variable in the 'StocktwitstScraper/settings.py' file
    or
    In case you want to use the scraper with a MySQL database, provide the necessary information there.
    
Now there will be two ways to run this scraper. 
	A. via the command line, which is the scrapy-way of doing it.
	B. directly by executing the python script
	
---------------------------------------------------------------------------------------------------------------------------------    
3.A  Uncomment the last 3 lines in 'StocktwitSscraper/spiders/twitscrawler.py'

4.A  Make the root folder of the project to your current folder (via 'cd' command)

5.A  Run the following code:
     $ scrapy crawl twitscraper -a query="examplestock"
    
---------------------------------------------------------------------------------------------------------------------------------    
3.B In 'StocktwitSscraper/spiders/twitscrawler.py' in the last but one line, replace 'examplestock' with any list of symbols

4.B run 'StocktwitSscraper/spiders/twitscrawler.py' 

---------------------------------------------------------------------------------------------------------------------------------    


# Acknowledgement #
Brought to you by Dominik Springer

# LICENSE
The DominikSpringer/Stocktwitsscraper is licensed under the GNU General Public License v3.0
