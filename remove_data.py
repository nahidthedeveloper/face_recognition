import os

user_id = input("Enter user ID to remove data: ")

data_folder = 'data'
if os.path.exists(data_folder):
    files_deleted = False
    for filename in os.listdir(data_folder):
        if filename.startswith(f'user.{user_id}.'):
            file_path = os.path.join(data_folder, filename)
            os.remove(file_path)
            files_deleted = True
    if files_deleted:
        print(f"Removed data for user ID: {user_id}")
    else:
        print(f"No data found for user ID: {user_id}.")
else:
    print(f"No data folder '{data_folder}' found.")
