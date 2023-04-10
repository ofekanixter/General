#download page
from bs4 import BeautifulSoup
import requests                                                                                             
response = requests.get("http://reports.kv-yavne.co.il/taxiv/daromTaxiv.asp")                                                       
response.status_code
#from the page , extract info
soup = BeautifulSoup(response.content, "html.parser")
soup.title                                   
soup.title.string                            
soup.find_all("p")