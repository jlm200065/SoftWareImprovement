#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2021 2021/4/2 13:48
@Author  : jiangliming
@File    : test.py
"""
from selenium import webdriver  # (1)

browser = webdriver.Chrome() # (2)

# Edith has heard about a cool new online to-do app. She goes
# to check out its homepage
browser.get('http://localhost:8000')  # (3)

# She notices the page title and header mention to-do lists
assert 'Django' in browser.title  # (4)

# She is invited to enter a to-do item staright away

# She types "Buy peacock feathers" into a text box (Edith's hobby
# is tying fly-fishing lures)

# when she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list

# There is still a text box inviting her to add another item. She
# enters "Use peacock feathers to make a fly" (Edith is very methodical)

# The page updates again, and now shows both item on her list

# Edith wonder whether the site will remember her list. Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.

# She visits that URL - her to-do list is still there.
# Satisfied, she goes back to sleep

#browser.quit()
