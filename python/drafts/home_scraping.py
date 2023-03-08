#download page
import requests                                                                                             
response = requests.get("https://whatweekisit.com/")                                                       
response.status_code
#from the page , extract info
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")
soup.title                                   
soup.title.string                            
soup.find_all("p")