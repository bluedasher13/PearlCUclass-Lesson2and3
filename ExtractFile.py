import zipfile

def unzip(zip_file_path, extract_folder):
    """
    解壓縮指定的ZIP文件到指定的目錄。

    Args:
        zip_file_path (str): 要解壓縮的ZIP文件路徑。
        extract_folder (str): 解壓縮到的目錄路徑。
    """
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zipf:
            zipf.extractall(extract_folder)
        print(f'成功解壓縮 {zip_file_path} 到 {extract_folder}')
    except:
        print(f'解壓縮過程中發生錯誤')

if __name__ == "__main__":
    zip_file_path = input("請輸入要解壓縮的ZIP文件路徑：")
    extract_folder = input("請輸入解壓縮到的目錄路徑：")
    
    unzip(zip_file_path, extract_folder)
