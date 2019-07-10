from budgeting.track_budget.model import get_trans_via_panda

class Model:
    def __init__(self):
        self.loader = get_trans_via_panda.Load_Transactions_via_Pandas()

    def get_budget_info(self):
        return self.loader.budget_info

    def get_accumulated_spending_by_category_by_month(self):
        return self.loader.accumulated_spending_by_category_by_month

    def get_transactions(self):
        return self.loader.transactions

    def get_accumulated_spending_by_category(self):
        return self.loader.accumulated_spending_by_category

    def get_accumulated_spending_by_super_category(self):
        return self.loader.accumulated_spending_by_super_category

    def get_accumulated_spending_for_past_year(self):
        return self.loader.accumulated_spending_for_past_year

