# -*- coding:utf-8 -*-

DOMAINS = [
    "amazon",
    "backcountry",
    "bluefly",
    "drugstore",
    "finishline",
    "jacobtime",
    "ashford",
    "jomashop",
    "thewatchery",
    "watchco",
    "worldofwatches",
    "zappos",
    "6pm",
    "eastbay",
    'ralphlauren',
    'adidas',
    '7forallmankind',
    'ae',
    'asos',
    'nordstrom',
    'newegg',
    'onlineshoes',
]


G_ALL_DOMAINS = [
    "jay_amazons",
    "jay_amazon_co_jps",
    "jay_amazon_des",
    "jay_eastbays",
    "jay_drugstores",
    "jay_zappos",
    "jay_zapposs",
    "jay_6pms",
    "jay_finishlines",
    "jay_ashfords",
    "jay_rakutens",
    "jay_vitaminworlds",
    "jay_jomashops",
    "jay_watchismos",
    "jay_jacobtimes",
    "jay_thewatcherys",
    "jay_watchcos",
    "jay_backcountrys",
    "jay_blueflys",
    "jay_jimmyjazzs",
    "jay_titleboxings",
    "jay_noblecollections",
    "jay_neimanmarcuss",
    "jay_pickyourshoes",
    "jay_worldofwatches",
    "jay_onlineshoess",
    "jay_macys",
    "jay_7forallmankinds",
    "jay_asoss",
    "jay_ralphlaurens",
    "jay_aes",
    "jay_neweggs",
]


G_DICT_QUERY_PARAMETER = {
    "amazon":          {"jay": 1, "color_images": 1, "images": 1},
    "amazon.co.jp":    {"jay": 1, "color_images": 1, "images": 1},
    "amazon.de":       {"jay": 1, "color_images": 1, "images": 1},
    "eastbay":         {"jay": 1, "sku_images": 1, "images": 1},
#    "eastbay":         {"jay": 1, "image_urls": 1, "images": 1},
    "drugstore":       {"jay": 1, "image_urls": 1, "images": 1},
    "zappos":          {"jay": 1, "color_images": 1, "colorIds": 1, "images": 1},
    "6pm":             {"jay": 1, "color_images": 1, "colorIds": 1, "images": 1},
    "finishline":      {"jay": 1, "image_urls": 1, "images": 1},
    "ashford":         {"jay": 1, "image_urls": 1, "images": 1},
    "rakuten":         {"jay": 1, "image_urls": 1, "images": 1},
    "vitaminworld":    {"jay": 1, "image_urls": 1, "images": 1},
    "jomashop":        {"jay": 1, "image_urls": 1, "images": 1},
    "watchismo":       {"jay": 1, "image_urls": 1, "images": 1},
    "jacobtime":       {"jay": 1, "image_urls": 1, "images": 1},
    "thewatchery":     {"jay": 1, "image_urls": 1, "images": 1},
    "watchco":         {"jay": 1, "image_urls": 1, "images": 1},
    "backcountry":     {"jay": 1, "image_urls": 1, "images": 1},
    "bluefly":         {"jay": 1, "image_urls": 1, "images": 1},
    "jimmyjazz":       {"jay": 1, "image_urls": 1, "images": 1},
    "titleboxing":     {"jay": 1, "image_urls": 1, "images": 1},
    "noblecollection": {"jay": 1, "image_urls": 1, "images": 1},
    "neimanmarcus":    {"jay": 1, "image_urls": 1, "images": 1},
    "pickyourshoes":   {"jay": 1, "image_urls": 1, "images": 1},
    "worldofwatches":  {"jay": 1, "image_urls": 1, "images": 1},
    "onlineshoes":     {"jay": 1, "image_urls": 1, "images": 1},
    "macys":           {"jay": 1, "image_urls": 1, "images": 1},
    "jay_amazons":          {"timestamp": 1, "color_images": 1, "images": 1},
    "jay_eastbays":         {"timestamp": 1, "sku_images": 1, "images": 1},
    "jay_drugstores":       {"timestamp": 1, "image_urls": 1, "images": 1},
    "jay_zapposs":          {"timestamp": 1, "color_images": 1, "colorIds": 1, "images": 1},
    "jay_6pms":             {"timestamp": 1, "color_images": 1, "colorIds": 1, "images": 1},
    "jay_finishlines":      {"timestamp": 1, "image_urls": 1, "images": 1},
    "jay_ashfords":         {"timestamp": 1, "image_urls": 1, "images": 1},
    "jay_rakutens":         {"timestamp": 1, "image_urls": 1, "images": 1},
    "jay_vitaminworlds":    {"timestamp": 1, "image_urls": 1, "images": 1},
    "jay_jomashops":        {"timestamp": 1, "image_urls": 1, "images": 1},
    "jay_watchismos":       {"timestamp": 1, "image_urls": 1, "images": 1},
    "jay_jacobtimes":       {"timestamp": 1, "image_urls": 1, "images": 1},
    "jay_thewatcherys":     {"timestamp": 1, "image_urls": 1, "images": 1},
    "jay_watchcos":         {"timestamp": 1, "image_urls": 1, "images": 1},
    "jay_backcountrys":     {"timestamp": 1, "image_urls": 1, "images": 1},
    "jay_blueflys":         {"timestamp": 1, "image_urls": 1, "images": 1},
    "jay_jimmyjazzs":       {"timestamp": 1, "image_urls": 1, "images": 1},
    "jay_titleboxings":     {"timestamp": 1, "image_urls": 1, "images": 1},
    "jay_noblecollections": {"timestamp": 1, "image_urls": 1, "images": 1},
    "jay_neimanmarcuss":    {"timestamp": 1, "image_urls": 1, "images": 1},
    "jay_pickyourshoess":   {"timestamp": 1, "image_urls": 1, "images": 1},
    "jay_worldofwatchess":  {"timestamp": 1, "image_urls": 1, "images": 1},
    "jay_onlineshoess":     {"timestamp": 1, "image_urls": 1, "images": 1},
    "jay_macyss":           {"timestamp": 1, "image_urls": 1, "images": 1},
    "jay_7forallmankindss": {"timestamp": 1, "image_urls": 1, "images": 1},
    "jay_asoss":            {"timestamp": 1, "image_urls": 1, "images": 1},
    "jay_ralphlaurens":     {"timestamp": 1, "image_urls": 1, "images": 1, "color_map":1},
    "jay_aes":              {"timestamp": 1, "image_urls": 1, "images": 1},
    "jay_neweggs":          {"timestamp": 1, "image_urls": 1, "images": 1},
}