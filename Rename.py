# 從Python標準函式庫中引入操作系統相關功能的模組
import os
import re

# 獲取路徑分隔符
separator = os.sep

# 設定存放檔案的資料夾路徑
folder_path = 'C:\\Users\\user\\Desktop\\PearlCUclass\\Lesson2and3\\Lesson2and3\\images'

# 列出資料夾中的檔案並進行批次處理
for filename in os.listdir(folder_path):
    #從檔名中擷取需要的部分，此處以 "o_" 為分隔字串
    #取第2部分作為新的檔名
    #加上前綴字串"Rename_"
    # new_filename = "rename_" + filename.split("o_")[1]

    # 使用正規表示法擷取檔名中的目標部分，以 "o_" 或 "rename_" 開頭的片段
    match = re.search(r'(?:o_|rename_)(.*)', filename)
    if match:
        # 從匹配中取出需要的部分，並加上前綴字串 "rename_"
        new_filename = "rename_" + match.group(1)
        # 使用 os.rename() 函式進行檔案重新命名
        os.rename(f"{folder_path}{separator}{filename}", f"{folder_path}{separator}{new_filename}")

# 批次處理完成
print("批次處理已完成。")
