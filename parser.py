from bs4 import BeautifulSoup
from selenium import webdriver

def main():
    # Open browser
    browser = webdriver.PhantomJS()

    # Leagues page
    browser.get('http://www.tsisports.ca/tsi/ligue.aspx')
    soup = BeautifulSoup(browser.page_source)
    content = soup.find(id='ContentPlaceHolder1_listA')
    contents = []
    longueuil_link = None
    for league in content.find_all('td'):
        # Get the link
        a = league.find('a')
        text = league.find_all(text=True)

        # Get all the text from the children
        if a and text and len(text) >= 4 and text[3]:
            contents.append((a['href'], text[3],))
            if text[3] == 'LONGUEUIL':
                longueuil_link = a['href']

    # League page
    browser.get(longueuil_link) # This will set the session to the selected league

    # Calendar page
    browser.get('http://www.tsisports.ca/soccer/ligue14/l_cal1.aspx')
    soup = BeautifulSoup(browser.page_source)
    menu = soup.find(id='MenuTop')
    content = soup.find(id='ContentPlaceHolder1_MatchsGr21_gridRap')
    for game in content.find_all('tr'):
        cols = game.find_all('td', text=True)
        print '%s on %s %s %s VS %s at %s' % (cols[0].text, cols[2].text, cols[3].text, cols[4].text, cols[6].text, cols[7].text,)

    # Close the browser
    browser.close()

if __name__ == "__main__":
    main()
