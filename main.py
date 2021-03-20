from user import User

if __name__ == '__main__':
    user_id_or_nickname = input("Введите id: ")
    vk_token = input("Введите Вк Token: ")
    yandex_token = input("Введите Яндекс Token: ")
    backup_folder = input("Введите название папки (Яндекс Диск): ")
    photos_count = int(input("Введите количество фотографии: "))
    user = User(user_id_or_nickname, vk_token, yandex_token)
    user.backup_profile_photos(photos_count, backup_folder)
