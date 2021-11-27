from constants.prompt_selections import PS


class PS(object):
    # Prompt Selections
    PROD_LEV = PS.PROD_LEV.value.upper()
    # People Scorecard Dropdown
    PS_DROP = ['Spend per Trip', 'Share of Category Req. (Units)', 'Projected Households',
               '% of Trips', 'Buyer Count']
    PS_HEAD = ['CATEGORIES', 'WEIGHTED AVG ACROSS ' + PROD_LEV]
