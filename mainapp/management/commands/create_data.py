from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from mainapp.models import Author, Book


class Command(BaseCommand):

    def handle(self, *args, **options):
        Book.objects.all().delete()
        Author.objects.all().delete()
        
        authors = [
            {'name': 'Грин', 'birthday_year': 1880},
            {'name': 'Пушкин', 'birthday_year': 1799}
        ]

        books = [
            {'name': 'Алые паруса', 'author': 'Грин'},
            {'name': 'Золотая цепь', 'author': 'Грин'},
            {'name': 'Пиковая дама', 'author': 'Пушкин'},
            {'name': 'Руслан и Людмила', 'author': 'Пушкин'}
        ]

        for item in authors:
            Author.objects.create(**item)

        for item in books:
            item['author'] = Author.objects.get(name=item['author'])
            Book.objects.create(**item)

        User.objects.all().delete()
        Group.objects.all().delete()

        # создаем суперпользователя. Админ может всё
        User.objects.create_superuser('admin', 'admin@test.com', 'admin123456')

        # Получаем Права
        # книги
        add_book = Permission.objects.get(codename='add_book')
        change_book = Permission.objects.get(codename='change_book')
        delete_book = Permission.objects.get(codename='delete_book')

        # авторы
        add_author = Permission.objects.get(codename='add_author')
        change_author = Permission.objects.get(codename='change_author')
        delete_author = Permission.objects.get(codename='delete_author')

        # создаем группы
        # младшие сотрудники
        little_staff = Group.objects.create(name='Младшие сотрудники')
        # права этой группы только книги, остальное просмотр
        
        little_staff.permissions.add(add_book)
        little_staff.permissions.add(change_book)
        little_staff.permissions.add(delete_book)
        # # старшие сотрудники
     
        big_staff = Group.objects.create(name='Старшие сотрудники')
        # права этой группы книги и авторы, остальное просмотр
        big_staff.permissions.add(add_book)
        big_staff.permissions.add(change_book)
        big_staff.permissions.add(delete_book)

        big_staff.permissions.add(add_author)
        big_staff.permissions.add(change_author)
        big_staff.permissions.add(delete_author)

        # Остальные могу только смотреть 

        # Создаем пользователей и добавляем в группы
        little = User.objects.create_user('little', 'little@little.com', 'little123456')
        little.groups.add(little_staff)
        little.save()

        big = User.objects.create_user('big', 'big@big.com', 'big123456')
        big.groups.add(big_staff)
        big.save()

        print('done')
