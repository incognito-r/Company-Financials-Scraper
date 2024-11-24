# Import dependencies
import pandas as pd
from src.financial_tool import get_financials

# Company name
company = 'RelianceIndustries'

# Url Dictionary
links = {
    'Balance Sheet': 'https://www.moneycontrol.com/financials/sbi/balance-sheetVI/RI#RI',
    'Profit Loss': 'https://www.moneycontrol.com/financials/sbi/profit-lossVI/RI#RI',
    'Quarterly Results': 'https://www.moneycontrol.com/financials/sbi/results/quarterly-results/RI#RI',
    'Half Yearly Results': 'https://www.moneycontrol.com/financials/sbi/results/half-yearly/RI#RI',
    'Nine Months Results': 'https://www.moneycontrol.com/financials/sbi/results/nine-months/RI#RI',
    'Yearly Results': 'https://www.moneycontrol.com/financials/sbi/results/yearly/RI#RI',
    'Cash Flow': 'https://www.moneycontrol.com/financials/sbi/cash-flowVI/RI#RI',
    'Ratios': 'https://www.moneycontrol.com/financials/sbi/ratiosVI/RI#RI',
}

get_financials(links, company)