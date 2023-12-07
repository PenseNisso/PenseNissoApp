from django.db.models import Q


class AbstractFilter:
    def get_q(self):
        pass


class BooleanFilter(AbstractFilter):
    def __init__(self, value, type) -> None:
        self.type = type
        self.value = value

    def get_q(self) -> Q:
        query = ""
        if self.value == "yes":
            q = Q()
        elif self.value == "no":
            q = Q()
        else:
            q = Q()
        return q


class TextFilter(AbstractFilter):
    def get_q(self) -> Q:
        return Q()
