from employee import get_employee
from salary import gross_salary, epf, socso, net_salary
from report import print_report


def main():
    name, employee_id, basic_salary, allowance = get_employee()

    gross = gross_salary(basic_salary, allowance)
    epf_amount = epf(gross)
    socso_amount = socso(gross)
    net = net_salary(gross, epf_amount, socso_amount)

    print_report(
        name,
        employee_id,
        gross,
        epf_amount,
        socso_amount,
        net
    )


if __name__ == "__main__":
    main()