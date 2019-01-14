
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"

# settings for spiders
BOT_NAME = "StocktwitsScraper"
LOG_LEVEL = "INFO"
DOWNLOAD_HANDLERS = {'s3': None,} # from http://stackoverflow.com/a/31233576/2297751, TODO

SPIDER_MODULES = ['StocktwitsScraper.spiders']
NEWSPIDER_MODULE = 'StocktwitsScraper.spiders'
ITEM_PIPELINES = {
    #'StocktwitsScraper.pipelines.SaveToFilePipeline':100
    'StocktwitsScraper.pipelines.savetomysqlpipeline':100
}

# settings for where to save data on disk
SAVE_TWEET_PATH = ""
MYSQL_USER=""
MYSQL_PWD=""
MYSQL_TBL = ""
MYSQL_DB=""
MYSQL_IP="0.0.0.0"

