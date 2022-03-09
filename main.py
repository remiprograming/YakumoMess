import discord
import os
import fbchat


pswd = []
with open(f'config.txt', 'r') as f:
    for x in f.readlines():
        pswd.append(x.replace('\n',''))

disc = discord.Client()

@disc.event
async def on_ready():

    print(f'{disc.user} has connected to Discord!')

    chan = disc.get_channel(951098686425927730)



    if os.path.isfile(f'cookie.txt'):
        try:
            with open(f'cookie.txt') as f:
                cookie = eval(f.read())
                session = fbchat.Session.from_cookies(cookie)
                print(f'Zalogowano z ciasteczek')
        except:
            session = fbchat.Session.login(pswd[0], pswd[1])
    else:
        session = fbchat.Session.login(pswd[0], pswd[1])

    x = fbchat.Client(session=session)
    if x.session.is_logged_in():
        print(f'Sukcesywnie zalogowano jako {pswd[0]}')
    cookie = x.session.get_cookies()
    f = open('cookie.txt', 'w')
    f.write(str(cookie))
    f.close()
    print(f'Zapisano cookie.txt')
    listener = fbchat.Listener(session=x.session, chat_on=False, foreground=False)

    for event in listener.listen():
        if isinstance(event, fbchat.MessageEvent):
            print(f"{event.message.text} from {event.author.name} in {event.thread.id}")
            # nad = fbchat.User(session= x.session, id=event.author.id)
            # await chan.send(f'{event}')
            # If you're not the author, echo
            if event.author.id != session.user.id:
                event.thread.send_text(event.message.text)

disc.run(pswd[2])






