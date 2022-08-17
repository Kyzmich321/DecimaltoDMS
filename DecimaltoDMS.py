def DecimaltoDMS(Decimal):
   d = int(Decimal)
   m = int((Decimal - d) * 60)
   if d >= 0:
      return f'{abs(d)}^{abs(m)}E'
   else:
      return f'{abs(d)}^{abs(m)}W'


