from __future__ import print_function
import pickle
import os.path
import threading
import requests

from notionpy.notion.client import NotionClient
from notionpy.notion.block import CodeBlock, ColumnListBlock, DividerBlock, ColumnBlock, ImageBlock, CalloutBlock, TextBlock, QuoteBlock
from datetime import datetime

API_URL = "https://api.lil.software/news"

# start - CHANGE THESE
NOTION_V2_TOKEN = "<NOTION_V2_TOKEN>" 
NOTION_PAGE_LINK = "<EMPTY_NOTION_PAGE_LINK>"
# end   - CHANGE THESE

def get_datetime():
    now = datetime.now()
    dt_string = now.strftime("%B %d, %Y at %I:%M %p")
    return dt_string

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def add_article(page, article):
    column_block = page.children.add_new(ColumnListBlock, title="")
    column_block_left = column_block.children.add_new(ColumnBlock)
    iamge_block = column_block_left.children.add_new(ImageBlock, source=article['image'])

    column_block_right = column_block.children.add_new(ColumnBlock)
    title_block = column_block_right.children.add_new(QuoteBlock, title="[%s](%s)" % (article['title'], article['url']))
    description_block = column_block_right.children.add_new(TextBlock, title=article['description'])
    description_block = column_block_right.children.add_new(TextBlock, title="_%s, (%s)_" % (article['author'], article['source']))

    divider = page.children.add_new(DividerBlock, title="")

def main():
    client = NotionClient(token_v2=NOTION_V2_TOKEN)
    page = client.get_block(NOTION_PAGE_LINK)

    r = requests.get(url = API_URL) 
    data = r.json() 
    articles = data['articles'] or []

    for child in page.children:
        child.remove()

    callout = page.children.add_new(CalloutBlock, title="News articles have been auto updated as of %s" % get_datetime())

    for article in articles:
        add_article(page, article)

if __name__ == '__main__':
    main()
    set_interval(main, 60 * 60 * 6)
