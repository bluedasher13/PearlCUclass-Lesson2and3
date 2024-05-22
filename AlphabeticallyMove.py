# 匯入 os 模組，用於執行與操作系統相關的功能
import os
# 匯入 shutil 模組，用於執行檔案和資料夾的操作，例如複製、移動、刪除等
import shutil
# 匯入 tqdm 模組，用於在迭代過程中顯示進度條，提供使用者視覺上的進度感知
import tqdm

# 檢查備份資料夾是否存在，如果存在則刪除它後重新複製
def create_backup_folder(source_folder, backup_folder):
    # 創建一個名為"Original"的資料夾，並複製指定的資料夾到"Original"中
    process_folder = os.path.join(source_folder, backup_folder)
    # 如果備份資料夾已經存在
    if os.path.exists(process_folder):  
        # 刪除它以便重新複製
        shutil.rmtree(process_folder)  
    # 複製原始資料夾內容到備份資料夾
    shutil.copytree(source_folder, process_folder)  

# 移動子資料夾到對應的資料夾
def move_folder_to_folder(folder_name, source_folder):
    # 取得資料夾名稱的第一個字母並轉換為大寫
    first_char = folder_name[0].upper()  
    
    # 如果第一個字母在'A'和'Z'之間
    if 'A' <= first_char <= 'Z':  
        # 計算目標資料夾的路徑
        target_folder = os.path.join(source_folder, first_char)  
    else:
        # 否則，設置目標資料夾為'others'資料夾
        target_folder = os.path.join(source_folder, 'others')  
    
		# 確保目標資料夾存在，檢查目標資料夾是否存在，如果不存在則創建它
		# 如果目標資料夾不存在
    if not os.path.exists(target_folder):
        # 創建該資料夾
        os.makedirs(target_folder)
    
    # 計算子資料夾的路徑
    source_subfolder = os.path.join(source_folder, folder_name)  
    # 計算目標子資料夾的路徑
    target_subfolder = os.path.join(target_folder, folder_name)  

    # 移動子資料夾到目標位置
    shutil.move(source_subfolder, target_subfolder)  

# 程式進入點
if __name__ == "__main__":
    # 讓使用者輸入原始資料夾的路徑
    source_folder = input("請輸入原始資料夾的路徑：")
    # 備份資料夾的名稱
    backup_folder = "Original"  
    
    # 將指定資料夾內容先備份到"Original"中
    create_backup_folder(source_folder, backup_folder)
    
    # 列出指定資料夾中的所有檔案
    for filename in tqdm.tqdm(os.listdir(source_folder), desc="檔案移動中"):
        # 移動子資料夾到對應的目標資料夾
        move_folder_to_folder(filename, source_folder)  
    
    # 印出移動完成的訊息
    print("檔案移動完成。")