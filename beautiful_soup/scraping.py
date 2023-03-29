from bs4 import BeautifulSoup
import requests

url = "https://www.bseindia.com/markets/equity/EQReports/mktwatchR.html?filter=gainer*all$all$"

# Get the HTML
r = requests.get(url)
html_content = r.content
#print(html_content)

# Parse the HTML

soup = BeautifulSoup(html_content, 'html.parser')
gainers_div = soup.find('div', {'class': 'col-lg-12 largetable'})
print(gainers_div)
