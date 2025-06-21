from address2 import Address
from mailing import Mailing


to_address = Address("4455", "Краснодар", "Красная", "4", 880)
from_address = Address("5544", "Сочи", "Набережная", "5", 880)
mailing = Mailing(to_address, from_address, 88, "3748")

print(mailing)
