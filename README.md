# Tarea5_NT
Tarea 5 de Nuevas Tecnologías

Primero se creó el repositorio. <br>
Después se seleccionó la carpeta con los documentos a subir al repositorio y se abrió en Git Bash. <br>

![img1](https://user-images.githubusercontent.com/56935771/118576197-aabfe680-b74d-11eb-976a-3af394fe04f4.jpeg)
Aquí se pueden ver los primeros comandos que se ingresaron para pasar todo el proyecto al repositorio.

Comandos:<br>
>> git init <br>
>> git add --all <br>
>> git commit -m "first commtit" <br>
>> git remote add origin https://github.com/melissalunam/Tarea5_NT.git <br>
>> git push -u origin master

Luego, se creó el segundo branch con el siguiente comando: <br>
>> git checkout -b branch2

![img2](https://user-images.githubusercontent.com/56935771/118576239-bf9c7a00-b74d-11eb-96b4-d42d62b72870.jpeg)

Se hizo cambios en la carpeta del proyecto y se subió en el segundo branch con los siguientes comandos: <br>
>> git add . <br>
>> git commit -m "aquí se hizo un cambio en branch2" <br>
>> git push --set-upstream origin branch2 <br>

Después de esto, ya se veía reflejado el cambio en el repositorio. <br>
Para hacer un merge, primero se cambió de branch (de branch2 a master) con el siguiente comando: <br>
>> git checkout master <br>

![img3](https://user-images.githubusercontent.com/56935771/118576253-c75c1e80-b74d-11eb-88b8-9206289d5c68.jpeg)

Para el merge, se utilizó el siguiente comando: <br>
>> git merge branch2 <br>

Y, por último, para que se viera reflejado en el repositorio se hizo un push: <br>
>> git push
