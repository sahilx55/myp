from pyrogram import Client
from generator import sudo_users
from classroom.bot.helper.links import get_links


async def mydata(client,callback_query):
  if str(callback_query.message.chat.id) in sudo_users:
    txt=callback_query.data
    listx = {'2WKV_completebatch83classes': ('COMPLETE BATCH 83 CLASSES', "['2815', '2816', '2817', '2818', '2819', '2820', '2821', '2822', '2823', '2824', '2825', '2826', '2827', '2828', '2829', '2830', '2831', '2832', '2833', '2834', '2835', '2836', '2837', '2838', '2839', '2840', '2841', '2842', '2843', '2844', '2845', '2846', '2847', '2848', '2849', '2850', '2851', '2852', '2853', '2854', '2855', '2856', '2857', '2858', '2859', '2860', '2861', '2862', '2863', '2864', '2865', '2867', '2866', '2868', '2869', '2870', '2871', '2872', '2873', '2875', '2874', '2876', '2877', '2878', '2879', '2880', '2881', '2882', '2883', '2884', '2885', '2886', '2887', '2888', '2889', '2890', '2891', '2892', '2893', '2894', '2895', '2896', '2897']", 'ressplpiyush'), 'MH31_extra4classes': ('EXTRA 4 CLASSES', "['2899', '2900', '2901', '2902']", 'ressplpiyush')}
    d = dict(listx)

    if txt in listx:
      vx = d[txt]
      await get_links(eval(vx[1]),vx[0],vx[2],client,callback_query)


  else:
    await client.send_message(chat_id=callback_query.message.chat.id,
                        text=f"What are you doing buddy.")