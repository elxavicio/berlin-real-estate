# berlin-real-estate

Analyzing best properties to purchase according to their estimated short rental price based on location.

I used BeautifulSoup to retrieve information on properties for sale from inmobilienscout24.de using the `scraper.py` script.

I used data from AirBnb to train the linear regression algorithm to get an estimate of the nightly rental price based on the property's location and the number of bedrooms. This is all done in the `regression.py` script.

You can see the sample of the results at: https://public.tableau.com/profile/javiercarceller#!/vizhome/BerlinRealEstate/Dashboard1
