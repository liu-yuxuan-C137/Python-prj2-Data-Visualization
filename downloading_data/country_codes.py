from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """根据指定的国家，返回Pygal使用的两个字母的国别码"""
    for code, name in COUNTRIES.items():
    # 用来返回一个包含字典中键值对的可迭代对象，每个元素是一个包含键和值的元组 (key, value)
    # 字典本身是可迭代对象，但默认情况下，它迭代的是键而不是键值对。
        if name == country_name:
            return code
    # 如果没有找到指定的国家，就返回None
    return None