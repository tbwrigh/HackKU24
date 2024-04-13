<script lang="ts">
    import type { PageData } from './$types';
    import { onMount } from 'svelte';

    import type { Patient } from '$lib/types';
  
    const backendUrl = import.meta.env.VITE_BACKEND_URL;

    export let data: PageData;

    let patient: Patient;

    onMount(async () => {
        console.log(data);
        const res = await fetch(`${backendUrl}/patients/${data.slug}`);
        patient = await res.json();
    });
    
  </script>

    <h1>{patient.name}'s Profile</h1>



  