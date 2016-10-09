from lxml import html
from bs4 import BeautifulSoup
import string
import requests

## the main program
## we were vary adament about not not accidentally overwriting files apparently
def getAllWarningDoNotUseUnlessStartingAnew():
    alphabet = list(string.ascii_lowercase)
    for letter in alphabet:
        getPlayerNames(letter)
      
## Takes a parameter letter and scrapes info for all players letter by letter
## writes to a file named [letter]Players that were all to be compile later
## does not return anything
        
### this came super in handy when the letter x failed on us, and we could pick up again at y
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

#takes the url to the players page and scrapes the data
#returns the string of player|team:year; team:year; team:year; ..... ;
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
    
            
            
            
            
            
