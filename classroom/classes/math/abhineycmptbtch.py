from pyrogram import Client
from generator import sudo_users
from classroom.bot.helper.links import get_links

async def mydata(client,callback_query):
  if str(callback_query.message.chat.id) in sudo_users:
    txt=callback_query.data
    listx = {'JSOF_algebra15classes': ('ALGEBRA 15 CLASSES', "['1631', '1632', '1633', '1634', '1635', '1636', '1637', '1638', '1639', '1640', '1641', '1642', '1643', '1644', '1645']", 'abhineycmptbtch'), 'NOCT_average6classes': ('AVERAGE 6 CLASSES', "['1647', '1648', '1649', '1650', '1651', '1652']", 'abhineycmptbtch'), 'XYBY_boatandstream3classes': ('BOAT AND STREAM 3 CLASSES', "['1654', '1655', '1656']", 'abhineycmptbtch'), 'P2EW_ci4classes': ('CI 4  CLASSES', "['1658', '1659', '1660', '1661']", 'abhineycmptbtch'), 'A24Y_coordinategeometry7classes': ('COORDINATE GEOMETRY 7 CLASSES', "['1663', '1664', '1665', '1666', '1667', '1668', '1669']", 'abhineycmptbtch'), '4XJ6_geometry41classes': ('GEOMETRY 41 CLASSES', "['1671', '1672', '1673', '1674', '1675', '1676', '1677', '1678', '1679', '1680', '1681', '1682', '1683', '1684', '1685', '1686', '1687', '1688', '1689', '1690', '1691', '1692', '1693', '1694', '1695', '1696', '1697', '1698', '1699', '1700', '1701', '1702', '1703', '1704', '1705', '1706', '1707', '1708', '1709', '1710', '1711']", 'abhineycmptbtch'), '23YW_lcmhcf4classes': ('LCM HCF 4  CLASSES', "['1713', '1714', '1715', '1716']", 'abhineycmptbtch'), 'BKU1_2dmensuration4classes': ('2D MENSURATION 4 CLASSES', "['1718', '1719', '1720', '1721']", 'abhineycmptbtch'), 'PS4A_3dmensuration7classes': ('3D MENSURATION 7 CLASSES', "['1723', '1724', '1725', '1726', '1727', '1728', '1729']", 'abhineycmptbtch'), 'ROM0_mixture3classes': ('MIXTURE 3 CLASSES', "['1732', '1733', '1734']", 'abhineycmptbtch'), '69A8_alligation3classes': ('ALLIGATION 3  CLASSES', "['1736', '1737', '1738']", 'abhineycmptbtch'), '3JVJ_numbersystem13classes': ('NUMBER SYSTEM 13 CLASSES', "['1740', '1741', '1742', '1743', '1744', '1745', '1746', '1747', '1748', '1749', '1750', '1751', '1752']", 'abhineycmptbtch'), 'D7VB_partnership2classes': ('PARTNERSHIP 2 CLASSES', "['1754', '1755']", 'abhineycmptbtch'), '5DNU_percentage6classes': ('PERCENTAGE 6 CLASSES', "['1757', '1758', '1759', '1760', '1761', '1762']", 'abhineycmptbtch'), '7EHR_pipeandcistern3classes': ('PIPE AND CISTERN 3 CLASSES', "['1765', '1766', '1764']", 'abhineycmptbtch'), 'NA4F_probability1class': ('PROBABILITY 1 CLASS', "['1768']", 'abhineycmptbtch'), '9IDJ_profitandloss8classes': ('PROFIT AND LOSS 8 CLASSES', "['1770', '1771', '1772', '1773', '1774', '1775', '1776', '1777']", 'abhineycmptbtch'), '1MT8_quadraticequations1class': ('QUADRATIC EQUATIONS 1 CLASS', "['1779']", 'abhineycmptbtch'), 'BYOO_ratioandproportion8classes': ('RATIO AND PROPORTION 8 CLASSES', "['1781', '1782', '1783', '1784', '1785', '1786', '1787', '1788']", 'abhineycmptbtch'), '61A5_si06classes': ('SI 06 CLASSES', "['1790', '1791', '1795', '1792', '1793', '1794']", 'abhineycmptbtch'), '4G5B_timeanddistance6classes': ('TIME AND DISTANCE 6 CLASSES', "['1798', '1799', '1800', '1801', '1802', '1803']", 'abhineycmptbtch'), 'CAZ8_train2classes': ('TRAIN 2 CLASSES', "['1805', '1806']", 'abhineycmptbtch'), 'B24T_timeandwork6classes': ('TIME AND WORK 6 CLASSES', "['1809', '1810', '1811', '1812', '1813', '1814']", 'abhineycmptbtch'), 'EP78_menwomen3classes': ('MEN WOMEN 3 CLASSES', "['1816', '1817', '1818']", 'abhineycmptbtch'), 'BPNU_workandwages2classes': ('WORK AND WAGES 2 CLASSES', "['1820', '1821']", 'abhineycmptbtch'), 'ALIA_trigonometry16classes': ('TRIGONOMETRY 16 CLASSES', "['1824', '1825', '1826', '1827', '1828', '1829', '1830', '1831', '1832', '1833', '1834', '1835', '1836', '1837', '1838', '1839']", 'abhineycmptbtch'), 'IIX5_heightanddistance3classes': ('HEIGHT AND DISTANCE 3 CLASSES', "['1841', '1842', '1843']", 'abhineycmptbtch')}
    d = dict(listx)

    if txt in listx:
      vx = d[txt]
      await get_links(eval(vx[1]),vx[0],vx[2],client,callback_query)


  else:
    await client.send_message(chat_id=callback_query.message.chat.id,
                        text=f"What are you doing buddy.")