import dearpygui.dearpygui as dpg


def init_dearpygui():
    dpg.create_context()


def set_default_font(font_file:str="NotoSansJP-Regular.otf", size:int = 20):
    with dpg.font_registry():
        with dpg.font(font_file, size) as font1:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Japanese)
            dpg.add_font_range(0x3100, 0x3ff0)
            dpg.add_font_chars([0x3105, 0x3107, 0x3108])
            dpg.add_char_remap(0x3084, 0x0025)
            dpg.bind_font(font1)

init_dearpygui()
set_default_font()

# # add a font registry
# with dpg.font_registry():
#     # first argument ids the path to the .ttf or .otf file
#     with dpg.font("NotoSansJP-Regular.otf", 20, label="NotoSans") as font1:
#         # add the default font range
#         dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)

#         # helper to add range of characters
#         #    Options:
#         #        mvFontRangeHint_Japanese
#         #        mvFontRangeHint_Korean
#         #        mvFontRangeHint_Chinese_Full
#         #        mvFontRangeHint_Chinese_Simplified_Common
#         #        mvFontRangeHint_Cyrillic
#         #        mvFontRangeHint_Thai
#         #        mvFontRangeHint_Vietnamese
#         dpg.add_font_range_hint(dpg.mvFontRangeHint_Japanese)

#         # add specific range of glyphs
#         dpg.add_font_range(0x3100, 0x3ff0)

#         # add specific glyphs
#         dpg.add_font_chars([0x3105, 0x3107, 0x3108])

#         # remap や to %
#         dpg.add_char_remap(0x3084, 0x0025)
#         # default_font = dpg.add_font("NotoSansJP-Regular.otf", 20)
#         # second_font = dpg.add_font("NotoSansJP-Regular.otf", 10)

#         dpg.bind_font(font1)

with dpg.window(label="Font Example", height=200, width=200):
    dpg.add_button(label="日本語")
    b2 = dpg.add_button(label="Secondary font")
    dpg.add_button(label="default")

    # set font of specific widget
    # dpg.bind_font(default_font)
    # dpg.bind_item_font(b2, second_font)

# dpg.show_font_manager()

def show(title:str="No Title", viewport_width:int = 800, viewport_height:int = 600):
    dpg.create_viewport(title=title, width=viewport_width, height=viewport_height)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()

def destory():
    dpg.destroy_context()

show()
destory()

# def save_callback():
#     print("Save Clicked")


# with dpg.font_registry():
#     # first argument ids the path to the .ttf or .otf file
#     default_font = dpg.add_font("NotoSansJP-Regular.otf", 20)
#     second_font = dpg.add_font("NotoSansJP-Regular.otf", 10)

# dpg.create_context()
# dpg.create_viewport()
# dpg.setup_dearpygui()

# with dpg.window(label="Example Window"):
#     dpg.add_text("日本語")
#     dpg.add_button(label="Save", callback=save_callback)
#     dpg.add_input_text(label="string")
#     dpg.add_slider_float(label="float")

# dpg.show_viewport()
# dpg.start_dearpygui()
# dpg.destroy_context()
