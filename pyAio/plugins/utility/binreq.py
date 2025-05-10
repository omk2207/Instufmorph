import requests
async def bin_data(bin):
    try:
        api = requests.get(f'http://ec2-3-145-174-228.us-east-2.compute.amazonaws.com:8000/bin/{bin}',timeout=10).json()
        ch = api.get('brand') or '------'
        type = api.get('type') or '------'
        ra = api.get('level') or '------'
        ame = api.get('bank') or '------' 
        cou = api.get('country') or '------' 
        emoji = api.get('flag') or '🏳️'

        return ch, type, ra, ame, cou, emoji
    except:
        return '------', '------', '------', '------', '------', '🏳️'
