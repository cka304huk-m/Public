import sqlite3
class Morse:
    """Азбука морзе."""

    def read_base(self):
        # Чтения базы
        connect = sqlite3.connect('base/symbols.db')
        cursor = connect.cursor()

        return cursor

    def convertInMorse(self, symbol):
        # Конвертация символа в морзе.
        cursor = self.read_base()
        cursor.execute("""SELECT morse_symb FROM morse
                        WHERE alf_symb == ?""",
                       (symbol))
        result = cursor.fetchone()[0]
        return result

    def convertInText(self, code):
        # Конвертация морзе в символ.
        cursor = self.read_base()
        cursor.execute("""SELECT alf_symb FROM morse
                        WHERE morse_symb == ?""",
                       (code,))
        result = cursor.fetchone()[0]
        return result