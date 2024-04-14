/** @type {import('tailwindcss').Config}*/
const config = {
  darkMode: 'class',
  content: ['./src/**/*.{html,js,svelte,ts}', './node_modules/flowbite-svelte/**/*.{html,js,svelte,ts}'],
  plugins: [require('flowbite/plugin')],

  theme: {
    extend: {},
  },

};

module.exports = config;
