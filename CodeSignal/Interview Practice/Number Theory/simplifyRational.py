def simplifyRational(numerator, denominator):
    if numerator == denominator:
        return [numerator/numerator,denominator/denominator]
    elif numerator == 0:
        return [0,1]
    elif denominator == 0:
        return [1,0]
    newx, newy, themin = numerator, denominator, min(abs(numerator),abs(denominator))
    while themin > 1:
        origx, origy = newx, newy
        for i in reversed(range(themin+1)):
            if (newx/i).is_integer() and (newy/i).is_integer():
                newx, newy = newx/i, newy/i
                break
        if newx == origx and newy == origy:
            if newy < 0:
                newx, newy = newx * -1, newy * -1
            return [newx,newy]
    if newy < 0:
        newx, newy = newx * -1, newy * -1
    return [newx,newy]