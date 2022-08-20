def DecimaltoDMS(Decimal):
    d = int(Decimal)
    m = int((Decimal - d) * 60)
    var = 'E' if d >= 0 else 'W'
    return f'{abs(d)}^{abs(m)}{var}'


