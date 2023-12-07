from django.db.models import Q

from infos.models import Lawsuit, Report, News


class AbstractFilter:
    def get_q(self):
        pass


class BooleanFilter(AbstractFilter):
    def __init__(self, value, type) -> None:
        self.type = type
        self.value = value
        if type == "report":
            pass
        elif type == "news":
            pass
        elif type == "lawsuits":
            pass

    def get_q(self) -> Q:
        query = ""
        if self.value == "yes":
            q = Q(pk__in=[report.company.id for report in Report.objects.all()])
        elif self.value == "no":
            q = Q()
        else:
            q = Q()
        return q


class TextFilter(AbstractFilter):
    def __init__(self, value, type) -> None:
        self.type = type
        self.value = value

    def get_q(self) -> Q:
        type = self.type
        return Q(**{type + "__icontains": self.value})
