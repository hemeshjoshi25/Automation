from constants.prompt_selections import LRN


class LRN(object):
    # Prompt Selections
    PROD_LEV = LRN.PROD_LEV.value
    CG_PROD_LEV = LRN.CG_PROD_LEV.value
    # Total Composition Tab Toggle
    LRN_TOG = ['% of Households', '% of Item Spend', '% of Item Units', '% of Item Trips']
    # Total Composition Tab Toggle [RV]
    LRN_TOG_RV = ['% of Households', '% of Basket Spend', '% of Basket Units', '% of Basket Trips']
    # Total Composition Tab Legend
    LRN_LEG = ['{}, New Shoppers', '{}, Repeat Shoppers', '{}, Lapsed Shoppers']
    # Total Composition Tab Header
    TOTAL_COMP_HEAD = ['{}, NEW SHOPPERS', '{}, REPEAT SHOPPERS', '{}, LAPSED SHOPPERS', 'HOUSEHOLD COUNT']
    # Comparison Tab Header
    COMPARE_HEAD = [PROD_LEV.upper(), '{}, NEW SHOPPERS', '{}, REPEAT SHOPPERS',
                    '{}, LAPSED SHOPPERS', 'HOUSEHOLD COUNT']
    # Comparison Tab Header [RV]
    COMPARE_HEAD_RV = ['BANNER', '{}, NEW SHOPPERS', '{}, REPEAT SHOPPERS', '{}, LAPSED SHOPPERS', 'HOUSEHOLD COUNT']
    # Comparison Tab Header [CG]
    COMPARE_HEAD_CG = [CG_PROD_LEV.upper(), '{}, NEW SHOPPERS', '{}, REPEAT SHOPPERS',
                       '{}, LAPSED SHOPPERS', 'HOUSEHOLD COUNT']
    # LRN Tab Dropdown
    LRN_DROP = ['Lapsed Shoppers', 'Repeat Shoppers', 'New Shoppers']
    # LRN Tab Card Titles
    LRN_CARDS = ['{}', 'Brand Purchases at Any Store', 'Category Purchases at Channel',
                 'Any Purchases at Channel']
    # LRN Tab Card Titles [RV]
    LRN_CARDS_RV = ['{}', 'Any Purchases at Store', 'Any Purchases at Channel']
    # Store Preferences Header
    STORE_HEAD = [['RETAILER', '{}, PREV-PERIOD', 'HOUSEHOLD COUNT, PREV-PERIOD',
                   '{}, POST-PERIOD', 'HOUSEHOLD COUNT, POST-PERIOD', 'CHANGE IN % OF HHS'],
                  ['RETAILER', '{}, PREV-PERIOD', 'HOUSEHOLD COUNT, PREV-PERIOD',
                   '{}, POST-PERIOD', 'HOUSEHOLD COUNT, POST-PERIOD', 'CHANGE IN {}']]
    # Store Preferences Header [RV]
    STORE_HEAD_RV = [['BANNER', '{}, PREV-PERIOD', 'HOUSEHOLD COUNT, PREV-PERIOD',
                      '{}, POST-PERIOD', 'HOUSEHOLD COUNT, POST-PERIOD', 'CHANGE IN % OF HHS'],
                     ['BANNER', '{}, PREV-PERIOD', 'HOUSEHOLD COUNT, PREV-PERIOD',
                      '{}, POST-PERIOD', 'HOUSEHOLD COUNT, POST-PERIOD', 'CHANGE IN {}']]
    # Store Preferences Header Col
    STORE_HEAD_COL = ['CHANGE IN % OF HHS', 'CHANGE IN % OF ITEM SPEND', 'CHANGE IN % OF ITEM UNITS',
                      'CHANGE IN % OF ITEM TRIPS']
    # Store Preferences Header Col [RV]
    STORE_HEAD_COL_RV = ['CHANGE IN % OF HHS', 'CHANGE IN % OF BASKET SPEND', 'CHANGE IN % OF BASKET UNITS',
                         'CHANGE IN % OF BASKET TRIPS']
    # Product Preferences Dropdown
    PROD_DROP = ['% of Households', '% of Spend', '% of Units', '% of Trips']
    # Product Preferences Header
    PROD_HEAD = [[PROD_LEV.upper(), '{}, PREV-PERIOD', 'HOUSEHOLD COUNT, PREV-PERIOD',
                  '{}, POST-PERIOD', 'HOUSEHOLD COUNT, POST-PERIOD', 'CHANGE IN % OF HHS'],
                 [PROD_LEV.upper(), '{}, PREV-PERIOD', 'HOUSEHOLD COUNT, PREV-PERIOD',
                  '{}, POST-PERIOD', 'HOUSEHOLD COUNT, POST-PERIOD', 'CHANGE IN {}']]
    # Product Preferences Header [RV]
    PROD_HEAD_RV = [['DEPARTMENT', '{}, PREV-PERIOD', 'HOUSEHOLD COUNT, PREV-PERIOD',
                     '{}, POST-PERIOD', 'HOUSEHOLD COUNT, POST-PERIOD', 'CHANGE IN % OF HHS'],
                    ['DEPARTMENT', '{}, PREV-PERIOD', 'HOUSEHOLD COUNT, PREV-PERIOD',
                     '{}, POST-PERIOD', 'HOUSEHOLD COUNT, POST-PERIOD', 'CHANGE IN {}']]
    # Product Preferences Header [CG]
    PROD_HEAD_CG = [[CG_PROD_LEV.upper(), '{}, PREV-PERIOD', 'HOUSEHOLD COUNT, PREV-PERIOD',
                     '{}, POST-PERIOD', 'HOUSEHOLD COUNT, POST-PERIOD', 'CHANGE IN % OF HHS'],
                    [CG_PROD_LEV.upper(), '{}, PREV-PERIOD', 'HOUSEHOLD COUNT, PREV-PERIOD',
                     '{}, POST-PERIOD', 'HOUSEHOLD COUNT, POST-PERIOD', 'CHANGE IN {}']]
    # Product Preferences Header Col
    PROD_HEAD_COL = ['CHANGE IN % OF HHS', 'CHANGE IN % OF SPEND', 'CHANGE IN % OF UNITS', 'CHANGE IN % OF TRIPS']
