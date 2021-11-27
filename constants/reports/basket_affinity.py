from constants.prompt_selections import BA


class BA(object):
    # Prompt Selections
    PROD = BA.PROD.value
    PL_1 = BA.PROD_LEV_1.value.upper()
    PL_2 = BA.PROD_LEV_2.value.upper()
    # Summary Tab Analysis Dropdown
    SUMMARY_DROP = ['Item Impact', 'Basket Impact', 'Cross-Promotion Lift']
    # Summary Tab Headers
    SUMMARY_HEAD = [
        # Item Impact Header
        [PL_1, PL_2, '% TRIPS', 'BASKET AFFINITY INDEX', 'SPEND PER TRIP TOGETHER',
         'SPEND PER TRIP COMPANION ONLY', 'DIFFERENCE IN SPEND PER TRIP', 'BUYER COUNT'],
        # Basket Impact Headers
        [PL_1, PL_2, '% TRIPS', 'BASKET AFFINITY INDEX', 'BASKET SIZE TOGETHER',
         'BASKET SIZE COMPANION ONLY', 'DIFFERENCE IN BASKET SIZE', 'BUYER COUNT'],
        # Cross-Promotion Lift Headers
        [PL_1, PL_2, '% PENETRATION', 'BASKET AFFINITY INDEX', 'TOTAL SALES IMPACT ON LEADER',
         'DIFFERENCE IN LEADER SPEND', 'TOTAL SALES IMPACT ON BASKET', 'BUYER COUNT']]
    # Retailer Preference Tab Header
    RETAIL_HEAD = ['STORE WITH THIS COMBINATION', '% COMBINED SPEND']
