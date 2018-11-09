class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        """任意一个类都可以添加魔法函数，返回item位置的值"""
        return self.employee[item]

    def __len__(self):
        return len(self.employee)

    def __str__(self):
        """打印时"""
        return ",".join(self.employee)

    def __repr__(self):
        """shell中"""
        return "shell: " + ",".join(self.employee)


company = Company(["tom", "bob", "jane"])

company1 = company[:2]

print(len(company1))
for em in company1:
    print(em)
print(len(company))
print(company)
