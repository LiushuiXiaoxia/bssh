import os

import logic
import page

if __name__ == '__main__':
    os.environ['QT_MAC_WANTS_LAYER'] = '1'
    logic.setup()
    page.start_ui()
