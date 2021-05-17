# Tarea5_NT
Tarea 5 de Nuevas Tecnologías

Primero se creó el repositorio. <br>
Después se seleccionó la carpeta con los documentos a subir al repositorio y se abrió en Git Bash. <br>

<img src="img1.jpeg"> Aquí se pueden ver los primeros comandos que se ingresaron para pasar todo el proyecto al repositorio. </img>

Comandos:<br>
>> git init <br>
>> git add --all <br>
>> git commit -m "first commtit" <br>
>> git remote add origin https://github.com/melissalunam/Tarea5_NT.git <br>
>> git push -u origin master

Luego, se creó el segundo branch con el siguiente comando: <br>
>> git checkout -b branch2

<img src="img2.jpeg"></img>

Se hizo cambios en la carpeta del proyecto y se subió en el segundo branch con los siguientes comandos: <br>
>> git add . <br>
>> git commit -m "aquí se hizo un cambio en branch2" <br>
>> git push --set-upstream origin branch2 <br>

Después de esto, ya se veía reflejado el cambio en el repositorio. <br>
Para hacer un merge, primero se cambió de branch (de branch2 a master) con el siguiente comando: <br>
>> git checkout master <br>

<img src="img3.jpeg"></img>

Para el merge, se utilizó el siguiente comando: <br>
>> git merge branch2 <br>

Y, por último, para que se viera reflejado en el repositorio se hizo un push: <br>
>> git push
