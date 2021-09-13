from sqlalchemy import select
from sqlalchemy.sql import func

from database.database import engine
from model.country import Country

if __name__ == '__main__':
    conn = engine.connect()
    c = [
        Country.region,
        func.sum(Country.population),
        func.max(Country.population),
        func.min(Country.population),

    ]
    s = select(c).group_by(Country.region)
    rs = conn.execute(s)
    print('*' * 80)
    print(f'Region_name|Total_population|Popul_of_larg_country|Popul_of_small_country')
    for row in rs:
        print(*row, sep=' ' * 5 + '|' + ' ' * 5)
    print('*' * 80)
