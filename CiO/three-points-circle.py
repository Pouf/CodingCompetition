def checkio(d):
    # get a list of coordinates
    d = [int(i) for i in d.replace('(','').replace(')','').split(',')]
    Ax, Ay = d[0:2]
    Bx, By = d[2:4]
    Cx, Cy = d[4:]
    
    # Avoid division by 0
    if Bx in [Ax, Cx]: Bx, Cx, By, Cy = Cx, Bx, Cy, By
    
    # Slope
    Ma = (By-Ay) / (Bx-Ax)
    Mb = (Cy-By) / (Cx-Bx)
    
    # Center coordinates
    Px = (Ma * Mb * (Ay-Cy) + Mb*(Ax+Bx) - Ma*(Bx+Cx)) / (2 * (Mb-Ma))
    
    # Avoid division by 0
    if Ma == 0.: 
        Py = ((Bx+Cx)/2 - Px)/Mb + (By+Cy)/2;
    else:
        Py = ((Ax+Bx)/2 - Px)/Ma + (Ay+By)/2
    
    radius = ((Px-Ax)**2 + (Py-Ay)**2)**.5
    
    C = [Px, Py, radius]
    for n in range(len(C)):
        C[n] = round(C[n], 2)
        if C[n] == int(C[n]):
            C[n] = int(C[n])
    
    return '(x-{})^2+(y-{})^2={}^2'.format(C[0], C[1], C[2])  
