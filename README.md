# Amazon webscraper
[section-1](#section-1)
- First thing I had to do was get the baseurl and then put the amazon standard indentification number or asin at the end of the url to get the page to load. Once I had that that we needed to use the requests_html library to get a response from the website. 
- From there I went to the amazon website and inspected the page for where the price and title were. Grabbed the text from the elements and then put them into a sqlite database. 
- To read the data I created a dataframe with pandas and printed out the results. 
- It was good practice to do something I've never done. 
