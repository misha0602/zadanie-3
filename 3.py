from osgeo import ogr
from osgeo import osr

# Выбираем драйвер для shp файла
driver = ogr.GetDriverByName("ESRI Shapefile")
ds = driver.CreateDataSource('Piste1.shp')

# Выбор проекции WGS84
srs = osr.SpatialReference()
srs.ImportFromEPSG(4326)

def points_creator(new_layer, x, y, petrol, st, dom, post, tel):
    # create features
    feature = ogr.Feature(new_layer.GetLayerDefn())
    point = ogr.Geometry(ogr.wkbPoint)
    # add point
    point.AddPoint(y,x)
    feature.SetGeometry(point)
    # Добавление атрибутов
    feature.SetField("petrol st", petrol)
    feature.SetField("street", st)
    feature.SetField("house", dom)
    feature.SetField("post", post)
    feature.SetField("phone", tel)
    new_layer.CreateFeature(feature)
    feature.Destroy()


# Создание слоя
layer = ds.CreateLayer('Piste', srs, ogr.wkbPoint)
# Создание полей со словами
pole = ogr.FieldDefn("petrol st", ogr.OFTString)
pole.SetWidth(100)
layer.CreateField(pole)
pole = ogr.FieldDefn("street", ogr.OFTString)
pole.SetWidth(200)
layer.CreateField(pole)
# Создание полей с цифрами
layer.CreateField(ogr.FieldDefn("house", ogr.OFTInteger))
layer.CreateField(ogr.FieldDefn("post", ogr.OFTInteger))
layer.CreateField(ogr.FieldDefn("phone", ogr.OFTInteger64))

# Наносим точки
points_creator(layer, 60.051510, 30.312002, "Shell", "Hochimina ul.", 2, 194355, 89118116014)
points_creator(layer, 60.042809, 30.372801, "Shell", "Kultury pr.", 19, 195274, 89111304289)
points_creator(layer, 60.020070, 30.432228, "Shell", "Rustaveli ul", 42, 195273, 89117427264)
points_creator(layer, 60.073984, 30.280689, "Shell", "Vyborgskoe shosse", 369, 194362, 89119709548)
points_creator(layer, 60.051939, 30.226878, "Shell", "Parashutnaya ul", 222, 197349, 89117718407)
points_creator(layer, 60.039125, 30.243853, "Shell", "Parashutnaya ul", 75, 197371, 89819113491)
points_creator(layer, 59.994317, 30.355025, "Shell", "Novorossiyskaya ul.", 350, 194021, 89817425942)
points_creator(layer, 59.991687, 30.320201, "Shell", "Torzhkovskaya ul.", 19, 197343, 89118441799)
points_creator(layer, 59.955095, 30.283884, "Shell", "Zhdanovskaya nab", 2, 197110, 89119387954)
points_creator(layer, 59.985316, 30.327231, "Shell", "Beloostrovskaya", 8, 197342, 89818200136)

#По аналогии создаем полигоны
def poligons_creator(poligon_layer, x1, y1, x2, y2, x3, y3, x4, y4, name, value, parking_place, amount_kassa, index):
    feature = ogr.Feature(poligon_layer.GetLayerDefn())
    geom = ogr.Geometry(ogr.wkbLinearRing)
    geom.AddPoint(y1, x1)
    geom.AddPoint(y2, x2)
    geom.AddPoint(y3, x3)
    geom.AddPoint(y4, x4)
    poligon = ogr.Geometry(ogr.wkbPolygon)
    poligon.AddGeometry(geom)
    feature.SetGeometry(poligon)
    # Добавление атрибутов
    feature.SetField("name", name)
    feature.SetField("value", value)
    feature.SetField("parking",parking_place )
    feature.SetField("kassa", amount_kassa)
    feature.SetField("post index", index)
    poligon_layer.CreateFeature(feature)
    feature.Destroy()


layer = ds.CreateLayer('Shop', srs, ogr.wkbPolygon)
pole = ogr.FieldDefn("name", ogr.OFTString)
pole.SetWidth(200)
layer.CreateField(pole)
pole = ogr.FieldDefn("value", ogr.OFTString)
pole.SetWidth(200)
layer.CreateField(pole)
layer.CreateField(ogr.FieldDefn("parking", ogr.OFTInteger))
layer.CreateField(ogr.FieldDefn("kassa", ogr.OFTInteger))
layer.CreateField(ogr.FieldDefn("post index", ogr.OFTInteger))


poligons_creator(layer, 60.038637, 30.319537, 60.037745, 30.320122, 60.038006, 30.321995, 60.038831, 30.321249, 'OKEY', 'Food', 200, 36, 194356)
poligons_creator(layer, 60.103055, 30.252759, 60.102241, 30.252316, 60.101558, 30.256065, 60.102400, 30.256602, 'Maksidom', 'Building', 150, 10, 194362)
poligons_creator(layer, 60.075253, 30.273543, 60.075746, 30.272215, 60.074716, 30.270855, 60.074221, 30.272023, 'Lenta', 'Food', 150, 40, 194362)
poligons_creator(layer, 60.003134, 30.268031, 60.001712, 30.267354, 60.001505, 30.269265, 60.002809, 30.269958, "Metro", 'Food', 100, 25, 197227)
poligons_creator(layer, 59.794616, 30.328198, 59.791996, 30.327819, 59.792008, 30.334149, 59.794728, 30.333870, 'Pulkovo Village', 'Fashion', 350, 80, 196140)
poligons_creator(layer, 59.824827, 30.315107, 59.823397, 30.315128, 59.823417, 30.317436, 59.824847, 30.317428, 'OBI', 'Building', 100, 8, 186)
poligons_creator(layer, 60.095435, 30.378067, 60.092836, 30.372853, 60.088286, 30.378068, 60.090414, 30.385861, 'Mega Parnas', 'Food, building, fashion', 1000, 150,194292 )
poligons_creator(layer, 60.062754, 30.326194, 60.062238, 30.325778, 60.062019, 30.326735, 60.062556, 30.327156, "Griffin", 'Auto', 20, 2, 194358)
poligons_creator(layer, 60.030373, 30.333724, 60.030497, 30.336090, 60.029882, 30.336186, 60.029899, 30.333820, 'Marshall', 'Autozapchasti', 50, 10, 194354)
poligons_creator(layer, 60.047823, 30.313809, 60.046531, 30.314466, 60.046746, 30.315988, 60.048006, 30.315257, 'Lenta', 'food', 200, 45, 194356)



