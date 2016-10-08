from lxml import html
from bs4 import BeautifulSoup
import string
import requests

def getAllWarningDoNotUseUnlessStartingAnew():
    alphabet = list(string.ascii_lowercase)
    for letter in alphabet[1:]:
        getPlayerNames(letter)
# successfully pulls all names from website alphabetically
#def getPlayerNames():
    #alphabet = list(string.ascii_lowercase)
    #for letterAlpha in alphabet:
       # URL = "http://www.databasefootball.com/players/playerlist.htm?lt=" + letterAlpha
#        page = requests.get(URL)
 #       pageText = page.text
  #      soup = BeautifulSoup(pageText, 'html.parser')
   #     data = soup.find_all('p')[3].find_all('td')
    #    for i in data:
     #       s = i.find_all('a')
      #      for n in s:
       #         name = n.get_text()
        #        print(name)       
                
def getPlayerNames(letter = 'a'):
    print("starting on: ", letter)
    filename = letter + "Players"
    f = open(filename, 'w')
    allURL = "http://www.databasefootball.com/players/playerlist.htm?lt=" + letter
    page = requests.get(allURL)
    pageText = page.text
    soup = BeautifulSoup(pageText, 'html.parser')
    data = soup.find_all('p')[3].find_all('td')
    for i in data:
        s = i.find_all('a')
        firstName = s[0].get_text()
        if(firstName != ""):
            break
    for n in s:
        playerName = n.get_text()
        playerPageCode = n.get('href')
        equalLoc = playerPageCode.index("=")
        playerPageURL = "http://www.databasefootball.com/players/playerpage.htm?ilkid" + playerPageCode[equalLoc:]
        playerInfo = getTeams(playerPageURL, playerName)
        f.write((playerInfo + "\n"))
    f.close()

#def getPlayerNames(letter = 'a'):
 #   filename = letter + "Players"
  #  f = open(filename, 'w')
   # allURL = "http://www.databasefootball.com/players/playerlist.htm?lt=" + letter
    #page = requests.get(allURL)
#    pageText = page.text
 #   soup = BeautifulSoup(pageText, 'html.parser')
  #  data = soup.find_all('p')[3].find_all('td')
   # for i in data:
    #    s = i.find_all('a')
     #   firstName = s[0].get_text()
      #  print(firstName)
       # for n in s:
        #    playerName = n.get_text()
         #   playerPageCode = n.get('href')
          #  equalLoc = playerPageCode.index("=")
           # playerPageURL = "http://www.databasefootball.com/players/playerpage.htm?ilkid" + playerPageCode[equalLoc:]
          #  playerInfo = getTeams(playerPageURL, playerName)
           # f.write((playerInfo + "\n"))

def getTeams(url = "http://www.databasefootball.com/players/playerpage.htm?ilkid=ALEXAROC01", playerName = "noName"):
    playerPageURL = url
    playerPage = requests.get(playerPageURL)
    playerPageText = playerPage.text
    playerSoup = BeautifulSoup(playerPageText,'html.parser')
    data = playerSoup.find("tbody").find_all('a')
    playerInfo = playerName + "|"
    for i in data:
        href = i.get("href")
        if(href.find("teamyear") != -1):
            teamEquiLoc = href.find("=")
            teamAmpLoc = href.find("&")
            teamName = href[(teamEquiLoc+1):(teamAmpLoc)]
            
            yearEquiLoc = href.find("=", teamAmpLoc)
            year = href[(yearEquiLoc+1):(yearEquiLoc+5)]
            playerInfo = playerInfo + teamName + ":" + year + ";"
    return playerInfo
    
            


    ## while(i<numYears):
        ##yearRec = data[i*19].get_text()
        ## teamRec = data[(i*19 + 2)].get_text()
        ## print(yearRec)
        ## print(teamRec)
        ## i+=1
            
            
            
            
