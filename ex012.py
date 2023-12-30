medida = float(input('Digite uma medida em metros:'))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A médida {} métros possui {},KM\n{},HM\n{},DAM\n{},DM\n{},CM\n{},MM'.format(medida, km, hm, dam, dm, cm, mm))