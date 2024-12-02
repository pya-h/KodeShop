from django import template
from kodeshop.utils import PaginationParams


register = template.Library()


@register.filter
def times(number):
    return range(1, number + 1)


@register.filter
def nearpage(pages, page=1, limit=PaginationParams.maxButtonsRange):
    return range(page - limit if page > limit + 1 else 1, page + limit + 1 if page + limit < pages else pages + 1)


@register.filter
def isplit(str_numbers):
    return [int(x) for x in str_numbers.split()]

