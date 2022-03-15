from django import template

register = template.Library()


@register.filter(name="Censor")
# регистрируем наш фильтр под именем stop, чтоб django понимал,
# что это именно фильтр, а не простая функция
def stop(value,arg):
    value_sp = value.split()
    value1 = ''
    for wrd in value_sp:
        if isinstance(wrd, str) and wrd == arg:
            a = len(arg) - 2
            value1 = value1 + f"{arg[0]}{'*' * a}{arg[-1]} "
        else:
            value1 = value1 + wrd + ' '
    return value1