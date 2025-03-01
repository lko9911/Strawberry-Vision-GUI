# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from gui.uis.windows.main_window.functions_main_window import *
import sys
import os
import cv2
import time
import threading

from gui.uis.windows.main_window.yolo_detection.webcam import *
from gui.uis.windows.main_window.yolo_detection.utils import *
from gui.uis.windows.main_window.yolo_detection.classify_disease import *

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from gui.uis.windows.main_window.ui_main import *

# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////
from gui.uis.windows.main_window.functions_main_window import *


# PY WINDOW
# ///////////////////////////////////////////////////////////////
class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # ADD LEFT MENUS
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon" : "icon_home.svg",
            "btn_id" : "btn_home",
            "btn_text" : "Home",
            "btn_tooltip" : "Home page",
            "show_top" : True,
            "is_active" : True
        },
        {
            "btn_icon" : "icon_send.svg",
            "btn_id" : "btn_page_2",
            "btn_text" : "Scan (Strawberry-Vision)",
            "btn_tooltip" : "Scan (Strawberry-Vision)",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_widgets.svg",
            "btn_id" : "btn_settings",
            "btn_text" : "Start Program",
            "btn_tooltip" : "Start Program",
            "show_top" : False,
            "is_active" : False
        }

    ]

    # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    
    add_title_bar_menus = [
        {
            "btn_icon" : "icon_info.svg",
            "btn_id" : "btn_top_settings",
            "btn_tooltip" : "Top settings",
            "is_active" : False
        }
    ]
    
    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])
        
        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # ADD Title
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to PyOneDark")

        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.page_1)
        MainFunctions.set_left_column_menu(
            self,
            menu = self.ui.left_column.menus.menu_1,
            title = "Settings Left Column",
            icon_path = Functions.set_svg_icon("icon_widgets.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # ///////////////////////////////////////////////////////////////
        # EXAMPLE CUSTOM WIDGETS
        # Here are added the custom widgets to pages and columns that
        # were created using Qt Designer.
        # This is just an example and should be deleted when creating
        # your application.
        #
        # OBJECTS FOR LOAD PAGES, LEFT AND RIGHT COLUMNS
        # You can access objects inside Qt Designer projects using
        # the objects below:
        #
        # <OBJECTS>
        # LEFT COLUMN: self.ui.left_column.menus
        # RIGHT COLUMN: self.ui.right_column
        # LOAD PAGES: self.ui.load_pages
        # </OBJECTS>
        # ///////////////////////////////////////////////////////////////

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # ADD CUSTOM BUTTON
        self.btn_1 = PyPushButton(
            text = "Manual",
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["dark_four"]
        )
        self.btn_1.setMinimumHeight(40)

        yolo_path = "gui/uis/windows/main_window/model/best4.pt"
        npz_path = "gui/uis/windows/main_window/stereo_calibration_result.npz"

        def webcam():
            detect_and_save(model_path=yolo_path, npz_path=npz_path ,save_path="detected_objects.json", time_interval=20)
        
        self.btn_1.clicked.connect(webcam)

        # ADD TO LAYOUT
        self.ui.left_column.menus.btn_1_layout_.addWidget(self.btn_1)

        self.btn_2 = PyPushButton(
            text="Update Result",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["bg_one"],
            bg_color_hover=self.themes["app_color"]["bg_two"],
            bg_color_pressed=self.themes["app_color"]["dark_three"]
        )
        self.btn_2.setMinimumHeight(40)

        # QLabel을 미리 생성하여 유지
        self.result_image = QLabel()
        self.result_image.setAlignment(Qt.AlignCenter)  # 중앙 정렬
        self.result_image.setScaledContents(True)  # QLabel 크기에 맞게 조정
        # self.image.setFixedSize(200, 198)  # 크기 설정
        self.ui.load_pages.result.addWidget(self.result_image, alignment=Qt.AlignTop | Qt.AlignHCenter)

        def update():
            # QPixmap으로 이미지 로드
            pixmap = QPixmap("gui/uis/windows/main_window/saved_frames/YOLO Depth Left.jpg") 

            # QLabel에 새로운 이미지 적용
            self.result_image.setPixmap(pixmap)
            detected_objects = load_detected_objects("detected_objects.json")
            message = print_detected_objects(detected_objects)
            self.info_label.setText(message)  # QLabel 업데이트
            
        self.btn_2.clicked.connect(update)

        # QLabel 생성
        self.info_label = QLabel("🔍 업데이트 해주세요 ")  # 기본 텍스트 설정
        self.info_label.setStyleSheet("font-size: 18px; font-weight: bold;")

        #self.info_label.setAlignment(Qt.AlignCenter)  # 중앙 정렬
        #self.info_label.setFixedSize(300, 40)  # 크기 설정

        # GUI에 QLabel 추가
        self.ui.left_column.menus.result_text_layout.addWidget(self.info_label, alignment=Qt.AlignTop | Qt.AlignHCenter)

        # ADD TO LAYOUT
        self.ui.left_column.menus.btn_2_layout_.addWidget(self.btn_2)


        self.auto_running = False  
        self.auto_thread = None  # 현재 실행 중인 스레드 참조 변수

        # Automatic 버튼
        self.btn_3 = PyPushButton(
            text="Automatic",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.btn_3.setMinimumHeight(40)
        self.ui.left_column.menus.btn_3_layout_.addWidget(self.btn_3)

        # Stop Auto 버튼
        self.btn_4 = PyPushButton(
            text="Stop Auto",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["bg_one"],
            bg_color_hover=self.themes["app_color"]["bg_two"],
            bg_color_pressed=self.themes["app_color"]["dark_three"]
        )
        self.btn_4.setMinimumHeight(40)
        self.ui.left_column.menus.btn_4_layout_.addWidget(self.btn_4)

        self.auto_running = False  
        
        def auto():
            """ 자동 실행 함수 (스레드에서 실행됨) """
            if self.auto_running:
                return  # 이미 실행 중이면 새 스레드를 만들지 않음

            self.auto_running = True  # 실행 플래그 ON
            try:
                while self.auto_running:
                    detect_and_save2(model_path=yolo_path, npz_path=npz_path, save_path="detected_objects.json", time_interval=20)
                    update()

                    # 10초를 1초씩 나누어 실행하며 중지 체크
                    for _ in range(10): 
                        if not self.auto_running:
                            print("자동 실행 중지됨")
                            return  # 즉시 종료
                        time.sleep(1)
                        
            except Exception as e:
                print(f"자동 실행 중 오류 발생: {e}")
            finally:
                self.auto_running = False  # 예외 발생 시 플래그 초기화

        def start_auto():
            """ Auto 시작 (스레드 실행) """
            if self.auto_thread is None or not self.auto_thread.is_alive():
                self.auto_thread = threading.Thread(target=auto, daemon=True)
                self.auto_thread.start()

        def stop_auto():
            """ Auto 중지 """
            self.auto_running = False  # 실행 플래그 OFF
            print("정지 버튼 클릭됨")  # 디버깅용 출력

        self.btn_3.clicked.connect(start_auto)
        self.btn_4.clicked.connect(stop_auto)     

        # ADD TO LAYOUT
        self.ui.left_column.menus.btn_4_layout_.addWidget(self.btn_4)

        '''
        # ADD TOGGLE BUTTON
        self.toggle_1 = PyToggle(
            active_color = self.themes["app_color"]["context_color"],
            bg_color = self.themes["app_color"]["dark_one"],
            circle_color = self.themes["app_color"]["icon_color"],
            width = 50
        )
        '''
        
        # ADD TO LAYOUT
        #self.ui.left_column.menus.btn_2_layout_.addWidget(self.toggle_1, Qt.AlignCenter, Qt.AlignCenter)

        # ADD LOGO TO HOME
        #self.logo = QSvgWidget(Functions.set_svg_image("logo_home.svg"))

        '''
        # ADD DEFAULT WIDGET
        self.line_edit = QLineEdit()
        self.button = QPushButton("Send")

        def print_text():
            print(self.line_edit.text())
            self.line_edit.setText("")
        
        self.button.clicked.connect(print_text)

        self.ui.load_pages.logo_layout.addWidget(self.line_edit)
        self.ui.load_pages.logo_layout.addWidget(self.button)
        '''

        # ADD TOGGLE
        self.toggle = PyToggle(
            width = 60,
            bg_color = self.themes["app_color"]["context_color"],
            circle_color = self.themes["app_color"]["icon_color"],
            active_color = self.themes["app_color"]["context_color"]
        )

        # QLabel 생성
        self.image = QLabel()

        # QPixmap으로 이미지 로드
        pixmap = QPixmap("gui/images/svg_images/cat.png")  # 이미지 경로 확인 필수

        # 이미지 설정
        self.image.setPixmap(pixmap)
        self.image.setAlignment(Qt.AlignCenter)  # 중앙 정렬

        # 이미지가 QLabel 크기에 맞게 자동으로 크기 조정되도록 설정
        self.image.setScaledContents(True)

        # QLabel 크기 설정
        self.image.setFixedSize(200, 198)  # 원하는 크기 설정

        # 중앙 위 정렬을 위해 레이아웃에 추가
        self.ui.load_pages.logo_layout.addWidget(self.image, alignment=Qt.AlignTop | Qt.AlignHCenter)

        # 스캔 결과 표시

        # ///////////////////////////////////////////////////////////////
        # END - EXAMPLE CUSTOM WIDGETS
        # ///////////////////////////////////////////////////////////////
        
    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
            
    
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)
