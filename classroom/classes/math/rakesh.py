from pyrogram import Client
from generator import sudo_users
from pyromod.helpers import ikb
import Config

linkx = str("https://classesbysahil.up.railway.app/")
d1 = ["[((", "))]", ")), ((", "), ["]
d2 = ["[[(", ")]]", ")], [(", "], ["]

async def mydata(client,callback_query):
  if str(callback_query.message.chat.id) in sudo_users:
    txt=callback_query.data
    listx = {'rk50': ('Rakesh Yadav Math Classes 1-50', ['153', '154', '155', '156', '157', '158', '159', '160', '161', '162', '163', '164', '165', '166', '167', '168', '169', '170', '171', '172', '173', '174', '175', '176', '177', '178', '179', '180', '181', '182', '183', '184', '185', '186', '187', '188', '189', '190', '191', '192', '193', '194', '195', '196', '197', '198', '199', '200', '201', '202'], 'rakesh'), 'rk100': ('Rakesh Yadav Math 51-100', ['203', '204', '205', '206', '207', '208', '209', '210', '211', '212', '213', '214', '215', '216', '217', '218', '219', '220', '221', '222', '223', '224', '225', '226', '227', '228', '229', '230', '231', '232', '233', '234', '235', '236', '237', '238', '239', '240', '241', '242', '243', '244', '245', '246', '247', '248', '249', '250', '251', '252'], 'rakesh'), 'rk150': ('Rakesh Yadav Math 101-150', ['253', '254', '255', '256', '257', '258', '259', '260', '261', '262', '263', '264', '265', '266', '267', '268', '269', '270', '271', '272', '273', '274', '275', '276', '277', '278', '279', '280', '281', '282', '283', '284', '285', '286', '287', '288', '289', '290', '291', '292', '293', '294', '295', '296', '297', '298', '299', '300', '301', '302'], 'rakesh'), 'rk200': ('Rakesh Yadav Math 151-200', ['303', '304', '305', '306', '307', '308', '309', '310', '311', '312', '313', '314', '315', '316', '317', '318', '319', '320', '321', '322', '323', '324', '325', '326', '327', '328', '329', '330', '331', '332', '333', '334', '335', '336', '337', '338', '339', '340', '341', '342', '343', '344', '345', '346', '347', '348', '349', '350', '351', '352'], 'rakesh'), 'rk250': ('Rakesh Yadav Math 201-250', ['353', '354', '355', '356', '357', '358', '359', '360', '361', '362', '363', '364', '365', '366', '367', '368', '369', '370', '371', '372', '373', '374', '375', '376', '377', '378', '379', '380', '381', '382', '383', '384', '385', '386', '387', '388', '389', '390', '391', '392', '393', '394', '395', '396', '397', '398', '399', '400', '401', '402'], 'rakesh'), 'rk297': ('Rakesh Yadav Classes 251-297', ['403', '404', '405', '406', '407', '408', '409', '410', '411', '412', '413', '414', '415', '416', '417', '418', '419', '420', '421', '422', '423', '424', '425', '426', '427', '428', '429', '430', '431', '432', '433', '434', '435', '436', '437', '438', '439', '440', '441', '442', '443', '444', '445', '446', '447', '448', '449'], 'rakesh'), 'rkdi': ('DI', ['450', '451', '452', '453', '454', '455'], 'rakesh')}

    if txt=="rk50":
      d = dict(listx)
      vx = d[txt]
      lis = eval(str(vx[1]))
      text = vx[0]
      call = vx[2]
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


    if txt=="rk100":
      d = dict(listx)
      vx = d[txt]
      lis = eval(str(vx[1]))
      text = vx[0]
      call = vx[2]
      n = ', '.join([f"('   Class- {str(i+51)}   ', '{linkx}{lis[i]}/stream/{str(i+51)}', 'url')" for i in range(len(lis))])
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

    if txt=="rk150":
      d = dict(listx)
      vx = d[txt]
      lis = eval(str(vx[1]))
      text = vx[0]
      call = vx[2]
      n = ', '.join([f"('   Class- {str(i+101)}   ', '{linkx}{lis[i]}/stream/{str(i+101)}', 'url')" for i in range(len(lis))])
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

    if txt=="rk200":
      d = dict(listx)
      vx = d[txt]
      lis = eval(str(vx[1]))
      text = vx[0]
      call = vx[2]
      n = ', '.join([f"('   Class- {str(i+151)}   ', '{linkx}{lis[i]}/stream/{str(i+151)}', 'url')" for i in range(len(lis))])
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

    if txt=="rk250":
      d = dict(listx)
      vx = d[txt]
      lis = eval(str(vx[1]))
      text = vx[0]
      call = vx[2]
      n = ', '.join([f"('   Class- {str(i+201)}   ', '{linkx}{lis[i]}/stream/{str(i+201)}', 'url')" for i in range(len(lis))])
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

    if txt=="rk297":
      d = dict(listx)
      vx = d[txt]
      lis = eval(str(vx[1]))
      text = vx[0]
      call = vx[2]
      n = ', '.join([f"('   Class- {str(i+251)}   ', '{linkx}{lis[i]}/stream/{str(i+251)}', 'url')" for i in range(len(lis))])
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

    if txt=="rkdi":
      d = dict(listx)
      vx = d[txt]
      lis = eval(str(vx[1]))
      text = vx[0]
      call = vx[2]
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
    


    if txt=="rkorder":
        from_chat_idx=Config.CLASSES_CHAT
        await client.copy_message(
            chat_id=callback_query.message.chat.id,
            from_chat_id=from_chat_idx,
            message_id=601)
        await client.copy_message(
            chat_id=callback_query.message.chat.id,
            from_chat_id=from_chat_idx,
            message_id=602)
        await client.copy_message(
            chat_id=callback_query.message.chat.id,
            from_chat_id=from_chat_idx,
            message_id=603)
        await client.copy_message(
            chat_id=callback_query.message.chat.id,
            from_chat_id=from_chat_idx,
            message_id=604)
        await client.copy_message(
            chat_id=callback_query.message.chat.id,
            from_chat_id=from_chat_idx,
            message_id=605)
        await client.copy_message(
            chat_id=callback_query.message.chat.id,
            from_chat_id=from_chat_idx,
            message_id=606)
        await client.copy_message(
            chat_id=callback_query.message.chat.id,
            from_chat_id=from_chat_idx,
            message_id=607)
        await client.copy_message(
            chat_id=callback_query.message.chat.id,
            from_chat_id=from_chat_idx,
            message_id=608)

    if txt=="rkallpdf":
        await client.copy_message(
            chat_id=callback_query.message.chat.id,
            from_chat_id=Config.CLASSES_CHAT,
            message_id=599)

    if txt=="rkallpdfchannel":
        keyboard = ikb([[('All Pdfs Channel', 't.me/c/1533111128/2', 'url')], [('Back', 'rakesh')]])
        await callback_query.message.edit('All Pdfs Channel , Ask Sahil if not joined',
                        disable_web_page_preview=True, reply_markup=keyboard)

  else:
    await client.send_message(chat_id=callback_query.message.chat.id,
                        text=f"What are you doing buddy.")