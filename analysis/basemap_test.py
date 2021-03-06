#!/usr/bin/python


from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np


names = []
pops = []
lats = []
lons = []
countries = []

for line in open("major_city"):
    info = line.split()
    names.append(info[0])
    pops.append(float(info[1]))
    lat = float(info[2][:-1])
    if info[2][-1] == 'S': lat = -lat
    lats.append(lat)
    lon = float(info[3][:-1])
    if info[3][-1] == 'w': lon = -lon
    lons.append(lon)
    country = info[4]
    countries.append(country)


# lat: 维度 lon：经度
map = Basemap(projection='ortho', lat_0=35, lon_0=120, resolution='l')
map.drawcoastlines(linewidth=0.25)
map.drawcountries(linewidth=0.25)
map.drawmapboundary(fill_color='#689CD2')

# 每隔 30 画一条经线
map.drawmeridians(np.arange(0, 360, 30))
# 每隔 30 画一条维线
map.drawparallels(np.arange(-90, 90, 30))
# 填充大陆和海洋颜色
map.fillcontinents(color='#BF9E30', lake_color='#689CD2', zorder=0)

x, y = map(lons, lats)
max_pop = max(pops)
size_factor = 80.0
y_offset = 15.0
rotation = 30
for i, j, k, name in zip(x, y, pops, names):
    size = size_factor*k/max_pop
    cs = map.scatter(i, j, s=size, marker='o', color='#FF5600')
    plt.text(1, j+y_offset, name, rotation=rotation, fontsize=10)

plt.title('Major Cities in Asia & Population')
plt.show()
