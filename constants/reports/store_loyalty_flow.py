
class SLF(object):
    # Summary Tab Buyer Segment Dropdown
    BUY_SEG_DROP = ['Exclude Non-Buyer', 'Include Non-Buyer']
    # Summary Tab Metric Dropdown
    MET_DROP = ['% of Households', '% of Spend', '% of Units', '% of Trips']
    # Summary Tab Legend
    SUM_LEG = [['Exclusive', 'Loyal', 'Occasional', 'Light'],
               ['Exclusive', 'Loyal', 'Occasional', 'Light', 'Non-Buyer']]
    # Summary Tab Header
    SUM_HEAD = ['LOYALTY TYPE', '{}, PREV-PERIOD', '{}, POST-PERIOD', 'POINT CHANGE',
                'HOUSEHOLD COUNT, PREV-PERIOD', 'HOUSEHOLD COUNT, POST-PERIOD']
    # Benchmarks Tab Metric Dropdown
    BENCH_DROP = ['% of Households', 'Share of Spend', 'Share of Units', 'Share of Trips']
    # Benchmarks Tab Legend
    BENCH_LEG = ['{}, Exclusive', 'Loyal', 'Occasional', 'Light', 'Non-Buyer']
    # Benchmarks Tab Header
    BENCH_HEAD = ['RETAILER', '{}, EXCLUSIVE', '{}, LOYAL', '{}, OCCASIONAL',
                  '{}, LIGHT', '{}, NON-BUYER', 'HOUSEHOLD COUNT']
    # Benchmarks Tab Format
    BENCH_FORM = ['% Households', '% Spend', '% Units', '% Trips']
    # Store Preference Tab Dropdown
    STORE_DROP = ['Non-Buyer', 'Light', 'Occasional', 'Loyal', 'Exclusive']
    # Store Preference Tab Legend
    STORE_LEG = ['Share of Wallet']
    # Store Preference Header
    STORE_HEAD = ['RETAILER', 'SHARE OF WALLET', 'FAIR SHARE', 'INDEX VS. FAIR SHARE.', 'HOUSEHOLD COUNT']
