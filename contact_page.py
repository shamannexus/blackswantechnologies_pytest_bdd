class ContactPage:

    def __init__(self):
        pass

    @staticmethod
    def click_submit_button(driver):
        a = '//*[@id="contact-form"]/div[5]/button'
        form = driver.find_element_by_xpath(a)
        form.submit()

    @staticmethod
    def fill_contact_form(driver, field_name, data):
        form = driver.find_element_by_xpath('//*[@id="form-{}"]'.format(field_name))
        form.send_keys(data)

