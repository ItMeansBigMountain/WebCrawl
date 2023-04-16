import requests
from LinkFinder import LinkFinder
from Generate_Files import *

# spider will grab link and connect to that page. 
# once connected, grab html
# throw it into link finder class 
# once it has all the links
# add links to waiting list
# once done crawling current page, it removes from queue and move to crawled


class Spider:
    
    # CLASS VARIABLE INIT  (SHARED AMONG ALL VARIABLES)
    project_name = ""
    base_url = ""
    domain_name = ""
    queue_file = ""
    crawled_file = ""

    queue = set()
    crawled = set()
    

    # INSTANCE VARIABLES INIT (SPECIFIC TO EACH SPIDER OBJECT)
    def __init__(self , project_name , base_url , domain_name):
        Spider.project_name = project_name 
        Spider.base_url = base_url 
        Spider.domain_name = domain_name 

        Spider.queue = Spider.project_name + "/queue.txt"
        Spider.crawled = Spider.project_name + "/crawled.txt"

        self.boot()
        self.crawl_page("Spider" , Spider.base_url)
    

    @staticmethod
    def boot():
        # check if data file directory are in the directory
        create_project_directory(Spider.project_name)
        create_data_files(Spider.project_name, base_url)

        # current state files converted to sets 
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)
    

    @staticmethod
    def crawl_page(thread_name , page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' now crawling ' + page_url)
            print(f"Queues left: {len(Spider.queue)}")
            print(f"Crawled page amount: {len(Spider.queue)}")

            # scrape
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            
            # update set
            Spider.queue.remove(page_url)
            Spider.crawled.remove(page_url)
            
            # update files
            Spider.update()



    def add_links_to_queue(links):
        ...

    def gather_links(page_url):
        ...

    def update(page_url):
        ...