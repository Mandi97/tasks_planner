from .models import Planner


def planners_count(request):
    if request.user.is_authenticated:
        count = Planner.objects.filter(owner=request.user).count()
    else:
        count = 0
    return {'user_planner_count': count}
