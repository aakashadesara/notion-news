## 🗞 Notion x News
Been working on some fun Notion hacks recently using [Notion-Py](https://github.com/jamalex/notion-py) (like a Notion x Sheets and Notion x Stocks and thought that it would be fun to be able to read my news in Notion! Thus an idea was born.

![Notion News Demo Screenshot](/demo.png)

### How to Use Notion x Google Sync
1. Get your Notion V2 Token by visiting your Notion page from a browser and copy the token_v2 Cookie. Replace `<YOUR_NOTION_TOKEN_V2>` with the cookie.

2. Make a new empty Notion page and replace `<YOUR_NOTION_PAGE_LINK>` in `news.py` with the link of the new page. 

3. And you should be good to go! Now just run `python news.py` and your news will update when the script starts, and then it will continue to update every 6 hours.

### Potential future changes
- [ ] Make the source + author gray in color (limited by Notion library)
- [ ] Add option to hard refresh news via Notion trigger
- [ ] Make images 33% the width (after ColumnList Block has attribute available)

If you want to help, feel free to fork + make a pull request. Contact me on Twitter [@aakashadesara](https://twitter.com/aakashadesara) before you work on something big so we do not have multiple people working on the same changes.

### Thanks
Special thanks to the folks working on the [Notion Python API](https://github.com/jamalex/notion-py) and to [Jordan Singer](https://ibuildmyideas.com/) for building a very handy [lil.api](https://lil.software/api/) to query for news.
