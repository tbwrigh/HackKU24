<script lang="ts">
    import { onMount } from 'svelte';
    import { Button } from 'flowbite-svelte'; // Import Flowbite components
    import { TrashBinOutline } from 'flowbite-svelte-icons';

    const backendUrl = import.meta.env.VITE_BACKEND_URL;

    export let id: string; 
    export let deleteCallback: any;

    let puzzleName = '';
    let puzzleFilename = '';

    onMount(async () => {
        console.log('Puzzles page mounted');

        const res = await fetch(`${backendUrl}/puzzle/${id}`);

        if (res.ok) {
            const data = await res.json();
            puzzleName = data.name;
            puzzleFilename = data.filename;
        } else {
            console.error('Error:', res.statusText);
        }
    });

    async function handleDelete() {
        await fetch(`${backendUrl}/puzzle/${id}`, {
            method: 'DELETE',
        }).then((response) => {
            if (response.ok) {
                console.log(`Successfully deleted item with ID: ${id}`);
                deleteCallback(id);
            } else {
                console.error(`Failed to delete item with ID: ${id}`);
            }
        }).catch((error) => {
            console.error('Error deleting item:', error);
        });
    }
</script>


<div class="flex justify-between items-center border-2 border-white shadow-md p-4 rounded-lg">
    <div class="flex-grow text-white" style="flex-basis: 0%; max-width: 45%;">{puzzleName}</div>
    <div class="flex-grow text-white" style="flex-basis: 0%; max-width: 45%;">{puzzleFilename}</div>  
    <Button class="w-1/10" color="blue" size="xs" on:click={handleDelete}>
      <TrashBinOutline/>
    </Button>
  </div>
