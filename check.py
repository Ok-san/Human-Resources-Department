class Check ():
    # Проверка правильности ввода

    def checkInput(self, base_line_edit):
        for line_edit in base_line_edit:
            if len(line_edit.text()) == 0:
                return 0
            else:
                return 1
