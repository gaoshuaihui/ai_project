import random

from Day02.homework01 import count

print(f"请编号为：{random.randint(2,8)} 同学回答")



"""
    select 
            a.id, b.name, c.age, d.class, 
            max(b.score), min(b.score), avg(b.score),count(b.address)
    from a 
        join b on a.id = b.id 
        join c on a.id = c.id
        join d on c.id = d.id
        where a.id >= 1 AND b.id < 20 and c.id > 10 and d.id < 100
        group by a.id, b.name, c.age, d.class
        having max(b.score) > 90
        order by a.id desc
        limit 3;
"""