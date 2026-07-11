# UD2 — Soluciones de ejercicios

> **Uso exclusivo del docente.**  
> Este archivo se publica en el repositorio privado `DWES_Soluciones`.  
> No contiene el enunciado ni la solución de la prueba de evaluación.

---

## E2.1 — De Java a PHP: observando el cambio de paradigma

**Fichero:** `ficha_producto.php`

```php
<?php
// A diferencia de Java, donde el dato y la vista están separados en clases
// (p. ej. una clase Producto y una clase VistaProducto), aquí mezclamos
// HTML y PHP en el mismo archivo: el dato se genera y se muestra en el mismo lugar.
// Tecnología de servidor (CE2.b): PHP.
// Mecanismo de generación embebida (CE2.a): bloques <?php ?> y <?= ?>.

$nombre_producto = "Teclado mecánico RGB";
$precio_producto = 59.90;
$stock_producto  = 14;
?>
<!DOCTYPE html>
<html lang="es">
<head><title>Ficha de producto</title></head>
<body>
  <h1>Ficha de producto</h1>
  <ul>
    <li>Nombre: <?= $nombre_producto ?></li>
    <li>Precio: <?= $precio_producto ?> €</li>
    <li>Stock: <?= $stock_producto ?> unidades</li>
  </ul>
</body>
</html>
```

**Notas de corrección:**

- El código fuente que recibe el navegador no debe contener `<?php`, `<?=` ni el símbolo `$`.  
- El comentario comparativo con Java es el indicador más fiable de comprensión conceptual; si lo omite o es superficial, pedir ampliación.  
- Valorar positivamente el uso de `<?= ?>` para los valores (más limpio que `<?php echo ... ?>`).

---

## E2.2 — Mapa de delimitadores en una plantilla compleja

**Fichero:** `tienda.php`

```php
<!DOCTYPE html>
<html lang="es">
<head><title>Tienda</title></head>
<body>

<!-- Zona 1: cabecera -->
<header>
  <?php $usuario = "Marta"; // bloque 1 — CE2.a, CE2.c ?>
  <h1>Hola, <?= $usuario ?></h1>  <!-- bloque 2 — CE2.c -->
</header>

<!-- Zona 2: listado de 3 productos -->
<section>
  <?php
  // bloque 3 — CE2.a, CE2.c, CE2.e
  $p1 = "Ratón";   $precio1 = 19.99;
  $p2 = "Teclado"; $precio2 = 49.99;
  $p3 = "Monitor"; $precio3 = 159.00;
  ?>
  <p><?= $p1 ?>: <?= $precio1 ?> €</p>  <!-- bloques 4, 5 — CE2.c -->
  <p><?= $p2 ?>: <?= $precio2 ?> €</p>
  <p><?= $p3 ?>: <?= $precio3 ?> €</p>
</section>

<!-- Zona 3: barra lateral de filtros -->
<aside>
  <?php $filtros_activos = 2; // bloque 6 — CE2.a, CE2.c ?>
  <p>Filtros activos: <?= $filtros_activos ?></p>  <!-- bloque 7 — CE2.c -->
</aside>

<!-- Zona 4: pie de página -->
<footer>
  <?php $anio = date('Y'); // bloque 8 — CE2.a, CE2.c ?>
  <p>&copy; <?= $anio ?> Mi Tienda</p>  <!-- bloque 9 — CE2.c -->
</footer>

</body>
</html>
```

**Explicación del cierre `?>`:**

Si se comenta el `?>` de cierre del bloque 3, PHP interpreta todo el HTML siguiente (las etiquetas `<p>`, los textos literales, etc.) como código PHP, intentando ejecutarlos como sentencias. El resultado es un `Parse error` o una página en blanco, porque el intérprete espera sentencias PHP válidas y encuentra etiquetas HTML.

**Notas de corrección:**

- Valorar que la tabla de CE esté completa y correctamente referenciada (CE2.a para el mecanismo general, CE2.c para los delimitadores concretos).  
- Si el alumno usa `date('Y')` para el año actual en el pie: bonificación por uso de función de fecha no exigida.

---

## E2.3 — Depurador humano: caza de errores en cadena

**Fragmento A** — Errores: falta `;` en la primera asignación y falta `?>` al cierre.

```php
<?php
$nombre = "Carlos";      // ← faltaba ; en la versión errónea
echo "Hola, $nombre";
?>                       // ← faltaba el cierre en la versión errónea
```

**Fragmento B** — Error: comillas dobles anidadas sin escapar.

```php
<?php
$mensaje = "El alumno dijo: \"Hola, mundo\"";  // ← escapar con \"
echo $mensaje;
?>
```

Alternativa válida: usar comillas simples en el exterior cuando no hay interpolación:

```php
$mensaje = 'El alumno dijo: "Hola, mundo"';
```

**Fragmento C** — Error: comentario de bloque no cerrado.

```php
<?php
/* Este es el comentario */   // ← faltaba el */ en la versión errónea
$valor = 42;
echo $valor;
?>
```

**Fragmento D** — Error lógico (sin Parse error): uso de `^` como potencia.

```php
<?php
// INCORRECTO: ^ es XOR de bits en PHP, no potencia
// $resultado = 2 ^ 8;   // da 10, no 256

// CORRECTO: usar ** o pow()
$resultado = 2 ** 8;   // 256
echo $resultado;       // resultado esperado: 256
?>
```

**Notas de corrección:**

- Fragmento D es el discriminador: quien solo busca errores de sintaxis (Parse error) no lo detectará. Hay que ejecutar el código y comparar con 256.  
- Penalizar con -0,5 pts si el alumno no anota la línea exacta del error en un comentario.

---

## E2.4 — Panel de configuración con variables y constantes

```php
<?php
define('IVA_GENERAL',  0.21);
define('IVA_REDUCIDO', 0.10);

$nombre_tienda     = "TechStore";
$moneda            = "EUR";
$descuento_activo  = true;
$numero_productos  = 248;
$email_contacto    = "contacto@techstore.example";
$modo_mantenimiento = false;
?>
<!DOCTYPE html>
<html lang="es">
<head><title>Panel de configuración</title></head>
<body>
<table border="1">
  <tr><th>Variable</th><th>Valor</th><th>Tipo</th></tr>
  <?php
  $vars = [
    'nombre_tienda'      => $nombre_tienda,
    'moneda'             => $moneda,
    'descuento_activo'   => $descuento_activo,
    'numero_productos'   => $numero_productos,
    'email_contacto'     => $email_contacto,
    'modo_mantenimiento' => $modo_mantenimiento,
  ];
  foreach ($vars as $nombre => $valor) {
      // Nota: foreach se estudia en UD3; es válido usarlo aquí o bien
      // repetir cada fila manualmente, que es lo esperable en UD2.
      $display = var_export($valor, true);
      echo "<tr><td>\$$nombre</td><td>$display</td><td>" . gettype($valor) . "</td></tr>\n";
  }
  ?>
</table>

<?php
// Intento de reasignación — descomenta para ver el error:
// define('IVA_GENERAL', 0.25);
// Fatal error: Cannot redefine constant IVA_GENERAL

/*
 * Diferencias si se reescribiera en Java (mínimo 3):
 * 1. En Java habría que declarar el tipo: String nombreTienda = "TechStore";
 * 2. Las constantes se declaran con 'final static': final static double IVA_GENERAL = 0.21;
 * 3. Todo debería estar dentro de una clase; en PHP funciona en el nivel superior del archivo.
 */
?>
</body>
</html>
```

**Notas de corrección:**

- Si el alumno usa `foreach`, es válido aunque se adelante a UD3; si no lo usa y repite las filas manualmente, también es correcto y más coherente con el alcance de la unidad.  
- Las 3 diferencias con Java son orientativas; cualquier diferencia correcta y bien argumentada puntúa.

---

## E2.5 — Catálogo de productos con array asociativo multinivel

```php
<?php
$catalogo = [
    ["nombre" => "Teclado",   "precio" => 45.50,  "stock" => 12, "categoria" => "Periféricos"],
    ["nombre" => "Monitor",   "precio" => 189.00, "stock" =>  5, "categoria" => "Pantallas"],
    ["nombre" => "Ratón",     "precio" =>  19.90, "stock" => 30, "categoria" => "Periféricos"],
    ["nombre" => "Disco SSD", "precio" =>  79.00, "stock" =>  8, "categoria" => "Almacenamiento"],
];

// Valor total del inventario (suma manual, sin array_sum ni bucles)
$valor_total = $catalogo[0]['precio'] * $catalogo[0]['stock']
             + $catalogo[1]['precio'] * $catalogo[1]['stock']
             + $catalogo[2]['precio'] * $catalogo[2]['stock']
             + $catalogo[3]['precio'] * $catalogo[3]['stock'];
// 45.50×12 + 189×5 + 19.90×30 + 79×8 = 546 + 945 + 597 + 632 = 2720 €

$categorias_disponibles = ["Periféricos", "Pantallas", "Almacenamiento"];
?>
<!DOCTYPE html>
<html lang="es">
<head><title>Catálogo</title></head>
<body>
<table border="1">
  <tr><th>Nombre</th><th>Precio</th><th>Stock</th><th>Categoría</th></tr>
  <tr>
    <td><?= $catalogo[0]['nombre'] ?></td>
    <td><?= $catalogo[0]['precio'] ?> €</td>
    <td><?= $catalogo[0]['stock'] ?></td>
    <td><?= $catalogo[0]['categoria'] ?></td>
  </tr>
  <tr>
    <td><?= $catalogo[1]['nombre'] ?></td>
    <td><?= $catalogo[1]['precio'] ?> €</td>
    <td><?= $catalogo[1]['stock'] ?></td>
    <td><?= $catalogo[1]['categoria'] ?></td>
  </tr>
  <tr>
    <td><?= $catalogo[2]['nombre'] ?></td>
    <td><?= $catalogo[2]['precio'] ?> €</td>
    <td><?= $catalogo[2]['stock'] ?></td>
    <td><?= $catalogo[2]['categoria'] ?></td>
  </tr>
  <tr>
    <td><?= $catalogo[3]['nombre'] ?></td>
    <td><?= $catalogo[3]['precio'] ?> €</td>
    <td><?= $catalogo[3]['stock'] ?></td>
    <td><?= $catalogo[3]['categoria'] ?></td>
  </tr>
</table>

<p>Valor total del inventario: <?= $valor_total ?> €</p>
<p>Categorías distintas: <?= count($categorias_disponibles) ?></p>

<?php
// print_r muestra la estructura con claves pero sin tipos ni longitudes:
echo "<pre>"; print_r($catalogo); echo "</pre>";

// var_dump añade el tipo de cada valor y la longitud (bytes) de cada string:
echo "<pre>"; var_dump($catalogo); echo "</pre>";

/*
 * var_dump aporta sobre print_r:
 * - El tipo exacto de cada valor: string(7), int, float, bool...
 * - La longitud en bytes de cada cadena: string(7) "Teclado"
 * print_r es más legible para depuración rápida; var_dump, para verificar tipos.
 */
?>
</body>
</html>
```

**Resultado esperado:** valor total = 2720 €; 3 categorías distintas.

---

## E2.6 — Validador de formulario de registro

```php
<?php
$edad_texto     = "17 años";
$precio_texto   = "29,99";
$acepta_texto   = "on";
$cantidad_texto = "3";

// 1. Conversión de edad
$edad     = (int) $edad_texto;   // 17
$es_adulto = $edad >= 18;        // false

// 2. Conversión de precio (corrigiendo la coma decimal)
$precio_normalizado = str_replace(",", ".", $precio_texto);  // "29.99"
$precio             = (float) $precio_normalizado;            // 29.99

// 3. Conversión de aceptación
// (bool) "on" daría true porque cualquier string no vacío (y distinto de "0") es truthy,
// pero (bool) "off" TAMBIÉN daría true. La comparación con "on" es la forma correcta:
$acepta = ($acepta_texto === "on");  // true

// 4. Importe final
$importe_final = round($precio * (int) $cantidad_texto, 2);  // 89.97

// 5. Comparaciones con === y ==
var_dump((int) $edad_texto === "17");  // bool(false) — int vs string
var_dump((int) $edad_texto === 17);    // bool(true)  — int vs int
var_dump((int) $edad_texto == "17");   // bool(true)  — == convierte antes
var_dump((int) $edad_texto == 17);     // bool(true)

echo "¿Es adulto? ";    var_dump($es_adulto);    // bool(false)
echo "Importe final: "; var_dump($importe_final); // float(89.97)
?>
```

**Notas de corrección:**

- El apartado 3 (por qué no usar `(bool)` directamente) es el discriminador conceptual. Si el alumno solo escribe `$acepta = (bool) $acepta_texto` sin el comentario, la solución funciona por casualidad pero no demuestra comprensión.  
- El apartado 5 requiere mostrar **4** comparaciones (=== con "17", === con 17, == con "17", == con 17) para evidenciar la diferencia completa.

---

## E2.7 — Comparativa de entornos: desarrollo vs. producción

```php
<?php
declare(strict_types=1);

// MODO DESARROLLO: mostrar todos los errores
error_reporting(E_ALL);
ini_set('display_errors', '1');

// Error 1: variable no definida
echo $variable_no_definida;   // Warning: Undefined variable $variable_no_definida

// Error 2: división entre cero
$resultado = 10 / 0;          // Warning: Division by zero (PHP 8: DivisionByZeroError)
echo $resultado;

/*
 * Con display_errors = '0' (modo producción):
 * La página se muestra en blanco o con el contenido anterior a los errores,
 * sin ningún mensaje visible. Los errores siguen ocurriendo internamente;
 * con log_errors = '1' quedarían registrados en el log del servidor.
 *
 * Con declare(strict_types=1) y una función tipada:
 * function sumar(int $a, int $b): int { return $a + $b; }
 * sumar("3", 5);  // TypeError: sin strict_types PHP convertiría "3" a 3;
 *                 // con strict_types lanza excepción inmediatamente.
 */
?>
```

---

## E2.8 — Motor de descuentos con operadores combinados

```php
<?php
$precio_base  = 120.0;
$es_socio     = true;
$unidades     = 5;
$codigo_promo = "VERANO10";

// Descuento 1: 15% por ser socio
$precio_tras_socio = $es_socio
    ? $precio_base * 0.85
    : $precio_base;                      // 102.0

// Descuento 2: 10% adicional por código promocional
$precio_tras_promo = ($codigo_promo === "VERANO10")
    ? $precio_tras_socio * 0.90
    : $precio_tras_socio;               // 91.8

// Precio final
$precio_final = round($precio_tras_promo * $unidades, 2);  // 459.0

// Condición de envío prioritario
$envio_prioritario = ($es_socio && $unidades > 3) || ($precio_final > 400);
// true — por el segundo criterio: 459 > 400

echo "Precio base:           $precio_base €\n";
echo "Tras descuento socio:  $precio_tras_socio €\n";
echo "Tras descuento promo:  $precio_tras_promo €\n";
echo "Precio final (x$unidades): $precio_final €\n";
echo "Envío prioritario:     " . ($envio_prioritario ? "Sí" : "No") . "\n";
?>
```

**Resultado esperado:** 102 € → 91,80 € → 459 €; envío prioritario = Sí.

---

## E2.9 — Sistema de tickets con tres estrategias de ámbito

```php
<?php
$ultimo_ticket = 0;

function generarTicketGlobal(): int {
    global $ultimo_ticket;
    $ultimo_ticket++;
    return $ultimo_ticket;
}

function generarTicketStatic(): int {
    static $contador = 0;
    $contador++;
    return $contador;
}

function generarTicketRoto(): int {
    $contador_local = 0;   // se reinicia en CADA llamada
    $contador_local++;
    return $contador_local; // siempre devuelve 1
}
?>
<!DOCTYPE html>
<html lang="es">
<head><title>Tickets</title></head>
<body>
<table border="1">
  <tr>
    <th>Llamada</th>
    <th>generarTicketGlobal()</th>
    <th>generarTicketStatic()</th>
    <th>generarTicketRoto()</th>
  </tr>
  <?php for ($i = 1; $i <= 4; $i++): ?>
  <tr>
    <td><?= $i ?></td>
    <td><?= generarTicketGlobal() ?></td>
    <td><?= generarTicketStatic() ?></td>
    <td><?= generarTicketRoto() ?></td>
  </tr>
  <?php endfor; ?>
</table>

<p>
  <strong>¿Por qué generarTicketRoto() siempre devuelve 1?</strong>
  Porque <code>$contador_local</code> se crea de nuevo (valor 0) en cada invocación
  de la función. No hay memoria entre llamadas: la variable local se destruye al salir
  de la función.
</p>
<p>
  <strong>Estrategia recomendada para un sistema real: <code>static</code>.</strong>
  La variable <code>static</code> conserva su valor entre llamadas igual que
  <code>global</code>, pero está encapsulada dentro de la función: ningún otro
  fragmento de código puede modificarla accidentalmente. Con <code>global</code>,
  cualquier parte del script podría cambiar <code>$ultimo_ticket</code> sin pasar
  por la función, lo que dificulta el mantenimiento y puede introducir errores difíciles
  de rastrear.
</p>
</body>
</html>
```

**Resultado esperado:**

| Llamada | Global | Static | Roto |
|:---:|:---:|:---:|:---:|
| 1 | 1 | 1 | 1 |
| 2 | 2 | 2 | 1 |
| 3 | 3 | 3 | 1 |
| 4 | 4 | 4 | 1 |
