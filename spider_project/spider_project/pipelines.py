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

def compare_single(item_json, json_data):
    """
    Compare the two json data and return list which contains the wrong value
    """
    item_json_data = item_json["data"]
    json_data_data = json_data["data"]

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

        item_json = json.loads(_encoder.encode(item))
        if len(json_data) == 1:
            cmp_ls = compare_single(item_json, json_data[0])
        else:
            # if the target json_data is a dataset, just pick the ong based
            # on sku
            if "sku" not in item["data"] or not item["data"]["sku"]:
                raise Exception("sku lost in item returned by spider")

            target_json_data = filter(
                lambda x:x["data"]["sku"] == item["data"]["sku"], json_data)
            if not target_json_data:
                raise Exception("sku wrong value, please check the doc")
            target_json_data = target_json_data[0]
            cmp_ls = compare_single(item_json, target_json_data)

        if cmp_ls:
            logger.info("Field below have some wrong value")
            logger.info("\n".join(cmp_ls))
        else:
            logger.info("Data got is right! Good job")

        logger.info(60 * "=")
        return item

