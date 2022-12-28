PI = 3.14159265359

#Calculates extraterrestial irradiance, I_0
#G_0n: normal irradiance and 0,n
#w1: hour angle for hourly endpoints (beginning)
#w2: hour angle for hourly endpoints (end)
#phi: latitude
#delta: declination at the day
def ExtrIrrad(G_0n, w1, w2, phi, delta):
    a = 12*3600/PI
    b = PI / 180
    c = b*(w2-w1)*sin(phi)*sin(delta)
    d = cos(phi)*cos(delta)*(sin(w2)-sin(w1))
    return a * G_0n * (c + d)

