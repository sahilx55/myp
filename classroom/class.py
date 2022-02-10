import os
import sys
import dash
import itertools
from string import digits
import dashx
hostx = os.getcwd()
import importdir
fimdir = os.listdir(hostx + "/classroom/classes")
for f in fimdir:
  importdir.do(hostx + '/classroom/classes/' + f, globals())
from generator import sudo_users
from pyrogram import Client, filters
from classroom.bot.helper.butn import butn
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import Config


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

def isevaluable(s):
    try:
        eval(s)
        return True
    except:
        return False

def testclass(s):
    try:
        eval(s)
        s = f"[{s}] Is Operational ✅"
        return s
    except:
        sd = f"[{s}] Is Not Operational ⚠️"
        return sd

unamex1 = open('uname.txt', 'r')
unamex = unamex1.read()
desx = dict(dashx.des1)
d = dict(dash.listx)
cmdx = getList(desx)
xcm1 = sorted(eval(str(cmdx)))
xcm1.remove('pdfs')
xcm1.remove('help')
xcm1.insert(len(xcm1), 'pdfs')
xcm1.insert(len(xcm1), 'help')
cmdsall = '\n\n'.join(['/' + xcm1[i] + f' - ' + xcm1[i].translate(str.maketrans('', '', digits)).upper().replace('GSSPECIAL', 'GS SPECIAL').replace('SSCMAINS', 'SSC MAINS') + ' SECTION' for i in range(len(getList(desx)))])



@Client.on_message(filters.command("testbatches@linkx5bot"))
async def testbatches(client, message):
  c1 = getList(d)
  c2 = getList(desx)
  cx1 =''
  cp = ''
  cy = []
  co = []
  lxr = ''
  lxr2 =[]
  for i, j in itertools.product(range(len(c1)), range(len(c2))):
    lx = eval(desx[c2[j]][2])
    for k in range(len(lx)):
        if lx[k] in eval(d[c1[i]][2])[-1:]:
            lxr+=c1[i] + ' , '
            lxr2.append(c1[i])
    z = eval(d[c1[i]][2])[-1:][0]
    if z in desx:
        z = z
        if str(c1[i]) in eval(desx[z][2]):
            co = co
        if str(c1[i]) not in eval(desx[eval(d[c1[i]][2])[-1:][0]][2]):
          co.append(c1[i])
    if str(c1[i]) in eval(desx[c2[j]][2]):
        cp = c2[j]
        opi = ''
        opi1 = ''
        if isevaluable(c1[i]):
          opi1 = f"[{c1[i]}] Is Operational ✅"
        if not isevaluable(c1[i]):
          opi1 = f"[{c1[i]}] Is Not Operational ⚠️"
        if c1[i] in lxr2:
          opi = f'(💠{c1[i]} in sub-folders,so not necessary to be operational💠)'
        cx1= f'[{cp}]' + ' - ' + d[c1[i]][0] + ' - ' + opi1 + ' ' + opi
        cy.append(cx1)
    
  cy.sort()
  co = list(dict.fromkeys(co))
  cx2 = ''
  for i in range(len(cy)):
    cx2+= cy[i] + '\n\n'
  cx3 = ''
  for i in range(len(co)):
    cx3+= co[i] + ' , '
  mst = f"Not Found In Dashboard - {cx3}\n\nSub-Folder Batches - {lxr}\n\n{cx2}"
  
  await client.send_message(chat_id=message.chat.id,
                        text=f'{str(mst)}')


@Client.on_message(filters.command([f"allbatches@{unamex}", "allbatches"]))
async def commands(client, message):
  if str(message.chat.id) in sudo_users:
    await client.send_message(chat_id=message.chat.id,
                        text="🔶All Batches🔶\n\n" + cmdsall + '\n\nBy [Sahil Nolia](https://t.me/sahil_nolia)', disable_web_page_preview=True)


@Client.on_callback_query()
async def newbt(client,callback_query):
  if str(callback_query.message.chat.id) in sudo_users:
    txt=callback_query.data

    if txt=="videoguide":
        await client.copy_message(
            chat_id=callback_query.message.chat.id,
            from_chat_id=Config.CLASSES_CHAT,
            message_id=2579)

    if txt=="downloadapp":
        await client.copy_message(
            chat_id=callback_query.message.chat.id,
            from_chat_id=Config.CLASSES_CHAT,
            message_id=2024)
            
    if txt=="classesstructure":
        await client.send_message(chat_id=callback_query.message.chat.id,
                        text=f"CLICK BELOW BUTTON TO VIEW THE DETAILED STRUCTURE OF ALL CLASSES",reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("FOR DETAILED STRUCTURE CLICK HERE", url="https://classroom-sequence.nolia.repl.co/Classes/")],[InlineKeyboardButton("Back", callback_data="help")]]))
      
    if txt=="pdfchannel":
        await client.send_message(chat_id=callback_query.message.chat.id,
                        text=f"CLICK BELOW BUTTON TO JOIN THE CHANNEL",reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("CLICK HERE TO JOIN CHANNEL", url="https://t.me/+aNiZWbJ9gA5mNzk1")],[InlineKeyboardButton("Back", callback_data="pdfs")]]))

    if txt in desx:
        vx = desx[txt]
        await butn(vx[1],vx[2],vx[0],client,callback_query)

    if txt in d:
        vx = d[txt]
        await butn(vx[1],vx[2],vx[0],client,callback_query)

    for i in range(len(getList(d))):
      if txt in eval(getvx(d)[i][2])[:-1] and isevaluable(getList(d)[i]):
        await eval(getList(d)[i]).mydata(client,callback_query)


  else:
    await client.send_message(chat_id=callback_query.message.chat.id,
                        text=f"What are you doing buddy.")