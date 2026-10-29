#EVIDENCIA 
##Evidencia inicial de la creación de estructura y el funcionamiento correcto del GitActions 
<img width="758" height="634" alt="image" src="https://github.com/user-attachments/assets/c51896d7-d360-4501-9536-5278a0a77c64" />
<img width="724" height="662" alt="image" src="https://github.com/user-attachments/assets/e43e7109-5bef-4269-9aab-2b6c46c39308" />
##Paso 6 -Provocar una falla de forma controlada
<img width="646" height="266" alt="image" src="https://github.com/user-attachments/assets/ee60482d-2c24-490a-8dc0-14d57e20e814" />

¿Qué step falló? 
Falló el step “Ejecutar pruebas”, el cual está marcado con un icono roja en forma de “x”
¿Qué mensaje produjo pytest? 
Produjo el mensaje AssertionError: assert 'CRITICO' == 'NORMAL' en la línea 28 de los logs, indicando que la prueba test_stock_critico falló porque el resultado obtenido fue "CRITICO", mientras que el cambio intencional esperaba que fuera "NORMAL".
¿Los steps anteriores habían terminado correctamente? 
Si , los steps anteriormente finalizaron correctamente, en la imagen se observa que el step inmediatamente anterior, “Validar sintaxis”, fue ejecutada exitosamente lo que confirma que pasó sin problemas antes de llegar a las pruebas. 
¿Qué diferencia visual encuentras entre esta ejecución y la anterior?
Por un lado en el panel lateral izquierdo vemos como el trabajo de validar-python aparece con un marcado icono rojo , y dentro de los logs del paso “Ejecutar pruebas” se despliega una sección detallada del error  “FAILURES” presentado en lugar de mostrar únicamente la lista de pruebas con estado “PASSED”.

##Paso 7 – Enter el valor de Actions en un Pull Request 
<img width="593" height="150" alt="image" src="https://github.com/user-attachments/assets/f5e3fd10-1f84-4c85-9a50-e91d000f0272" />
<img width="561" height="459" alt="image" src="https://github.com/user-attachments/assets/6c87d206-22bd-4aa2-b1af-47c3e6679afe" />
<img width="719" height="524" alt="image" src="https://github.com/user-attachments/assets/735f99b1-bcb4-4955-96e6-942f9ee62980" />

## Paso 8 -  Ejecutar el workflow manualmente
![Uploading image.png…]()

##PREGUNTAS DE ANÁLISIS PARA RESPONDER DESPUÉS DE EJECUTAR
1. Identifica una ejecución exitosa y una fallida. ¿Qué commit o cambio produjo cada una y qué step determinó el resultado? 
Ejecución fallida: Al realizar el commit donde cambie el estado de “CRÍTICO” a “NORMAL” intencionalmente causo que el workflow fallara. El step que determinnó el resultado fue “Ejecutar pruebas”
Ejecución exitosa: Cuando volvi a restaurar como tenia antes de realizar el commit de el cambio de estado se puede observar como todos los steps funcionaban correctamente.

2. ¿Por qué ejecutar pytest localmente no reemplaza ejecutar pytest en GitHub Actions?
Por que de manera local guarda un historial de configuraciones y archivos que usualmente no estan en el repositorio debido a que localmente me funcionaba todo debido a que tenia la carpeta srv y el archivo requirements.txt en mi disco duro, pero en github fallaba por que la maquina virtual no tenia esos archivos hata que los subi con el git push. 

 3. ¿Qué riesgo tendría hacer merge a main sin esperar los checks del Pull Request? 
El riesgo es grande debido a que si el código lleva algún error rompería la versión que habría en el repositorio y afectará a todo el equipo incluyendo los avances que ya se encuentran en el repositorio. 

4. En tu ejecución fallida, copia solo la línea esencial del error y explica qué te permitió diagnosticar. 
En mi ejecución fallida me aparecio este linea de error AssertionError: assert 'CRITICO' == 'NORMAL' 
Con esto me permitió diagnosticar que la función estaba retonando “CRITICO”, pero la prueba esperaba que el resultado fuera “NORMAL”, evidenciando una falla en la lógica de negocio.

5. ¿Qué diferencia existe entre un step que usa `uses:` y uno que utiliza `run:`? 
uses: invoca una action (un componente reutilizable)como cuando usamos actions/checkout para descargar el repositorio. 
run: ejecuta un comando de consola directo del sistema operativo dentro del runner, como cuando se utilizó run: pytest -v para ejecutar las pruebas. 

6. ¿Qué información aporta `${{ github.actor }}` en `run-name` y por qué puede ser útil en un proyecto en equipo? 
Aporta el nombre de usuario de la persona que inició la ejecución o hizo el push. En un equipo, es útil para identificar rápidamente quien realizó los cambios y sirve como evidencia de participación. 

7. Si tu workflow pasa pero la aplicación completa falla localmente con Docker, ¿significa que Actions “no sirve”? Explica qué está verificando y qué no. 
No significa que no sirva, significa que Actions no arregla nada , solo verifica lo que ya esta desarrollado . En este caso, Actions solo está comprobando la sintaxis y las pruebas unitarias de Python. No está levantando Docker, ni base de datos, ni contenedores  porque el equipo decide no automatizar pruebas tan pesadas en cada push por temas de tiempo. 

8. Propón tres checks para tu variante de RapidGo. Para cada uno explica qué error concreto evitaría. 
Check 1: Validar umbral crítico de demanda 
Que probraria: Que el sistema identifique correctamente cuando se superan los 50ped/min y dispare la alerta de nivel “CRITICAL”.
Error que evitara: Evitaria que un error de código clasifique por accidente un pido crítico como “NORMAL” , lo que causaría que no se active la tarifa y que el sistema colapse por falta de repartidores. 

Check 2: Validar Acumulaciones de Órdenes sin asignar 
Que probraria:Comprobar que si se acymulan > 80 pedidos en estado CREADO durando > 10 min, se active la ALERTA_ZONA_SIN_CAPACIDAD
Error que evitaría: Evitaría un error lógico que permita que los pedidos superen el tiempo límite de espera sin que se dispare la pausa preventiva de admisión de nuevos pedidos.  

Check 3: Validar división por cero rendimiento  
Que probaría:Asegurarse de que el cálculo del “Rendimiento” para el KPI 1 no falle si por algún motivo la ventana de tiempo o los pedidos son cero. 
Error que evitaba: Evitaría que un error matemático o una excepción tumbe toda la plataforma o detenga el procesamiento en spark. 

9. ¿Cuál de esos checks debería implementarse primero y por qué? 
Deberíamos implementar primero el check 1 por que según nuestro caso de estudio el riesgo principal es la saturación y el deficit de flota debido a picos masivos de pedidos. Si el sistema falla en detectar cuando se supera el umbral de 50 ped/min , no podra activar la tarifa dinámica para frenar la demanda ni podrá ofrecer incentivos a los repartidores. 

10. ¿Qué prueba sería demasiado costosa o frágil para ejecutar en cada push y cómo la valorarías entonces? 
Levantar un clúster completo de spark y enviar cientos de eventos simulando pedidos por minuto y calcular los porcentajes de particiones del KPI 2 o la segmentación horaria del KPI3 en tiempo real sería demasiado costoso. 
Porque esto requeriría mucha memoria, tiempo y levantaría la infraestructura para probar una simple línea de código, retrasando el trabajo de los integrantes del equipo. 
Lo validará haciendo pruebas muy simples con datos inventados. En lugar de encender todos los programas pesados de datos (como Kafka o Spark), solo le pasaría números fijos a la fórmula (por ejemplo, ver si calcula bien el porcentaje de 20 pedidos sobre un total de 100) para comprobar si la matemática funciona bien por sí sola. 


