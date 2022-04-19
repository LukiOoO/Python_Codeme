def get_salary_net_under_26(salary_gross):
    """returns salary netto annually"""
    if salary_gross < 85000:  # PIT 0%
        return salary_gross
    else:  # wejście w próg podatkowy
        return 85000 + (salary_gross - 85000) * 0.83