from pageobjects.prompts.prompt import GenericPromptPage
from pageobjects.modules.groups import GroupsPage
from constants.enums import PromptElements


class SelectPromptPage(GenericPromptPage):

    def __init__(self, driver):
        super(SelectPromptPage, self).__init__(driver)
        self.groups = GroupsPage(self.driver)

    def basic_input(self, prompt, input, idx=None):
        self.get_prompt(prompt, idx).click()
        if input is None:
            self.validate_prompt(prompt, idx)
        else:
            self.get_input(input).click()
            self.validate_prompt(input)

    def folder_input(self, prompt, input, folder, idx=None):
        self.get_prompt(prompt, idx).click()
        if None in [input, folder]:
            self.validate_prompt(prompt, idx)
        else:
            self.get_folder(folder).click()
            self.get_input(input).click()
            self.validate_prompt(input)

    def search_input(self, prompt, input, idx=None):
        self.get_prompt(prompt, idx).click()
        if input is None:
            self.validate_prompt(prompt, idx)
        else:
            self.search_field.send_keys(input)
            self.get_input(input).click()
            self.validate_prompt(input)

    def search_hierarchy(self, prompt, input, level, idx=None):
        self.get_prompt(prompt, idx).click()
        if None in [input, level]:
            self.validate_prompt(prompt, idx)
        else:
            self.search_field.send_keys(input)
            self.get_hierarchy_search_results(level, input).click()
            self.validate_prompt(input)

    def search_hierarchy_select(self, prompt, input, level, select, idx=None):
        self.get_prompt(prompt, idx).click()
        if None in [input, level, select]:
            self.validate_prompt(prompt, idx)
        else:
            self.search_field.send_keys(input)
            self.get_hierarchy_search_results(level, select + ' > ' + input).click()
            self.validate_prompt(input)

    def product_levels(self, prompt, levels):
        self.get_prompt(prompt).click()
        if levels[0] is None:
            self.validate_prompt(prompt)
            return
        for lev, level in enumerate(levels):
            if level is None:
                return
            self.get_input(level).click()
            if lev == 0:
                self.validate_prompt(level)
            else:
                self.validate_prompt(levels[0] + ' or ' + str(lev) + ' more')

    def promo_dates(self, prompt, start_date, end_date):
        self.get_prompt(prompt).click()
        if None in [start_date, end_date]:
            self.validate_prompt(prompt)
        self.get_input(PromptElements.CUSTOM_TIME.value).click()
        self.custom_date_fields[0].send_keys(start_date)
        self.custom_date_fields[1].send_keys(end_date)
        self.validate_prompt(start_date + ' to ' + end_date)

    def list_inputs(self, prompt, inputs, folders, idx=None):
        count = 0
        self.get_prompt(prompt, idx).click()
        if None in [inputs, folders]:
            self.validate_prompt(prompt, idx)
            return
        for i, input in enumerate(inputs):
            if None in [input, folders[i]]:
                continue
            else:
                count += 1
                self.get_folder(folders[i]).click()
                self.get_input(input).click()
                self.breadcrumbs[0].click()
        if count == 0:
            self.validate_prompt(prompt)
        elif count == 1:
            self.validate_prompt(inputs[0])
        else:
            self.validate_prompt(inputs[0] + ' or ' + str(count - 1) + ' more')

    def ranked_inputs(self, prompt, inputs, folders):
        count = 0
        self.get_prompt(prompt).click()
        if None in [inputs, folders]:
            self.validate_prompt(prompt)
            return
        for i, input in enumerate(inputs):
            if None in [input, folders[i]]:
                continue
            else:
                count += 1
                self.get_folder(folders[i]).click()
                self.get_input(input).click()
                self.breadcrumbs[0].click()
        if count == 0:
            self.validate_prompt(prompt)
        elif count == 1:
            self.validate_prompt(inputs[0])
        else:
            prompt_str = ''
            for i, input in enumerate(inputs):
                if i == len(inputs) - 1:
                    prompt_str = prompt_str + input
                else:
                    prompt_str = prompt_str + input + ' then '
            self.validate_prompt(prompt_str)

    def new_items(self, prompt, items):
        self.get_prompt(prompt).click()
        if None in items or len(items) == 0:
            self.validate_prompt(prompt)
            return
        for i in items:
            if i is None:
                continue
            else:
                self.search_field.send_keys(i)
                self.get_input(i).click()
                self.search_field.clear()
        if len(items) == 1:
            self.validate_prompt(items[0])
        else:
            self.validate_prompt(items[0] + ' or ' + str(len(items) - 1) + ' more')

    def deselect_list(self, list):
        for l in range(len(list) - 1):
            self.search_field.send_keys(list[l + 1])
            self.get_input(list[l + 1]).click()
            self.search_field.clear()
        self.validate_prompt(list[0])

    def pg_custom_filter(self, prompt, option, operator, value, idx=None):
        self.get_prompt(prompt, idx).click()
        self.get_input(option).click()
        self.groups.filter_dropdown.click()
        self.dropdown_option(operator).click()
        self.groups.custom_filter_textbox.send_keys(value)

    def bins_input(self, prompt, bins, width, lower, upper):
        self.get_prompt(prompt).click()
        if None in [bins, width, lower, upper]:
            self.validate_prompt(prompt)
            return
        for l, li in enumerate(bins):
            self.get_input(li).click()
        for l, li in enumerate(bins):
            self.get_bin_input('width')[l].send_keys(width)
            self.get_bin_input('lower')[l].send_keys(lower)
            self.get_bin_input('upper')[l].send_keys(upper)
        self.validate_prompt(bins[0] + ' (Bin Width: ' + str(width) + ', Lower Bound: '
                             + str(lower) + ', Upper Bound: ' + str(upper) + ') and ' + str(len(bins) - 1) + ' more')

    def hml_input(self, prompt, metric, high, med, low):
        self.get_prompt(prompt).click()
        if None in [metric, high, med, low]:
            self.validate_prompt(prompt)
            return
        self.get_input(metric).click()
        self.bin_high.send_keys(high)
        self.bin_med.send_keys(med)
        self.bin_low.send_keys(low)
        self.validate_prompt(metric + ' (High: ' + str(high) + ', Medium: ' + str(med) + ', Low: ' + str(low) + ')')
