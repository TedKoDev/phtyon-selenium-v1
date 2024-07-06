import time
import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import telegram
from telegram.error import BadRequest, TimedOut

# 비동기 함수 정의
async def send_telegram_message(bot, chat_id, text):
    try:
        await bot.send_message(chat_id=chat_id, text=text)  # 타임아웃 인수 제거
    except BadRequest as e:
        print(f"텔레그램 메시지 전송 오류 (BadRequest): {e}")
    except TimedOut as e:
        print(f"텔레그램 메시지 전송 시간 초과 (TimedOut): {e}")
    except Exception as e:
        print(f"텔레그램 메시지 전송 중 예기치 않은 오류: {e}")

# 텔레그램 봇 설정
bot_token = ''
chat_id = ''  # 얻은 개인 채팅 ID
bot = telegram.Bot(token=bot_token)

# 크롬 드라이버 경로 설정 및 포트 지정
driver_path = '/opt/homebrew/bin/chromedriver'
options = webdriver.ChromeOptions()
service = webdriver.chrome.service.Service(driver_path, port=9516)
driver = webdriver.Chrome(service=service, options=options)

try:
    # 웹사이트 열기
    driver.get('https://.me/login')

    # 로그인 정보 입력
    email = '@naver.com'
    password = '!'
    price = '4000'


    email_field = driver.find_element(By.ID, 'io-email-field-input-2')
    password_field = driver.find_element(By.ID, 'io-password-field-input-3')

    email_field.send_keys(email)
    password_field.send_keys(password)

    # 로그인 버튼 클릭
    login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    login_button.click()

    # 로그인 대기 (필요에 따라 조정)
    time.sleep(5)

    # 관리자 페이지로 이동
    driver.get('https://goco.imweb.me/admin/?type=page')

    # 추가 로그인 정보 입력 (요소가 로드될 때까지 대기)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'txt_email'))
    )
    additional_email_field = driver.find_element(By.ID, 'txt_email')
    additional_password_field = driver.find_element(By.ID, 'txt_pass')

    additional_email_field.send_keys(email)
    additional_password_field.send_keys(password)

    # 추가 로그인 버튼 클릭 (요소가 로드될 때까지 대기)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'btn_login_check'))
    )
    admin_login_button = driver.find_element(By.ID, 'btn_login_check')
    admin_login_button.click()

    # "다시 보지 않기" 버튼 클릭 (요소가 로드될 때까지 대기)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button._btn-close.button.button--outlined'))
        )
        close_button = driver.find_element(By.CSS_SELECTOR, 'button._btn-close.button.button--outlined')
        close_button.click()
    except:
        print("다시 보지 않기 버튼이 나타나지 않았습니다.")

    # 쇼핑 관리 페이지로 이동 (요소가 로드될 때까지 대기)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/admin/shopping"]'))
    )
    shopping_menu = driver.find_element(By.CSS_SELECTOR, 'a[href="/admin/shopping"]')
    shopping_menu.click()
    time.sleep(2)

    # 상품 관리 페이지로 이동 (요소가 로드될 때까지 대기)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/admin/shopping/product"]'))
    )
    product_menu = driver.find_element(By.CSS_SELECTOR, 'a[href="/admin/shopping/product"]')
    product_menu.click()
    time.sleep(2)

    # 상품명 검색 입력 (요소가 로드될 때까지 대기)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'keyword_search_input'))
    )
    search_input = driver.find_element(By.ID, 'keyword_search_input')
    search_input.send_keys('롯데상품권')
    search_input.send_keys(Keys.RETURN)

    # 검색 대기 (필요에 따라 조정)
    time.sleep(2)

    # 체크박스 선택 (요소가 로드될 때까지 대기)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[value="s20231217098aa8d10ff2a"]'))
    )
    checkbox = driver.find_element(By.CSS_SELECTOR, 'input[value="s20231217098aa8d10ff2a"]')

    # JavaScript를 사용하여 클릭
    driver.execute_script("arguments[0].click();", checkbox)

    # 판매가 변경 버튼 클릭 (요소가 로드될 때까지 대기)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a[onclick="SHOP_PROD_LIST.openModifyProdPriceMulti();"]'))
    )
    modify_price_button = driver.find_element(By.CSS_SELECTOR, 'a[onclick="SHOP_PROD_LIST.openModifyProdPriceMulti();"]')
    modify_price_button.click()

    # 직접입력 라디오 버튼 선택 (요소가 로드될 때까지 대기)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="type"][value="fix"]'))
    )
    direct_input_radio = driver.find_element(By.CSS_SELECTOR, 'input[name="type"][value="fix"]')

    # JavaScript를 사용하여 클릭
    driver.execute_script("arguments[0].click();", direct_input_radio)

    # 가격 입력 (요소가 로드될 때까지 대기)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'fix[price]'))
    )
    price_input = driver.find_element(By.NAME, 'fix[price]')
    price_input.clear()  # 기존 값 지우기
    price_input.send_keys(price)

    # 저장 버튼 클릭 (요소가 로드될 때까지 대기)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button[onclick="SHOP_PROD_MANAGE.saveProdPriceModify();"]'))
    )
    save_button = driver.find_element(By.CSS_SELECTOR, 'button[onclick="SHOP_PROD_MANAGE.saveProdPriceModify();"]')
    save_button.click()

    # 20초간 대기
    time.sleep(20)

    # 텔레그램으로 완료 메시지 전송 // 얼마로 바뀌었습니다. 
    asyncio.run(send_telegram_message(bot, chat_id, f"롯데상품권 가격이 {price}원으로 변경되었습니다."))
    


except Exception as e:
    asyncio.run(send_telegram_message(bot, chat_id, f"스크립트 실행 중 오류가 발생했습니다: {str(e)}"))

finally:
    # 드라이버 종료
    driver.quit()
