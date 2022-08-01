from .models import Info


def infochoc(request):
    return {
        'info': Info.objects.last()
    }

