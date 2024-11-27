import re
from time import sleep
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, args=['--start-maximized'])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("http://jy2meswebcluster/Apriso/Start/?track=client")
    page.get_by_role("link", name="Log In to DELMIA Apriso").click()
    page.get_by_role("link", name="Standard Login Log in by").click()
    page.get_by_label("名称/批次").fill("EX07820")
    page.get_by_label("密码").fill("!QAZ2wsx")
    page.get_by_role("button", name="登录").click()
    IOCIframe = page.locator("iframe").nth(2).content_frame.locator("#mainid").content_frame.locator("#TechIOCCreate").content_frame
    IOCIframe.get_by_role("tab", name="全部设备").click()
    IOCIframe.get_by_placeholder("请选择").click()
    IOCIframe.get_by_text("江阴基地").click()
    IOCIframe.get_by_text("JYP2-CL01").click()
    IOCIframe.get_by_text("装配").click()
    IOCIframe.get_by_text("切叠一体机05").click()
    IOCIframe.get_by_role("button", name="确定").click()
    sleep(120)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)