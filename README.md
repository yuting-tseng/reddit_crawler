# reddit_crawler
-----------

### About this proejct
a crawler to crawl reddit 

### Setup
First, download the source code
```
$ git clone https://github.com/yuting-tseng/reddit_crawler.git
$ cd reddit-crawler/
```
Launch python virtual environment
```
$ virtualenv --no-site-packages --python /usr/bin/python3 .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```
### Usage
```
$ python run.py SUBREDDIT CRAWLING_DEPTH OUTPUT_FILE
```
For example,
```
python run.py https://www.reddit.com/r/MachineLearning/ 2 output.json
```
The data would be store in `output.json`
