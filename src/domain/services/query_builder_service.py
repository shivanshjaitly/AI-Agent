        # It will work for single data 
        # say...What is the total GMV for November


# def build_query(intent, month):
#     if intent == "GMV":
#         return f"""
#         SELECT SUM(order_value) AS total_gmv
#         FROM XYZ
#         WHERE MONTH(order_date) = {month}
#         """

# def build_query(metric, months):

#     if not metric or not months:
#         return None

#     if metric.lower() == "gmv":
#         month_list = ",".join(str(m) for m in months)
#         return f"""
#         SELECT SUM(order_value)
#         FROM XYZ
#         WHERE MONTH(order_date) IN ({month_list})
#         """

#     return None

# def build_query(metric, months, merchant=None):

#     month_list = ",".join(str(m) for m in months)

#     if metric.lower() == "gmv":
#         return f"""
#         SELECT SUM(o.order_value)
#         FROM orders o
#         JOIN merchants m ON o.merchant_id = m.merchant_id
#         WHERE o.order_status = 'SUCCESS'
#         AND MONTH(o.order_date) IN ({month_list})
#         """
def build_query(parsed):
    kpi = parsed["kpi"]
    months = parsed["months"]
    year = parsed["year"]
    quarter = parsed["quarter"]
    period = parsed["period"]

    # ✅ Month filter clause
    month_clause = ""
    if months:
        month_list = ",".join(str(m) for m in months)
        month_clause = f"AND MONTH(txn_date) IN ({month_list})"

    # ✅ Year filter
    year_clause = f"AND YEAR(txn_date) = {year}" if year else ""

    # ✅ Quarter filter
    quarter_clause = f"AND QUARTER(txn_date) = {quarter}" if quarter else ""

    # ✅ KPI Queries
    if kpi == "GMV":
        return f"""
        SELECT SUM(order_value)
        FROM transactions
        WHERE status='SUCCESS'
        {month_clause} {year_clause} {quarter_clause}
        """

    elif kpi == "REVENUE":
        return f"""
        SELECT SUM(revenue)
        FROM transactions
        WHERE status='SUCCESS'
        {month_clause} {year_clause} {quarter_clause}
        """

    elif kpi == "BANK_COST":
        return f"""
        SELECT SUM(b.cost_amount)
        FROM bank_costs b
        JOIN transactions t ON b.txn_id=t.txn_id
        WHERE 1=1
        {month_clause.replace("txn_date","b.cost_date")}
        {year_clause.replace("txn_date","b.cost_date")}
        """
    
    elif kpi == "GROSS_MARGIN":
        return f"""
        SELECT (SUM(revenue) / SUM(order_value)) * 100
        FROM transactions
        WHERE status='SUCCESS'
        {year_clause}
        """
    elif kpi == "SUCCESS_RATE":
        return f"""
    SELECT (SUM(status='SUCCESS') / COUNT(*)) * 100
    FROM transactions
    WHERE 1=1
    {month_clause} {year_clause}
    """

    else:
        raise ValueError("Unknown KPI")
