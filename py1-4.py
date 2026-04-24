import os
import shutil
from datetime import datetime

def backup_file(source_file, target_folder):

    if not os.path.exists(source_file):
        print(f"錯誤: 找不到來源檔案 '{source_file}'")
        return
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
        print(f"建立新資料夾: {target_folder}")
    try:
        # 產生時間戳記檔名 (例如: 20260413_1530_data.csv)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        print("timestamp:",timestamp)
        file_name = os.path.basename(source_file)
        print("file_name:",file_name)
        new_file_name = f"{timestamp}_{file_name}"
        print("new_file_name:",new_file_name)
        # 組合完整的 目標路徑
        destination = os.path.join(target_folder, new_file_name)
        print("destination:",destination)
        shutil.copy2(source_file, destination) # 執行複製
        print(f"備份成功 檔案已存至: {destination}")
    except Exception as e:
        print(f"備份失敗: {e}")

backup_file("data.csv","my_backups")




