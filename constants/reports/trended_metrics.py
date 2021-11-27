from constants.prompt_selections import TM


class TM(object):
    # Prompt Selections
    LEV_1 = TM.LEV_1.value.upper()
    LEV_2 = TM.LEV_2.value.upper()
    LEV_3 = TM.LEV_3.value.upper()
    LEV_4 = TM.LEV_4.value.upper()
    LEV_5 = TM.LEV_5.value.upper()
    # Trended Metrics Dropdown
    TM_DROP = ['Spend per Trip', 'Share of Category Req. (Units)', 'Projected Households',
               '% of Trips', 'Buyer Count']
    # Trended Metrics Header
    TM_HEAD = [LEV_3 + ', ' + LEV_4 + ', ' + LEV_5 + ', ' + LEV_1 + ' & ' + LEV_2]
