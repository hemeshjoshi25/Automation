from constants.prompt_selections import LT


class LT(object):
    # Prompt Selections
    PG = LT.PG.value if LT.PG.value else 'All Shoppers'
    STORE = LT.STORE.value
    PROD = LT.PROD.value if LT.PROD.value else (LT.CAT.value if LT.CAT.value else '')
    CG_PROD = LT.CG_PROD.value
    CHAN = LT.CHAN.value.upper()
    # Tree Titles
    TREE_TITLES = [PG, STORE + ' Shoppers', 'Not ' + STORE + ' Shoppers', PROD + ' Buyer',
                   PROD + ' Non-Buyer', 'Closers', 'Non-Closers', 'Share of Wallet', 'Leakage']
    TREE_TITLES_CG = [PG, STORE + ' Shoppers', 'Not ' + STORE + ' Shoppers', CG_PROD + ' Buyer',
                      CG_PROD + ' Non-Buyer', 'Closers', 'Non-Closers', 'Share of Wallet', 'Leakage']
    # Tree Titles [RV]
    TREE_TITLES_RV = [PG, 'Closers', 'Non-Closers', 'Share of Wallet', 'Leakage']
    # Stores Shopped Shopper Type Dropdown
    STORE_SHOP_DROP = ['Closers', 'Non-Closers']
    # Stores Shopped Metric Dropdown
    METRIC_DROP = ['Share of Wallet', 'Share of Trips', 'Share of Units', 'Unit Price',
                   'Units per Trip', 'Purchase Frequency', 'Spend per Trip']
    # Stores Shopped Metric Dropdown [RV]
    METRIC_DROP_RV = ['Share of Wallet', 'Share of Trips', 'Share of Units',
                      'Units per Trip', 'Purchase Frequency', 'Spend per Trip']
    # Stores Shopped Static Header
    SHOPPER_STATIC_HEAD = [['RETAILER', 'SHARE OF WALLET', 'SOW POINT CHG. VS YEAR AGO', '{}'],
                           ['RETAILER', 'SHARE OF TRIPS', 'SOT POINT CHG. VS YEAR AGO', 'BUYER COUNT'],
                           ['RETAILER', 'SHARE OF UNITS', 'SOU POINT CHG. VS YEAR AGO', 'BUYER COUNT']]
    # Stores Shopped Header
    SHOPPER_HEAD = ['BUYER COUNT', None, None, 'AVERAGE ITEM UNIT PRICE', 'AVERAGE ITEM UNITS PER TRIP',
                    'PURCHASE FREQUENCY', 'AVERAGE ITEM SPEND PER TRIP']
    # Stores Shopped Header [RV]
    SHOPPER_HEAD_RV = ['BUYER COUNT', None, None, 'AVERAGE BASKET UNITS PER TRIP',
                       'PURCHASE FREQUENCY', 'AVERAGE BASKET SPEND PER TRIP']
    # Top Products Shopper Dropdowns
    PROD_SHOP_DROP = ['Closers Top Product by Store', 'Non-Closers Top Product by Store']
    # Top Products Shopper Dropdowns [RV]
    PROD_SHOP_DROP_RV = ['Closers Top Department by Store', 'Non-Closers Top Department by Store']
    # Top Products Product Level Dropdowns
    PROD_LEV_DROP = ['Brand', 'Items', 'Parent Brand']
    # Top Products Product Level Dropdowns [RV]
    PROD_LEV_DROP_RV = ['Department']
    # Top Products Headers
    PROD_HEAD = ['PRODUCT', '% OF ITEM SPEND', 'AVERAGE ITEM UNIT PRICE', '% OF TRIPS', 'BUYER COUNT']
    # Top Products Headers [RV]
    PROD_HEAD_RV = ['DEPARTMENT', '% OF ITEM SPEND', '% OF TRIPS', 'BUYER COUNT']
    # Benchmark Header
    BENCH_HEAD = ['TOP STORES IN ' + CHAN, 'CLOSURE', 'INDEX (CLOSURE)',
                  'SHARE OF WALLET', 'INDEX (SHARE OF WALLET)', 'BUYER COUNT']
