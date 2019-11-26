from django import template

register = template.Library()

URL_PREFIX = '/media/'
# URL_PREFIX = '/mediafiles/'


def media_folder_products(string):
    if not string:
        string = 'products_images/default.jpg'

    new_string = "{}{}".format(URL_PREFIX, string)

    return new_string


@register.filter(name='media_folder_users')
def media_folder_users(string):
    if not string:
        string = 'users_avatars/default.jpg'

    new_string = "{}{}".format(URL_PREFIX, string)

    return new_string


register.filter('media_folder_products', media_folder_products)
# register.filter('media_folder_users', media_folder_users)