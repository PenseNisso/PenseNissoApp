class TrigramSearch:
    def __init__(self, min_score) -> None:
        self.min_score = min_score

    def filter_set(self, keyword: str, set) -> "list[str]":
        filtered = []
        for string in set:
            score = 0
            for i in range(len(keyword) - 2):
                if keyword[i : i + 3] in string:
                    score += 1
            if score >= self.min_score:
                filtered.append(string)
        return filtered
