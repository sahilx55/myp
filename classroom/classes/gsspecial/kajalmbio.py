from pyrogram import Client
from generator import sudo_users
from classroom.bot.helper.links import get_links


async def mydata(client,callback_query):
  if str(callback_query.message.chat.id) in sudo_users:
    txt=callback_query.data
    listx = {'VCQZ_biologyspecial40classes': ('BIOLOGY SPECIAL 40 CLASSES', "['1953', '1954', '1965', '1976', '1987', '1988', '1989', '1990', '1991', '1992', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986']", 'kajalmbio')}
    d = dict(listx)

    if txt in listx:
      vx = d[txt]
      await get_links(eval(vx[1]),vx[0],vx[2],client,callback_query)


  else:
    await client.send_message(chat_id=callback_query.message.chat.id,
                        text=f"What are you doing buddy.")