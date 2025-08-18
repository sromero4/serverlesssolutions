require('dotenv').config();
const { Nuxt, Builder } = require('nuxt');
const express = require('express');
const compression = require('compression');


const app = express();
app.use(compression()); // Habilita la compresión Gzip


// Configuración de Nuxt.js
const config = require('./nuxt.config.js');
config.dev = !(process.env.NODE_ENV === 'production');


async function start() {
 const nuxt = new Nuxt(config);


 // Construye la aplicación Nuxt.js en el entorno de desarrollo
 if (config.dev) {
   const builder = new Builder(nuxt);
   await builder.build();
 }


 // Agrega el middleware de Nuxt.js al servidor
 app.use(nuxt.render);


 // Inicia el servidor
 console.log("Puerto de escucha....")
 console.log(process.env.PORT_FRONTEND)
 app.listen(process.env.PORT_FRONTEND);
 console.log('Servidor de desarrollo en ejecución...');
}


start();