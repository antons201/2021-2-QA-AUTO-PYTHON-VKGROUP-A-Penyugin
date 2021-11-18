def capability_select(file_path):
    capability = {
        "platformName": "Android",
        "platformVersion": "10.0",
        "automationName": "Appium",
        "appPackage": "ru.mail.search.electroscope",
        "appActivity": ".ui.activity.AssistantActivity",
        "app": file_path,
        "orientation": "PORTRAIT",
        "autoGrantPermissions": "true"
}
    return capability
