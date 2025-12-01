# def format_result(metric, value):

#     if value == 0:
#         return "No data found for selected period."

#     if metric.lower() == "gmv":
#         return f"Total GMV is ₹{value:,.0f}"

#     return "Unknown metric"

def format_result(kpi, value):

    if value is None:
        return "No data available"

    if kpi in ["GMV", "REVENUE", "BANK_COST"]:
        return f"{kpi} is ₹{value:,.2f}"

    if kpi in ["GROSS_MARGIN", "SUCCESS_RATE"]:
        return f"{kpi.replace('_',' ')} is {value:.2f}%"

    return "Unknown KPI"
