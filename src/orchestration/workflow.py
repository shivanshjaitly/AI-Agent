from adapters.langchain_adapter import LangchainAdapter
from adapters.database_adapter import DatabaseAdapter
from domain.services.query_builder_service import build_query
from domain.services.result_formatter_service import format_result


def normalize_months(months):
    month_map = {
        "january": 1, "february": 2, "march": 3,
        "april": 4, "may": 5, "june": 6,
        "july": 7, "august": 8, "september": 9,
        "october": 10, "november": 11, "december": 12
    }

    numeric = []

    for m in months:
        if isinstance(m, int):
            numeric.append(m)
        elif isinstance(m, str):
            m_lower = m.lower().strip()
            if m_lower in month_map:
                numeric.append(month_map[m_lower])

    return numeric


class Workflow:

    def __init__(self):
        self.ai = LangchainAdapter()
        self.db = DatabaseAdapter()

    def process(self, user_input):

        parsed = self.ai.parse(user_input)

        metric = parsed.get("metric")
        raw_months = parsed.get("months", [])

        # ✅ FIX HERE
        months = normalize_months(raw_months)

        query = build_query(metric, months)

        result = self.db.run(query)

        return format_result(metric, result)
