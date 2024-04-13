import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	preview: {
		port: 8080,
		strictPort: true,
		host: "0.0.0.0",
	}
});
