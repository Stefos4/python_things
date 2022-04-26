import berserk

token = "lip_HfTQrYNvMvmtE2pfcjjn"

session = berserk.TokenSession(token)
client = berserk.Client(session=session)

resp = client.users.get_public_data('stefos_18')
#print(resp)
try:
    cheat = resp["tosViolation"]
    print(cheat)
    if cheat==True:
        print("Cheater")
except:
    print("Not")
