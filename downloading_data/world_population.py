import json
import pygal
from country_codes import get_country_code
import pygal_maps_world.maps
from pygal.style import RotateStyle

# 将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f) # 将数据处理为一个列表,每个元素都是字典，包含四个键—值对

# 创建一个包含人口数量的字典
cc_populations = {} # 存储国别码和相对应的人口数量
# 打印每个国家2010年的人口数量
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
            # 同时赋值键值对：如果这个键 code 已经存在于字典中，它会更新该键对应的值；
            # 如果这个键不存在，则会新建一个键值对，将 code 作为键，population 作为值。
            # print(code + ": " + str(population))
        # else:
        #     print('ERROR - ' + country_name + ': no country code')
        # print(country_name + ": " + str(population))

# 根据人口数量将所有的国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# 看看每组分别包含多少个国家
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))
wm_style = RotateStyle('#336699')
wm = pygal_maps_world.maps.World(style=wm_style)

wm.title = 'World Population in 2010, by Country'
# wm.add('2010', cc_populations)
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')