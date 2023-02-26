from django import template

register = template.Library()

@register.filter(name='censor')    
def currency(value):

    cenc_words = ['чемпионат', 'популярного', 'Украине'] #Это наш словарь со словами, попавшими
    cenc_str = ' '                                       #под цензуру
    value_list = value.split() #Преобразуем наши заголовки и тексты статей в списки

    for i in value_list:

        if i in cenc_words:
            cenc_str = cenc_str + ' ' + i.replace(i, '****')
        else:
            cenc_str = cenc_str + ' ' +  i
    return cenc_str