# In-Person-And-Online-Hackathons-Infinite-scroll-scraped-with-scrapy-spider
In Person And Online Hackathons Infinite scroll scraped with scrapy spider


### PROCESS TO RUN THIS SCRAPY SPIDER

##### Firstly be sure that you have scrapy installed . Otherwise install it with : pip install scrapy

##### After that you can generate now a single spider with: scrapy genspider "name of your spider" "following by domains if you want to add it"

##### Finally you can copy just the content of the quotestoscrapespider.py file into your file 

##### Just run it now with : scrapy runspider filename

##### Additionally , if you want to save the output to a csv file or others options , run this command: scrapy runspider "your spider file name".py -o "your desired csv file name".csv -t csv


# COMMANDS RAN TO SCRAPE THE DATA:

### scrapy genspider inpersonAndOnlineHackathons x

### scrapy runspider inpersonAndOnlineHackathons.py -o hackathons.csv -t csv

## THANK YOU FOR YOUR ATTENTION!!