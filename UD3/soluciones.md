# UD3 · Soluciones de ejercicios

> Documento de uso exclusivo del docente.  
> Numeración: E3.n corresponde al ejercicio n de la UD3.  
> Sin contenido de examen ni sus soluciones.

---

## E3.1 — Motor de tarifas

```php
<?php
/**
 * Determina la tarifa aplicable según la edad y el tipo de abono del cliente.
 *
 * @param array $cliente Array asociativo con claves 'edad' (int) y 'abono' (bool).
 * @return string Nombre de la tarifa aplicable.
 */
function calcularTarifa(array $cliente): string {
    $edad      = $cliente['edad'];
    $tieneAbono = $cliente['abono'] ?? false;

    if ($edad < 18) {
        $tarifa = "juvenil";
    } elseif ($edad < 65) {
        $tarifa = "general";
    } else {
        $tarifa = "senior";
    }

    // Operador ternario: añade sufijo si el cliente tiene abono
    $tarifa .= $tieneAbono ? " con descuento de abono" : "";

    return $tarifa;
}

// Casos de prueba
$clientes = [
    ["edad" => 15, "abono" => false],  // juvenil
    ["edad" => 30, "abono" => true],   // general con descuento de abono
    ["edad" => 70, "abono" => false],  // senior
    ["edad" => 17, "abono" => true],   // juvenil con descuento de abono
];

foreach ($clientes as $c) {
    echo "Edad {$c['edad']}: " . calcularTarifa($c) . "<br>";
}
?>
```

---

## E3.2 — Selector de plan de hosting

```php
<?php
/**
 * Devuelve los datos de un plan de hosting según su código.
 *
 * @param string $codigo Código del plan ('A', 'B', 'C' o 'D').
 * @return array Array asociativo con 'nombre', 'precio' y 'caracteristicas'.
 */
function obtenerPlan(string $codigo): array {
    // match usa comparación estricta (===) y es una expresión que devuelve valor.
    // switch usaría comparación débil (==) y requeriría break en cada caso.
    // Diferencia práctica aquí: match('0') no coincidiría con case 0 de un switch
    // debido a la coerción; match es más seguro y más conciso para este caso.
    return match ($codigo) {
        'A'      => ["nombre" => "Básico",    "precio" => 9.99,
                     "caracteristicas" => "1 dominio, 10 GB"],
        'B'      => ["nombre" => "Estándar",  "precio" => 19.99,
                     "caracteristicas" => "5 dominios, 50 GB"],
        'C', 'D' => ["nombre" => "Premium",   "precio" => 29.99,
                     "caracteristicas" => "Dominios ilimitados, 200 GB"],
        default  => ["nombre" => "Desconocido", "precio" => 0.0,
                     "caracteristicas" => "-"],
    };
}

foreach (['A', 'B', 'C', 'D', 'Z'] as $codigo) {
    $plan = obtenerPlan($codigo);
    echo "{$codigo}: {$plan['nombre']} — {$plan['precio']} € ({$plan['caracteristicas']})<br>";
}
?>
```

---

## E3.3 — Generador de tablas de multiplicar

```php
<?php
/**
 * Genera en HTML la tabla de multiplicar de un número usando for.
 *
 * @param int $numero Número del que generar la tabla.
 * @return string Bloque HTML con la tabla.
 */
function generarTablaFor(int $numero): string {
    $html = "<h3>Tabla del $numero (for)</h3><ul>";
    for ($i = 1; $i <= 10; $i++) {
        $html .= "<li>$numero × $i = " . ($numero * $i) . "</li>";
    }
    return $html . "</ul>";
}

/**
 * Genera en HTML la tabla de multiplicar de un número usando while.
 *
 * @param int $numero Número del que generar la tabla.
 * @return string Bloque HTML con la tabla.
 */
function generarTablaWhile(int $numero): string {
    $html = "<h3>Tabla del $numero (while)</h3><ul>";
    $i = 1;
    while ($i <= 10) {
        $html .= "<li>$numero × $i = " . ($numero * $i) . "</li>";
        $i++;
    }
    return $html . "</ul>";
}

// a) y b) Tablas del 5 con for y while
echo generarTablaFor(5);
echo generarTablaWhile(5);

// c) do-while con centinela -1
$numeros = [3, 7, 9, -1, 4]; // -1 es el centinela; 4 no debe procesarse
$idx = 0;
do {
    $actual = $numeros[$idx];
    if ($actual === -1) {
        break; // centinela encontrado: detiene el proceso
    }
    echo generarTablaFor($actual);
    $idx++;
} while ($idx < count($numeros));
?>
```

---

## E3.4 — Filtro de inventario

```php
<?php
$inventario = [
    ["nombre" => "Teclado",   "precio" => 25.0,  "stock" => 12],
    ["nombre" => "Ratón",     "precio" => 15.0,  "stock" => 0],
    ["nombre" => "Monitor",   "precio" => 180.0, "stock" => 5],
    ["nombre" => "Cable USB", "precio" => 5.0,   "stock" => 30],
];

// a) break: muestra productos hasta encontrar el primero agotado
echo "<h3>Recorrido con break</h3>";
foreach ($inventario as $producto) {
    if ($producto["stock"] === 0) {
        echo "Producto agotado: {$producto['nombre']}. Deteniendo recorrido.<br>";
        break;
    }
    echo "{$producto['nombre']}: {$producto['stock']} unidades<br>";
}

// b) continue: omite productos con precio > 50 €
$umbral = 50;
echo "<h3>Productos con precio ≤ $umbral € (continue)</h3>";
foreach ($inventario as $producto) {
    if ($producto["precio"] > $umbral) {
        continue; // salta este producto
    }
    echo "{$producto['nombre']}: {$producto['precio']} €<br>";
}
?>
```

---

## E3.5 — Catálogo de cursos

```php
<?php
$catalogo = [
    "DAW2"  => "Desarrollo de Aplicaciones Web",
    "DAM2"  => "Desarrollo de Aplicaciones Multiplataforma",
    "ASIR2" => "Administración de Sistemas Informáticos en Red",
    "SMR1"  => "Sistemas Microinformáticos y Redes",
];

/**
 * Busca un curso por código y devuelve su nombre o null si no existe.
 *
 * @param array  $catalogo Array asociativo código → nombre.
 * @param string $codigo   Código del curso a buscar.
 * @return string|null Nombre del curso o null.
 */
function buscarCurso(array $catalogo, string $codigo): ?string {
    return $catalogo[$codigo] ?? null;
}

/**
 * Comprueba si un nombre de curso existe en el catálogo.
 *
 * @param array  $catalogo Array asociativo código → nombre.
 * @param string $nombre   Nombre del curso a buscar.
 * @return bool true si el nombre existe.
 */
function existeCurso(array $catalogo, string $nombre): bool {
    return in_array($nombre, $catalogo, strict: true);
}

var_dump(buscarCurso($catalogo, "DAW2"));   // string "Desarrollo de Aplicaciones Web"
var_dump(buscarCurso($catalogo, "XXX"));    // NULL
var_dump(existeCurso($catalogo, "Desarrollo de Aplicaciones Web")); // true
var_dump(existeCurso($catalogo, "Robótica")); // false

// Ordenado por código (ksort mantiene asociación clave-valor)
$porCodigo = $catalogo;
ksort($porCodigo);
echo "<h3>Por código</h3>";
foreach ($porCodigo as $codigo => $nombre) {
    echo "$codigo: $nombre<br>";
}

// Ordenado por nombre (asort mantiene asociación clave-valor)
$porNombre = $catalogo;
asort($porNombre);
echo "<h3>Por nombre</h3>";
foreach ($porNombre as $codigo => $nombre) {
    echo "$codigo: $nombre<br>";
}
?>
```

---

## E3.6 — Inventario multinivel de almacén

```php
<?php
$almacenes = [
    "Madrid" => [
        ["producto" => "Portátil", "precio" => 600.0, "stock" => 4],
        ["producto" => "Tablet",   "precio" => 250.0, "stock" => 1],
    ],
    "Valencia" => [
        ["producto" => "Monitor",  "precio" => 180.0, "stock" => 8],
        ["producto" => "Teclado",  "precio" => 25.0,  "stock" => 2],
    ],
];

// a) Incremento del 10 % en todos los precios, sin modificar $almacenes
// array_map externo: itera sobre almacenes
// array_map interno: itera sobre productos de cada almacén
$almacenesActualizados = array_map(function (array $productos): array {
    return array_map(function (array $p): array {
        $p["precio"] = round($p["precio"] * 1.10, 2);
        return $p;
    }, $productos);
}, $almacenes);

// b) Productos con stock <= 2, manteniendo estructura por almacén
// array_map itera sobre almacenes; array_filter filtra dentro de cada uno
$stockBajo = array_map(function (array $productos): array {
    return array_filter($productos, fn(array $p): bool => $p["stock"] <= 2);
}, $almacenes);

echo "<h3>Precios actualizados (+10 %)</h3>";
print_r($almacenesActualizados);

echo "<h3>Productos con stock bajo (≤ 2 unidades)</h3>";
print_r($stockBajo);
?>
```

---

## E3.7 — Librería de funciones de validación

```php
<?php
/**
 * Valida el formato de un DNI español (8 dígitos + letra mayúscula).
 *
 * @param string $dni Cadena con el DNI a validar (p. ej. "12345678Z").
 * @return bool true si el formato es correcto.
 */
function validarDNI(string $dni): bool {
    return preg_match('/^[0-9]{8}[A-Z]$/', $dni) === 1;
}

/**
 * Calcula la edad en años cumplidos a partir de una fecha de nacimiento.
 *
 * @param string $fechaNacimiento Fecha en formato 'Y-m-d' (p. ej. '2000-05-15').
 * @return int Edad en años cumplidos.
 */
function calcularEdad(string $fechaNacimiento): int {
    $nacimiento = new DateTime($fechaNacimiento);
    $hoy        = new DateTime();
    return (int) $hoy->diff($nacimiento)->y;
}

/**
 * Formatea un valor numérico como precio en euros.
 *
 * @param float $valor     Valor a formatear.
 * @param int   $decimales Número de decimales (por defecto 2).
 * @return string Precio formateado (p. ej. "1.234,50 €").
 */
function formatearPrecio(float $valor, int $decimales = 2): string {
    return number_format($valor, $decimales, ',', '.') . ' €';
}

/**
 * Intercambia los valores de dos variables.
 *
 * El paso por referencia (&) es imprescindible: sin él, PHP crearía copias
 * locales de $a y $b dentro de la función; al salir, las variables originales
 * no habrían cambiado. Con &, la función opera directamente sobre las variables
 * del ámbito llamante.
 *
 * @param mixed $a Primera variable (modificada in situ).
 * @param mixed $b Segunda variable (modificada in situ).
 */
function intercambiar(mixed &$a, mixed &$b): void {
    $temp = $a;
    $a    = $b;
    $b    = $temp;
}

// --- Pruebas ---
var_dump(validarDNI("12345678Z"));  // true
var_dump(validarDNI("1234567z"));   // false (letra minúscula)

echo calcularEdad("2000-05-15") . " años<br>";
echo calcularEdad("1990-01-01") . " años<br>";

echo formatearPrecio(19.5)       . "<br>"; // 19,50 €
echo formatearPrecio(1234.5, 0)  . "<br>"; // 1.235 €
echo formatearPrecio(1234.5)     . "<br>"; // 1.234,50 €

$x = 10; $y = 20;
intercambiar($x, $y);
echo "x=$x y=$y<br>"; // x=20 y=10
?>
```

---

## E3.8 — Formulario de inscripción a curso

```html
<!-- inscripcion.html
     Se usa method="post" porque los datos son personales (nombre, email)
     y no deben aparecer en la URL ni en el historial del navegador. -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Inscripción a curso</title>
</head>
<body>
<h1>Formulario de inscripción</h1>
<form action="procesar_inscripcion.php" method="post">

    <label for="nombre">Nombre completo:</label>
    <input type="text" id="nombre" name="nombre" required>
    <br>

    <label for="email">Correo electrónico:</label>
    <input type="email" id="email" name="email" required>
    <br>

    <label for="curso">Curso:</label>
    <select id="curso" name="curso">
        <option value="daw2">2º DAW</option>
        <option value="dam2">2º DAM</option>
        <option value="asir2">2º ASIR</option>
    </select>
    <br>

    <fieldset>
        <legend>Modalidad</legend>
        <input type="radio" id="presencial" name="modalidad" value="presencial" checked>
        <label for="presencial">Presencial</label>
        <input type="radio" id="semipresencial" name="modalidad" value="semipresencial">
        <label for="semipresencial">Semipresencial</label>
    </fieldset>

    <input type="checkbox" id="condiciones" name="condiciones" value="1" required>
    <label for="condiciones">Acepto las condiciones del curso</label>
    <br><br>

    <button type="submit">Enviar inscripción</button>
</form>
</body>
</html>
```

---

## E3.9 — Procesador de inscripción con validación

```php
<?php
// --- Dependencias ---
// Reutilizamos formatearPrecio() de la librería de E3.7
require_once 'libreria_validacion.php';

// --- Recogida de datos con ?? para evitar avisos si el campo no llega ---
$nombre     = trim($_POST['nombre']     ?? '');
$email      = trim($_POST['email']      ?? '');
$curso      = trim($_POST['curso']      ?? '');
$condiciones = $_POST['condiciones']   ?? null;

// Valores permitidos para el campo 'curso'
$cursosPermitidos = ['daw2', 'dam2', 'asir2'];

// --- Validación ---
$errores = [];

if ($nombre === '') {
    $errores[] = "El nombre es obligatorio.";
}

if ($email === '') {
    $errores[] = "El correo electrónico es obligatorio.";
} elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    $errores[] = "El correo electrónico no tiene un formato válido.";
}

if (!in_array($curso, $cursosPermitidos, strict: true)) {
    $errores[] = "Debe seleccionar un curso válido.";
}

if ($condiciones !== "1") {
    $errores[] = "Debe aceptar las condiciones del curso.";
}

// --- Resultado ---
if (empty($errores)) {
    // Saneamiento antes de mostrar en HTML
    $nombreSeguro = htmlspecialchars($nombre, ENT_QUOTES, 'UTF-8');
    $emailSeguro  = htmlspecialchars($email,  ENT_QUOTES, 'UTF-8');
    $cursoSeguro  = htmlspecialchars($curso,  ENT_QUOTES, 'UTF-8');

    echo "<h2>Inscripción registrada correctamente</h2>";
    echo "<p>Nombre: $nombreSeguro</p>";
    echo "<p>Email: $emailSeguro</p>";
    echo "<p>Curso: $cursoSeguro</p>";
    // Reutilización de formatearPrecio() de E3.7
    echo "<p>Importe de matrícula: " . formatearPrecio(45.0) . "</p>";
} else {
    echo "<h2>Se han encontrado errores</h2>";
    echo "<ul>";
    foreach ($errores as $error) {
        echo "<li>" . htmlspecialchars($error, ENT_QUOTES, 'UTF-8') . "</li>";
    }
    echo "</ul>";
}
?>
```
