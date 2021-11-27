from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.moments_of_truth import MomentsOfTruthPage
from constants.enums import ReportTypes
from constants.reports.moments_of_truth import MOT


class TestMomentsOfTruth(IscE2eTestCase):
    def setUp(self):
        super(TestMomentsOfTruth, self).setUp()
        self.history = HistoryPage(self.driver)
        self.mot = MomentsOfTruthPage(self.driver)

    def test_a_nav_mot(self):
        mot = ReportTypes.MOMENTS_OF_TRUTH.value
        title = ReportTypes.PREFIX.value + mot
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.mot.title.text, mot + ': ' + title)

    def test_b_summary_tab(self):
        self.mot.summary_tab()
        self.mot.card_titles_validate(MOT.CARD_TITLES)

    def test_c_comp_mot_tab(self):
        self.mot.comp_mot_tab()
        self.mot.dropdown_validate(MOT.MOT_DROP[0])
        for d in range(4):
            self.mot.select_dropdown(d, MOT.MOT_DROP[d])
            self.mot.legend_validate(MOT.MOT_LEG)
            self.mot.headers_validate(MOT.MOT_HEAD)
            self.mot.copy_table_validate()
            for c in range(3):
                self.mot.test_sort(c)
            self.mot.scroll_top()

    def test_d_ex_survey_tab(self):
        self.mot.ex_survey_tab()
        self.mot.dropdown_validate(MOT.SURVEY_DROP[0])
        for d in range(16):
            self.mot.select_dropdown(d, MOT.SURVEY_DROP[d])
            self.mot.legend_validate(MOT.SURVEY_LEG)
            self.mot.headers_validate(MOT.EX_HEAD)
            self.mot.copy_table_validate()
            if d == 1:
                for c in range(2, 3):
                    self.mot.test_sort(c)
                self.mot.scroll_top()
            else:
                for c in range(3):
                    self.mot.test_sort(c)
                self.mot.scroll_top()

    def test_e_comp_survey_tab(self):
        self.mot.comp_survey_tab()
        self.mot.dropdown_validate(MOT.SURVEY_DROP[0])
        for d in range(16):
            self.mot.select_dropdown(d, MOT.SURVEY_DROP[d])
            self.mot.legend_validate(MOT.SURVEY_LEG)
            self.mot.headers_validate(MOT.COMP_HEAD)
            self.mot.copy_table_validate()
            for c in range(3):
                self.mot.test_sort(c)
            self.mot.scroll_top()

    def test_f_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
