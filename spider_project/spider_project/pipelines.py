# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from six.moves.urllib.parse import urljoin

import os
import json
import logging

import scrapy
from scrapy.utils.serialize import ScrapyJSONEncoder
_encoder = ScrapyJSONEncoder()

logger = logging.getLogger('SpiderProjectPipeline')

def compare(item_json, json_data):
    """
    Compare the two json data and return list which contains the wrong value
    """
    item_json_data = item_json[0]["data"]
    json_data_data = json_data[0]["data"]

    output = []
    for key, value in json_data_data.items():
        if key not in item_json_data:
            output.append(key)
        else:
            if item_json_data[key] != value:
                output.append(key)
    return output

class SpiderProjectPipeline(object):
    def process_item(self, item, spider):
        logger.info(60 * "=")
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        base_dir = base_dir + "/release/"

        if "taskid" not in item or not item["taskid"]:
            raise Exception("taskid lost in item returned by spider")

        if "data" not in item or not item["data"]:
            raise Exception("data lost in item returned by spider")

        taskid = item["taskid"]
        file_path = urljoin(base_dir, taskid + ".json")
        if not os.path.isfile(file_path):
            raise Exception(file_path + " not found")

        with open(file_path) as f:
            json_data = json.loads(f.read())

        item_json = json.loads(_encoder.encode([item]))
        cmp_ls = compare(item_json, json_data)
        if cmp_ls:
            logger.info("field below have some wrong value")
            logger.info("\n".join(cmp_ls))
        else:
            pass

        logger.info(60 * "=")
        return item

# class SpiderProjectPipeline(object):
#     def process_item(self, item, spider):
#         logger.info(60 * "=")
#         # get task url from the taskid
#         settings = spider.settings
#         prefix = settings["WEB_APP_PREFIX"]

#         if "taskid" not in item:
#             raise Exception("taskid lost in item returned by spider")

#         taskid = item["taskid"]
#         prefix = urljoin(prefix, "task")
#         url = urljoin(prefix + "/", taskid)
#         logger.info("start to check on url " + url)

#         if "data" not in item:
#             raise Exception("data lost in item returned by spider")

#         data = item["data"]
#         dic = {
#             "taskid": taskid,
#             "data": data
#         }
#         json_data = json.dumps(dic)
#         r = requests.post(url, data = {'json':json_data})
#         resp_json = r.json()
#         if resp_json["resp"]:
#             logger.info("OOPS! you have failed " + taskid)
#             logger.info("\n".join(resp_json["resp"]))
#         else:
#             logger.info("Congratulations! you have passed " + taskid)
#             logger.info("Please continue to get more!")

#         logger.info(60 * "=")
#         return item

