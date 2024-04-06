import requests, time, gdrb

print("Welcome to InfiniteLoot Tool.")
print("Finding Discord Authorization token for you...")
token = gdrb.GetTokens()

caught = {}
while True:
    req = requests.post(
        'https://discord.com/api/v9/users/@me/lootboxes/open',
        headers={
            'Authorization': '',
            'X-Debug-Options': 'bugReporterEnabled',
            'X-Discord-Locale': 'en-US',
            'X-Discord-Timezone': 'Australia/Sydney'
        }
    )

    if not caught.get(req.json().get('opened_item')):
        caught[req.json().get('opened_item')] = 0
    caught[req.json().get('opened_item')] += 1
    print(f"Sent lootbox request, opened in category: {caught[req.json().get('opened_item')]}")
    
    req2 = requests.get(
        'https://discord.com/api/v9/users/@me/lootboxes',
        headers={
            'Authorization': '',
            'X-Debug-Options' :'bugReporterEnabled',
            'X-Discord-Locale': 'en-US',
            'X-Discord-Timezone': 'Australia/Sydney'
        }
    )
    
    print(f"Status Update > {req2.json()}")
