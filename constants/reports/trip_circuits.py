from constants.prompt_selections import TC


class TC(object):
    # Prompt Selections
    CAT_LEV = TC.CAT_LEV.value.upper()
    RV_CAT_LEV = 'SECTOR'
    CG_CAT_LEV = TC.CG_CAT_LEV.value.upper()
    STORE_LEV = TC.STORE_LEV.value.upper()
    RV_STORE_LEV = TC.RV_STORE_LEV.value.upper()
    # Summary Tab Card Titles
    TC_CARDS = ['Closed Circuits', 'Leaked Circuits']
    # Trip Circuits Metric Dropdown
    MET_DROP = ['% of Trip Circuits', '% of Trips', '% of Spend', 'Avg. Basket Spend at Focus Store',
                'Avg. Basket Spend at Competitive Store']
    # Closed Circuits Tab Dropdown
    STOP_DROP = ['Multiple Stops', 'One Stop']
    # Trip Circuits Legend
    TC_LEG = ['{}, Before', '{}, After']
    # Store Header
    STORE_HEAD = [STORE_LEV, '{}, BEFORE', '{}, AFTER', '{}, TOTAL', 'TRIP COUNT']
    # Store Header [RV]
    STORE_HEAD_RV = [RV_STORE_LEV, '{}, BEFORE', '{}, AFTER', '{}, TOTAL', 'TRIP COUNT']
    # Product Header
    PROD_HEAD = [CAT_LEV, 'DEPARTMENT', '{}, BEFORE', '{}, AFTER', '{}, TOTAL', 'TRIP COUNT']
    # Product Header [RV]
    PROD_HEAD_RV = [RV_CAT_LEV, 'DEPARTMENT', '{}, BEFORE', '{}, AFTER', '{}, TOTAL', 'TRIP COUNT']
    # Product Header [CG]
    PROD_HEAD_CG = [CG_CAT_LEV, 'DEPARTMENT', '{}, BEFORE', '{}, AFTER', '{}, TOTAL', 'TRIP COUNT']
    # Leaked Circuits, Store Tab Dropdown
    PROD_DROP = ['All Products', 'Focus Product Only']
    # Common Circuits Tab Dropdown
    COMMON_DROP = ['Closed', 'Leaked']
    # Common Circuits Tab Header
    COMMON_HEAD = ['COMMON TRIP CIRCUIT', '% OF TRIP CIRCUITS', 'TRIP CIRCUIT COUNT']
