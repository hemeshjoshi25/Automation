from constants.prompt_selections import CR


class CR(object):
    # Prompt Selection
    STAT = CR.STAT.value
    # Main Tab Dropdowns
    PROJ_DROP = [STAT]
    MET_DROP = ['Demographically Weighted', 'Trend Adjusted', 'Raw (Not Weighted)']
    # Main Tab Header
    CR_HEAD = ['BRAND', 'PARENT BRAND', 'MAJOR CATEGORY', 'CATEGORY', 'SUBCATEGORY', 'HH COUNT ({})', 'TRIP COUNT ({})']
    CR_FORM = ['DEMOGRAPHICALLY WEIGHTED', 'TREND ADJUSTED', 'NOT WEIGHTED']
