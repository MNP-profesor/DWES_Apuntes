# Soluciones UD1 — Arquitecturas y tecnologías de programación Web en entorno servidor

> **Uso exclusivo del docente.** Este fichero va en el repositorio privado `DWES_Soluciones`, carpeta `UD1/`.
> Numeración: E1.n corresponde a `#exr-UD1-n` en el libro público.

---

## E1.1 — Clasificación de tecnologías por lugar de ejecución

| # | Elemento | Dónde se ejecuta | Justificación |
|---|---|---|---|
| 1 | PHP | Servidor | El intérprete reside en el servidor; el cliente nunca recibe el código fuente PHP. |
| 2 | JavaScript del navegador | Cliente | El navegador descarga y ejecuta JS en el dispositivo del usuario. |
| 3 | jQuery | Cliente | Biblioteca JS; se descarga en el cliente y manipula el DOM. |
| 4 | Node.js | Servidor (o ambos) | Node.js ejecuta JS en el servidor; no confundir con JS de navegador. Se acepta «ambos» con razonamiento adecuado. |
| 5 | CSS | Cliente | El motor de renderizado del navegador interpreta el CSS. |
| 6 | Java/Servlets | Servidor | Los Servlets se ejecutan en el contenedor de servidor (Tomcat, etc.). |
| 7 | Python/Django | Servidor | Django es un framework de servidor; genera HTML antes de enviarlo. |
| 8 | AJAX (petición desde el cliente) | Ambos | El cliente inicia la petición, pero el servidor la procesa y responde. Se acepta «cliente → servidor». |
| 9 | WebSockets desde el cliente | Ambos | El cliente abre el socket; el servidor mantiene la conexión bidireccional. |
| 10 | Consulta SQL ejecutada desde PHP | Servidor | PHP ejecuta la consulta contra la BD, todo en el lado del servidor. |
| 11 | Validación de formulario con JavaScript | Cliente | Se ejecuta en el navegador antes de enviar el formulario. |
| 12 | API REST consumida con `fetch()` | Cliente | `fetch()` es una API del navegador; la respuesta puede venir del servidor, pero la llamada la inicia el cliente. |

**Criterio de calificación:** 1 punto por elemento correcto con justificación válida (máx. 12, normalizado a 10). Se acepta «ambos» para Node.js, AJAX y WebSockets con razonamiento adecuado.

---

## E1.2 — Estático, dinámico embebido o script independiente

| # | Fragmento | Clasificación | Pista identificadora |
|---|---|---|---|
| 1 | Página HTML pura | Estático | Ausencia total de delimitadores de código; ningún proceso lo ejecuta en el servidor. |
| 2 | PHP embebido en HTML | Dinámico — código embebido | Presencia de `<?php ... ?>` dentro del documento HTML. |
| 3 | Script Python con `print()` | Dinámico — script independiente | El script genera todo el HTML mediante instrucciones `print`; no hay plantilla HTML base. |
| 4 | HTML + JS modifica DOM | Estático (en servidor) | El servidor envía HTML fijo; la dinamicidad la aporta JS en el cliente, no el servidor. |
| 5 | Plantilla `{{variable}}` | Ninguno / plantilla sin resolver | Los marcadores `{{}}` no se han procesado; falta el motor de plantillas que los resuelva. |
| 6 | ASP clásico (`<% ... %>`) | Dinámico — código embebido | Los delimitadores `<% ... %>` indican código de servidor embebido en el documento. |

**Criterio:** 1,5 puntos por clasificación correcta con pista textual señalada (máx. 9, normalizado a 10). Se descuenta 0,5 si la clasificación es correcta pero la pista no está señalada.

---

## E1.3 — Identificación de roles en una arquitectura real

**Arquitectura presentada:** navegador → balanceador de carga → 2× Nginx → 3× PHP-FPM → MySQL.

**Servidor Web:** Nginx.  
*Justificación:* Nginx es el proceso que recibe las peticiones HTTP, sirve los ficheros estáticos directamente y delega las peticiones dinámicas a PHP-FPM. Cumple la definición de servidor Web estudiada en clase.

**Componente más próximo al servidor de aplicaciones:** PHP-FPM.  
*Justificación:* el pool de procesos PHP-FPM mantiene intérpretes PHP activos en memoria, gestiona la concurrencia de peticiones y ejecuta la lógica de la aplicación, de manera análoga a un servidor de aplicaciones ligero. No es un servidor de aplicaciones en sentido estricto (no ofrece transacciones distribuidas ni servicios de infraestructura empresarial), pero es el elemento que más se aproxima en este stack.

**Balanceador de carga:** no es ni servidor Web ni servidor de aplicaciones.  
*Justificación:* su función es distribuir el tráfico entre las instancias de Nginx según algún algoritmo (round-robin, least connections, etc.), sin procesar el contenido de las peticiones ni ejecutar código de aplicación.

**Criterio:** 3 puntos por cada respuesta correctamente justificada (servidor Web, componente más cercano a servidor de aplicaciones, balanceador). Se exige justificación; sin ella, máx. 1 punto por respuesta.

---

## E1.4 — Estudio comparativo razonado

Esta actividad es de respuesta abierta. Se evalúa la solidez del razonamiento, no la tecnología elegida.

**Criterios de corrección:**

- Coherencia entre el escenario y la tecnología recomendada (3 puntos): la elección debe responder a características concretas del escenario (volumen, presupuesto, equipo, requisitos de rendimiento).
- Argumentos técnicos (3 puntos): tres argumentos técnicos válidos y diferenciados, no de preferencia personal.
- Descarte razonado de una alternativa (2 puntos): se nombra explícitamente una alternativa descartada y se argumenta por qué no es la más adecuada para ese escenario.
- Claridad expositiva y terminología técnica en la defensa oral (2 puntos): uso correcto de los conceptos de la unidad.

**Ejemplos de respuesta por escenario:**

**Escenario A — Tienda online de pequeño volumen → PHP + Laravel.**  
Alta cuota de mercado en comercio electrónico, amplio ecosistema de extensiones, coste de infraestructura reducido, equipo de desarrollo fácil de contratar.  
Alternativa descartada: Java EE (sobrecarga de configuración y coste de servidor de aplicaciones injustificado para ese volumen).

**Escenario B — Intranet corporativa gran empresa Java → Java EE / Spring Boot.**  
El equipo ya tiene experiencia en Java, la plataforma ofrece transacciones y seguridad declarativa, integración natural con sistemas ERP existentes.  
Alternativa descartada: PHP (curva de aprendizaje inversa para el equipo existente y ecosistema menos maduro para integraciones empresariales complejas).

**Escenario C — API de altísima concurrencia → Node.js.**  
El modelo de E/S no bloqueante está diseñado para gestionar miles de conexiones simultáneas con un único proceso y consumo reducido de memoria. El equipo puede reutilizar conocimientos de JavaScript del cliente.  
Alternativa descartada: PHP síncrono/multiproceso (mayor consumo de recursos para esa concurrencia).

**Escenario D — Proyecto académico personal → cualquier tecnología con justificación de aprendizaje.**  
Se acepta PHP (facilidad de puesta en marcha), Python (legibilidad, recursos de aprendizaje) o Node.js (JS ya conocido). Lo evaluable es la justificación, no la elección.

---

## E1.5 — Trazado manual de la salida generada

**Documento original (pseudocódigo embebido):**

```
<html><body>
  [INICIO_CÓDIGO: imprimir 'Bienvenido' FIN_CÓDIGO]
  [INICIO_CÓDIGO: imprimir 3 + 5 FIN_CÓDIGO]
  [INICIO_CÓDIGO: SI variable_rol = 'admin' ENTONCES imprimir 'Panel de control' FIN_CÓDIGO]
</body></html>
```

**HTML que el navegador recibiría si `variable_rol = 'admin'`:**

```html
<html><body>
  Bienvenido
  8
  Panel de control
</body></html>
```

**HTML que el navegador recibiría si `variable_rol` tiene cualquier otro valor:**

```html
<html><body>
  Bienvenido
  8
  
</body></html>
```

*(Sin «Panel de control» y sin rastro alguno de delimitadores ni código.)*

**Criterio:** 4 puntos por cada bloque correctamente trazado (valor fijo, resultado aritmético, condicional); total 12 normalizado a 10. Se descuenta 1 punto por cada rastro de delimitador o código que permanezca en el HTML resultante.

---

## E1.6 — Puesta en marcha del entorno de trabajo

La actividad es procedimental. Se evalúa la memoria entregada con los siguientes criterios:

| Ítem | Puntos |
|---|---|
| Fichero `info.php` creado y ejecutado correctamente (evidencia: captura de pantalla o descripción del resultado) | 4 |
| Versión de PHP instalada correctamente identificada y anotada (ej. `8.2.x`) | 2 |
| Ruta del fichero `php.ini` cargado (*Loaded Configuration File*) identificada | 2 |
| Valor de la directiva `memory_limit` localizado y anotado | 2 |

**Valores habituales de referencia:**

- XAMPP en Windows: PHP 8.2.x, `memory_limit = 128M` o `256M`, `php.ini` en `C:\xampp\php\php.ini`.
- Docker con imagen oficial `php:8.2-apache`: `memory_limit = 128M`, `php.ini` en `/usr/local/etc/php/`.
