import time


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_good_page_has_add_button(browser):
    browser.get(link)
    time.sleep(30)
    try:
        button = [browser.find_element_by_class_name("btn-add-to-basket")]
    except:
        button = []
    assert len(button) > 0, "Button is not found"
