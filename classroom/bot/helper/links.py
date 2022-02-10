from pyrogram import Client, filters
from pyromod.helpers import ikb
import json
import Config

linkx = str("https://classesbysahil.up.railway.app/")
d1 = ["[((", "))]", ")), ((", "), ["]
d2 = ["[[(", ")]]", ")], [(", "], ["]
chat_id = Config.CLASSES_CHAT

async def get_links(lis,text,call,client,callback_query):
  lis = eval(str(lis))
  n = ', '.join([f"('    Class- {str(i+1)}    ', '{linkx}{lis[i]}/stream/{str(i+1)}', 'url')" for i in range(len(lis))])
  m = eval(f'[{n}]')
  m1 = len(m) % 3
  p = []
  if m1 == 0 :
    p1 = [(m[i],m[i+1],m[i+2]) for i in range(0,len(m),3)]
    p1.append([('Back', f'{call}')])
    p = repr(p1)
    for i in range(len(d1)):
        p = p.replace(d1[i], d2[i])
  if m1 == 1 :
    m2 = m[:-1]
    y = m[-1:]
    y.append(('Back', f'{call}'))
    p1 = [(m2[i],m2[i+1],m2[i+2]) for i in range(0,len(m2),3)]
    p1.append(y)
    p = repr(p1)
    for i in range(len(d1)):
        p = p.replace(d1[i], d2[i])
  if m1 == 2 :
    m2 = m[:-2]
    y = m[-2:]
    y.append(('Back', f'{call}'))
    p1 = [(m2[i],m2[i+1],m2[i+2]) for i in range(0,len(m2),3)]
    p1.append(y)
    p = repr(p1)
    for i in range(len(d1)):
        p = p.replace(d1[i], d2[i])
  await client.send_message(chat_id=callback_query.message.chat.id, text=text, disable_web_page_preview=True, reply_markup=ikb(eval(p)))
  await callback_query.message.delete()
  api_id_msg = await client.ask(callback_query.message.chat.id, f'Send: y\n\n🔘 If you want these {str(len(lis))} classes name️.', filters=filters.text)
  api_id = api_id_msg.text
  delp = int(int(api_id_msg.message_id)-1)
  resp1 = ['Yes', 'yes', 'Y', 'y']
  reo = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
  if str(api_id) in resp1:
    await client.delete_messages(
    chat_id=callback_query.message.chat.id,
    message_ids=delp)
    msgx = await client.send_message(chat_id=callback_query.message.chat.id, text="♻️ Please Wait Generating Classes Name️ ♻️\n\nBot By [Sahil Nolia](https://t.me/sahil_nolia)", disable_web_page_preview=True)
    nx = ''
    for i in range(len(lis)):
      file_id = int(lis[i])
      m = await client.get_messages(chat_id, file_id, replies=0)
      info = json.loads(str(m))
      name = info[info['media']]['file_name']
      nx+=f'📌 Class {i+1} - {name}' + '\n\n'
      if i in reo:
        await msgx.edit_text(f"♻️ Please Wait Generating Classes Name️ ♻️\n\n✅ Successfully Generated : {str(i)}\n\nBot By [Sahil Nolia](https://t.me/sahil_nolia)", disable_web_page_preview=True)
    await msgx.delete()
    await client.send_message(chat_id=callback_query.message.chat.id, text=f"{str(nx)}Bot By [Sahil Nolia](https://t.me/sahil_nolia)", disable_web_page_preview=True)
    return

  if str(api_id).startswith("/"):
    await client.delete_messages(
    chat_id=callback_query.message.chat.id,
    message_ids=delp)
    await client.send_message(chat_id=callback_query.message.chat.id, text=f"🤦‍♀️ I was waiting for the response for classes name.\n\nSend {api_id} again if this was a command.", disable_web_page_preview=True)
    return
  else:
    await client.send_message(chat_id=callback_query.message.chat.id, text=f"🤦‍♀️ I was waiting for the response for classes name.\nI will take it as no by default.", disable_web_page_preview=True)

  