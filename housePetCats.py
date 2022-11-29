from housePetCatsConstr import Cats

cat1 = Cats('Семен', 'мальчик', '2 года')
cat2 = Cats('Алиса', 'девочка', '3 года')
cat3 = Cats('Жюльен', 'мальчик', '1 год')

cats = [(cat1.getName(), cat1.getGender(), cat1.getAge()),
        (cat2.getName(), cat2.getGender(), cat2.getAge()),
        (cat3.getName(), cat3.getGender(), cat3.getAge())]

print('Коты в приюте "Дом Питомца": ')

for cat in cats:
    print(",".join(cat))
