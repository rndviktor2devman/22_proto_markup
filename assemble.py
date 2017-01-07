import staticjinja

index_data = {
    'page': 'index',
    'user': 'Леонид Федорович',
    'title': 'Главная | Поиск',
    'requests': 'Свежие заявки',
    'comments': 4,
    'show_footer': True,
    'items': 3,
    'user_info': 'Кирилл, 29 лет, г. Барабинск',
    'item_comment': '''Бла-бла, мне помогло, все супер! Бла-бла,
                мне помогло, все супер! Бла-бла, мне помогло,
                все супер! Бла-бла, мне помогло, все супер!
                Бла-бла, мне помогло, все супер!'''
}

comments_data = {
    'comment_time': 'вчера, в 12:50',
    'request_text': '''60шт. ПК от 72-15  до ПК 21-15,
                        Криводановка, с доставкой.''',
    'request_name': 'Алексей',
    'views_count': '9'
}

requests_data = {
    'title': 'Заявки',
    'user': 'Леонид Федорович',
    'comments': 7,
    'show_footer': True
}

private_data = {
    'user': 'Леонид Федорович',
    'title': 'Каталог организаций',
    'items': 7,
    'show_footer': True
}

partners_data = {
    'partner_name': 'ООО Строй-Сервис-Монтаж',
    'partner_area': 'Место деятельности: Новосибирск',
    'partner_production': 'Продукция: ЖБИ, бетон',
    'partner_address': 'Адрес: Под часами, на том-же месте',
    'partner_contact_phone': '00-00-00'
}

catalog_data = {
    'user': 'Some user',
    'title': 'Catalog',
    'items': 5,
    'show_footer': True
}

companies_data = {
    'user': 'Леонид Федорович',
    'title': 'Каталог организаций',
    'items': 5,
    'footer': True
}
company_data = {
    'user': 'Леонид Федорович',
    'title': 'Информация о организации',
    'footer': True
}

index_data.update(comments_data)
requests_data.update(comments_data)
catalog_data.update(partners_data)
companies_data.update(partners_data)

if __name__ == '__main__':
    site = staticjinja.make_site(outpath='static', contexts=[
        ('index.html', index_data),
        ('catalog.html', catalog_data),
        ('private.html', private_data),
        ('requests.html', requests_data),
        ('company.html', company_data),
        ('companies.html', companies_data)
    ])
    site.render()
