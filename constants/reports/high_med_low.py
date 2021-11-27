from constants.prompt_selections import HML


class HML(object):
    # Prompt Selections
    PROD = HML.PROD.value
    CG_PROD = HML.CG_PROD.value
    CAT = HML.CAT.value
    CG_CAT = HML.CG_CAT.value
    CHAN = HML.CHAN.value
    PROD_LEVEL = HML.PROD_LEVEL.value.upper()
    STORE_LEVEL = HML.STORE_LEVEL.value.upper()
    # Summary Tab Card Titles
    CARD_TITLES = ['High ' + CHAN + ' ' + PROD + ' ' + CAT + ' Purchaser',
                   'Medium ' + CHAN + ' ' + PROD + ' ' + CAT + ' Purchaser',
                   'Low ' + CHAN + ' ' + PROD + ' ' + CAT + ' Purchaser']
    CARD_TITLES_CG = ['High ' + CHAN + ' ' + CG_PROD + ' ' + CG_CAT + ' Purchaser',
                      'Medium ' + CHAN + ' ' + CG_PROD + ' ' + CG_CAT + ' Purchaser',
                      'Low ' + CHAN + ' ' + CG_PROD + ' ' + CG_CAT + ' Purchaser']
    # Demographics Tab
    MET_DROP = ['Households', 'Spend', 'Trips']
    DEMO_HEAD = [[None, '% OF {} - BENCHMARK ALL SHOPPERS', '% OF {} - HIGH',
                  '% OF {} - MEDIUM', '% OF {} - LOW', 'RAW BUYER COUNT'],
                 [None, 'HIGH SHOPPERS, INDEX TO BENCHMARK - ALL SHOPPERS',
                  'MEDIUM SHOPPERS, INDEX TO BENCHMARK - ALL SHOPPERS',
                  'LOW SHOPPERS, INDEX TO BENCHMARK - ALL SHOPPERS', 'RAW BUYER COUNT']]
    # Top Products Tab
    PROD_DROP = ['Households', 'Spend', 'Trips', 'Share of Requirements']
    SHARE_CAT = 'Share of Category Requirements'
    SHARE_CAT_U = SHARE_CAT.upper()
    TOP_LEG = [['% Of {} - Benchmark All Shoppers', '% Of {} - High', '% Of {} - Medium', '% Of {} - Low'],
               [SHARE_CAT + ' - Benchmark All Shoppers', SHARE_CAT + ' - High',
                SHARE_CAT + ' - Medium', SHARE_CAT + ' - Low']]
    PROD_HEAD = [[PROD_LEVEL, '% OF {} - BENCHMARK ALL SHOPPERS', '% OF {} - HIGH',
                  '% OF {} - MEDIUM', '% OF {} - LOW', 'RAW BUYER COUNT'],
                 [PROD_LEVEL, 'HIGH SHOPPERS, INDEX TO BENCHMARK - ALL SHOPPERS',
                  'MEDIUM SHOPPERS, INDEX TO BENCHMARK - ALL SHOPPERS',
                  'LOW SHOPPERS, INDEX TO BENCHMARK - ALL SHOPPERS', 'RAW BUYER COUNT']]
    PROD_SHARE_HEAD = [[PROD_LEVEL, SHARE_CAT_U + ' - BENCHMARK ALL SHOPPERS', SHARE_CAT_U + ' - HIGH',
                        SHARE_CAT_U + ' - MEDIUM', SHARE_CAT_U + ' - LOW', 'RAW BUYER COUNT'],
                       [PROD_LEVEL, 'HIGH SHOPPERS, INDEX TO BENCHMARK - ALL SHOPPERS',
                        'MEDIUM SHOPPERS, INDEX TO BENCHMARK - ALL SHOPPERS',
                        'LOW SHOPPERS, INDEX TO BENCHMARK - ALL SHOPPERS', 'RAW BUYER COUNT']]
    # Top Stores Tab
    STORE_HEAD = [[STORE_LEVEL, '% OF {} - BENCHMARK ALL SHOPPERS', '% OF {} - HIGH',
                   '% OF {} - MEDIUM', '% OF {} - LOW', 'RAW BUYER COUNT'],
                  ['HIGH SHOPPERS, INDEX TO BENCHMARK - ALL SHOPPERS',
                   'MEDIUM SHOPPERS, INDEX TO BENCHMARK - ALL SHOPPERS',
                   'LOW SHOPPERS, INDEX TO BENCHMARK - ALL SHOPPERS', 'RAW BUYER COUNT']]
