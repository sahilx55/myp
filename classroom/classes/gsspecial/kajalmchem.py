from pyrogram import Client
from generator import sudo_users
from classroom.bot.helper.links import get_links


async def mydata(client,callback_query):
  if str(callback_query.message.chat.id) in sudo_users:
    txt=callback_query.data
    listx = {'7WIO_chemistryspecialkajalmamcomplete26classes': ('CHEMISTRY SPECIAL KAJAL MAM COMPLETE 26 CLASSES', "['1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']", 'kajalmchem')}
    d = dict(listx)

    if txt in listx:
      vx = d[txt]
      await get_links(eval(vx[1]),vx[0],vx[2],client,callback_query)


  else:
    await client.send_message(chat_id=callback_query.message.chat.id,
                        text=f"What are you doing buddy.")