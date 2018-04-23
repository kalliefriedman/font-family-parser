#Font Family Scraper

Given a URL input, scrape the webpage and its related files to find all fonts being used on the site.


### Details

Construct an endpoint that will receive a URL. Your service will then parse the URL, and find all fonts that are being used on that page. (no need to crawl the entire domain and traverse all the links).

- Inline style fonts
- CSS stylesheet defined fonts

The API response of your endpint should include a list of the font families used.

### Setup
- Clone the repo locally
- Create a virtualenv from the project folder using the commands "virtualenv env", "source env/bin/activate" and finally "pip install -r requirements.txt"
- Run your server by running "python web/app.py" from the command line in project folder
- Navigate to your localhost in browser and enter url into search bar (ex. http://localhost:5000/font_extraction?url=http://www.fullstory.com/)
