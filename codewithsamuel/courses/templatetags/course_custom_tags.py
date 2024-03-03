from django import template
import math

from courses.models import UserCourse , Course
register = template.Library()

# 100 -> 10% --> 100 - (  mrp * discount *  0.01 ) = selprice
@register.simple_tag
def cal_sellprice(price , discount):
    if discount is None or discount is 0:
        return price
    sellprice = 0
    sellprice = ( price - discount)
    return math.floor(sellprice)

@register.filter
def rupee(price):
    return f'₹{price}'


@register.simple_tag
def is_enrolled(request , course):
    user = None
    if not request.user.is_authenticated :
        return False
    user = request.user
    try:
        user_course = UserCourse.objects.get(user = user , course = course)
        return True
    except:
        return False
