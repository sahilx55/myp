from pyrogram import Client
from generator import sudo_users
from classroom.bot.helper.links import get_links
import Config

async def mydata(client,callback_query):
  if str(callback_query.message.chat.id) in sudo_users:
    txt=callback_query.data
    listx = {'ssbhartiage1': ('ㅤAGE 1 CLASS', ['615'], 'ssbharti'), 'ssbhartialg64': ('ㅤALGEBRA 64 CLASSES', ['617', '618', '619', '620', '621', '622', '623', '624', '625', '626', '627', '628', '629', '630', '631', '632', '633', '634', '635', '636', '637', '638', '639', '640', '641', '642', '643', '644', '645', '646', '647', '648', '649', '650', '651', '652', '653', '654', '655', '656', '657', '658', '659', '660', '661', '662', '663', '664', '665', '666', '667', '668', '669', '670', '671', '672', '673', '674', '675', '676', '677', '678', '679', '680'], 'ssbharti'), 'ssbhartialgm14': ('ㅤALLIGATION & MIXTURE 14 CLASSES', ['682', '688', '689', '690', '691', '692', '693', '694', '695', '683', '684', '685', '686', '687'], 'ssbharti'), 'ssbhartiavg25': ('ㅤAVERAGE 25 CLASSES', ['697', '698', '699', '700', '701', '702', '703', '704', '705', '706', '707', '708', '709', '710', '711', '712', '713', '714', '715', '716', '717', '718', '719', '720', '721'], 'ssbharti'), 'ssbhartibst7': ('BOAT & STREAM 7 CLASSES', ['726', '727', '728', '729', '724', '725', '723'], 'ssbharti'), 'ssbhartical8': ('CALCULATION 8 CLASSES', ['731', '732', '1362', '734', '735', '736', '737', '738'], 'ssbharti'), 'ssbhartici20': ('COMPOUND INTEREST 20 CLASSES', ['741', '742', '743', '744', '745', '746', '747', '748', '749', '750', '751', '752', '753', '754', '755', '756', '757', '758', '759', '740'], 'ssbharti'), 'ssbhartidtsuf1': ('DATA SUFFICIENCY 1 CLASS', ['779'], 'ssbharti'), 'ssbharticg17': ('COORDINATE GEOMETERY 17 CLASSES', ['761', '762', '769', '770', '771', '772', '773', '763', '774', '775', '764', '765', '766', '767', '768', '776', '777'], 'ssbharti'), 'ssbhartidi19': ('DATA Interpretation 19 CLASSES', ['781', '792', '793', '794', '795', '796', '797', '798', '799', '782', '783', '784', '785', '786', '787', '788', '789', '790', '791'], 'ssbharti'), 'ssbhartidisc13': ('DISCOUNT 13 CLASSES', ['801', '802', '803', '804', '805', '806', '807', '808', '809', '810', '811', '812', '813'], 'ssbharti'), 'ssbhartigeobsc26': ('GEOMETERY BASIC 26 CLASSES', ['816', '817', '818', '819', '820', '821', '822', '823', '824', '825', '826', '827', '828', '829', '830', '831', '832', '833', '834', '835', '836', '837', '838', '839', '840', '841'], 'ssbharti'), 'ssbhartigeocir33': ('GEOMETERY CIRCLE 33 CLASSES', ['843', '844', '845', '846', '847', '848', '849', '850', '851', '852', '853', '854', '855', '856', '857', '858', '859', '860', '861', '862', '863', '864', '865', '866', '867', '868', '869', '870', '871', '872', '873', '874', '875'], 'ssbharti'), 'ssbhartigeopoly4': ('GEOMETERY POLYGON 4 CLASSES', ['877', '878', '879', '880'], 'ssbharti'), 'ssbhartihg6': ('HEIGHT & DISTANCE 6 CLASSES', ['882', '883', '884', '885', '886', '887'], 'ssbharti'), 'ssbhartilchc13': ('LCM & HCF 13 CLASSES', ['892', '889', '890', '893', '891', '894', '895', '896', '897', '898', '899', '900', '901'], 'ssbharti'), 'ssbhartimenar36': ('MENSURATION AREA 36 CLASSES', ['904', '915', '926', '934', '935', '936', '937', '938', '939', '905', '906', '907', '908', '909', '910', '911', '912', '913', '914', '916', '917', '918', '919', '920', '921', '922', '923', '924', '925', '927', '928', '929', '930', '931', '932', '933'], 'ssbharti'), 'ssbhartimenvol31': ('MENSURATION VOLUME 31 CLASSES', ['941', '942', '943', '944', '945', '946', '947', '948', '949', '950', '951', '952', '953', '954', '955', '956', '957', '958', '959', '960', '961', '962', '963', '964', '965', '966', '967', '968', '969', '970', '971'], 'ssbharti'), 'ssbhartimxp11': ('MIXED PROPORTION 11 CLASSES', ['973', '974', '975', '976', '977', '978', '979', '980', '981', '982', '983'], 'ssbharti'), 'ssbhartins37': ('NUMBER SYSTEM 37 CLASSES', ['1020', '1021', '985', '986', '1007', '1014', '1015', '1016', '1017', '1018', '1019', '987', '988', '989', '990', '991', '992', '993', '994', '995', '996', '997', '998', '999', '1000', '1001', '1002', '1003', '1004', '1005', '1006', '1008', '1009', '1010', '1011', '1012', '1013'], 'ssbharti'), 'ssbhartiprt10': ('PARTNERSHIP 10 CLASSES', ['1023', '1025', '1026', '1027', '1028', '1029', '1030', '1031', '1032', '1024'], 'ssbharti'), 'ssbhartipert37': ('PERCENTAGE 37 CLASSES', ['1034', '1045', '1056', '1065', '1066', '1067', '1068', '1069', '1070', '1035', '1036', '1037', '1038', '1039', '1040', '1041', '1042', '1043', '1044', '1046', '1047', '1048', '1049', '1050', '1051', '1052', '1053', '1054', '1055', '1057', '1058', '1059', '1060', '1061', '1062', '1064', '1063'], 'ssbharti'), 'ssbhartipermcmb15': ('PERMUTATION & COMBINATION 15 CLASSES', ['1072', '1073', '1074', '1075', '1076', '1077', '1078', '1079', '1080', '1081', '1082', '1083', '1084', '1085', '1086'], 'ssbharti'), 'ssbhartipipcis12': ('PIPE & CISTERN 12 CLASSES', ['1088', '1089', '1090', '1091', '1092', '1093', '1094', '1095', '1096', '1097', '1098', '1099'], 'ssbharti'), 'ssbhartiprob9': ('PROBABILITY 9 CLASSES', ['1101', '1102', '1103', '1104', '1105', '1106', '1107', '1108', '1109'], 'ssbharti'), 'ssbhartiplss24': ('PROFIT & LOSS 24 CLASSES', ['1111', '1122', '1128', '1129', '1130', '1131', '1132', '1133', '1134', '1112', '1113', '1114', '1115', '1116', '1117', '1118', '1119', '1120', '1121', '1123', '1124', '1125', '1126', '1127'], 'ssbharti'), 'ssbhartiquad1': ('QUADRATIC EQ 1 CLASS', ['1136'], 'ssbharti'), 'ssbhartirprop25': ('RATIO & PROPORTION 25 CLASSES', ['1138', '1139', '1150', '1156', '1157', '1158', '1159', '1160', '1161', '1162', '1140', '1141', '1142', '1143', '1144', '1145', '1146', '1147', '1148', '1149', '1151', '1152', '1153', '1154', '1155'], 'ssbharti'), 'ssbhartisi13': ('SIMPLE INTEREST 13 CLASSES', ['1164', '1165', '1166', '1167', '1168', '1169', '1170', '1171', '1172', '1173', '1174', '1175', '1176'], 'ssbharti'), 'ssbhartisimpli8': ('SIMPLICATION 8 CLASSES', ['1178', '1179', '1180', '1181', '1182', '1183', '1184', '1185'], 'ssbharti'), 'ssbhartistat1': ('STATICS 1 CLASS', ['1187'], 'ssbharti'), 'ssbhartisrdin23': ('SURDS & INDICIES 23 CLASSES', ['1189', '1200', '1204', '1205', '1206', '1207', '1208', '1209', '1210', '1211', '1190', '1191', '1192', '1193', '1194', '1195', '1196', '1197', '1198', '1199', '1201', '1202', '1203'], 'ssbharti'), 'ssbhartitw22': ('TIME & WORK 22 CLASSES', ['1213', '1224', '1228', '1229', '1230', '1231', '1232', '1233', '1234', '1214', '1215', '1216', '1217', '1218', '1219', '1220', '1221', '1222', '1223', '1225', '1226', '1227'], 'ssbharti'), 'ssbhartitdis36': ('TIME & DISTANCE 36 CLASSES', ['1236', '1247', '1258', '1266', '1267', '1268', '1269', '1270', '1271', '1237', '1238', '1239', '1240', '1241', '1242', '1243', '1244', '1245', '1246', '1248', '1249', '1250', '1251', '1252', '1253', '1254', '1255', '1256', '1257', '1259', '1260', '1261', '1262', '1263', '1264', '1265'], 'ssbharti'), 'ssbhartitrigo31': ('TRIGONOMETRY 31 CLASSES', ['1273', '1285', '1296', '1298', '1299', '1300', '1301', '1302', '1303', '1274', '1275', '1276', '1278', '1277', '1279', '1280', '1281', '1282', '1283', '1284', '1286', '1287', '1288', '1289', '1290', '1291', '1292', '1293', '1294', '1295', '1297'], 'ssbharti'), 'ssbhartiwprob19': ('WORD PROBLEM 19 CLASSES', ['1305', '1306', '1307', '1308', '1309', '1310', '1311', '1312', '1313', '1314', '1315', '1316', '1317', '1318', '1319', '1320', '1321', '1322', '1323'], 'ssbharti')}

    if txt in listx:
      d = dict(listx)
      vx = d[txt]
      await get_links(vx[1],vx[0],vx[2],client,callback_query)
    

    if txt=="ssbhartipdfs":
        await client.copy_message(
            chat_id=callback_query.message.chat.id,
            from_chat_id=Config.CLASSES_CHAT,
            message_id=1325)



  else:
    await client.send_message(chat_id=callback_query.message.chat.id,
                        text=f"What are you doing buddy.")