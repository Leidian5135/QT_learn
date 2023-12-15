import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# 创建基础地图实例
m = Basemap(projection='merc', llcrnrlat=20, urcrnrlat=50, llcrnrlon=70, urcrnrlon=140, lat_ts=20, resolution='c')

# 绘制海岸线和国家边界
m.drawcountries()
m.drawcoastlines()

# 定义起点和终点城市的经纬度
locations = {
    'Beijing': {'lat': 39.9042, 'lon': 116.4074},
    'Shanghai': {'lat': 31.2304, 'lon': 121.4737},
    'Guangzhou': {'lat': 23.1291, 'lon': 113.2644}
}

# 绘制流线图
# 从北京到上海
start_lon, start_lat = locations['Beijing']['lon'], locations['Beijing']['lat']
end_lon, end_lat = locations['Shanghai']['lon'], locations['Shanghai']['lat']
m.drawgreatcircle(start_lon, start_lat, end_lon, end_lat, linewidth=2, color='blue')

# 从广州到上海
start_lon, start_lat = locations['Guangzhou']['lon'], locations['Guangzhou']['lat']
m.drawgreatcircle(start_lon, start_lat, end_lon, end_lat, linewidth=1, color='red')

# 添加图例
plt.text(0.5, 0.1, 'Beijing to Shanghai (10000 people)', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, color='blue')
plt.text(0.5, 0.05, 'Guangzhou to Shanghai (5000 people)', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, color='red')

# 显示地图
plt.show()
