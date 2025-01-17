# Generar secret key

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

# Generar API Key para simuladores

primero ejecuta
```bash
docker compose -f docker-compose.local.yml exec api-cobranza python manage.py shell
```

y despues en la shell
```python
from rest_framework_api_key.models import APIKey
api_key, key = APIKey.objects.create_key(name="simuladores")
print(key)
```

copia la key y guardala en las variables de entorno de simuladores

# Configuración inicial de Docker con `docker compose`

Para asegurarse de levantar un grupo de `docker compose` limpio
```bash
docker compose up --build -d
```

Para asegurarse de eliminar todo hasta las imagenes del grupo
```bash
docker compose down --rmi local --remove-orphans
```
