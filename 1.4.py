def rel_error_add(x, dx, y, dy):
    z = x + y
    Dz = dx + dy
    return Dz / abs(z)

def rel_error_sub(x, dx, y, dy):
    z = x - y
    Dz = dx + dy
    return Dz / abs(z)

def rel_error_mul(x, dx, y, dy):
    return dx / abs(x) + dy / abs(y)

def rel_error_div(x, dx, y, dy):
    return dx / abs(x) + dy / abs(y)