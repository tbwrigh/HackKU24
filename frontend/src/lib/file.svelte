<script lang="ts">
  import { onMount } from 'svelte';

  const backendUrl = import.meta.env.VITE_BACKEND_URL;

  export let patient_id;
  export let filename;

  let src;

  onMount(async () => {
    try {
      const response = await fetch(`${backendUrl}/patient/${patient_id}/download/${filename}`);
      src = URL.createObjectURL(await response.blob());
    } catch (error) {
      console.error('Error:', error);
    }
  });
</script>

<img draggable="false" {src} alt={filename} class="object-scale-down min-w-min max-h-72" />
