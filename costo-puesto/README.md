# Costo Puesto: app para importadores

Aplicación web para importadores de zapatillas, accesorios y otros productos puntuales.
Responde lo que todo importador pregunta antes de pedir mercancía: **¿cuánto me cuesta cada unidad puesta en mi bodega y a cuánto la vendo?**

Abre `index.html` en cualquier navegador. No requiere instalación. Los datos se guardan en el navegador del usuario.

## Módulos

| Módulo | Qué resuelve |
|---|---|
| **Cotizador** | Costo puesto (landed cost) por producto: FOB, flete, seguro, arancel, IVA, agencia de aduana, flete local y otros gastos. Reparte los gastos según el valor de cada producto. Acepta Incoterms EXW, FOB, CIF y DDP. Sugiere precio mayorista y detal según el margen objetivo. |
| **Importaciones** | Seguimiento de cada pedido: Cotizado → Pagado → En producción → Embarcado → En aduana → En bodega. Guarda la fecha de llegada (ETA) y el número de contenedor. |
| **Inventario** | Existencias por talla (curva de tallas en zapatillas, `U` para accesorios). Al recibir una importación se carga sola con costo promedio ponderado. Avisa cuando el stock está bajo. |
| **Ventas** | Registra cada venta por canal (detal, mayorista, marketplace), descuenta la talla y calcula la utilidad real. |
| **Catálogo WhatsApp** | Arma un texto listo para pegar en estados, grupos y listas de difusión, solo con lo disponible, con precios y tallas. |
| **Resumen** | Capital en tránsito, inventario valorizado, ventas y utilidad del mes, productos por reponer y los más vendidos. |

## Fórmula de costo puesto

```
CIF (US$)        = FOB + flete + seguro
Base aduanera    = CIF × tasa de cambio
Arancel          = Base × % arancel
IVA importación  = (Base + Arancel) × % IVA   → costo solo si el importador no es responsable de IVA
Total puesto     = Base + Arancel + IVA no descontable + agencia + flete local + otros
Factor           = Total puesto ÷ (FOB × tasa de cambio)
Costo unitario   = FOB unitario × tasa de cambio × Factor
Precio detal     = Costo unitario ÷ (1 − margen)
```

Los porcentajes de arancel e IVA son configurables. El usuario debe confirmar con su agencia de aduanas el arancel exacto de su partida arancelaria.

## Cómo venderla

**Cliente objetivo:** importadores pequeños y medianos que traen mercancía de China (zapatillas, gorras, medias, accesorios, productos de temporada) y hoy calculan en Excel o en el cuaderno.

**Propuesta de valor:** dejar de vender a pérdida por no sumar flete, arancel y gastos locales en el precio.

**Planes sugeridos (para validar con clientes):**

| Plan | Incluye |
|---|---|
| Emprendedor | Cotizador + catálogo WhatsApp, 1 usuario |
| Importador | Todo lo anterior + importaciones, inventario por talla y ventas |
| Empresa | Varios usuarios y bodegas, datos en la nube, reportes y soporte |

## Siguiente fase

1. Datos en la nube con Supabase (el repositorio ya tiene el cliente en `app/core/supabase_client.py`): cuentas por empresa, varios dispositivos, varios usuarios.
2. Tasa de cambio automática del día.
3. Catálogo con fotos y enlace público para clientes mayoristas.
4. Exportar a Excel y PDF de la cotización para enviar al socio o al banco.
5. Volumen y peso (CBM) para comparar contenedor 20', 40' o carga consolidada.
