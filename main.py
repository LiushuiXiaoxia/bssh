from encodings import idna

import logic
import page

if __name__ == '__main__':
    print(f'idna = {idna}')

    logic.setup()
    page.start_ui()
