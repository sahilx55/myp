from pyrogram import Client
from generator import sudo_users
from pyromod.helpers import ikb

linkx = str("https://classesbysahil.up.railway.app/")
d1 = ["[((", "))]", ")), ((", "), ["]
d2 = ["[[(", ")]]", ")], [(", "], ["]


async def mydata(client,callback_query):
  if str(callback_query.message.chat.id) in sudo_users:
    txt=callback_query.data
    listx = {'0QR7_class1-50': ('CLASS 1-50', "['2582', '2583', '2584', '2585', '2586', '2587', '2588', '2589', '2590', '2591', '2592', '2593', '2594', '2595', '2596', '2597', '2598', '2599', '2600', '2601', '2602', '2603', '2604', '2605', '2606', '2607', '2608', '2609', '2610', '2611', '2612', '2613', '2614', '2615', '2616', '2617', '2618', '2619', '2620', '2621', '2622', '2623', '2624', '2625', '2626', '2627', '2628', '2629', '2630', '2631']", 'geographysplbtch'), 'KJW9_class51-100': ('CLASS 51-100', "['2632', '2633', '2634', '2635', '2636', '2637', '2701', '2639', '2640', '2641', '2642', '2643', '2644', '2645', '2646', '2647', '2648', '2649', '2650', '2651', '2652', '2653', '2654', '2655', '2656', '2657', '2658', '2659', '2660', '2661', '2662', '2663', '2664', '2665', '2666', '2667', '2668', '2669', '2670', '2671', '2672', '2690', '2691', '2692', '2693', '2694', '2695', '2696', '2697', '2698']", 'geographysplbtch'), 'EL9Z_classes101-117': ('CLASSES 101-117', "['2699', '2700', '2675', '2676', '2677', '2678', '2679', '2680', '2681', '2682', '2683', '2684', '2685', '2686', '2687', '2688', '2689']", 'geographysplbtch')}

    if txt=="0QR7_class1-50":
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


    if txt=="KJW9_class51-100":
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

    if txt=="EL9Z_classes101-117":
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


  else:
    await client.send_message(chat_id=callback_query.message.chat.id,
                        text=f"What are you doing buddy.")