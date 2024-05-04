import scrapy
base = "https://devpost.com/api/hackathons?page={}"
class InpersonandonlinehackathonsSpider(scrapy.Spider):
    name = "inpersonAndOnlineHackathons"
    # allowed_domains = ["x"]
    page=1
    number_of_hackathons = 0
    start_urls = [base.format(page)]

    def parse(self, response):
        data = response.json()
        print(data['meta']['fuzzy'])
        hackathons = data['hackathons']
        
        for item in hackathons:
            self.number_of_hackathons += 1
            yield {
                "Title": item["title"],
                "Displayed Location": item["displayed_location"],
                "Open State": item['open_state'],
                "Analytics Identifier": item["analytics_identifier"],
                "Url": item['url'],
                "Submission Period Dates": item['submission_period_dates'],
                "Themes": item['themes'],
                "Prize Amount" : item['prize_amount'],
                "Registrations Count": item['registrations_count'],
                "Featured": item['featured'],
                "Organization Name": item['organization_name'],
                "Winners Announced": item['winners_announced'],
                "Submission Gallery Url": item['submission_gallery_url'],
                "Start A Submission Url": item['start_a_submission_url'],
                "Invite Only": item['invite_only'],
                "Eligibility Requirement Invite Only Description": item['eligibility_requirement_invite_only_description']
                
            }
            
        self.page += 1
            
        if self.number_of_hackathons < data["meta"]["total_count"]:
            
            next_page_url = base.format(self.page)

            yield scrapy.Request(next_page_url)