from decimal import Decimal

from django.test import TestCase
from .models import PrecioServicio, Servicio


class ServiciosViewsTests(TestCase):
    def setUp(self):
        self.servicio_con_precio = Servicio.objects.create(
            nombre="Diseño Web",
            descripcion="Creamos sitios web modernos y adaptables.",
            disponibilidad="Inmediata",
        )
        Servicio.objects.create(
            nombre="Desarrollo Django",
            descripcion="Desarrollamos aplicaciones web utilizando Django.",
            disponibilidad="Inmediata",
        )
        PrecioServicio.objects.create(
            servicio=self.servicio_con_precio,
            precio=Decimal("15000.00"),
            moneda="CLP",
        )

    def test_servicios_muestra_precio_guardado_por_admin(self):
        response = self.client.get("/servicios/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Diseño Web")
        self.assertContains(response, "Creamos sitios web modernos y adaptables.")
        self.assertContains(response, "Inmediata")
        self.assertContains(response, "CLP 15000,00")
        self.assertContains(response, "Desarrollo Django")
        self.assertContains(response, "Precio no informado")
        self.assertNotContains(response, "No hay servicios disponibles")

    def test_precios_muestra_precio_guardado_por_admin(self):
        response = self.client.get("/servicios/precios/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Diseño Web")
        self.assertContains(response, "CLP 15000,00")
        self.assertContains(response, "Desarrollo Django")
        self.assertContains(response, "Precio no informado")
