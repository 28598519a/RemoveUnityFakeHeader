import os

def process_ab_files(root_folder):
    signature = b'UnityFS'  # 用於搜尋 UnityFS 的標記

    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith('.ab'):
                file_path = os.path.join(dirpath, filename)
                
                with open(file_path, 'rb') as f:
                    data = f.read()
                
                # 搜尋 UnityFS 的位置
                unityfs_index = data.find(signature)
                
                if unityfs_index != -1:
                    data = data[unityfs_index:]
                    
                    # 覆寫原始檔案
                    with open(file_path, 'wb') as f:
                        f.write(data)

root_folder = 'path_to_your_directory'  # 修改成你的目錄路徑
process_ab_files(root_folder)
