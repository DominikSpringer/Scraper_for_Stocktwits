from scrapy.conf import settings
import logging
import json
import os
import mysql.connector

from StocktwitsScraper.items import Twit
from StocktwitsScraper.utils import mkdirs


logger = logging.getLogger(__name__)


class SaveToFilePipeline(object):
    def __init__(self):
        self.saveTweetPath = settings['SAVE_TWEET_PATH']
        mkdirs(self.saveTweetPath)


    def process_item(self, item, spider):
        if isinstance(item, Twit):
            savePath = os.path.join(os.path.join(self.saveTweetPath, str(item['twit_id'])),'.txt')
            if os.path.isfile(savePath):
                pass
            else:
                self.save_to_file(item,savePath)
                logger.debug("Add twit with id:%s" %item['twit_id'])

        else:
            logger.info("Item type is not recognized! type = %s" %type(item))


    def save_to_file(self, item, fname):
        with open(fname,'w') as f:
            json.dump(dict(item), f)

class savetomysqlpipeline(object):

    def __init__(self):
        user = settings["MYSQL_USER"]
        pwd = settings["MYSQL_PWD"]
        self.conn = mysql.connector.connect(
            host=settings["MYSQL_IP"],
            user=user,
            password=pwd,
            database=settings["MYSQL_DB"])
        self.cursor=self.conn.cursor()
        self.insert= "insert into %s(id,text) values (%s, %s)"

    def process_item (self, item, spider):
        values_insert=(settings["MYSQL_TBL"], item['twit_id'], item['body'])
        print(values_insert)
        self.cursor.execute(self.insert % values_insert)
        try:
            self.conn.commit()
        except mysql.connector.Error as err:
            print(err.msg)
        else:
            print("Inserted into MySQL")
