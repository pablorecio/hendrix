from .models import Link


def portal_links(self):
    return {
        "links": Link.objects.all()
    }
