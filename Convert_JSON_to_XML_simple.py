# 導入 json 模組，該模組提供用於 JSON 處理
import json, dicttoxml
from xml.dom.minidom import parseString

json_file_path = r"courses.json"
xml_file_path = r"courses.xml"

with open(json_file_path, mode="r", encoding="utf-8") as file:
    json_data = json.load(file)

with open(xml_file_path, mode="w", encoding="utf-8") as file:
    xml_string = dicttoxml.dicttoxml(json_data, return_bytes=False)
    xml_string = parseString(xml_string).toprettyxml()
    file.write(xml_string)

print(f"XML 檔案已寫入：{xml_file_path}")
