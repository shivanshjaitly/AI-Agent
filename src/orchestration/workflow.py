from domain.services.query_intent_service import detect_intent
# from domain.services.nlp_extraction_service import extract_month
from domain.services.nlp_extraction_service import extract_months
from domain.services.query_builder_service import build_query
from adapters.database_adapter import DatabaseAdapter
from domain.services.result_formatter_service import format_result

class Workflow:

    def process(self, user_input):
        intent = detect_intent(user_input)

        # It will work for single data 
        # say...What is the total GMV for November
        
        # month = extract_month(user_input)
        # query = build_query(intent, month)

        #for multiple records
        months = extract_months(user_input)
        query = build_query(intent, months)

        db = DatabaseAdapter()
        result = db.run(query)

        return format_result(intent, result)
