from constants.prompt_selections import DE


class DE(object):
    # Prompt Selections
    LEV_1 = DE.LEV_1.value.upper()
    LEV_2 = DE.LEV_2.value.upper()
    LEV_3 = DE.LEV_3.value.upper()
    LEV_4 = DE.LEV_4.value.upper()
    LEV_5 = DE.LEV_5.value.upper()
    LEV_6 = DE.LEV_6.value.upper()
    LEV_7 = DE.LEV_7.value.upper()
    LEV_8 = DE.LEV_8.value.upper()
    # Metric Type Dropdown
    MET_DROP = ['Household', 'Spend', 'Unit']
    # Data Explorer Headers
    DE_HEAD = [
        # Household Header
        [LEV_1, LEV_2, LEV_8, LEV_4, LEV_5, LEV_6, LEV_7, LEV_3,
         'PROJECTED HOUSEHOLDS', 'BUYER COUNT'],
        # Spend Header
        [LEV_1, LEV_2, LEV_8, LEV_4, LEV_5, LEV_6, LEV_7, LEV_3,
         'SPEND PER TRIP', 'SHARE OF WALLET', 'BUYER COUNT'],
        # Unit Header
        [LEV_1, LEV_2, LEV_8, LEV_4, LEV_5, LEV_6, LEV_7, LEV_3,
         'SHARE OF CATEGORY REQ. (UNITS)', 'BUYER COUNT']]
