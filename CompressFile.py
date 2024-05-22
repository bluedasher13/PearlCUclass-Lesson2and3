# 從Python標準函式庫中引入操作系統相關功能的模組
import os
# 引入 Python 的 zipfile 模組，用於處理 ZIP 壓縮
import zipfile

def zip_path(source_path, zip_file_path):
    """
    壓縮指定文件或資料夾內容到一個ZIP檔中。
    Args:
        source_path (str): 要壓縮的檔案或資料夾路徑。
        zip_file_path (str): 指定要操作的ZIP檔路徑。
    """
    zipf = zipfile.ZipFile(zip_file_path, 'w')
    # 如果指定路徑是一個檔案
    if os.path.isfile(source_path):
        # 將該檔案壓縮成 ZIP
        zipf.write(source_path, os.path.basename(source_path))
    # 如果指定路徑是一個資料夾
    elif os.path.isdir(source_path):
        # 遍歷資料夾內容
        for root, dirs, files in os.walk(source_path):
            for file in files:
                # 取得檔案的完整路徑
                file_path = os.path.join(root, file)
                # 將檔案壓縮成 ZIP
                zipf.write(file_path, os.path.relpath(file_path, source_path))
    print(f'成功壓縮 {source_path} 到 {zip_file_path}')
    # 在操作結束後需記得關閉和釋放資源
    zipf.close()

if __name__ == "__main__":
    # 提示用戶輸入要壓縮的檔案或資料夾路徑
    source_path = input("請輸入要壓縮的檔案或資料夾路徑：")
    # 提示用戶輸入輸出的 ZIP 檔路徑，並加上 .zip 的擴展名    
    output_zip = input("請輸入輸出的ZIP檔路徑：") + '.zip'
    # 呼叫 zip_path 函數執行壓縮操作
    zip_path(source_path, output_zip)