from constants.prompt_selections import CP


class CP(object):
    # Prompt Selections
    COMP_PROD = CP.COMP_PROD.value
    # Buyer Overlap Tab Legend
    BUY_LEG = ['{} (Focus)', '{} (Focus) and ' + COMP_PROD + ' (Comparison)', COMP_PROD + ' (Comparison)']
    # Buyer Overlap Tab Metric Dropdown
    BUY_MET_DROP = ['% of Households', '% of Spend', '% of Units']
    # Buyer Overlap Tab Table Header
    BUY_HEAD = ['PRODUCT', None, 'CHANGE VS. YAG', 'BUY RATE', 'SPEND PER TRIP', 'PURCHASE FREQUENCY']
    # Product Matrix Tab Metric Dropdown
    PROD_MET_DROP = ['% of Focus HHs purchasing comparison product',
                     '% of Comparison HHs purchasing focus product',
                     'Product Affinity Index',
                     '% of Households, Overlapping',
                     '% of Exclusive Households, Focus Product',
                     '% of Exclusive Households, Comparison Product',
                     '% of Combined Spend, among overlapping Households',
                     '% of Combined Units, among overlapping Households',
                     'Projected Households Overlapping',
                     'Households Overlapping']
    # Product Matrix Header
    PROD_HEAD = 'COMPARISON PRODUCT'
    # Product Matrix Table Row Content
    PROD_TABLE = [COMP_PROD]
