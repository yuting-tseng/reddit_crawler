import requests
from sys import argv
import json


class RedditCrawler():
    ''' crawler object'''

    def __init__(self, subreddit, crawling_depth, output):
        ''' ARGS: 
            subreddit: String, the url of subreddit ['http://www.reddit.com/r/dailyprogrammer/']
            crawling_depth: int, amount of pages would be crawling
        '''
        self.subreddit = subreddit[:-1] + '.json'
        self.crawling_depth = crawling_depth
        self.output = output
        self.data = ''

    def crawl(self):
        ''' Method: crawling subreddit
            Output
            data: String(json)
        '''
        # r = requests.get(self.subreddit)
        r = requests.get(self.subreddit, headers = {'User-agent': 'my bot 0.1'})
        self.data = r.json()

    def save(self):
        with open(self.output, 'w') as outfile:
            json.dump(self.data, outfile, indent=4)

    def __str__(self):
        t = 'subreddit: {}\n'.format(self.subreddit)
        t += 'crawling depth: {}'.format(self.crawling_depth)
        return t 

def create_crawler(sys_args):
    subreddit = sys_args[1]
    crawling_depth = sys_args[2]
    output_file = sys_args[3]
    crawler = RedditCrawler(subreddit, crawling_depth, output_file)
    print("Create Crawler...\n")
    print(crawler)
    return crawler

def main():
    crawler = create_crawler(argv)
    crawler.crawl()
    crawler.save()

# Run the main function when executed from the command line.
if __name__ == "__main__":
    main()
