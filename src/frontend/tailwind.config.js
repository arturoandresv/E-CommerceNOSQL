/** @type {import('tailwindcss').Config} */
export default {
  darkMode: "class",
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        "surface-container-high": "#141f38",
        "surface-bright": "#1f2b49",
        "surface-dim": "#060e20",
        "surface-container": "#0f1930",
        "on-surface": "#dee5ff",
        "surface-variant": "#192540",
        "background": "#060e20",
        "primary": "#8eabff",
        "on-surface-variant": "#a3aac4",
        "error": "#ff6e84",
        "tertiary": "#47c4ff",
        "surface": "#060e20",
        "surface-container-low": "#091328",
        "surface-container-highest": "#192540",
        "outline": "#6d758c",
        "outline-variant": "#40485d",
        "secondary-container": "#3c475a",
        "on-primary": "#002970",
        "secondary": "#d8e3fb",
        "on-background": "#dee5ff",
        "primary-container": "#799dff",
        "on-primary-container": "#001e58",
      },
      fontFamily: {
        headline: ["Manrope"],
        body: ["Manrope"],
        label: ["Manrope"]
      }
    },
  },
  plugins: [],
}