from pygal_maps_world.i18n import COUNTRIES

# 获取两个字母的国别码
for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])


