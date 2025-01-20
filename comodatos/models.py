from django.db import models


class Comodatos(models.Model):
    contrato = models.CharField(max_length=150)
    compra_minima_mensual_dinero = models.IntegerField()
    compra_minima_mensual_reactivos = models.IntegerField()
    fecha_inicio = models.DateField(auto_now=False, auto_now_add=False)
    fecha_termino = models.DateField(auto_now=False, auto_now_add=False)
    is_renovable = models.BooleanField()
    is_renovable_automatico = models.BooleanField()

    estado = models.ForeignKey("master_data.Estados", on_delete=models.CASCADE)
    cliente = models.ForeignKey("clientes.Clientes", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)


class ComodatosInstrumentos(models.Model):
    valor_neto = models.IntegerField()

    comodato = models.ForeignKey("comodatos.Comodatos", on_delete=models.CASCADE)
    instrumentos = models.ForeignKey(
        "instrumentos.Instrumentos", on_delete=models.CASCADE
    )

    ubicacion = models.ForeignKey("master_data.Ubicaciones", on_delete=models.CASCADE)
    moneda = models.ForeignKey("master_data.Monedas", on_delete=models.CASCADE)
