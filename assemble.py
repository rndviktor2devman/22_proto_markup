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

company_data = {
    'name': '',
    'area': '',
    'production': '',
    'address': '',
    'contact_phone': ''
}

if __name__ == '__main__':
    site = staticjinja.make_site(outpath='static', contexts=[
        ('index.html', index_data)
    ])
    site.render()
