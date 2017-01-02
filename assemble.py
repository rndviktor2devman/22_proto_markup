import staticjinja

index_data = {
    'page': 'index',
    'user': 'Леонид Федорович',
    'title': 'Главная | Поиск',
    'requests': 'Свежие заявки',
    'comments': 4,
    'show_footer': True
}

comments_data = {

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

catalog_data.update(partners_data)

if __name__ == '__main__':
    site = staticjinja.make_site(outpath='static', contexts=[
        ('index.html', index_data),
        ('catalog.html', catalog_data)
    ])
    site.render()
