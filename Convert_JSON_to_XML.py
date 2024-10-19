# 導入 json 模組，該模組提供用於 JSON 處理
import json

# 指定 JSON 檔案的路徑
json_file_path = r"C:\Users\user\Desktop\PearlCUclass\Lesson2and3\Lesson2and3\courses.json"
# 指定輸出的 XML 檔案的路徑
xml_file_path = r"C:\Users\user\Desktop\PearlCUclass\Lesson2and3\Lesson2and3\courses.xml"

# 以讀取模式 "r" 讀取 JSON 檔案，並使用 utf-8 編碼開啟 JSON 檔案
with open(json_file_path, mode="r", encoding="utf-8") as file:
    # 讀取 JSON 檔案內容並將其轉換為字典
    json_data = json.load(file)

# 初始化 XML 資料的列表
xml_data = ['<courses>']

# # 建立 XML 字串
# _xml_string = ""

# 讀取 JSON 資料中的每一個課程
for course in json_data:
    # 添加course標籤
    xml_data.append('    <course>')

    # 讀取課程中的每一個key及value
    for key, value in course.items():
        # 添加對應的 XML 標籤和內容，格式為 <key>value</key>
        xml_data.append(f"        <{key}>{value}</{key}>")

    # 添加course的結束標籤
    xml_data.append('    </course>')

xml_data.append('</courses>')

# 以寫入模式 "w" 將 XML 字串寫入 XML 檔案，並使用 utf-8 編碼開啟 XML 檔案
with open(xml_file_path, mode="w", encoding="utf-8") as file:
    # 將 xml_data 列表中的內容連接成一個字串，並寫入 XML 檔案
    file.write("\n".join(xml_data))

# 輸出 XML 檔案的路徑
print(f"XML 檔案已寫入：{xml_file_path}")
