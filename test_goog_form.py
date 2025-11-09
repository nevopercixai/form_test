import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://docs.google.com/forms/d/1q3oIKB0t-oIH7reWkYXSBTSmUwp42YLCq7_KxYNkN6M/viewform?pli=1&pli=1&edit_requested=true")
    expect(page.get_by_role("heading", name="טופס ללא כותרת")).to_be_visible()
    expect(page.get_by_text("name *התשובה שלך")).to_be_visible()
    expect(page.get_by_text("email *התשובה שלך")).to_be_visible()
    expect(page.get_by_text("phone numberהתשובה שלך")).to_be_visible()
    expect(page.get_by_text("do you want to sign upyesno")).to_be_visible()
    page.get_by_role("textbox", name="name שאלת חובה").click()
    page.get_by_role("textbox", name="name שאלת חובה").fill("ishmael levi")
    page.get_by_role("textbox", name="email שאלת חובה").click()
    page.get_by_role("textbox", name="email שאלת חובה").fill("ismael.levi@gamil.com")
    page.get_by_role("textbox", name="phone number").click()
    page.get_by_role("textbox", name="phone number").fill("0543869038")
    page.get_by_role("radio", name="yes").click()
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("תגובתך נרשמה")).to_be_visible()

