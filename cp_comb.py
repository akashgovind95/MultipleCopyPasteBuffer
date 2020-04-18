class cp_comb:
    copy_combinations = [["Key.ctrl_l", 'u\'c\'', 'u\'1\''], ["Key.ctrl_l", 'u\'C\'', 'u\'1\''],
                         ["Key.ctrl_l", 'u\'c\'', 'u\'2\''], ["Key.ctrl_l", 'u\'C\'', 'u\'2\''],
                         ["Key.ctrl_l", 'u\'c\'', 'u\'3\''], ["Key.ctrl_l", 'u\'C\'', 'u\'3\''],
                         ["Key.ctrl_l", 'u\'c\'', 'u\'4\''], ["Key.ctrl_l", 'u\'C\'', 'u\'4\''],
                         ["Key.ctrl_l", 'u\'c\'', 'u\'5\''], ["Key.ctrl_l", 'u\'C\'', 'u\'5\''],
                         ["Key.ctrl_l", 'u\'c\'', 'u\'6\''], ["Key.ctrl_l", 'u\'C\'', 'u\'6\''],
                         ["Key.ctrl_l", 'u\'c\'', 'u\'7\''], ["Key.ctrl_l", 'u\'C\'', 'u\'7\''],
                         ["Key.ctrl_l", 'u\'c\'', 'u\'8\''], ["Key.ctrl_l", 'u\'C\'', 'u\'8\''],
                         ["Key.ctrl_l", 'u\'c\'', 'u\'9\''], ["Key.ctrl_l", 'u\'C\'', 'u\'9\'']]

    paste_combinations = [["Key.ctrl_l", 'u\'1\''],
                          ["Key.ctrl_l", 'u\'2\''],
                          ["Key.ctrl_l", 'u\'3\''],
                          ["Key.ctrl_l", 'u\'4\''],
                          ["Key.ctrl_l", 'u\'5\''],
                          ["Key.ctrl_l", 'u\'6\''],
                          ["Key.ctrl_l", 'u\'7\''],
                          ["Key.ctrl_l", 'u\'8\''],
                          ["Key.ctrl_l", 'u\'9\'']]

    def get_copy_combinations(self):
        return self.copy_combinations

    def get_paste_combinations(self):
        return self.paste_combinations