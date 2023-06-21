# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
sbis_site = 'https://sbis.ru/'
sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'
tensor_site = 'https://tensor.ru/'
tensor_title = 'Тензор — IT-компания'

try:
    # Перейти на https://sbis.ru/
    driver.get(sbis_site)
    sleep(1)

    # Проверить адрес сайта и заголовок страницы
    assert driver.current_url == sbis_site, 'Неверный адрес сайта'
    assert driver.title == sbis_title, 'Неверный заголовок сайта'

    # Проверить отображение четырех вкладок
    tabs = driver.find_elements(By.CSS_SELECTOR, '.sbisru-Header__menu-item')
    assert len(tabs) == 4

    # Перейти в раздел "Контакты"
    contacts_btn = driver.find_element(By.CSS_SELECTOR, '[href ="/contacts"]')
    assert contacts_btn.text == 'Контакты'
    assert contacts_btn.is_displayed(), 'Элемент не отображается'
    contacts_btn.click()
    sleep(1)

    # Найти баннер Тензор, кликнуть по нему
    logo = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__logo-link')
    logo.click()

    # Перейти на https://tensor.ru/
    driver.get(tensor_site)
    sleep(1)

    # Проверить адрес сайта и заголовок страницы
    assert driver.current_url == tensor_site, 'Неверный адрес сайта'
    assert driver.title == tensor_title, 'Неверный заголовок сайта'

    # Проверить, что есть блок новости "Сила в людях"
    block4 = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content')
    assert block4.is_displayed(), 'Блок новости "Сила в людях" не отображается'
    sleep(1)

    # Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
    info_btn = driver.find_element(By.CSS_SELECTOR, '[href="/about"].tensor_ru-link.tensor_ru-Index__link')
    into_btn = info_btn.location_once_scrolled_into_view
    info_btn.click()
    assert driver.current_url == 'https://tensor.ru/about', 'Неверный адрес сайта'
finally:
    driver.quit()
