from pyrogram import Client
from generator import sudo_users
from classroom.bot.helper.links import get_links


async def mydata(client,callback_query):
  if str(callback_query.message.chat.id) in sudo_users:
    txt=callback_query.data
    listx = {'Z4M7_hsschindicomplete28classes': ('HSSC HINDI COMPLETE 28 CLASSES', "['2703', '2704', '2705', '2706', '2707', '2708', '2709', '2710', '2711', '2712', '2713', '2714', '2715', '2716', '2717', '2718', '2719', '2720', '2721', '2722', '2723', '2724', '2725', '2726', '2727', '2728', '2729', '2730']", 'hsschindi')}
    d = dict(listx)

    if txt in listx:
      vx = d[txt]
      await get_links(eval(vx[1]),vx[0],vx[2],client,callback_query)


  else:
    await client.send_message(chat_id=callback_query.message.chat.id,
                        text=f"What are you doing buddy.")