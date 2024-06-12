import scrapy
import argparse
from pprint import pprint
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# class AaSpider(scrapy.Spider):
class AaSpider(CrawlSpider):
    name = "aa"
    allowed_domains = ["aa.com"]
    start_urls = ["https://www.aa.com/"]
    #start_urls = ["https://www.aa.com/booking/"]
    #start_urls = ["https://www.aa.com/booking/search?locale=en_US&pax=1&adult=1&child=0&type=OneWay&searchType=Award&cabin=&carriers=ALL&slices=%5B%7B%22orig%22:%22MSN%22,%22origNearby%22:true,%22dest%22:%22DFW%22,%22destNearby%22:true,%22date%22:%222024-07-30%22%7D%5D&maxAwardSegmentAllowed=2"]
    #allowed_domains = ["toscrapea.com"]
    #start_urls = ["http://books.toscrape.com/"]
    rules = (
        Rule(LinkExtractor(allow="catalogue/category")),
    )
    # rules = (scrapy.Spider.Rule(LinkExtractor(allow="price")))
    # rules = (
    #     Rule(LinkExtractor(allow="price")),
    # )





    def parse(self, response):
        pass
    def generate_url(
            depart_date: str,
            origin: str,
            destination: str,
            n_adults: int,
            n_children: int,
    ) -> str:
        """
        Generates the URL for the AA award flight page.

        Args:
            depart_date: Departure date in YYYY-MM-DD format.
            origin: Origin airport code.
            destination: Destination airport code.
            n_adults: Number of adults.
            n_children: Number of children.

        Returns:
            url: URL of the AA award flight page to scrape.

        """
        n_passengers = n_adults + n_children
        url = f"https://www.aa.com/booking/search?locale=en_US&pax={n_passengers}&adult={n_adults}&child={n_children}&type=OneWay&searchType=Award&cabin=&carriers=ALL&slices=%5B%7B%22orig%22:%22{origin}%22,%22origNearby%22:true,%22dest%22:%22{destination}%22,%22destNearby%22:true,%22date%22:%22{depart_date}%22%7D%5D&maxAwardSegmentAllowed=2"
        return url
    def parser_maker(self):
        parser = argparse.ArgumentParser(
            description="Search for AA award availability for multiple origin/destination pairs and dates."
        )
        parser.add_argument(
            "-d",
            "--depart_date",
            nargs="+",
            help="Departure date(s) in YYYY-MM-DD format.",
            required=True,
        )
        parser.add_argument(
            "-o", "--origin", nargs="+", help="Origin airport codes.", required=True
        )
        parser.add_argument(
            "-des",
            "--destination",
            nargs="+",
            help="Destination airport codes.",
            required=True,
        )
        parser.add_argument("--n_adults", type=int, help="Number of adults.", default=1)
        parser.add_argument("--n_children", type=int, help="Number of children.", default=0)
        parser.add_argument(
            "--max_miles_main",
            type=int,
            default=20,
            help="Maximum number of miles in thousands.",
        )
        parser.add_argument(
            "--max_duration",
            type=int,
            default=11 * 60,
            help="Maximum duration of flight in minutes.",
        )
        parser.add_argument(
            "--depart_time_range",
            nargs=2,
            default=["07:00", "16:00"],
            help="Departure time range in HH:MM format.",
        )
        parser.add_argument(
            "--arrive_time_range",
            nargs=2,
            default=["12:00", "22:00"],
            help="Arrival time range in HH:MM format.",
        )
        parser.add_argument(
            "--max_stops", type=int, default=1, help="Maximum number of stops."
        )
        parser.add_argument(
            "--output_file_raw",
            default="flights_all.csv",
            help="Output file for raw flight data.",
        )
        parser.add_argument(
            "--output_file_filtered",
            default="flights_filtered.csv",
            help="Output file for filtered flight data.",
        )
        parser.add_argument(
            "--sleep_init_sec",
            type=int,
            default=10,
            help="Initial sleep time in seconds when loading browser.",
        )
        parser.add_argument(
            "--sleep_sec",
            type=int,
            default=5,
            help="Sleep time in seconds between each page load.",
        )
        args = parser.parse_args()
        print("Arguments:")
        pprint(vars(args))
