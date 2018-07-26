# ¿ Porque python ?

El primer lenguaje que conocí fue **JavaScript**, otro excelente lenguaje al menos desde mi punto de vista que llegue a la programación desde tierras lejanas como el Diseño web que es otro cuento totalmente distinto es un mundo de colores, formas y experiencia de usuario pero cuando quieres dotar a tus paginas web de funcionalidades interesantes aprendes a las malas que tendrás que toparte con la programación en algún momento, te surgiran muchísimas dudas en cuanto a que lenguaje debes aprender para entonces comenzar tu inmenso viaje en el fascinante mundo de la programación.

Llegando a este punto estaras bastante confundido debido a la gran cantidad de lenguajes disponibles para programar y pues cadadesarrollador tratara de venderte el lenguaje que conoce como el lenguaje ideal. La verdad es que no hay nada escrito en piedra, existe incluso algunas web donde se indica el ranking mundial de uso de lenguajes de programación, en esta web [TIOBE](https://es.statista.com/estadisticas/576927/indice-tiobe-popularidad-de-los-lenguajes-de-programacion/) puedes ver que python esta en los primeros lugares, ydiráss vaya pero no es el numero uno. Pues la verdad es que python es el lenguaje de scripting mas popular del mundo! y lo es precisamente por las características que lo distinguen, escribir en Python es diferente a escribir código en otro lenguaje.

Pero si no me crees miralo por ti mismo, vamos a recrear un ejemplo simple, pero suficiente para apreciar una de sus principales virtudes **su sintaxis**, vamos a abrir un archivo y leeremos su contenido. Para ello voy a tomar como comparación a otro gran lenguaje **Java** uno de los mas usados en el mundo.

## Como lo hariamos usando Python

```python
f = open("sample.txt")

print(f.read())
```

## Como lo hariamos usando Java

```java
package com.journaldev.files;

import java.awt.Desktop;
import java.io.File;
import java.io.IOException;

public class JavaOpenFile {

    public static void main(String[] args) throws IOException {
        //text file, should be opening in default text editor
        File file = new File("sample.txt");

        //first check if Desktop is supported by Platform or not
        if(!Desktop.isDesktopSupported()){
            System.out.println("Desktop is not supported");
            return;
        }

        Desktop desktop = Desktop.getDesktop();
        if(file.exists()) desktop.open(file);

        //let's try to open PDF file
        file = new File("sample.txt");
        if(file.exists()) desktop.open(file);
    }

}
```

Como puedes ver necesitas menos lineas de codigo en Python, su sintaxis es simple, es facil de comprender y tiene una gran comunidad desarrolladores comprometidos con el proyecto.

## ¿ Quien debe aprender a programar en python ?

Sin temor a equivocarme python es para ti, no importa si estas inicinado en el mundo de la programacion o si ya eres un gran programador en otro lenguaje, python es un lenguaje con una curva de aprendizaje extermadamente corta, gracias a su simplicidad por ende si ya eres un gran programador en otro lenguaje aprender las mejores practicas en python te llevara menos de lo que estas pensando y podras ponerlas en practica en tu vida profesional, python incrementara tu productividad y tu codigo ahora sera codigo limpio y maravilloso!

## ¿ En que ambitos es ideal python ?

Python es un lenguaje multiparadigma, flexible y eficiente 100% pero es muy usuado en:

- Desarrollo web
- Ciencia de datos
- Inteligencia artifical
- Hacking

En definitiva python es un gran lenguaje y puedes hacer cualquier cosa con el.

## ¿ Que encontraras en este repositorio de python ?

- Trucos
- Cargas utiles
- recursos
- Tutoriales

## Un ultimo consejo

No puedo obligarte a programar en python pero puedo brindarte los recursos para adentrarte en este maravilloso lenguaje de programacion. Esta Comprobado que quienes desarrollan en este tipo de lenguajes no promovidos en las universidades son programadores mas comprometidos y apasionado por lo que hacen, el simple hecho de que lo aprendas por tu cuenta demuestra tu gran interes en convertirte en un profesional.
