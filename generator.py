import Config
import os
import logging
from string import digits
import msgupd
import dashx
import keep_alive
import telegram.ext as tg
from telegram import ParseMode, BotCommand
from pyromod import listen
from pyrogram import Client, idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid


logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def getvx(dict): 
    list = [] 
    for key in dict.values(): 
        list.append(key)
    return list
def getList(dict): 
    list = [] 
    for key in dict.keys(): 
        list.append(key)
    return list


sudo_usersx = ['-1001653024769', '-1001612477783', '-1001795596358', '-1001753668704', '-1001580553724']
sudo_users = eval(str(sudo_usersx))
sudox1 = ["830785064", "1542508017", "872830003"]
sudox = eval(str(sudox1))
app = Client(
    ":memory:",
    api_id=8763712,
    api_hash="835d27216f117e22a5c192b89a4ce457",
    bot_token="5095390657:AAH3zgBuZDjuDBaF_0IvJcv8x9UJ3KVUpiQ",
    plugins=dict(root="classroom"),
)

# Run Bot
if __name__ == "__main__":
    try:
        keep_alive.keep_alive()
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    uname = app.get_me().username
    print(f"@{uname} Starting⚡")
    app.send_message(chat_id=-1001677612672, text=f'Bot Restarted', disable_web_page_preview=True)
    cm1 = "BotCommand(f'/"
    cm2 = "','"
    cm3 = "')"
    xcm1x1 = getList(dashx.des1)
    xcm1 = sorted(eval(str(xcm1x1)))
    xcm1.remove('pdfs')
    xcm1.remove('help')
    xcm1.insert(len(xcm1), 'pdfs')
    xcm1.insert(len(xcm1), 'help')
    xcm2 = ',\n'.join([cm1 + xcm1[i] + cm2 + xcm1[i].translate(str.maketrans('', '', digits)).capitalize().replace('Gs', 'GS').replace('Sscmains', 'SSC Mains') + ' Section' + cm3 for i in range(len(xcm1))])
    xcm3 = eval("[" + xcm2 + "]")
    updater = tg.Updater(token=Config.BOT_TOKEN)
    bot = updater.bot
    def bcmds():
      botcmds = xcm3
      bot.set_my_commands(botcmds)
    bcmds()
    owner = ['nik66', 'sahilnolia', 'sahil_nolia']
    if msgupd.msgupd != 'No New Update' :
      for i in range(len(sudo_usersx)):
        print(f'checking {i+1} : ' + sudo_usersx[i])
        admin=app.iter_chat_members(eval(sudo_usersx[i]),filter='all')
        v=""
        for u in admin:
          if u.user.is_bot ==False  and str(u.user.username) not in owner:
            v+=u.user.mention()+'\n'
        mntv = f'\n\n✨ Hello Friends! There Is An Update ✨\n\n{v}'
        x567e = app.send_message(chat_id=eval(sudo_usersx[i]), text=f'{mntv}\n🔶 Update 🔶\n\n' + msgupd.msgupd + '\n\nBot By [Sahil Nolia](https://t.me/sahil_nolia)', disable_web_page_preview=True)
        print(f'{msgupd.msgupd}')
    else:
      print(f'{msgupd.msgupd}')
    e13 = dashx.des1
    w1d = open("update.txt", "w")
    w1d.write(repr(e13))
    w1d.close()
    if os.path.isfile('upd.txt'):
      mnb = open('upd.txt', 'r')
      mnbx = mnb.read()
      for i in range(len(sudo_usersx)):
        print(f'checking {i+1} : ' + sudo_usersx[i])
        admin=app.iter_chat_members(eval(sudo_usersx[i]),filter='all')
        v=""
        for u in admin:
          if u.user.is_bot ==False  and str(u.user.username) not in owner:
            v+=u.user.mention()+'\n'
        mntv = f'\n\n✨ Hello Friends! There Is An Update ✨\n\n{v}'
        x567e = app.send_message(chat_id=eval(sudo_usersx[i]), text=f'{mntv}\n🔶 Update 🔶\n\n' + mnbx + '\n\nBot By [Sahil Nolia](https://t.me/sahil_nolia)', disable_web_page_preview=True)
        print(f'{mnbx}')
    if os.path.isfile('upd.txt'):
      os.remove("upd.txt")
    w1 = open("uname.txt", "w")
    w1.write(uname)
    w1.close()
    print(f"@{uname} Started💪 Successfully!")
    idle()
    app.stop()
    print("Bot stopped. Alvida!")
