

import sys
from PyQt5.QtCore import QTimer, QObject

from jira_model import jira_model
from build_board_view import build_board_view


class BuildBoardController(QObject):
    def __init__(self):
        super().__init__()
        # Timer update build progress
        update_build_board_timer = QTimer(self)
        update_build_board_timer.timeout.connect(build_board_view.update_board)
        update_build_board_timer.start(10000)  # update every 10 seconds


if __name__ == 'build_board_controller':
    build_board_controller = BuildBoardController()
