#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from mechanize import Browser
import ssl
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context
br = Browser()
br.set_handle_robots(False)
url = 'https://login.yahoo.com/?.src=Fantasy&.intl=us&.pd=c%3Dkcs6vdu72ejHy2fVOliEIYwScg--&.done=https%3A%2F%2Ffootball.fantasysports.yahoo.com%2Ff1%2F592798&specId=usernameRegWithName'
response = br.open(url)
forms = br.forms()[0]
username_form = forms.find_control(id='login-username')
username_form.value = 'george01835' # variable
print('username set...')
forms.find_control(id='login-signin').selected = True
passwd_url = forms._click(name='signin', type='submit', id='login-signin', nr=0, coord=(1,1), return_type='url', label=None)
response = br.open(passwd_url)
forms = br.forms()[0]
passwd_form = forms.find_control(id='login-passwd')
passwd_form.value = '6km24m8vwabw' # variable
print('password set...')
forms.find_control(id='login-signin').selected = True
forms = br.forms()[0]
submit = forms.find_control('verifyPassword')
login_homepage = submit._click(form=forms, coord=(1,1), return_type='url')
response = br.open(login_homepage)
test_page = br.open('https://football.fantasysports.yahoo.com/f1/592798/addplayer?apid=100024')
roster_forms = br.forms()[1]
dpid = roster_forms.find_control('dpid')
dpid.items[1].selected = True
roster_forms.find_control('submit_drop_player').selected = True
html = test_page.read()
soup = BeautifulSoup(html, 'html5lib')
print(soup.prettify())
'''
while (True):
    player_page = br.open('https://football.fantasysports.yahoo.com/f1/592798/addplayer?apid=32671') # variable 
    html = player_page.read()
    soup = BeautifulSoup(html, 'html5lib')
    # if the target is a free agent,
    adpc = soup.find('div', {"id" : "add-drop-player-content"})
    if (str(adpc).find("Claim Player From Waivers") != -1):
        print("player on waivers")
        continue
    elif (str(adpc).find("Add Free Agent") != -1):
        print("player on free agency")
        break
'''
# then drop bench player,
# and then add target
