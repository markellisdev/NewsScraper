# NewsScraper - Scrape any newspaper automatically
This is a simple python script for automatically scraping the most recent articles from any news-site.
Just add the websites you want to scrape to `NewsPapers.json` and the script will go through
and scrape each site listed in the file.

For more info read comments in `NewsScraper.py`.

This is my own version, forked from [NewsScraper](https://github.com/holwech/NewsScraper) and adapted to my own desires.

---
## 2020-0714 Update
Decide to attempt to scrape using Selenium, so incorporated code from [this tutorial](https://towardsdatascience.com/how-to-use-selenium-to-web-scrape-with-example-80f9b23a843a) as well.
Now scraping from Marketwatch financial news and printing a list of ticker symbols. Only symbols with positive movement are included.

## Libraries
This script uses the following libraries:

https://github.com/codelucas/newspaper

https://github.com/kurtmckee/feedparser
