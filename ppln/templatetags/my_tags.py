from django import template

register = template.Library()

@register.filter
def modulo(num, val):
    return num % val
    
@register.simple_tag
def relative_url(value, field_name, urlencode=None):
    url = '?{}={}'.format(field_name, value)
    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(lambda p: p.split('=')[0] != field_name, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = '{}&{}'.format(url, encoded_querystring)
    return url
@register.simple_tag
def sum(v1,v2):
    return v1+v2
@register.simple_tag
def vote_total(party):
    sum=0
    for c in party:
        sum += c.vote_count_tps
        sum += c.vote_count_pos
    return sum   

@register.simple_tag
def follow_up_needed(reg):
    if  reg.registrationType == 'NRSP':
        return True
    if  reg.status == 'PEN':
        return True
    return False

