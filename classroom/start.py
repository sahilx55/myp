import os
import string
from string import digits
import random
import shutil
import dash
import dashx
from generator import sudo_users
from pyrogram import Client, emoji, filters
from classroom.bot.helper.desb import desb
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import Config

def make_archive(source, destination):
        base = os.path.basename(destination)
        name = base.split('.')[0]
        format = base.split('.')[1]
        archive_from = os.path.dirname(source)
        archive_to = os.path.basename(source.strip(os.sep))
        print(source, destination, archive_from, archive_to)
        shutil.make_archive(name, format, archive_from, archive_to)
        shutil.move('%s.%s'%(name,format), destination)

def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z
x = {}

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

def Repeat(x):
    _size = len(x)
    dict = {}
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in dict:
                dict[x[i]] = f'{[o for o, p in enumerate(x) if p == x[i]]}'
                
    return dict

def repeatz(x):
    _size = len(x)
    dict = {}
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in dict:
                dict[x[i]] = f'{[o+1 for o, p in enumerate(x) if p == x[i]]}'
        ls = '\n'.join([getList(dict)[i] + ' at ' + getvx(dict)[i] for i in range(len(getvx(dict)))])
    return ls

# Start Message
hostx = os.getcwd()
sudort = ['-1001677612672']
unamex = Config.BOT_USERNAME
MENTION = "[{}](tg://user?id={})"
desx = dict(dashx.des1)
d = dict(dash.listx)
cmdx = getList(desx)
xcm1 = sorted(eval(str(cmdx)))
xcm1.remove('pdfs')
xcm1.remove('help')
xcm1.insert(len(xcm1), 'pdfs')
xcm1.insert(len(xcm1), 'help')
cmdsall = '\n\n'.join(['/' + xcm1[i] + f' - ' + xcm1[i].translate(str.maketrans('', '', digits)).upper().replace('GSSPECIAL', 'GS SPECIAL').replace('SSCMAINS', 'SSC MAINS') + ' SECTION' for i in range(len(getList(desx)))])
MESSAGE = "{} Hey {} ! Welcome to our learning group. I am a robot created by sahil, i can provide you the available lectures & the study material at any time on your demand.\n\nHow to use this bot: Just hit the available commands & follow the steps onwards or watch the detailed video by clicking 'Video Guide' button given below.\n\nHow can you watch the classes: You can watch the classes in our App or in VLC player(available on play store). Just download & install one of these apps. To download our App click on 'Download App' button or to download VLC Player click on 'Download VLC Player' button. Both buttons are given below.\n\n\n🔶Available commands🔶\n\n" + cmdsall + "\n\n\nMore lectures will be added soon.\nHappy Learning!\n\nBot By [Sahil Nolia](https://t.me/sahil_nolia)"


@Client.on_message(filters.new_chat_members)
async def welcome(client, message):
  if str(message.chat.id) in sudo_users:
    new_members = [u.mention for u in message.new_chat_members]
    text = MESSAGE.format(emoji.SPARKLES, ", ".join(new_members))
    await client.send_message(chat_id=message.chat.id,
                        text=text,reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Video Guide", callback_data="videoguide")],[InlineKeyboardButton("Download App", callback_data="downloadapp")],[InlineKeyboardButton("Download VLC Player(Play Store Link)", url="https://play.google.com/store/apps/details?id=org.videolan.vlc")]]))


@Client.on_message(filters.command("sequencegenerate@linkx5bot"))
async def sequencegen(client, message):
 if os.path.isfile('btop.txt'):
      mnb34x1 = open('listx.txt', 'r')
      mnbxop1 = mnb34x1.read()
      ct1 = eval(mnbxop1)
      ct2 = getList(ct1)
      ct3 = 0
      for i in range(len(ct2)):
        ct3 = ct3 + len(eval(str(ct1[ct2[i]][1])))
      cxt2 = getList(ct1)
      dictct = {}
      for i in range(len(cxt2)):
        if len(eval(str(ct1[cxt2[i]][1]))) != len(set(eval(str(ct1[cxt2[i]][1])))):
          cxt3 = str(ct1[cxt2[i]][0])
          cxt4 = Repeat(eval(str(ct1[cxt2[i]][1])))
          dictct[cxt3] = f'{cxt4}'
      if len(dictct)!=0:
        await client.send_message(chat_id=message.chat.id, text=f"Repeating Found\n{repr(eval(str(dictct)))}\n\n{str(ct3)} CLASSES")
      if len(dictct)==0:
        await client.send_message(chat_id=message.chat.id, text=f"NO Repeating\n\n{str(ct3)} CLASSES")
      fzlinkr58 = open('drefer.txt', 'r')
      nfzlinkr58 = fzlinkr58.read()
      frontzwe = open('btop.txt', 'r')
      frontxwe = frontzwe.read()
      mnb = open('btop2.txt', 'r')
      mnbx = mnb.read()
      lisr2 = open('d1.txt', 'r')
      l12 = lisr2.read()
      y = eval(l12)
      lisr = open('listx.txt', 'r')
      l1 = lisr.read()
      x = eval(l1)
      l90 = "', '".join([getvx(x)[i][0] for i in range(len(getList(x)))])
      l91 = "['" + l90 + "', 'Back']"
      opv8 = str(nfzlinkr58)
      opv82 = str(frontxwe)
      xv8 = eval(d[opv8][2])
      if not os.path.isdir(hostx + '/classroom/classes/' + nfzlinkr58):
        parent_dir = hostx + "/classroom/classes/"
        path = os.path.join(parent_dir, nfzlinkr58)
        os.mkdir(path)
        await client.send_message(chat_id=message.chat.id, text=f"{nfzlinkr58} Folder created \n{path}")
      z = str(getList(x))
      c = z[:-1] + ", '" + nfzlinkr58 + "']"
      li9x = "{'" + frontxwe + "': ('" + mnbx + "', " + '"' + str(l91) + '", ' + '"' + str(c) + '")}'
      callbx2 = open("dash.txt", "w")
      callbx2.write(str(li9x))
      callbx2.close()
      ftx = merge_two_dicts(y, eval(li9x))
      ftx2 = open("d1.txt", "w")
      ftx2.write(repr(ftx))
      ftx2.close()
      e1 = open('t1.txt', 'r')
      e1x = e1.read()
      e2 = open('seq2.txt', 'r')
      e2x = e2.read()
      e3 = e1x + l1 + e2x
      e4 = open("final.txt", "w")
      e4.write(e3)
      e4.close()
      e5 = open("dash.py", "w")
      e5.write('listx = ' + repr(ftx))
      e5.close()
      new = hostx + '/classroom/classes/' + nfzlinkr58 +'/' + frontxwe + '.py'
      file = hostx + "/final.txt"
      e796 = open("fp.txt", "w")
      e796.write(new)
      e796.close()
      shutil.copy(file, new)
      make_archive(hostx, hostx + "/classroom.zip")
      e4 = open("listx.txt", "w")
      e4.write("{}")
      e4.close()
      os.remove("btop.txt")
      await client.send_document(chat_id=message.chat.id, document="classroom.zip")
      await client.send_document(chat_id=message.chat.id, document=new)
      await client.send_document(chat_id=message.chat.id, document="dash.py")
      await client.send_message(chat_id=message.chat.id, text='"' + frontxwe + '" Batch Generated Successfully')
      toidxz=-1001324720821
      await client.send_message(chat_id=toidxz, text=frontxwe + ' Batch Complete')
      await client.send_document(chat_id=toidxz, document=new)
      await client.send_document(chat_id=toidxz, document="dashboard.txt")
      await client.send_document(chat_id=toidxz, document="dashboardx.txt")
      await client.send_document(chat_id=toidxz, document="bkpd1.txt")
      await client.send_document(chat_id=toidxz, document="bkpd2.txt")
      sendto = await client.get_chat(chat_id=toidxz)
      await client.send_message(chat_id=message.chat.id, text='"' + frontxwe + '" Batch Send To\n"' + sendto.title + '"\nSuccessfully')
      await client.send_message(chat_id=message.chat.id,
                        text=f"Restarting Bot")
      os.system('python3 generator.py')

 else:
   await client.send_message(chat_id=message.chat.id, text="Nothing To Generate")



@Client.on_message(filters.command("appendsequence@linkx5bot"))
async def appendsequence(client, message):
 if len(message.command) > 1:
      aplx = message.command[1].lower()
      aplx1 = f"{str(aplx)}sequencepdfs"
      chatidxy = message.command
      countzx = len(chatidxy)
      myxzx = list(range(2, countzx))
      aplx2 = ' '.join([chatidxy[myxzx[i]] for i in range(len(myxzx))]).upper()
      await client.send_message(chat_id=message.chat.id, text=f"callbackfrom = {aplx}\ncallbackto = {aplx1}\nText = {aplx2}\n\n\nAppending....")
      mnb34x1 = open('d1.txt', 'r')
      mnbxop1 = mnb34x1.read()
      numi = eval(mnbxop1)
      apl0 = numi[aplx][0]
      apl1 = eval(numi[aplx][1])
      apl2 = eval(numi[aplx][2])
      pos = 0
      apl2.insert(pos, aplx1)
      apl1.insert(pos, aplx2)
      apl3 = (apl0, f"{apl1}", f"{apl2}")
      numi[aplx] = apl3
      callbxk = open("btop.txt", "w")
      callbxk.write(aplx1)
      callbxk.close()
      callbxk2 = open("btop2.txt", "w")
      callbxk2.write(aplx2)
      callbxk2.close()
      callbxk3b = open("drefer.txt", "w")
      callbxk3b.write(aplx)
      callbxk3b.close()
      make_archive(hostx, hostx + "/classroom.zip")
      await client.send_document(chat_id=message.chat.id, document="classroom.zip")
      e5 = open("dash.py", "w")
      e5.write('listx = ' + repr(numi))
      e5.close()
      e52 = open("d1.txt", "w")
      e52.write(repr(numi))
      e52.close()
      await client.send_document(chat_id=message.chat.id, document="dash.py")
      await client.send_message(chat_id=message.chat.id, text=f"Listx appended Successfully For Sequence.")



@Client.on_message(filters.command("unzip@linkx5bot"))
async def unzipbotx(client, message):
  api_id_msg = await client.ask(message.chat.id, f'Give file location \n\ne.g  /sahil/classes.zip', filters=filters.text)
  filename = str(api_id_msg.text)
  api_id_msg1 = await client.ask(message.chat.id, f'Where to unzip this give location\n\ne.g  /classroom/classes', filters=filters.text)
  extract_dir = str(api_id_msg1.text)
  archive_format = "zip"
  shutil.unpack_archive(hostx + filename, hostx + extract_dir, archive_format)
  await client.send_message(chat_id=message.chat.id,
                        text=f'Successfully Unzipped\n{hostx + filename}\nto\n{hostx + extract_dir}')


@Client.on_message(filters.command("upload@linkx5bot"))
async def uploadtobot(client, message):
 if len(message.command) > 1:
      file_id = int(message.command[1])
      chat_id = message.chat.id
      m = await client.get_messages(chat_id, file_id, replies=0)
      DEFAULT_DOWNLOAD_DIR = str(message.command[2])
      path = await client.download_media(m, DEFAULT_DOWNLOAD_DIR)
      await client.send_message(chat_id=message.chat.id,
                        text=f'Successfully Uploaded To\n\n{str(path)}')




@Client.on_message(filters.command("zip@linkx5bot"))
async def zipbotx(client, message):
  await client.send_message(chat_id=message.chat.id,
                        text=f'Creating Archive')
  make_archive(hostx, hostx + "/classroom.zip")
  await client.send_document(chat_id=message.chat.id, document="classroom.zip")



@Client.on_message(filters.command("allcall@linkx5bot"))
async def allcall(client, message):
  await client.send_document(chat_id=message.chat.id, document="dash.py")
  await client.send_document(chat_id=message.chat.id, document="dashx.py")
  c1 = getList(d)
  cx1 =''
  for i in range(len(c1)):
    cx1+=str(c1[i]) + '\n\n'
  
  await client.send_message(chat_id=message.chat.id,
                        text=f'Listx Calls\n\n\n{cx1}')
  c2 = getList(desx)
  cx2 = ''
  for i in range(len(c2)):
    cx2+=str(c2[i]) + " - " + str(desx[c2[i]][2]) + '\n\n'
  
  await client.send_message(chat_id=message.chat.id,
                        text=f'Dashboard Calls\n\n\n{cx2}')


@Client.on_message(filters.command("appenddashboard@linkx5bot"))
async def appenddashboard(client, message):
 if len(message.command) > 1:
      aplx1 = message.command[2].lower()
      aplx = message.command[1].lower()
      chatidxy = message.command
      countzx = len(chatidxy)
      myxzx = list(range(3, countzx))
      aplx2 = ' '.join([chatidxy[myxzx[i]] for i in range(len(myxzx))]).upper()
      mnb34x1 = open('d1.txt', 'r')
      mnbxop1 = mnb34x1.read()
      numi = eval(mnbxop1)
      mnb34x1d = open('d2.txt', 'r')
      mnbxop1d = mnb34x1d.read()
      numid = eval(mnbxop1d)
      nfzlinkr58 = aplx
      nf1 = aplx1
      nf2 = aplx2
      if nfzlinkr58 not in numid:
        dictdw2 = {}
        xw2 = nfzlinkr58
        yw2 = '\\n\\n🌼 ' + xw2.translate(str.maketrans('', '', digits)).capitalize() + ' Section 🌼\\n\\nBy [Sahil Nolia](https://t.me/sahil_nolia)\\n\\n\\n/allbatches - 🔶All Batches🔶'
        keyw2 = "('" + yw2 + "', " + '"[' + f"'{nf2}']" + '", "[' + f"'{nf1}']" + '")'
        dictdw2[xw2] = eval(keyw2)
        x5yw2 = merge_two_dicts(numid, dictdw2)
        e4 = open("d2.txt", "w")
        e4.write(repr(x5yw2))
        e4.close()
        e6 = open("dashx.py", "w")
        e6.write('des1 = ' + repr(x5yw2))
        e6.close()
        await client.send_message(chat_id=message.chat.id,
                        text=f'{nfzlinkr58} Added Successfully To Dashboard')
      if nfzlinkr58 in numid:
        apl0 = numid[nfzlinkr58][0]
        apl1 = eval(numid[nfzlinkr58][1])
        apl2 = eval(numid[nfzlinkr58][2])
        pos = len(apl1)
        apl2.insert(pos, nf1)
        apl1.insert(pos, nf2)
        apl3 = (apl0, f"{apl1}", f"{apl2}")
        numid[nfzlinkr58] = apl3
        e4 = open("d2.txt", "w")
        e4.write(repr(numid))
        e4.close()
        e6 = open("dashx.py", "w")
        e6.write('des1 = ' + repr(numid))
        e6.close()
        await client.send_message(chat_id=message.chat.id,
                        text=f'{nfzlinkr58} Appended Successfully To Dashboard')
      dict2l = {}
      dict2l[nf1] = (f'{nf2}', "['Back']", f"['{nfzlinkr58}']")
      x5yw2l = merge_two_dicts(numi, dict2l)
      e4l = open("d1.txt", "w")
      e4l.write(repr(x5yw2l))
      e4l.close()
      e5 = open("dash.py", "w")
      e5.write('listx = ' + repr(x5yw2l))
      e5.close()
      make_archive(hostx, hostx + "/classroom.zip")
      await client.send_document(chat_id=message.chat.id, document="classroom.zip")
      await client.send_message(chat_id=message.chat.id,
                        text=f"Restarting Bot")
      os.system('python3 generator.py')


@Client.on_message(filters.command("appendgenerate@linkx5bot"))
async def appendxgen(client, message):
 if os.path.isfile('btop.txt'):
      mnb34x1 = open('listx.txt', 'r')
      mnbxop1 = mnb34x1.read()
      ct1 = eval(mnbxop1)
      ct2 = getList(ct1)
      ct3 = 0
      for i in range(len(ct2)):
        ct3 = ct3 + len(eval(str(ct1[ct2[i]][1])))
      callbx245 = open("btop2.txt", "a")
      callbx245.write(' ' + str(ct3) + ' CLASSES')
      callbx245.close()
      cxt2 = getList(ct1)
      dictct = {}
      for i in range(len(cxt2)):
        if len(eval(str(ct1[cxt2[i]][1]))) != len(set(eval(str(ct1[cxt2[i]][1])))):
          cxt3 = str(ct1[cxt2[i]][0])
          cxt4 = Repeat(eval(str(ct1[cxt2[i]][1])))
          dictct[cxt3] = f'{cxt4}'
      if len(dictct)!=0:
        await client.send_message(chat_id=message.chat.id, text=f"Repeating Found\n{repr(eval(str(dictct)))}\n\n{str(ct3)} CLASSES")
      if len(dictct)==0:
        await client.send_message(chat_id=message.chat.id, text=f"NO Repeating\n\n{str(ct3)} CLASSES")
      fzlinkr58 = open('drefer.txt', 'r')
      nfzlinkr58 = fzlinkr58.read()
      frontzwe = open('btop.txt', 'r')
      frontxwe = frontzwe.read()
      mnb = open('btop2.txt', 'r')
      mnbx = mnb.read()
      lisr2 = open('d1.txt', 'r')
      l12 = lisr2.read()
      y = eval(l12)
      upd1 = open("upd.txt", "w")
      upd1.write(f'New Batch In /{nfzlinkr58} Section ; {mnbx}')
      upd1.close()
      lisr = open('listx.txt', 'r')
      l1 = lisr.read()
      x = eval(l1)
      l90 = "', '".join([getvx(x)[i][0] for i in range(len(getList(x)))])
      l91 = "['" + l90 + "', 'Back']"
      opv8 = str(nfzlinkr58)
      opv82 = str(frontxwe)
      xv8 = eval(d[opv8][2])
      if not os.path.isdir(hostx + '/classroom/classes/' + nfzlinkr58):
        parent_dir = hostx + "/classroom/classes/"
        path = os.path.join(parent_dir, nfzlinkr58)
        os.mkdir(path)
        await client.send_message(chat_id=message.chat.id, text=f"{nfzlinkr58} Folder created \n{path}")
      z = str(getList(x))
      c = z[:-1] + ", '" + nfzlinkr58 + "']"
      li9x = "{'" + frontxwe + "': ('" + mnbx + "', " + '"' + str(l91) + '", ' + '"' + str(c) + '")}'
      callbx2 = open("dash.txt", "w")
      callbx2.write(str(li9x))
      callbx2.close()
      ftx = merge_two_dicts(y, eval(li9x))
      ftx2 = open("d1.txt", "w")
      ftx2.write(repr(ftx))
      ftx2.close()
      e1 = open('t1.txt', 'r')
      e1x = e1.read()
      e2 = open('t2.txt', 'r')
      e2x = e2.read()
      e3 = e1x + l1 + e2x
      e4 = open("final.txt", "w")
      e4.write(e3)
      e4.close()
      e5 = open("dash.py", "w")
      e5.write('listx = ' + repr(ftx))
      e5.close()
      new = hostx + '/classroom/classes/' + nfzlinkr58 +'/' + frontxwe + '.py'
      file = hostx + "/final.txt"
      e796 = open("fp.txt", "w")
      e796.write(new)
      e796.close()
      shutil.copy(file, new)
      make_archive(hostx, hostx + "/classroom.zip")
      e4 = open("listx.txt", "w")
      e4.write("{}")
      e4.close()
      os.remove("btop.txt")
      await client.send_document(chat_id=message.chat.id, document="classroom.zip")
      await client.send_document(chat_id=message.chat.id, document=new)
      await client.send_document(chat_id=message.chat.id, document="dash.py")
      await client.send_message(chat_id=message.chat.id, text='"' + frontxwe + '" Batch Generated Successfully')
      toidxz=-1001324720821
      await client.send_message(chat_id=toidxz, text=frontxwe + ' Batch Complete')
      await client.send_document(chat_id=toidxz, document=new)
      await client.send_document(chat_id=toidxz, document="dashboard.txt")
      await client.send_document(chat_id=toidxz, document="dashboardx.txt")
      await client.send_document(chat_id=toidxz, document="bkpd1.txt")
      await client.send_document(chat_id=toidxz, document="bkpd2.txt")
      sendto = await client.get_chat(chat_id=toidxz)
      await client.send_message(chat_id=message.chat.id, text='"' + frontxwe + '" Batch Send To\n"' + sendto.title + '"\nSuccessfully')
      await client.send_message(chat_id=message.chat.id,
                        text=f"Restarting Bot")
      os.system('python3 generator.py')

 else:
   await client.send_message(chat_id=message.chat.id, text="Nothing To Generate")


@Client.on_message(filters.command("appendnumgenerate@linkx5bot"))
async def appendxnumgen(client, message):
 if os.path.isfile('btop.txt'):
      mnb34x1 = open('listx.txt', 'r')
      mnbxop1 = mnb34x1.read()
      ct1 = eval(mnbxop1)
      ct2 = getList(ct1)
      ct3 = 0
      for i in range(len(ct2)):
        ct3 = ct3 + len(eval(str(ct1[ct2[i]][1])))
      callbx245 = open("btop2.txt", "a")
      callbx245.write(' ' + str(ct3) + ' CLASSES')
      callbx245.close()
      cxt2 = getList(ct1)
      dictct = {}
      for i in range(len(cxt2)):
        if len(eval(str(ct1[cxt2[i]][1]))) != len(set(eval(str(ct1[cxt2[i]][1])))):
          cxt3 = str(ct1[cxt2[i]][0])
          cxt4 = Repeat(eval(str(ct1[cxt2[i]][1])))
          dictct[cxt3] = f'{cxt4}'
      if len(dictct)!=0:
        await client.send_message(chat_id=message.chat.id, text=f"Repeating Found\n{repr(eval(str(dictct)))}\n\n{str(ct3)} CLASSES")
      if len(dictct)==0:
        await client.send_message(chat_id=message.chat.id, text=f"NO Repeating\n\n{str(ct3)} CLASSES")
      fzlinkr58 = open('drefer.txt', 'r')
      nfzlinkr58 = fzlinkr58.read()
      frontzwe = open('btop.txt', 'r')
      frontxwe = frontzwe.read()
      mnb = open('btop2.txt', 'r')
      mnbx = mnb.read()
      upd1 = open("upd.txt", "w")
      upd1.write(f'New Batch In /{nfzlinkr58} Section ; {mnbx}')
      upd1.close()
      lisr2 = open('d1.txt', 'r')
      l12 = lisr2.read()
      y = eval(l12)
      lisr = open('listx.txt', 'r')
      l1 = lisr.read()
      x = eval(l1)
      l90 = "', '".join([getvx(x)[i][0] for i in range(len(getList(x)))])
      l91 = "['" + l90 + "', 'Back']"
      opv8 = str(nfzlinkr58)
      opv82 = str(frontxwe)
      xv8 = eval(d[opv8][2])
      if not os.path.isdir(hostx + '/classroom/classes/' + nfzlinkr58):
        parent_dir = hostx + "/classroom/classes/"
        path = os.path.join(parent_dir, nfzlinkr58)
        os.mkdir(path)
        await client.send_message(chat_id=message.chat.id, text=f"{nfzlinkr58} Folder created \n{path}")
      z = str(getList(x))
      c = z[:-1] + ", '" + nfzlinkr58 + "']"
      li9x = "{'" + frontxwe + "': ('" + mnbx + "', " + '"' + str(l91) + '", ' + '"' + str(c) + '")}'
      callbx2 = open("dash.txt", "w")
      callbx2.write(str(li9x))
      callbx2.close()
      ftx = merge_two_dicts(y, eval(li9x))
      ftx2 = open("d1.txt", "w")
      ftx2.write(repr(ftx))
      ftx2.close()
      e1 = open('tn1.txt', 'r')
      e1x = e1.read()
      e1y1 = open('tn2.txt', 'r')
      e1y1x = e1y1.read()
      e2 = open('tn3.txt', 'r')
      e2x = e2.read()
      ytnx = getList(eval(l1))
      numi = ['1', '51', '101', '151', '201', '251', '301', '351', '401', '451', '501']
      w=""
      for i in range(len(eval(l1))):
        w+=e1y1x.replace('callxfrom', ytnx[i]).replace('numxopt', numi[i])
      e3 = e1x + l1 + w + e2x
      e4 = open("final.txt", "w")
      e4.write(e3)
      e4.close()
      e5 = open("dash.py", "w")
      e5.write('listx = ' + repr(ftx))
      e5.close()
      new = hostx + '/classroom/classes/' + nfzlinkr58 +'/' + frontxwe + '.py'
      file = hostx + "/final.txt"
      e796 = open("fp.txt", "w")
      e796.write(new)
      e796.close()
      shutil.copy(file, new)
      make_archive(hostx, hostx + "/classroom.zip")
      e4 = open("listx.txt", "w")
      e4.write("{}")
      e4.close()
      os.remove("btop.txt")
      await client.send_document(chat_id=message.chat.id, document="classroom.zip")
      await client.send_document(chat_id=message.chat.id, document=new)
      await client.send_document(chat_id=message.chat.id, document="dash.py")
      await client.send_message(chat_id=message.chat.id, text='"' + frontxwe + '" Batch Generated Successfully')
      toidxz=-1001324720821
      await client.send_message(chat_id=toidxz, text=frontxwe + ' Batch Complete')
      await client.send_document(chat_id=toidxz, document=new)
      await client.send_document(chat_id=toidxz, document="dashboard.txt")
      await client.send_document(chat_id=toidxz, document="dashboardx.txt")
      await client.send_document(chat_id=toidxz, document="bkpd1.txt")
      await client.send_document(chat_id=toidxz, document="bkpd2.txt")
      sendto = await client.get_chat(chat_id=toidxz)
      await client.send_message(chat_id=message.chat.id, text='"' + frontxwe + '" Batch Send To\n"' + sendto.title + '"\nSuccessfully')
      await client.send_message(chat_id=message.chat.id,
                        text=f"Restarting Bot")
      os.system('python3 generator.py')

 else:
   await client.send_message(chat_id=message.chat.id, text="Nothing To Generate")

@Client.on_message(filters.command("appendlistx@linkx5bot"))
async def appendlistx(client, message):
 if len(message.command) > 1:
      aplx1 = message.command[2].lower()
      aplx = message.command[1].lower()
      chatidxy = message.command
      countzx = len(chatidxy)
      myxzx = list(range(3, countzx))
      aplx2 = ' '.join([chatidxy[myxzx[i]] for i in range(len(myxzx))]).upper()
      await client.send_message(chat_id=message.chat.id, text=f"callbackfrom = {aplx}\ncallbackto = {aplx1}\nText = {aplx2}\n\n\nAppending....")
      mnb34x1 = open('d1.txt', 'r')
      mnbxop1 = mnb34x1.read()
      numi = eval(mnbxop1)
      apl0 = numi[aplx][0]
      apl1 = eval(numi[aplx][1])
      apl2 = eval(numi[aplx][2])
      pos = len(apl1)-1
      apl2.insert(pos, aplx1)
      apl1.insert(pos, aplx2)
      apl3 = (apl0, f"{apl1}", f"{apl2}")
      numi[aplx] = apl3
      callbxk = open("btop.txt", "w")
      callbxk.write(aplx1)
      callbxk.close()
      callbxk2 = open("btop2.txt", "w")
      callbxk2.write(aplx2)
      callbxk2.close()
      callbxk3b = open("drefer.txt", "w")
      callbxk3b.write(aplx)
      callbxk3b.close()
      make_archive(hostx, hostx + "/classroom.zip")
      await client.send_document(chat_id=message.chat.id, document="classroom.zip")
      e5 = open("dash.py", "w")
      e5.write('listx = ' + repr(numi))
      e5.close()
      e52 = open("d1.txt", "w")
      e52.write(repr(numi))
      e52.close()
      await client.send_document(chat_id=message.chat.id, document="dash.py")
      await client.send_message(chat_id=message.chat.id, text=f"Listx appended Successfully.")




@Client.on_message(filters.command("numgenerate@linkx5bot"))
async def numgen(client, message):
 if os.path.isfile('btop.txt'):
      mnb34x1 = open('listx.txt', 'r')
      mnbxop1 = mnb34x1.read()
      ct1 = eval(mnbxop1)
      ct2 = getList(ct1)
      ct3 = 0
      for i in range(len(ct2)):
        ct3 = ct3 + len(eval(str(ct1[ct2[i]][1])))
      callbx245 = open("btop2.txt", "a")
      callbx245.write(' ' + str(ct3) + ' CLASSES')
      callbx245.close()
      cxt2 = getList(ct1)
      dictct = {}
      for i in range(len(cxt2)):
        if len(eval(str(ct1[cxt2[i]][1]))) != len(set(eval(str(ct1[cxt2[i]][1])))):
          cxt3 = str(ct1[cxt2[i]][0])
          cxt4 = Repeat(eval(str(ct1[cxt2[i]][1])))
          dictct[cxt3] = f'{cxt4}'
      if len(dictct)!=0:
        await client.send_message(chat_id=message.chat.id, text=f"Repeating Found\n{repr(eval(str(dictct)))}\n\n{str(ct3)} CLASSES")
      if len(dictct)==0:
        await client.send_message(chat_id=message.chat.id, text=f"NO Repeating\n\n{str(ct3)} CLASSES")
      fzlinkr58 = open('drefer.txt', 'r')
      nfzlinkr58 = fzlinkr58.read()
      frontzwe = open('btop.txt', 'r')
      frontxwe = frontzwe.read()
      mnb = open('btop2.txt', 'r')
      mnbx = mnb.read()
      mnb1w2 = open('d2.txt', 'r')
      mnbx1w2 = mnb1w2.read()
      xxw2 = eval(mnbx1w2)
      if nfzlinkr58 not in xxw2:
        dictdw2 = {}
        xw2 = nfzlinkr58
        yw2 = '\\n\\n🌼 ' + xw2.translate(str.maketrans('', '', digits)).capitalize() + ' Section 🌼\\n\\nBy [Sahil Nolia](https://t.me/sahil_nolia)\\n\\n\\n/allbatches - 🔶All Batches🔶'
        keyw2 = "('" + yw2 + "', " + '"[' + "'']" + '", "[' + "'']" + '")'
        dictdw2[xw2] = eval(keyw2)
        x5yw2 = merge_two_dicts(xxw2, dictdw2)
        callbxk2 = open("d2.txt", "w")
        callbxk2.write(repr(eval(str(x5yw2))))
        callbxk2.close()
        await client.send_message(chat_id=message.chat.id, text=f"{nfzlinkr58} Added To Dashboard")
      lisr2v8 = open('d2.txt', 'r')
      l12v8 = lisr2v8.read()
      d = eval(l12v8)
      lisr2 = open('d1.txt', 'r')
      l12 = lisr2.read()
      y = eval(l12)
      lisr = open('listx.txt', 'r')
      l1 = lisr.read()
      x = eval(l1)
      l90 = "', '".join([getvx(x)[i][0] for i in range(len(getList(x)))])
      l91 = "['" + l90 + "', 'Back']"
      opv8 = str(nfzlinkr58)
      opv82 = str(frontxwe)
      xv8 = eval(d[opv8][2])
      if opv82 in xv8:
        index = xv8.index(opv82)
        x2 = eval(d[opv8][1])
        del x2[index]
        del xv8[index]
        x3 = str(d[opv8][0]).replace("\n", "\\n")
        x4 = "('" + x3 + "', " + '"' + repr(x2) + '", "' + repr(xv8) + '")'
        d[opv8] = eval(x4)
        ftx2v8 = open("d2.txt", "w")
        ftx2v8.write(repr(d))
        ftx2v8.close()
      if not os.path.isdir(hostx + '/classroom/classes/' + nfzlinkr58):
        parent_dir = hostx + "/classroom/classes/"
        path = os.path.join(parent_dir, nfzlinkr58)
        os.mkdir(path)
        await client.send_message(chat_id=message.chat.id, text=f"{nfzlinkr58} Folder created \n{path}")
      z = str(getList(x))
      c = z[:-1] + ", '" + nfzlinkr58 + "']"
      li9x = "{'" + frontxwe + "': ('" + mnbx + "', " + '"' + str(l91) + '", ' + '"' + str(c) + '")}'
      callbx2 = open("dash.txt", "w")
      callbx2.write(str(li9x))
      callbx2.close()
      ftx = merge_two_dicts(y, eval(li9x))
      ftx2 = open("d1.txt", "w")
      ftx2.write(repr(ftx))
      ftx2.close()
      mnb1 = open('d2.txt', 'r')
      mnbx1 = mnb1.read()
      xx = eval(mnbx1)
      z0 = xx[str(nfzlinkr58)][0]
      z1 = xx[str(nfzlinkr58)][1]
      z2 = xx[str(nfzlinkr58)][2]
      c1 = z1[:-1] + ", '" + str(mnbx) + "']"
      c2 = z2[:-1] + ", '" + str(frontxwe) + "']"
      c1x1 = [string for string in eval(c1) if string != ""]
      c1x2 = [string for string in eval(c2) if string != ""]
      zx = '"' + z0.replace("\n", "\\n") + '", "' + str(repr(c1x1)) + '", "' + str(repr(c1x2)) + '"'
      xx[str(nfzlinkr58)] = eval(zx)
      w1 = open("d2.txt", "w")
      w1.write(repr(xx))
      w1.close()
      e1 = open('tn1.txt', 'r')
      e1x = e1.read()
      e1y1 = open('tn2.txt', 'r')
      e1y1x = e1y1.read()
      e2 = open('tn3.txt', 'r')
      e2x = e2.read()
      ytnx = getList(eval(l1))
      numi = ['1', '51', '101', '151', '201', '251', '301', '351', '401', '451', '501']
      w=""
      for i in range(len(eval(l1))):
        w+=e1y1x.replace('callxfrom', ytnx[i]).replace('numxopt', numi[i])
      e3 = e1x + l1 + w + e2x
      e4 = open("final.txt", "w")
      e4.write(e3)
      e4.close()
      e5 = open("dash.py", "w")
      e5.write('listx = ' + repr(ftx))
      e5.close()
      e6 = open("dashx.py", "w")
      e6.write('des1 = ' + repr(xx))
      e6.close()
      new = hostx + '/classroom/classes/' + nfzlinkr58 +'/' + frontxwe + '.py'
      file = hostx + "/final.txt"
      e796 = open("fp.txt", "w")
      e796.write(new)
      e796.close()
      shutil.copy(file, new)
      make_archive(hostx, hostx + "/classroom.zip")
      e4 = open("listx.txt", "w")
      e4.write("{}")
      e4.close()
      os.remove("btop.txt")
      await client.send_document(chat_id=message.chat.id, document="classroom.zip")
      await client.send_document(chat_id=message.chat.id, document=new)
      await client.send_document(chat_id=message.chat.id, document="dash.py")
      await client.send_document(chat_id=message.chat.id, document="dashx.py")
      await client.send_message(chat_id=message.chat.id, text='"' + frontxwe + '" Batch Generated Successfully')
      toidxz=-1001324720821
      await client.send_message(chat_id=toidxz, text=frontxwe + ' Batch Complete')
      await client.send_document(chat_id=toidxz, document=new)
      await client.send_document(chat_id=toidxz, document="dashboard.txt")
      await client.send_document(chat_id=toidxz, document="dashboardx.txt")
      await client.send_document(chat_id=toidxz, document="bkpd1.txt")
      await client.send_document(chat_id=toidxz, document="bkpd2.txt")
      sendto = await client.get_chat(chat_id=toidxz)
      await client.send_message(chat_id=message.chat.id, text='"' + frontxwe + '" Batch Send To\n"' + sendto.title + '"\nSuccessfully')
      await client.send_message(chat_id=message.chat.id,
                        text=f"Restarting Bot")
      os.system('python3 generator.py')

 else:
   await client.send_message(chat_id=message.chat.id, text="Nothing To Generate")



@Client.on_message(filters.command("silentnumgenerate@linkx5bot"))
async def silnumgen(client, message):
 if os.path.isfile('btop.txt'):
      mnb34x1 = open('listx.txt', 'r')
      mnbxop1 = mnb34x1.read()
      ct1 = eval(mnbxop1)
      ct2 = getList(ct1)
      ct3 = 0
      for i in range(len(ct2)):
        ct3 = ct3 + len(eval(str(ct1[ct2[i]][1])))
      callbx245 = open("btop2.txt", "a")
      callbx245.write(' ' + str(ct3) + ' CLASSES')
      callbx245.close()
      cxt2 = getList(ct1)
      dictct = {}
      for i in range(len(cxt2)):
        if len(eval(str(ct1[cxt2[i]][1]))) != len(set(eval(str(ct1[cxt2[i]][1])))):
          cxt3 = str(ct1[cxt2[i]][0])
          cxt4 = Repeat(eval(str(ct1[cxt2[i]][1])))
          dictct[cxt3] = f'{cxt4}'
      if len(dictct)!=0:
        await client.send_message(chat_id=message.chat.id, text=f"Repeating Found\n{repr(eval(str(dictct)))}\n\n{str(ct3)} CLASSES")
      if len(dictct)==0:
        await client.send_message(chat_id=message.chat.id, text=f"NO Repeating\n\n{str(ct3)} CLASSES")
      fzlinkr58 = open('drefer.txt', 'r')
      nfzlinkr58 = fzlinkr58.read()
      frontzwe = open('btop.txt', 'r')
      frontxwe = frontzwe.read()
      mnb = open('btop2.txt', 'r')
      mnbx = mnb.read()
      mnb1w2 = open('d2.txt', 'r')
      mnbx1w2 = mnb1w2.read()
      xxw2 = eval(mnbx1w2)
      if nfzlinkr58 not in xxw2:
        dictdw2 = {}
        xw2 = nfzlinkr58
        yw2 = '\\n\\n🌼 ' + xw2.translate(str.maketrans('', '', digits)).capitalize() + ' Section 🌼\\n\\nBy [Sahil Nolia](https://t.me/sahil_nolia)\\n\\n\\n/allbatches - 🔶All Batches🔶'
        keyw2 = "('" + yw2 + "', " + '"[' + "'']" + '", "[' + "'']" + '")'
        dictdw2[xw2] = eval(keyw2)
        x5yw2 = merge_two_dicts(xxw2, dictdw2)
        callbxk2 = open("d2.txt", "w")
        callbxk2.write(repr(eval(str(x5yw2))))
        callbxk2.close()
        await client.send_message(chat_id=message.chat.id, text=f"{nfzlinkr58} Added To Dashboard")
      lisr2v8 = open('d2.txt', 'r')
      l12v8 = lisr2v8.read()
      d = eval(l12v8)
      lisr2 = open('d1.txt', 'r')
      l12 = lisr2.read()
      y = eval(l12)
      lisr = open('listx.txt', 'r')
      l1 = lisr.read()
      x = eval(l1)
      l90 = "', '".join([getvx(x)[i][0] for i in range(len(getList(x)))])
      l91 = "['" + l90 + "', 'Back']"
      opv8 = str(nfzlinkr58)
      opv82 = str(frontxwe)
      xv8 = eval(d[opv8][2])
      if opv82 in xv8:
        index = xv8.index(opv82)
        x2 = eval(d[opv8][1])
        del x2[index]
        del xv8[index]
        x3 = str(d[opv8][0]).replace("\n", "\\n")
        x4 = "('" + x3 + "', " + '"' + repr(x2) + '", "' + repr(xv8) + '")'
        d[opv8] = eval(x4)
        ftx2v8 = open("d2.txt", "w")
        ftx2v8.write(repr(d))
        ftx2v8.close()
      if not os.path.isdir(hostx + '/classroom/classes/' + nfzlinkr58):
        parent_dir = hostx + "/classroom/classes/"
        path = os.path.join(parent_dir, nfzlinkr58)
        os.mkdir(path)
        await client.send_message(chat_id=message.chat.id, text=f"{nfzlinkr58} Folder created \n{path}")
      z = str(getList(x))
      c = z[:-1] + ", '" + nfzlinkr58 + "']"
      li9x = "{'" + frontxwe + "': ('" + mnbx + "', " + '"' + str(l91) + '", ' + '"' + str(c) + '")}'
      callbx2 = open("dash.txt", "w")
      callbx2.write(str(li9x))
      callbx2.close()
      ftx = merge_two_dicts(y, eval(li9x))
      ftx2 = open("d1.txt", "w")
      ftx2.write(repr(ftx))
      ftx2.close()
      mnb1 = open('d2.txt', 'r')
      mnbx1 = mnb1.read()
      xx = eval(mnbx1)
      z0 = xx[str(nfzlinkr58)][0]
      z1 = xx[str(nfzlinkr58)][1]
      z2 = xx[str(nfzlinkr58)][2]
      c1 = z1[:-1] + ", '" + str(mnbx) + "']"
      c2 = z2[:-1] + ", '" + str(frontxwe) + "']"
      c1x1 = [string for string in eval(c1) if string != ""]
      c1x2 = [string for string in eval(c2) if string != ""]
      zx = '"' + z0.replace("\n", "\\n") + '", "' + str(repr(c1x1)) + '", "' + str(repr(c1x2)) + '"'
      xx[str(nfzlinkr58)] = eval(zx)
      w1 = open("d2.txt", "w")
      w1.write(repr(xx))
      w1.close()
      e1 = open('tn1.txt', 'r')
      e1x = e1.read()
      e1y1 = open('tn2.txt', 'r')
      e1y1x = e1y1.read()
      e2 = open('tn3.txt', 'r')
      e2x = e2.read()
      ytnx = getList(eval(l1))
      numi = ['1', '51', '101', '151', '201', '251', '301', '351', '401', '451', '501']
      w=""
      for i in range(len(eval(l1))):
        w+=e1y1x.replace('callxfrom', ytnx[i]).replace('numxopt', numi[i])
      e3 = e1x + l1 + w + e2x
      e4 = open("final.txt", "w")
      e4.write(e3)
      e4.close()
      e5 = open("dash.py", "w")
      e5.write('listx = ' + repr(ftx))
      e5.close()
      e6 = open("dashx.py", "w")
      e6.write('des1 = ' + repr(xx))
      e6.close()
      new = hostx + '/classroom/classes/' + nfzlinkr58 +'/' + frontxwe + '.py'
      file = hostx + "/final.txt"
      e796 = open("fp.txt", "w")
      e796.write(new)
      e796.close()
      shutil.copy(file, new)
      make_archive(hostx, hostx + "/classroom.zip")
      e4 = open("listx.txt", "w")
      e4.write("{}")
      e4.close()
      os.remove("btop.txt")
      await client.send_document(chat_id=message.chat.id, document="classroom.zip")
      await client.send_document(chat_id=message.chat.id, document=new)
      await client.send_document(chat_id=message.chat.id, document="dash.py")
      await client.send_document(chat_id=message.chat.id, document="dashx.py")
      await client.send_message(chat_id=message.chat.id, text='"' + frontxwe + '" Batch Generated Successfully')
      toidxz=-1001324720821
      await client.send_message(chat_id=toidxz, text=frontxwe + ' Batch Complete')
      await client.send_document(chat_id=toidxz, document=new)
      await client.send_document(chat_id=toidxz, document="dashboard.txt")
      await client.send_document(chat_id=toidxz, document="dashboardx.txt")
      await client.send_document(chat_id=toidxz, document="bkpd1.txt")
      await client.send_document(chat_id=toidxz, document="bkpd2.txt")
      sendto = await client.get_chat(chat_id=toidxz)
      await client.send_message(chat_id=message.chat.id, text='"' + frontxwe + '" Batch Send To\n"' + sendto.title + '"\nSuccessfully')
      await client.send_message(chat_id=message.chat.id,
                        text=f"Silent Generate Not Restarting Bot")

 else:
   await client.send_message(chat_id=message.chat.id, text="Nothing To Generate")


@Client.on_message(filters.command("send@linkx5bot"))
async def send(bot, msg):
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, 'Give message to send', filters=filters.text)
    api_id = api_id_msg.text
    api_hash_msg = await bot.ask(user_id, f'Do you want to send\n\n{api_id}\n\nyes/no?', filters=filters.text)
    gx = api_hash_msg.text
    choice1 = 'yes'
    choice2 = 'Yes'
    choice3 = 'no'
    choice4 = 'No'
    if gx==choice1 or gx ==choice2:
      for i in range(len(sudo_users)):
        admin=bot.iter_chat_members(eval(sudo_users[i]),filter='all')
        v=""
        w=""
        owner = ['nik66', 'sahilnolia', 'sahil_nolia']
        async for u in admin:
          if u.user.is_bot ==False  and str(u.user.username) not in owner:
            v+=u.user.mention()+'\n'
            w+=u.user.first_name +'\n'
        mntv = f'\n\n✨ Hello Friends! There Is A Message ✨\n\n{v}'
        await bot.send_message(chat_id=eval(sudo_users[i]), text=f'{mntv}\n🔶 Message 🔶\n\n' + api_id + '\n\n\nBot By [Sahil Nolia](https://t.me/sahil_nolia)')
        io = sudo_users[i].replace('-100', '')
        await bot.send_message(chat_id=user_id, text=f'Successfully Sended To\nhttps://t.me/c/{io}/1\n\n{w}')
    if gx==choice3 or gx ==choice4:
      await bot.send_message(chat_id=user_id, text='Nothing was sent')


@Client.on_message(filters.command("silentgenerate@linkx5bot"))
async def silentgen(client, message):
 if os.path.isfile('btop.txt'):
      mnb34x1 = open('listx.txt', 'r')
      mnbxop1 = mnb34x1.read()
      ct1 = eval(mnbxop1)
      ct2 = getList(ct1)
      ct3 = 0
      for i in range(len(ct2)):
        ct3 = ct3 + len(eval(str(ct1[ct2[i]][1])))
      callbx245 = open("btop2.txt", "a")
      callbx245.write(' ' + str(ct3) + ' CLASSES')
      callbx245.close()
      cxt2 = getList(ct1)
      dictct = {}
      for i in range(len(cxt2)):
        if len(eval(str(ct1[cxt2[i]][1]))) != len(set(eval(str(ct1[cxt2[i]][1])))):
          cxt3 = str(ct1[cxt2[i]][0])
          cxt4 = Repeat(eval(str(ct1[cxt2[i]][1])))
          dictct[cxt3] = f'{cxt4}'
      if len(dictct)!=0:
        await client.send_message(chat_id=message.chat.id, text=f"Repeating Found\n{repr(eval(str(dictct)))}\n\n{str(ct3)} CLASSES")
      if len(dictct)==0:
        await client.send_message(chat_id=message.chat.id, text=f"NO Repeating\n\n{str(ct3)} CLASSES")
      fzlinkr58 = open('drefer.txt', 'r')
      nfzlinkr58 = fzlinkr58.read()
      frontzwe = open('btop.txt', 'r')
      frontxwe = frontzwe.read()
      mnb = open('btop2.txt', 'r')
      mnbx = mnb.read()
      mnb1w2 = open('d2.txt', 'r')
      mnbx1w2 = mnb1w2.read()
      xxw2 = eval(mnbx1w2)
      if nfzlinkr58 not in xxw2:
        dictdw2 = {}
        xw2 = nfzlinkr58
        yw2 = '\\n\\n🌼 ' + xw2.translate(str.maketrans('', '', digits)).capitalize() + ' Section 🌼\\n\\nBy [Sahil Nolia](https://t.me/sahil_nolia)\\n\\n\\n/allbatches - 🔶All Batches🔶'
        keyw2 = "('" + yw2 + "', " + '"[' + "'']" + '", "[' + "'']" + '")'
        dictdw2[xw2] = eval(keyw2)
        x5yw2 = merge_two_dicts(xxw2, dictdw2)
        callbxk2 = open("d2.txt", "w")
        callbxk2.write(repr(eval(str(x5yw2))))
        callbxk2.close()
        await client.send_message(chat_id=message.chat.id, text=f"{nfzlinkr58} Added To Dashboard")
      lisr2v8 = open('d2.txt', 'r')
      l12v8 = lisr2v8.read()
      d = eval(l12v8)
      lisr2 = open('d1.txt', 'r')
      l12 = lisr2.read()
      y = eval(l12)
      lisr = open('listx.txt', 'r')
      l1 = lisr.read()
      x = eval(l1)
      l90 = "', '".join([getvx(x)[i][0] for i in range(len(getList(x)))])
      l91 = "['" + l90 + "', 'Back']"
      opv8 = str(nfzlinkr58)
      opv82 = str(frontxwe)
      xv8 = eval(d[opv8][2])
      if opv82 in xv8:
        index = xv8.index(opv82)
        x2 = eval(d[opv8][1])
        del x2[index]
        del xv8[index]
        x3 = str(d[opv8][0]).replace("\n", "\\n")
        x4 = "('" + x3 + "', " + '"' + repr(x2) + '", "' + repr(xv8) + '")'
        d[opv8] = eval(x4)
        ftx2v8 = open("d2.txt", "w")
        ftx2v8.write(repr(d))
        ftx2v8.close()
      if not os.path.isdir(hostx + '/classroom/classes/' + nfzlinkr58):
        parent_dir = hostx + "/classroom/classes/"
        path = os.path.join(parent_dir, nfzlinkr58)
        os.mkdir(path)
        await client.send_message(chat_id=message.chat.id, text=f"{nfzlinkr58} Folder created \n{path}")
      z = str(getList(x))
      c = z[:-1] + ", '" + nfzlinkr58 + "']"
      li9x = "{'" + frontxwe + "': ('" + mnbx + "', " + '"' + str(l91) + '", ' + '"' + str(c) + '")}'
      callbx2 = open("dash.txt", "w")
      callbx2.write(str(li9x))
      callbx2.close()
      ftx = merge_two_dicts(y, eval(li9x))
      ftx2 = open("d1.txt", "w")
      ftx2.write(repr(ftx))
      ftx2.close()
      mnb1 = open('d2.txt', 'r')
      mnbx1 = mnb1.read()
      xx = eval(mnbx1)
      z0 = xx[str(nfzlinkr58)][0]
      z1 = xx[str(nfzlinkr58)][1]
      z2 = xx[str(nfzlinkr58)][2]
      c1 = z1[:-1] + ", '" + str(mnbx) + "']"
      c2 = z2[:-1] + ", '" + str(frontxwe) + "']"
      c1x1 = [string for string in eval(c1) if string != ""]
      c1x2 = [string for string in eval(c2) if string != ""]
      zx = '"' + z0.replace("\n", "\\n") + '", "' + str(repr(c1x1)) + '", "' + str(repr(c1x2)) + '"'
      xx[str(nfzlinkr58)] = eval(zx)
      w1 = open("d2.txt", "w")
      w1.write(repr(xx))
      w1.close()
      e1 = open('t1.txt', 'r')
      e1x = e1.read()
      e2 = open('t2.txt', 'r')
      e2x = e2.read()
      e3 = e1x + l1 + e2x
      e4 = open("final.txt", "w")
      e4.write(e3)
      e4.close()
      e5 = open("dash.py", "w")
      e5.write('listx = ' + repr(ftx))
      e5.close()
      e6 = open("dashx.py", "w")
      e6.write('des1 = ' + repr(xx))
      e6.close()
      new = hostx + '/classroom/classes/' + nfzlinkr58 +'/' + frontxwe + '.py'
      file = hostx + "/final.txt"
      e796 = open("fp.txt", "w")
      e796.write(new)
      e796.close()
      shutil.copy(file, new)
      make_archive(hostx, hostx + "/classroom.zip")
      e4 = open("listx.txt", "w")
      e4.write("{}")
      e4.close()
      os.remove("btop.txt")
      await client.send_document(chat_id=message.chat.id, document="classroom.zip")
      await client.send_document(chat_id=message.chat.id, document=new)
      await client.send_document(chat_id=message.chat.id, document="dash.py")
      await client.send_document(chat_id=message.chat.id, document="dashx.py")
      await client.send_message(chat_id=message.chat.id, text='"' + frontxwe + '" Batch Generated Successfully')
      toidxz=-1001324720821
      await client.send_message(chat_id=toidxz, text=frontxwe + ' Batch Complete')
      await client.send_document(chat_id=toidxz, document=new)
      await client.send_document(chat_id=toidxz, document="dashboard.txt")
      await client.send_document(chat_id=toidxz, document="dashboardx.txt")
      await client.send_document(chat_id=toidxz, document="bkpd1.txt")
      await client.send_document(chat_id=toidxz, document="bkpd2.txt")
      sendto = await client.get_chat(chat_id=toidxz)
      await client.send_message(chat_id=message.chat.id, text='"' + frontxwe + '" Batch Send To\n"' + sendto.title + '"\nSuccessfully')
      await client.send_message(chat_id=message.chat.id,
                        text=f"Silent Generate Not Restarting Bot")

 else:
   await client.send_message(chat_id=message.chat.id, text="Nothing To Generate")



@Client.on_message(filters.command("batchgenerate@linkx5bot"))
async def bgen(client, message):
 if os.path.isfile('btop.txt'):
      mnb34x1 = open('listx.txt', 'r')
      mnbxop1 = mnb34x1.read()
      ct1 = eval(mnbxop1)
      ct2 = getList(ct1)
      ct3 = 0
      for i in range(len(ct2)):
        ct3 = ct3 + len(eval(str(ct1[ct2[i]][1])))
      callbx245 = open("btop2.txt", "a")
      callbx245.write(' ' + str(ct3) + ' CLASSES')
      callbx245.close()
      cxt2 = getList(ct1)
      dictct = {}
      for i in range(len(cxt2)):
        if len(eval(str(ct1[cxt2[i]][1]))) != len(set(eval(str(ct1[cxt2[i]][1])))):
          cxt3 = str(ct1[cxt2[i]][0])
          cxt4 = Repeat(eval(str(ct1[cxt2[i]][1])))
          dictct[cxt3] = f'{cxt4}'
      if len(dictct)!=0:
        await client.send_message(chat_id=message.chat.id, text=f"Repeating Found\n{repr(eval(str(dictct)))}\n\n{str(ct3)} CLASSES")
      if len(dictct)==0:
        await client.send_message(chat_id=message.chat.id, text=f"NO Repeating\n\n{str(ct3)} CLASSES")
      fzlinkr58 = open('drefer.txt', 'r')
      nfzlinkr58 = fzlinkr58.read()
      frontzwe = open('btop.txt', 'r')
      frontxwe = frontzwe.read()
      mnb = open('btop2.txt', 'r')
      mnbx = mnb.read()
      mnb1w2 = open('d2.txt', 'r')
      mnbx1w2 = mnb1w2.read()
      xxw2 = eval(mnbx1w2)
      if nfzlinkr58 not in xxw2:
        dictdw2 = {}
        xw2 = nfzlinkr58
        yw2 = '\\n\\n🌼 ' + xw2.translate(str.maketrans('', '', digits)).capitalize() + ' Section 🌼\\n\\nBy [Sahil Nolia](https://t.me/sahil_nolia)\\n\\n\\n/allbatches - 🔶All Batches🔶'
        keyw2 = "('" + yw2 + "', " + '"[' + "'']" + '", "[' + "'']" + '")'
        dictdw2[xw2] = eval(keyw2)
        x5yw2 = merge_two_dicts(xxw2, dictdw2)
        callbxk2 = open("d2.txt", "w")
        callbxk2.write(repr(eval(str(x5yw2))))
        callbxk2.close()
        await client.send_message(chat_id=message.chat.id, text=f"{nfzlinkr58} Added To Dashboard")
      lisr2v8 = open('d2.txt', 'r')
      l12v8 = lisr2v8.read()
      d = eval(l12v8)
      lisr2 = open('d1.txt', 'r')
      l12 = lisr2.read()
      y = eval(l12)
      lisr = open('listx.txt', 'r')
      l1 = lisr.read()
      x = eval(l1)
      l90 = "', '".join([getvx(x)[i][0] for i in range(len(getList(x)))])
      l91 = "['" + l90 + "', 'Back']"
      opv8 = str(nfzlinkr58)
      opv82 = str(frontxwe)
      xv8 = eval(d[opv8][2])
      if opv82 in xv8:
        index = xv8.index(opv82)
        x2 = eval(d[opv8][1])
        del x2[index]
        del xv8[index]
        x3 = str(d[opv8][0]).replace("\n", "\\n")
        x4 = "('" + x3 + "', " + '"' + repr(x2) + '", "' + repr(xv8) + '")'
        d[opv8] = eval(x4)
        ftx2v8 = open("d2.txt", "w")
        ftx2v8.write(repr(d))
        ftx2v8.close()
      if not os.path.isdir(hostx + '/classroom/classes/' + nfzlinkr58):
        parent_dir = hostx + "/classroom/classes/"
        path = os.path.join(parent_dir, nfzlinkr58)
        os.mkdir(path)
        await client.send_message(chat_id=message.chat.id, text=f"{nfzlinkr58} Folder created \n{path}")
      z = str(getList(x))
      c = z[:-1] + ", '" + nfzlinkr58 + "']"
      li9x = "{'" + frontxwe + "': ('" + mnbx + "', " + '"' + str(l91) + '", ' + '"' + str(c) + '")}'
      callbx2 = open("dash.txt", "w")
      callbx2.write(str(li9x))
      callbx2.close()
      ftx = merge_two_dicts(y, eval(li9x))
      ftx2 = open("d1.txt", "w")
      ftx2.write(repr(ftx))
      ftx2.close()
      mnb1 = open('d2.txt', 'r')
      mnbx1 = mnb1.read()
      xx = eval(mnbx1)
      z0 = xx[str(nfzlinkr58)][0]
      z1 = xx[str(nfzlinkr58)][1]
      z2 = xx[str(nfzlinkr58)][2]
      c1 = z1[:-1] + ", '" + str(mnbx) + "']"
      c2 = z2[:-1] + ", '" + str(frontxwe) + "']"
      c1x1 = [string for string in eval(c1) if string != ""]
      c1x2 = [string for string in eval(c2) if string != ""]
      zx = '"' + z0.replace("\n", "\\n") + '", "' + str(repr(c1x1)) + '", "' + str(repr(c1x2)) + '"'
      xx[str(nfzlinkr58)] = eval(zx)
      w1 = open("d2.txt", "w")
      w1.write(repr(xx))
      w1.close()
      e1 = open('t1.txt', 'r')
      e1x = e1.read()
      e2 = open('t2.txt', 'r')
      e2x = e2.read()
      e3 = e1x + l1 + e2x
      e4 = open("final.txt", "w")
      e4.write(e3)
      e4.close()
      e5 = open("dash.py", "w")
      e5.write('listx = ' + repr(ftx))
      e5.close()
      e6 = open("dashx.py", "w")
      e6.write('des1 = ' + repr(xx))
      e6.close()
      new = hostx + '/classroom/classes/' + nfzlinkr58 +'/' + frontxwe + '.py'
      file = hostx + "/final.txt"
      e796 = open("fp.txt", "w")
      e796.write(new)
      e796.close()
      shutil.copy(file, new)
      make_archive(hostx, hostx + "/classroom.zip")
      e4 = open("listx.txt", "w")
      e4.write("{}")
      e4.close()
      os.remove("btop.txt")
      await client.send_document(chat_id=message.chat.id, document="classroom.zip")
      await client.send_document(chat_id=message.chat.id, document=new)
      await client.send_document(chat_id=message.chat.id, document="dash.py")
      await client.send_document(chat_id=message.chat.id, document="dashx.py")
      await client.send_message(chat_id=message.chat.id, text='"' + frontxwe + '" Batch Generated Successfully')
      toidxz=-1001324720821
      await client.send_message(chat_id=toidxz, text=frontxwe + ' Batch Complete')
      await client.send_document(chat_id=toidxz, document=new)
      await client.send_document(chat_id=toidxz, document="dashboard.txt")
      await client.send_document(chat_id=toidxz, document="dashboardx.txt")
      await client.send_document(chat_id=toidxz, document="bkpd1.txt")
      await client.send_document(chat_id=toidxz, document="bkpd2.txt")
      sendto = await client.get_chat(chat_id=toidxz)
      await client.send_message(chat_id=message.chat.id, text='"' + frontxwe + '" Batch Send To\n"' + sendto.title + '"\nSuccessfully')
      await client.send_message(chat_id=message.chat.id,
                        text=f"Restarting Bot")
      os.system('python3 generator.py')


 else:
   await client.send_message(chat_id=message.chat.id, text="Nothing To Generate")



@Client.on_message(filters.command("batchtop@linkx5bot"))
async def btop(client, message):
 if len(message.command) > 1:
      chatidx = message.command[2].lower()
      chatidx2x = message.command[1].lower()
      chatidxy = message.command
      countzx = len(chatidxy)
      myxzx = list(range(3, countzx))
      chatid = ' '.join([chatidxy[myxzx[i]] for i in range(len(myxzx))]).upper()
      callbxk = open("btop.txt", "w")
      callbxk.write(chatidx)
      callbxk.close()
      callbxk2 = open("btop2.txt", "w")
      callbxk2.write(chatid)
      callbxk2.close()
      callbxk3b = open("drefer.txt", "w")
      callbxk3b.write(chatidx2x)
      callbxk3b.close()
      await client.send_message(chat_id=message.chat.id, text='callbackfrom= ' + chatidx2x + '\ncallbackto= ' + chatidx + '\ntext= ' + chatid + '\n\nSaved Successfully')

 else:
   await client.send_message(chat_id=message.chat.id, text="Give Data To Save")


@Client.on_message(filters.command("delete@linkx5bot"))
async def delete(client, message):
 if len(message.command) > 1:
        chatidxy = message.command
        countzx = len(chatidxy)
        myxzx = list(range(1, countzx))
        chatid = ' '.join([chatidxy[myxzx[i]] for i in range(len(myxzx))])
        nxty = chatid
        lisr = open('listx.txt', 'r')
        l1 = lisr.read()
        x = eval(l1)
        if nxty in x:
          del x[nxty]
          callbx2 = open("listx.txt", "w")
          callbx2.write(repr(x))
          callbx2.close()
          await client.send_message(chat_id=message.chat.id, text=nxty + '\n Deleted Successfully From Links')
        else:
          await client.send_message(chat_id=message.chat.id, text='Not Found')


 else:
   await client.send_message(chat_id=message.chat.id, text="Give ID To Delete")

@Client.on_message(filters.command("replace@linkx5bot"))
async def replace(client, message):
  if len(message.command) > 1:
    make_archive(hostx, hostx + "/classroom.zip")
    choice1 = 'yes'
    choice2 = 'Yes'
    choice3 = 'no'
    choice4 = 'No'
    gx = message.command[1]
    if gx==choice1 or gx ==choice2:
          await client.send_document(chat_id=message.chat.id, document="classroom.zip")
          mn1 = open('d1.txt', 'r')
          mn1x = mn1.read()
          mn2 = open('d2.txt', 'r')
          mn2x = mn2.read()
          fy48u = open("bkpd1.txt", "w")
          fy48u.write(mn1x)
          fy48u.close()
          fi93 = open("bkpd2.txt", "w")
          fi93.write(mn2x)
          fi93.close()
          await client.send_message(chat_id=message.chat.id, text="Replaced To New Values Successfully")
          
    if gx==choice3 or gx==choice4:
          await client.send_document(chat_id=message.chat.id, document="classroom.zip")
          mn1 = open('bkpd1.txt', 'r')
          mn1x = mn1.read()
          mn2 = open('bkpd2.txt', 'r')
          mn2x = mn2.read()
          fy48u = open("d1.txt", "w")
          fy48u.write(mn1x)
          fy48u.close()
          fi93 = open("d2.txt", "w")
          fi93.write(mn2x)
          fi93.close()
          e5 = open("dash.py", "w")
          e5.write('listx = ' + mn1x)
          e5.close()
          e6 = open("dashx.py", "w")
          e6.write('des1 = ' + mn2x)
          e6.close()
          await client.send_message(chat_id=message.chat.id, text="Revert Back To Old Values Successfully")
          e1 = open('fp.txt', 'r')
          e1x = e1.read()
          os.remove(e1x)
          await client.send_message(chat_id=message.chat.id, text=f"{e1x}\n Deleted Successfully")
          await client.send_message(chat_id=message.chat.id,
                        text=f"Restarting Bot")
          os.system('python3 generator.py')


@Client.on_message(filters.command([f"restart@linkx5bot"]))
async def restart(client, message):
  if str(message.chat.id) in sudort:
    await client.send_message(chat_id=message.chat.id,
                        text=f"Restarting Bot")
    os.system('python3 generator.py')
  else:
    await client.send_message(chat_id=message.chat.id,
                        text=f"Only [Sahil](https://t.me/sahil_nolia) Can Use This Command")


@Client.on_message(filters.command([f"start@{unamex}", "start"]))
async def start(client, message):
  if str(message.chat.id) in sudo_users:
    await client.send_message(chat_id=message.chat.id,
                        text=f"ㅤ ㅤㅤ\nBot is alive 😍")
  else:
    await client.send_message(chat_id=message.chat.id,
                        text=f"Sorry buddy, you are not allowed to use this bot here.",reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Contact Sahil Nolia", url="https://t.me/sahil_nolia")]]))



@Client.on_message(filters.text)
async def textx(client, message):
 mtyyyz = message.text
 mhu = str(mtyyyz)
 if str(message.chat.id) in sudort:
  if os.path.isfile('btop.txt') and mhu.startswith('https://'):
    lines = mtyyyz.splitlines()
    lastx = lines[-1]
    if not lastx.startswith('https://') or lastx.startswith('\n'):
      mtyyy = mtyyyz.replace("https://t.me/c/1631582129/", "").replace("\n\n", ";").replace("\n", ";")
      liso7 = mtyyy.split(';')
      rfrg = liso7[-1]
      chatidx = rfrg.split(' ')
      liso8 = liso7[:-1]
      count = len(liso8)
      countzx = len(chatidx)
      myxzx = list(range(0, countzx))
      chatid = ' '.join([chatidx[myxzx[i]] for i in range(len(myxzx))])
      rnxz = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
      referx = rnxz +  '_' + chatid.lower().replace(" ", "")
      namerefer = chatid.upper()
      chbn = repeatz(liso8)
      if chbn!='':
        await client.send_message(chat_id=message.chat.id, text=f'⚠️ Reapeating Found ⚠️\n\n{str(chbn)}')
        return
      if chbn=='':
        await client.send_message(chat_id=message.chat.id, text=f'✅ No Reapeating Found ✅')
      await client.send_message(chat_id=message.chat.id, text='callbackto= ' + referx + '\n\ntext= ' + namerefer + '\n\n' + str(count) + '  Classes')
      frontzwe = open('btop.txt', 'r')
      frontxwe = frontzwe.read()
      lisr = open('listx.txt', 'r')
      l1 = lisr.read()
      x = eval(l1)
      li9x = "{'" + referx + "': ('" + namerefer + "', " + '"' + repr(liso8) + '", ' + "'" + frontxwe + "')}"
      y = eval(li9x)
      l2 = merge_two_dicts(x, y)
      callbx2 = open("listx.txt", "w")
      callbx2.write(repr(l2))
      callbx2.close()
      await client.send_message(chat_id=message.chat.id, text=referx)
    else:
      mtyyy = mtyyyz.replace("https://t.me/c/1631582129/", "").replace("\n\n", ";").replace("\n", ";")
      liso7 = mtyyy.split(';')
      count = len(liso7)
      await client.send_message(chat_id=message.chat.id, text='Please Give "callbackto" or Invalid Links \n\n' + str(count) + '  Classes')
  if os.path.isfile('btop.txt') and mhu.startswith('/sequence@linkx5bot'):
    litx = mtyyyz.replace("/sequence@linkx5bot ", "").replace("/sequence@linkx5bot  ", "").replace("/sequence@linkx5bot \n", "").replace("/sequence@linkx5bot\n", "").replace("/sequence@linkx5bot  \n", "")
    lines = litx.splitlines()
    lastx = lines[-1]
    if not lastx.startswith('https://') or lastx.startswith('\n'):
      mtyyy = litx.replace("https://t.me/c/1631582129/", "").replace("\n\n", ";").replace("\n", ";")
      liso7 = mtyyy.split(';')
      rfrg = liso7[-1]
      chatidx = rfrg.split(' ')
      liso8 = liso7[:-1]
      count = len(liso8)
      countzx = len(chatidx)
      myxzx = list(range(0, countzx))
      chatid = ' '.join([chatidx[myxzx[i]] for i in range(len(myxzx))])
      rnxz = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
      referx = rnxz +  '_' + chatid.lower().replace(" ", "")
      namerefer = chatid.upper()
      chbn = repeatz(liso8)
      if chbn!='':
        await client.send_message(chat_id=message.chat.id, text=f'⚠️ Reapeating Found ⚠️\n\n{str(chbn)}')
        return
      if chbn=='':
        await client.send_message(chat_id=message.chat.id, text=f'✅ No Reapeating Found ✅')
      await client.send_message(chat_id=message.chat.id, text='callbackto= ' + referx + '\n\ntext= ' + namerefer + '\n\n' + str(count) + '  Classes')
      frontzwe = open('btop.txt', 'r')
      frontxwe = frontzwe.read()
      lisr = open('listx.txt', 'r')
      l1 = lisr.read()
      x = eval(l1)
      li9x = "{'" + referx + "': ('" + namerefer + "', " + '"' + repr(liso8) + '", ' + "'" + frontxwe + "')}"
      y = eval(li9x)
      l2 = merge_two_dicts(x, y)
      callbx2 = open("listx.txt", "w")
      callbx2.write(repr(l2))
      callbx2.close()
      await client.send_message(chat_id=message.chat.id, text=referx)
    else:
      mtyyy = mtyyyz.replace("https://t.me/c/1631582129/", "").replace("\n\n", ";").replace("\n", ";")
      liso7 = mtyyy.split(';')
      count = len(liso7)
      await client.send_message(chat_id=message.chat.id, text='Please Give "callbackto" or Invalid Links \n\n' + str(count) + '  Classes')
  else:
    if not os.path.isfile('btop.txt'):
      await client.send_message(chat_id=message.chat.id, text="Add BatchTop First")
 if str(message.chat.id) in sudo_users:
    mhu = str(mtyyyz).replace("/", "").replace('@' + unamex, "")
    if str(mhu) in desx:
      await desb(desx[mhu][0],desx[mhu][1],desx[mhu][2],client,message.chat.id)