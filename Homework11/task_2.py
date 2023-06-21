# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты.
# Отправить сообщение самому себе.
# Убедиться, что сообщение появилось в реестре.
# Удалить это сообщение и убедиться, что удалили.
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from time import sleep

driver = webdriver.Chrome()
sbis_site = 'https://fix-online.sbis.ru/'

try:
    print(f'Открываем сайт {sbis_site}')
    driver.get(sbis_site)
    sleep(1)
    user_login, user_password = 'dynasty', 'dynasty123'
    print(f'Вводим логин {user_login}')
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.click()
    login.send_keys(user_login, Keys.ENTER)
    assert login.get_attribute('value') == user_login
    sleep(1)
    print(f'Вводим пароль {user_password}')
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password, Keys.ENTER)
    sleep(3)
    print('Переходим в контакты')
    contacts_menu = driver.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"]')
    contacts_menu.click()
    sleep(1)
    contacts = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle')
    contacts.click()
    sleep(1)

    print('Жмем на плюс')
    plus = driver.find_element(By.CSS_SELECTOR, '[data-qa = "sabyPage-addButton"]')
    plus.click()
    sleep(2)
    print('Клик по Мои контакты')
    my_cont_btn = driver.find_element(By.CSS_SELECTOR, '.controls-text-label.ws-align-self-center')
    my_cont_btn.click()
    sleep(2)
    print('Выбираем из списка себя')
    driver.find_element(By.CSS_SELECTOR, "[title='Чернышова Светлана']").click()
    sleep(2)
    print('Вводим текст сообщения и отправляем')
    driver.find_element(By.CSS_SELECTOR, '[data-slate-node="element"]').send_keys('Этот мир наш',
                                                                                  Keys.CONTROL + Keys.ENTER)
    print('Проверяем, что наше сообщение есть в реестре сообщений')
    sleep(2)
    sms = driver.find_element(By.XPATH, '//p[contains(text(),"Этот мир наш")]')
    assert sms
    print('Удаляем наше сообщение')
    sleep(2)
    # driver.find_element(By.XPATH, '//p[contains(text(),"Этот мир наш")]').click()
    action_chains = ActionChains(driver)
    action_chains.move_to_element(sms)
    action_chains.perform()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, '.controls-itemActionsV__wrapper [title="Перенести в удаленные"]').click()
    sleep(1)
    print('Вводим в поиске текст нашего сообщения')
    sleep(2)
    driver.find_element(By.CSS_SELECTOR,
                        '.controls-Field.js-controls-Field.controls-InputBase__nativeField_hideCustomPlaceholder') \
        .send_keys("Этот мир наш", Keys.ENTER)
    print('Поиск сообщения "Не найдено ни одного сообщения"')
    sleep(2)
    assert driver.find_element(By.CSS_SELECTOR, '.hint-Template__text_message_m_withOffset').get_attribute(
        'textContent') == "Не найдено ни одного сообщения"

finally:
    driver.quit()
