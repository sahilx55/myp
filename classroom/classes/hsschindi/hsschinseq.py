from pyrogram import Client
from generator import sudo_users
from classroom.bot.helper.links import get_links
import Config

async def mydata(client,callback_query):
  if str(callback_query.message.chat.id) in sudo_users:
    txt=callback_query.data
    listx = {'EBWZ_hindihsscsequence': ('HINDI HSSC SEQUENCE', "['2904']", 'hsschinseq')}


    if txt in listx:
      d = dict(listx)
      vx = d[txt]
      for i in range(len(eval(vx[1]))):
        fileid = int(eval(vx[1])[i])
        await client.copy_message(chat_id=callback_query.message.chat.id,
            from_chat_id=Config.CLASSES_CHAT,
            message_id=fileid)


  else:
    await client.send_message(chat_id=callback_query.message.chat.id,
                        text=f"What are you doing buddy.")