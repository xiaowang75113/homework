import sys
from datetime import datetime
from dateutil.relativedelta import relativedelta

class License():

    #身份证号码、姓名、类型、发证日期、有效期
    def __init__(self, id, name, type, date, expiry):
        self.id = id
        self.name = name
        self.type = type
        self.date = date
        self.expiry = expiry

    def __str__(self):
        return "这是License对象"

    def print_info(self):
        print("您的身份证号：" + self.id)
        print("您的姓名：" + self.name)
        print("您的驾驶证类型：" + self.type)
        print("您的发放日期：" + str(self.date))
        print("您的有效期：" + str(self.expiry) + "年")

class LicenseManager():

    def register(self):
        print("这里是注册页面，请依次输入您的身份证号、姓名、类型、发放日期，用逗号隔开。")
        a = sys.stdin.readline()
        c = a.split(",")
        date_start = datetime.strptime(c[3][:-1], "%Y-%m-%d").date()
        license = License(c[0], c[1], c[2], date_start, 6)
        license.print_info()
        return license

    def delete(self, license):
        print("您确认要注销吗？确认输入 1 ，取消输入 2 ")
        a = sys.stdin.readline()
        if int(a) == 1:
            print("撤销成功！")
        if int(a) == 2:
            print("不撤销！")

    def select(self, license):
        print("请输入您的身份证号为您查询：")
        a = sys.stdin.readline()
        print("您的驾驶证类型为：" + license.type)
        date_end = (license.date + relativedelta(years=license.expiry)).strftime('%Y-%m-%d')
        print("您的到期时间为：" + date_end)

    def updateType(self, license):
        print("请您输入您要修改的驾驶证类型：")
        a = sys.stdin.readline()
        license.type = a[:-1]
        print("您的驾驶证类型修改成功！")
        license.print_info()

    def updateExpiry(self, license):
        print("请输入您的年龄：")
        a = sys.stdin.readline()
        if int(a) >= 70:
            print("对不起，超过70岁不能延长驾驶证有效期")
        if int(a) < 70:
            print("请输入需要延长的年数：")
            b = sys.stdin.readline()
            license.expiry += int(b)
            print("您的驾驶证有效期修改成功！")
            license.print_info()

def alert():
    print("                 ")
    print("                 ")
    print("-----------------------")
    print("请输入您要进行的操作编号：")
    print("    1、驾驶证注册")
    print("    2、驾驶证查询")
    print("    3、修改驾驶证类型")
    print("    4、修改驾驶证有效期")
    print("    5、驾驶证撤销")
    print("    6、退出程序")

    a = sys.stdin.readline()
    num = int(a)
    return num


if __name__ == '__main__':

    licenseManager = LicenseManager()

    while 1:
        num = alert()
        if num == 1:
            license = licenseManager.register()

        elif num == 2:
            licenseManager.select(license)

        elif num == 3:
            licenseManager.updateType(license)

        elif num == 4:
            licenseManager.updateExpiry(license)

        elif num == 5:
            licenseManager.delete(license)

        else:
            print("程序退出")
            break

