from selenium import webdriver

# Launch the Flipkart URL
driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")

# Do a Product search
search_box = driver.find_element_by_name("q")
search_box.send_keys("iPhone 14 pro")
search_box_button_xpath="//button[@class='L0Z3Pu']"
driver.find_element_by_xpath(search_box_button_xpath).click()

# Select any product & Add that to the cart
product = driver.find_element_by_xpath("//div[@class='IIdQZO _1SSAGr']//a")
product.click()
add_to_cart = driver.find_element_by_xpath("//button[@class='_2KpZ6l _2U9uOA _3v1-ww']")
add_to_cart.click()

# Place Order & Login to the application
place_order = driver.find_element_by_xpath("//button[@class='_2KpZ6l _2ObVJD _3AWRsL']")
place_order.click()
login_button = driver.find_element_by_xpath("//button[@class='_2KpZ6l _2HKlqd _3AWRsL']")
login_button.click()

# Select Address & Select Payment option
address = driver.find_element_by_xpath("//div[@class='_1GEhLw']/div[1]")
address.click()
payment_option = driver.find_element_by_xpath("//div[@class='_1QrT3s']/div[1]")
