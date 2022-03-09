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

    chant1 = disc.get_channel(951098686425927730)
    chantele = disc.get_channel(951181520767438898)


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
            if event.author.id != session.user.id:
                print(f"{event.message.text} from {event.author.id} in {event.thread.id}")

                t = x.fetch_threads(limit=50)

                for a in t:
                    if a.id == event.thread.id:
                        if a.id == '3315449928542074':
                            ids = []
                            nickn = a.participants
                            for users in nickn:
                                ids.append(users.id)

                            user = nickn[ids.index(event.author.id)]
                            info = x._fetch_info(user.id)
                            nick = info[event.author.id]['name']
                            obrz = []
                            obrz = event.message.attachments
                            ur = f''
                            for obr in obrz:
                                ur += f'{x.fetch_image_url(obr.id)}\n'
                            if event.message.text is None:
                                print(f'{nick}: {ur}')
                                await chant1.send(f'{nick}: {ur}')
                            else:

                                print(f'{nick}: {event.message.text}')
                                await chant1.send(f'{nick}: {ur} {event.message.text}')


                        elif a.id == '3199744420124369':
                            ids = []
                            nickn = a.participants
                            for users in nickn:
                                ids.append(users.id)

                            user = nickn[ids.index(event.author.id)]
                            info = x._fetch_info(user.id)
                            nick = info[event.author.id]['name']
                            obrz = []
                            obrz = event.message.attachments
                            ur = f''
                            for obr in obrz:
                                ur += f'{x.fetch_image_url(obr.id)}\n'
                            if event.message.text is None:
                                print(f'{nick}: {ur}')
                                await chantele.send(f'{nick}: {ur}')
                            else:

                                print(f'{nick}: {event.message.text}')
                                await chantele.send(f'{nick}: {ur} {event.message.text}')



disc.run(pswd[2])






