import astropy.io.fits as pyfits

file = pyfits.open('~/Desktop/v523cas60s-001.fit')
data = file[0].data

centre = input('Введите координаты центра звезды (сначала х, а затем у через запятую): ')
l1 = centre.split(',')
x0 = int(l1[0])
y0 = int(l1[1])
radius_star = int(input('Введите радиус звезды: '))
radius_ring = int(input('Введите радиус кольца: '))
time = 60
file.close()

h = 0
k = 0
energy = 0
energy_ring = 0
for i in range(x0 - radius_ring, x0 + radius_ring):
    for j in range(y0 - radius_ring, y0 + radius_ring):
        equation = (i - x0) ** 2 + (j - y0) ** 2
        if equation <= radius_star ** 2:
            energy += data[j][i]
            h += 1  # pixels in star
        if equation > radius_star ** 2 and equation <= radius_ring ** 2:
            energy_ring += data[j][i]
            k += 1  # pixels in ring

m = energy / time
E = energy_ring / (time * k)  # E average
N = E * h  # N
I = m - N
print(f'I = {I}')