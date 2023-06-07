from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import sqlite3

db = sqlite3.connect('test_articles')
c = db.cursor()

try:
    created_table = c.execute(
        """
        SELECT * FROM articles
        """
    )
    if created_table.rowcount >= 0:
        print("Table created")
except sqlite3.OperationalError:
    c.execute(
        '''
           CREATE TABLE IF NOT EXISTS articles
           ([id] INTEGER PRIMARY KEY, [article_name] TEXT, [article_url] TEXT)
        '''
    )


def extract_info():
    base_dir = "./articles/"
    base_url = "https://www.bbc.com"
    resources_list = ["https://www.bbc.com/news/business", "https://www.bbc.com/news/technology"]
    for item in resources_list:
        print("Searching from: " + item)
        res = []
        options = Options()
        options.add_argument('--headless=new')
        driver = webdriver.Chrome(options=options)
        driver.get(item)
        news = driver.find_elements(By.CLASS_NAME, "lx-stream__post-container")
        news_list = []
        for new_item in news:
            url = base_url + new_item.find_element(By.CLASS_NAME, "qa-heading-link").get_dom_attribute("href")
            news_list.append(url)

        for url_item in news_list:
            driver.get(url_item)
            new_item_title = driver.find_element(By.ID, "main-heading").text
            sql_syntax = '''SELECT * FROM articles WHERE article_name=?'''
            c.execute(sql_syntax, (new_item_title,))
            article_search = c.fetchall()
            if len(article_search) == 0:
                sql_insert = ''' INSERT INTO articles(article_name,article_url) 
                    VALUES(?,?) '''
                c.execute(sql_insert, (new_item_title, url_item,))
                db.commit()
                new_body_items = driver.find_elements(
                    By.CLASS_NAME,
                    'ssrcss-11r1m41-RichTextComponentWrapper'
                )
                new_item_body = ""
                for p in new_body_items:
                    new_item_body += p.text
                item = {
                    "TITLE": new_item_title,
                    "BODY": new_item_body
                }
                filename = base_dir + \
                           new_item_title.replace('.', '_').replace('?', '_').replace('$', '_') \
                               .replace(' ', '_') \
                               .replace('-', '_') \
                               .replace(':', '_') \
                               .lower() + ".json"
                with open(filename, "w") as outfile:
                    outfile.write(json.dumps(item, indent=4))
                    outfile.close()

                res.append(item)

        print(res)
        driver.close()

    db.close()


extract_info()
