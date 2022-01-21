from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='wazeyes')

latitude = float(input('Digite a latitude: '))
longitude = float(input('Digite a longitude: '))
resultado = str(geolocator.reverse(f"{latitude}, {longitude}")).split(',')

if resultado[0] != 'None':
    print('Endereço completo.', resultado)
    print('Bairro............', resultado[1])
    print('Cidade............', resultado[2])
    print('Região............', resultado[3])
