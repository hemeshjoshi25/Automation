from constants.prompt_selections import HA


class HA(object):
    # Prompt Selections
    PL_1 = HA.PROD_LEV_1.value.upper()
    PL_2 = HA.PROD_LEV_2.value.upper()
    PL_3 = HA.PROD_LEV_3.value.upper()
    PG = HA.PG.value.upper() if HA.PG.value else 'ALL SHOPPERS'
    COMP_PG = HA.COMP_PG.value.upper() if HA.COMP_PG.value else 'ALL SHOPPERS'
    # Household Dropdowns
    HH_DROP = ['% of Households', '% of Spend', 'Spend per Trip']
    # HH Headers
    HH_HEAD = [
        # % of Households Header
        [PL_2, PL_3, PL_1, PG + ', % OF HHS',
         COMP_PG + ', % OF HHS', 'INDEX (% OF HHS)', 'RELEVANCE SCORE'],
        # % of Spend Header
        [PL_2, PL_3, PL_1, PG + ', % OF SPEND',
         COMP_PG + ', % OF SPEND', 'INDEX (% OF SPEND)', 'RELEVANCE SCORE'],
        # Spend per Trip Header
        [PL_2, PL_3, PL_1, PG + ', SPEND PER TRIP',
         COMP_PG + ', SPEND PER TRIP', 'INDEX (SPEND PER TRIP)', 'RELEVANCE SCORE']]
