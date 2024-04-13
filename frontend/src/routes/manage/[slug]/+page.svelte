<script lang="ts">
    import type { PageData } from './$types';
    import { onMount } from 'svelte';

    import { Button, Modal, Label } from 'flowbite-svelte';

    import type { Patient } from '$lib/types';
  
    const backendUrl = import.meta.env.VITE_BACKEND_URL;

    export let data: PageData;

    let patient: Patient = {
        name: "",
        id: "",
        id_string: "",
    };

    onMount(async () => {
        console.log(data);
        console.log(data.slug);
        console.log(`${backendUrl}/patients/${data.slug}`);
        const res = await fetch(`${backendUrl}/patient/${data.slug}`);
        patient = await res.json();
    });

    let addModal = false;
    
  </script>

    <h1>{patient.name}'s Profile</h1>

<Modal bind:open={addModal} size="md" autoclose={false} class="w-full">

</Modal>